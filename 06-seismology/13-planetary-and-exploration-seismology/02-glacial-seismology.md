---
id: 06-13-02
title: "Glacial and Cryoseismology: Icequakes and Calving"
level: doctoral
prereqs: ["06-01-03", "06-01-02", "06-10-04"]
tags: [seismology, cryoseismology, icequakes, calving, love-waves, dispersion, ice-thickness]
---

# Glacial and Cryoseismology: Icequakes and Calving

Ice is a seismic material with two properties that make glacial seismology a
distinct subject. It is **slow** — its shear velocity is under
$2\ \mathrm{km\,s^{-1}}$ — and it sits on a substrate that is usually faster, so
an ice body is a natural **waveguide**: surface waves are trapped in it, and
their dispersion carries a measurement of its thickness. And it is **noisy**:
ice deforms, cracks and calves, so a glacier generates its own seismicity,
continuously in places and in large discrete events in others.

The honest difficulty of the subject is a product of two quantities. A
dispersion curve constrains the layer thickness **and** its velocity, and the
two trade off: a thicker, slower layer can produce nearly the same dispersion as
a thinner, faster one. The lesson derives that trade-off, measures it on a
synthetic dispersion curve, and reports what the measurement actually says —
which, at the precision achievable over a wide band, is less ambiguous than the
textbook warning suggests, and *more* sensitive to the velocity than a naive
reading of the trade-off would predict. Understanding why those two statements
are compatible is the point of the lesson.

All models and data in this module are **SYNTHETIC**. The ice properties below
are stated model choices, not laboratory measurements, and no real glacier,
icequake or inversion result is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $V_p$ and $V_s$ from the elastic moduli of ice and **compute**
   them from a stated $(E,\nu,\rho)$.
2. **Quantify** the temperature and porosity sensitivities of $V_s$, and
   **explain** why porosity dominates at the same fractional change.
3. **Derive** the Love-wave dispersion relation for a slow layer over a fast
   half-space, and its limiting behaviour at low and high frequency.
4. **Explain** why ice over water is a different (and stronger) waveguide than
   ice over bedrock.
5. **Measure** the thickness–velocity trade-off on a synthetic dispersion curve
   and **state** the tolerance at which the family collapses.
6. **Explain** what an independent thickness measurement contributes, and why
   radar, boreholes and refraction are the usual sources of one.
7. **Describe** the source mechanisms of glacial seismicity at the level of
   what each one produces on a record, and **state** which of those statements
   are model-driven and which are qualitative background.

## Prerequisites

- [06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity](../01-elastic-wave-propagation/03-surface-waves.md) —
  the dispersion relation and the depth sensitivity of surface waves.
- [06-01-02 P and S Waves](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  the moduli-to-velocity relations used in §2.
- [06-10-04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](../10-refraction-and-near-surface-seismology/04-masw-sasw.md) —
  the practical dispersion-curve workflow.

## 1. Why ice is a seismic waveguide

Surface waves exist when a low-velocity layer overlies a higher-velocity
substrate, because energy trapped in the slow layer cannot leak downward. For a
shear velocity $\beta_1$ in a layer of thickness $H$ over a half-space with
shear velocity $\beta_2 > \beta_1$, the fundamental Love mode exists at every
frequency and its phase velocity $c$ satisfies $\beta_1 < c < \beta_2$: the
mode is trapped, and the trapping is what makes the thickness measurable.

Three consequences follow, and they organise the whole lesson:

- At **low frequency** (wavelength $\gg H$) the wave samples mostly the
  substrate, and $c \to \beta_2$.
- At **high frequency** (wavelength $\ll H$) the wave is confined to the layer,
  and $c \to \beta_1$. The transition between the two limits occurs where the
  wavelength is comparable with $H$, which is where the thickness information
  lives.
- Because both limits are set by *velocities* and the transition location is set
  by $H$, a dispersion curve measures the combination. Separating the two is the
  inversion problem of §4.

## 2. Velocities of ice from its moduli

Start from the isotropic elastic relations, in terms of Young's modulus $E$ and
Poisson's ratio $\nu$:

$$G = \frac{E}{2(1+\nu)}, \qquad K = \frac{E}{3(1-2\nu)}, \qquad
V_s = \sqrt{\frac{G}{\rho}}, \qquad
V_p = \sqrt{\frac{K + \frac{4}{3}G}{\rho}} .$$

The vanishing denominator in $K$ at $\nu = 1/2$ is not a curiosity: it is the
mathematical statement that an incompressible material has no finite P-wave
modulus ratio, and it is why $\nu$ must be known well for a P-wave (or, in
glaciology, for a $V_p/V_s$ measurement) to mean anything.

*Worked example (SYNTHETIC choice).* The demonstration's ice model is
$\rho = 917\ \mathrm{kg\,m^{-3}}$, $E = 9.3\ \mathrm{GPa}$, $\nu = 0.33$:

$$G = \frac{9.3\times10^{9}}{2(1.33)} = 3.4962\times10^{9}\ \mathrm{Pa},
\qquad
K = \frac{9.3\times10^{9}}{3(0.34)} = 9.1176\times10^{9}\ \mathrm{Pa},$$

$$V_s = \sqrt{\frac{3.4962\times10^{9}}{917}} = \sqrt{3.8129\times10^{6}}
= 1952.6\ \mathrm{m\,s^{-1}},$$

$$V_p = \sqrt{\frac{9.1176\times10^{9} + \frac{4}{3}(3.4962\times10^{9})}{917}}
= \sqrt{\frac{1.37792\times10^{10}}{917}} = 3876.4\ \mathrm{m\,s^{-1}},$$

both of which are printed by
[`code/ice_dispersion_demo.py`](code/ice_dispersion_demo.py), together with
$V_p/V_s = 1.985$. Note what this says about ice as a seismic material: it is
slower than any common rock, its Poisson ratio is close to that of a normal
solid, and its impedance is roughly a fifth of granitic rock's — so the
ice/bedrock interface is a strong contrast and a good reflector, which is why
radar (an electromagnetic contrast) and seismics agree so easily on where the
base is.

### 2.1 Temperature

The demonstration models the temperature effect as a linearised fractional
reduction of the shear modulus, $G(T) = G_0\left[1 - \gamma_T (T - T_{\text{ref}})\right]$
with $\gamma_T = 3.0\times10^{-3}\ \mathrm{K^{-1}}$ (a **model choice**; a real
coefficient must come from a measured compilation). Then

$$\frac{\mathrm{d}V_s}{\mathrm{d}T}
= \frac{\mathrm{d}}{\mathrm{d}T}\sqrt{\frac{G}{\rho}}
= \frac{1}{2}\frac{V_s}{G}\frac{\mathrm{d}G}{\mathrm{d}T}
= -\frac{\gamma_T V_s}{2}
= -\frac{3.0\times10^{-3} \times 1952.6}{2}
= -2.929\ \mathrm{m\,s^{-1}\,K^{-1}}$$

as a tangent at the reference temperature. Over the interval $-40$ to $0\
^{\circ}\mathrm{C}$ the demonstration measures a *mean* slope of
$-2.887\ \mathrm{m\,s^{-1}\,K^{-1}}$; the difference from the tangent is the
curvature of $\sqrt{\cdot}$, and it is the reason the model reports the mean over
the interval it used.

The physical significance is in the *product*: over $40\ \mathrm{K}$ the
velocity changes by about $2.3\%$. That is small compared with the ice/rock
contrast, but a $2.3\%$ velocity change over a $1\ \mathrm{km}$ column is a
travel-time change of order $20\ \mathrm{ms}$ — comparable with a thickness error
of a few tens of metres, which is the level of precision the inversion of §4 is
trying to reach.

### 2.2 Porosity

Porosity acts on the moduli directly. The demonstration's linearisation is
$f(\varphi) = 1 - 0.3\varphi$ applied to both $K$ and $G$, so

$$\frac{V_s(\varphi)}{V_s(0)} = \sqrt{1 - 0.3\varphi}
\qquad\Longrightarrow\qquad
\varphi = 0.20 \Rightarrow \frac{V_s}{V_s(0)} = \sqrt{0.94} = 0.9695,$$

i.e. a $3\%$ velocity reduction at $20\%$ porosity. The *sensitivity* is not the
point; the point is that firn — the porous surface layer of an ice sheet — is the
largest near-surface velocity anomaly present, and it is a *layer*, so it
contaminates the low-frequency end of every dispersion curve measured on an ice
sheet. A dispersion inversion with a single-layer parameterisation is fitting two
layers with one.

## 3. Love-wave dispersion for a layer over a half-space

Let the layer have shear velocity $\beta_1$, density $\rho_1$ and thickness $H$;
the half-space has $\beta_2$, $\rho_2$, and $\beta_2 > \beta_1$. Write
$\mu_i = \rho_i \beta_i^{2}$ for the shear moduli. For the fundamental Love mode
(the SH-polarised mode, which is what a horizontal transverse component records)
the dispersion relation is

$$\tan\left(\omega H \sqrt{\frac{1}{\beta_1^{2}} - \frac{1}{c^{2}}}\right)
= \frac{\mu_2}{\mu_1}\,
\frac{\sqrt{\frac{1}{c^{2}} - \frac{1}{\beta_2^{2}}}}
{\sqrt{\frac{1}{\beta_1^{2}} - \frac{1}{c^{2}}}} ,$$

an implicit equation for $c(\omega)$ that must be solved numerically — the
demonstration does exactly that, by bracketting the fundamental branch between
$\beta_1$ and $\beta_2$ and solving with a root finder.

Two limits can be read off without solving anything, and they are the reason the
curve carries thickness information:

- **$\omega \to 0$** (long wavelength): the tangent's argument is small, so the
  right-hand side must be small too, which requires
  $\sqrt{1/c^{2} - 1/\beta_2^{2}} \to 0$, i.e. $c \to \beta_2$.
- **$\omega \to \infty$** (short wavelength): the tangent oscillates rapidly, and
  the solution settles onto the branch where the argument is bounded away from
  $\pi/2$, giving $c \to \beta_1$.

The transition is centred where the wavelength is a few times $H$. For the
demonstration's model ($\beta_1 = 1900\ \mathrm{m\,s^{-1}}$, $\rho_1 = 917\
\mathrm{kg\,m^{-3}}$, $H = 1000\ \mathrm{m}$; $\beta_2 = 3000\
\mathrm{m\,s^{-1}}$, $\rho_2 = 2700\ \mathrm{kg\,m^{-3}}$) the modulus contrast is

$$\frac{\mu_2}{\mu_1} = \frac{2700 \times 3000^{2}}{917 \times 1900^{2}}
= \frac{2.430\times10^{10}}{3.310\times10^{9}} = 7.341,$$

and the measured phase velocity runs from $1916.5\ \mathrm{m\,s^{-1}}$ at
$20\ \mathrm{Hz}$ to $2907.5\ \mathrm{m\,s^{-1}}$ at $0.4\ \mathrm{Hz}$ over the
demonstration's band. The corresponding wavelengths,
$\lambda = c/f$, span $96\ \mathrm{m}$ to $7.3\ \mathrm{km}$, i.e.
$\lambda/H$ from $0.10$ to $7.3$ — the band deliberately brackets the transition,
because a band entirely on one side of it measures only a velocity.

### 3.1 Ice over water is a different waveguide

A half-space of water cannot support a shear wave ($\mu_2 = 0$). In the relation
above the right-hand side vanishes, giving
$\tan(\omega H\sqrt{1/\beta_1^{2} - 1/c^{2}}) = 0$, i.e.

$$c = \frac{\beta_1}{\sqrt{1 - \left(\frac{\omega_n}{\omega}\right)^{2}}}
\quad\text{with } \omega_n = \frac{n\pi\beta_1}{H}, \qquad n = 1, 2, \ldots$$

so the free (floating) ice sheet behaves as a **plate with stress-free faces**:
all modes have cut-off frequencies $\omega_n = n\pi\beta_1/H$, and each mode
approaches $\beta_1$ from above as frequency rises (which is what "dispersive
plate mode" means physically — shorter waves are more strongly guided, so they
travel faster here, the opposite of the ice-over-rock case where $c$ falls with
frequency toward $\beta_1$). The practical consequence is that ice over rock and
ice over water have *qualitatively different* dispersion shapes, and the sign of
$\mathrm{d}c/\mathrm{d}f$ is a first-order discrimination between grounded and
floating ice — which is why dispersion, not amplitude, is the standard
glaciological tool. The honest caveat: a real glacier has a firn layer on top and
a possibly soft till below, both of which change the shape, so the sign test is a
*consistency* test, not a proof.

## 4. The thickness–velocity trade-off, measured

Synthesise a dispersion curve from the model above, then invert it for
$(H, \beta_1)$ with everything else fixed — this is the standard test of what a
dispersion curve can and cannot deliver. The demonstration fits 40 log-spaced
frequencies in $[0.4, 20]\ \mathrm{Hz}$, minimises the rms misfit in **phase
slowness** $1/c$ (the linearised quantity), and accepts every model within $1\%$
rms. Its search grid is $H \in [400, 2500]\ \mathrm{m}$ in 106 steps
($20\ \mathrm{m}$ spacing) and $\beta_1 \in [1520, 2280]\ \mathrm{m\,s^{-1}}$ in
81 steps ($9.5\ \mathrm{m\,s^{-1}}$ spacing).

The measured result:

| quantity | measured |
|---|---|
| accepted models | **1 of 8586** grid points |
| ice thickness range | $1000$ to $1000\ \mathrm{m}$ (true $1000$) |
| layer velocity range | $1900.0$ to $1900.0\ \mathrm{m\,s^{-1}}$ (true $1900.0$) |
| correlation of $H$ with $\beta_1$ over accepted models | undefined ($+$nan: one point) |
| true model accepted? | yes |

And with the layer velocity *forced* to a wrong value:

| assumed $\beta_1$ | accepted thickness |
|---|---|
| $1710.0\ \mathrm{m\,s^{-1}}$ ($-10\%$) | none |
| $1805.0\ \mathrm{m\,s^{-1}}$ ($-5\%$) | none |
| $1900.0\ \mathrm{m\,s^{-1}}$ | $H = 1000$ to $1000\ \mathrm{m}$ |
| $1995.0\ \mathrm{m\,s^{-1}}$ ($+5\%$) | none |
| $2090.0\ \mathrm{m\,s^{-1}}$ ($+10\%$) | none |

Read this honestly, because it is **not** the familiar story, and the difference
matters:

- The trade-off is real in principle — the layer velocity and the thickness are
  both free, and there is a curve in $(H, \beta_1)$ space along which the
  dispersion barely changes. But at a $1\%$ tolerance the accepted set is
  *smaller than the search grid*: it collapses to a single grid point. The data
  over-determine $(H, \beta_1)$ in this configuration, because the band spans
  1.7 decades ($\log_{10}(20/0.4) = 1.699$) and brackets the transition.
- Consequently, a $5\%$ velocity error **cannot be compensated by any thickness**
  in the searched range. The misfit rises above tolerance. This is the opposite
  of the textbook warning that "a $5\%$ velocity error trades against a thickness
  change of similar size", and it is a *measurement*, so it wins: for this model,
  band and tolerance, the dispersion curve constrains the layer velocity tightly
  enough that the trade-off does not absorb a $5\%$ error.
- Notice the asymmetry with the *other* experiment, also measured: fixing the
  thickness to $600$, $800$, $1200$ or $1500\ \mathrm{m}$ and inverting for
  velocity finds **no accepted velocity**, while fixing $H = 1000\ \mathrm{m}$
  finds $1900.0$–$1900.0\ \mathrm{m\,s^{-1}}$. Thickness errors are *not*
  absorbed by velocity either.

So the honest conclusion of the demonstration is narrower — and stronger — than
the folklore: **for a wide-band dispersion curve that brackets the transition,
neither a $5\%$ velocity error nor a $20\%$ thickness error can be masked by the
other parameter within a $1\%$ rms slowness tolerance.** The corollary is where
the real difficulty lies: the conclusion holds only *because* the band is wide
and the substrate is assumed known. Perturb $\beta_2$, or restrict the band to
one side of the transition, and the accepted set widens again.

That is exactly what makes the independent thickness valuable. The demonstration's
own framing carries the message: the elastic constants of ice — and their
temperature and porosity dependence — are model inputs, and a $1\%$ error in the
assumed layer velocity is worth more than any amount of extra frequency sampling,
because it enters the forward model multiplicatively. A radar echo, a borehole or
a short refraction profile fixes $H$ independently, and then the dispersion
measures $\beta_1$ — which is what glaciology actually needs, since shear velocity
is the quantity that maps onto ice temperature and fabric.

## 5. What breaks the trade-off

Ordered by what they deliver per unit of field effort:

1. **An independent thickness** (radar echo, borehole, refraction). Fixes one
   parameter outright and leaves the dispersion to measure the other.
2. **Bandwidth that brackets the transition.** The demonstration's band spans
   $\lambda/H$ from $0.1$ to $7.3$; a band confined to high frequencies sees
   $c \to \beta_1$ and measures a velocity with almost no $H$ sensitivity.
3. **Higher modes and the cut-off frequencies.** The $n$-th mode's cut-off
   depends on $H\beta$ products and on the substrate; a well-identified second
   mode adds independent constraints.
4. **Oblique ancillaries**: receiver functions for $V_p/V_s$, or a $P$-wave
   refraction profile for $V_p$, which fix the ratio rather than the magnitudes.
5. **Not more frequencies in the same band.** Once the band is wide enough, extra
   sampling buys noise averaging only — the same lever-arm argument as in
   [06-05-01 Measuring Q](../05-attenuation-and-anelasticity/01-attenuation-measurement.md) §5.

## 6. What glacial seismology records

Unlike a tectonic setting, the sources of glacial seismicity are mostly at or
near the surface, and their diversity is the subject's signature. The following is
**qualitative background**, not a measurement from this module, and no numbers are
quoted:

- **Calving and iceberg detachment.** Large, discrete events at the terminus,
  with emergent or impulsive onsets depending on failure style, and often
  repeating on a tidal cycle because the tide changes the buoyancy and the
  back-stress on the ice front. Tidally modulated repeating events are the
  clearest evidence that the source is the ice/water boundary rather than the
  bed.
- **Basal stick-slip and icequakes.** Small repeating events from the sliding
  interface, whose recurrence and amplitude respond to subglacial water pressure.
  These are the cryospheric analogue of induced seismicity: the loading is
  hydrological, not tectonic.
- **Creep and crevasse events.** Distributed, small, with frequencies controlled
  by the near-surface structure; the firn layer is the dominant scatterer.
- **Hydraulic transients.** Water-filled crevasses and drainage paths radiate
  short, high-frequency energy because the source is small and the surrounding
  medium is stiff relative to the water.

The measurement consequence is that glacial seismology is dominated by
**repeating sources** — the same location radiating again and again. That is
fortunate: repeating sources turn a monitoring problem into a differential
problem, and differential travel-time and amplitude measurements between
repeats are insensitive to the source and to the absolute velocity, which is why
glacial monitoring detects seasonal and tidal velocity changes in the ice and
the till with far more precision than an absolute dispersion inversion achieves.
This is the same logic as the receiver-function and interferometry modules:
relative measurements buy precision at the cost of an absolute quantity.

## 7. Worked numeric examples

### Example 1 — moduli and velocities

For $\rho = 900\ \mathrm{kg\,m^{-3}}$, $E = 9.0\ \mathrm{GPa}$,
$\nu = 0.35$:

$$G = \frac{9.0\times10^{9}}{2(1.35)} = 3.3333\times10^{9}\ \mathrm{Pa}, \qquad
K = \frac{9.0\times10^{9}}{3(0.30)} = 1.0\times10^{10}\ \mathrm{Pa},$$

$$V_s = \sqrt{\frac{3.3333\times10^{9}}{900}} = 1924.5\ \mathrm{m\,s^{-1}}, \qquad
V_p = \sqrt{\frac{1.0\times10^{10} + 4.4444\times10^{9}}{900}}
= 4006.2\ \mathrm{m\,s^{-1}},$$

so $V_p/V_s = 2.082$. Increasing $\nu$ from $0.33$ to $0.35$ at fixed $E$ *lowers*
$V_s$ (a stiffer bulk response at the expense of shear stiffness) and *raises*
$V_p$: a reminder that "stiffer" is not a single number.

### Example 2 — the temperature effect on a travel time

Take the demonstration's tangent $-2.929\ \mathrm{m\,s^{-1}\,K^{-1}}$ at
$V_s = 1952.6\ \mathrm{m\,s^{-1}}$. Over a $1\ \mathrm{km}$ vertical path,

$$t = \frac{H}{V_s} = \frac{1000}{1952.6} = 0.51214\ \mathrm{s},$$

and warming the column by $10\ \mathrm{K}$ changes $V_s$ by
$-29.29\ \mathrm{m\,s^{-1}}$ to $1923.3\ \mathrm{m\,s^{-1}}$, giving
$t = 1000/1923.3 = 0.51994\ \mathrm{s}$: **a delay of $7.8\ \mathrm{ms}$**. A
$1\%$ thickness error changes the same travel time by $5.1\ \mathrm{ms}$. So in
this synthetic model, a decade of warming and a $1.5\%$ thickness error are
indistinguishable in a single travel time — the reason dispersion (which
separates the two effects by their different frequency behaviour) is used
instead.

### Example 3 — the plate cut-off frequency

For floating ice with $\beta_1 = 1900\ \mathrm{m\,s^{-1}}$ and
$H = 500\ \mathrm{m}$, the first plate mode cuts off at

$$f_1 = \frac{\beta_1}{2H} = \frac{1900}{2 \times 500} = 1.90\ \mathrm{Hz},$$

and the second at $3.80\ \mathrm{Hz}$. Below $1.90\ \mathrm{Hz}$ no Love mode
propagates in the ice plate: energy at those frequencies goes into the water
(because water supports acoustic, not shear, motion, it can still carry
compressional energy, but not the SH mode of the plate). This is why floating-ice
studies work at a few hertz and grounded-ice studies can work at a fraction of a
hertz: the cut-off frequencies themselves encode the thickness.

## 8. Assumptions and regime of validity

1. **Elastic, isotropic, homogeneous layer.** Ice fabric (crystal preferred
   orientation) makes real ice mildly anisotropic; ignored here.
2. **A single layer over a half-space.** Real profiles have a firn layer, a
   temperature profile and a soft till: at least three layers, whose signatures
   overlap in the low-frequency part of the band.
3. **Known substrate properties.** $\beta_2$ and $\rho_2$ enter the dispersion
   relation directly; the demonstration fixes them, which is part of the result
   rather than a separate assumption.
4. **Straight-limit ray geometry absent**: the phase-slowness misfit used here
   assumes a laterally homogeneous, flat structure and a known propagation
   azimuth to the source.
5. **The dispersion curve is measured, not assumed.** Amplitude or single-channel
   data cannot supply it; an array (or a moving source) is required.
6. **Temperature and porosity coefficients are model choices** in this module.
   The real values must come from a measured compilation, and the linearised
   forms used here are valid only over the small ranges stated.
7. **The sign test for floating ice is a consistency test**, not a proof: firn
   and till both change the dispersion shape.

## 9. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | |
| moduli | $E$, $K$, $G$ | Pa | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |
| velocity | $V$ | $\mathrm{m\,s^{-1}}$ | $\sqrt{\mathrm{Pa}/(\mathrm{kg\,m^{-3}})}$ |
| thickness | $H$ | m | |
| phase velocity | $c$ | $\mathrm{m\,s^{-1}}$ | |
| angular frequency | $\omega$ | $\mathrm{rad\,s^{-1}}$ | $2\pi f$ |
| dispersion argument | $\omega H\sqrt{\beta^{-2} - c^{-2}}$ | dimensionless | $\mathrm{s^{-1}}\cdot\mathrm{m}\cdot\mathrm{s\,m^{-1}}$ |
| modulus ratio | $\mu_2/\mu_1$ | dimensionless | |
| plate cut-off | $f_1 = \beta_1/2H$ | Hz | $\mathrm{m\,s^{-1}}/\mathrm{m}$ |

The dimensionless check in row seven is the one worth doing by hand: the
argument of the tangent must be an angle, and it is
$(\mathrm{s^{-1}})(\mathrm{m})(\mathrm{s\,m^{-1}}) = 1$.

## 10. Python demonstration

[`code/ice_dispersion_demo.py`](code/ice_dispersion_demo.py) is the numerical
heart of this lesson. Section 1 computes the moduli and velocities and the
temperature and porosity tables; section 2 solves the Love dispersion relation
over $[0.4, 20]\ \mathrm{Hz}$; section 3 performs the $(H, \beta_1)$ inversion and
reports the accepted family and the marginal widths; section 4 asks what happens
when each parameter is fixed and the other is inverted. Run section 3 twice with
a narrower band and watch the accepted family widen — that is the whole lesson in
one experiment. (The dispersion solve is a root find for 40 frequencies over
thousands of trial models, so this demonstration takes about two minutes.)

Full sets with worked solutions are in
[`exercises/02-glacial-seismology-exercises.md`](exercises/02-glacial-seismology-exercises.md)
and
[`exercises/02-glacial-seismology-solutions.md`](exercises/02-glacial-seismology-solutions.md).

## Mastery checkpoint

Without notes:

> A Love-wave dispersion curve on a grounded ice sheet is measured over
> $[0.5, 10]\ \mathrm{Hz}$; the phase velocity falls from $2500$ to
> $1950\ \mathrm{m\,s^{-1}}$ across the band, and the substrate is assumed to be
> a half-space with $\beta_2 = 3200\ \mathrm{m\,s^{-1}}$,
> $\rho_2 = 2700\ \mathrm{kg\,m^{-3}}$. **(a)** Sketch $c(f)$ and mark where the
> thickness information is. **(b)** Compute the wavelength range and estimate
> $H$ from the frequency at which $c$ is midway between the two limits.
> **(c)** State two model choices that would move your answer and give the sign
> of each effect. **(d)** An independent radar echo gives $H$ to $\pm 5\ \mathrm{m}$;
> explain what the dispersion now measures and why that is the quantity
> glaciology wants. **(e)** If the ice were floating instead of grounded, state
> the qualitative change in $c(f)$ and the physical reason.

A worked version appears in the
[solutions](exercises/02-glacial-seismology-solutions.md).

## Common pitfalls

1. **Quoting an inverted thickness without the assumed layer velocity.** The
   forward model is part of the result.
2. **Asserting that the trade-off always absorbs a velocity error by an equal
   thickness error.** The demonstration measures it *not* doing so for a wide
   band at $1\%$ tolerance; what it does depends on band, substrate and tolerance.
3. **Ignoring the firn layer.** It is a real low-velocity layer on top of the
   target one.
4. **Using a floating-ice model on grounded ice** (or the reverse). The shapes
   differ qualitatively, and the sign of $\mathrm{d}c/\mathrm{d}f$ is diagnostic.
5. **Treating linearised temperature and porosity coefficients as physics.**
   They are parameterisations with stated ranges of validity.
6. **Confusing phase velocity with group velocity.** Dispersion curves are often
   measured as group velocity and inverted as phase; the two differ wherever
   $\mathrm{d}c/\mathrm{d}f \neq 0$, which is the entire informative band.
7. **Forgetting that the source is unknown and often repeating.** Repeating
   sources are the reason differential measurements work so well here.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the dispersion and depth-sensitivity theory used throughout.
- [06-10 Refraction and Near-Surface Seismology](../10-refraction-and-near-surface-seismology/README.md) —
  MASW/SASW, the same inversion on soil rather than ice.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  the technique that makes continuous monitoring of an ice body possible.
- [04-08 Planetary Science and Comparative Planetology](../../04-earth-science-geology/08-planetary-science/README.md) —
  ice as a planetary material, not only a terrestrial one.

## Self-assessment checklist

- [ ] I can compute $V_p$ and $V_s$ from $(E, \nu, \rho)$ with units.
- [ ] I can state the temperature and porosity sensitivities and their signs.
- [ ] I can write the Love dispersion relation and its two limits.
- [ ] I can explain why a free plate has cut-off frequencies.
- [ ] I can run and interpret a two-parameter dispersion inversion.
- [ ] I can say exactly what an independent thickness buys.
- [ ] I can separate the qualitative source description from the measured results.
