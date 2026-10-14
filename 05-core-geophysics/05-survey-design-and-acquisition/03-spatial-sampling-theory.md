---
id: 05-05-03
title: "Spatial Sampling, Wavenumber Aliasing and Reconstruction"
level: graduate
prereqs: ["01-10-05", "05-01-03"]
tags: [nyquist, aliasing, sampling-theory, wavenumber, reconstruction, sinc]
---

# Spatial Sampling, Wavenumber Aliasing and Reconstruction

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the spatial Nyquist condition from the sampling theorem, in both
   wavelength and wavenumber form.
2. **Compute** the apparent wavenumber of an aliased sinusoid using the folding
   formula, and predict the apparent wavelength that a survey will report.
3. **Demonstrate**, by construction, that an aliased field is *indistinguishable*
   from the true one at the sample locations, so that no processing step can
   remove it.
4. **Reconstruct** a band-limited field from its samples with the sinc interpolant,
   and state the conditions under which the reconstruction is exact.
5. **Distinguish** the aliasing limit (set by sample spacing) from the resolution
   limit (set by bandwidth, geometry and the physics) and from the depth of
   investigation (set by source strength and noise).
6. **Choose** a station spacing from a target wavelength, and state the safety
   factor and why it is needed.

## Prerequisites

- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md)
  — the one-dimensional theory, including the folding formula and the DFT
  conventions used here. This lesson applies it in space rather than in time.
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
  — the qualitative distinction of Section 7.
- [05-03-02 Analytical Solutions for Simple Bodies](../03-forward-modelling-principles/02-analytical-solutions.md)
  — the fields whose wavenumber content is discussed in Section 8.

## 1. Intuition: the survey samples a continuum

The Earth's field is a function of position, defined everywhere. A survey records
it at a finite set of points and then *interpolates* and *contours* as though the
continuum had been measured. The sampling theorem states exactly when that
pretence is legitimate, and what happens when it is not.

Two facts make this the most consequential topic in survey design:

- **Sampling is a lossy operation, and the loss is silent.** A field sampled too
  coarsely is not merely blurred — it is *replaced* by a different field, one with
  a longer wavelength, and the replacement is a perfect description of the samples.
  Nothing in the recorded numbers signals that a substitution occurred.
- **The substitution cannot be undone.** It is not a filter with an inverse. The
  information about the original wavelength was never recorded, and no operator can
  apply to it.

Aliasing is therefore the one processing failure that is decided at the planning
stage and cannot be repaired later. Everything else in a processing sequence can,
at worst, be redone.

## 2. Precise definitions

### 2.1 Spatial sampling

Let a field $f(x)$ be sampled at $x_n = n\Delta x$, $n \in \mathbb{Z}$. Write its
Fourier representation with the convention

$$f(x) = \int_{-\infty}^{\infty} F(k)\,e^{\,\mathrm{i}kx}\,\mathrm{d}k ,
\qquad k = \frac{2\pi}{\lambda} ,
\tag{1}$$

so that $k$ has units of radians per metre and $\lambda$ is wavelength in metres.

### 2.2 Nyquist wavenumber

The **Nyquist wavenumber** of the sampling is

$$\boxed{\ k_N = \frac{\pi}{\Delta x}\ }
\tag{2}$$

and the **Nyquist wavelength** is

$$\lambda_N = \frac{2\pi}{k_N} = 2\Delta x .
\tag{3}$$

A field whose spectrum vanishes for $|k| > k_N$ is **band-limited to the grid** and
can be recovered exactly. A field with content at $|k| > k_N$ is **aliased**.

### 2.3 Apparent (folded) wavenumber

A component at wavenumber $k_0$ is recorded at the **apparent wavenumber**

$$k_{\text{app}} = \big((k_0 + k_N) \bmod 2k_N\big) - k_N ,
\tag{4}$$

where $\bmod$ is the positive remainder. Equation (4) is the spatial version of the
temporal folding formula in
[01-10-05](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) and
reduces to it under $k \leftrightarrow 2\pi f$ and $\Delta x \leftrightarrow 1/f_s$.
The apparent wavelength is $\lambda_{\text{app}} = 2\pi/|k_{\text{app}}|$.

## 3. Derivation of the folding formula

The sampled field is the product of the continuous field with the **comb**

$$\mathrm{III}(x) = \sum_n \delta(x - n\Delta x) ,
$$

whose Fourier transform is another comb of spacing $1/\Delta x$:

$$\widehat{\mathrm{III}}(k) = \frac{1}{\Delta x}\sum_m \delta\!\left(k - \frac{2\pi m}
{\Delta x}\right) .
$$

Multiplication in space is convolution in wavenumber, so the spectrum of the
sampled field is

$$\hat f_s(k) = F(k) * \widehat{\mathrm{III}}(k)
= \frac{1}{\Delta x}\sum_{m=-\infty}^{\infty} F\!\left(k - \frac{2\pi m}{\Delta x}\right).
\tag{5}$$

Equation (5) is the whole of aliasing: **sampling replicates the spectrum at
intervals of $2\pi/\Delta x = 2k_N$, and the replicas overlap.** A component at
$k_0$ therefore contributes to the record at every $k_0 + 2mk_N$; the replica that
falls inside the fundamental interval $(-k_N, k_N]$ is the apparent wavenumber of
equation (4). Two distinct true wavenumbers

$$k_0 \quad\text{and}\quad k_0 + 2m k_N$$

are recorded at exactly the same apparent wavenumber, for every integer $m$. That
is not an approximation; it is an identity.

For a real sinusoid $\cos(k_0 x)$ sampled on the grid, equation (4) with the sign
preserved gives the apparent wavenumber directly, and the amplitude is unchanged:
the alias has the *same* amplitude as the original.

## 4. The decisive demonstration

[`code/aliasing_demo.py`](./code/aliasing_demo.py) samples a 100 m wavelength
sinusoid at $\Delta x = 60$ m, which is above the Nyquist wavelength of
$2\Delta x = 120$ m. Every number below is printed by that script.

### 4.1 The prediction

| quantity | value |
|---|---|
| true wavelength | 100.000 m |
| true wavenumber $k_0$ | 0.062832 rad/m |
| station spacing $\Delta x$ | 60.000 m |
| Nyquist wavelength $2\Delta x$ | 120.000 m |
| Nyquist wavenumber $k_N = \pi/\Delta x$ | 0.052360 rad/m |
| $k_0/k_N$ | 1.2000 (greater than 1: aliased) |
| folded wavenumber, equation (4) | $-0.041888$ rad/m |
| **apparent wavelength** | **150.000 m** |

The survey will report a 150 m anomaly. Note that the report is internally
consistent: 150 m is longer than 120 m, so it is a *legal* answer for this grid, and
nothing about the record is anomalous.

### 4.2 The alias fits the data exactly

A least-squares fit of a sinusoid to the ten coarse samples gives

| fitted wavelength | amplitude | phase (deg) | RMS residual |
|---|---|---|---|
| 150.000 m (apparent) | 1.000000 | 0.000 | $7.052\times10^{-16}$ |
| 100.000 m (true) | 1.000000 | 0.000 | $1.755\times10^{-16}$ |

Both fits are exact to machine precision, and the maximum difference between the
two fitted curves *at the sample locations* is $1.72\times10^{-15}$. There is no
statistic of the samples that can prefer one. Constructing the alias directly
confirms it: the maximum difference between the true samples and the samples of a
genuine 150 m sinusoid is $1.776\times10^{-15}$.

This is the sense in which aliasing is a *substitution* and not a *distortion*:
the two distinct Earths are indistinguishable, and the record describes both
perfectly.

### 4.3 The spectrum shows the fold, and the truth is outside the band

| quantity | value |
|---|---|
| representable band | $\lvert k\rvert \le k_N = 0.052360$ rad/m |
| peak spectral bin | $+0.041888$ rad/m, i.e. wavelength 150.000 m |
| folded wavenumber from equation (4) | $-0.041888$ rad/m, wavelength 150.000 m |
| $\lvert k_0\rvert$ vs $k_N$ | 0.062832 vs 0.052360, ratio 1.200 |

The measured spectral peak sits exactly at the closed-form folded wavenumber — the
FFT bins were chosen so that it lands on a bin, which is why the agreement is exact
rather than approximate. The true wavenumber lies **outside the representable band**
by a factor 1.2, so it cannot appear in any spectrum computed from this record.
Consequently:

- **low-pass filtering does not help.** Removing the apparent 150 m peak does not
  reveal a 100 m feature; it removes the only thing there is, leaving nothing.
- **Continuing or transforming the field does not help.** Every linear operator
  acts on the recorded band, in which only the alias exists.
- **Increasing the line length does not help.** Longer records sharpen the spectrum
  but do not widen the band; $k_N$ is set by $\Delta x$ alone.

### 4.4 A finer grid does show the truth

Sampling the same field at $\Delta x = 2$ m recovers the 100 m wavelength with a
fit residual of $2.437\times10^{-16}$. The difference between the two surveys is
60 m of station spacing, and it is the difference between measuring the field and
measuring a different field. **No amount of processing afterwards substitutes for
those 58 metres.**

## 5. Reconstruction

If the field is band-limited to $\lvert k\rvert \le k_N$, the sampling theorem gives
an exact reconstruction:

$$f(x) = \sum_{n} f(x_n)\,\operatorname{sinc}\!\left(\frac{x - x_n}{\Delta x}\right),
\qquad \operatorname{sinc}(u) = \frac{\sin \pi u}{\pi u} .
\tag{6}$$

Four properties of equation (6) matter in practice:

1. **It is exact**, but only under the band-limit assumption. For an aliased field
   it reconstructs the alias perfectly — that is the trap.
2. **The interpolant is infinite in extent.** Truncating it (which every real
   interpolation does) introduces the edge and ripple errors measured in
   [05-06-05 Gridding, Merging and Levelling of Survey Data](../06-data-processing-principles/05-merge-and-regularisation.md).
3. **It requires far more samples than the Nyquist minimum.** The sinc has slow
   $1/u$ decay, so several samples per shortest wavelength are needed for a
   practical reconstruction. This is the reason for the four-to-five stations per
   anomaly rule of thumb; the minimum is two, and the minimum is unusable.
4. **Gridding is not reconstruction.** Splines, kriging and minimum curvature are
   *interpolants*, not band-limited reconstructions; they invent plausible
   intermediate values rather than recovering measured ones, as quantified in
   [05-06-05](../06-data-processing-principles/05-merge-and-regularisation.md).

## 6. Worked examples

### 6.1 Apparent wavelength of an aliased anomaly

A magnetic survey uses $\Delta x = 200$ m (so $k_N = \pi/200 = 0.015708$ rad/m) and
the true anomaly has $\lambda_0 = 300$ m, i.e. $k_0 = 2\pi/300 = 0.020944$ rad/m.
Then $k_0/k_N = 1.333$, so the anomaly is aliased. Folding:

$$k_{\text{app}} = \big((0.020944 + 0.015708) \bmod 0.031416\big) - 0.015708
= 0.005236 - 0.015708 = -0.010472\ \mathrm{rad\,m^{-1}},$$

so $\lambda_{\text{app}} = 2\pi/0.010472 = 600$ m. The survey reports a 600 m
anomaly from a 300 m source. Note the arithmetic shortcut for a single fold:
$\lambda_{\text{app}}^{-1} = \lvert \lambda_0^{-1} - 2/\lambda_N^{-1}\rvert$ is not
needed; use equation (4) and never guess.

### 6.2 Required station spacing

An orebody's gravity anomaly has a half-width of about 250 m. To sample it at five
stations across the half-width, $\Delta x = 100$ m; at the Nyquist minimum,
$\Delta x = 250$ m. For the *shape* to be interpretable, use the five-station
choice. Then $k_N = 0.031416$ rad/m, $\lambda_N = 200$ m, and the shortest anomaly
wavelength representable is 200 m — comfortably shorter than the anomaly's
half-width scale, which is the requirement.

### 6.3 The 2-D case

On a grid with spacings $\Delta x$, $\Delta y$, the Nyquist condition is applied
per axis:

$$|k_x| \le \frac{\pi}{\Delta x}, \qquad |k_y| \le \frac{\pi}{\Delta y} .
\tag{7}$$

A **diagonal** structure of wavelength $\lambda$ along the diagonal has components
$k_x = k_y = 2\pi/(\lambda\sqrt{2})$; it is the *components* that must be below the
per-axis limits, not the total wavenumber. Therefore a grid with a coarse spacing
along one axis aliases structures that are resolved along the other: an
anisotropy in the *sampling*, which will be reported as an anisotropy in the
*geology* unless the grid is symmetric or the effect is quantified.

## 7. Three different limits, kept separate

| limit | set by | improved by | worsened by |
|---|---|---|---|
| **Aliasing** | $\Delta x$ alone | smaller $\Delta x$ | — |
| **Resolution** | bandwidth, geometry, physics (Fresnel zone $\sqrt{\lambda h/2}$, or the two-body limit $h$) | a closer spacing *only* up to the physical limit | deeper or weaker sources |
| **Depth of investigation** | source strength, depth, noise | lower noise, more repeats | greater depth |

They are independent, and each has its own arithmetic. The classic planning error is
to reduce $\Delta x$ in the belief that this increases the depth of investigation;
it does not, because the depth reach is set by the noise and the source, and denser
stations do not lower the noise *per station*. The second classic error is to reduce
$\Delta x$ in the belief that this improves resolution below the physical limit: it
does not, as the Fresnel-zone numbers in
[05-05-02](./02-geometry-and-coverage.md) show.

## 8. Aliasing of potential-field and wavefield data compared

The two cases differ in what sets the shortest natural wavelength:

- **Potential fields.** The field of a compact body at depth $h$ has essentially no
  energy above $k \sim 2/h$. Sampling at $\Delta x = h/4$ gives
  $k_N = 4\pi/h \gg 2/h$, so potential-field *aliasing* is rarely a problem in
  practice: the depth itself band-limits the signal. What *is* a problem is
  **cultural noise** — fences, pipes, roads — which is generated at the surface,
  has very high wavenumbers, and aliases freely. A gravity survey for a deep target
  with a 200 m spacing will alias a nearby road into a broad, plausible anomaly.
- **Wavefields.** Here the band is set by the source (a 5–80 Hz sweep, say) and the
  material velocity. The aliasing condition is usually written in terms of
  apparent velocity,

  $$f_{\max} = \frac{v_a}{2\Delta x} ,
  \tag{8}$$

  and it applies on the *receiver* and the *source* axes independently. Ground roll
  with a low apparent velocity requires a much smaller spacing than a reflection at
  the same frequency, which is why arrays (spatial filters, which are
  *anti-alias* filters for the ground-roll band) are used rather than smaller
  spacings for the whole spread.

## 9. Assumptions

1. **Uniform sampling.** All of the above assumes a constant $\Delta x$. Scattered
   or irregular stations have no single $k_N$; the effect is equivalent to adding
   noise, and the honest procedure is to grid to a regular interval and then apply
   the theory to that interval, remembering that the gridding itself interpolated.
2. **Infinite, uniformly sampled record.** Real profiles are finite; leakage and
   windowing apply
   ([01-10-05](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md)).
3. **Ideal point samples.** Real measurements are averages over a detector or a
   station footprint. A receiver array is itself a spatial filter with its own
   wavenumber response, which attenuates some wavenumbers before sampling and
   therefore changes the alias — usually in a helpful direction.
4. **Linearity.** Equations (5)–(6) are linear. Aliasing of a *product* of fields
   (as in a non-linear inversion or a migrated image) is not described by a simple
   fold.
5. **Positional accuracy.** Aliasing theory assumes the sample *positions* are
   exact. Positioning error acts as a random phase perturbation and raises the
   effective noise floor; see [05-05-04](./04-positioning-gnss.md).

## 10. Units and dimensional analysis

$$[k] = \mathrm{rad\,m^{-1}}, \qquad [\lambda] = \mathrm{m}, \qquad
[k_N] = [\pi/\Delta x] = \mathrm{m^{-1}} .$$

Radians are dimensionless, so $k$ and $1/\Delta x$ have the same units, which is
why the folded wavenumber in equation (4) can be added to $k_N$ directly. The
argument of the sinc, $(x-x_n)/\Delta x$, is a length ratio — dimensionless, as
required. In equation (8),
$[v_a/2\Delta x] = \mathrm{m\,s^{-1}/m} = \mathrm{s^{-1}}$: a frequency, as
required.

A caution on units: the same survey is often described in **cycles per metre**
($1/\lambda$) and in **radians per metre** ($2\pi/\lambda$). The Nyquist limit is
$1/(2\Delta x)\ \mathrm{cycles\,m^{-1}}$ or $\pi/\Delta x\ \mathrm{rad\,m^{-1}}$.
Confusing the two produces a factor $2\pi$ error, and a survey aliasing by a factor
$2\pi$ is usually still aliasing, so the mistake survives the first review.

## 11. Python demonstration

[`code/aliasing_demo.py`](./code/aliasing_demo.py) produces every number in
Section 4. The two essential lines are the fold and the exact-fit test:

```python
def fold_wavenumber(k, k_nyq):
    return (k + k_nyq) % (2.0 * k_nyq) - k_nyq          # equation (4)

k_app = fold_wavenumber(2 * np.pi / 100.0, np.pi / 60.0)  # -0.041888 rad/m
lam_app = 2 * np.pi / abs(k_app)                          # 150.000 m
```

Measured results: apparent wavelength 150.000 m against a true 100.000 m; both
sinusoids fit the ten samples with RMS residual below $10^{-15}$; the spectrum peaks
at the folded wavenumber; and the true wavenumber exceeds the Nyquist wavenumber by
a factor 1.2 and is therefore unrepresentable.

## 12. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/03-spatial-sampling-theory-exercises.md`](./exercises/03-spatial-sampling-theory-exercises.md)
and [`exercises/03-spatial-sampling-theory-solutions.md`](./exercises/03-spatial-sampling-theory-solutions.md).

### Common mistakes

1. **Believing aliasing is a filtering problem.** It is a sampling problem, decided
   before acquisition. Section 4.3 shows why no filter helps.
2. **Using the Nyquist minimum as a working spacing.** Two samples per wavelength
   is exact only for infinite, perfectly band-limited data; use four to five.
3. **Confusing cycles per metre with radians per metre.** Section 10.
4. **Forgetting the source axis.** In a wavefield survey both the receiver and the
   shot axes must satisfy the Nyquist condition; their spacings are often different.
5. **Assuming an irregular survey is safe.** Irregular spacing has no clean
   Nyquist limit; it degrades gracefully only if it is finer than a regular grid
   would need to be.
6. **Diagnosing an alias only after interpretation.** A coherent-looking anomaly at
   double or half the expected scale is the signature; check the spacing against the
   ratio $\lambda_0/\lambda_N$ before mapping it.

### Real-world applications

- **Aeromagnetic surveys for shallow targets.** Flight-line spacing of 200 m cannot
  resolve a 100 m dyke; the survey reports a 200 m-scale anomaly. Section 6.1 is
  exactly this calculation.
- **Ground-roll suppression.** Receiver arrays are spatial anti-alias filters that
  remove ground roll *before* sampling, at the cost of attenuating short-wavelength
  reflections as well.
- **Regional gravity surveys.** Deep targets are naturally band-limited, so coarse
  spacing is acceptable — but near-surface cultural features are not, and they alias
  into the regional field.
- **Satellite altimetry and gravity.** The intrinsic sampling of the satellite track
  sets the shortest recoverable wavelength; no processing recovers a seamount
  smaller than the track spacing demands.

## 13. Further reading

- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications* (3rd ed.).
  McGraw-Hill.** Chapters 5 and 10 for sampling and the comb, from which Section 3
  is drawn. Level: intermediate.
- **Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-Time Signal Processing*
  (3rd ed.). Pearson.** Chapter 4. The rigorous treatment of aliasing, folding and
  reconstruction. Level: intermediate to advanced.
- **Vermeer, G. J. O. (2002). *3-D Seismic Survey Design*. SEG.** On the
  spatial-sampling requirements specific to seismic acquisition, including the
  source and receiver axes. Level: advanced practitioner.
- **Mallick, S., & Sharma, S. (2015). *Seismic and Petroleum Exploration* — see
  your library for a current edition.** General survey-design background. Level:
  intermediate.
- **EarthScope / IRIS instrumentation pages** — <https://www.earthscope.org> — for
  practical sampling rates and array spacings used in observing systems.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 14. Related lessons

- [05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](./02-geometry-and-coverage.md) — the bin size as an aliasing limit, and the Fresnel zone.
- [05-05-04 Positioning with GNSS/DGPS and Static Corrections](./04-positioning-gnss.md) — position error as a phase perturbation.
- [05-06-05 Gridding, Merging and Levelling of Survey Data](../06-data-processing-principles/05-merge-and-regularisation.md) — what interpolation does and does not recover.
- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) — the temporal theory this lesson transposes to space.
- [01-10-08 Power Spectra, Admittance and Coherence of Geophysical Fields](../../01-mathematics/10-fourier-analysis/08-spatial-spectra.md) — how to read a measured spatial spectrum and see an alias in it.

## 15. Self-assessment checklist

- [ ] I can derive $k_N = \pi/\Delta x$ and state the corresponding Nyquist wavelength.
- [ ] I can apply the folding formula and get the apparent wavelength right, with the sign.
- [ ] I can explain why the alias fits the samples exactly, not approximately.
- [ ] I can say why no filter, continuation or inversion removes an alias.
- [ ] I can write the sinc reconstruction and name the two assumptions behind it.
- [ ] I can keep aliasing, resolution and depth of investigation separate and give the controlling parameter for each.
- [ ] I can choose a station spacing from a target wavelength with a stated safety factor.
- [ ] I can name the case in which potential-field aliasing is dominated by cultural rather than geological sources.
