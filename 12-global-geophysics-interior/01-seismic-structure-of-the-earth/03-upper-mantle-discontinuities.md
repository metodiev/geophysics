---
id: 12-01-03
title: "Upper-Mantle Discontinuities at 410 and 660 km"
level: doctoral
prereqs: ["12-01-01", "12-01-02", "06-02-02", "02-05-06"]
tags: [global-geophysics, earth-interior, mantle-transition-zone, phase-transitions, clapeyron, precursors, sharpness]
---

# Upper-Mantle Discontinuities at 410 and 660 km

> **All models and data in this module are SYNTHETIC.** The Clapeyron slopes,
> densities, velocities, entropy and volume changes used here are chosen teaching
> values. The depths 410 km and 660 km are used as conventional labels for the
> two boundaries, not as measurements reported by this repository.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the topographic response of a phase boundary,
   $\mathrm{d}z/\mathrm{d}T = \gamma/(\rho g)$, from the boundary condition
   $P = P_0 + \gamma(T-T_0)$, and **derive** $\gamma = \Delta S/\Delta V$ from the
   Clapeyron–Clausius relation.
2. **Compute** the two-way delay of an underside reflection at a given slowness,
   and **invert** an observed delay change for boundary displacement and then for
   temperature.
3. **Explain** and **quantify** why the transition zone is an *amplified*
   thermometer: the two boundaries move in opposite directions, so the thickness
   sensitivity is the sum, not the difference, of the individual responses.
4. **Compute** normal-incidence reflection coefficients and **explain** why the
   "sharpness" of a boundary is a statement about a frequency band, not a length
   in kilometres.
5. **Quantify** the degeneracy between topography and velocity in a single delay,
   and state which additional observable breaks it.
6. **Explain** how a first-order jump in velocity produces a triplication, and
   how that appears as a discontinuity in $\mathrm{d}T/\mathrm{d}\Delta$.
7. **State** the assumptions that must hold before a measured boundary depth can
   be converted into a temperature.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the radial model and the slowness identity.
- [12-01-02 Crustal Structure and Continental vs Oceanic Crust](02-crustal-structure.md) —
  the depth–velocity trade-off in its simplest form.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter and vertical slowness.
- [02-05-06 Geotherms](../../02-physics/05-thermodynamics/06-geotherms.md) —
  how temperature varies with depth and why a boundary can be used as a
  thermometer at all.

## 1. Why a discontinuity in the mantle is a thermometer

The two boundaries near 410 and 660 km are not compositional interfaces. They are
**phase transitions**: at a particular pressure and temperature, one mineral
assemblage becomes another, and the change happens over a depth interval short
enough to look like a jump in seismic velocity.

The boundary is defined by a thermodynamic condition. Writing the transition
pressure as a linear function of temperature around a reference point,

$$P_\text{tr}(T) = P_0 + \gamma\left(T - T_0\right),
\qquad \gamma \equiv \left.\frac{\mathrm{d}P}{\mathrm{d}T}\right|_\text{boundary},$$

and noting that in a hydrostatic mantle the pressure at depth $z$ increases at
the rate $\rho g$,

$$z(T) = z_0 + \frac{\gamma\left(T - T_0\right)}{\rho g}
\qquad\Longrightarrow\qquad
\boxed{\;\frac{\mathrm{d}z}{\mathrm{d}T} = \frac{\gamma}{\rho g}.\;}$$

This single relation is the reason upper-mantle seismology is interesting. A
boundary whose depth can be *measured* and whose Clapeyron slope is *known*
becomes a thermometer. The demonstration evaluates it for chosen values
$\gamma_{410} = +2.0\ \mathrm{MPa\,K^{-1}}$, $\rho_{410} = 3600\
\mathrm{kg\,m^{-3}}$, $\gamma_{660} = -3.0\ \mathrm{MPa\,K^{-1}}$,
$\rho_{660} = 4400\ \mathrm{kg\,m^{-3}}$:

$$\frac{\mathrm{d}z_{410}}{\mathrm{d}T} = \frac{2.0\times10^{6}}{3600 \times 9.81}
= +56.63\ \mathrm{m\,K^{-1}},$$
$$\frac{\mathrm{d}z_{660}}{\mathrm{d}T} = \frac{-3.0\times10^{6}}{4400 \times 9.81}
= -69.50\ \mathrm{m\,K^{-1}}.$$

The signs carry the physics: **the 410 deepens when hot, the 660 shallows when
hot.** A 100 K anomaly moves them by 5.7 and 7.0 km in opposite directions.

### 1.1 Where the Clapeyron slope comes from

$\gamma$ is not a free parameter. For a phase change between two phases $\alpha$
and $\beta$ at equilibrium, the Gibbs energies are equal,
$G_\alpha = G_\beta$, and differentiating along the boundary gives the
**Clapeyron–Clausius relation**

$$\gamma = \frac{\mathrm{d}P}{\mathrm{d}T} = \frac{\Delta S}{\Delta V},$$

with $\Delta S = S_\beta - S_\alpha$ and $\Delta V = V_\beta - V_\alpha$ per mole.
The demonstration uses chosen values $\Delta S = -5.5\ \mathrm{J\,mol^{-1}\,K^{-1}}$
and $\Delta V = -2.6\times10^{-6}\ \mathrm{m^{3}\,mol^{-1}}$ for the 410, giving

$$\gamma = \frac{-5.5}{-2.6\times10^{-6}} = +2.12\ \mathrm{MPa\,K^{-1}},$$

within 6 % of the value assumed in the topography calculation — the difference is
simply that the two numbers were chosen independently. For the 660 the chosen
values are $\Delta S = +8.0$ and $\Delta V = -3.0\times10^{-6}$, giving
$\gamma = -2.67\ \mathrm{MPa\,K^{-1}}$

Because $\Delta S < 0$ at the 410, that transition releases heat (exothermic); the
660 is endothermic. This is not a curiosity: an exothermic transition that is
displaced downward by a cold downwelling also *helps* the downwelling, and an
endothermic one resists it. That mechanical feedback is one of the reasons
transition-zone topography is studied at all — it is a coupling between phase
changes and flow, treated in
[13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).

## 2. Measuring a boundary depth: the underside reflection

The cleanest depth measurement of these boundaries does not come from a ray that
passes through them, but from a ray that **reflects off the underside**. A
long-period S wave that has already bounced at the surface (the phase called SS)
can also reflect from the 410 or the 660 on its way, arriving tens of seconds
*before* the surface bounce. These are the **SS precursors**.

For a boundary at depth $z$ and a ray parameter $p$, the precursor arrives before
the surface reflection by the two-way path through the layer above:

$$\Delta t_\text{prec} = 2z\,q_s(p), \qquad
q_s(p) = \sqrt{v_s^{-2} - p^{2}}.$$

With $p = 0.055\ \mathrm{s\,km^{-1}}$ (a chosen teleseismic value) and the
demonstration's velocities:

| boundary | $v_s$ (km s$^{-1}$) | $q_s$ (s km$^{-1}$) | two-way delay (s) |
|---|---|---|---|
| 410 km | 4.70 | 0.20553 | 168.54 |
| 660 km | 5.80 | 0.16341 | 215.70 |

The two precursors are separated by **47.16 s**, which is twice the S travel time
across the transition zone at this slowness. That separation is a direct
measurement of transition-zone *thickness*, and it is the quantity that most
precursor studies fit.

Note the two structural differences from a direct-arrival depth measurement:

- the delay is **proportional to depth** ($\Delta t \propto z$), not to a
  difference of slownesses; the inversion is nearly linear;
- the path samples the *overlying* structure only, so a velocity error above the
  boundary enters directly, but the measurement is insensitive to what lies below.

## 3. From delay to topography to temperature

Differentiating $\Delta t = 2z q_s$ at fixed slowness,

$$\frac{\partial \Delta t}{\partial z} = 2q_s
= 2 \times 0.20553 = 0.41107\ \mathrm{s\,km^{-1}}$$

for the 410. The demonstration's table:

| $\Delta T$ (K) | $\delta z$ (km) | $\delta(\Delta t)$ (s) |
|---|---|---|
| −200 | −11.33 | −4.656 |
| −100 | −5.66 | −2.328 |
| −50 | −2.83 | −1.164 |
| +50 | +2.83 | +1.164 |
| +100 | +5.66 | +2.328 |
| +200 | +11.33 | +4.656 |

Inverting: a measured differential delay of $+1.00\ \mathrm{s}$ implies

$$\delta z = \frac{1.00}{2 \times 0.20553} = 2.433\ \mathrm{km}
\quad\Longrightarrow\quad
\Delta T = \frac{2433\ \mathrm{m}}{56.63\ \mathrm{m\,K^{-1}}}
= +43.0\ \mathrm{K}.$$

So a ~40 K temperature anomaly is a ~1 s precursor delay. That is *measurable*,
and it is why transition-zone topography is a standard tool. But note how many
inputs the last equality consumed: one measured delay, and then the assumed
$v_s$ (through $q_s$), the assumed $\gamma$, the assumed $\rho$, and the assumed
$g$ — four assumptions and one measurement, with the temperature error
inheriting all four.

## 4. The transition zone as an amplified thermometer

Because the two boundaries respond with opposite signs, the *thickness*
$H_{TZ} = z_{660} - z_{410}$ responds with the **sum** of the magnitudes:

$$\frac{\mathrm{d}H_{TZ}}{\mathrm{d}T} = \frac{\gamma_{660}}{\rho_{660}g}
- \frac{\gamma_{410}}{\rho_{410}g}
= -69.50 - 56.63 = -126.13\ \mathrm{m\,K^{-1}}.$$

The demonstration's table shows the mechanism explicitly:

| $\Delta T$ (K) | $\delta z_{410}$ (km) | $\delta z_{660}$ (km) | $\delta H_{TZ}$ (km) |
|---|---|---|---|
| −200 | −11.33 | +13.90 | +25.23 |
| −100 | −5.66 | +6.95 | +12.61 |
| +100 | +5.66 | −6.95 | −12.61 |
| +200 | +11.33 | −13.90 | −25.23 |

A 100 K cooling thickens the transition zone by **12.61 km** — twice what either
boundary alone would contribute. This amplification is the single most useful
property of the pair:

- the **thickness** is a thermometer with ~126 m K$^{-1}$ of leverage, roughly
  twice that of a single boundary;
- the **mean depth** $\left(z_{410}+z_{660}\right)/2$ responds to temperature with
  the *difference* of the coefficients, $-69.50 + 56.63 = -12.87\
  \mathrm{m\,K^{-1}}$ — nearly insensitive to temperature, and therefore a
  measure of something else (the average pressure of the transition, hence bulk
  composition).

A well-designed study fits the two depths separately precisely because the sum
and the difference of the two depths carry different physical information.

## 5. Reflection coefficients, and why "sharpness" is a band-limited statement

At normal incidence the amplitude reflection coefficient of a boundary is set by
the impedance contrast $Z = \rho v$:

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1}.$$

For the SYNTHETIC jumps of
[lesson 01](01-prem-and-reference-models.md) (an S-wave jump from
$(\rho, v_s) = (3.54, 4.66)$ to $(3.65, 4.80)$ at 410 km, and from
$(3.99, 5.55)$ to $(4.01, 5.85)$ at 660 km):

| boundary | $Z_1$ | $Z_2$ | $R$ |
|---|---|---|---|
| 410 km | 16.496 | 17.520 | +0.0301 (3.01 %) |
| 660 km | 22.145 | 23.458 | +0.0288 (2.88 %) |

A ~3 % reflection is small: the boundary is visible in long-period stacks
averaging many recordings, not in a single trace.

Now the important part. A boundary is never infinitely sharp. If the transition
takes a one-way time $\tau$ to complete, the reflection is filtered by the
Fourier transform of the ramp, which is a sinc:

$$R(f) = R_0\,\operatorname{sinc}\!\left(\pi f \tau\right)
= R_0\,\frac{\sin\left(\pi f \tau\right)}{\pi f \tau}.$$

The demonstration evaluates this at $f = 0.20\ \mathrm{Hz}$ (a 5 s period) for
transition widths $w$, with $\tau = w/v_s$:

| width (km) | $\tau$ (s) | $\lvert R\rvert/R_0$ |
|---|---|---|
| 0 | 0.000 | 1.0000 |
| 2 | 0.426 | 0.9881 |
| 5 | 1.064 | 0.9272 |
| 10 | 2.128 | 0.7277 |
| 20 | 4.255 | 0.1687 |
| 23.5 | 5.000 | 0.0000 |
| 40 | 8.511 | 0.1506 |

Three results to internalise:

1. **There is a null.** The reflection vanishes identically when $\tau = 1/f$:
   here 5.0 s, i.e. **23.5 km** of transition at 4.70 km s$^{-1}$. A boundary that
   is gradational over exactly that width is *invisible at that frequency* while
   being perfectly detectable at another.
2. **Beyond the null the amplitude returns** (the side lobe at 40 km, 15 % of
   $R_0$) **with reversed polarity**. A weak inverted reflection is therefore not
   evidence of a sharp interface; it may be a wide ramp.
3. **Sharpness is meaningless without a frequency.** "The boundary is sharp to
   better than 10 km" is a statement about the band in which it was measured. The
   same 10 km transition is sharp at 0.05 Hz ($\lvert R\rvert/R_0 = 0.99$) and
   invisible at 0.5 Hz (null at 9.4 km, side-lobe minimum near 10 km).

This is the *detection versus resolution* distinction in its purest form, and it
is the same mathematics that governs the receiver-function Moho
([06-08-03](../../06-seismology/08-receiver-functions-and-crustal-structure/03-moho-interface.md)).

## 6. One delay, two explanations: topography versus velocity

A precursor delay can change for two reasons: the boundary moves, or the velocity
above it changes. The demonstration quantifies the degeneracy:

$$\frac{\partial \Delta t}{\partial z} = 2q_s = +0.41107\ \mathrm{s\,km^{-1}},$$

while a fractional S-velocity change $\epsilon$ distributed over the whole
250 km transition zone changes the delay by

$$\delta(\Delta t) \approx 2H_{TZ}\,\frac{\epsilon}{v_s}
= 2 \times 250 \times \frac{0.01}{4.70} = 1.064\ \mathrm{s}
\quad \left(\epsilon = 0.01\right),$$

i.e. $-106.4\ \mathrm{s}$ per unit fractional velocity change — but note the sign:
a velocity *reduction* makes the precursor arrive *later*, the same sense as
moving the boundary *down*.

Equating the two responses, **1 % of S velocity is exactly equivalent to
2.59 km of boundary displacement** in a single delay measurement. The two
mechanisms are degenerate: a cold anomaly that lifts the 410 by 5 km produces the
same precursor timing as a warm anomaly that slows the overlying transition zone
by 2 %.

Breaking the degeneracy requires a second, differently weighted observation.
Three standard routes:

- **Moveout.** Topography and velocity have different dependence on $p$: the
  topographic term is $\propto q_s(p) \approx v_s^{-1} - \tfrac12 p^2 v_s$, while
  the velocity term carries $H_{TZ}$ and the local gradient. Measuring the
  precursor delay at several slownesses separates them in principle, though
  slowly.
- **An absolute constraint on one of them.** A tomographic model with independent
  resolution of the transition zone fixes $\epsilon$, leaving $z$.
- **A different phase.** A transmitted phase (a triplication, Section 7) samples
  the jump itself rather than the path above it.

Reporting a boundary depth from precursors without stating the velocity model is
therefore the same overclaim as reporting a crustal thickness without one.

## 7. Triplication: what a first-order jump does to travel times

A jump in velocity produces a *fold* in the travel-time curve. Rays that turn
slightly above the boundary, rays that graze it, and rays that turn just below it
all arrive at similar distances but with different times — three branches at the
same $\Delta$, a **triplication**. Because $\mathrm{d}T/\mathrm{d}\Delta = p$, the
signature is a discontinuity in the observed slowness: the branch above the jump
has a *large* $p$, the branch below has a *small* one, and there is a gap between
them.

The demonstration computes $U = r/v$ on either side of a SYNTHETIC 410 km jump
from 8.90 to 9.60 km s$^{-1}$:

| side | $r$ (km) | $U = r/v$ (s rad$^{-1}$) |
|---|---|---|
| above the jump | 5962.0 | 669.89 |
| below the jump | 5960.0 | 620.83 |

so $p$ drops by 49.05 s rad$^{-1}$ (7.9 %) across the boundary. Every ray with $p$
in that interval turns *within a kilometre* of the same depth and therefore
arrives at nearly the same distance at nearly the same time — that is the physical
origin of the enhanced amplitude near a triplication, and of the characteristic
"three arrivals" pattern in a record section.

By contrast, a smooth velocity gradient gives a continuous $p(\Delta)$: no gap, no
triplication, and no travel-time evidence of a "discontinuity" at all. An observed
triplication is thus a *sharpness* measurement of the same kind as Section 5, but
performed with travel times instead of amplitudes. The two are not
interchangeable: the amplitude method favours long periods (the sinc filter
becomes more permissive as $f \to 0$), while long periods smear the triplication
in distance.

## 8. Assumptions and regime of validity

Each step of the inference chain in this lesson has its own regime:

1. **Hydrostatic pressure.** $\mathrm{d}P/\mathrm{d}z = \rho g$ assumes no
   deviatoric stress. In a vigorously convecting mantle the dynamical pressure can
   be a few hundred MPa, which displaces a boundary by kilometres — the same size
   as the thermal signal. This is a real, not hypothetical, limit to
   "topography = temperature".
2. **Linear Clapeyron slope.** $\gamma$ is itself temperature-dependent, and for
   the 660 the transition has a finite width (the assemblage change is spread over
   a depth range). Over a ±200 K interval the linear form is an approximation
   whose error is rarely reported.
3. **Known $\gamma$.** The conversion of depth to temperature is only as good as
   the experimental or computed Clapeyron slope, which carries uncertainties of
   tens of per cent (see
   [12-02-02 High-Pressure Experiments](../02-composition-and-mineral-physics/02-high-pressure-experiments.md)
   and [12-02-03 Ab Initio Mineral Physics](../02-composition-and-mineral-physics/03-ab-initio-mineral-physics.md)).
4. **Single-arrival picking.** Precursor stacks contain several phases; a
   mis-identified phase contaminates both the depth and its apparent lateral
   variation.
5. **Lateral homogeneity along the path.** A precursor samples a broad region; a
   reported "depth" is a path average over thousands of kilometres.
6. **Elastic isotropy** (Section 5's impedance formula) and **no attenuation**.
   Attenuation broadens pulses the same way a gradient does, so a wide transition
   and a strongly attenuating one are partially degenerate.
7. **The sinc filter assumes a linear ramp.** A different transition profile (a
   sigmoid, or a two-stage transformation) filters differently, and the
   "sharpness" recovered then depends on the assumed profile shape.

## 9. Worked examples

### Example 1 — temperature from a two-boundary fit

A study reports a transition-zone thickness of $248.0\ \mathrm{km}$ for a region,
against a reference of $250.0\ \mathrm{km}$, with the two boundaries displaced
symmetrically about the reference mid-depth. Using the demonstration's
sensitivities:

$$\delta H_{TZ} = -2.0\ \mathrm{km} = -126.13\ \mathrm{m\,K^{-1}} \times \Delta T
\times 10^{-3}\ \mathrm{km\,m^{-1}},$$
$$\Delta T = \frac{-2.0}{-0.12613} = +15.9\ \mathrm{K}.$$

The region is ~16 K warm. If instead the reference thickness were uncertain at
±3 km (a realistic systematic), the temperature is uncertain at
$3/0.126 = \pm23.8\ \mathrm{K}$ — the systematic dominates the signal. **This
ratio, not the measurement precision, is what limits the method.**

### Example 2 — a precursor delay and its two explanations

A stacked SS precursor section gives a 410 delay of 166.0 s where a reference
model predicts 168.5 s, i.e. $\delta(\Delta t) = -2.5\ \mathrm{s}$ at
$p = 0.055\ \mathrm{s\,km^{-1}}$.

*Topographic interpretation:*

$$\delta z = \frac{-2.5}{2 \times 0.20553} = -6.08\ \mathrm{km}
\;\Rightarrow\;
\Delta T = \frac{-6080}{56.63} = -107\ \mathrm{K}.$$

*Velocity interpretation:* from Section 6, the velocity coefficient is
$-106.4\ \mathrm{s}$ per unit $\epsilon$, so

$$\epsilon = \frac{-2.5}{-106.4} = +0.0235,$$

a 2.35 % *increase* in S velocity over the transition zone. A 2.4 % velocity
increase at these depths is far outside the plausible range for a thermal
anomaly (which would be accompanied by a *lower* velocity, not a higher one, and
the sign of the topographic effect requires a cold anomaly while the velocity
interpretation requires a fast one — so here the two are not just degenerate,
they are *incompatible* under the assumption that the velocity change is thermal).
The resolution: a fast, cold region lifts the 410 (−107 K) and should also raise
$v_s$, and 2.4 % is too large for 107 K at the assumed sensitivity. Either the
region has a compositional component, or the reference model's velocity above
410 km is wrong for this path. **Both explanations are inconsistent with a purely
thermal, laterally homogeneous mantle** — which is the useful conclusion, and one
that a single-method study could not reach.

### Example 3 — the depth of the null for a sharpness claim

A reflection is detected at 0.5 Hz with an amplitude half the value expected for a
sharp boundary, i.e. $\operatorname{sinc}(\pi f \tau) = 0.5$ for
$f = 0.5\ \mathrm{Hz}$. The first solution is $\pi f \tau = 1.8955$ rad, so

$$\tau = \frac{1.8955}{\pi \times 0.5} = 1.207\ \mathrm{s}
\quad\Longrightarrow\quad
w = v_s \tau = 4.70 \times 1.207 = 5.67\ \mathrm{km}.$$

Reporting "the transition is gradational over about 5.7 km" is legitimate; it is
conditional on the linear-ramp model and on the frequency. At 0.05 Hz the same
5.7 km would give $\operatorname{sinc}(0.18955) = 0.994$ — indistinguishable from
sharp. **Any sharpness number must come with its band.**

## 10. Python demonstration

`code/upper_mantle_discontinuities_demo.py` computes: the topographic response
from $\gamma/(\rho g)$ with an independent $\gamma = \Delta S/\Delta V$ check; the
precursor delays; the topography-to-delay table and its inversion; the summed
transition-zone sensitivity; the reflection coefficients and the sinc filter;
the topography/velocity degeneracy with explicit coefficients; and the $p$ jump
across a first-order interface. It prints labelled results with units and runs in
under a second:

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python upper_mantle_discontinuities_demo.py
```

## 11. Exercises

Full sets with worked solutions are in
[`exercises/03-upper-mantle-discontinuities-exercises.md`](exercises/03-upper-mantle-discontinuities-exercises.md)
and
[`exercises/03-upper-mantle-discontinuities-solutions.md`](exercises/03-upper-mantle-discontinuities-solutions.md).

- **★** Compute $\mathrm{d}z/\mathrm{d}T$ and the precursor delay for a boundary.
- **★★** Invert a delay pair (410 and 660) for a temperature anomaly and a
  composition-sensitive mean depth.
- **★★** Compute the transition width that nulls a reflection at a stated
  frequency.
- **★★★** Design a precursor study that separates topography from velocity, with
  a predicted error budget.

## Mastery checkpoint

Without notes:

> A region has its 410 km boundary displaced by $-4.0\ \mathrm{km}$ and its 660 km
> boundary by $+5.5\ \mathrm{km}$ relative to a reference model.
> **(a)** Compute the transition-zone thickness change and the temperature anomaly
> implied by the demonstration's coefficients.
> **(b)** Compute the precursor delay change for a boundary at 410 km at
> $p = 0.055\ \mathrm{s\,km^{-1}}$, $v_s = 4.70\ \mathrm{km\,s^{-1}}$.
> **(c)** A tomographic model instead prefers a 1.5 % S-velocity reduction across
> the transition zone. Which explanation does the delay in (b) favour, and by how
> much?
> **(d)** State what additional measurement would settle the question.

A worked version appears in the lesson-03
[solutions](exercises/03-upper-mantle-discontinuities-solutions.md).

## Common pitfalls

1. **Treating the transition zone as one boundary.** Its two boundaries move in
   opposite directions; a single "transition-zone depth" throws away the
   amplification that makes the pair useful.
2. **Converting depth to temperature without stating $\gamma$.** The conversion
   factor is $\gamma/(\rho g)$, and $\gamma$ carries tens of per cent uncertainty.
3. **Quoting a transition width in kilometres with no frequency.** Section 5: the
   reflection *vanishes* at $\tau = 1/f$.
4. **Reading a side lobe as a second boundary.** Past the first null the sinc
   returns with reversed polarity.
5. **Forgetting dynamical pressure.** Deviatoric stresses displace boundaries by
   kilometres, the same order as the thermal signal.
6. **Assuming a velocity anomaly and a topography anomaly are the same
   measurement.** They are degenerate in one delay (2.59 km per 1 % here) and can
   even have incompatible signs (Example 2).
7. **Ignoring the overlying structure.** The precursor samples everything above
   the boundary; a wrong $q_s$ is a wrong depth, one-for-one.

## Related modules

- [01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the reference profile the displacements are measured against.
- [02 Crustal Structure and Continental vs Oceanic Crust](02-crustal-structure.md) —
  the same depth-versus-velocity logic at the Moho.
- [04 Lower-Mantle Heterogeneity and LLSVPs](04-lower-mantle-heterogeneity.md) —
  what happens when the 1-D assumption is dropped for the deeper mantle.
- [06-06-06 Global Mantle Tomography and Its Geodynamic Interpretation](../../06-seismology/06-seismic-tomography/06-global-mantle-tomography.md) —
  the tomographic models that provide the velocity side of the degeneracy.
- [12-02-03 Ab Initio Mineral Physics and Elastic Constants](../02-composition-and-mineral-physics/03-ab-initio-mineral-physics.md) —
  where $\gamma$ and the elastic contrasts come from.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — the
  mechanical feedback between phase transitions and mantle flow.

## Self-assessment checklist

- [ ] I can derive $\mathrm{d}z/\mathrm{d}T = \gamma/(\rho g)$ and
      $\gamma = \Delta S/\Delta V$.
- [ ] I can compute a precursor delay and invert a delay change for depth.
- [ ] I can compute a temperature anomaly from a boundary displacement, and state
      the four assumptions it consumed.
- [ ] I can explain why the transition-zone thickness sensitivity is a sum.
- [ ] I can compute a reflection coefficient from $\rho$ and $v_s$.
- [ ] I can find the frequency at which a given ramp is invisible.
- [ ] I can quantify the topography/velocity degeneracy in seconds and kilometres.
- [ ] I can state what a triplication measures that an amplitude does not.
