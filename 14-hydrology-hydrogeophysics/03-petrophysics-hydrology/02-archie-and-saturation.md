---
id: 14-03-02
title: "Archie's Law and Saturation Estimation"
level: graduate
prereqs: ["14-03-01", "05-04-07", "09-01-02", "14-01-05"]
tags: [hydrology, hydrogeophysics, petrophysics, archie, saturation, resistivity, formation-factor]
---

# Archie's Law and Saturation Estimation

> **All models and data in this module are SYNTHETIC.** The texture exponents,
> resistivities, clay conductance and saturation profiles below are chosen
> teaching values. No log, core, well or published compilation is quoted.

Archie's law is the only rock-physics relation that a hydrogeophysical survey
uses routinely and unembarrassed: measure a formation resistivity, divide by a
pore-fluid resistivity, and read off a water saturation. It is also a purely
empirical pair of power laws whose two exponents change from formation to
formation, and it is the source of a large fraction of the wrong saturations in
print. This lesson derives what can be derived (the formation factor of a
simplified pore geometry), states precisely what cannot be derived, and measures
the two failure modes that matter in hydrology: clay conduction and the coupling
between porosity and salinity.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the formation factor $F$, the resistivity index $I$ and the water
   saturation $S_w$, and **write** Archie's two equations with every symbol and
   unit named.
2. **Derive** $F = \tau^{2}/\phi$ for a bundle of tubes and **explain** why the
   measured exponent $m > 1$ is evidence that the tortuosity factor itself grows
   as porosity falls.
3. **Invert** a measured formation resistivity for $S_w$ and **report** it with
   the exponent set and the pore-fluid resistivity that were assumed.
4. **Propagate** uncertainties in $\rho_t$, $\phi$, $\rho_w$ and the exponents to
   an uncertainty in $S_w$, and **identify** which input dominates.
5. **Diagnose** clay conduction from an inverted $S_w > 1$ and **explain** why the
   impossible value is quantitatively useful rather than merely wrong.
6. **Explain** why a saturation and a salinity cannot both be recovered from one
   resistivity, and **state** the independent measurement that resolves them.

## Prerequisites

- [14-03-01 Porosity-Permeability and Kozeny-Carman Relations](01-porosity-permeability-relations.md) —
  porosity, effective porosity and specific surface.
- [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  the same relations from the rock-physics side, with the parallel-conduction
  mechanisms derived.
- [09-01-02 Archie's Law](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md) —
  the field version: how $F$ and $I$ are measured.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md) —
  total dissolved solids, ionic strength and why salinity is not a single number.

## 1. Intuition: conduction through an insulator full of conductor

A dry rock is an insulator; its grains are silicates and carbonates with
resistivities of order $10^{6}$ to $10^{12}\ \Omega\,\mathrm{m}$. All the current
in a saturated rock flows through the pore fluid. The formation factor is
therefore a *geometric* quantity: how much longer and narrower is the fluid path
than the straight line through the sample?

$$
F = \frac{\rho_0}{\rho_w} = \frac{\text{resistivity of the rock}}{\text{resistivity of the pore fluid}} .
$$

Two clean limits check the definition. A rock whose pores are straight tubes
filling the whole volume ($\phi \to 1$, $\tau = 1$) has $F \to 1$: rock and
fluid are the same conductor. A rock with no connected pores has
$F \to \infty$. Everything between is geometry, and the geometry is what Archie's
exponent $m$ reports.

## 2. Definitions

$$
F = \frac{a}{\phi^{m}}, \qquad
I = \frac{\rho_t}{\rho_0} = S_w^{-n}, \qquad
\rho_t = \rho_0\,S_w^{-n} = \frac{a\,\rho_w}{\phi^{m}S_w^{n}} .
$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\rho_t$ | formation resistivity at partial saturation | $\Omega\,\mathrm{m}$ |
| $\rho_0$ | formation resistivity at $S_w = 1$ | $\Omega\,\mathrm{m}$ |
| $\rho_w$ | pore-fluid (water) resistivity | $\Omega\,\mathrm{m}$ |
| $F$ | formation factor, dimensionless | — |
| $I$ | resistivity index, dimensionless | — |
| $S_w$ | water saturation, fraction of connected pore volume | — |
| $a$ | tortuosity/geometry coefficient (fitted) | — |
| $m$ | cementation exponent (fitted) | — |
| $n$ | saturation exponent (fitted) | — |

Three warnings about the exponents, all of which the derivation below makes
concrete: $a$, $m$ and $n$ are **not** universal constants; they are fitted per
formation; and a laboratory measurement of $m$ on a core does not transfer to a
different lithology. Values quoted from a compilation are ranges with a
provenance, and this lesson will not pretend otherwise.

**Salinity enters only through $\rho_w$.** Converting $\rho_w$ to a total
dissolved solids, a chloride concentration or a salinity requires a *further*
empirical relation, which is a separate model with its own error. Section 9 shows
how much ambiguity that adds.

## 3. Derivation: the formation factor of a tube bundle

**Geometry.** Let $n$ tubes cross unit bulk area, each of cross-sectional area
$A_t$ and length $L_e = \tau L$ for a bulk path length $L$. The porosity of this
ideal medium is the pore volume per bulk volume:

$$
\phi = \frac{n A_t L_e}{L} = n A_t \tau .
$$

**Resistance of one tube.** $R_\text{tube} = \rho_w L_e/A_t = \rho_w \tau L/A_t$.

**Parallel combination at the sample scale.** The bulk sample of cross-section
$A$ contains $nA$ tubes, so the total conductance is

$$
\frac{nA}{R_\text{tube}} = \frac{nA\,A_t}{\rho_w \tau L}.
$$

The bulk resistance is $R_\text{bulk} = \rho_\text{bulk}L/A$, so

$$
\frac{1}{R_\text{bulk}} = \frac{A}{\rho_\text{bulk}L}
\;\;\Longrightarrow\;\;
\rho_\text{bulk} = \frac{\rho_w \tau^{2}}{n A_t}
= \rho_w\frac{\tau^{2}}{\phi} ,
$$

using $nA_t = \phi/\tau$. Two results follow immediately.

$$
\boxed{\;F = \frac{\tau^{2}}{\phi}\;}
\qquad\Longrightarrow\qquad a = \tau^{2}, \quad m = 1 .
$$

**The tortuosity paradox.** The bundle model *derives* $m = 1$, but real rocks
have $m$ between about $1.3$ and $2.5$. The demonstration computes the implied
$\tau^{2} = F\phi$ when $F$ is forced to follow $\phi^{-2}$:

| $\phi$ | $F = \phi^{-2}$ | implied $\tau^{2} = F\phi$ |
|---|---|---|
| 0.10 | 100.00 | 10.000 |
| 0.20 | 25.00 | 5.000 |
| 0.30 | 11.11 | 3.333 |
| 0.40 | 6.25 | 2.500 |

The implied tortuosity factor *rises* as porosity falls. This is not a paradox
once stated: in a tighter rock the path detours further around grains, so
$\tau$ is itself a decreasing function of $\phi$. Archie's $m > 1$ is the
statement $\tau^{2} \propto \phi^{-(m-1)}$ folded into a single exponent. That is
why $m$ is a texture parameter rather than a physical constant, and why it must
be fitted locally.

## 4. The saturation law

With an insulating matrix, adding gas to the pores removes conducting fluid from
the path. Partially saturating a rock therefore *raises* its resistivity. The
empirical form is $I = S_w^{-n}$, and its consequence, rearranged for use,
is

$$
\boxed{\;S_w = \left(\frac{a\,\rho_w}{\phi^{m}\,\rho_t}\right)^{1/n} .}
$$

Setting the argument to $1$ gives the **saturation-one resistivity**
$\rho_0 = a\rho_w/\phi^{m}$, and any measured $\rho_t < \rho_0$ implies
$S_w > 1$: more water than the pores can hold. That impossibility is not a
numerical nuisance. Section 8 shows it is a *measurement of the model error*.

The demonstration's synthetic example uses $\phi = 0.28$, $a = 1.00$, $m = 2.00$,
$n = 2.00$, $\rho_w = 2.50\ \Omega\,\mathrm{m}$, giving
$\rho_0 = 31.888\ \Omega\,\mathrm{m}$, and inverts a small synthetic suite:

| $\rho_t$ ($\Omega$ m) | $I = \rho_t/\rho_0$ | inverted $S_w$ |
|---|---|---|
| 15.00 | 0.4704 | 1.4580 (impossible) |
| 20.00 | 0.6272 | 1.2627 (impossible) |
| 31.89 | 1.0001 | 1.0000 |
| 50.00 | 1.5680 | 0.7986 |
| 80.00 | 2.5088 | 0.6313 |

## 5. Units and dimensional analysis

$F$ and $I$ are ratios of two resistivities, so they are dimensionless and the
units cancel. The inverted saturation is therefore dimensionless by construction
— a useful check, because a formula that mixes $\mathrm{S\,m^{-1}}$ with
$\Omega\,\mathrm{m}$ will produce a saturation that drifts when you switch
conventions. Write conductivity as the reciprocal only at the last step:

$$
\sigma_t = \frac{1}{\rho_t} = \frac{\phi^{m}S_w^{n}}{a\,\rho_w}
\qquad (\mathrm{S\,m^{-1}}) .
$$

The demonstration's clay model in Section 8 adds a term in $\mathrm{S\,m^{-1}}$
to $\sigma_t$, which is why it works in conductivity.

## 6. Worked example 1 — a saturation from a measured resistivity

**Problem.** In a synthetic clean sand, $\phi = 0.28$, $a = 1.00$, $m = 2.00$,
$n = 2.00$, and the pore fluid has $\rho_w = 2.50\ \Omega\,\mathrm{m}$. A
resistivity survey returns $\rho_t = 50.0\ \Omega\,\mathrm{m}$. Compute
$\rho_0$, $F$, $I$ and $S_w$.

**Solution.**

$$
F = \frac{a}{\phi^{m}} = \frac{1}{0.28^{2}} = \frac{1}{0.0784} = 25.510 ,
$$

$$
\rho_0 = F\rho_w = 25.510\times2.50 = 31.888\ \Omega\,\mathrm{m},
$$

$$
I = \frac{\rho_t}{\rho_0} = \frac{50.0}{31.888} = 1.5680 ,
\qquad
S_w = I^{-1/n} = 1.5680^{-0.5} = 0.7986 .
$$

Equivalent direct inversion:
$S_w = (a\rho_w/(\phi^{m}\rho_t))^{1/2}
 = (2.50/1.5680)^{1/2} = 0.7986$. The demonstration prints all four numbers.

**Interpretation.** "$S_w = 0.80$, assuming a clean sand with $m = n = 2$,
$a = 1$ and a pore fluid of $2.50\ \Omega\,\mathrm{m}$." Every one of those
clauses is part of the answer.

## 7. Worked example 2 — the error budget

**Problem.** Using the same model, propagate (a) a $5\%$ error in $\rho_t$,
(b) a $5\%$ error in $\phi$, (c) a $10\%$ error in $m$ and (d) a $20\%$ error in
$\rho_w$ into $S_w$.

**Solution.** Take logarithms of $S_w = (a\rho_w\phi^{-m}\rho_t^{-1})^{1/n}$:

$$
\ln S_w = \frac{1}{n}\left(\ln a + \ln\rho_w - m\ln\phi - \ln\rho_t\right).
$$

Differentiating gives the elasticities directly:

$$
\frac{\partial\ln S_w}{\partial\ln\rho_t} = -\frac{1}{n} = -0.50, \qquad
\frac{\partial\ln S_w}{\partial\ln\phi} = -\frac{m}{n} = -1.00, \qquad
\frac{\partial\ln S_w}{\partial\ln\rho_w} = +\frac{1}{n} = +0.50 .
$$

| perturbed input | perturbation | resulting error in $S_w$ |
|---|---|---|
| $\rho_t$ | 5% | 2.50% |
| $\rho_t$ | 20% | 10.00% |
| $\phi$ | 5% | 5.00% |
| $\phi$ | 10% | 10.00% |
| $\rho_w$ | 20% | 10.00% |

The exponent error is not a scaling at all: with $m$ wrong by $10\%$
($2.00 \to 1.80$ at fixed $\rho_t$) the ratio of the two inversions is
$\phi^{\,(2.00-1.80)/2} = \phi^{0.1}$, i.e. $0.28^{0.1} = 0.880$, an $12\%$ error
in $S_w$ at every depth. The demonstration's profile section shows the whole
inverted curve shifting:

| $z$ (m) | true $S_w$ | $\rho_t$ ($\Omega$ m) | $S_w$ at $m = 2.0$ | $S_w$ at $m = 1.8$ |
|---|---|---|---|---|
| 0.0 | 0.9989 | 31.961 | 0.9989 | 0.8795 |
| 5.0 | 0.9690 | 33.961 | 0.9690 | 0.8532 |
| 10.0 | 0.5500 | 105.414 | 0.5500 | 0.4843 |
| 15.0 | 0.1310 | 1858.133 | 0.1310 | 0.1153 |
| 20.0 | 0.1011 | 3117.055 | 0.1011 | 0.0891 |

**Moral.** A porosity error of $\pm5\%$ spans $S_w$ from $0.7606$ to $0.8406$
around $0.7986$ — a range wider than most hydrological questions tolerate. The
exponent set must be justified, not assumed.

## 8. Failure mode 1 — clay conduction and the $S_w > 1$ diagnostic

Clay minerals conduct along their surfaces through an electrical double layer.
That path is in **parallel** with the pore-fluid path, so it adds a conductivity
that Archie's single mechanism cannot represent:

$$
\sigma_t = \underbrace{\frac{\phi^{m}S_w^{n}}{a\,\rho_w}}_{\text{Archie pore fluid}}
+ \underbrace{\sigma_\text{clay}}_{\text{surface conduction}} .
$$

The demonstration uses a synthetic shaly sand with $\phi = 0.28$,
$\rho_w = 2.50\ \Omega\,\mathrm{m}$ and $\sigma_\text{clay} =
0.02\ \mathrm{S\,m^{-1}}$:

| true $S_w$ | $\sigma_t$ ($\mathrm{S\,m^{-1}}$) | $\rho_t$ ($\Omega$ m) | Archie $S_w$ |
|---|---|---|---|
| 1.00 | 0.05136 | 19.470 | 1.2797 |
| 0.80 | 0.04007 | 24.956 | 1.1304 |
| 0.60 | 0.03129 | 31.960 | 0.9989 |
| 0.50 | 0.02784 | 35.920 | 0.9422 |
| 0.40 | 0.02502 | 39.972 | 0.8932 |
| 0.30 | 0.02282 | 43.817 | 0.8531 |

At a true $S_w = 0.50$ the measured resistivity is
$35.920\ \Omega\,\mathrm{m}$ and Archie returns $\mathbf{0.9422}$. At full
saturation, Archie returns $1.2797$ — an impossible saturation, and therefore an
unambiguous flag that a second conduction path exists.

The useful part: the *size* of the discrepancy is a measurement. An inversion
that returns $S_w = 1.28$ in a rock known to be fully saturated says the clay
path carries a substantial share of the current, and the shortfall can be
attributed quantitatively through a shaly-sand model. A silently clipped
$S_w = 1.00$ discards that information. This is why the correct response to an
impossible saturation is a better model, not a clamp.

## 9. Failure mode 2 — saturation and salinity are not separable

The measured quantity is $\rho_t$; the unknowns are $\phi$, $S_w$, $a$, $m$, $n$
and the fluid. Even with $a$, $m$, $n$ fixed, the pair $(\phi, \rho_w)$ is
degenerate: a less porous rock with a fresher fluid has the same resistivity as a
more porous rock with a saltier one. The demonstration fixes
$\rho_t = 50.0\ \Omega\,\mathrm{m}$ and uses a synthetic pore-fluid relation
$\rho_w = 2.00 + 0.60/C$ with $C$ in $\mathrm{mol\,L^{-1}}$:

| $\phi$ | required $\rho_w$ ($\Omega$ m) | required $C$ ($\mathrm{mol\,L^{-1}}$) |
|---|---|---|
| 0.24 | 1.837 | no solution |
| 0.26 | 2.156 | 3.856 |
| 0.28 | 2.500 | 1.200 |
| 0.30 | 2.870 | 0.690 |
| 0.32 | 3.265 | 0.474 |

The salinity varies by a factor of eight across a porosity range of six points.
The 0.24 row has **no solution**: that combination cannot reach the measured
resistivity at all, which is itself useful information — the data have excluded
the low-porosity end. But within the admissible band the measurement does not
choose, and a hydrological interpretation must bring an independent porosity
(neutron, NMR, seismic) or fluid sample.

Note also that $\rho_w \leftrightarrow$ concentration is an *additional* empirical
relation, in this case a purely synthetic straight line. Real relations are
non-linear, temperature-dependent and ion-specific, and the confidence interval
on salinity is usually dominated by that step rather than by the resistivity.

## 10. Assumptions and regime of validity

**Archie assumes, and you must state:**

1. **Clean matrix.** No clay or other conductive mineral. The presence of either
   breaks the single-mechanism model of Section 8.
2. **Single conducting phase.** Water in the pores, hydrocarbons or gas being
   insulators. If the non-wetting phase is conductive, $I = S_w^{-n}$ has no
   basis.
3. **Connected, homogeneous pore water.** Uniform $\rho_w$ throughout the
   measured volume. A salinity gradient inside the support volume of the
   measurement violates this and produces an apparent saturation that is a
   mixture.
4. **Empirical exponents with a stated provenance.** $a$, $m$, $n$ are fitted on
   comparable rock; $n$ in particular is known to depend on saturation history
   (drainage versus imbibition) and can be far from 2.
5. **No interfacial polarisation or frequency dispersion.** At low frequency in
   the presence of clay, or in the presence of metallic minerals, complex
   conductivity is required, and induced polarisation is the diagnostic.
6. **Isotropic, homogeneous medium at the scale of the measurement.** A
   fractured medium with oriented fractures is anisotropic, and the resistivity
   is directional.

**Where the numbers come from.** Every number in this lesson is printed by
[`code/archie_and_saturation_demo.py`](./code/archie_and_saturation_demo.py) and
is a synthetic teaching value. The only standard constants used are the
definitions of resistivity and conductivity.

## 11. Python demonstration

[`code/archie_and_saturation_demo.py`](./code/archie_and_saturation_demo.py)
prints the $F$ table, the bundle derivation and the tortuosity paradox, the
saturation inversion, the elasticity table, the clay-conduction table with the
$S_w > 1$ diagnostic, the synthetic transition-zone inversion at two different
$m$, the $(\phi, \text{salinity})$ ambiguity, and the reference numbers used
above.

```bash
cd 14-hydrology-hydrogeophysics/03-petrophysics-hydrology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python archie_and_saturation_demo.py
```

## 12. Exercises

Graded problems are in
[`exercises/02-archie-and-saturation-exercises.md`](./exercises/02-archie-and-saturation-exercises.md)
with worked solutions in
[`exercises/02-archie-and-saturation-solutions.md`](./exercises/02-archie-and-saturation-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Write Archie's two equations and name every symbol, its unit and
> whether it is measured or fitted. **(b)** Derive $F = \tau^{2}/\phi$ for a tube
> bundle and explain why a measured $m = 2$ is not a contradiction of the
> derivation. **(c)** A synthetic sand has $\phi = 0.30$, $m = 2$, $n = 2$ and
> $\rho_w = 1.50\ \Omega\,\mathrm{m}$. Compute $\rho_0$ and the saturation for
> $\rho_t = 30.0\ \Omega\,\mathrm{m}$. **(d)** The correct $\rho_w$ was
> $2.00\ \Omega\,\mathrm{m}$. Recompute the saturation and state the direction of
> your error. **(e)** An inversion in a clay-rich interval returns $S_w = 1.2$.
> State what has happened and how you would use the number rather than discard
> it.

## Common pitfalls

1. **Quoting $S_w$ without the exponent set.** A saturation is a conditional
   statement.
2. **Clipping $S_w > 1$ to 1.** The excess is the measurement of the model error.
3. **Applying clean-sand exponents in a shaly interval.** This is the single most
   common source of wrong saturations.
4. **Treating $\rho_w$ as known.** It is usually the largest single unknown, and
   it is coupled to porosity.
5. **Forgetting that $n$ may depend on saturation history.** A drainage-derived
   $n$ applied to an imbibition curve is a model error, not noise.
6. **Letting the salinity step hide.** $\rho_w \to$ concentration is a second
   empirical relation with its own error; propagate both.
7. **Confusing water saturation with water content.** $S_w$ is a fraction of the
   pore volume; volumetric water content is $\theta = \phi S_w$. Reporting one as
   the other changes the answer by a factor of $\phi$.

## Related modules

- [01 Porosity-Permeability and Kozeny-Carman Relations](01-porosity-permeability-relations.md) —
  the porosity that Archie needs, and the error amplification downstream.
- [03 Seismic Velocity vs Saturation and Gassmann](03-seismic-velocity-saturation.md) —
  a second measurement of the same saturation that fails differently.
- [04 Building Geophysical Proxies for Hydrological Properties](04-geophysical-proxy-relations.md) —
  combining the two into a posterior.
- [Module 14-04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md) —
  where conductivity changes *because the fluid changed*, not the saturation.
- [Module 09-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  conduction mechanisms and the shaly-sand models.
- [Module 05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  Archie's law in the wider property-relations context.
