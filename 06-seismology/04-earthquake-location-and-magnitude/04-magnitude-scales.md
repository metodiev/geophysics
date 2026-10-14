---
id: 06-04-04
title: "Magnitude Scales: Local, Body, Surface, Duration, Moment"
level: advanced
prereqs: ["06-03-05", "06-03-03", "06-04-01"]
tags: [seismology, magnitude, moment-magnitude, source-spectrum, calibration]
---

# Magnitude Scales: Local, Body, Surface, Duration, Moment

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the far-field displacement spectrum of a self-similar source and
   identify which part of it each magnitude scale samples.
2. **Derive** the two slopes a fixed-band magnitude can have,
   $\mathrm{d}M/\mathrm{d}M_w = 3/2$ on the flat branch and $1/2$ on the
   $f^{-2}$ branch, and explain the transition as a corner-frequency crossing.
3. **Derive** why a duration-based scale has a slope of exactly 1 in the
   self-similar model.
4. **Compute** a band amplitude from a spectrum, convert it to a magnitude with
   a stated calibration, and state the units at every step.
5. **Explain** why an additive constant calibrated at one event cannot be
   compared with a published scale's constant.
6. **State** which magnitude is defined without reference to any frequency band,
   and why that matters when events span many sizes.

## Prerequisites

- [06-03-05 Source Spectra, Corner Frequency and Stress Drop](../03-earthquake-sources/05-source-spectra.md).
- [06-03-03 Moment Tensors, Decomposition and Physical Meaning](../03-earthquake-sources/03-moment-tensors.md) —
  the scalar moment $M_0$ used throughout.
- [01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md) —
  why a reported event also has a location and a time.

## 1. Intuition: a magnitude is a scale, not a size

An earthquake does not have a magnitude any more than a person has a height
measurement. What it has is a source: a rupture of some area, with some average
slip, releasing some energy over some duration. *Magnitude* is a way of
reporting a measurement of that source on a logarithmic scale, and because
different scales measure different parts of the same source, they disagree — not
by accident, but by construction.

Three ideas organise the whole subject.

- **The logarithm is for the observer.** Amplitudes in seismology span more than
  ten orders of magnitude, and the relative precision of a measurement does not
  improve with size. Taking $\log_{10}$ compresses the range and makes the
  uncertainty *additive*: an uncertainty of 0.2 magnitude units means the same
  relative error in amplitude at every size.
- **A narrowband scale samples one frequency.** A body-wave magnitude is built
  from energy near 1 Hz, a surface-wave magnitude from energy near 20 s period,
  a local magnitude from the response peak of a short-period instrument. Each is
  a one-number summary of a spectrum at a fixed place on it.
- **The spectrum slides.** A larger event has the same spectral *shape* but its
  corner frequency moves to lower frequency. So a fixed-band probe moves from
  one branch of the spectrum to another as the event grows, and the scale's
  slope changes. That is the origin of saturation, the subject of lesson
  [05](05-magnitude-saturation.md).

Moment magnitude is different in kind: it is read from the low-frequency plateau
of the spectrum, and the plateau is proportional to the source's moment. It is
therefore band-independent, which is why it is the scale that can be compared
across the full size range.

## 2. Definitions

### 2.1 Moment magnitude

The scalar seismic moment is

$$
M_0 = \mu\,\bar{D}\,A \qquad (\mathrm{N\,m}),
$$

where $\mu$ is the rigidity, $\bar{D}$ the average slip and $A$ the rupture area.
Moment magnitude is defined from it by

$$
M_w = \frac{2}{3}\left(\log_{10} M_0 - 9.1\right) ,
\qquad M_0 \ \text{in} \ \mathrm{N\,m} .
$$

The constant 9.1 is the SI form of the definition; it makes $M_w$ dimensionless.
The factor $2/3$ is chosen so that $M_w$ agrees with older magnitude scales over
the range where they are not saturated, and the logarithm is taken of a moment,
which is a physical quantity with units — a point worth stating because "the log
of a dimensioned quantity" only makes sense once the unit (N m) is fixed.

### 2.2 The log-amplitude form of the other scales

Every other scale in this lesson has the structure

$$
M = \log_{10} A + f(\Delta, h) + c_{\text{station}} ,
$$

in which $A$ is a measured ground amplitude in $\mathrm{\mu m}$ (or mm),
$f(\Delta, h)$ is a distance and depth correction, and $c_{\text{station}}$ is an
instrument/station constant. The **correction term is the scale**: the two
people who disagree about $f$ are using different scales even if they both call
the result "magnitude".

The scales considered here, written as narrowband probes at frequencies
$f_{\text{band}}$:

| scale | band centre | nominal period | what it samples |
|---|---|---|---|
| $m_l$ | 1.25 Hz | 0.8 s | the short-period part of the S coda, near the Wood-Anderson response peak |
| $m_b$ | 1.0 Hz | 1 s | a short-period P phase |
| $M_s$ | 0.05 Hz | 20 s | a long-period surface wave |
| $M_d$ | — | — | the duration of the recorded signal, not a band amplitude |
| $M_w$ | — | — | the low-frequency plateau of the spectrum |

## 3. Derivations

### 3.1 The far-field displacement spectrum

For a point source of moment $M_0$ at distance $R$, the far-field displacement
spectrum in one direction is

$$
\Omega(f) = \frac{M_0\, a(\theta, \phi)}{4\pi \rho \beta^{3} R}\,
S(f) ,
$$

where $a$ is the radiation pattern coefficient, $\rho$ the density, $\beta$ the
shear speed, and $S(f)$ the normalised source spectrum. Everything ahead of
$S(f)$ is the **plateau**: the frequency-independent amplitude the source would
have if $S = 1$. In the demo's synthetic model
$\rho = 2700\ \mathrm{kg\,m^{-3}}$, $\beta = 3500\ \mathrm{m\,s^{-1}}$,
$R = 100\ \mathrm{km}$ and $a = \sqrt{\langle a^{2}\rangle} = \sqrt{2/5} = 0.6325$,
giving

$$
\Omega_0 = \frac{M_0\,a}{4\pi\rho\beta^{3}R}
= \frac{M_0 \times 0.6325}{1.4547\times10^{20}}
= 4.348\times10^{-6}\ \mathrm{m\,s}
\quad \text{for } M_0 = 10^{15}\ \mathrm{N\,m}.
$$

The plateau is just proportional to $M_0$: it is the part of the spectrum from
which the moment is read. That is the whole reason $M_w$ does not saturate.

### 3.2 The self-similar source spectrum and the sliding corner

Adopt the one-parameter shape

$$
S(f) = \frac{1}{1 + (f/f_c)^{2}} ,
\qquad
\Omega(f) = \frac{\Omega_0}{1 + (f/f_c)^{2}} ,
$$

which is flat below $f_c$ and falls as $f^{-2}$ above it. **Self-similarity**
means the shape is the same for every event and only $f_c$ moves, with

$$
f_c \propto M_0^{-1/3} ,
$$

the standard consequence of constant stress drop: the source dimension grows as
$L \propto M_0^{1/3}$ while $f_c \propto \beta/L$. The demonstration fixes
$f_c = 0.6\ \mathrm{Hz}$ at $M_0 = 10^{15}\ \mathrm{N\,m}$, so
$f_c = 0.6\,(M_0/10^{15})^{-1/3}\ \mathrm{Hz}$; a $M_0 = 10^{22}\ \mathrm{N\,m}$
event therefore has $f_c = 0.0028\ \mathrm{Hz}$, and a
$M_0 = 10^{12}\ \mathrm{N\,m}$ event has $6.0\ \mathrm{Hz}$. The corner slides by
more than three decades across the range of the demonstration's family.

### 3.3 The two slopes of a fixed-band scale

Let $A$ be the spectral amplitude at a fixed band centre $f_b$, and let
$M = \log_{10} A + \text{const}$. Two regimes.

**Flat branch** ($f_b \ll f_c$). Then $A \approx \Omega_0 \propto M_0$, so

$$
M = \log_{10} M_0 + \text{const}
= \tfrac{3}{2} M_w + \text{const}
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}M}{\mathrm{d}M_w} = \frac{3}{2} .
$$

**$f^{-2}$ branch** ($f_b \gg f_c$). Then
$A \approx \Omega_0 (f_c/f_b)^{2} \propto M_0 f_c^{2} \propto M_0^{1/3}$, so

$$
M = \tfrac{1}{3}\log_{10} M_0 + \text{const}
= \tfrac{1}{2}M_w + \text{const}
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}M}{\mathrm{d}M_w} = \frac{1}{2} .
$$

The two conversions used above are worth stating once:
$\log_{10} M_0 = \tfrac{3}{2} M_w + 9.1$ from the definition of $M_w$, so a
factor $\alpha$ in $\log_{10} M_0$ becomes $\tfrac{2}{3}\alpha$ in $M_w$.

The **transition** happens when $f_c$ passes through $f_b$, i.e. at the size
where the corner frequency equals the band centre. That size is the scale's
saturation onset, and it is a property of the instrument, not of the earthquake.

### 3.4 The duration scale

A duration scale uses the length of the signal instead of an amplitude. The
natural duration is the source duration $\tau \propto 1/f_c$, so
$\tau \propto M_0^{1/3}$ and, with the conventional coefficient 2,

$$
M_d = 2\log_{10}\!\left(\frac{\tau_d}{1\ \mathrm{s}}\right) + c
= \tfrac{2}{3}\log_{10} M_0 + c'
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}M_d}{\mathrm{d}M_w} = 1 .
$$

A duration scale therefore tracks $M_w$ in a self-similar family, and it does not
saturate — because it measures the *whole* source rather than a fixed-frequency
slice of it. Whether it tracks $M_w$ in reality depends on whether the recorded
duration is controlled by the source or by path and site effects, which is a
separate measurement.

## 4. Worked examples

All numbers are printed by `code/magnitude_scales_demo.py`. The model constants
are $\rho = 2700\ \mathrm{kg\,m^{-3}}$, $\beta = 3500\ \mathrm{m\,s^{-1}}$,
$R = 100\ \mathrm{km}$, path $Q = 400$ so $t^{*} = R/\beta = 28.57\ \mathrm{s}$,
$a = 0.6325$, $f_c = 0.6\ \mathrm{Hz}$ at $M_0 = 10^{15}\ \mathrm{N\,m}$, and
bands at 1.25, 1.00 and 0.05 Hz. The attenuation factor applied to an amplitude
is $\exp(-\pi f t^{*}/Q)$.

### Example 1 — moment, corner frequency and plateau

| $M_0$ (N m) | $M_w$ | $f_c$ (Hz) | $\Omega_0$ (m s) | $\tau = 1/(2\pi f_c)$ (s) |
|---|---|---|---|---|
| $10^{12}$ | 1.93 | 6.0000 | $4.348\times10^{-9}$ | 0.027 |
| $10^{15}$ | 3.93 | 0.6000 | $4.348\times10^{-6}$ | 0.265 |
| $10^{18}$ | 5.93 | 0.0600 | $4.348\times10^{-3}$ | 2.653 |
| $10^{22}$ | 8.60 | 0.0028 | $4.348\times10^{1}$ | 57.148 |

Hand check of the first row's $M_w$:
$M_w = \tfrac{2}{3}(12 - 9.1) = \tfrac{2}{3}(2.9) = 1.933$. Hand check of the
plateau: $4\pi\rho\beta^{3}R = 1.4547\times10^{20}$, so
$\Omega_0 = 10^{15}\times0.6325/1.4547\times10^{20} = 4.348\times10^{-6}$. Hand
check of the last row's corner frequency: the $10^{22}$ event is a factor
$10^{7}$ above the reference, so

$$
f_c = 0.6 \times (10^{7})^{-1/3}
= 0.6 \times 10^{-2.333}
= 0.6 \times 4.642\times10^{-3}
= 2.785\times10^{-3}\ \mathrm{Hz},
$$

which is the printed $0.0028\ \mathrm{Hz}$. The corner slides by more than three
decades across this family while the plateau changes by a factor of $10^{10}$.

The demonstration also checks the pulse against the spectrum: integrating the
time-domain displacement pulse of the $10^{16}\ \mathrm{N\,m}$ event gives
$4.344854\times10^{-5}\ \mathrm{m\,s}$ against a closed-form plateau of
$4.347627\times10^{-5}\ \mathrm{m\,s}$, a relative difference of
$6.38\times10^{-4}$ — the discretisation of a numerical integral, which is what
makes a duration scale and an amplitude scale comparable at all.

### Example 2 — one band amplitude, by hand

Take the $M_w = 5.93$ event ($f_c = 0.06\ \mathrm{Hz}$, $\Omega_0 = 4.348\times10^{-3}\ \mathrm{m\,s}$)
and the 1 Hz body-wave band:

$$
A = \frac{\Omega_0}{1 + (f/f_c)^{2}}\,e^{-\pi f t^{*}/Q}
= \frac{4.348\times10^{-3}}{1 + 277.8}\times e^{-0.2244}
= 1.5595\times10^{-5} \times 0.7990 = 1.246\times10^{-5}\ \mathrm{m}
= 12.46\ \mathrm{\mu m},
$$

which is the $1.246\times10^{1}\ \mathrm{\mu m}$ printed for that event — a
factor of 278 below the plateau, so the band is firmly on the $f^{-2}$ branch.

### Example 3 — the classification event, and the separation away from it

Every band-limited scale is calibrated **inside** the demo to equal $M_w$ at the
single reference event $M_0 = 10^{15}\ \mathrm{N\,m}$: the constants are
$c_{m_l} = +4.1445$, $c_{m_b} = +3.9698$, $c_{M_s} = +3.3030$, all with the
amplitude in micrometres. These are teaching constants internal to this synthetic
model. A real catalogue scale carries an empirical distance correction and a
station calibration fitted over a range of distances and stations; none of that
is imported here, and the numbers above must never be compared with a published
scale's constants.

At the reference event all five scales read 3.93. At $M_w = 8.60$ they read

| scale | value at $M_w = 8.60$ | difference from $M_w$ |
|---|---|---|
| $m_l$ | 6.36 | $-2.24$ |
| $m_b$ | 6.40 | $-2.20$ |
| $M_s$ | 8.43 | $-0.17$ |
| $M_d$ | 8.60 | $+0.00$ |

A 2.2 magnitude-unit difference is a factor of
$10^{1.5\times2.2} = 2.0\times10^{3}$ in moment — the same earthquake, reported
three thousand times smaller or larger depending on the scale. The sign of the
difference is not a universal law either: it follows from where each band sits
relative to the sliding corner.

### Example 4 — measured slopes, and the arithmetic that predicts them

| scale | slope, first third | middle third | last third |
|---|---|---|---|
| $m_l$ | 1.299 | 0.564 | 0.500 |
| $m_b$ | 1.356 | 0.595 | 0.501 |
| $M_s$ | 1.500 | 1.457 | 0.632 |
| $M_d$ | 1.000 | 1.000 | 1.000 |
| $M_w$ | 1.000 | 1.000 | 1.000 |

These are exactly the numbers Section 3.3 predicts. Hand check with two printed
values: $m_l$ goes from 1.64 at $M_w = 1.93$ to 3.37 at $M_w = 3.27$, so

$$
\frac{\Delta m_l}{\Delta M_w} = \frac{3.37 - 1.64}{3.27 - 1.93}
= \frac{1.73}{1.34} = 1.29 ,
$$

against the least-squares value of 1.299 for the same third. Over this range the
1.25 Hz band is still below the corner frequencies of the events concerned
($f_c = 6.0$ to $1.29$ Hz), so the slope tends to the flat-branch value of 1.5;
by the last third the same band is far above the corner
($f_c = 0.06$ to $0.0028$ Hz) and the slope is the $f^{-2}$ value of 0.5. The
$M_s$ band at 0.05 Hz does the same dance later, because it only passes the
corner of the largest events in the family, and the duration scale never leaves
1.000.

## 5. Assumptions and regime of validity

1. **Self-similarity.** The relation $f_c \propto M_0^{-1/3}$ is an assumption
   of constant stress drop. Real stress drops vary by at least a factor of ten
   between events, which is enough to break the correspondence between $M_w$ and
   any corner-frequency-derived quantity.
2. **Point source.** A finite fault has a duration set by rupture propagation as
   well as by its final size, so the spectrum of a great earthquake is not the
   simple one-corner shape used here; this is the main limit of the model, and
   lesson [05](05-magnitude-saturation.md) states what it costs.
3. **Band-centre sampling.** A real narrowband scale integrates a response over a
   band and takes a peak or an rms, not an amplitude at one frequency. The
   simplification changes the numbers, not the slopes.
4. **Fixed distance and a known path.** The attenuation factor uses a stated $Q$
   and $t^{*}$; with a different path the constants change, which is exactly why
   a real scale needs a distance correction.
5. **No radiation-pattern or directivity correction.** Substituting the average
   $a = 0.6325$ for a station-specific coefficient introduces an error of order
   20 to 30 per cent in a single-station moment.
6. **Amplitudes are in micrometres.** Magnitudes are dimensionless once the
   amplitude unit is fixed; changing the unit shifts every value by a constant.

## 6. The demonstration

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_scales_demo.py
```

It builds the 11-event family, prints the spectrum parameters (Example 1), the
band amplitudes (Example 2), the five scales with their difference from $M_w$
(Example 3), and the slopes by thirds (Example 4), and it checks the time-domain
pulse against the spectral plateau.

Exercises:
[`exercises/04-magnitude-scales-exercises.md`](exercises/04-magnitude-scales-exercises.md)
and
[`exercises/04-magnitude-scales-solutions.md`](exercises/04-magnitude-scales-solutions.md).

> All models and data in this module are **SYNTHETIC**. The source family, the
> path, the bands and every calibration constant are teaching values. The only
> imported physics is the standard definition of moment magnitude; no published
> magnitude correction is reproduced or approximated.

## Mastery checkpoint

Without notes:

1. Derive $\Omega_0 \propto M_0$ from the far-field displacement expression.
2. Derive the slopes $3/2$ and $1/2$ for a fixed-band scale on the two branches.
3. Compute $f_c$ for $M_0 = 10^{19}\ \mathrm{N\,m}$ given
   $f_c = 0.6\ \mathrm{Hz}$ at $10^{15}\ \mathrm{N\,m}$.
4. Explain why $M_w$ cannot saturate in this model, in one sentence about the
   part of the spectrum it uses.
5. State one way in which a real $m_b$ differs from the synthetic one above, and
   why that difference changes the *constant* but not the *slope*.

## Common pitfalls

1. **Comparing magnitudes from different scales.** They measure different parts
   of the source and disagree by design.
2. **Treating a magnitude as a physical quantity.** It is a scale reading; the
   physical quantities are $M_0$, the corner frequency and the radiated energy.
3. **Forgetting the unit of amplitude.** A magnitude is defined only once the
   amplitude unit (µm, mm, m) is fixed.
4. **Comparing a synthetic calibration constant with a published one.** Real
   constants absorb distance and station corrections that are absent here.
5. **Assuming a slope of 1 everywhere.** A fixed-band scale has a slope of
   $3/2$ at small sizes and $1/2$ at large ones in this model.
6. **Reading saturation as an absence of growth.** A slope of $1/2$ still grows;
   it grows at half the rate, and the energy keeps growing at the full rate.

## Related modules

- [05 Magnitude Saturation and Why Moment Magnitude Is Preferred](05-magnitude-saturation.md) —
  what the slopes above cost a catalogue.
- [06 Energy Release, Moment Calculations and Scaling](06-energy-moment-calculations.md) —
  moment and energy from the same spectrum.
- [06-03-05 Source Spectra, Corner Frequency and Stress Drop](../03-earthquake-sources/05-source-spectra.md).
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  what happens to a hazard calculation when scales are mixed.
