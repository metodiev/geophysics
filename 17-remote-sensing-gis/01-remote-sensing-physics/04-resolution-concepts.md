---
id: 17-01-04
title: "Spatial, Spectral, Temporal and Radiometric Resolution"
level: intermediate
prereqs: ["17-01-01", "20-01-05", "02-10-02"]
tags: [remote-sensing, gis, resolution, sampling, mtf, radiometry]
---

# Spatial, Spectral, Temporal and Radiometric Resolution

"Resolution" is the most overworked word in remote sensing, and the damage is
done by treating it as one number. Four different quantities hide behind it, they
trade against each other, and none of them is a property of the instrument alone:

- **spatial resolution** — the smallest ground separation that can be
  distinguished, set by the aperture, the altitude and the detector pitch;
- **spectral resolution** — the narrowest wavelength interval that can be
  separated, set by the dispersing element, the slit and the detector;
- **temporal resolution** — how often the same place is observed, set by the
  orbit, the swath and the pointing;
- **radiometric resolution** — the smallest radiance difference that can be
  detected, set by the detector noise and the quantiser.

The essential quantitative fact of this lesson is the **trade**. With a fixed
aperture, collecting area and integration time, the signal collected per pixel
scales as the square of the ground sample distance times the band width. Halving
the pixel size quarters the signal; halving the band width halves it; doing both
divides it by eight. Sharper and finer is *bought* with radiometric precision,
and the purchase price is arithmetic, not engineering taste. The demonstration
measures it: relative signal $1.000 \to 0.250$ for a halved GSD, $\to 0.125$ for
a halved GSD and a halved band width.

A second fact is that a "ground sample distance" is a *sampling* interval, not a
resolution. The demonstration's synthetic instrument has a $7.00\ \mathrm{m}$
GSD with a $0.30\ \mathrm{m}$ aperture at $700\ \mathrm{km}$, and its optical
cut-off is $13.09\times$ the sampling Nyquist frequency in the visible — meaning
it is **undersampled** and can only avoid aliasing because the optics already
attenuate the detail the detector cannot represent.

All models and data in this module are **SYNTHETIC**. The instrument here is a
teaching geometry defined entirely by parameters in
`code/resolution_concepts_demo.py` (altitude, aperture, detector pitch, grating,
swath, orbit rate, bit depth). No real instrument, mission or orbit is
represented.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the ground sample distance from altitude and instantaneous field
   of view, and **explain** why it is a sampling interval rather than a
   resolution.
2. **Compute** the diffraction-limited spot and the incoherent cut-off frequency,
   and **decide** whether a design is aperture-limited or detector-limited.
3. **Apply** the Nyquist criterion to a detector pitch and **state** whether a
   band is aliased.
4. **Compute** the system MTF as the product of component MTFs and **interpret**
   the contrast at the Nyquist frequency.
5. **Derive** the spectral resolving power of a grating and **compute** the
   minimum resolvable wavelength interval.
6. **Derive** the equatorial revisit time of a single swath and **state** the
   idealisations that make the achieved revisit worse.
7. **Compute** the noise-equivalent temperature difference from a stated
   noise-equivalent radiance, and **quantify** the spatial/spectral/radiometric
   trade.

## Prerequisites

- [17-01-01 The Electromagnetic Spectrum and Sensing Windows](01-em-spectrum-remote-sensing.md)
  — the wavelengths and radiance units used throughout.
- [20-01-05 Sampling, Nyquist and Reconstruction](../../20-signal-processing/01-signals-and-systems/05-sampling-theory.md)
  — the sampling theorem behind the aliasing criterion.
- [02-10-02 Interference and Diffraction in Optical Instruments](../../02-physics/10-optics-and-photometry/02-interference-diffraction-optics.md)
  — the Airy pattern and the grating equation.

---

## 1. Intuition: four knobs and one budget

Picture the instrument as a bucket collecting photons. The bucket has three
handles:

- how much of the ground each detector element sees (spatial);
- how wide a slice of the spectrum it accepts (spectral);
- how long it stares, and through how big an aperture (radiometric).

Turn any handle toward "finer" and the number of photons in the bucket falls.
That is the whole trade, and the rest of the lesson is the arithmetic.

Temporal resolution enters differently: it is fixed by where the platform is, not
by the detector. A narrow swath gives fine spatial sampling and infrequent
revisits; a wide swath gives the opposite. A constellation buys revisit time with
the number of satellites, and that is why constellations exist.

Two warnings that recur in the rest of the folder. First, a finer GSD does not
mean a finer *resolution* if the aperture cannot deliver the detail: at
$10.8\ \mathrm{\mu m}$ the synthetic instrument's Airy spot is
$30.74\ \mathrm{m}$ against a $7.00\ \mathrm{m}$ GSD, so its thermal band is
utterly aperture-limited. Second, a single band cannot separate a small hot
target from a large warm one — the *mixed pixel* problem of Section 3.7.

## 2. Precise definitions and units

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| ground sample distance | GSD | m | altitude × IFOV |
| instantaneous field of view | IFOV | rad | angular subtense of one detector |
| detector pitch | $w$ | rad or m | centre-to-centre spacing on the ground |
| Nyquist frequency | $f_N$ | cycles m⁻¹ | $1/(2w)$ |
| Airy spot | $d_A$ | m | $1.22\,\lambda H/D$ |
| incoherent cut-off | $f_c$ | cycles m⁻¹ | $D/(\lambda H)$ |
| MTF | — | dimensionless | modulus of the normalised transfer function |
| resolving power | $R$ | dimensionless | $\lambda/\Delta\lambda$ |
| revisit time | $T_r$ | days | time to re-observe a latitude circle |
| quantisation step | $q$ | W m⁻² sr⁻¹ m⁻¹ | $L_{\max}/2^{b}$ |
| NEΔL, NEΔT | — | W m⁻² sr⁻¹ m⁻¹, K | radiance/temperature giving SNR = 1 |

Two conventions are worth pinning down because sources differ. The **Airy first
zero** is at $1.22\lambda/D$ in angle; the **incoherent cut-off frequency** of a
circular aperture is at $D/(\lambda H)$ cycles per unit ground length, which is a
factor $1.22$ higher. This lesson uses both and says which is which.

## 3. Derivations

### 3.1 Ground sample distance

For a nadir-looking detector subtending angle $\theta_{\rm IFOV}$ from altitude
$H$,

$$\mathrm{GSD} = H\,\theta_{\rm IFOV}
\qquad(\text{small-angle, flat Earth}).$$

*Numerical check.* $H = 700\ \mathrm{km}$, $\theta_{\rm IFOV} = 10\ \mathrm{\mu rad}$:

$$\mathrm{GSD} = 7.00\times10^{5}\ \mathrm{m}\times10\times10^{-6}
= 7.00\ \mathrm{m}.$$

At an off-nadir look angle $\phi$ the same angular IFOV projects onto the ground
as $H\theta_{\rm IFOV}/\cos^{2}\phi$ (flat Earth), so the footprint grows as
$\sec^{2}\phi$ — a $30°$ off-nadir view widens the pixel by $1.33\times$ and a
$60°$ view by $4\times$. **A quoted single GSD therefore describes nadir only.**

### 3.2 Diffraction and the aperture limit

A circular aperture of diameter $D$ forms an Airy pattern whose first zero is at
angle

$$\theta_A = 1.22\,\frac{\lambda}{D}
\;\Longrightarrow\;
d_A = 1.22\,\frac{\lambda H}{D} \quad\text{on the ground}.$$

The incoherent transfer function of the same aperture vanishes at

$$f_c = \frac{D}{\lambda H} \quad[\mathrm{cycles\,m^{-1}}].$$

*Numerical check.* With $D = 0.30\ \mathrm{m}$, $H = 700\ \mathrm{km}$:

| $\lambda$ (µm) | $d_A$ (m) | GSD/$d_A$ |
|---|---|---|
| 0.45 | 1.281 | 5.464 |
| 0.66 | 1.879 | 3.726 |
| 1.65 | 4.697 | 1.490 |
| 10.8 | 30.744 | 0.228 |

At $10.8\ \mathrm{\mu m}$ the GSD is *smaller* than the Airy spot, so the system
cannot deliver its nominal GSD: the design is aperture-limited, and the only
remedies are a larger aperture, a lower orbit, or a coarser GSD accepted as such.

### 3.3 Nyquist and aliasing

A detector that samples the ground at pitch $w$ represents spatial frequencies up
to

$$f_N = \frac{1}{2w}.$$

Content above $f_N$ folds back to a false lower frequency (aliasing). The design
criterion is $f_c \le f_N$, or equivalently a detector whose pitch satisfies
$w \le \lambda H/(2D)$.

*Numerical check.* $w = 8.40\ \mathrm{m}$ gives $f_N = 0.05952\
\mathrm{cycles\,m^{-1}}$. The optical cut-off is $D/(\lambda H)$:

| $\lambda$ (µm) | $f_c$ (cycles/m) | $f_c/f_N$ | verdict |
|---|---|---|---|
| 0.45 | 0.95238 | 16.00 | aliased |
| 0.55 | 0.77922 | 13.09 | aliased |
| 0.86 | 0.49834 | 8.37 | aliased |
| 1.65 | 0.25974 | 4.36 | aliased |
| 10.8 | 0.03968 | 0.67 | ok |

The synthetic design is Nyquist-compliant only in the thermal band. In the
visible it is undersampled, and what saves it is that the optical MTF has already
attenuated the high frequencies the detector cannot represent — an accidental
protection, not a design guarantee.

### 3.4 MTF and the contrast that remains

The system MTF is the product of its parts:

$$\mathrm{MTF}_{\rm sys}(f) = \mathrm{MTF}_{\rm opt}(f)\cdot
\mathrm{MTF}_{\rm det}(f)\cdot\mathrm{MTF}_{\rm motion}(f)\cdots$$

For a rectangular detector of ground width $w$,
$\mathrm{MTF}_{\rm det}(f) = \operatorname{sinc}(fw) =
\sin(\pi fw)/(\pi fw)$, and for a cut-off-limited circular aperture we use the
standard approximation $\mathrm{MTF}_{\rm opt}(f) = 1 - f/f_c$.

At a design's own Nyquist frequency, $f = 1/(2w)$, so $fw = 1/2$ and

$$\mathrm{MTF}_{\rm det}(f_N) = \operatorname{sinc}(\tfrac{1}{2}) = 0.6366
\quad\text{for every design}.$$

What changes between designs is the optical factor:

| pitch $w$ (m) | $f_N$ (cyc/m) | $\mathrm{MTF}_{\rm opt}$ | net contrast |
|---|---|---|---|
| 16.000 | 0.03125 | 0.9519 | 0.6060 |
| 8.400 | 0.05952 | 0.9083 | 0.5783 |
| 4.000 | 0.12500 | 0.8075 | 0.5141 |
| 2.000 | 0.25000 | 0.6150 | 0.3915 |
| 1.879 | 0.26610 | 0.5902 | 0.3757 |
| 1.000 | 0.50000 | 0.2300 | 0.1464 |

Read the table twice. **Coarser pixels keep more contrast at their Nyquist
frequency** (0.6060 at $16\ \mathrm{m}$ against 0.1464 at $1\ \mathrm{m}$), but
their Nyquist frequency is lower, so the finest recoverable scale, $2w$, is
worse. Resolution and contrast are different quantities, and quoting one without
the other is the ambiguity that the single word "resolution" conceals.

### 3.5 Spectral resolution

A grating with groove spacing $d$ disperses order $m$ according to

$$m\lambda = d\left(\sin\theta_i + \sin\theta_m\right).$$

The diffraction-limited resolving power of a grating illuminated across $N$
grooves is

$$R = \frac{\lambda}{\Delta\lambda} = mN .$$

*Numerical check.* $d = 10.00\ \mathrm{\mu m}$ (100 lines/mm), illuminated width
$0.20\ \mathrm{m}$, so $N = 0.20/10^{-5} = 20\,000$ grooves. At $m = 1$,
$R = 20\,000$, and at $\lambda = 0.55\ \mathrm{\mu m}$,

$$\Delta\lambda = \frac{\lambda}{R} = \frac{0.550}{20\,000}
= 2.750\times10^{-5}\ \mathrm{\mu m} = 0.027500\ \mathrm{nm}.$$

That is the *diffraction-limited* value. A finite slit or detector element usually
sets a coarser achieved resolution, and the achieved value is what should be
quoted.

The **spectral sampling ratio** is the band full width at half maximum divided by
the band spacing. Contiguous sampling (ratio $1$) tiles the spectrum;
oversampling (ratio $<1$) leaves redundancy used for noise reduction;
undersampling (ratio $>1$) means adjacent measurements are correlated, which
changes what a band ratio or an unmixing model means
(see [17-02-02](../02-optical-and-thermal-remote-sensing/02-hyperspectral.md)).

### 3.6 Temporal resolution

Consider one satellite in a near-polar orbit, imaging a single swath of width $W$
with no pointing. Per orbit it covers a fraction $W/(2\pi R_E)$ of an equatorial
circle; with $N$ orbits per day the circle is completed in

$$T_r = \frac{2\pi R_E}{N W}\ \text{days},
\qquad
T_r^{\rm const} = \frac{T_r}{N_{\rm sat}} .$$

*Numerical check.* $R_E = 6371\ \mathrm{km}$, $N = 14.3$ orbits/day:

| swath $W$ (km) | $T_r$ (days) | with 3 satellites (days) |
|---|---|---|
| 50 | 55.99 | 18.66 |
| 100 | 27.99 | 9.33 |
| 290 | 9.65 | 3.22 |
| 1000 | 2.80 | 0.93 |
| 2900 | 0.97 | 0.32 |

The $100\ \mathrm{km}$ swath needs $28$ days for an equatorial revisit; the
$2900\ \mathrm{km}$ swath covers it in under a day. **Spatial sampling and
temporal sampling are the same budget seen from two sides.** The formula is an
idealised geometric bound: swath overlap at high latitude, Earth rotation,
off-nadir pointing, daylight-only operation and cloud all make the achieved
revisit worse, and the $\sec^{2}\phi$ pixel growth of Section 3.1 makes a
pointed revisit radiometrically different from a nadir one.

### 3.7 Radiometric resolution and mixed pixels

A quantiser with $b$ bits and full-scale radiance $L_{\max}$ has

$$q = \frac{L_{\max}}{2^{b}},\qquad
\sigma_q = \frac{q}{\sqrt{12}}\ \text{(uniform quantisation noise)},$$

and a signal-to-noise ratio at full scale $\mathrm{SNR} = L_{\max}/\mathrm{NE}\Delta L$
for a detector noise-equivalent radiance $\mathrm{NE}\Delta L$.

*Numerical check.* $L_{\max} = 5.0\times10^{7}$,
$\mathrm{NE}\Delta L = 2.0\times10^{4}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$,
$b = 12$: $q = 1.221\times10^{4}$, $\sigma_q = 3.53\times10^{3}$, so
$\sigma_q/\mathrm{NE}\Delta L = 0.176$ — **the quantiser is not the limit; the
detector is.**

Converting a radiance resolution to a temperature resolution uses the Planck
sensitivity. For $L = \varepsilon B_\lambda(T)$ in the Wien limit,

$$\frac{\mathrm{d}L}{\mathrm{d}T} = L\frac{hc}{\lambda k_B T^{2}},
\qquad
\mathrm{NE}\Delta T = \frac{\mathrm{NE}\Delta L}{\mathrm{d}L/\mathrm{d}T}.$$

*Numerical check.* At $\lambda = 10.8\ \mathrm{\mu m}$, $T = 300\ \mathrm{K}$,
$L = 9.6694\times10^{6}$:

$$\frac{hc}{\lambda k_B T^{2}} = \frac{1}{67.56} = 1.4801\times10^{-2}\
\mathrm{K^{-1}},$$
$$\frac{\mathrm{d}L}{\mathrm{d}T} = 9.6694\times10^{6}\times1.4801\times10^{-2}
= 1.4313\times10^{5}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}\,K^{-1}},$$
$$\mathrm{NE}\Delta T = \frac{2.0\times10^{4}}{1.4313\times10^{5}}
= 0.1397\ \mathrm{K}.$$

For **mixed pixels**, a pixel containing a fraction $f$ of a target at $T_{\rm hot}$
and $(1-f)$ of background at $T_{\rm bg}$ has

$$L_{\rm pix} = fL_{\rm hot} + (1-f)L_{\rm bg}
\;\Longrightarrow\;
\frac{\Delta L}{\mathrm{NE}\Delta L}
= \frac{f\left(L_{\rm hot}-L_{\rm bg}\right)}{\mathrm{NE}\Delta L}.$$

The smallest detectable fraction is therefore

$$f_{\min} = \frac{\mathrm{NE}\Delta L}{L_{\rm hot}-L_{\rm bg}}.$$

*Numerical check.* $T_{\rm hot} = 360\ \mathrm{K}$, $T_{\rm bg} = 300\ \mathrm{K}$ at
$10.8\ \mathrm{\mu m}$: $L_{\rm hot} = 2.0537\times10^{7}$,
$L_{\rm bg} = 9.6694\times10^{6}$, so

$$f_{\min} = \frac{2.0\times10^{4}}{1.0868\times10^{7}} = 1.84\times10^{-3},$$

i.e. about $0.18\%$ of a pixel at a $1\sigma$ detection. In the demonstration's
table a $1\%$ cover gives $5.43\sigma$ and a $10\%$ cover $54.3\sigma$.

## 4. Physical interpretation

- **A quoted GSD is a sampling interval at nadir.** Off-nadir it grows as
  $\sec^{2}\phi$, and if the aperture cannot deliver that scale, the effective
  resolution is worse than the number on the datasheet.
- **The trade is arithmetic.** Signal per pixel $\propto \mathrm{GSD}^{2}\times
  \Delta\lambda$ at fixed aperture and integration time. The demonstration's
  relative signals are $1.000$, $0.250$, $0.500$, $0.125$ and $8.000$ for five
  synthetic designs — a factor-8 range from choices alone.
- **Nyquist is a criterion, not a target.** A design may legitimately undersample
  if the optics attenuate the excluded detail; the risk is that a high-contrast
  scene (a shoreline, a road grid) contains content the MTF did not remove.
- **NEΔT is the resolution in the units of the answer.** $0.1397\ \mathrm{K}$ at
  $10.8\ \mathrm{\mu m}$ for this synthetic design is the radiometric resolution
  that matters to a thermal study, not the bit depth.
- **A single band cannot separate small-and-hot from large-and-warm.** This is a
  genuine non-uniqueness: $f$ and $T_{\rm hot}$ trade in one equation. The
  demonstration holds the pixel radiance fixed and finds that
  $f = 0.01$ with $T = 509.49\ \mathrm{K}$, $f = 0.10$ with $T = 332.94\
  \mathrm{K}$ and $f = 0.50$ with $T = 307.28\ \mathrm{K}$ all produce the same
  measurement. Two bands, or a known target size, are required, and even then the
  problem is underdetermined (the subject of
  [17-02-02](../02-optical-and-thermal-remote-sensing/02-hyperspectral.md) and
  [18-inverse-problems](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md)
  in general).

## 5. Assumptions and regime of validity

1. **Flat Earth and small angles** for $\mathrm{GSD} = H\theta$ and the
   $\sec^{2}\phi$ growth. Earth curvature matters for wide swaths and large
   off-nadir angles.
2. **Nadir viewing for the nominal GSD.** A single GSD cannot describe a
   scanning instrument's full field.
3. **A cut-off-limited optics MTF** as an approximation to the true diffraction
   MTF of an obscured circular aperture. Real systems have central obscurations,
   aberrations and pointing jitter; the product rule still applies, but the
   factors differ.
4. **A rectangular detector for $\operatorname{sinc}(fw)$.** Real detector
   responses are close to this; crosstalk and diffusion in the focal plane add
   further factors.
5. **No atmospheric blur** in the MTF. The atmosphere adds a factor that depends
   on the path and on the target contrast; see
   [17-01-03](03-atmospheric-effects.md).
6. **Diffraction-limited spectral resolution** for $R = mN$. The achieved value
   is usually slit- or detector-limited.
7. **Idealised orbit geometry** for the revisit formula, as stated in Section 3.6.
8. **Uncorrelated detector noise and uniform quantisation** for the NEΔL and
   $\sigma_q$ relations. Correlated noise (striping, 1/f) changes both.
9. **A two-component linear mixture** for the fractional-cover relation. Real
   pixels mix many materials, and multiple scattering makes the mixture non-linear.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $\mathrm{GSD} = H\theta$ | $\mathrm{m}\cdot\mathrm{rad}$ | m |
| $d_A = 1.22\lambda H/D$ | $\mathrm{m}\cdot\mathrm{m}/\mathrm{m}$ | m |
| $f_c = D/(\lambda H)$ | $\mathrm{m}/(\mathrm{m}\cdot\mathrm{m})$ | cycles m⁻¹ |
| $f_N = 1/(2w)$ | $1/\mathrm{m}$ | cycles m⁻¹ |
| $R = mN$ | dimensionless count | dimensionless |
| $T_r = 2\pi R_E/(NW)$ | $\mathrm{m}/(\mathrm{m}\cdot\mathrm{m})$ | days after conversion |
| $q = L_{\max}/2^{b}$ | radiance/1 | radiance |
| $\mathrm{NE}\Delta T = \mathrm{NE}\Delta L/(\mathrm{d}L/\mathrm{d}T)$ | $\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}/(\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}\,K^{-1}})$ | K |

The revisit row is the one that needs care: $2\pi R_E$ is a length, $N$ has
units day⁻¹ and $W$ is a length, so the expression has units of days directly —
provided $N$ is per day rather than per second. Mixing orbit period and orbit
rate is the usual source of a factor of $\sim14$ error.

## 7. Worked examples

### Example 1 — is the thermal band aperture-limited?

At $\lambda = 10.8\ \mathrm{\mu m}$, $H = 700\ \mathrm{km}$,
$D = 0.30\ \mathrm{m}$:

1. $d_A = 1.22\times10.8\times10^{-6}\times7.0\times10^{5}/0.30
   = 30.744\ \mathrm{m}$.
2. GSD $= 7.00\ \mathrm{m}$, so $\mathrm{GSD}/d_A = 0.228$.
3. Conclusion: the nominal GSD overstates the achievable resolution by
   $4.4\times$. Either the thermal band is delivered at a coarser GSD (the
   usual engineering answer), or the aperture is enlarged.

### Example 2 — radiometric resolution to temperature resolution

Given $\mathrm{NE}\Delta L = 2.0\times10^{4}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$
at $10.8\ \mathrm{\mu m}$, $T = 300\ \mathrm{K}$:

1. $L = B_\lambda(300) = 9.6694\times10^{6}$ (with $\varepsilon = 1$).
2. $hc/(\lambda k_BT^{2}) = 1.4801\times10^{-2}\ \mathrm{K^{-1}}$.
3. $\mathrm{d}L/\mathrm{d}T = 1.4313\times10^{5}$.
4. $\mathrm{NE}\Delta T = 2.0\times10^{4}/1.4313\times10^{5} = 0.1397\ \mathrm{K}$.

Note the scaling with temperature: $\mathrm{d}L/\mathrm{d}T$ grows steeply with
$T$ in this band, so the *same* instrument achieves a better NEΔT over a hot
target than over a cold one. NEΔT is a function of the scene, not only of the
instrument.

### Example 3 — revisit versus swath

For $W = 100\ \mathrm{km}$ and $N = 14.3$ orbits/day:

$$T_r = \frac{2\pi\times6371\ \mathrm{km}}{14.3\times100\ \mathrm{km}}
= \frac{40030}{1430} = 27.99\ \mathrm{days}.$$

Three satellites reduce this to $27.99/3 = 9.33$ days. To reach a $1$-day
equatorial revisit with one satellite the swath would need to be
$40030/14.3 = 2800\ \mathrm{km}$, which is why wide-swath radiometers are the
revisit instruments and narrow-swath imagers are the detail instruments.

### Example 4 — the smallest detectable hot fraction

For $T_{\rm hot} = 360\ \mathrm{K}$, $T_{\rm bg} = 300\ \mathrm{K}$,
$\mathrm{NE}\Delta L = 2.0\times10^{4}$:

$$f_{\min} = \frac{2.0\times10^{4}}{2.0537\times10^{7} - 9.6694\times10^{6}}
= \frac{2.0\times10^{4}}{1.0868\times10^{7}} = 1.84\times10^{-3}.$$

At $7.00\ \mathrm{m}$ GSD the pixel area is $49\ \mathrm{m^{2}}$, so
$f_{\min}$ corresponds to $0.090\ \mathrm{m^{2}}$ of the $360\ \mathrm{K}$ target
— about a third of a square metre. The arithmetic is right, but the
interpretation must be guarded: at that scale the two-component mixture model and
the assumption of an isothermal target both fail, so the number is a *detection
threshold* for the model, not a claim that a $0.09\ \mathrm{m^{2}}$ fire can be
mapped. **The model's non-uniqueness is the point: $f$ and $T_{\rm hot}$ are not
separately determined by one band.**

## 8. Python demonstration

`code/resolution_concepts_demo.py` prints, with units:

1. GSD $7.000\ \mathrm{m}$ and pitch $8.400\ \mathrm{m}$ (Nyquist
   $0.05952\ \mathrm{cycles\,m^{-1}}$);
2. Airy spots from $1.281$ to $30.744\ \mathrm{m}$ and the GSD/spot ratios;
3. $f_c/f_N$ from $16.00$ (aliased) to $0.67$ (compliant), band by band;
4. net contrast at each design's own Nyquist frequency, $0.6060$ down to
   $0.1464$;
5. grating $R = 20\,000$ and $\Delta\lambda = 0.027500\ \mathrm{nm}$;
6. the spectral sampling table;
7. revisit times $55.99$ to $0.97$ days and the constellation variants;
8. quantisation step, SNR $2500$ and $\mathrm{NE}\Delta T = 0.1397\ \mathrm{K}$;
9. the spatial/spectral/radiometric signal trade;
10. the mixed-pixel table and $f_{\min} = 0.00184$;
11. the one-parameter null space of the single-band mixture, from
    $f = 0.01 \to T = 509.492\ \mathrm{K}$ to
    $f = 0.50 \to T = 307.279\ \mathrm{K}$ at the same measured radiance.

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-resolution-concepts-exercises.md`](./exercises/04-resolution-concepts-exercises.md)
and
[`exercises/04-resolution-concepts-solutions.md`](./exercises/04-resolution-concepts-solutions.md).

- **★** Compute the GSD for $H = 600\ \mathrm{km}$ and
  $\theta_{\rm IFOV} = 15\ \mathrm{\mu rad}$, and its value at $45°$ off-nadir.
- **★** Compute $f_N$ for a $5\ \mathrm{m}$ pitch and state the smallest
  representable wavelength.
- **★★** Find the detector pitch that makes $f_c = f_N$ at
  $\lambda = 0.66\ \mathrm{\mu m}$, $D = 0.30\ \mathrm{m}$, $H = 700\ \mathrm{km}$.
- **★★** Compute NEΔT at $320\ \mathrm{K}$ and compare with the value at
  $300\ \mathrm{K}$; explain the direction of the change.
- **★★★** Show that one band cannot determine both $f$ and $T_{\rm hot}$,
  parametrise the null space, and state what a second band adds.

## Mastery checkpoint

Without notes: $H = 650\ \mathrm{km}$, $D = 0.25\ \mathrm{m}$,
IFOV $= 12\ \mathrm{\mu rad}$, pitch $= 15\ \mathrm{\mu rad}$,
$\lambda = 0.66\ \mathrm{\mu m}$. **(a)** Compute the GSD. **(b)** Compute the
Airy spot on the ground and say whether the design is aperture-limited. **(c)**
Compute $f_N$ and $f_c$ and decide whether the band is aliased. **(d)** Compute the
equatorial revisit for a $200\ \mathrm{km}$ swath with $14.3$ orbits per day.

## 10. Common pitfalls

1. **Treating GSD as resolution.** The aperture, the atmosphere and the MTF all
   intervene; here the thermal GSD is $4.4\times$ finer than the Airy spot.
2. **Quoting a single GSD for a scanning instrument.** Off-nadir pixels are wider
   by $\sec^{2}\phi$.
3. **Ignoring sampling.** A $13\times$ mismatch between cut-off and Nyquist is an
   aliasing risk, masked here only by the optics.
4. **Reporting bit depth as radiometric resolution.** The quantiser here is
   $5.7\times$ finer than the detector noise, so it is not the limit.
5. **Comparing NEΔT between scenes.** It depends on target temperature through
   $\mathrm{d}L/\mathrm{d}T$.
6. **Reading a revisit time as a guarantee.** Clouds, pointing, daylight and
   latitude all intervene; the formula is a geometric bound.
7. **Inverting a mixed pixel with one band.** $f$ and $T_{\rm hot}$ are not
   separately identifiable without a second measurement or a size constraint.

## 11. Real-world applications

- **Sensor design.** The four resolutions are the design variables, and the
  trade in Section 4 is why no single instrument is best at everything.
- **Thermal anomaly detection.** $f_{\min}$ is the quantity that decides whether a
  small hot feature is detectable, which is central to geothermal and volcanic
  monitoring ([17-08-02](../08-remote-sensing-applications-geophysics/02-geothermal-rs.md)).
- **Time-series analysis.** Revisit time and consistent geometry are prerequisites
  for the trend detection of
  [17-02-05](../02-optical-and-thermal-remote-sensing/05-change-detection.md).
- **Resampling and GIS.** Merging layers of different GSD is a resampling problem
  with its own MTF, treated in
  [17-05-03](../05-gis-fundamentals/03-raster-data-model.md).
- **Uncertainty reporting.** A reflectance or temperature product without a
  stated resolution and NEΔT cannot be compared with another product; the
  numbers in Sections 3.4 and 3.7 are what such a statement requires.

## 12. Further reading

- *Physical Principles of Remote Sensing* (Rees) — imaging geometry, the MTF and
  radiometric resolution in one treatment.
- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — instrument
  design trade-offs in an applied context.
- [20-01-05 Sampling, Nyquist and Reconstruction](../../20-signal-processing/01-signals-and-systems/05-sampling-theory.md)
  — the sampling theorem and aliasing.
- [02-10-02 Interference and Diffraction in Optical Instruments](../../02-physics/10-optics-and-photometry/02-interference-diffraction-optics.md)
  — the Airy pattern and the grating equation.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 The Electromagnetic Spectrum and Sensing Windows](01-em-spectrum-remote-sensing.md) —
  the wavelengths and radiance units.
- [03 Atmospheric Attenuation, Scattering and Correction](03-atmospheric-effects.md) —
  a further MTF and radiance term the instrument must live with.
- [17-02-01 Multispectral Imaging, Band Ratios and Indices](../02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md) —
  what band width and band placement buy.
- [17-05-03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md) —
  handling grids of unequal GSD in practice.

## 14. Self-assessment checklist

- [ ] I can compute a GSD and its off-nadir growth.
- [ ] I can compute an Airy spot and decide if a design is aperture-limited.
- [ ] I can apply the Nyquist criterion and identify an aliased band.
- [ ] I can compute a grating resolving power and its bandwidth.
- [ ] I can compute an equatorial revisit time and a constellation variant.
- [ ] I can convert NEΔL to NEΔT and say how it varies with scene temperature.
- [ ] I can explain why one band cannot separate fractional cover from target temperature.
