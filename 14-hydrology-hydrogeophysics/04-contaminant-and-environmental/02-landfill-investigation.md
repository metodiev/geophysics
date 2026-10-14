---
id: 14-04-02
title: "Landfill Investigation and Leachate Mapping"
level: graduate
prereqs: ["14-04-01", "14-01-02", "09-02-04", "09-04-01", "14-03-02"]
tags: [hydrology, hydrogeophysics, landfill, leachate, dc-resistivity, sounding, self-potential, water-balance, dupuit]
---

# Landfill Investigation and Leachate Mapping

> **All models and data in this module are SYNTHETIC.** The landfill, the
> leachate, the layer resistivities, the recharge rate and the self-potential
> source strength are chosen teaching values for an idealised archetype. No real
> site, licence, regulation, waste stream or discharge limit is described.

An old landfill is a three-part system: a waste body whose permeability and
water content control how much rain becomes leachate, a leachate plume that
travels with the groundwater, and a geological substrate that decides where it
goes. Geophysics is used at all three scales, and this lesson treats each with a
model that can be written down and checked: a Dupuit mound for the hydrological
part, a genuine two-layer Wenner forward model for the sounding, and a compact
current source for the self-potential signature.

The mathematical centrepiece is the two-layer apparent-resistivity series, which
is derived here from the image solution rather than quoted, and which is then
used twice: once to ask what a sounding can resolve, and once to ask what it
*cannot* — the admitted set of models that fit the same curve within a stated
noise level.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the steady Dupuit mound $h = w b^{2}/(2T)$ above a strip source,
   and **compute** how it scales with recharge, source width and transmissivity.
2. **Derive** the two-layer Wenner apparent-resistivity series from the image
   solution for a point source on a layered half-space.
3. **Verify** a forward model against its analytic limits rather than against
   intuition, and **state** the two limits used here.
4. **Compute** the bulk resistivity of a leachate-affected layer from a stated
   mixing relation and Archie's law, and **state** every assumption.
5. **Choose** the electrode spacings that carry the most information about layer
   depth, and **explain** why neither very small nor very large spacings do.
6. **Compute** the admitted set of layer models for a stated noise level, and
   **explain** why the classical equivalence is weaker than it is often assumed
   to be for a two-layer earth.
7. **Interpret** a self-potential hump as a source location rather than a source
   strength, and **explain** why.

## Prerequisites

- [14-04-01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md) —
  the concentration-to-property-to-data chain this lesson reuses.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md) —
  transmissivity and the aquifer/aquitard distinction.
- [09-02-04 Sounding and Profiling](../../09-electrical-em-methods/02-dc-resistivity/04-sounding-profiling.md) —
  the array geometries and the geometric factor.
- [09-04-01 Self-Potential Sources](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md) —
  electrochemical and streaming potentials.
- [14-03-02 Archie's Law and Saturation Estimation](../03-petrophysics-hydrology/02-archie-and-saturation.md) —
  the pore-fluid-to-bulk conversion.

## 1. Intuition: three questions, three models

A landfill investigation asks three questions, each with its own physics.

- **How much leachate is being produced, and where is it going?** A water balance
  on the waste body, then a flow model of the substrate. The output is a flux and
  a mound height.
- **Where is the leachate in the subsurface now?** A property model: leachate
  raises the pore-fluid conductivity, and that is what a resistivity survey sees.
- **What is the substrate that controls the path?** A structural model: layer
  resistivities and thicknesses, which is what a sounding measures.

Confusing the three is the standard failure. A conductive anomaly in the third
category (a clay layer) is not evidence of the second (leachate), and a mound
height calculated in the first category is not a depth to contamination.

## 2. The water balance and the mound

Let $P$ be the precipitation rate, $ET$ the evapotranspiration, $I$ the
interception and runoff, and $w$ the **percolation** reaching the base of the
waste. Then

$$
w = P - ET - I, \qquad (\mathrm{m\,day^{-1}}),
$$

and the leachate volume per unit area per unit time is $w$ when the waste is at
field capacity. Two things follow. First, the leachate flux is controlled by the
*cover*, not by the waste: sealing a cover reduces $w$ directly. Second, the
mound that the leachate forms above the regional water table depends on $w$ and
on the substrate transmissivity.

**Dupuit derivation.** Consider a one-dimensional strip source of half-width $b$
with uniform recharge $w$, over an aquifer of transmissivity $T$, with a fixed
head $h_0$ at the edges $x = \pm b$ and symmetry at the centre. Steady
conservation of water for a column of width $\mathrm{d}x$ gives

$$
T\frac{\mathrm{d}^{2}h}{\mathrm{d}x^{2}} = -w,
\qquad
h(x) = h_0 + \frac{w}{2T}\left(b^{2} - x^{2}\right),
$$

using $\mathrm{d}h/\mathrm{d}x = 0$ at $x = 0$ to fix the constant. The mound is
therefore greatest at the centre:

$$
\boxed{\;\Delta h_\text{max} = \frac{w\,b^{2}}{2T}\;}
$$

The **square** on $b$ is the whole engineering content: doubling the landfill
footprint quadruples the mound (and the gradient that drives leachate outward).

## 3. Deriving the two-layer Wenner apparent resistivity

**Potential of a point source on a layered half-space.** A current $I$ injected
at the surface of a two-layer earth ($\rho_1$ over $\rho_2$ with the interface at
depth $h$) produces, at surface distance $r$,

$$
V(r) = \frac{\rho_1 I}{2\pi}\left[\frac{1}{r}
+ 2\sum_{n=1}^{\infty}\frac{k^{n}}{\sqrt{r^{2} + (2nh)^{2}}}\right],
\qquad
k = \frac{\rho_2 - \rho_1}{\rho_2 + \rho_1},
$$

where $k$ is the reflection coefficient. The series is the image solution: the
$n$-th term is a reflection of the source in the interface, at effective depth
$2nh$. Each term follows from
$\int_0^{\infty} k^{n}e^{-2n\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda
= k^{n}/\sqrt{r^{2}+(2nh)^{2}}$.

**The Wenner array.** Electrodes at $x = 0, a, 2a, 3a$, current into 0 and out of
$3a$, potential difference measured between $a$ and $2a$. Summing the two
current sources and using $\rho_a = 2\pi a\,\Delta V/I$ gives, after the inner
potentials combine,

$$
\boxed{\;
\rho_a = \rho_1\left[1 + 4a\sum_{n=1}^{\infty}k^{n}
\left(\frac{1}{\sqrt{a^{2}+4n^{2}h^{2}}}
- \frac{1}{\sqrt{4a^{2}+4n^{2}h^{2}}}\right)\right].}
$$

**Two analytic limits, which are the implementation check.**

*Small spacing.* As $a \to 0$ every term of the sum vanishes
($1/(2nh) - 1/(2nh) \to 0$), so $\rho_a \to \rho_1$: a small array samples only
the top layer.

*Large spacing.* As $a \to \infty$ each bracket tends to
$1/a - 1/(2a) = 1/(2a)$, so
$4a\sum k^n/(2a) = 2k/(1-k) = (\rho_2-\rho_1)/\rho_1$ and therefore
$\rho_a \to \rho_1 + (\rho_2 - \rho_1) = \rho_2$: a large array samples only the
bottom layer.

Both limits are printed by the demonstration. For the synthetic model
$\rho_1 = 60$, $\rho_2 = 400\ \Omega\,\mathrm{m}$, $h = 8\ \mathrm{m}$ the code
returns $60.0000\ \Omega\,\mathrm{m}$ at $a = 10^{-3}\ \mathrm{m}$ and
$399.9998\ \Omega\,\mathrm{m}$ at $a = 10^{5}\ \mathrm{m}$. **A forward model that
fails its own limits is not a model**; this is the first check to run, before any
inversion.

## 4. Worked example 1 — mound, then resistivity

**Problem.** (a) A synthetic landfill half-width $b = 100\ \mathrm{m}$ generates
percolation $w = 5.0\times10^{-4}\ \mathrm{m\,day^{-1}}$ over an aquifer of
transmissivity $T = 10\ \mathrm{m^{2}\,day^{-1}}$. Compute the steady mound rise.
(b) The leachate-affected pore fluid has a conductivity corresponding to $750$
CU on the synthetic relation $\sigma_w = 0.050 + 1.0\times10^{-4}C$; with
$\phi = 0.30$, $a = 1$, $m = 2$, compute its bulk resistivity and the contrast
against clean water.

**Solution (a).**

$$
\Delta h_\text{max} = \frac{w b^{2}}{2T}
= \frac{5.0\times10^{-4}\times100^{2}}{2\times10}
= \frac{5.0}{20} = 0.2500\ \mathrm{m} .
$$

The demonstration also gives the scaling table: doubling $w$ doubles the mound
($1.0000\ \mathrm{m}$), and doubling $b$ quadruples it ($1.0000\ \mathrm{m}$ for
$w = 5.0\times10^{-4}$ and $b = 200\ \mathrm{m}$). The mound is inversely
proportional to $T$, by the formula as derived.

**Solution (b).**
$\sigma_w = 0.050 + 1.0\times10^{-4}\times750 = 0.125\ \mathrm{S\,m^{-1}}$, so
$\sigma_b = \phi^{m}\sigma_w = 0.09\times0.125 = 0.01125\ \mathrm{S\,m^{-1}}$ and
$\rho_b = 88.9\ \Omega\,\mathrm{m}$ against $222.2\ \Omega\,\mathrm{m}$ for clean
water: **a factor of 2.50**. This is the contrast a sounding must resolve — and
it is entirely a fluid effect, so it is independent of the rock type.

## 5. Worked example 2 — the sounding curve and where the information is

**Problem.** For $\rho_1 = 60$, $\rho_2 = 400\ \Omega\,\mathrm{m}$,
$h = 8\ \mathrm{m}$, compute $\rho_a$ at $a = 0.5, 2, 10, 50\
\mathrm{m}$, and find where a 10% error in $h$ changes $\rho_a$ most.

**Solution.** From the series (the demonstration prints the same values):

| $a$ (m) | 0.5 | 2.0 | 10.0 | 50.0 |
|---|---|---|---|---|
| $\rho_a$ ($\Omega\,\mathrm{m}$) | 60.01 | 60.55 | 90.90 | 245.87 |
| fraction of the way to $\rho_2$ | 0.000 | 0.002 | 0.091 | 0.546 |

The curve reaches 50% of the full contrast only at $a \approx 41\ \mathrm{m}$,
about five times the layer thickness — the classic result that a DC sounding
needs spacings comparable to *several* times the target depth.

The sensitivity to a 10% thickness error, printed as the fractional change in
$\rho_a$:

| $a/h$ | 0.25 | 0.50 | 1.00 | 2.00 | 4.00 |
|---|---|---|---|---|---|
| $\Delta\rho_a/\rho_a$ | $-0.0022$ | $-0.0136$ | $-0.0456$ | $-0.0638$ | $-0.0545$ |

The maximum is near $a/h \approx 2$: small spacings never leave the cover, and
large spacings average the two layers and lose the depth resolution. **Acquisition
design means choosing $a/h$, not adding electrodes.**

## 6. The admitted set

What a sounding actually delivers is not a pair of numbers but the set of models
consistent with the data at the stated noise. The demonstration computes, for
every $(\rho_1, h)$ pair on a grid with $\rho_2$ fixed, the rms difference from
the reference curve in $\log\rho_a$, and reports the set admitted at $5\%$ and
$10\%$ noise:

| noise level | admitted $\rho_1$ ($\Omega$ m) | admitted $h$ (m) | number of pairs |
|---|---|---|---|
| 5% | 60 (grid resolution) | 7.5 – 9.0 | 4 |
| 10% | 55 – 65 | 6.0 – 10.5 | 21 |

And the trade-off is monotone — a more conductive cover must be thinner to fit:

| $\rho_1$ ($\Omega$ m) | best $h$ (m) | typical misfit |
|---|---|---|
| 40 | 4.5 | 27.5% |
| 50 | 6.0 | 12.2% |
| 60 | 8.0 | 0.0% |
| 70 | 10.0 | 10.7% |
| 80 | 11.5 | 21.2% |
| 100 | 15.5 | 42.0% |

**Read this honestly.** With the half-space resistivity fixed, the two-layer
curve is *well determined*: the best alternative anywhere in the family is 10%
away, and everything beyond $\rho_1 = 80\ \Omega\,\mathrm{m}$ is 20% or more
away. The classical thin-layer equivalence — that the sounding determines only
the conductance $h/\rho$ of a thin layer — requires the layer to be thin compared
with its depth *and* a much wider spacing range than one decade. Reporting
"equivalence" as an excuse for a two-layer curve is not supported by the numbers;
reporting the admitted set at a stated noise level is.

## 7. Self-potential: a location, not a strength

Redox reactions at the edge of a leachate plume drive electrochemical current
that appears at the surface as a self-potential anomaly. The simplest teaching
model is a compact current source of strength $I$ at depth $d$ in a half-space of
resistivity $\rho$:

$$
V(x) = \frac{\rho I}{2\pi\sqrt{x^{2} + d^{2}}} .
$$

For the synthetic values $\rho = 100\ \Omega\,\mathrm{m}$,
$I = 0.05\ \mathrm{A}$ equivalent, $d = 6\ \mathrm{m}$, the demonstration prints
a peak of $132.6\ \mathrm{mV}$ at $x = 0$ falling to $19.7\ \mathrm{mV}$ at
$x = \pm 40\ \mathrm{m}$, a peak-to-offset amplitude of $94.5\ \mathrm{mV}$.

Two properties deserve emphasis. The anomaly is a **single-signed hump** whose
half-width is the source depth, so SP locates a source well. But $\rho$ and $I$
enter only as the product: a strong source in a resistive medium and a weak one
in a conductive medium are indistinguishable. SP gives a map of where the redox
activity is, and no map at all of how much there is. Pairing it with the
resistivity model is what converts an anomaly into a hypothesis.

## 8. Assumptions and regime of validity

**Water balance and Dupuit mound.** (i) Steady state — a mound takes years to
equilibrate and the seasonality is real. (ii) Uniform recharge over the strip and
uniform $T$. (iii) The Dupuit assumption (horizontal flow, hydrostatic pressure),
which fails near the edges where the gradients are largest. (iv) No leakage
through the base, no regional gradient. A regional flow field tilts the mound and
advects it downstream, so the observed mound is not centred on the source.

**Two-layer sounding.** (i) The Earth is two layers, flat and homogeneous within
each, and isotropic. Three layers are the norm in a real basin, and a two-layer
inversion of a three-layer curve is the most common damaging error in this
subject. (ii) Surface electrodes, no topography. (iii) The current is DC, or low
enough in frequency that induced polarisation is negligible; in clay-rich ground
it is not, and the discrepancy appears as an apparent resistivity that depends on
frequency. (iv) Apparent resistivity must be inverted with a model; the values in
the table are a forward calculation, not an inversion.

**Leachate as a conductive fluid.** As lesson 01 §6: a clean matrix, a known
porosity, full saturation, and a stated concentration-to-conductivity relation.
A clay liner or a clay-rich natural substrate adds a parallel conduction path and
will be misread as leachate.

## 9. Python demonstration

[`code/landfill_investigation_demo.py`](./code/landfill_investigation_demo.py)
prints the two-layer series with both analytic limits, a sounding curve, the
Dupuit mound table, the leachate resistivity conversion, the depth-sensitivity
table, the admitted sets, the monotone trade-off, and the self-potential profile.

```bash
cd 14-hydrology-hydrogeophysics/04-contaminant-and-environmental/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landfill_investigation_demo.py
```

## 10. Exercises

Graded problems are in
[`exercises/02-landfill-investigation-exercises.md`](./exercises/02-landfill-investigation-exercises.md)
with worked solutions in
[`exercises/02-landfill-investigation-solutions.md`](./exercises/02-landfill-investigation-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Derive $\Delta h_\text{max} = wb^{2}/(2T)$ and state the four
> assumptions. **(b)** A site has $w = 2.0\times10^{-3}\ \mathrm{m\,day^{-1}}$,
> $b = 50\ \mathrm{m}$ and $T = 20\ \mathrm{m^{2}\,day^{-1}}$; compute the mound.
> What happens to it if the cover is improved so that $w$ falls by a factor of
> four, and what happens if the site is doubled in width instead? **(c)** Write
> the two-layer Wenner series and state the two limits that check it.
> **(d)** For $\rho_1 = 60$, $\rho_2 = 400\ \Omega\,\mathrm{m}$,
> $h = 8\ \mathrm{m}$, at which $a/h$ is a thickness error best resolved, and
> why is it neither 0.1 nor 10? **(e)** A resistivity survey shows a conductive
> layer. Name three non-leachate explanations and the constraint that separates
> each.

## Common pitfalls

1. **Calling a conductive anomaly "leachate".** A clay layer is the alternative
   hypothesis until a clay indicator says otherwise.
2. **Inverting a three-layer curve with a two-layer model.** The fitted thickness
   is then an artefact of the model, not of the ground.
3. **Using the smallest electrode spacing "for resolution".** The information is
   at $a/h \approx 1$–$2$.
4. **Treating a mound as a depth to contamination.** The mound is a head
   perturbation; the plume is advected by the whole flow field.
5. **Reading an SP amplitude as a source strength.** $\rho I$ is not separable
   from the potential alone.
6. **Forgetting that the water balance controls the leachate flux.** Cover
   design is often more effective than any remediation of the plume.
7. **Reporting a two-layer model as unique.** Report the admitted set at a stated
   noise level.

## Related modules

- [01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md) —
  the transport model this lesson's leachate field obeys.
- [03 Seawater Intrusion and Coastal Aquifer Monitoring](03-saline-intrusion.md) —
  the same sounding applied to a sharper, denser contrast.
- [04 Acid Mine Drainage and Mining Environmental Geophysics](04-acid-mine-drainage.md) —
  a leachate generated by reaction rather than by percolation.
- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  aquifers, transmissivity, well hydraulics.
- [Module 09-02 DC Resistivity and ERT](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  arrays, sounding curves and inversion.
- [Module 09-04 Self-Potential and Mise-à-la-Masse](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/README.md) —
  the sources behind Section 7.
