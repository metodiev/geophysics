---
id: 10-01-03
title: "Attenuation, Penetration Depth and Frequency Trade-Offs"
level: advanced
prereqs: ["10-01-01", "10-01-02"]
tags: [gpr, near-surface, gpr-principles, attenuation, penetration, quality-factor, dynamic-range]
---

# Attenuation, Penetration Depth and Frequency Trade-Offs

> **All models and data in this module are SYNTHETIC.** The conductivities,
> quality factors, reflection coefficient, noise level and detectability
> threshold used below are chosen model parameters, labelled where they appear.
> No field site, instrument or measured attenuation is involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the conduction attenuation constant $\alpha$ in
   $\mathrm{m^{-1}}$ and in $\mathrm{dB\,m^{-1}}$, and the two-way depth at which
   the amplitude falls to $1/e$.
2. **Explain** why conduction loss in the low-loss regime is *frequency
   independent*, and therefore why the frequency dependence of penetration needs
   a second mechanism.
3. **Model** an additional loss with a quality factor $Q$, and **derive**
   $\alpha_Q = \pi f/(vQ)$.
4. **Build** a full two-way amplitude budget — spreading, reflection,
   transmission and attenuation — and **solve** for the depth at which a stated
   dynamic range is exhausted.
5. **Derive** the spectral-ratio estimator for $\alpha$ and $Q$ from two
   reflections, and **state** its fitting band and its assumptions.
6. **Test** the spectral-centroid estimator in its own first-order regime, and
   **explain** when it fails.
7. **Compare** two independent estimates of $\alpha$ and **decide** which one
   measures the quantity you want.

## Prerequisites

- [01 GPR Physics](01-gpr-physics.md) — Maxwell's equations in a lossy
  dielectric, the loss tangent and the low-loss attenuation (3.3).
- [02 Velocity Estimation and Depth Conversion in GPR](02-gpr-velocity-and-depth.md) —
  depth conversion, which every penetration estimate depends on.

## 1. The conduction attenuation constant

From the low-loss expansion of the exact dispersion relation,

$$\alpha_{\mathrm{cond}} = \frac{\sigma}{2}\sqrt{\frac{\mu_0}{\varepsilon}}
= \frac{\sigma\,\eta_0}{2\sqrt{\varepsilon_r}}, \qquad
\eta_0 = 376.73\ \Omega. \tag{1.1}$$

Field amplitude decays as $\exp(-\alpha z)$ over a one-way distance $z$, so the
two-way amplitude decays as $\exp(-2\alpha d)$ with $d$ the reflector depth. The
conversions used throughout this module are

$$\frac{\alpha}{1\ \mathrm{m^{-1}}}
\times 8.686 = \frac{\alpha}{\mathrm{dB\,m^{-1}}},
\qquad
\delta_{\mathrm{skin}} = \frac{1}{\alpha},
\qquad
d_{1/e,\ \mathrm{two\ way}} = \frac{1}{2\alpha}. \tag{1.2}$$

**Worked example 1.** For a wet sand with $\sigma =
1\times10^{-3}\ \mathrm{S\,m^{-1}}$ and $\varepsilon_r = 16$:

$$\alpha = \frac{1\times10^{-3}}{2}\sqrt{\frac{1.2566\times10^{-6}}
{1.4166\times10^{-10}}} = 4.709\times10^{-2}\ \mathrm{m^{-1}},$$

or $8.686 \times 4.709\times10^{-2} = 0.409\ \mathrm{dB\,m^{-1}}$, with a skin
depth of $21.24\ \mathrm{m}$ and a two-way $1/e$ depth of $10.62\ \mathrm{m}$.
The two-way losses are then $0.41\ \mathrm{dB}$ at $0.5\ \mathrm{m}$,
$0.82\ \mathrm{dB}$ at $1.0\ \mathrm{m}$, $1.64\ \mathrm{dB}$ at $2.0\
\mathrm{m}$ and $3.27\ \mathrm{dB}$ at $4.0\ \mathrm{m}$.

Now change the conductivity by two orders. A clay-rich soil at
$\sigma = 0.1\ \mathrm{S\,m^{-1}}$ loses that same $3.3\ \mathrm{dB}$ in
$0.040\ \mathrm{m}$ instead of $4.0\ \mathrm{m}$ — a hundred times shallower. In
one sentence: **at fixed permittivity the penetration depth scales as
$1/\sigma$**, which is why GPR works in sand and dies in clay.

## 2. The frequency paradox of conduction loss

Equation (1.1) contains no frequency. Conduction loss in the low-loss regime is
**broadband**: doubling the antenna frequency barely changes how fast a wave is
absorbed. This is not what most GPR practitioners expect, and it is worth
stating as a theorem rather than an observation, because the opposite belief
leads to bad survey design.

So where does the familiar "lower frequency goes deeper" rule come from? Three
mechanisms, all of which are *not* conduction:

- **Relaxation loss.** Water molecules cannot follow the field at high frequency;
  the imaginary part of the permittivity grows with $f$ over a broad band and
  vanishes at low $f$. This is the dominant loss in wet, low-salinity ground.
- **Scattering loss.** Heterogeneity at a scale comparable with the wavelength
  removes energy from the coherent field. It grows rapidly with $f$.
- **Radiated, not absorbed.** A higher-frequency antenna has a smaller aperture
  and couples differently to the ground; some of the "penetration" difference is
  a source-strength difference, not an attenuation difference.

The honest way to model the first of these without inventing a site-specific
relaxation spectrum is a **constant-$Q$** loss:

$$\alpha_Q = \frac{\pi f}{v\,Q}, \tag{2.1}$$

which follows from the definition of $Q$ as the inverse fractional energy loss
per radian, $1/Q = -\Delta E/(2\pi E)$ per cycle, applied to a wave of speed
$v$. $Q$ is a *chosen model parameter* in this module, not a measured value. The
total attenuation is then

$$\alpha(f) = \alpha_{\mathrm{cond}} + \frac{\pi f}{v Q}. \tag{2.2}$$

**Worked example 2.** With $v = 0.07495\ \mathrm{m\,ns^{-1}}$,
$\alpha_{\mathrm{cond}} = 0.0471\ \mathrm{m^{-1}}$ and $Q = 12$:

| $f$ (MHz) | $\lambda$ (m) | $\alpha_{\mathrm{cond}}$ | $\alpha_Q$ | $\alpha$ total | dB/m |
|---|---|---|---|---|---|
| 50 | 1.499 | 0.0471 | 0.1747 | 0.2217 | 1.93 |
| 100 | 0.749 | 0.0471 | 0.3493 | 0.3964 | 3.44 |
| 200 | 0.375 | 0.0471 | 0.6986 | 0.7457 | 6.48 |
| 400 | 0.187 | 0.0471 | 1.3972 | 1.4443 | 12.55 |
| 900 | 0.083 | 0.0471 | 3.1438 | 3.1909 | 27.72 |

Note the structure: at 50 MHz with $Q=12$ the conduction term is only $21\%$ of
the total, so frequency is the dominant lever; at $Q = 30$ it is $40\%$ of the
total already at 50 MHz, so dropping to 25 MHz buys far less than the factor of
two that the $Q$ term alone would suggest. The saturation of the gain is the
practical content of this section.

## 3. Penetration depth from a dynamic-range budget

"Penetration" is not a property of the ground alone: it is where the received
amplitude crosses the system's noise floor. A defensible budget is

$$\frac{A(d)}{A_{\mathrm{ref}}}
= \underbrace{R}_{\text{reflection}}
\;\underbrace{\frac{r_{\mathrm{ref}}}{2d}}_{\text{spreading}}
\;\underbrace{e^{-2\alpha d}}_{\text{attenuation}}, \tag{3.1}$$

in dB,

$$20\log_{10}\frac{A}{A_{\mathrm{ref}}}
= 20\log_{10}R - 20\log_{10}\!\left(\frac{2d}{r_{\mathrm{ref}}}\right)
- 8.686 \times 2\alpha d. \tag{3.2}$$

Three assumptions are packed into (3.1) and each must be stated when a number is
quoted: the reflector is specular and larger than the Fresnel zone; the far-field
dipole field decays as $1/r$ (so the round-trip amplitude as $1/(2d)$ with
$r_{\mathrm{ref}} = 1\ \mathrm{m}$); and no transmission losses from overlying
interfaces are included.

**Worked example 3.** With $|R| = 0.2$ ($-13.98\ \mathrm{dB}$), $f = 200\
\mathrm{MHz}$, $Q = 12$, $\sigma = 1\times10^{-3}\ \mathrm{S\,m^{-1}}$ and a
chosen detectability threshold of $-80\ \mathrm{dB}$:

| $d$ (m) | reflection (dB) | spreading (dB) | attenuation (dB) | total (dB) |
|---|---|---|---|---|
| 0.5 | $-13.98$ | $0.00$ | $6.48$ | $-20.46$ |
| 1.0 | $-13.98$ | $-6.02$ | $12.95$ | $-32.95$ |
| 2.0 | $-13.98$ | $-12.04$ | $25.91$ | $-51.93$ |
| 3.0 | $-13.98$ | $-15.56$ | $38.86$ | $-68.41$ |
| 4.0 | $-13.98$ | $-18.06$ | $51.82$ | $-83.86$ |

Solving (3.2) for the crossing gives $d = 3.746\ \mathrm{m}$, where the budget is
$-13.98\ \mathrm{dB}$ reflection, $-17.49\ \mathrm{dB}$ spreading and
$-48.53\ \mathrm{dB}$ attenuation. **Attenuation is the largest term by a factor
of three**, and it grows linearly with depth while spreading grows
logarithmically: beyond about $2\ \mathrm{m}$ in this medium the question "how
deep can we see" has the answer "as far as the absorption allows", and no
increase in source power or stacking changes the exponent.

## 4. Measuring $\alpha$ and $Q$ from two reflections

If two reflections from different depths share a reflection coefficient — or if
their ratio is otherwise known — their spectra differ only by attenuation:

$$\ln\frac{A_1(f)}{A_2(f)} = 2\alpha(f)\,(d_2 - d_1). \tag{4.1}$$

Substituting (2.2) makes the right side linear in $f$:

$$\ln\frac{A_1}{A_2} = \underbrace{2\alpha_{\mathrm{cond}}\,\Delta d}
_{\text{intercept}} + \underbrace{\frac{2\pi\Delta d}{v Q}}_{
\text{slope}} f, \qquad \Delta d = d_2 - d_1. \tag{4.2}$$

So a single straight-line fit separates the two mechanisms: the intercept gives
the frequency-independent conduction loss and the slope gives $Q$,

$$\alpha_{\mathrm{cond}} = \frac{\text{intercept}}{2\Delta d},
\qquad
Q = \frac{2\pi\Delta d}{v \times \text{slope}}. \tag{4.3}$$

Two practical requirements follow from (4.2) and are easy to get wrong:

- The **fitting band** must be restricted to frequencies where both spectra are
  above the noise. In the demonstration the noise is a chosen $1\times10^{-4}$ of
  the source peak and the band where both spectra exceed ten times the noise is
  $9.8$–$327.1\ \mathrm{MHz}$, 65 bins out of 2049. Fitting the whole band would
  fit noise.
- The estimator needs a *frequency-dependent* loss to have anything to fit. With
  conduction loss alone the true slope is zero and $Q$ is undefined — a fact that
  is easy to lose behind a fitted number.

**Worked example 4.** Two synthetic reflectors at $0.50\ \mathrm{m}$ and
$2.50\ \mathrm{m}$ through the medium of Example 2, with $Q = 12$ and
$\alpha_{\mathrm{cond}} = 0.0471\ \mathrm{m^{-1}}$: the fit returns intercept
$0.1925$ and slope $1.39342\times10^{-8}\ \mathrm{s}$, giving

$$\alpha_{\mathrm{cond}} = \frac{0.1925}{2\times2.0} = 0.0481\ \mathrm{m^{-1}}
\quad (+2.19\%), \qquad
Q = 12.033 \quad (+0.27\%).$$

Both mechanisms are recovered from one line because they have different frequency
signatures.

## 5. The spectral-centroid estimator, and its regime of validity

A second, cheaper estimator uses the **downshift of the spectral centroid**. For
a small loss, expanding the attenuated spectrum in the loss gives, to first order,

$$f_{c,2} - f_{c,1} \approx -\frac{\pi\,t_{\mathrm{eff}}}{Q}
\operatorname{var}(f), \qquad
t_{\mathrm{eff}} = \frac{2\Delta d}{v}, \tag{5.1}$$

where $\operatorname{var}(f)$ is the variance of the *reference* spectrum about
its own centroid. Rearranged:

$$Q = \frac{\pi\,t_{\mathrm{eff}}\operatorname{var}(f)}{f_{c,1}-f_{c,2}}.
\tag{5.2}$$

Equation (5.1) is a first-order relation, so it assumes the loss removes only a
small part of the band, and (5.2) requires the variance of the reference
spectrum, which is itself a measurement.

**Worked example 5.** With $Q = 60$ (chosen weak attenuation), reflectors at
$0.50$ and $1.00\ \mathrm{m}$ so $t_{\mathrm{eff}} = 13.34\ \mathrm{ns}$, and the
centroid measured over the source passband: $f_{c,1} = 219.395\ \mathrm{MHz}$,
$f_{c,2} = 213.390\ \mathrm{MHz}$, a downshift of $6.004\ \mathrm{MHz}$ or
$2.737\%$, with a reference rms bandwidth of $93.595\ \mathrm{MHz}$. Then

$$Q = \frac{\pi \times 13.34 \times 10^{-9} \times
\left(93.595\times10^{6}\right)^{2}}{6.004\times10^{6}} = 61.15 \quad
(+1.92\%).$$

Applied instead to the strongly attenuating pair of Example 4, the same formula
returns a value far from the model $Q$: the first-order expansion has failed.
**A Q estimate obtained from a spectral centroid should always be accompanied by
the fractional loss it presupposes**; if the loss over the path removes more than
a few decibels, use the spectral ratio.

## 6. Assumptions and regime of validity

1. **Low loss**, $\tan\delta = \sigma/(\omega\varepsilon) \lesssim 0.1$; above
   this both (1.1) and the frequency-independence of $\alpha_{\mathrm{cond}}$
   degrade (see [01 GPR Physics](01-gpr-physics.md) §4).
2. **Constant $Q$ over the band.** Real relaxation loss is frequency dependent;
   a constant $Q$ is an average and is a chosen model parameter here.
3. **Two reflections with a known amplitude relation.** Unknown reflection or
   transmission coefficients propagate straight into $\alpha$.
4. **No geometric-spreading difference.** A deeper reflector is further away, so
   the spectral ratio must correct for spreading before it can be attributed to
   absorption — the demonstration isolates the effect by construction, and a real
   analysis may not be able to.
5. **Single scattering.** Where multiples are strong the deeper event is not a
   single-path arrival and (4.1) fails.
6. **The pulse is not distorted by the instrument.** Filtering or AGC applied
   before the spectral ratio changes the spectrum being fitted.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $\alpha$ | $\mathrm{m^{-1}}$ (nepers/m) | $\sigma\eta_0/(2\sqrt{\varepsilon_r})$ |
| $\alpha$ | $\mathrm{dB\,m^{-1}}$ | $8.686\,\alpha$ |
| skin depth | m | $1/\alpha$ |
| two-way loss | dB | $8.686 \times 2\alpha d$ |
| $Q$ | 1 | $\pi f/(v\alpha_Q)$ |
| spectral slope | s | $2\pi\Delta d/(vQ)$ |

Two traps: nepers and decibels differ by $8.686$ (not $20$), and "attenuation in
dB per metre" is ambiguous unless it is stated whether it is one-way or two-way.
Every number in this lesson is labelled.

## 8. Python demonstration

`code/gpr_attenuation_penetration_demo.py` prints all of the above. It:

1. tabulates $\alpha$, $\mathrm{dB\,m^{-1}}$, skin depth and two-way $1/e$ depth
   for four conductivities and three permittivities;
2. tabulates two-way loss in dB against depth, and shows the factor-100
   difference between a sand and a clay at the same loss level;
3. builds $\alpha(f)$ from (2.2) and solves for the 60 dB penetration depth at
   five frequencies and two $Q$ values, reporting how much of the total is
   conduction;
4. computes a full amplitude budget, prints each term separately, and bisects for
   the depth at which the chosen threshold is crossed ($3.746\ \mathrm{m}$);
5. recovers $\alpha_{\mathrm{cond}}$ and $Q$ from a synthetic spectral ratio, with
   the fitting band reported;
6. tests the centroid estimator in its own regime and prints the recovery error;
7. cross-checks with a peak-amplitude-only estimate and shows that it is biased
   ($0.5834$ against a model value of $0.7457\ \mathrm{m^{-1}}$, $-21.8\%$ at
   $200\ \mathrm{MHz}$) because it mixes the frequency-independent and
   frequency-dependent losses.

## Mastery checkpoint

Without notes:

> A survey targets a reflector at $d = 1.5\ \mathrm{m}$ in soil with
> $\varepsilon_r = 9$, $\sigma = 4\times10^{-3}\ \mathrm{S\,m^{-1}}$, and a
> chosen $Q = 20$ at $f = 250\ \mathrm{MHz}$.
> **(a)** Compute $v$, $\alpha_{\mathrm{cond}}$, $\alpha_Q$ and the total
> $\alpha$.
> **(b)** Compute the two-way attenuation loss in dB at the reflector.
> **(c)** Decide whether the low-loss approximation is valid by computing
> $\tan\delta$.
> **(d)** Two reflections at $0.5\ \mathrm{m}$ and $1.5\ \mathrm{m}$ give a
> spectral-ratio slope; state whether the slope measures the conduction or the
> relaxation loss, and why.
> **(e)** State one reason the true penetration could be *less* than your budget
> predicts.

Parts (a)–(e) are worked in
[`exercises/03-gpr-attenuation-penetration-solutions.md`](./exercises/03-gpr-attenuation-penetration-solutions.md).

## Common pitfalls

1. **Believing that lower frequency always penetrates deeper.** Conduction loss
   is frequency independent; the frequency dependence comes from relaxation and
   scattering, and it saturates.
2. **Confusing nepers with decibels**, or one-way with two-way attenuation.
3. **Reporting a penetration depth without the detection threshold.** (3.2)
   contains a chosen number; the depth is meaningless without it.
4. **Fitting a spectral ratio over the whole band.** Beyond the noise floor the
   "fit" is a fit to noise.
5. **Using the centroid estimator on a strongly attenuating path.** Its
   first-order expansion has broken down, silently.
6. **Reading an amplitude ratio as a reflection coefficient** when the deeper
   event also suffered more spreading and more transmission loss.
7. **Assuming $Q$ is a measured property** rather than a fitted or assumed model
   parameter with its own uncertainty.

## Related modules

- [01 GPR Physics](01-gpr-physics.md) — where $\alpha$ and the loss tangent come
  from.
- [05 Vertical and Horizontal Resolution Limits](05-gpr-resolution.md) — the other
  consequence of frequency choice.
- [06-05 Attenuation and Anelasticity](../../06-seismology/05-attenuation-and-anelasticity/README.md) —
  the same spectral-ratio and centroid estimators in seismology.
- [09-07 EM Data Processing, QC and Uncertainty](../../09-electrical-em-methods/07-em-data-processing-and-qc/README.md) —
  how conductivity and permittivity estimates are made and qualified in EM.

Materials: [`code/gpr_attenuation_penetration_demo.py`](./code/gpr_attenuation_penetration_demo.py),
[`exercises/03-gpr-attenuation-penetration-exercises.md`](./exercises/03-gpr-attenuation-penetration-exercises.md),
[`exercises/03-gpr-attenuation-penetration-solutions.md`](./exercises/03-gpr-attenuation-penetration-solutions.md).
