---
id: 11-05-03
title: "Seismic Refraction and Surface Waves for Aquifers"
level: graduate
prereqs: ["11-05-01", "06-10-01", "06-10-04"]
tags: [exploration-geophysics, groundwater, refraction, surface-waves, masw, gassmann, resolution]
---

# Seismic Refraction and Surface Waves for Aquifers

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the head-wave travel-time equation from Snell's law and the
   critical angle, and **derive** the crossover distance and the depth formula.
2. **Recover** a two-layer depth from a crossover distance and from an intercept
   time, and **explain** why the agreement of the two is a check, not an
   independent measurement.
3. **Compute** the depth error produced by a stated velocity error for a range
   of velocity contrasts, and identify the regime in which refraction depth is
   unreliable.
4. **Explain** why the water table is a $v_p$ refractor and a poor $v_s$
   target, and **compute** the crossover distance from a Gassmann contrast.
5. **Derive** the approximate depth sampled by a Rayleigh wave of wavelength
   $\lambda$, and **compute** the sampling depth of a dispersion curve.
6. **Quantify** the non-uniqueness of a surface-wave profile by comparing two
   profiles that fit the same dispersion curve.

## Prerequisites

- [11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces](../05-groundwater-exploration/01-aquifer-signatures.md)
  — the Gassmann velocity contrast across a water table used throughout.
- [06-10-01 Refraction Basics](../../06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md)
  — the head wave and the travel-time curve.
- [06-10-04 MASW and SASW](../../06-seismology/10-refraction-and-near-surface-seismology/04-masw-sasw.md)
  — how a dispersion curve is measured and inverted.
- [10-04-02 Shear-Wave Velocity Modelling](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/02-shear-wave-velocity-modelling.md)
  — the $v_s$ profile as a geotechnical product.

> All models and data in this module are **SYNTHETIC**. Velocities, thicknesses
> and noise levels are chosen teaching values, not measurements of any site.

## 1. Intuition: two seismic questions, two different answers

A refraction survey asks *where does the velocity first increase strongly?* It
therefore finds the base of the low-velocity layer — weathered rock, dry sand, or
unsaturated sediment — and, because saturating a rock raises its $v_p$, it often
finds the water table. That is a statement about **compressibility**, and
therefore about the pore fluid.

A surface-wave survey asks *how does the shear velocity change with depth?*
Rayleigh waves of wavelength $\lambda$ sample roughly the top $\lambda/3$ of the
ground, so sweeping the frequency from low to high builds a profile of $v_s$
versus depth. That is a statement about **shear stiffness** and density, and
therefore about the *framework* (porosity, cementation, stress), not about the
fluid.

The two methods therefore answer different questions that are commonly confused:
refraction can see the water table but is nearly blind to porosity, while surface
waves can see porosity and compaction but are nearly blind to saturation. Both
limits follow from the same physics — Gassmann changes the bulk modulus and the
density but not the shear modulus — and the demonstration measures both.

## 2. Precise definitions

### 2.1 Head waves and the critical angle

When a wave in a layer of speed $v_1$ meets an interface with a faster medium
$v_2 > v_1$, Snell's law gives a critical angle

$$ \theta_c = \arcsin\!\left(\frac{v_1}{v_2}\right). $$

At incidence $\ge\theta_c$ the transmitted wave travels along the interface and
continuously radiates energy back into the upper layer as a **head wave**. A
head wave exists **only** if $v_2 > v_1$; a velocity *decrease* refracts the ray
away from the interface and produces no head wave, which is why a low-velocity
zone is invisible to refraction.

### 2.2 The crossover, the intercept and the depth

For a layer of thickness $z$ over a half-space,

$$ t_{\text{head}}(x) = \frac{x}{v_2} + \frac{2z\cos\theta_c}{v_1}
= \frac{x}{v_2} + t_i, $$

with $t_i$ the **intercept (delay) time**. The head wave overtakes the direct
wave at the **crossover distance**

$$ x_c = 2z\sqrt{\frac{v_2+v_1}{v_2-v_1}},
\qquad\text{so}\qquad
z = \frac{x_c}{2}\sqrt{\frac{v_2-v_1}{v_2+v_1}}, $$

and from the intercept time

$$ z = \frac{v_1 t_i}{2\cos\theta_c}. $$

### 2.3 Dispersion, phase velocity and the sampling depth

In a layered medium, surface waves are **dispersive**: the phase velocity
$v_R(f)$ depends on frequency because different wavelengths sample different
depths. The measurement is the curve $v_R$ versus $f$; the inversion seeks the
$v_s(z)$ profile whose predicted curve matches it.

The standard rule of thumb is that a Rayleigh wave of wavelength
$\lambda = v_R/f$ is most sensitive to depths near $\lambda/3$. It is a
*heuristic*, not an identity: the true sensitivity kernel spreads over roughly
$\lambda/3$ to $\lambda/2$ and depends on the velocity gradient. This lesson
treats it as a stated sampling model, and Section 3.4 measures what it implies
for resolution.

## 3. Derivations

### 3.1 The head-wave time and the crossover

Along the path down to the interface at the critical angle, along the interface,
and back up, the travel time is

$$ t_{\text{head}} = \frac{2z}{v_1\cos\theta_c}
+ \frac{x - 2z\tan\theta_c}{v_2}. $$

Use Snell's law $\sin\theta_c = v_1/v_2$, so $1/v_2 = \sin\theta_c/v_1$, to
eliminate the along-interface leg:

$$ \frac{x - 2z\tan\theta_c}{v_2}
= \frac{x\sin\theta_c}{v_1} - \frac{2z\sin^{2}\theta_c}{v_1\cos\theta_c}
= \frac{x}{v_2} - \frac{2z\sin^{2}\theta_c}{v_1\cos\theta_c}, $$

because $x\sin\theta_c/v_1 = x/v_2$. Adding the down-and-up leg gives

$$ t_{\text{head}} = \frac{x}{v_2}
+ \frac{2z}{v_1\cos\theta_c}\left(1 - \sin^{2}\theta_c\right)
= \frac{x}{v_2} + \frac{2z\cos\theta_c}{v_1}, $$

using $1-\sin^{2}\theta_c = \cos^{2}\theta_c$ and cancelling one factor of
$\cos\theta_c$. The intercept time is therefore
$t_i = 2z\cos\theta_c/v_1$.

Setting $t_{\text{head}} = x/v_1$ and solving for $x$:

$$ \frac{x}{v_1} = \frac{x}{v_2} + \frac{2z\cos\theta_c}{v_1}
\;\Longrightarrow\;
x\left(\frac{1}{v_1}-\frac{1}{v_2}\right) = \frac{2z\cos\theta_c}{v_1}, $$
$$ x_c = \frac{2z\cos\theta_c\,v_2}{v_2 - v_1}
= 2z\sqrt{\frac{v_2+v_1}{v_2-v_1}}, $$

using $\cos\theta_c = \sqrt{v_2^{2}-v_1^{2}}/v_2$.

**Numerical check (SYNTHETIC).** $v_1 = 800$, $v_2 = 2400\ \mathrm{m\,s^{-1}}$:
$\theta_c = \arcsin(1/3) = 19.47^\circ$, $\cos\theta_c = 0.9428$,
$t_i = 2(12)(0.9428)/800 = 28.28\ \mathrm{ms}$, and

$$ x_c = 2(12)\sqrt{3400/1600} = 24\sqrt{2.125} = 33.94\ \mathrm{m}. $$

Inverting the formula returns $z = 12.000\ \mathrm{m}$; the demonstration prints
both $12.000\ \mathrm{m}$ from the crossover and $12.000\ \mathrm{m}$ from the
intercept. The two formulas are both derived from the same two-layer model, so the
agreement is **algebraic consistency, not independent confirmation**.

### 3.2 How a velocity error becomes a depth error

Differentiate the depth formula. Since $z \propto x_c\sqrt{(v_2-v_1)/(v_2+v_1)}$,

$$ \frac{\partial z}{\partial v_1} = -z\,\frac{v_2}{v_2^{2}-v_1^{2}},
\qquad
\frac{\partial z}{\partial v_2} = +z\,\frac{v_1}{v_2^{2}-v_1^{2}}. $$

Both blow up as $v_2 \to v_1$: near-unit contrast is the ill-conditioned regime.
The demonstration's table makes the magnitude concrete for $+5\%$ velocity
errors:

| $v_2/v_1$ | Depth error from $v_1 + 5\%$ | Depth error from $v_2 + 5\%$ |
|---|---|---|
| 1.25 | $-11.5\%$ | $+10.3\%$ |
| 1.50 | $-6.1\%$ | $+5.7\%$ |
| 2.00 | $-3.3\%$ | $+3.2\%$ |
| 5.00 | $-1.0\%$ | $+1.0\%$ |

The signs are opposite because increasing $v_1$ makes the layer look thinner
(everything happens faster) while increasing $v_2$ makes the refractor look
deeper.

### 3.3 The water-table refractor from Gassmann

The synthetic Gassmann frame of
[11-05-01](./01-aquifer-signatures.md) gives $v_p = 1642\
\mathrm{m\,s^{-1}}$ unsaturated and $2272\ \mathrm{m\,s^{-1}}$ saturated, a
contrast of $1.384$. Then

$$ \theta_c = \arcsin(1642/2272) = 46.26^\circ, \qquad \cos\theta_c = 0.6913, $$

and the crossover distances are $9.97\ \mathrm{m}$ (2 m deep),
$24.92\ \mathrm{m}$ (5 m) and $49.83\ \mathrm{m}$ (10 m).

Because the contrast is only $1.38$, the head wave is *weak* and arrives at a
shallow angle: it is easy to mis-pick, and a $5\%$ velocity error is a $\sim3\%$
depth error at this contrast (interpolating the table above). The physics also
imposes a hard limit: where saturation does not raise $v_p$ — a stiff rock with
low porosity, or a clay whose frame softens on wetting — there is no refractor at
all, and a refraction survey will simply not see the water table.

### 3.4 Surface-wave sampling and the resolution limit

Take the sampling heuristic $z \approx \lambda/3 = v_R/(3f)$. Inverting gives
the frequency at which a given depth is sampled, and the sequence of sampling
depths in the demonstration is

| $f$ (Hz) | $\lambda/3$ (m) |
|---|---|
| 2 | 64.9 |
| 4 | 32.3 |
| 8 | 14.7 |
| 16 | 4.2 |
| 32 | 2.1 |

Two implications follow, and both are honest limitations rather than caveats.

- **Resolution degrades with depth.** At 2 Hz the sampled depth is
  $64.9\ \mathrm{m}$; a $5\ \mathrm{m}$ feature at that depth is averaged into a
  window 20 times its thickness. Surface waves resolve *trends*, not thin layers,
  at depth.
- **A profile is a family.** The demonstration compares a sharp step
  ($200 \to 400\ \mathrm{m\,s^{-1}}$ at $10\ \mathrm{m}$) with a linear gradient
  ($200$ to $400\ \mathrm{m\,s^{-1}}$ from $5$ to $25\ \mathrm{m}$). Their
  dispersion curves differ by at most $6.07\%$ (at 16 Hz), and by less than
  $1.7\%$ below 8 Hz. Against a 3-5% data noise level, the deep part of the two
  profiles is effectively one measurement. An inversion that returns a single
  layered model is returning a choice from that family.

## 4. Worked examples

### Example 1 — depth from a picked crossover, with its error

A two-layer survey over saturated sand measures $v_1 = 900\
\mathrm{m\,s^{-1}}$, $v_2 = 2700\ \mathrm{m\,s^{-1}}$ and picks
$x_c = 45.0\ \mathrm{m}$.

$$ z = \frac{45.0}{2}\sqrt{\frac{2700-900}{2700+900}}
= 22.5\sqrt{0.5} = 15.91\ \mathrm{m}. $$

If the true $v_1$ is $945\ \mathrm{m\,s^{-1}}$ ($+5\%$) and $x_c$ is unchanged,

$$ z = 22.5\sqrt{\frac{1755}{3645}} = 22.5\sqrt{0.48148} = 15.61\ \mathrm{m}, $$

an error of $-0.30\ \mathrm{m}$ ($-1.9\%$). The same $5\%$ error at a contrast of
$1.25$ would move the depth by $-11.5\%$ (the demonstration's table). **The
contrast, not the survey quality, is what sets the reliability.**

### Example 2 — why $v_s$ is not a water-table tool

From the synthetic frame,

$$ v_p: 1642 \to 2272\ \mathrm{m\,s^{-1}}\ (+38.4\%), \qquad
v_s: 1272 \to 1180\ \mathrm{m\,s^{-1}}\ (-7.2\%). $$

A surface-wave survey is sensitive to $v_R \approx 0.9\,v_s$; a $7\%$ $v_s$ change
with the opposite sign to $v_p$ is at the edge of what a dispersion curve can
resolve in a noisy urban setting. The practical consequence is that a
"surface-wave water table" is usually the *lithological* boundary that the water
table follows (the base of the soil, the top of a cemented layer), not the
saturation front itself. Attributing it to saturation requires an independent
water-level measurement.

### Example 3 — how deep is 8 Hz looking, and what does that resolve?

At 8 Hz the demonstration's step profile gives $v_R = 352.0\
\mathrm{m\,s^{-1}}$, so $\lambda = 352/8 = 44.0\ \mathrm{m}$ and the sampling
depth is $\lambda/3 = 14.7\ \mathrm{m}$. A layer 3 m thick at that depth occupies
one fifth of the sampling window: it can shift the phase velocity slightly but
its thickness and its velocity cannot be separated. To resolve it, the profile
must include frequencies near $f = v_R/(3z) \approx 39\ \mathrm{Hz}$, if the
acquisition supports them — which for a small array and a soft, attenuating
near-surface it often does not.

## 5. Assumptions and regime of validity

1. **Two horizontal layers for refraction.** A thin intermediate fast layer that
   never appears as a first arrival (a *hidden* layer) biases the depth of the
   deeper refractor shallow; a velocity reversal cannot be detected at all.
2. **Lateral invariance.** Dipping refractors make the apparent velocity
   depend on the shooting direction; a single spread mis-locates the interface.
3. **Near-surface condition.** The source-receiver offsets must exceed several
   times the depth for a head wave to be identifiable, and the receiver spacing
   must be fine enough to pick the crossover.
4. **Rayleigh sampling heuristic.** $\lambda/3$ is not exact; the true kernel is
   broader and asymmetric, and for a strong velocity increase with depth the
   actual sampling depth is smaller.
5. **1-D layered model for the dispersion inversion.** Laterally varying
   structure, and higher modes (which appear whenever there is a strong velocity
   inversion), invalidate the fundamental-mode interpretation.

## 6. Python demonstration

`code/seismic_groundwater_demo.py` prints:

1. the two-layer travel-time curve, its crossover, and the depth recovered two
   ways;
2. the depth error from a $+5\%$ velocity error across a range of contrasts;
3. the water-table refractor computed from Gassmann velocities;
4. a Rayleigh dispersion curve for a sharp step and for a gradient, the maximum
   difference between them, and the sampling depth of each frequency;
5. the $v_p$ versus $v_s$ sensitivity to saturation.

```bash
cd 11-exploration-geophysics/05-groundwater-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_groundwater_demo.py
```

Companions:
[`exercises/03-seismic-groundwater-exercises.md`](./exercises/03-seismic-groundwater-exercises.md)
and
[`exercises/03-seismic-groundwater-solutions.md`](./exercises/03-seismic-groundwater-solutions.md).

## Common pitfalls

1. **Reporting a refraction depth without the velocity contrast.** Below a
   contrast of about 1.5 the depth is dominated by the velocity error.
2. **Assuming the water table is always a refractor.** $v_2 > v_1$ is required;
   in stiff, low-porosity rock saturation changes $v_p$ little.
3. **Treating the two depth formulas as independent checks.** They are algebra
   on one model; a misfit indicates a mis-pick or a departure from two layers.
4. **Using $v_s$ as a water indicator.** Gassmann leaves $\mu$ unchanged; $v_s$
   responds to density and to the framework.
5. **Forcing a layered answer from a dispersion curve.** The curve determines a
   family; a single profile is a regularised choice.

## Mastery checkpoint

Complete this without notes:

> A refraction line over alluvium gives $v_1 = 700\
> \mathrm{m\,s^{-1}}$, $v_2 = 2100\ \mathrm{m\,s^{-1}}$ and a crossover at
> $x_c = 31\ \mathrm{m}$; a companion surface-wave survey gives $v_R = 240\
> \mathrm{m\,s^{-1}}$ at 10 Hz and $v_R = 180\ \mathrm{m\,s^{-1}}$ at 40 Hz.
> **(a)** Compute the refractor depth and the intercept time. **(b)** Compute the
> depth error if $v_1$ were $10\%$ higher. **(c)** Compute the sampling depth at
> each surface-wave frequency, and state whether the surface-wave data could
> resolve a 3 m layer between them. **(d)** Explain in two sentences why the two
> methods could place the "water table" at different depths without either being
> wrong.

A worked version of (a)-(c) is in the lesson-05-03
[solutions](./exercises/03-seismic-groundwater-solutions.md).

## Related modules

- [11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces](./01-aquifer-signatures.md)
  — the Gassmann contrast used in Section 3.3.
- [11-05-02 EM and ERT for Groundwater Mapping](./02-em-and-ert-groundwater.md)
  — the conductivity alternative, with a different non-uniqueness.
- [11-05-04 Airborne EM for Regional Aquifer Mapping](./04-airborne-groundwater.md)
  — regional imaging of the same targets.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  — the methods in full.
- [10-04 Near-Surface Seismic and Geotechnical Methods](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/01-spt-cpt-crosshole.md)
  — how $v_s$ becomes a design parameter.

## Self-assessment checklist

- [ ] I can derive the head-wave time and the crossover distance.
- [ ] I can compute a depth from $x_c$ and from $t_i$.
- [ ] I can estimate the depth error for a stated velocity error.
- [ ] I can state when a water table is not a refractor.
- [ ] I can compute the sampling depth of a dispersion curve.
- [ ] I can explain why a dispersion curve gives a family of profiles.
