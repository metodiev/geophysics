# Solutions — 07-03-07 Time-Variable Gravity: Hydrology, Ice and Mass Redistribution

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [07 Time-Variable Gravity](../07-time-variable-gravity.md).

---

## ★1 — $5\ \mathrm{cm}$ of water

$$2\pi G\rho_w h = 2\pi(6.67430\times10^{-11})(1000)(0.05)
= 2.097\times10^{-8}\ \mathrm{m\,s^{-2}} = \mathbf{2.097\ \mu Gal},$$

$$4\pi G\rho_w h = 4.194\times10^{-8}\ \mathrm{m\,s^{-2}} =
\mathbf{4.194\ \mu Gal}.$$

A factor of two, from geometry alone: the slab field is the half-space value, the
shell field is the full radial value. The demonstration prints exactly these two
numbers for $h = 0.05\ \mathrm{m}$.

---

## ★2 — Which constant applies

- **A $100\ \mathrm{km}$ basin:** the flat-Earth slab constant $2\pi G\rho h$,
  because the horizontal scale is small compared with the Earth's radius and the
  layer is effectively infinite compared with the observation height. The
  demonstration's altitude study shows the ground peak is
  $2\pi G\rho h = 41.94\ \mu$Gal per metre of water for *any* footprint size.
- **A global ocean-mass change:** the shell constant $4\pi G\rho h$, because the
  mass is distributed over the whole sphere and the field at the surface is
  radial and additive.

Using the wrong one is a factor-of-two error, and the two are not
interchangeable at any scale: the correct choice is set by whether the layer
subtends a hemisphere or a whole sphere.

---

## ★3 — Gravity change to equivalent water height

$$\mathrm{EWH} = \frac{\Delta g}{2\pi G\rho_w}
\qquad \left[\frac{\mathrm{m\,s^{-2}}}{\mathrm{m^{3}kg^{-1}s^{-2}}\cdot
\mathrm{kg\,m^{-3}}}\right] = \mathrm{m} ✔$$

Equivalently, in convenient units,
$\mathrm{EWH\,[m]} = \Delta g\,[\mu\mathrm{Gal}]/41.936$.

---

## ★4 — $0.3\ \mathrm{m\,yr^{-1}}$ over $150\times150\ \mathrm{km}$

Gravity change:

$$\Delta g = 2\pi G\rho_w h
= 2\pi(6.67430\times10^{-11})(1000)(0.3)
= 1.258\times10^{-7}\ \mathrm{m\,s^{-2}} = \mathbf{12.58\ \mu Gal\ per\ year}.$$

Mass loss over $A = (150\times10^{3})^{2} = 2.25\times10^{10}\ \mathrm{m^{2}}$:

$$\Delta M = \frac{\Delta g\,A}{2\pi G}
= \frac{(1.258\times10^{-7})(2.25\times10^{10})}{2\pi(6.67430\times10^{-11})}
= \mathbf{6.75\times10^{12}\ kg\ per\ year}.$$

Sanity check from the water column directly:
$\rho_w h A = 1000\times0.3\times2.25\times10^{10} = 6.75\times10^{12}\ \mathrm{kg}$ ✔
— the two routes agree exactly, which is the internal consistency test for the
$2\pi G$ constant.

---

## ★5 — De-leaking a $0.35\ \mathrm{m}$ recovery

From the lesson's leakage table, a Gaussian feature of scale $\sigma$ recovered
after a filter of radius $r_f$ has amplitude

$$\text{recovered} = \text{true}\times\frac{\sigma^{2}}{\sigma^{2}+r_f^{2}} .$$

With $\sigma = r_f = 40\ \mathrm{km}$, the factor is $0.5$. The recovered
$0.35\ \mathrm{m}$ therefore corresponds to

$$\mathrm{EWH}_{\text{true}} = \frac{0.35}{0.5} = \mathbf{0.70\ m}.$$

**Direction of the bias:** ignoring the correction *underestimates* the true
storage by a factor of two — the recovered amplitude is a lower bound. The
demonstration's table quantifies the same effect across filter radii
($-20\%$ at $r_f/\sigma = 0.5$, $-50\%$ at $1$, $-80\%$ at $2$, $-94\%$ at $4$).
Note also that the de-leaking factor depends on the *assumed* source scale, so a
de-leaked amplitude carries an additional systematic uncertainty that must be
reported.

---

## ★6 — Trend precision from the table

| noise ($\mu$Gal) | scatter of the trend ($\mathrm{m\,yr^{-1}}$) | scatter of the annual amplitude (m) |
|---|---|---|
| 0.5 | 0.00039 | 0.00151 |
| 1.0 | 0.00078 | 0.00319 |
| 2.0 | 0.00159 | 0.00610 |

With $1\ \mu$Gal noise the trend is determined to about
$\mathbf{0.0008\ m\,yr^{-1}}$ — two orders of magnitude finer than the
$0.05\ \mathrm{m\,yr^{-1}}$ signal, because ten years of that trend integrate to
$0.5\ \mathrm{m}$ of EWH, i.e. about $21\ \mu$Gal, which is twenty-one times the
noise.

The **annual amplitude is determined less precisely in relative terms**
($0.00319/0.30 = 1.1\%$ against $0.00078/0.05 = 1.6\%$) — comparable. The reason
both are well determined is that the model is *orthogonal*: the trend is a ramp,
the season is a sinusoid, and over ten years their projections onto each other are
small. Over a one-year record they would be nearly collinear and both would be
poorly determined. **Record length, not amplitude, is the controlling factor.**

---

## ★7 — Separating a trend from seasons in a five-year record

**Model.**

$$y(t) = a + b\,t + c_1\cos\frac{2\pi t}{T} + d_1\sin\frac{2\pi t}{T}
+ c_2\cos\frac{4\pi t}{T} + d_2\sin\frac{4\pi t}{T},$$

with $T = 365.25\ \mathrm{d}$ and $t$ in years, fitted by least squares (or by
generalised least squares if the noise is correlated).

**Design matrix conditioning.** Over five years the trend regressor $t/YR$ spans
$[0,5]$ and the annual terms complete five full cycles, so the cross-products
between the trend and the seasonal terms are of order $1/(2\pi)\approx16\%$ of the
diagonal — small enough that the parameters are nearly orthogonal.

**Expected uncertainties** (white noise): the trend uncertainty scales as
$\sigma_g/(\text{span}\times\sqrt{n})$ — for the demonstration's daily sampling
and $1.5\ \mu$Gal noise it is roughly
$0.0008\times1.5\times\sqrt{10/5} \approx 0.0017\ \mathrm{m\,yr^{-1}}$, and the
annual amplitude to about $0.007\ \mathrm{m}$. With correlated noise these
inflate by the factors measured in
[07-04-04](../../04-geodesy-reference-frames/04-gnss-geodesy-applications.md)
(a factor of several), which must be included.

**Residual risk.**

1. **Aliasing.** If the sampling is irregular or the record is short compared with
   a cycle, the seasonal terms leak into the trend. Daily or weekly sampling over
   five years avoids this.
2. **Amplitude-modulated seasons.** A real cycle whose amplitude grows with time
   (drought years, for example) is not captured by a constant-amplitude annual
   term; its residual correlates with the trend and biases it.
3. **Unmodelled steps or a non-linear trend.** A single offset biases the trend by
   offset/span — for a $10\ \mu$Gal step in a five-year record that is about
   $0.05\ \mathrm{m\,yr^{-1}}$, larger than the signal. Steps must be searched for,
   not assumed absent.
4. **Correlated noise.** The formal uncertainties, if computed under a white-noise
   assumption, are optimistic by the factor measured in the GNSS lesson; the
   *rank* of the parameters is unaffected, but the uncertainty statements are not.

**Report:** the trend with its uncertainty under a *stated* noise model, the
seasonal amplitudes, the offsets identified, and the residual spectrum, so a
reviewer can judge the noise model rather than take it on trust.

---

## ★8 — The mass-estimate error budget, $300\ \mathrm{km}$ region

For a change $\Delta g$ measured over area $A$ with density $\rho_w$ assumed:

$$\delta(\Delta M) = \Delta M\left[
\frac{\delta(\Delta g)}{\Delta g} \oplus
\frac{\delta A}{A} \oplus
\frac{\delta\rho}{\rho} \oplus
\frac{\delta(\text{leakage})}{1}
\right].$$

Ordered by size for a $300\ \mathrm{km}$ region:

1. **Leakage / filtering (largest, often $20$–$90\%$).** The demonstration's table
   gives $-20\%$ to $-94.1\%$ for filter radii between $0.5\times$ and
   $4\times$ the source scale. This is systematic, does not average away, and
   depends on the unknown source scale, so a correction is itself uncertain.
2. **Attribution / competing signals (large).** Groundwater depletion plus rebound
   plus ice loss all contribute; separating them needs spatial patterns or
   independent data. Not a noise term at all.
3. **Density assumption ($\sim10$–$100\%$).** Water versus rock versus ice changes
   the inferred thickness by the density ratio; for ice at
   $917\ \mathrm{kg\,m^{-3}}$ it is an $8\%$ effect, for rock at
   $2500\ \mathrm{kg\,m^{-3}}$ a $250\%$ one.
4. **Area ($\sim$few %).** Depends on how the region boundary is defined relative
   to the mass distribution; enters linearly.
5. **Measurement noise (smallest, $\sim10\%$).** From the demonstration's table,
   $0.2\ \mu$Gal on a $2\ \mu$Gal signal is $10\%$, and it is the only term that
   averaging can reduce.

**Which a reviewer should challenge first:** the **leakage/filtering term**,
because it is the largest, it is systematic, and it cannot be assessed without the
filter parameters and an assumed source scale — and because a paper that reports
only a measurement noise budget is implicitly claiming a precision the data do not
support.
