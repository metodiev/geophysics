---
id: 01-10-07
title: "Two-Dimensional Fourier Analysis and Wavenumber Filtering"
level: graduate
prereqs: ["01-10-04", "01-10-05"]
estimated_minutes: 90
tags: [f-k-filtering, wavenumber, dip-filtering, up-down-separation, spatial-aliasing]
---

# Two-Dimensional Fourier Analysis and Wavenumber Filtering

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the 2-D DFT and compute it separably, and verify it against the
   direct double sum.
2. **Explain** why a dipping plane wave occupies a straight line through the
   origin of the $f$–$k_x$ plane, with slope equal to the apparent slowness.
3. **State** the sign convention that fixes which half-plane is which, and show
   why it must be stated rather than assumed.
4. **Design** a dip (fan) filter and measure its leakage, distinguishing exact
   separation of grid-aligned plane waves from the imperfect separation of real
   wave packets.
5. **Perform** up/down separation by quadrant filtering and state what the
   cone around the origin costs.
6. **Quantify** spatial aliasing as a wrap in the $f$–$k_x$ plane and **explain**
   why a hard wavenumber cut requires a spatial taper.

## Prerequisites

[01-10-04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) —
the DFT, its bin layout and its separability;
[01-10-05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
the spatial Nyquist relation and the windowing trade-off, both of which this
lesson applies in two dimensions.

## 1. Intuition: a dipping event is a line, not a wiggle

In the time–offset domain a reflection from a dipping interface is a hyperbola or
a slanted line crossing many traces. Nothing about the display *looks* like a
single object with a single frequency. Transform the same gather in both
variables — time and offset — and the event collapses onto a **line**:

$$k_x = p\,f \qquad\text{(equivalently } f = v\,k_x\text{)},$$

where $p$ is the apparent slowness (s/m) of the event along the receiver line.
The line passes through the origin, and its slope is the slowness.

That is the whole reason f-k (frequency–wavenumber) filtering exists. In the
time–offset domain, "remove the ground roll" means "find a curve and follow it
across 200 traces, deciding at every trace where the wavelet is". In the f-k
domain it means "zero everything above a line". The second is a few lines of
code, it is exact for the geometry it assumes, and it is the standard first tool
of VSP and surface-wave processing.

The price is stated at the outset: every event's line passes through the origin,
so in the neighbourhood of $f = 0$ and $k_x = 0$ all dips are indistinguishable,
and any f-k filter must leave a cone there unmuted. Sections 4–6 quantify that
and the other limitations.

## 2. The two-dimensional transform

### 2.1 Definition

For a grid $g[x, t]$ of $N_x$ traces at spacing $dx$ and $N_t$ samples at
spacing $dt$:

$$G[k_x, k_f] = \sum_{n_x=0}^{N_x-1}\sum_{n_t=0}^{N_t-1}
g[n_x, n_t]\,e^{-2\pi i\left(k_x n_x/N_x + k_f n_t/N_t\right)},$$

with inverse carrying $1/(N_xN_t)$ and the conjugate kernel. The bin spacings are

$$dk_x = \frac{1}{N_x\,dx} = \frac{1}{L}, \qquad
df = \frac{1}{N_t\,dt} = \frac{1}{T},$$

($L$ the array length, $T$ the record length), and the Nyquist wavenumber is
$1/(2\,dx)$. Note the exact parallel with
[01-10-05](./05-windowing-aliasing.md): the transform can only *resolve*
$1/L$ in wavenumber and $1/T$ in frequency, while it can *sample* those axes as
finely as padding allows.

### 2.2 Separability

The kernel factorises, so the 2-D transform can be computed as one 1-D transform
per trace followed by one per frequency — $2N$ 1-D transforms, not $(N_xN_t)^{2}$
operations. The demo verifies this on an 8×8 grid against the direct double sum:
the maximum difference is $5.7\times10^{-14}$.

The order of the two passes does not matter, but *which axis each pass is applied
to* does. Getting it wrong — applying the time transform to the space axis —
produces numbers of plausible magnitude and a completely wrong wavenumber axis.
This is a real failure mode: it is the kind of bug that survives a visual check
because the output still "looks like" an f-k panel.

### 2.3 The grid used throughout this lesson

| quantity | value |
|---|---|
| traces | $N_x = 64$ |
| trace spacing | $dx = 12.5$ m |
| array length | $L = 800$ m |
| samples | $N_t = 256$ |
| sample interval | $dt = 4$ ms |
| record length | $T = 1.024$ s |
| $dk_x$ | 0.00125 cycles/m |
| $df$ | 0.9766 Hz |
| Nyquist wavenumber | 0.04 cycles/m |
| Nyquist frequency | 125 Hz |

## 3. Where an event sits in the f-k plane

### 3.1 The ridge, measured

The demo builds a narrow-band event on the line $t = t_0 + p\,x$ **exactly on the
bin grid** (so that its two-dimensional spectrum is concentrated in a few bins),
transforms it, and finds the peak bin at each frequency:

| event | $f$ (Hz) | peak $k_x$ (cycles/m) | $k_x/f$ (s/m) | true $p$ (s/m) |
|---|---|---|---|---|
| $v = 1500$ m/s | 15.0 | $-0.01000$ | $-6.667\times10^{-4}$ | $6.667\times10^{-4}$ |
| $v = 1500$ m/s | 20.0 | $-0.01250$ | $-6.250\times10^{-4}$ | $6.667\times10^{-4}$ |
| $v = 1000$ m/s, opposite dip | 20.0 | $+0.02000$ | $+1.000\times10^{-3}$ | $-1.000\times10^{-3}$ |
| $v = 1500$ m/s | 25.0 | $-0.01750$ | $-7.000\times10^{-4}$ | $6.667\times10^{-4}$ |
| $v = 1500$ m/s | 30.0 | $-0.02000$ | $-6.667\times10^{-4}$ | $6.667\times10^{-4}$ |

The measured $\lvert k_x/f\rvert$ reproduces $\lvert p\rvert$ to within 6%, and the
residual is wavenumber-bin quantisation: one bin is 0.00125 cycles/m, which at
20 Hz is a slowness step of $6.25\times10^{-5}$ s/m, i.e. 9% of $p$. Where the
event's line happens to fall on a bin (15, 20, 25 and 30 Hz do, at
$k_x/f = \pm10^{-3}$ for the opposite-dip event) the agreement is exact.
**The equality of the ratio to the slowness is exact; the discrepancy is bin
quantisation**, which is the finite array length speaking again.

### 3.2 The sign, which must be stated

The signs in the table are not arbitrary. With the forward kernel
$e^{-2\pi i(k_x x + k_t t)}$ used throughout this module, an event whose arrival
time *increases* with offset ($t = t_0 + p\,x$, $p>0$) has its
positive-frequency energy at

$$k_x = -p\,f .$$

So **energy moving towards increasing $x$ occupies the negative-$k_x$ half of the
$f$–$k_x$ plane**. With the opposite kernel it would occupy the positive half.
Both conventions are in use; a paper or a program that does not state which one
it uses cannot be checked, and the failure mode is silent (the filtered output
still looks like data). This is the two-dimensional version of the convention
discussion in [01-10-04](./04-discrete-fourier.md) Section 2.

## 4. Dip filtering: measured performance

### 4.1 Exact separation of grid-aligned plane waves

Two continuous plane waves are placed exactly on the bin grid — one at
$k_x = 10$ bins, the other at $k_x = -24$ bins, both at $k_f = 14$ bins
(13.672 Hz) — giving apparent velocities 1093.8 m/s and 455.7 m/s (the second
resembling ground roll: slower, and moving the other way). A fan filter keeps
$\lvert k_x/f\rvert < 1/800$ s/m, i.e. events faster than 800 m/s:

| quantity | RMS | fraction of its own event |
|---|---|---|
| event A (fast) surviving the filter | $7.0711\times10^{-1}$ | $1.000\times10^{0}$ |
| event B (slow) surviving the filter | $4.2179\times10^{-15}$ | $5.965\times10^{-15}$ |
| filter output minus event A | $4.5118\times10^{-15}$ | $6.381\times10^{-15}$ |

So for events that sit on the grid the separation is **exact to round-off**,
because each event occupies two bins and the mask is a straight line between
them. This is worth seeing once, because it shows that the *algebra* of f-k
filtering is not what limits it.

### 4.2 The same experiment with wave packets

Real events are not continuous plane waves; they are wave packets with a finite
spatial extent. Repeating the experiment with packets of various widths:

| packet width (s) | fraction of B leaking through | fraction of A lost |
|---|---|---|
| 0.06 | 0.2220 | 0.1274 |
| 0.12 | 0.2101 | 0.1254 |
| 0.24 | 0.1994 | 0.1266 |
| 0.48 | 0.1673 | 0.1049 |

About a fifth of a short, steep packet survives a fan filter, and a similar
fraction of the wanted event is removed. The cause is that a packet has a finite
spatial extent, so its f-k ridge is broadened in $k_x$ with a Dirichlet-like
spread; part of that spread lies on the wrong side of the mask, and part of the
wanted event's spread lies on the wrong side too.

**Both numbers should be quoted when an f-k filter is used.** "The ground roll was
removed" is incomplete without a measure of what else was removed.

## 5. Up/down separation is a quadrant filter

Two plane waves of the same frequency and opposite slowness occupy opposite
halves of the $f$–$k_x$ plane (Section 3.2). Keeping one half-plane together with
its conjugate — which is what makes the output a real signal — separates them.
On the grid-aligned test events:

| variant | RMS of B leaking in | RMS of A lost | leak/B | loss/A |
|---|---|---|---|---|
| quadrant only | $2.0019\times10^{-15}$ | $1.6081\times10^{-15}$ | $2.8\times10^{-15}$ | $2.3\times10^{-15}$ |
| quadrant + cone mute | $1.9841\times10^{-15}$ | $1.6596\times10^{-15}$ | $2.8\times10^{-15}$ | $2.3\times10^{-15}$ |

The separation is exact for on-grid events, and the cone mute changes nothing
here because these events have no near-origin content. With wave packets the
leakage returns to the few-per-cent level of Section 4.2.

This is the standard first step in vertical seismic profile (VSP) and walkaway
processing: separating up- from down-going energy requires **no velocity model**,
only the geometry, because opposite directions of propagation occupy opposite
halves of the plane. The cone around the origin is left unmuted because there the
two halves meet and no filter can tell them apart.

## 6. Spatial aliasing in the f-k plane

The demo places an event with $v = 1000$ m/s on a grid with $dx = 12.5$ m, so the
alias frequency is $v/(2dx) = 40$ Hz, and measures the peak wavenumber:

| $f$ (Hz) | true $\lvert k_x\rvert$ | observed $k_x$ | apparent $\lvert v\rvert$ (m/s) | aliased? |
|---|---|---|---|---|
| 20.0 | 0.02000 | $-0.02000$ | 1000 | no |
| 40.0 | 0.04000 | $+0.04000$ | 1000 | no (at the limit) |
| 52.0 | 0.05200 | $+0.02875$ | 1809 | **yes** |
| 80.0 | 0.08000 | $0.00000$ | $\infty$ | **yes** |

Below 40 Hz the measured wavenumber equals the true one. Above it the peak lands
on the far side of the Nyquist wavenumber: the apparent slowness stops
increasing, folds back, and the event reads as a *slower* dip in the *opposite*
direction. In f-k space aliasing is a wrap of the $k_x$ axis, and it is
completely invisible in the time–offset display — the event still looks like a
clean dipping arrival, just with the wrong dip.

This is the diagnostic used in practice: an event whose apparent dip *reverses*
between adjacent traces while its amplitude stays coherent is aliased, and the
reversal frequency identifies the sampling interval that would be needed.

## 7. Hard wavenumber cuts and the taper requirement

A wavenumber cut is a filter whose impulse response decays as $1/x$ (the
two-dimensional analogue of the sinc of
[01-10-03](./03-convolution.md)), so it is not local, and a record that does not
return to zero at the array edges has a discontinuity there. The demo applies a
cut at 6 bins to an event whose wavenumber is 10 bins — so real signal is removed
— and measures the resulting edge artefact:

| version | RMS in the first 4 traces | RMS in traces 20–43 | ratio |
|---|---|---|---|
| no taper | $9.3625\times10^{-2}$ | $1.5011\times10^{-2}$ | 6.237 |
| 10% cosine taper on all four edges | $5.6871\times10^{-2}$ | $1.3750\times10^{-2}$ | 4.136 |

The taper removes 14.38% of the total energy of the synthetic event and cuts the
edge amplitude by about 40%. Its larger benefit is that the remaining ringing is
pushed into the taper zone, where it is not interpreted.

The claim to remember: **a hard cut in wavenumber rings at the edges for the same
reason a hard cut in frequency rings in time** (Section 4 of
[01-10-03](./03-convolution.md)): a step through a brick wall produces the Gibbs
overshoot. Real f-k filtering therefore always comes with a spatial and temporal
taper, and often with padding, and amplitudes at the array edges are never
trustworthy.

## 8. Python demonstration

[`code/fk_filter_demo.py`](./code/fk_filter_demo.py) produces every table above in
a second or two:

```text
python3 code/fk_filter_demo.py
```

Four implementation notes.

1. **Two event generators are used deliberately.** `plane_event` places a
   continuous plane wave exactly on the bin grid, so that the algebra of f-k
   filtering can be tested without a discretisation error; `band_event` builds a
   finite wave packet, so that the same filter can be tested on something closer
   to field data. The difference between the two results *is* the lesson.
2. **The mask is defined by $k_x/f$, not by $k_x$ alone.** A dip filter is a
   statement about slowness, so it must be a cone through the origin; a mask on
   $k_x$ alone would be a different (and rarely wanted) filter.
3. **Leakage is measured on the *components separately*.** Applying the filter to
   event B alone gives the leakage of B; applying it to event A alone and
   differencing gives the distortion of A. Measuring the residual of the combined
   output against one component alone would confound B's leakage with A's
   distortion — and the two are equal by construction in a two-event test.
4. **The taper is applied to the data before the transform**, and the script
   reports both the edge-to-middle ratio and the energy it removed, so the cost of
   the taper is visible alongside the benefit.

## 9. Common mistakes

1. **Believing f-k filtering is lossless.** Section 4.2: about a fifth of a
   packet on the wrong side of the mask leaks through, and about a tenth of the
   wanted event is removed. Both must be reported.
2. **Not stating the sign convention.** The mask that removes the ground roll
   under one convention keeps it under the other, and both outputs look like
   seismic data.
3. **Using no spatial taper.** The edge artefacts of Section 7 are larger than
   the signal at the edges — which is where interpreters look for faults.
4. **Forgetting that aliased events have wrapped dips.** A fan filter applied to
   aliased data removes the wrong events; the aliased ground roll may share a
   quadrant with real reflections.
5. **Designing the filter on the f-k panel's appearance.** The mask must be
   derived from the velocities present in the data and the velocities wanted, and
   its effect on both must be measured.
6. **Applying an f-k filter to data that has not been spatially regularised.** A
   missing trace changes the effective $dx$ and hence the wavenumber axis.
7. **Confusing the f-k domain with the $f$–$k_z$ domain.** $k_z$ (vertical
   wavenumber) is what one-way wave equations use for depth extrapolation; $k_x$
   as used here is the horizontal wavenumber along the receiver line. They are
   related by the dispersion relation but they are not the same axis.
8. **Assuming a 2-D filter is applicable to 3-D data.** In three dimensions the
   ground roll is a cone, not a line, and the filter must be applied in
   $f$–$k_x$–$k_y$ with the correct mask — the extension is straightforward but
   not automatic.

## 10. Real-world applications

- **Ground-roll removal.** Ground roll is slow and dips at a distinctive
  slowness; a fan filter that keeps faster energy removes most of it in one step
  (subject to the aliasing caveat of Section 6).
- **VSP and walkaway up/down separation.** Section 5's quadrant filter is the
  first processing step in any VSP workflow, and it precedes any velocity model.
- **Multiple attenuation in the f-k (or Radon) domain.** Multiples have different
  moveout from primaries, so the geometry-based separation is the same idea with
  a more sophisticated transform.
- **Steering and directional filtering of potential-field data.** Wavenumber
  filtering of a gridded gravity or magnetic map separates short-wavelength
  anomalies with a preferred elongation (dykes, ridges) from isotropic noise.
- **Coherent noise removal in seismic shot records.** Linear noise from a
  vibrating source, power lines or a pipeline is exactly a set of lines in the
  f-k plane.
- **Two-dimensional spectral analysis of maps.** The radial wavenumber spectrum
  of topography, gravity or bathymetry is the natural tool for anisotropy and
  fabric analysis, and it is the transform of this lesson applied to an image —
  see [01-10-08](./08-spatial-spectra.md).

## 11. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** The sections on f-k and Radon filtering. Level: intermediate
  to advanced. The standard reference for what these filters do to real data,
  including their artefacts.
- **Embree, P., Burg, J. P. & Backus, M. M. (1963). Wide-band velocity filtering
  — the pie-slice process. *Geophysics*, 28(6), 948–974.** Level: advanced. The
  original development of dip filtering as a velocity-discrimination operation.
- **Sheriff, R. E. & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Chapter 9. Level: intermediate. The geometry of
  moveout and why events map to lines in f-k.
- **Hardage, B. A. (1985). *Vertical Seismic Profiling, Part A: Principles*.
  Geophysical Press.** Level: intermediate to advanced. Up/down separation in
  practice, including the cone around the origin.
- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapter 10 (two-dimensional transforms). Level:
  intermediate. Separability, the two-dimensional sampling theorem and the
  rotation theorem of the 2-D transform.
- **Vermeer, G. J. O. (2012). *3-D Seismic Survey Design* (2nd ed.). Society of
  Exploration Geophysicists.** Level: advanced. Spatial sampling as an engineering
  discipline, and why 3-D aliasing is a cone rather than a line.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 12. Related lessons

- [04 Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) — the
  one-dimensional transform this extends, and the sign convention it fixes.
- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) — the
  spatial Nyquist relation used in Section 6.
- [08 Power Spectra, Admittance and Coherence of Geophysical Fields](./08-spatial-spectra.md) —
  what to do with a 2-D spectrum when the question is statistical rather than
  kinematical.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](./03-convolution.md) —
  the one-dimensional counterpart of Section 7's ringing.
- [06-seismology](../../06-seismology/README.md) — surface waves, ground roll and
  the acquisition context of Sections 4 and 6.
- [20-signal-processing](../../20-signal-processing/README.md) — where f-k
  filtering sits in a processing sequence.

## 13. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/07-2d-fourier-exercises.md`](./exercises/07-2d-fourier-exercises.md).
Solutions: [`exercises/07-2d-fourier-solutions.md`](./exercises/07-2d-fourier-solutions.md).

## Self-assessment checklist

- [ ] I can write the 2-D DFT and its inverse, and state the bin spacings and the
      Nyquist wavenumber.
- [ ] I can explain why the transform is separable and verify it numerically.
- [ ] I can derive $k_x = p\,f$ for a plane wave and state the sign convention.
- [ ] I can design a fan filter from velocities and measure its leakage and its
      distortion of the wanted event.
- [ ] I can explain the difference between filtering ideal plane waves and real
      wave packets, with numbers.
- [ ] I can perform up/down separation by quadrant filtering and explain the cone
      around the origin.
- [ ] I can compute the spatial alias frequency and recognise an aliased event
      from its dip reversal.
- [ ] I can explain why a hard wavenumber cut needs a spatial taper, and quote
      the measured edge-to-middle ratio improvement.
