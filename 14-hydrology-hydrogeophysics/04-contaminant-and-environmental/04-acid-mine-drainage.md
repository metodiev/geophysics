---
id: 14-04-04
title: "Acid Mine Drainage and Mining Environmental Geophysics"
level: doctoral
prereqs: ["14-04-01", "04-06-02", "09-04-01", "14-01-05", "14-03-02"]
tags: [hydrology, hydrogeophysics, acid-mine-drainage, sulphide-oxidation, stoichiometry, conductivity, self-potential, mine-waste]
---

# Acid Mine Drainage and Mining Environmental Geophysics

> **All models and data in this module are SYNTHETIC.** The waste composition,
> the percolation ratio, the conductivity relation and the transport parameters
> are chosen teaching values for an idealised archetype. No real mine, site,
> lease, waste facility or discharge limit is described. The only numbers used
> as constants are standard atomic weights, the molar masses they imply, and the
> equivalent weight of calcium carbonate.

Acid mine drainage (AMD) differs from the plumes of lesson 01 in one essential
way: the tracer is *manufactured in place* by a reaction. Sulphide minerals left
in waste rock oxidise when they meet oxygen and water, and the products are
sulphate and acidity, both of which raise the pore-fluid conductivity. The
source term is therefore a chemistry problem, and its magnitude follows from a
balanced reaction and standard atomic weights — not from a monitoring well.

This lesson follows that chain end to end: reaction stoichiometry, water
balance, concentration, conductivity, resistivity, transport, and the
self-potential signature of the redox front that drives the reaction. The
geophysical method is the same as in the previous lessons; what changes is where
the number comes from.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the idealised overall reaction for sulphide oxidation and **verify**
   it by an atom and charge balance rather than by matching a remembered formula.
2. **Compute** the sulphate, acidity and oxygen yields per kilogram of sulphide
   from standard atomic weights, and the calcium-carbonate equivalent needed to
   neutralise the acidity.
3. **Explain** why a concentration cannot be reported without a water balance,
   and **compute** the concentration as a function of the percolation ratio.
4. **Convert** that concentration to a pore-fluid conductivity, then to a bulk
   resistivity, and **state** each model assumption.
5. **Compute** the arrival time and transition width of the conductive front from
   a one-dimensional transport model.
6. **Interpret** a self-potential anomaly over a redox front as a location
   rather than a mass, and **state** why the amplitude is not invertible alone.
7. **List** the false positives for a conductive anomaly and **name** the
   independent measurement that separates each.

## Prerequisites

- [14-04-01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md) —
  the transport model, the detection threshold and the time-lapse argument.
- [04-06-02 Mineral Deposits](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md) —
  sulphide mineralogy and the deposit setting that generates AMD.
- [09-04-01 Self-Potential Sources](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md) —
  the electrochemical and redox origins of the SP anomaly.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md) —
  ionic strength, conductivity and the relation between them.
- [14-03-02 Archie's Law and Saturation Estimation](../03-petrophysics-hydrology/02-archie-and-saturation.md) —
  the pore-fluid-to-bulk conversion.

## 1. Intuition: a source term that is a reaction

Every other lesson in this module takes the contaminant as given and asks where
it goes. Here the question is inverted: the *mass* of the contaminant is the
product of a mineral reaction, and the reaction is limited by oxygen, water,
bacterial catalysis and surface area — none of which geophysics sees. What
geophysics sees is the consequence: elevated sulphate, lowered pH, and therefore
a conductive pore fluid, and a redox front that generates a self-potential.

The practical consequence is a division of labour that is easy to state and often
violated. **Chemistry gives the source term; hydrology gives the water balance;
geophysics gives the distribution.** A conductivity map is evidence about where
the products are. It is not evidence about how much sulphide remains, because the
reaction rate is not in the data.

## 2. The idealised reaction and its balance check

The overall oxidation of pyrite in the presence of water and oxygen is
conventionally written as

$$
\text{FeS}_2 + \tfrac{15}{4}\,\text{O}_2 + \tfrac{7}{2}\,\text{H}_2\text{O}
\;\longrightarrow\;
\text{Fe(OH)}_3 + 2\,\text{SO}_4^{2-} + 4\,\text{H}^{+} .
$$

The demonstration verifies the balance by counting atoms on both sides rather
than trusting the formula:

| element | left | right |
|---|---|---|
| Fe | 1 | 1 |
| S | 2 | 2 |
| O | $11$ | $11$ |
| H | $7$ | $7$ |

and the net charge on the right is $2(-2) + 4(+1) = 0$. This is the only check
available without invoking a mechanism; the real process is a chain of abiotic
and bacterially catalysed steps, and the overall reaction says nothing about how
fast any of them proceeds.

## 3. Stoichiometric yields

With standard atomic weights $\mathrm{Fe} = 55.845$, $\mathrm{S} = 32.060$,
$\mathrm{O} = 15.999$, $\mathrm{H} = 1.008$:

$$
M(\text{FeS}_2) = 55.845 + 2\times32.060 = 119.965\ \mathrm{g\,mol^{-1}},
$$
$$
M(\text{SO}_4) = 32.060 + 4\times15.999 = 96.056\ \mathrm{g\,mol^{-1}},
\qquad
M(\text{O}_2) = 31.998\ \mathrm{g\,mol^{-1}} .
$$

Per mole of pyrite oxidised, the reaction delivers 2 mol of sulphate, 4 mol of
acidity and consumes 3.75 mol of oxygen. Per gram of pyrite:

$$
\text{sulphate} = \frac{2\times96.056}{119.965} = 1.6014\
\mathrm{g\,SO_4^{2-}\,g^{-1}} ,
$$

$$
\text{acidity} = \frac{4}{119.965}\times1000 = 33.34\
\mathrm{mol\,H^{+}\,kg^{-1}} = 33.34\ \mathrm{eq\,kg^{-1}} ,
$$

$$
\text{oxygen} = \frac{3.75\times31.998}{119.965} = 1.0002\
\mathrm{g\,O_2\,g^{-1}} .
$$

The neutralisation demand follows from the equivalent weight of calcium
carbonate, $M(\text{CaCO}_3)/2 = (40.078 + 12.011 + 3\times15.999)/2
= 50.043\ \mathrm{g\,eq^{-1}}$:

$$
33.34\ \mathrm{eq}\times50.043\ \mathrm{g\,eq^{-1}}
= 1669\ \mathrm{g\ CaCO_3\ per\ kg\ pyrite} .
$$

The oxygen figure is a pleasant check on the arithmetic: it comes out as
$\approx 1.000\ \mathrm{g\,O_2}$ per gram of pyrite, because
$3.75\times32 = 120 \approx M(\text{FeS}_2)$. Two independent roundings landing
on unity is a sign the balance is right.

## 4. Worked example 1 — yields per kilogram of pyrite

**Problem.** A synthetic waste contains $1.0\%$ pyrite by mass and has an in-place
density of $2000\ \mathrm{kg\,m^{-3}}$. Compute the mass of pyrite, of sulphate
and of neutralisation demand per cubic metre of waste, assuming complete
oxidation.

**Solution.** Per $\mathrm{m^{3}}$ of waste the mass is $2000\ \mathrm{kg}$, so

$$
m_\text{pyrite} = 0.010\times2000 = 20.0\ \mathrm{kg},
$$

$$
m_\text{sulphate} = 20.0\times1.6014 = 32.03\ \mathrm{kg},
$$

$$
m_\text{CaCO}_3 = 20.0\times1.669 = 33.4\ \mathrm{kg} .
$$

The demonstration prints $20.0\ \mathrm{kg}$ pyrite, $32.03\ \mathrm{kg}$
sulphate and $1669\ \mathrm{g\ CaCO_3}$ per kg pyrite (i.e. $33.4\
\mathrm{kg\,m^{-3}}$ by the multiplication above). **Note the last number**: the
neutralisation demand is larger than the mass of pyrite that generates it, which
is why AMD is a long-term liability rather than a treatment problem with a
budget. Note also that this assumes complete oxidation — see Section 8.

## 5. Worked example 2 — concentration needs a water balance

**Problem.** Using the waste of Worked example 1, compute the sulphate
concentration in the percolating water for a percolation ratio of $2.0\
\mathrm{m^{3}}$ of water per $\mathrm{m^{3}}$ of waste, and for a range of
ratios.

**Solution.** The water volume is $2.0\ \mathrm{m^{3}} = 2000\ \mathrm{L}$, so

$$
C = \frac{32.03\times10^{6}\ \mathrm{mg}}{2000\ \mathrm{L}}
= 1.6014\times10^{4}\ \mathrm{mg\,L^{-1}} \approx 16\,014\
\mathrm{mg\,L^{-1}} .
$$

The demonstration's table:

| percolation ratio ($\mathrm{m^{3}\,m^{-3}}$) | 0.5 | 1.0 | 2.0 | 5.0 | 20.0 |
|---|---|---|---|---|---|
| sulphate ($\mathrm{mg\,L^{-1}}$) | 64 056 | 32 028 | 16 014 | 6 406 | 1 601 |

**The concentration is inversely proportional to the percolation ratio.** The
same pyrite mass flushed with ten times the water gives a ten-fold lower
concentration. A concentration without a water balance is a property of the
arithmetic, not of the site. Note also that this is an *idealised upper bound*: it
assumes complete oxidation and no solubility limit, no secondary-mineral
precipitation, no attenuation and no dilution. The point of the calculation is
the chain, not the number.

## 6. From concentration to anomaly

The demonstration uses a synthetic linear relation
$\sigma_w = 0.050 + 2.0\times10^{-5}C\ \mathrm{S\,m^{-1}}$ (with $C$ in
$\mathrm{mg\,L^{-1}}$) and Archie with $a = 1$, $m = 2$, $S_w = 1$,
$\phi = 0.30$, so $\sigma_b = 0.09\,\sigma_w$:

| $C$ ($\mathrm{mg\,L^{-1}}$) | 0 | 250 | 500 | 1000 | 2500 | 16 014 |
|---|---|---|---|---|---|---|
| $\sigma_w$ ($\mathrm{S\,m^{-1}}$) | 0.0500 | 0.0550 | 0.0600 | 0.0700 | 0.1000 | 0.3703 |
| $\rho_b$ ($\Omega$ m) | 222.22 | 202.02 | 185.19 | 158.73 | 111.11 | 30.01 |
| change | $+0.00\%$ | $-9.09\%$ | $-16.67\%$ | $-28.57\%$ | $-50.00\%$ | $-86.50\%$ |

The background resistivity falls by $86.5\%$ at the synthetic source
concentration. As in every lesson of this module, the contrast is entirely in the
pore fluid and therefore independent of the rock type — which is why a
conductivity survey transfers from site to site while a concentration estimate
does not.

## 7. Transport: when the anomaly arrives

Reusing the one-dimensional advection model with $v = 0.040\
\mathrm{m\,day^{-1}}$ and $\alpha_L = 2.0\ \mathrm{m}$ (no retardation: sulphate
is a conservative anion in most settings), the demonstration gives:

| $t$ (days) | front (m) | 10–90% width (m) | $\rho$ at 25 m ($\Omega$ m) |
|---|---|---|---|
| 365 | 14.6 | 19.6 | 127.4 |
| 1095 | 43.8 | 33.9 | 31.4 |
| 2555 | 102.2 | 51.8 | 30.0 |
| 3650 | 146.0 | 61.9 | 30.0 |

The front reaches $25\ \mathrm{m}$ at $t = 25/0.040 = 625$ days. Before that the
anomaly at that station is **zero, not small** — the same point as lesson 01 §8,
and the same design consequence: the rising limb carries the transport
information. The 10–90% width is $61.9\ \mathrm{m}$ after ten years, so spacings
of $10\ \mathrm{m}$ resolve the transition comfortably and spacings of $1\
\mathrm{m}$ buy nothing but survey time.

## 8. The self-potential signature, and what it does not give

The redox front is an electrochemical current source. The simplest teaching model
places a compact source of equivalent strength $I$ at depth $d$ in a half-space
of resistivity $\rho$:

$$
V(x) = \frac{\rho I}{2\pi\sqrt{x^{2}+d^{2}}} .
$$

For $\rho = 100\ \Omega\,\mathrm{m}$, $I = 0.02\ \mathrm{A}$ equivalent and
$d = 5\ \mathrm{m}$ the demonstration prints $63.662\ \mathrm{mV}$ at $x = 0$
and $20.132\ \mathrm{mV}$ at $x = \pm 15\ \mathrm{m}$, a peak-to-15 m amplitude of
$43.5\ \mathrm{mV}$.

$V$ depends on $\rho$ and $I$ only through their product, so **SP locates a
source and cannot size it.** This is not a limitation of the instrument; it is a
property of the potential field. Converting an SP anomaly into a reaction rate
requires an independent estimate of $\rho$ (from the co-located resistivity
survey) *and* a model of the electrochemical coupling coefficient, which is a
laboratory calibration.

## 9. Assumptions and regime of validity

**Chemistry.** (i) Stoichiometric and complete: the yields are upper bounds, and
the actual extent of reaction is a kinetic problem involving oxygen supply,
grain size, bacterial catalysis and passivation by iron-oxide coatings. (ii) One
sulphide mineral; a mixed assemblage (pyrite, pyrrhotite, galena, sphalerite)
produces different yields per unit mass and different trace-metal loads. (iii)
No secondary-mineral sinks: ferrihydrite and gypsum remove iron and sulphate from
solution, so the measured sulphate is a lower bound on the produced amount. (iv)
No neutralisation by carbonate minerals in the waste, which is the single largest
control on the resulting acidity in practice.

**Water balance.** A percolation ratio is a *scenario*, not a measurement. It
must be stated, and it usually dominates the uncertainty in any predicted
concentration.

**Property and transport.** As lesson 01: a clean matrix, a known porosity, full
saturation, a stated concentration-to-conductivity relation, one-dimensional
uniform steady flow, constant dispersivity, and no density-driven or multiphase
effects.

**What geophysics can and cannot claim.** It can map the conductivity
distribution, and by time-lapse differencing it can locate a moving front and
date its arrival. It cannot measure the remaining sulphide mass, the reaction
rate, or the acidity, because none of those is in the conductivity.

## 10. False positives

| mechanism | bulk resistivity change | independent constraint |
|---|---|---|
| clay-rich rock, fresh water | $2$–$3\times$ lower | natural gamma, cation exchange capacity, NMR bound fluid |
| brackish-water intrusion | up to $80\times$ lower | coastal setting; fluid samples |
| metallic conductor body | orders of magnitude | very low resistivity plus a strong induced-polarisation phase |
| increased water saturation | $2$–$3\times$ lower | sampling shows the pore-fluid conductivity unchanged |
| higher porosity | $1.5$–$2\times$ lower | an independent porosity measurement |

The last two rows matter most on a mine site, where the waste itself has an
unusual and highly variable porosity and saturation. A resistivity drop is a
statement about the product $\phi^{m}\sigma_w$; every mechanism that raises either
factor produces the same observation, and an environmental interpretation must
name at least one independent constraint.

## 11. Python demonstration

[`code/acid_mine_drainage_demo.py`](./code/acid_mine_drainage_demo.py) prints the
balanced reaction with its atom check, the yield table, the concentration versus
percolation ratio, the conductivity and resistivity conversion, the transport
table, the self-potential profile and the false-positive table.

```bash
cd 14-hydrology-hydrogeophysics/04-contaminant-and-environmental/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python acid_mine_drainage_demo.py
```

## 12. Exercises

Graded problems are in
[`exercises/04-acid-mine-drainage-exercises.md`](./exercises/04-acid-mine-drainage-exercises.md)
with worked solutions in
[`exercises/04-acid-mine-drainage-solutions.md`](./exercises/04-acid-mine-drainage-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Write the idealised sulphide-oxidation reaction and verify the atom and
> charge balance. **(b)** Compute the sulphate and acidity yields per kilogram of
> pyrite from standard atomic weights, and the calcium-carbonate equivalent
> needed to neutralise one kilogram of pyrite. **(c)** A waste contains $0.4\%$
> pyrite by mass at $1800\ \mathrm{kg\,m^{-3}}$; compute the sulphate mass per
> cubic metre and the concentration for a percolation ratio of
> $3.0\ \mathrm{m^{3}\,m^{-3}}$. **(d)** With
> $\sigma_w = 0.050 + 2.0\times10^{-5}C$ and $\phi^{m} = 0.09$, compute the bulk
> resistivity at the background and at $1000\ \mathrm{mg\,L^{-1}}$.
> **(e)** State three reasons the computed concentration is an upper bound, and
> one measurement that would test the largest of them. **(f)** Explain why an SP
> amplitude cannot be inverted for a reaction rate.

## Common pitfalls

1. **Reporting a concentration without the percolation ratio.** The ratio
   dominates the answer.
2. **Treating the stoichiometric yield as a prediction.** It is an upper bound;
   kinetics and secondary minerals reduce it.
3. **Forgetting carbonate neutralisation in the waste.** It can remove most of
   the acidity and leave the sulphate.
4. **Inverting an SP amplitude alone.** $\rho I$ is not separable.
5. **Reading a conductive anomaly as AMD without a clay check.** The ambiguity is
   identical to lesson 03 §8.
6. **Assuming the reaction proceeds uniformly in space.** It is controlled by
   oxygen access, which is controlled by the water table and the cover.
7. **Confusing sulphate mass with acidity.** They scale together in this reaction
   but are measured differently and are limited by different things.

## Related modules

- [01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md).
- [02 Landfill Investigation and Leachate Mapping](02-landfill-investigation.md).
- [03 Seawater Intrusion and Coastal Aquifer Monitoring](03-saline-intrusion.md).
- [05 Permafrost Monitoring with Geophysics](05-permafrost-monitoring.md).
- [Module 11-exploration-geophysics](../../11-exploration-geophysics/README.md) —
  the same sulphide mineralogy as an ore target rather than a liability.
- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  groundwater chemistry and the water balance.
