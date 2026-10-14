---
id: 20-06-03
title: "Seismic Array Design and Resolution"
level: research
prereqs: ["20-06-02", "20-02-03"]
tags: [signal-processing, array-processing, array-design, resolution, sidelobes, tapering, spatial-aliasing]
---

# Seismic Array Design and Resolution

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the array transfer function of a uniform linear array and **state**
   the roles of aperture, spacing and weighting separately.
2. **Measure** the peak sidelobe of a uniformly weighted array and **compare** it
   with the standard $-13.26\ \mathrm{dB}$.
3. **Measure** the resolution-versus-contrast trade of at least three tapers and
   **choose** a taper from a stated requirement.
4. **Predict** the grating-lobe onset from the aliasing-free range $1/(2fd)$ and
   **verify** it by measurement.
5. **Explain** what an irregular layout buys and what it costs, and **report** the
   ensemble rather than a single realisation.
6. **Show** that the half-power width scales as $1/(fL)$ and **design** an array
   for a stated slowness resolution.

All models and data in this module are **SYNTHETIC**. The arrays and responses
are computed by the accompanying demonstration; no real array is used and no
number is quoted from a published measurement.

## Prerequisites

- [20-06-02 Beamforming, Slowness Estimation and f-k Analysis](02-beamforming.md) —
  the beamformer, the array response, the grating-lobe position $1/(fd)$ and the
  array gain.
- [20-02-03 Window Functions and Spectral Leakage Control](../02-fourier-and-spectral-analysis/03-windowing-advanced.md) —
  the taper theory reused here with space in place of time.
- [06-02-02 Snell's Law and Layered Media](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  why a real wave arrives with the slownesses an array scans.

## 1. Intuition: three knobs, three effects

Every array-design question is a negotiation among exactly three quantities.

- **Aperture $L$** — the overall size. It sets the **resolution**: how close two
  slownesses can be and still be separated.
- **Spacing $d$** — the typical distance between neighbouring sensors. It sets
  the **aliasing-free range**: the band of slownesses that can be represented
  without ambiguity.
- **Weighting $w_j$** — how much each sensor counts. It sets the **sidelobe
  level**: how much a wave at the wrong slowness leaks into the estimate.

The three are almost independent, and the classical designs are ways of
trading one against another. A uniform array gives the narrowest main lobe for
its aperture but sidelobes only 13 dB down; tapering suppresses the sidelobes and
widens the main lobe; increasing the aperture sharpens the main lobe but, if the
sensors are left at the old spacing, changes nothing about aliasing.

## 2. Precise definitions

### 2.1 Array transfer function

For $N$ sensors at positions $x_j$ with weights $w_j$ normalised to
$\sum_j w_j = 1$, the power response to a monochromatic plane wave of frequency
$f$ and slowness difference $\Delta s = s - s_0$ is

$$B(\Delta s) = \left|\sum_{j=1}^{N} w_j\, e^{i2\pi f\,\Delta s\, x_j}\right|^{2}.$$

This is the object of the lesson. It is the spatial analogue of a window's
frequency response; every term has a direct counterpart in
[20-02-03](../02-fourier-and-spectral-analysis/03-windowing-advanced.md).

### 2.2 The four design numbers

| quantity | definition | what it controls |
|---|---|---|
| aperture | $L = \max_j x_j - \min_j x_j$ | main-lobe width, $\propto 1/(fL)$ |
| spacing | $d$, for a uniform layout | grating lobes at $m/(fd)$ |
| peak sidelobe | $\max B$ outside the main lobe | leakage from wrong slownesses |
| array gain | $N$ (incoherent noise) | SNR improvement |

### 2.3 Aliasing-free range and redundancy

The **aliasing-free range** is $|s - s_0| < 1/(2fd)$, from
[20-06-02 §3.3](02-beamforming.md). The **redundancy** of a layout is the number
of times each sensor-pair separation occurs: a uniform array is highly redundant
(its separations repeat), which is exactly why its pattern has the clean
periodic sidelobe structure and the discrete grating lobes.

## 3. Derivations

### 3.1 Where the $-13.26\ \mathrm{dB}$ sidelobe comes from

For a uniform linear array the response is
$B(u) = \frac{1}{N^{2}}\frac{\sin^{2}(Nu\pi)}{\sin^{2}(u\pi)}$ with
$u = f\Delta s d$. For large $N$ the envelope of the sidelobes is
$1/(N^{2}\sin^{2}(u\pi))$, maximised where $|\sin(u\pi)| = 1$ but bounded below
the first null. The first sidelobe of the continuous equivalent,
$\operatorname{sinc}^{2}(u) = \sin^{2}(\pi u)/(\pi u)^{2}$, peaks at
$u \approx 1.4303$ with the value

$$20\log_{10}\left|\frac{\sin(\pi u)}{\pi u}\right|
= -13.26\ \mathrm{dB},$$

the standard uniform-aperture sidelobe level. The demonstration measures
$-13.15\ \mathrm{dB}$ on a 16-sensor array — within $0.11\ \mathrm{dB}$ of the
asymptotic value, the residual being the finite number of sensors and the
discrete slowness grid.

### 3.2 Tapering

Weighting the sensors is *exactly* windowing in space. A Hann taper,

$$w_j = \tfrac{1}{2}\left[1 - \cos\!\left(\frac{2\pi j}{N-1}\right)\right],
\qquad j = 0,\dots,N-1,$$

suppresses the sidelobes at the price of a wider main lobe, because the effective
aperture is reduced (the outer sensors, which set the resolution, are
down-weighted). The demonstration measures:

| weighting | peak sidelobe | half-power width | width relative to uniform |
|---|---|---|---|
| uniform | $-13.15$ dB | $0.00560\ \mathrm{s\,km^{-1}}$ | 1.00 |
| triangular | $-27.05$ dB | $0.00800\ \mathrm{s\,km^{-1}}$ | 1.43 |
| Hann | $-31.50$ dB | $0.00980\ \mathrm{s\,km^{-1}}$ | 1.75 |
| Hamming | $-39.37$ dB | $0.00860\ \mathrm{s\,km^{-1}}$ | 1.54 |

Two standard asymptotic values to compare against: Hann's peak sidelobe is
$-31.5\ \mathrm{dB}$ (measured $-31.50$, an exact match) and Hamming's is
$-42.7\ \mathrm{dB}$. The measured Hamming value, $-39.37\ \mathrm{dB}$, is
$3.3\ \mathrm{dB}$ short of the asymptote: at 16 sensors the far sidelobes have
not yet decayed to their asymptotic level. **The asymptotic window numbers are
limits, not promises, at small $N$.**

### 3.3 Spacing and the aliasing-free range

Because the pattern is periodic in $\Delta s$ with period $1/(fd)$
([20-06-02 §3.3](02-beamforming.md)), the aliasing-free range narrows as the
spacing grows. Fixing the aperture at 30 km and varying $d$:

| spacing $d$ | sensors | $1/(fd)$ | aliasing-free $1/(2fd)$ | measured grating offsets |
|---|---|---|---|---|
| 0.5 km | 61 | 0.4000 | 0.2000 | none above $-14$ dB |
| 1.0 km | 31 | 0.2000 | 0.1000 | none above $-14$ dB |
| 2.0 km | 16 | 0.1000 | 0.0500 | none above $-14$ dB |
| 4.0 km | 8 | 0.0500 | 0.0250 | $-0.050$, $+0.050$ |
| 8.0 km | 4 | 0.0250 | 0.0125 | $-0.050$, $0.000$, $+0.025$, $+0.050$ |

The onset is exactly where the table says: a grating lobe appears once the
inter-sensor phase shift $2\pi f d\, \Delta s$ can reach $2\pi$, i.e.
$\Delta s \ge 1/(fd)$, and the slowness it aliases to is $1/(2fd)$ away — the
Nyquist limit. **The same aperture at four spacings has the same resolution and
four different aliasing ranges**, which is the clearest demonstration that the
two knobs are separate.

### 3.4 Aperture and resolution

With 16 sensors at every aperture, the measured half-power width and its product
with $fL$:

| aperture $L$ | half-power width | $1/(fL)$ | width $\times fL$ |
|---|---|---|---|
| 8 km | $0.02080\ \mathrm{s\,km^{-1}}$ | 0.02500 | 0.832 |
| 16 km | $0.01040$ | 0.01250 | 0.832 |
| 24 km | $0.00700$ | 0.00833 | 0.840 |
| 32 km | $0.00520$ | 0.00625 | 0.832 |

The last column is dimensionless and constant to within 1%: the half-power width
is $0.83/(fL)$ for this layout, so the scaling is confirmed and the constant is
specific to the weighting (a uniform array; a Hann taper would give about
$1.46/(fL)$). **Resolution is bought with aperture and with frequency, never with
more sensors at the same aperture.** The derivation of the constant in the
continuous limit gives $0.886$ for a uniform aperture; the measured $0.832$
reflects the finite $N$ and the discrete slowness grid.

## 4. Worked example: irregular layouts

Replacing the uniform line by 16 sensors placed randomly in the same 30-km
aperture (with a 1-km minimum spacing) removes the periodicity that creates
grating lobes, because no two sensor separations repeat. Over 50 realisations:

| layout | peak sidelobe | half-power width | layouts with a grating lobe |
|---|---|---|---|
| uniform linear | $-13.15$ dB | $0.00560\ \mathrm{s\,km^{-1}}$ | — |
| random, 16 in 30 km | $-10.86 \pm 1.68$ dB | $0.00601 \pm 0.00035$ | 1 of 50 |

The random layouts have a **higher** average sidelobe floor ($-10.9$ dB against
$-13.2$ dB) and a slightly wider main lobe, and one layout in fifty still
produced a discrete grating lobe above 20% by chance. The scatter is
$\pm1.68\ \mathrm{dB}$, comparable to the difference from the uniform array:
**a single irregular layout can be lucky or unlucky, and reporting one without
its ensemble is not a measurement.** Irregular designs are chosen when a
grating lobe is fatal and a raised sidelobe floor is tolerable — for example when
a strong coherent source sits at an unknown slowness.

## 5. Worked example: choosing a design

**Requirement.** Resolve slownesses $0.01\ \mathrm{s\,km^{-1}}$ apart at 2 Hz,
with no grating lobe within $|s| < 0.2\ \mathrm{s\,km^{-1}}$, and keep the peak
sidelobe below $-25\ \mathrm{dB}$.

1. Resolution: $\Delta s = 1/(fL) \Rightarrow L = 1/(f\Delta s) =
   1/(2 \times 0.01) = 50\ \mathrm{km}$.
2. Aliasing: $1/(2fd) > 0.2 \Rightarrow d < 1/(2 \times 2 \times 0.2) =
   1.25\ \mathrm{km}$. With $L = 50$ km this needs $N \gtrsim 50/1.25 = 40$
   sensors.
3. Sidelobes: a uniform array gives $-13$ dB, so a taper is needed. From the
   table, a triangular taper reaches $-27$ dB at a $1.43\times$ resolution cost.
   Buying that back means $L \approx 72$ km, hence $N \gtrsim 58$ sensors.

**Answer.** About 60 sensors over 72 km, triangular taper. If the hardware is
capped at 30 sensors, the honest response is that the design cannot meet all
three requirements: state which one is being relaxed (usually the sidelobe level,
which is the least damaging) and by how much.

## 6. Assumptions and regime of validity

1. **A plane wave.** For a source close to the array the wavefront curvature must
   be modelled; the flat beampattern then no longer describes the response.
2. **Known positions.** Position errors of a fraction of a wavelength broaden the
   beam and raise the sidelobes, mimicking a bad design. Field surveys must
   survey the sensor positions, not assume them.
3. **A single frequency for the design.** Real signals are broadband, and the
   response at each frequency has a different width and a different aliasing
   onset. The design must be checked over the band, at the *highest* frequency
   for aliasing and the *lowest* for resolution.
4. **Identical sensors.** Gain or phase differences between sensors act like an
   uncontrolled weighting and can raise the sidelobes above the design value.
5. **Incoherent noise for the gain.** $N$-fold gain assumes independence between
   sensors.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| aperture | $L$ | km | |
| spacing | $d$ | km | |
| frequency | $f$ | Hz | |
| slowness resolution | $1/(fL)$ | $\mathrm{s\,km^{-1}}$ | Hz$^{-1}$ km$^{-1}$ |
| product | width $\times fL$ | dimensionless | (s/km)(Hz)(km) |
| weights | $w_j$ | dimensionless | normalised to 1 |

The dimensionless product in Section 3.4 is the correct way to compare layouts:
a resolution quoted in $\mathrm{s\,km^{-1}}$ without the frequency and aperture
that produced it is not a measurement.

## 8. Python demonstration

[`code/array_design_demo.py`](./code/array_design_demo.py) computes every number
above:

1. the transfer function, main-lobe width and peak sidelobe of a uniform array;
2. the taper trade-off for four weightings;
3. the grating-lobe onset versus spacing at fixed aperture;
4. the ensemble statistics of 50 random layouts;
5. the half-power width against $1/(fL)$.

```bash
cd 20-signal-processing/06-polarisation-and-array-processing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python array_design_demo.py
```

## 9. Exercises

[`exercises/03-array-design-exercises.md`](./exercises/03-array-design-exercises.md)
and
[`exercises/03-array-design-solutions.md`](./exercises/03-array-design-solutions.md).
The ★★★ problem is a full design under conflicting requirements.

## 10. Mastery checkpoint

1. A 24-sensor array has 2 km spacing and records 3 Hz waves. State the aperture,
   resolution, aliasing-free range and expected sidelobe level.
2. The same array is to be tapered with Hann. State the new resolution and
   sidelobe level, and the number of sensors needed to restore the old
   resolution.
3. A grating lobe appears at a slowness the science case cares about. Which knob
   fixes it, and what does the fix cost?
4. A colleague reports a random layout with $-30$ dB sidelobes. Give two reasons
   to distrust the number.

## 11. Common pitfalls

1. **Adding sensors at the same aperture and expecting better resolution.** It
   improves sidelobes and gain, not resolution.
2. **Quoting one irregular layout.** Report the ensemble mean and scatter.
3. **Using asymptotic window numbers at small $N$.** Hamming's $-42.7\ \mathrm{dB}$
   is not reached at 16 sensors.
4. **Designing at one frequency.** Aliasing is worst at the top of the band and
   resolution at the bottom.
5. **Forgetting position errors.** They raise the sidelobes and broaden the beam
   in the same way a bad weighting does.

## 12. Related lessons

- [20-06-02 Beamforming, Slowness Estimation and f-k Analysis](02-beamforming.md) —
  the response being designed here.
- [04 Back-Projection Imaging of Rupture](04-backprojection.md) — an application
  in which the array resolution is the scientific limit.
- [20-02-03 Window Functions and Spectral Leakage Control](../02-fourier-and-spectral-analysis/03-windowing-advanced.md) —
  the same tapers in the time domain.
- [20-03-06 Multichannel and Array Filtering (f-k, Radon)](../03-digital-filtering/06-multichannel-filtering.md) —
  array responses used to filter rather than to estimate.
- [23-02 Seismic Sensors and Arrays](../../23-field-methods-instruments/README.md) —
  the hardware side of an array deployment.

## 13. Further reading

Titles are given so the works can be located; this repository does not host or
reproduce copyrighted text.

- **Rost & Thomas, "Array seismology: methods and applications", *Reviews of
  Geophysics*, 2002.** Level: research. Array geometries and their response as
  used in seismology.
- **Johnson & Dudgeon, *Array Signal Processing: Concepts and Techniques*,
  Prentice-Hall, 1993.** Level: graduate. The design relations in this lesson,
  in full generality.
- **Harris, "On the use of windows for harmonic analysis with the discrete
  Fourier transform", *Proceedings of the IEEE*, 1978.** Level: research. The
  origin of the $-13.26$, $-31.5$ and $-42.7$ dB numbers used here.
- **Van Veen & Buckley, "Beamforming: a versatile approach to spatial
  filtering", *IEEE ASSP Magazine*, 1988.** Level: graduate. Gain, resolution and
  sidelobe control as a single design problem.

## 14. Self-assessment checklist

- [ ] I can write the array transfer function with weights.
- [ ] I can state which knob controls resolution, aliasing and sidelobes.
- [ ] I can predict the grating-lobe onset and verify it.
- [ ] I can read a taper trade-off table and choose a taper.
- [ ] I can design for a resolution and an aliasing range together.
- [ ] I can report an irregular layout as an ensemble.
