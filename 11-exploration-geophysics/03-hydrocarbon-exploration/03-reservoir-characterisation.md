---
id: 11-03-03
title: "Reservoir Characterisation and Property Prediction"
level: research
prereqs: ["11-03-01", "11-03-02", "05-04-03", "06-09-05"]
tags: [exploration-geophysics, reservoir-characterisation, rock-physics, bayesian, quantitative-interpretation]
---

# Reservoir Characterisation and Property Prediction

**All models and data in this module are SYNTHETIC.** The sand model, its
mineral and fluid constants, the facies spreads and the prior probabilities
below are chosen teaching values, not measurements from any field. No well,
reservoir or company is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** a rock-physics model (dry moduli, fluid mixing, Gassmann,
   density) and **compute** $v_p$, $v_s$, $\rho$, acoustic impedance and
   $v_p/v_s$ for a stated porosity and saturation.
2. **Derive** the fluid-mixing relations (Wood's equation and arithmetic density
   mixing) and **state** why Gassmann leaves the shear modulus unchanged.
3. **Quantify** the sensitivity of impedance and $v_p/v_s$ to a fluid
   substitution, and **show** which attribute carries which information.
4. **Construct** the equal-impedance curve and **demonstrate** that one
   attribute constrains porosity while leaving saturation free.
5. **Compute** a Bayesian posterior facies probability from two attributes and
   **explain** the base-rate effect on precision and recall.
6. **Quantify** the ambiguity between net-to-gross and clean-sand porosity at
   a fixed impedance.
7. **State** the scale at which a seismic property is defined and **explain**
   why permeability is not among the predictable properties.

## Prerequisites

- [11-03-01 Reflection Seismic in Exploration](01-seismic-in-exploration.md) —
  resolution and the meaning of an amplitude.
- [11-03-02 Seismic Stratigraphy and Sequence Interpretation](02-seismic-stratigraphy.md) —
  thin-bed interference, which limits what any of this can claim.
- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  the derivation of the fluid-substitution equation is there; this lesson uses
  it and quantifies its consequences.
- [06-09-05 AVO/AVA Analysis and Its Assumptions](../../06-seismology/09-reflection-seismology/05-amplitude-vs-offset.md) —
  where angle-dependent amplitudes come from.

## 1. What can and cannot be predicted

Quantitative interpretation (QI) predicts **bulk elastic properties** of a
resolution cell: impedance, $v_p/v_s$, density, and from those a rock-physics
model's worth of porosity and saturation estimates. It does not predict
permeability, connectivity, relative permeability, or producibility. Those are
pore-scale and network properties, and no surface measurement touches them:
the demonstration measures the scale gap — a $25\times25\times10$ m resolution
cell is $6250\ \mathrm{m^3}$, a $25$ mm × $50$ mm core plug is
$24.5\ \mathrm{cm^3}$, and the ratio is $2.5\times10^{8}$. At a 0.1 mm grain
size the same cell contains of order $10^{15}$ grains, and the wavelength at
30 Hz in a 3 km/s rock exceeds a grain by $10^{6}$.

Everything below is therefore a statement about a **bulk average over a
cell**, with two consequences that the demonstrations quantify: several
different rocks produce the same average (§4, §6), and the average is defined
only where the geophysical measurement is defined (§7).

## 2. The rock-physics model

The workflow is a chain, and each link adds an assumption:

**(a) Dry-rock moduli.** A simple, explicit model is critical porosity: with
mineral modulus $K_m$, shear modulus $\mu_m$ and porosity $\phi$,

$$K_{\text{dry}} = K_m\left(1-\frac{\phi}{\phi_c}\right), \qquad
\mu_{\text{dry}} = \mu_m\left(1-\frac{\phi}{\phi_c}\right),$$

with a stated critical porosity $\phi_c$ (0.40 here). This is a *model* — a
linear interpolation between the mineral point and the suspension point — and
real sandstones deviate from it; the point is that the dry frame is a chosen
closure, not a measurement.

**(b) Fluid mixing.** The effective bulk modulus of a uniform mixture of
immiscible fluids is the Reuss (harmonic) average — Wood's equation:

$$\frac{1}{K_{\text{fl}}} = \sum_i \frac{S_i}{K_i},
\qquad \rho_{\text{fl}} = \sum_i S_i\rho_i .$$

The density average is exact (mass per unit volume is additive). The modulus
average is a model of a fine, uniform mixture; patchy saturation gives a
stiffer effective fluid and is a well-known source of error in gas
quantification.

**(c) Gassmann substitution.** Fluid substitution replaces the pore fluid
without changing the frame:

$$K_{\text{sat}} = K_{\text{dry}} +
\frac{\left(1 - K_{\text{dry}}/K_m\right)^2}
{\dfrac{\phi}{K_{\text{fl}}} + \dfrac{1-\phi}{K_m} -
 \dfrac{K_{\text{dry}}}{K_m^{2}}},
\qquad \mu_{\text{sat}} = \mu_{\text{dry}} .$$

The shear modulus is untouched because a fluid at rest supports no shear: this
is a rigorous consequence of the assumptions, not a modelling convenience.

**(d) Velocities and density.** With $\rho = (1-\phi)\rho_m + \phi\rho_{\text{fl}}$,

$$v_p = \sqrt{\frac{K_{\text{sat}} + \frac{4}{3}\mu_{\text{dry}}}{\rho}},
\qquad v_s = \sqrt{\frac{\mu_{\text{dry}}}{\rho}} .$$

### 2.1 What the model produces

Using standard mineral and fluid constants (quartz $K = 36.6$ GPa,
$\mu = 45.0$ GPa, $\rho = 2650\ \mathrm{kg\,m^{-3}}$; brine $K = 2.2$ GPa,
$\rho = 1000$; oil $K = 1.0$ GPa, $\rho = 800$; gas $K = 0.02$ GPa,
$\rho = 200\ \mathrm{kg\,m^{-3}}$), the demonstration prints:

| fluid | $\phi$ | $v_p$ (km/s) | $v_s$ (km/s) | $\rho$ (g/cm³) | AI (MRayl) | $v_p/v_s$ |
|---|---|---|---|---|---|---|
| brine | 0.15 | 5.09 | 3.42 | 2.402 | 12.23 | 1.488 |
| brine | 0.20 | 4.68 | 3.11 | 2.320 | 10.86 | 1.503 |
| brine | 0.25 | 4.20 | 2.75 | 2.237 | 9.39 | 1.528 |
| oil | 0.20 | 4.66 | 3.13 | 2.290 | 10.67 | 1.486 |
| gas | 0.20 | 4.69 | 3.20 | 2.200 | 10.31 | 1.466 |
| gas | 0.25 | 4.17 | 2.84 | 2.087 | 8.70 | 1.466 |

The demonstration summarises the sensitivity at $\phi = 0.20$: a gas
substitution lowers impedance by 5.0% and $v_p/v_s$ by 2.5%; oil lowers them by
1.8% and 1.1%. Note the accidental near-equality of $v_p$ for brine and gas at
$\phi = 0.20$ (4.68 vs 4.69 km/s): the impedance difference comes almost
entirely from **density**, which is why density information — and therefore
long offsets — matters for fluid discrimination
([06-09-05](../../06-seismology/09-reflection-seismology/05-amplitude-vs-offset.md)).

## 3. Two attributes, two pieces of information

Porosity and saturation affect the two measurable attributes differently, and
the whole subject rests on that difference:

$$\frac{\partial \ln \text{AI}}{\partial \phi} \approx -2.9
\quad\text{(at } \phi = 0.2\text{, brine)}\ \text{per unit porosity},
\qquad
\frac{\partial \ln \text{AI}}{\partial S_g} \approx -0.069
\ \text{per unit gas saturation},$$

a factor of forty between the two sensitivities. $v_p/v_s$ responds
comparatively more to the fluid: the same porosity step moves it $+1.7\%$,
while the brine-to-gas substitution moves it $-2.5\%$.

The numbers are the demonstration's. Moving porosity from 0.20 to 0.25 at
constant brine saturation changes impedance by $(9.39-10.86)/10.86 = -13.5\%$
(and $\ln(0.8646)/0.05 = -2.9$ per unit porosity); changing the fluid from
brine to gas at constant porosity changes impedance by $-5.0\%$
($\ln(0.9494)/0.75 = -0.069$ per unit gas saturation) and $v_p/v_s$ by
$-2.5\%$.

That is the rock-physics template in two lines: **impedance is mostly a
porosity-lithology attribute; $v_p/v_s$ is comparatively a fluid attribute — and
both are weak compared with the spread of real reservoirs.**

## 4. The equal-impedance curve

Fix a target impedance — the demonstration uses the pay sand at
$\phi = 0.20$, gas, $\text{AI} = 10.31$ MRayl — and solve for every $(\phi, S_g)$
that reproduces it. Within 1%:

- **241 combinations** qualify;
- porosity is pinned to **0.20–0.22**;
- gas saturation is free over **0.00–0.90**;
- $v_p/v_s$ over the admitted set spans **1.466 to 1.512**, a 3.2% range.

Two conclusions, both of which the interpreter must live with:

1. **Impedance alone gives porosity and says nothing about fluid.** A
   brine-filled sand and a gas-filled sand of slightly different porosity are
   the same number.
2. **$v_p/v_s$ does constrain the fluid, but weakly.** The 3.2% spread is barely
   more than the 3% attribute noise assumed in §5, which is exactly why the
   joint separation below is small. The classic "gas sand" AVO anomaly is real
   and detectable; the step from "anomaly" to "saturation" is where the
   uncertainty lives.

## 5. Bayesian prediction, and the base rate

Give each facies a distribution in $(\text{AI}, v_p/v_s)$. The demonstration
uses pay sand ($\text{AI} = 9.68$ MRayl, $v_p/v_s = 1.466$) and wet sand
($\text{AI} = 10.28$ MRayl, $v_p/v_s = 1.511$) with $\sigma_{\text{AI}} = 0.50$
MRayl and $\sigma_{v_p/v_s} = 0.045$ (both chosen). Then

$$d_1 = \frac{|\Delta \text{AI}|}{\sigma_{\text{AI}}} = 1.20, \qquad
d_2 = \sqrt{\left(\frac{\Delta \text{AI}}{\sigma_{\text{AI}}}\right)^2 +
\left(\frac{\Delta v_p/v_s}{\sigma_{v_p/v_s}}\right)^2} = 1.58 .$$

**Both attributes together give 1.58 standard deviations of separation.** In a
single-attribute world this is a mediocre discriminant, and no classification
scheme can make it better: the information is not there. What a Bayesian
formulation adds is an honest bookkeeping of that fact.

For a measurement with likelihood ratio $\Lambda$,

$$P(\text{pay}\mid x) = \frac{\Lambda\,p}{\Lambda\,p + (1-p)},$$

and the demonstration prints:

| $\Lambda$ | prior 0.50 | prior 0.20 | prior 0.05 | prior 0.01 |
|---|---|---|---|---|
| 1 | 0.500 | 0.200 | 0.050 | 0.010 |
| 4 | 0.800 | 0.500 | 0.174 | 0.039 |
| 10 | 0.909 | 0.714 | 0.345 | 0.092 |
| 50 | 0.980 | 0.926 | 0.725 | 0.336 |
| 200 | 0.995 | 0.980 | 0.913 | 0.669 |

A 10:1 likelihood ratio sounds decisive and leaves a 0.05 base rate at 0.345 —
a two-to-one bet against. This is the **base-rate effect**, and in exploration
it is not a hypothetical: the base rate on undrilled prospects is genuinely
low, and the same seismic anomaly is a good prospect in a proven fairway and a
poor one in a frontier basin. The prior is not a statistical decoration; it is
the fairway.

The simulation the demonstration runs makes the same point operationally, with
200 000 synthetic prospects and a 0.5 decision threshold:

| prior | called pay | precision | recall |
|---|---|---|---|
| 0.50 | 100 381 | 0.785 | 0.787 |
| 0.20 | 26 023 | 0.706 | 0.461 |
| 0.05 | 2 145 | 0.656 | 0.141 |

Lowering the threshold to 0.2 at a 0.05 prior raises recall to 0.423 and drops
precision to 0.367. **The threshold is a cost decision, not a physical one**:
it encodes what a dry hole costs relative to a discovery, which is the value-of-
information argument of
[11-01-03 Cost, Risk and Value of Information](../01-exploration-workflow/03-cost-benefit.md).

## 6. Net-to-gross: the same impedance, different mixtures

A resolution cell is not a homogeneous rock. Average over net and non-net:

$$\rho_{\text{cell}} = \text{NTG}\,\rho_{\text{sand}} +
(1-\text{NTG})\rho_{\text{shale}}, \qquad
\frac{1}{v_{\text{cell}}} = \frac{\text{NTG}}{v_{\text{sand}}} +
\frac{1-\text{NTG}}{v_{\text{shale}}} ,$$

where the second relation is exact for the transit time through the cell (the
travel times of the constituent layers add) and the first is exact for mass per
unit volume. Note the caveat: the *impedance* of the cell is only approximately
$\rho_{\text{cell}}v_{\text{cell}}$ as an amplitude predictor; the rigorous
long-wavelength construction is Backus averaging
([11-03-06](06-borehole-and-integration.md)).

With a chosen shale end member ($v_p = 2.80\ \mathrm{km\,s^{-1}}$,
$\rho = 2450\ \mathrm{kg\,m^{-3}}$) the demonstration prints cell impedances from
7.08 to 9.88 MRayl over $\text{NTG} \in \{0.30,0.50,0.70\}$ and
$\phi \in \{0.15,\dots,0.30\}$, and then searches for mixtures matching the
target produced by 50% NTG with $\phi = 0.25$ ($\text{AI} = 7.87$ MRayl):

> **214 different (NTG, clean-sand porosity) combinations** reproduce that
> impedance to 1%, from NTG = 0.25/$\phi$ = 0.10 to NTG = 0.86/$\phi$ = 0.29.

A single band-limited impedance therefore does not separate net-to-gross from
clean-sand porosity. Two measurements that do help: $v_p/v_s$ (because the
shale and sand trends differ) and, decisively, a well. This is the quantitative
form of the oldest rule in QI — **calibrate, then predict**.

## 7. Worked examples

### Example 1 — a fluid substitution, step by step

Sand at $\phi = 0.20$, brine-saturated, with $K_{\text{dry}} =
36.6(1-0.2/0.4) = 18.30$ GPa, $\mu_{\text{dry}} = 45.0(1-0.5) = 22.50$ GPa.

1. Brine: $K_{\text{fl}} = 2.2$ GPa,
   $\rho = 0.8(2650) + 0.2(1000) = 2320\ \mathrm{kg\,m^{-3}}$.
2. Gassmann: $(1-18.30/36.6)^2 = 0.25$;
   denominator $= 0.2/2.2 + 0.8/36.6 - 18.30/36.6^2 = 0.09091 + 0.02186 -
   0.01366 = 0.09911$;
   $K_{\text{sat}} = 18.30 + 0.25/0.09911 = 20.82$ GPa.
3. $v_p = \sqrt{(20.82 + 4(22.50)/3)/2.320\times10^{3}} = \sqrt{(50.82\times10^9)/
   (2.32\times10^3)} = 4680\ \mathrm{m\,s^{-1}}$;
   $v_s = \sqrt{22.50\times10^9/2.32\times10^3} = 3114\ \mathrm{m\,s^{-1}}$;
   $\text{AI} = 2320\times4680 = 10.86$ MRayl; $v_p/v_s = 1.503$.
4. Substituting gas (75% gas, 25% brine): $K_{\text{fl}} = 1/(0.25/2.2 +
   0.75/0.02) = 0.0266$ GPa, $\rho_{\text{fl}} = 0.25(1000)+0.75(200) = 400\ \mathrm{kg\,m^{-3}}$,
   $\rho = 2200\ \mathrm{kg\,m^{-3}}$; the denominator becomes
   $0.2/0.0266 + 0.02186 - 0.01366 = 7.526$, so $K_{\text{sat}} = 18.30 +
   0.25/7.526 = 18.33$ GPa;
   $v_p = \sqrt{(18.333+30.00)\times10^9/2200} = 4687\ \mathrm{m\,s^{-1}}$.

The demonstration prints 4.69 km/s and $\text{AI} = 10.31$ MRayl for exactly
this case. The $v_p$ is essentially unchanged; the impedance falls 5.0% because
$\rho$ fell 5.2%. **A gas sand is a density anomaly more than a velocity
anomaly**, which is why accurate density (long offsets, or a gravity tie) is
what converts an anomaly into a saturation estimate.

### Example 2 — the posterior, by hand

A prospect is in a fairway with a 0.10 base rate. An attribute pair gives a
likelihood ratio of 8.

$$P = \frac{8(0.10)}{8(0.10) + 0.90} = \frac{0.80}{1.70} = 0.47 .$$

Just under a coin toss, from an anomaly that would be called "strong". The same
anomaly in a fairway with a 0.40 base rate gives $3.20/3.80 = 0.84$. Nothing
about the data changed.

### Example 3 — what the resolution cell contains

At 30 Hz with $\lambda/4 = 25$ m and bin 25 m, one cell is
$25\times25\times10\ \mathrm{m} = 6250\ \mathrm{m^3}$. With $\phi = 0.20$ and a
cell-average water saturation of 0.35, the cell contains about
$6250\times0.20\times0.65 = 813\ \mathrm{m^3}$ of pore space occupied by water.
The seismic measurement is one number per cell, and the recovery factor will be
applied to this volume with an uncertainty two orders of magnitude larger than
the seismic error bars — the honest framing of
[04-06-01](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md).

## 8. Assumptions and regime of validity

1. **Critical-porosity dry moduli are a closure, not a measurement.** Real
   sandstones require a cementation or inclusion model calibrated to core.
2. **Gassmann assumes a low-frequency, homogeneous, isotropic, fully saturated
   frame with a single effective fluid.** Patchy saturation, squirt flow and
   frequency dependence all violate it, and the violations are largest where
   the answer matters most (gas).
3. **Wood's equation assumes a uniform mixture.** Patchy saturation raises the
   effective fluid modulus; using Wood's value over-estimates the gas effect.
4. **The attributes are Gaussian with stated spreads.** Real attribute
   distributions are skewed and correlated with lithology; the Bayesian
   machinery is only as good as those distributions.
5. **The attributes are measured where the wavelet is known.** Lateral
   amplitude variation from wavelet, tuning and acquisition variation appears
   as a spurious attribute variation, and it is the commonest cause of a false
   anomaly ([05-07-06](../../05-core-geophysics/07-interpretation-and-integration/06-interpretation-pitfalls.md)).
6. **No permeability, no connectivity, no recovery factor.** These are not in
   the data at any processing effort.
7. **The base rate is a judgement.** It is estimated from analogues and history,
   and it dominates the posterior; a sensitivity test on the prior belongs in
   every prospect report.

## 9. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| bulk modulus | $K$ | Pa = kg m⁻¹ s⁻² | $\rho(v_p^2 - 4v_s^2/3)$ |
| shear modulus | $\mu$ | Pa | $\rho v_s^2$ |
| density | $\rho$ | kg m⁻³ | arithmetic mixture |
| acoustic impedance | AI | kg m⁻² s⁻¹ | $\rho v$; 10⁶ = 1 MRayl |
| $v_p/v_s$ | | 1 | dimensionless |
| likelihood ratio | $\Lambda$ | 1 | ratio of densities |

The impedances quoted throughout are in MRayl $= 10^6\ \mathrm{kg\,m^{-2}\,s^{-1}}$;
an editor's request for "impedance in MRayl" is a request for $\rho v/10^6$ with
$\rho$ in kg m⁻³ and $v$ in m s⁻¹.

## 10. Python demonstration

`code/reservoir_characterisation_demo.py` prints:

1. the critical-porosity + Wood + Gassmann table of $v_p$, $v_s$, $\rho$, AI and
   $v_p/v_s$ for brine, oil and gas at three porosities, with the substitution
   sensitivities;
2. the equal-impedance scan (how many $(\phi,S_g)$ pairs match, and the
   $v_p/v_s$ spread among them);
3. the Bayesian posterior table versus likelihood ratio and prior, and a
   200 000-prospect confusion matrix at three priors and two thresholds;
4. the net-to-gross averaging table and the count of mixtures matching one
   impedance;
5. the scale comparison between a resolution cell and a core plug.

Print-only, seeded with `np.random.default_rng(20261014)`, exits 0.

## 11. Exercises

- [`exercises/03-reservoir-characterisation-exercises.md`](exercises/03-reservoir-characterisation-exercises.md)
- [`exercises/03-reservoir-characterisation-solutions.md`](exercises/03-reservoir-characterisation-solutions.md)

## Mastery checkpoint

> A sand has $\phi = 0.18$, $K_{\text{dry}} = 19.0$ GPa,
> $\mu_{\text{dry}} = 24.0$ GPa, $\rho_m = 2650\ \mathrm{kg\,m^{-3}}$,
> $K_{\text{brine}} = 2.2$ GPa, $K_{\text{gas}} = 0.02$ GPa. **(a)** Compute the
> brine-saturated density, $K_{\text{sat}}$, $v_p$ and AI. **(b)** Repeat for
> $S_g = 0.7$ and state the percentage change in AI. **(c)** For attribute
> spreads $\sigma_{\text{AI}} = 4\%$ and $\sigma_{v_p/v_s} = 3\%$, compute the
> joint separation if the $v_p/v_s$ difference is 2%. **(d)** With a 0.06 base
> rate and a likelihood ratio of 20, compute the posterior and state in one
> sentence why the answer is not a property of the seismic data.

## Common pitfalls

1. **Treating an impedance anomaly as a fluid indicator.** The demonstration's
   equal-impedance curve has 241 members spanning the whole saturation range.
2. **Reporting a saturation without the base rate.** The posterior is not a
   data quantity.
3. **Quoting precision without the prior.** The same classifier has precision
   0.79 at a 0.5 base rate and 0.66 at 0.05.
4. **Confusing resolution with information content.** A bed can be resolved and
   its net-to-gross unresolvable: 214 mixtures match one impedance.
5. **Applying Gassmann outside its regime.** Patchy saturation and frequency
   dependence break it precisely for gas.
6. **Predicting permeability.** Nothing in this chain measures it.

## Related modules

- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  the physics behind the model used here.
- [06-09-05 AVO/AVA Analysis and Its Assumptions](../../06-seismology/09-reflection-seismology/05-amplitude-vs-offset.md) —
  how the attributes are actually estimated from angle gathers.
- [18-05 Bayesian Inversion](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the systematic treatment of priors and likelihoods used in §5.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) —
  how a cell-average prediction is extrapolated and its uncertainty mapped.
- [11-03-04 Seismic Inversion for Reservoir Properties](04-seismic-inversion-reservoir.md) —
  where impedance comes from.
- [11-01-03 Cost, Risk and Value of Information](../01-exploration-workflow/03-cost-benefit.md) —
  what to do with the posterior.

## Further reading

- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. Elastic
  properties and their measurement.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Amplitude and attribute
  interpretation.
- Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists. Level: reference. Amplitude preservation and inversion
  practice.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
