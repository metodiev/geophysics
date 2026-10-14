---
id: 06-11-06
title: "Hazard Maps, Site Amplification and Design Codes"
level: graduate
prereqs: ["06-11-04", "06-11-05", "06-08-01"]
tags: [seismology, hazard, site-response, amplification, hazard-maps, design-codes]
---

# Hazard Maps, Site Amplification and Design Codes

> **All models and data in this module are SYNTHETIC.** The soil and rock
> profiles, the bedrock hazard curve and the nonlinearity below are chosen
> teaching values. No measured site response and no published design map or code
> coefficient is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the SH transfer function of a single layer on a half-space from the
   wave equation, the free-surface condition and interface continuity, and show
   that its resonance amplitude is the impedance ratio.
2. **Explain** why the peak amplification is set by damping rather than by the
   impedance contrast alone, and **measure** both.
3. **Explain** why "the amplification factor" is only meaningful with a stated
   frequency band, and **measure** the band dependence.
4. **Derive** how a site factor shifts an entire hazard curve,
   $\lambda_\text{surface}(z) = \lambda_\text{bedrock}(z/F)$, and **compute** the
   change in a design amplitude.
5. **Solve** the nonlinear site-response problem by fixed-point iteration and
   **state** the direction of its effect on the design motion.
6. **Compare** three defensible interpolation rules for a mapped site parameter
   and **quantify** the spread they introduce.
7. **State** how a design value is obtained from a hazard curve, and why a
   uniform-hazard map is not a uniform-risk map.

## Prerequisites

- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  the bedrock curve this lesson modifies.
- [06-11-05 Ground-Motion Prediction Equations and Their Uncertainty](05-ground-motion-models.md) —
  the reference-rock motion being amplified.
- [06-08-01 Receiver Functions: Deconvolution and Ps Conversions](../08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the layered-medium bookkeeping of angles, impedances and delays.

## 1. From a curve to a map

A **hazard map** is a grid of amplitudes, each read off a hazard curve at a fixed
annual exceedance rate (commonly the rate corresponding to 10% or 2% probability
in 50 years). Three operations stand between the curve and the map pixel:

1. **Interpolation** of the parameterised site condition between measurement
   points (Section 7);
2. **Site correction** from the reference rock condition to the actual surface
   (Sections 2–6);
3. **A design rule** converting a probabilistic amplitude into the number printed
   in a code (Section 8).

Each operation introduces its own uncertainty, and all three are invisible in the
finished map pixel. That is the honest difficulty of this lesson: a map looks like
a measurement and is actually a chain of models.

## 2. Deriving the site transfer function

Consider vertically propagating SH waves, a soil layer of thickness $H$, density
$\rho_1$ and shear speed $\beta_1$ over a half-space with $\rho_2, \beta_2$.
Measure $z$ upward from the interface, so the surface is at $z = H$. With time
dependence $e^{-i\omega t}$, the layer displacement is a superposition of up- and
down-going waves,

$$u_1(z) = A e^{ik_1 z} + B e^{-ik_1 z}, \qquad k_1 = \omega/\beta_1,$$

and the half-space contains an incident wave (travelling $+z$) and a reflected
wave: $u_2(z) = C e^{ik_2 z} + D e^{-ik_2 z}$.

**Free surface.** Shear traction vanishes at $z = H$: $\mathrm{d}u_1/\mathrm{d}z = 0$,
giving $B = A e^{2ik_1 H}$ and

$$u_1(z) = 2A e^{ik_1H}\cos\big[k_1(H - z)\big],
\qquad u_1(H) = 2A e^{ik_1 H}.$$

**Continuity at the interface.** Displacement and traction ($\mu\,\mathrm{d}u/
\mathrm{d}z$, with $\mu = \rho\beta^2$) must match at $z = 0$. Using
$\mu k = \omega\rho\beta = \omega Z$ with $Z$ the impedance:

$$C + D = 2A e^{ik_1H}\cos(k_1H), \qquad
C - D = i\,2A e^{ik_1H}\frac{Z_1}{Z_2}\sin(k_1H).$$

Eliminating $D$ gives the surface motion relative to the **incident** amplitude,

$$\frac{u_1(H)}{C} = \frac{2}{\cos(k_1H) + i\,(Z_1/Z_2)\sin(k_1H)}.$$

The free surface of a uniform half-space also doubles the motion, so relative to
the **bedrock outcrop** (which is what a reference-rock hazard curve reports) the
factor of 2 cancels:

$$\boxed{\ A(f) = \left|\frac{1}{\cos(2\pi f H/\beta_1)
+ i\,(Z_1/Z_2)\sin(2\pi f H/\beta_1)}\right|\ }$$

with $Z_1/Z_2 = \rho_1\beta_1/(\rho_2\beta_2)$. Two limits follow immediately:

- $f \to 0$: $\cos \to 1$, $\sin \to 0$, so $A \to 1$ — long-period motion is not
  amplified;
- at $\cos(k_1H) = 0$, i.e. $f_n = (2n+1)\beta_1/(4H)$ for $n = 0,1,2,\dots$,
  $A = Z_2/Z_1$ — the **impedance ratio**;
- at $\sin(k_1H) = 0$, i.e. the even multiples of $\beta_1/(4H)$, $A = 1$:
  anti-resonances.

The demonstration's SYNTHETIC profile ($\beta_1 = 200\ \mathrm{m\,s^{-1}}$,
$\rho_1 = 1.8\ \mathrm{g\,cm^{-3}}$, $H = 30$ m over
$\beta_2 = 800\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2.4\ \mathrm{g\,cm^{-3}}$) gives

$$Z_2/Z_1 = \frac{2.4\times800}{1.8\times200} = 5.333, \qquad
f_0 = \frac{\beta_1}{4H} = 1.6667\ \mathrm{Hz},$$

and prints $A = 5.3333$ at $1.667\ \mathrm{Hz}$, $5.3333$ at $5.0\ \mathrm{Hz}$,
$1.0000$ at $3.333$ and $6.667\ \mathrm{Hz}$, and $1.0043$ at $0.1\ \mathrm{Hz}$.

### Worked example 1 — a different profile

For $\beta_1 = 250\ \mathrm{m\,s^{-1}}$, $\rho_1 = 1.9$, $H = 40$ m over
$\beta_2 = 900\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2.5$:

$$\frac{Z_2}{Z_1} = \frac{2.5\times900}{1.9\times250} = \frac{2250}{475} = 4.737,
\qquad f_0 = \frac{250}{4\times40} = 1.5625\ \mathrm{Hz}.$$

The peak amplification is 4.74 and it sits at 1.56 Hz: a *thicker, faster* soil
column has a *lower* resonance, and a *weaker* impedance contrast has a *smaller*
peak.

## 3. Damping sets the height of the peak

The lossless layer has infinite $Q$ and a resonance as tall as the impedance ratio
no matter how small the contrast is. Real soil attenuates. The standard causal
substitution for a constant quality factor $Q$ is

$$k_1 \rightarrow \frac{\omega}{\beta_1}\left(1 - \frac{i}{2Q}\right),$$

which both lowers and broadens the peak:

| $Q$ | $A(f_0)$ | peak frequency (Hz) |
|---|---|---|
| infinite | 5.333 | 1.6674 |
| 100 | 5.119 | 1.6659 |
| 20 | 4.408 | 1.6597 |
| 10 | 3.755 | 1.6521 |
| 5 | 2.893 | 1.6279 |

At $Q = 20$ — a plausible value for soft soil — only 83% of the impedance ratio is
realised at the resonance, and the peak has moved down slightly. **Reporting a site
amplification without the damping is reporting half a model**, and the missing half
is the part that controls the peak.

## 4. "The" amplification factor is a band average

A structure responds over a band, so design practice uses a band-averaged factor.
The demonstration averages the same response over several bands ($Q = 20$):

| band (Hz) | mean $A(f)$ |
|---|---|
| 0.1–1.0 | 1.1095 |
| 0.5–2.0 | 2.1254 |
| 0.5–10.0 | 1.7989 |
| 1.0–10.0 | 1.9524 |
| 0.1–10.0 | 1.5310 |

The same site has factors of 1.11, 2.13, 1.80, 1.95 and 1.53 depending only on the
band. The peak is 4.4082 at 1.660 Hz. Those numbers are not in conflict: they
answer different questions. The lesson is that a site factor is meaningful only
with its band (and, for a spectral factor, with its period).

## 5. Applying a site factor to a hazard curve

If the surface amplitude is $F$ times the reference-rock amplitude for every
event, then

$$P(A_\text{surface} > z) = P(A_\text{rock} > z/F)
\quad\Longrightarrow\quad
\lambda_\text{surface}(z) = \lambda_\text{rock}\!\left(\frac{z}{F}\right).$$

So the site correction **shifts the curve horizontally in log amplitude**, and the
amplitude at a fixed probability scales by exactly $F$:

$$z_\text{surface}(T) = F \times z_\text{rock}(T).$$

The demonstration uses the band-averaged $F = 1.7989$ (0.5–10 Hz, $Q = 20$) on the
synthetic bedrock curve $\lambda = 0.002\,(z/0.1)^{-2.5}\ \mathrm{yr^{-1}}$:

| case | amplitude at 474.6 yr | rate of exceeding 0.2 g |
|---|---|---|
| bedrock | 0.0979 g | $3.5\times10^{-4}\ \mathrm{yr^{-1}}$ |
| surface ($F = 1.799$) | 0.1762 g | $1.53\times10^{-3}\ \mathrm{yr^{-1}}$ |

The amplitude rises by 1.80 and the rate of exceeding a fixed 0.2 g rises by a
factor of 4.3 — the same physics seen from two sides. Because the hazard curve is
steep, a factor of 1.8 in amplitude is a factor of 4 in rate.

### Worked example 2 — the surface rate at a higher threshold

With $F = 1.7989$, the surface rate of exceeding $0.3\ \mathrm{g}$ equals the
bedrock rate at $0.3/1.7989 = 0.1668\ \mathrm{g}$:

$$\lambda = 0.002\left(\frac{0.1668}{0.1}\right)^{-2.5}
= 0.002 \times 1.668^{-2.5} = 5.6\times10^{-4}\ \mathrm{yr^{-1}},$$

a return period of about 1800 yr. At the bedrock condition the same threshold has
rate $0.002 \times 3^{-2.5} = 1.28\times10^{-4}\ \mathrm{yr^{-1}}$ (7800 yr): the
site factor has shortened the return period of $0.3\ \mathrm{g}$ by a factor of
4.4.

## 6. Nonlinearity: the factor depends on the shaking

Soil stiffness increases with strain rate and decreases with strain amplitude; the
net effect at strong shaking is a *reduction* of the amplification. The
demonstration uses the synthetic form

$$F(z_s) = 1 + \frac{F_\text{lin} - 1}{1 + (z_s/0.30\ \mathrm{g})^2},$$

where $z_s$ is the surface amplitude. Then the design equation becomes implicit,

$$\lambda_\text{rock}\!\left(\frac{z_s}{F(z_s)}\right) = \lambda_\text{target},$$

solved by fixed-point iteration (each evaluation of the hazard curve supplies the
next $z_s$). The measured amplification:

| surface PGA (g) | amplification | implied bedrock PGA (g) |
|---|---|---|
| 0.020 | 1.7954 | 0.0111 |
| 0.050 | 1.7773 | 0.0281 |
| 0.100 | 1.7190 | 0.0582 |
| 0.200 | 1.5531 | 0.1288 |
| 0.400 | 1.2876 | 0.3107 |
| 0.800 | 1.0985 | 0.7283 |

At the 474.6-yr target the linear solution is $0.1762\ \mathrm{g}$ and the
nonlinear one $0.1590\ \mathrm{g}$, a ratio of $0.903$. **Ignoring nonlinearity
overestimates the design motion at strong shaking levels and underestimates it at
weak ones**, and the crossover is a property of the soil model, not a universal
number.

## 7. Maps are interpolation rules

A site-parameter map (for example $V_{S30}$) is built from sparse measurements.
The demonstration places four synthetic boreholes at $x = 0, 4, 9, 15$ km with
$V_{S30} = 420, 260, 620, 330\ \mathrm{m\,s^{-1}}$ and asks for the value at
$x = 6.5$ km, using three defensible rules and a synthetic first-order
amplification rule $A = (760/V_{S30})^{0.5}$:

| rule | $V_{S30}$ (m/s) | amplification (0.5–10 Hz) |
|---|---|---|
| nearest borehole | 260.0 | 1.710 |
| inverse-distance weighting | 425.1 | 1.337 |
| linear interpolation | 440.0 | 1.314 |

The three rules span 69% in $V_{S30}$ and a factor of 1.30 in amplification. None
of them is wrong; they encode different assumptions about spatial continuity. The
uncertainty they introduce is **epistemic and invisible on the map**, and it is
usually larger than the difference between the two nearest boreholes suggests.

## 8. From a hazard curve to a design value

The standard chain is:

1. choose a target probability and exposure, e.g. 2% in 50 years, and convert to
   a rate with $P = 1 - e^{-\lambda t}$;
2. read the **uniform-hazard** spectral amplitude from the map or curve at that
   rate (this is a fixed *hazard*, not a fixed *risk*);
3. apply site factors to obtain the surface spectrum;
4. apply the code's design factor.

Two subtleties belong in any honest presentation:

- **Uniform hazard is not uniform risk.** The annual probability of collapse is
  $\int P(\text{collapse} \mid IM)\,|\mathrm{d}\lambda/\mathrm{d}IM|\,\mathrm{d}IM$,
  so structures with different fragility curves inherit different risks from the
  same hazard. Risk-targeted design inverts this: it chooses the amplitude whose
  convoluted collapse probability equals a target. The conversion requires a
  fragility curve and is therefore not something a hazard map alone can supply.
- **The design factor is a convention, not a measurement.** Codes that define a
  design-level motion as two-thirds of a risk-targeted maximum considered level are
  adopting a policy choice; with a maximum considered amplitude of $0.50\ \mathrm{g}$
  the design value would be $0.333\ \mathrm{g}$. This module uses no code's numbers,
  only the arithmetic of the definitions.

## 9. Assumptions and regime of validity

1. **One-dimensional, horizontally layered, vertically propagating SH.** No basin
   geometry, no surface waves, no 2D or 3D focusing. The largest site amplifications
   observed in nature come from exactly the effects this model omits.
2. **Uniform shaking across the layer.** The derivation assumes a plane wave with a
   single ray parameter; at large distances the incidence angle matters (the
   receiver-function lesson uses the same geometry with a different observable).
3. **Linear viscoelastic response with constant $Q$.** Real damping is
   frequency-dependent and strain-dependent; the constant-$Q$ substitution is a
   first-order approximation.
4. **A frequency-independent site factor.** Applying one number across the whole
   spectrum of interest is a strong simplification; a real soil column amplifies
   periods near $4H/\beta_1$ much more than others.
5. **Site factor independent of the rock amplitude.** True only in the linear
   regime; Section 6 shows the nonlinear correction and its sign.
6. **Ergodic transferability.** The $V_{S30}$-to-amplification relation is
   transferred between sites; it holds on average and fails at individual sites.
7. **Interpolation rule.** Every map pixel between stations is a model output.
8. **Reference condition.** The hazard curve must be for the same reference rock
   condition the amplification factors are defined against, or the correction is
   applied twice or not at all.

## 10. Python demonstration

[`code/hazard_mapping_demo.py`](./code/hazard_mapping_demo.py) computes the SH
transfer function, measures the effect of damping and of the averaging band,
shifts a bedrock hazard curve by a site factor, solves the nonlinear problem by
fixed-point iteration, and compares three interpolation rules.

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hazard_mapping_demo.py
```

It prints labelled results with units and exits 0. Every number in this lesson is
one of its outputs.

## Mastery checkpoint

Use the demonstration's profiles and the synthetic bedrock curve
$\lambda = 0.002(z/0.1)^{-2.5}\ \mathrm{yr^{-1}}$.

**(a)** For $\beta_1 = 180\ \mathrm{m\,s^{-1}}$, $\rho_1 = 1.7$, $H = 25$ m over
$\beta_2 = 900\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2.5$, compute the impedance ratio,
the fundamental frequency and the lossless peak amplification.
**(b)** With $F = 2.0$ and the bedrock amplitude $0.0979\ \mathrm{g}$ at 474.6 yr,
compute the surface amplitude at the same probability and the surface rate of
exceeding $0.2\ \mathrm{g}$.
**(c)** With the nonlinearity of Section 6, compute the amplification at
$0.2\ \mathrm{g}$ and the implied bedrock amplitude, and state whether the
nonlinear design amplitude is larger or smaller than in (b).
**(d)** Two boreholes 5 km apart report $V_{S30} = 240$ and $V_{S30} = 700\
\mathrm{m\,s^{-1}}$. Using $A = (760/V_{S30})^{0.5}$, compute the two
amplifications, and state what a map that interpolates linearly between them
assumes.
**(e)** Explain in two sentences why a uniform-hazard map is not a uniform-risk
map, and what extra ingredient is needed to make it one.

## Common pitfalls

1. **Quoting a site factor with no band and no damping.** The demonstration gives
   1.11, 1.80 and 2.13 for the same site.
2. **Applying a linear factor at strong shaking.** The demonstration's factor falls
   from 1.80 to 1.55 between 0.05 g and 0.2 g.
3. **Correcting twice.** The hazard curve is on a reference condition; check which
   one before applying a factor.
4. **Reading the map as data.** Between stations a map is an interpolation rule,
   and the demonstration's three rules differ by a factor of 1.3 in amplification.
5. **Treating the resonance as the design factor.** A structure whose period does
   not match the site resonance sees much less than the peak.
6. **Confusing uniform hazard with uniform risk.** The design amplitude must come
   from a target risk and a fragility curve if risk is what the code promises.
7. **Forgetting that the site term is epistemic before it is aleatory.** The
   profile, the interpolation and the $V_{S30}$-transfer relation are all models.

## Related modules

- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  where the curve comes from.
- [06-11-05 Ground-Motion Prediction Equations and Their Uncertainty](05-ground-motion-models.md) —
  the reference-rock motion.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  the layered-medium response measured from real conversions.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) —
  impedance contrasts and multiples in exploration geometry.
- [10-04 Shear-Wave Velocity Modelling and Site Classification](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/02-shear-wave-velocity-modelling.md) —
  measuring the near-surface parameters this lesson assumes.
- [04-07 Geologic and Geophysical Hazards](../../04-earth-science-geology/07-geologic-hazards/README.md) —
  how maps become policy.

## Exercises

Full problem sets and worked solutions:
[`exercises/06-hazard-mapping-exercises.md`](./exercises/06-hazard-mapping-exercises.md)
and
[`exercises/06-hazard-mapping-solutions.md`](./exercises/06-hazard-mapping-solutions.md).
