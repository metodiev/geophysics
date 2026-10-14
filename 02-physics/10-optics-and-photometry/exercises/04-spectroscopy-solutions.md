# Solutions — 02-10-04 Spectroscopy Principles for Remote Sensing

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The demo's spectrum is synthetic: its feature
> positions are **not** measurements of any real mineral, and mineral positions
> throughout are given as ranges.

---

## ★1 — Wavelength and wavenumber

**(a)** $\tilde\nu = 1/\lambda = 1/(2.33\times10^{-6}\ \mathrm m)
= 4.2918\times10^{5}\ \mathrm{m^{-1}} = \mathbf{4291.8}$ **cm⁻¹**.

**(b)** $\lambda = 10^{4}/2200 = \mathbf{4.5455}$ **µm**.

**(c)** At 2.2 µm, $1/\lambda$ changes from $1/2.199\times10^{-6}$ to
$1/2.201\times10^{-6}$, i.e. $4547.5-4543.4 =
\mathbf{2.07}$ **cm⁻¹** per nm (computed exactly: $\Delta\tilde\nu \approx
\Delta\lambda/\lambda^2 = 10^{-9}/(2.2\times10^{-6})^2 = 206.6\ \mathrm{m^{-1}}
= 2.07$ cm⁻¹). At 0.9 µm the same 1 nm is
$\Delta\tilde\nu = 10^{-9}/(0.9\times10^{-6})^2 = 1234.6$ m⁻¹ $= \mathbf{12.3}$
**cm⁻¹** — six times larger.

**(d)** Because a spectrum is *uniformly* sampled in wavenumber by an
interferometer: the optical path difference $x$ and the wavenumber $\tilde\nu$
are conjugate variables, and a transform-limited spectrum requires uniform
sampling in one of them. Sampling uniformly in *wavelength* would give a
non-uniform wavenumber grid whose spacing changes by a factor of six across the
region of interest, so the effective resolution would vary with wavelength and
the interferogram's retrieval would require a resampling step that could have
been avoided by design.

---

## ★2 — Beer–Lambert

**(a)** $T = e^{-0.3} = \mathbf{0.740\,818}$, $A = 1-T = \mathbf{0.259\,182}$.

**(b)** $A = 1-e^{-0.6} = \mathbf{0.451\,188}$.

**(c)** $0.451\,188/0.259\,182 = \mathbf{1.7408}$, against a ratio of optical
depths of 2.000. The response is already 13 per cent sub-linear at an optical
depth of 0.3 and has lost 26 per cent of the linearity by $\tau = 0.6$: the
saturation begins much earlier than the strong-band limit of $\tau \sim 5$ might
suggest.

**(d)** The demo's table gives the depth/$\tau$ ratio: 0.975 412 at $\tau = 0.05$
and 0.198 652 at $\tau = 5$. Half of 0.975 means $\dfrac{1-e^{-\tau}}{\tau}
= 0.4877$, which is satisfied near $\tau \approx \mathbf{1.6}$; reading the table
at $\tau = 2$ gives 0.432 332 and at $\tau = 1$ gives 0.632 121, so the
interpolation brackets the answer at about $\tau = 1.6$. Beyond an optical depth
of order unity, a doubling of abundance no longer doubles the band depth.

---

## ★3 — Instrument specification

**(a)** $\mathcal{R} = \lambda/\Delta\lambda = 2200\ \mathrm{nm}/10\ \mathrm{nm}
= \mathbf{220}$.

**(b)** $\mathcal{R} = 10\,000/10 = \mathbf{1000}$ — the same bandwidth buys a
higher resolving power at longer wavelength, because resolving power is a ratio.

**(c)** $(2500-400)/10 = \mathbf{210}$ bands.

**(d)** Detecting a feature **wider than the band** is governed by the band
width: both instruments have 10 nm bands, and a 25 nm feature is 2.5 times wider
than the band, so both *detect* it — but detecting it also requires enough
signal-to-noise to see a depth that, from ★4, is reduced by the ratio of widths.
*Separating* two nearby lines is governed by the resolving power: at 2.2 µm a
10 nm band gives $\mathcal{R} = 220$ and the closest separable pair is 10 nm
apart; at 10 µm the same 10 nm band gives $\mathcal{R} = 1000$ and separates a
pair 10 nm apart as well, but those 10 nm correspond to a much smaller fractional
wavelength difference, which matters when the diagnostic is a *position* rather
than a *presence*. The two specifications therefore answer different questions:
band width sets the smallest feature you can see at all, resolving power sets the
smallest wavelength *difference* you can measure, and SNR sets the smallest
*depth* you can see. A specification that quotes only one of the three is
incomplete.

---

## ★4 — Depth loss from a wide instrument function

**(a)** $\sigma_f = 20/2.355 = \mathbf{8.4937}$ **nm**;
$\sigma_i = 30/2.355 = \mathbf{12.7406}$ **nm**.

**(b)**
$d_{\text{obs}} = 0.30\times\dfrac{8.4937}{\sqrt{8.4937^2+12.7406^2}}
= 0.30\times\dfrac{8.4937}{15.3117} = 0.30\times0.5547
= \mathbf{0.1664}$.

The approximation can be checked numerically: convolving a Gaussian dip of
$\sigma_f = 8.4937$ nm and depth 0.30 with a Gaussian of
$\sigma_i = 12.7406$ nm and measuring the depth of the result gives 0.166 419,
against the formula's 0.166 410 — agreement to $5\times10^{-5}$, so the
approximation is good to five significant figures for depths of this size. State
the approximation and its verification; do not present it as exact.

**(c)** Fractional loss $= 1-0.5547 = \mathbf{0.445}$, i.e. 45 per cent of the
depth is destroyed.

**(d)** The **position** is more robust, provided the feature is symmetric: a
symmetric convolution shifts neither the minimum of a symmetric feature nor the
position of the second-derivative maximum, so the diagnostic wavelength survives
even when the depth is halved. The *depth* is degraded by the ratio of widths,
which is why positions are used for identification (§8 of the lesson) and depths
only for semi-quantitative abundance.

---

## ★5 — Reading the demo

**(a)** The narrow feature has a true depth of **0.2892**; at 40 nm FWHM the
recovered depth is **0.2085**.

**(b)** The broad 0.90 µm feature has a true depth of **0.1743** and a recovered
depth of **0.1688** at 40 nm FWHM. The fractional losses are
$1-0.2085/0.2892 = \mathbf{0.279}$ for the narrow feature and
$1-0.1688/0.1743 = \mathbf{0.032}$ for the broad one — a factor nine difference
in sensitivity to the same instrument.

**(c)** At 10 nm sampling (grid offset by 0.37 of a step) the depth is
**0.2824** with a recovered centre of **2.2037** µm, an error of +3.7 nm. At
20 nm sampling the depth is **0.2631** with a centre of **2.2074** µm, an error
of +7.4 nm. The depth loss grows and, more seriously, the *position* moves: an
under-sampled feature is reported at the wrong wavelength, which is a
misidentification and not merely a weaker signal.

**(d)** At 50 nm sampling the sampled spectrum contains no point inside the
22 nm feature at all with the grid phase used, so the metric returns a depth of
**0.0000** at a displaced centre of **2.1685** µm. An analyst applying a
threshold test would report "no feature present" — a false negative — while an
analyst reading the depth as a real number would report a feature that is not
there. Under-sampling converts an identification into a coin flip.

---

## ★6 — A normalised difference index

**(a)** $\mathrm{IDX} = \dfrac{0.35-0.20}{0.35+0.20} = \dfrac{0.15}{0.55}
= \mathbf{0.2727}$.

**(b)** Multiplying both by 0.5 gives $\dfrac{0.175-0.10}{0.275} = 0.2727$ and
multiplying by 2 gives $\dfrac{0.70-0.40}{1.10} = 0.2727$: the index is
**invariant** to any positive multiplicative factor.

**(c)** The un-normalised differences are 0.15, 0.075 and 0.30 — they scale
linearly with the continuum, so they carry no invariant information about the
surface. This is why indices are normalised: the ratio removes a gain
(illumination, topography, atmospheric transmission in the first order) while
retaining the compositional contrast.

**(d)** It removes a *multiplicative* effect, so it is a first-order correction
for illumination and topography and for a wavelength-independent atmospheric
transmission. It does **not** remove an *additive* path radiance from the
atmosphere (aerosol scattering adds light that carries no surface information) or
a wavelength-dependent atmospheric absorption, which is why indices are computed
on atmospherically corrected surface reflectance.

---

## ★7 — Emissivity and its cost

**(a)** $\epsilon = 1-\rho = 1-0.45 = \mathbf{0.55}$.

**(b)** $F/F_{\text{blackbody}} = \epsilon = \mathbf{0.55}$, i.e. the surface
emits 55 per cent of a blackbody's flux at the same temperature (in the
broadband greybody approximation).

**(c)** $T_B = \epsilon^{1/4}T = 0.55^{0.25}\times300 = 0.8611\times300
= \mathbf{258.3}$ **K**, an error of $\mathbf{-41.7}$ **K** if the emissivity is
assumed to be 1. This is the broadband greybody limit: in a real retrieval the
correction is applied band by band, and the error at 11 µm for an emissivity error
of this size would be smaller but still tens of kelvin. The point stands: an
emissivity error is not a correction, it is a first-order term.

**(d)** The surface must be **opaque** ($\tau_{\text{surface}}\gg1$, so no
transmission term and no radiation from beneath) and **isothermal** over the
measurement footprint and over the depth probed at that wavelength. Both are
idealizations: a coating can be semi-transparent, and a pixel may contain
materials at different temperatures, in which case the Planck-weighted radiance
is not the radiance of any single temperature.

---

## ★8 — Reading the demo's reflectance-to-emissivity conversion

**(a)** At the 2.20 µm feature the model reflectance is **0.2560**, giving an
emissivity of **0.7440**; on the 2.10 µm shoulder the reflectance is **0.3606**,
giving an emissivity of **0.6394**.

**(b)** The spectral contrast is $0.6394-0.7440 = \mathbf{-0.1046}$ in
emissivity, equal in magnitude to $0.3606-0.2560 = 0.1046$ in reflectance.

**(c)** Because the conversion is $\epsilon = 1-\rho$ at each wavelength
independently, so the difference of two emissivities is the negative of the
difference of the two reflectances:
$\epsilon_b-\epsilon_a = (1-\rho_b)-(1-\rho_a) = -(\rho_b-\rho_a)$.

**(d)** A reflectance library measured in the 1.0–2.5 µm region can be converted
into an expected emissivity spectrum for the 8–14 µm region *of the same
material* (with the caveat that the transitions are different ones), and more
directly: the same vibrational information appears in both regions, so an
emissivity retrieval can be checked against a reflectance library. The
conversion fails when the surface is not opaque or not isothermal, when the
viewing geometry differs between the two measurements (the relation holds at the
same direction), or when the two spectral regions sample different transition
types with different cation substitution effects.

---

## ★★★9 — Quantitative abundance

**(a)** For a purely absorbing layer with no scattering and no emission,
$I = I_0e^{-\tau}$, so the *absorptance*
$A = 1-I/I_0 = 1-e^{-\tau}$. A reflectance band depth $D$ measured against a
fitted continuum has the same form when the surface is described by a
single-scattering, optically thin model, because in that limit the reflectance
is proportional to $\exp(-\tau_{\text{absorption}})$ along the effective path.
The two behave the same way at small $\tau$ because both expand as
$\tau-\tau^2/2+\cdots$: they share the first two terms, which is why a linear
calibration of band depth against abundance works at all, and only at small
$\tau$.

**(b)** $D = 0.5 \Rightarrow e^{-\tau} = 0.5 \Rightarrow
\tau = \ln 2 = \mathbf{0.6931}$.

**(c)** $\dfrac{\mathrm dD}{\mathrm d\tau} = e^{-\tau} = 0.5$ at that point,
against the weak-absorption limit of 1. The sensitivity has halved, which is the
precise sense in which a half-depth band is a saturated measurement: the same
change in abundance now produces half the change in depth that it would at
$\tau \to 0$.

**(d)** $D = 0.5$ tells you that the optical depth is 0.693 **if** the absorber
is the only one contributing in that window, **if** the continuum has been fitted
correctly, **if** the grain size and path length are known or constant, and
**if** the scattering contribution is negligible. It does **not** tell you the
abundance of a specific mineral, because $\tau = kcl$ depends on the absorption
coefficient $k$ (which varies with composition and grain size), on the
concentration $c$ (which for a mineral in a rock is a modal abundance, not a
number density), and on the effective path length $l$ (which depends on grain
size and packing). Converting depth into abundance requires a radiative-transfer
model and an independent constraint on the grain size.

---

## ★★★10 — Continuum choice

Using the demo's synthetic spectrum:

| Continuum window | Band depth | Recovered centre | Continuum at the minimum |
|---|---|---|---|
| 2.14–2.26 µm | **0.2892** | 2.2000 µm | 0.3602 |
| 2.10–2.33 µm | **0.2169** | 2.1990 µm | 0.3270 |
| 1.90–2.45 µm | **0.2025** | 2.2010 µm | 0.3212 |

**(d)** None of the three is "correct": each is a different model of the
background, and the depth differs by **30 per cent** between the tightest and
the widest window. What *is* robust is the **band centre**, which moves by at
most 1.1 nm across the three choices, confirming the lesson's point that position
is the diagnostic and depth is a model-dependent quantity. An author must
therefore report: the wavelength window used to fit the continuum, the functional
form of the continuum (straight line, convex hull, polynomial), and the
wavelength range over which the depth was measured. Without those three numbers a
band depth in the literature is not comparable with a band depth in your data,
and quoting one without them is quoting an uncalibrated instrument.

---

## ★★★11 — Separating abundance from mineralogy

**(a)** A single-band index measures a contrast between two wavelengths, which
depends on the product of the abundance and the absorption coefficient of
whatever is present. Two different minerals can produce the same contrast at
those two wavelengths, and a mixture of A and B can mimic a third mineral C.
Separating them requires either more bands (so that the shape of each feature
can be constrained) or an explicit mixture model with endmembers.

**(b)** A depth scales with abundance, which is a continuously variable quantity
that also depends on grain size and geometry. A **position** is set by the
energy of the transition, i.e. by the chemistry of the site: which cation
occupies which site, how the structure distorts it, and what the neighbouring
sheet is. Position is therefore a chemical identification, whereas depth is a
concentration estimate. Substitution of Al by Fe, for example, shifts the Al–OH
combination feature within its nominal range, and the position of that shift is
the compositional signal.

**(c)** Three reasons a 2 per cent residual is not proof: (i) a rock is a
*mixture*, and a single-mineral library spectrum is the wrong model — many
mixtures will fit a single spectrum to within a few per cent; (ii) the library
spectrum was measured at a different grain size and viewing geometry, and both
change the spectral shape by more than 2 per cent; (iii) the residual is
computed after a continuum removal whose choice affects the result, so a
2 per cent residual is inside the model uncertainty rather than outside it. A
mineral identification needs independent evidence — a second, independent
feature; a spatial pattern consistent with geology; or a field or drill sample.

**(d)** The four parameters are: **band count** (how many spectral channels and
over what range), **band width** (the instrument function, in nanometres),
**sampling interval** (the spacing between band centres), and **signal-to-noise
ratio per band** (which sets the smallest detectable depth). Only with all four
is a statement about detection or identification meaningful; the lesson's §4
shows that a wide band destroys depth while a coarse sampling can destroy the
feature entirely, and those are different failures with different remedies.
