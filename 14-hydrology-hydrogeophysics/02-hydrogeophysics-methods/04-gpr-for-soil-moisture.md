---
id: 14-02-04
title: "GPR for Soil Moisture and Water Table"
level: doctoral
prereqs: ["14-02-03", "14-01-06", "10-01-01"]
tags: [hydrogeophysics, gpr, soil-moisture, permittivity, water-table, attenuation]
---

# GPR for Soil Moisture and Water Table

Ground-penetrating radar is the only routine geophysical method that measures
**water content** rather than a proxy for it. Water has a relative permittivity of
about 81 against 4.5 for soil minerals and 1 for air, so the bulk permittivity of
a soil is dominated by its water content; and because radar velocity is
$c/\sqrt{\varepsilon}$, a travel-time measurement is a water-content measurement.
That is a short and unusually reliable chain of physics, and it is why GPR is the
default tool for the vadose zone.

Its limits are equally definite, and this lesson is organised around them:
penetration is set by ionic conductivity (clay and salinity), resolution and
penetration trade against each other through frequency, and the inversion to water
content is only as good as its calibration. The electromagnetic theory — Maxwell's
equations, the low-loss regime, antenna behaviour and processing — is in
[10-gpr-near-surface/01-gpr-principles](../../10-gpr-near-surface/01-gpr-principles/README.md);
this lesson assumes it and concentrates on the hydrological measurement.

**All models and data in this module are SYNTHETIC.** The soils, water contents,
conductivities and synthetic radar records below are invented teaching values. No
real radar system, site or dataset is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the permittivity and radar velocity of a soil from its water content
   with a mixing model, and **invert** the relation.
2. **Compute** the reflection coefficient at the ground surface and at the water
   table, and **explain** the polarity reversal that identifies a wetting front.
3. **Recover** a radar velocity from a multi-offset gather by normal-moveout
   analysis, and **quantify** the depth error from assuming it.
4. **Quantify** the bias introduced by an uncalibrated mixing model in a
   clay-bearing soil and **state** the calibration that removes it.
5. **Compute** the low-loss attenuation from conductivity and permittivity and
   **derive** the achievable penetration for a stated dynamic range.
6. **State** why the velocity changes by more than a factor of two across the water
   table, and **design** a survey that handles it.
7. **Distinguish** what a permittivity measurement determines (water content) from
   what it cannot (pore-water salinity, clay-bound water).

## Prerequisites

- [14-02-03 Seismic Methods for Aquifer Geometry](03-seismic-hydrogeophysics.md) —
  the reflection and moveout machinery, reused here with dielectric impedances.
- [14-01-06 The Unsaturated Zone](../01-hydrology-fundamentals/06-unsaturated-zone.md)
  — the water content that GPR measures, and the CRIM relation derived there.
- [10-01-01 GPR Physics](../../10-gpr-near-surface/01-gpr-principles/01-gpr-physics.md)
  — the low-loss approximation, dielectric reflection and antenna behaviour.

---

## 1. Velocity, permittivity and water content

In the low-loss regime the radar velocity is
$v = c/\sqrt{\varepsilon_{\text{eff}}}$ with $c = 0.299792458\
\mathrm{m\,ns^{-1}}$ (exact), and the CRIM mixing model makes
$\sqrt{\varepsilon}$ linear in water content:

$$\sqrt{\varepsilon_{\text{eff}}}
= (1-\phi)\sqrt{\varepsilon_s} + \theta\sqrt{\varepsilon_w}
+ (\phi-\theta)\sqrt{\varepsilon_a},$$

with $\varepsilon_s = 4.5$, $\varepsilon_w = 81$, $\varepsilon_a = 1$ and
$\phi = 0.40$ in the synthetic soil:

| $\theta$ | $\varepsilon_{\text{eff}}$ | $v$ (m ns$^{-1}$) | TWT over 1 m (ns) | depth for a 10 ns two-way time (m) |
|---|---|---|---|---|
| 0.02 | 3.359 | 0.1636 | 12.23 | 0.82 |
| 0.05 | 4.296 | 0.1446 | 13.83 | 0.72 |
| 0.10 | 6.115 | 0.1212 | 16.50 | 0.61 |
| 0.20 | 10.711 | 0.0916 | 21.83 | 0.46 |
| 0.30 | 16.588 | 0.0736 | 27.17 | 0.37 |
| 0.40 | 23.744 | 0.0615 | 32.51 | 0.31 |

The velocity falls by a **factor of 2.66** between nearly dry and saturated, and
the depth implied by a fixed 10 ns two-way time changes from 0.82 m to 0.31 m. **A
single conversion velocity cannot be applied to a whole vadose-zone profile**, and
the error from trying is largest exactly at the water table, where the velocity
changes most rapidly.

## 2. Reflections and the polarity of the water table

At normal incidence between two low-loss dielectrics,

$$R = \frac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}}
{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}}
= \frac{v_2 - v_1}{v_2 + v_1}.$$

(The second form follows because $v \propto 1/\sqrt{\varepsilon}$; the equality is
verified in the demonstration against the impedance form $R = (Z_2-Z_1)/(Z_2+Z_1)$
with $Z = \sqrt{\mu/\varepsilon}$, which agrees to machine precision in the
low-loss limit.)

For the synthetic soil:

- **air to ground** ($\varepsilon = 1 \to 4.296$): $R = -0.349$. A strong,
  negative-polarity surface reflection, which is why the ground reflection is used
  to time-zero a GPR section.
- **dry to saturated** ($4.296 \to 23.744$): $R = -0.403$.

**The water-table reflection has negative polarity.** The wave enters a
higher-permittivity medium, so the reflected pulse is inverted relative to the
incident one. That polarity reversal is the most reliable GPR water-table
diagnostic, because it distinguishes a wetting front from a reflector caused by a
texture change at constant water content — and texture changes can have either
sign, so amplitude alone does not discriminate.

As with seismics, the *strength* of the water-table reflection is a statement about
the zone above it:

| $\theta$ above | $\theta$ below | $R$ |
|---|---|---|
| 0.02 | 0.40 | $-0.453$ |
| 0.05 | 0.40 | $-0.403$ |
| 0.10 | 0.40 | $-0.327$ |
| 0.20 | 0.40 | $-0.196$ |
| 0.05 | 0.20 | $-0.225$ |

A wet cover or a small saturation step halves or removes the reflection.

## 3. Measuring the velocity instead of assuming it

A common-midpoint gather over a flat reflector satisfies the normal-moveout
relation $t^{2} = t_0^{2} + x^{2}/v^{2}$, so a least-squares fit of $t^{2}$ against
$x^{2}$ yields the velocity from the curvature and the zero-offset time from the
intercept. For a reflector at 2 m depth, with 0.2 ns of picking noise added to the
synthetic travel times:

**Dry sand** ($\varepsilon = 4.30$, $v_{\text{true}} = 0.1446\
\mathrm{m\,ns^{-1}}$, $t_0 = 27.66$ ns):

| $x$ (m) | 0.2 | 0.5 | 1.0 | 1.5 | 2.0 |
|---|---|---|---|---|---|
| $t$ (ns) | 27.597 | 27.964 | 28.345 | 29.909 | 30.628 |

Fitted slope $45.71\ \mathrm{ns^2\,m^{-2}}$ gives
$v_{\text{NMO}} = 0.1479\ \mathrm{m\,ns^{-1}}$ (**+2.27%**), and the fitted
intercept gives $d = 2.048$ m (**+2.41%**).

**Moist sand** ($\varepsilon = 16.59$, $v_{\text{true}} = 0.0736\
\mathrm{m\,ns^{-1}}$): fitted $v_{\text{NMO}} = 0.0727\ \mathrm{m\,ns^{-1}}$
($-1.19\%$).

Against this, **using a velocity 1.5× too high gives $d = 3.00$ m from the same
$t_0$ — a 50% depth error.** The moveout fit reduces a potentially 50% error to
about 2%, which is the entire reason multi-offset GPR is worth the complexity. The
practical limit is that the moveout needed to resolve $v$ requires antenna
separations comparable with the target depth, where the plane-layer assumption and
the antenna's directivity both begin to fail — the same tension as in seismic
reflection ([14-02-03 §3](03-seismic-hydrogeophysics.md)).

## 4. The inversion, and the calibration that decides it

CRIM is a *model*. In a clay-bearing soil, some water is bound to mineral surfaces
and behaves dielectrically like a solid with $\varepsilon \approx 5$–6 rather than
81, so the bulk permittivity is lower than CRIM predicts for the true water
content. The demonstration models this as a true water content 0.04 above the CRIM
prediction:

| true $\theta$ | $\varepsilon$ measured | $\theta$(CRIM) | bias | relative bias |
|---|---|---|---|---|
| 0.06 | 3.359 | 0.0200 | $-0.0400$ | $-66.7\%$ |
| 0.10 | 4.635 | 0.0600 | $-0.0400$ | $-40.0\%$ |
| 0.15 | 6.517 | 0.1100 | $-0.0400$ | $-26.7\%$ |
| 0.20 | 8.719 | 0.1600 | $-0.0400$ | $-20.0\%$ |
| 0.30 | 14.083 | 0.2600 | $-0.0400$ | $-13.3\%$ |

The bias is a **constant** $-0.04$ in absolute water content, but a **67% relative
error at $\theta = 0.06$**. The relative error is worst where the water content is
smallest, which is precisely where a hydrologist may care most (the dry-season
state, the wilting point, the recharge threshold). The remedy is a **site
calibration** — three to five gravimetric samples across the range of interest,
each with the permittivity measured at the same location — rather than an
end-member mixing model. Note also that the bias is one-sided: a
mal-calibrated GPR does not produce noise, it produces a systematically low water
content that looks entirely plausible.

## 5. Attenuation: what actually limits penetration

The exact attenuation constant of a lossy dielectric is

$$\alpha = \omega\sqrt{\frac{\mu_0\varepsilon}{2}}\,
\sqrt{\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^{2}} - 1}
\ [\mathrm{Np\,m^{-1}}], \qquad 1\ \mathrm{Np} = 8.686\ \mathrm{dB},$$

with the **loss tangent** $\sigma/(\omega\varepsilon)$ deciding the regime:

- **low loss** ($\sigma \ll \omega\varepsilon$): $\alpha \to
  \frac{\sigma}{2}\sqrt{\mu_0/\varepsilon}$, which is **independent of
  frequency**;
- **high loss** ($\sigma \gg \omega\varepsilon$): $\alpha \to
  \sqrt{\omega\mu_0\sigma/2}$, which grows as $\sqrt{f}$.

With a stated 60 dB dynamic-range convention (full table printed by the
demonstration):

| $f$ (MHz) | $\sigma$ (S m$^{-1}$) | $\varepsilon$ | loss tangent | $\alpha$ (dB m$^{-1}$) | 60 dB depth (m) | regime |
|---|---|---|---|---|---|---|
| 100 | 0.005 | 4.30 | 0.209 | 3.93 | 15.3 | transition |
| 100 | 0.005 | 16.59 | 0.054 | 2.01 | 29.9 | low loss |
| 100 | 0.020 | 16.59 | 0.217 | 7.99 | 7.5 | transition |
| 100 | 0.050 | 16.59 | 0.542 | 19.43 | 3.1 | transition |
| 100 | 0.200 | 16.59 | 2.167 | 61.74 | 1.0 | high loss |
| 250 | 0.005 | 4.30 | 0.084 | 3.94 | 15.2 | low loss |
| 250 | 0.050 | 16.59 | 0.217 | 19.97 | 3.0 | transition |
| 250 | 0.200 | 16.59 | 0.867 | 74.54 | 0.8 | transition |

The low-loss limit is checked in the demonstration against the exact formula:
at $\sigma = 0.001\ \mathrm{S\,m^{-1}}$ and $f = 100$ MHz the ratio of exact to
approximate is 0.999781, and at 250 MHz it is 0.999965 — the approximation
improves as the loss tangent falls, as it must.

Three consequences, all of them counter-intuitive and all of them measurable in
the table:

1. **In the low-loss regime, lowering the frequency does not improve
   penetration at all.** $\alpha$ is frequency-independent there, so a 100 MHz
   antenna reaches exactly as deep as a 250 MHz one in the same dry sand
   (15.3 m versus 15.2 m at $\sigma = 0.005$) and simply resolves less. The
   familiar instruction to "use a lower frequency for more depth" is only
   correct where the loss tangent is large — that is, in the conductive ground
   where the low-loss approximations of Section 1 have already failed.
2. **Conductivity, not depth, sets penetration.** At 250 MHz, 60 dB of loss is
   reached at 15.2 m in a clean dry sand ($\sigma = 0.005$) and at 3.0 m in a
   clay-rich soil ($\sigma = 0.05$): a factor of 5.1 in depth from a factor of 10
   in conductivity. Since clay content and salinity both raise $\sigma$, GPR is
   a vadose-zone tool in temperate clay-bearing soils and a much deeper tool in
   arid, resistive ones.
3. **At fixed conductivity a wetter soil attenuates slightly less**, because
   $\alpha \to (\sigma/2)\sqrt{\mu_0/\varepsilon}$ falls as $\varepsilon$
   rises (7.99 versus 19.43 dB m$^{-1}$ at 100 MHz and $\sigma = 0.02$–0.05 with
   $\varepsilon$ changing from 16.59 to 4.30). **A survey that suddenly loses
   penetration almost always has a conductivity problem — clay, salinity or a
   contaminant — rather than a moisture problem.**

## 6. What GPR does and does not determine

| Quantity | Determined? | Why |
|---|---|---|
| volumetric water content $\theta$ | **yes**, to $\pm 0.01$–0.03 with calibration | permittivity is dominated by free water |
| water-table depth | **yes** in resistive soils, with the polarity diagnostic | the saturation step is a dielectric contrast |
| layer geometry (thickness, dip) | **yes**, to the resolution of the wavelet | travel-time measurement |
| pore-water salinity | **no** | it affects the conductivity (attenuation), not the permittivity appreciably |
| clay-bound water | **no** (it is under-counted) | bound water has $\varepsilon \approx 5$–6, not 81 |
| saturated hydraulic conductivity | **no** | no mechanistic link from permittivity |
| porosity | only with an independent constraint | $\theta = \phi S_w$ mixes the two |

The last row is the reason a GPR-derived water content cannot be converted to a
saturation without a porosity from elsewhere, and it is the same ambiguity that
[14-02-01](01-ert-for-hydrology.md) found in the resistivity direction — arriving
from the opposite end.

## 7. Python demonstration

`code/gpr_for_soil_moisture_demo.py` prints all of the above with units. It:

1. tabulates $\theta \to \varepsilon \to v$ and reports the 2.66× velocity range;
2. computes the surface and water-table reflection coefficients with their
   polarities, and shows how the water-table reflection weakens as the cover wets;
3. recovers velocities and depths from noisy synthetic moveout gathers for a dry
   and a moist soil, comparing them with the 50% error from assuming the velocity;
4. quantifies the calibration bias in a clay-bearing soil (a constant $-0.04$ in
   absolute terms, $-67\%$ relatively at $\theta = 0.06$);
5. computes the exact attenuation and its loss-tangent regime, tabulates the 60 dB
   depth against conductivity, permittivity and frequency, verifies the low-loss
   limit against the exact formula (ratio 0.9998 at 100 MHz), and prints the three
   counter-intuitive consequences;
6. verifies CRIM against its end-member limits ($\theta(0) = 0$ to
   $1.4 \times 10^{-17}$, $\theta(\phi) = 0.400000$), the dielectric and impedance
   forms of $R$ (agreeing to $0.00 \times 10^{0}$), and the moveout formula at
   zero offset.

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_for_soil_moisture_demo.py
```

## 8. Assumptions and regime of validity

1. **Low-loss, non-magnetic, non-dispersive.** The velocity $c/\sqrt{\varepsilon}$
   and the impedance form of $R$ both assume $\sigma/(\omega\varepsilon) \ll 1$.
   The demonstration measures the loss tangent for each case: it exceeds 1
   (high loss) at $\sigma = 0.05\ \mathrm{S\,m^{-1}}$ and 100 MHz with
   $\varepsilon = 4.3$, and reaches 8.4 at $\sigma = 0.2$. In that regime the
   velocity is dispersive, the reflection coefficient is complex, and the
   water-content inversion of Section 1 is unreliable — which is exactly the
   clay- and salt-rich ground where GPR struggles anyway. The failure is graceful
   (migration and amplitude interpretation degrade) rather than obvious.
2. **CRIM is a mixing model.** It assumes three phases with fixed permittivities and
   no clay-bound water. Its accuracy is limited by that assumption, and the bias is
   systematic and one-sided (Section 4).
3. **A flat, laterally uniform soil.** The common moveout formulae assume flat
   layering and a known antenna offset; in a 3-D heterogeneous soil the "velocity"
   recovered by NMO is an average that may not correspond to any interval.
4. **Antenna radiation and coupling.** Ground-coupled antennas vary their
   effective height and coupling with soil permittivity, and air-coupled antennas
   need a velocity-dependent height correction; ignoring either
   produces amplitude and velocity biases.
5. **Water content is free water only.** The measurement is insensitive to
   bound water, to ice (except where it changes the permittivity dramatically) and
   to vapour.
6. **No frequency dependence of the target property.** A wetting front thinner than
   the wavelength is a frequency-dependent, dispersive reflector; the amplitude
   analysis here assumes the front is thin compared with the pulse.
7. **The 60 dB convention is a convention.** Reporting a penetration depth without
   the dynamic range, frequency and conductivity is not reproducible.

## Mastery checkpoint

A synthetic sandy vadose zone has $\phi = 0.38$ and two layers: 1.5 m of soil at
$\theta = 0.08$ over soil at $\theta = 0.32$ with a water table at 1.5 m.

**(a)** Compute $\varepsilon$ and $v$ for both layers. **(b)** Compute the two-way
travel time to the water table. **(c)** Compute the reflection coefficient at the
water table and state its polarity. **(d)** Compute the depth error introduced by
converting the entire record with the dry-layer velocity. **(e)** The soil has
$\sigma = 0.03\ \mathrm{S\,m^{-1}}$. Compute the attenuation and the 60 dB depth at
200 MHz, and state whether the water table at 1.5 m is detectable with a stated
margin. **(f)** A gravimetric calibration is available at three points, and the
inferred water content is systematically 0.02 low. State two distinct physical
causes and the measurement that would distinguish them.

## Common pitfalls

1. **Using one velocity for the whole profile.** Across the water table the change
   is a factor of 2.7.
2. **Ignoring the polarity of the water-table reflection.** It is the diagnostic
   that separates a saturation front from a texture change.
3. **Treating a mixing model as a calibration.** A one-sided 0.04 bias in $\theta$
   looks completely plausible.
4. **Blaming moisture for a penetration failure.** The cause is usually
   conductivity.
5. **Reading salinity from permittivity.** Salinity moves the conductivity and the
   attenuation, not the permittivity.
6. **Converting water content to saturation without a porosity.** GPR measures
   $\theta$, not $S_w$.
7. **Quoting a penetration depth without the dynamic range and conductivity.**

## Related modules

- [10-01-01 GPR Physics](../../10-gpr-near-surface/01-gpr-principles/01-gpr-physics.md)
  and [10-01-05 GPR Resolution](../../10-gpr-near-surface/01-gpr-principles/05-gpr-resolution.md) —
  the theory and the resolution conventions.
- [10-02-03 GPR Velocity Analysis](../../10-gpr-near-surface/02-gpr-acquisition-and-processing/03-gpr-velocity-analysis.md) —
  the field implementation of the moveout analysis used in §3.
- [14-01-06 The Unsaturated Zone](../01-hydrology-fundamentals/06-unsaturated-zone.md) —
  what the water content means hydrologically.
- [14-02-03 Seismic Methods for Aquifer Geometry](03-seismic-hydrogeophysics.md) —
  the same reflection and moveout machinery with elastic impedances.
- [06 Near-Surface Monitoring](../05-hydrogeophysical-monitoring/README.md) — the
  time-lapse use of this measurement.

## Code and exercises

- Demonstration:
  [`code/gpr_for_soil_moisture_demo.py`](code/gpr_for_soil_moisture_demo.py)
- Exercises: [`exercises/04-gpr-for-soil-moisture-exercises.md`](exercises/04-gpr-for-soil-moisture-exercises.md)
- Worked solutions: [`exercises/04-gpr-for-soil-moisture-solutions.md`](exercises/04-gpr-for-soil-moisture-solutions.md)
