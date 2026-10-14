---
id: 05-04-07
title: "Electrical Properties, Archie's Law and Clay Effects"
level: advanced
prereqs: ["05-04-01"]
tags: [archie, resistivity, clay, shaly-sand, cementation-exponent]
---

# Electrical Properties, Archie's Law and Clay Effects

## Learning objectives

1. **Derive** the form of Archie's law from a geometric scaling argument, and
   state what each exponent means.
2. **State** the assumptions of Archie's law and identify the rock types that
   violate each.
3. **Demonstrate** the failure of Archie's law in clay-bearing rock, and
   quantify the bias as a function of porosity.
4. **Describe** the conduction mechanisms that operate in parallel, and how a
   shaly-sand model adds an explicit clay term.
5. **Explain** why a resistivity measurement is a *bulk* property that depends on
   the fluid and on the geometry of the pore space.

## Prerequisites

- [05-04-01 Porosity, Density and Velocity](./01-porosity-density-velocity.md)
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md)

## 1. Intuition

Current in a water-saturated rock flows through the pore water, along a
tortuous path whose length and connectivity depend on porosity. Add a
conducting mineral (clay, sulphide, graphite) and a second, solid-state path
appears. Archie's law describes the first path only; it therefore overestimates
water saturation whenever the second path is active. The failure is not
subtle — the demonstration below returns a saturation greater than 1.

## 2. Archie's law

$$S_w^n = \frac{a\,R_w}{\phi^m R_t}, \qquad \text{or} \qquad
R_t = \frac{a\,R_w}{\phi^m S_w^n}.$$

| Symbol | Meaning | Unit | Typical role |
|---|---|---|---|
| $R_t$ | bulk (true) resistivity of the formation | Ω·m | measured |
| $R_w$ | pore-water resistivity | Ω·m | measured or estimated |
| $\phi$ | porosity | dimensionless | measured |
| $S_w$ | water saturation | dimensionless | unknown to be found |
| $a$ | empirical prefactor | dimensionless | fitted, often near 1 |
| $m$ | cementation exponent | dimensionless | typically 1.3–3 |
| $n$ | saturation exponent | dimensionless | typically near 2 |

Dimensional check: $R_w/(\phi^m R_t)$ is dimensionless (Ω·m cancels), so the
left side must be dimensionless — it is. ✓

## 3. Derivation of the scaling form

Consider a cube of side $L$ saturated with water. Conduction along a
tortuous path of length $L_e = L\,L_r$ (tortuosity factor $L_r \ge 1$) and
effective cross-section $A_e = L^2\,\phi/L_r$ (volume conservation). Resistance
along the path:

$$R = \frac{R_w L_e}{A_e} = \frac{R_w\,L\,L_r}{L^2\phi/L_r}
= \frac{R_w L_r^2}{L\phi}.$$

Bulk resistivity $R_t = R(L^2/L) = R_w L_r^2/\phi$. Comparing with Archie's
form $R_t = aR_w/\phi^m$ shows:

- $m = 1$ corresponds to straight tubes ($L_r = 1$, $a = 1$);
- $m > 1$ arises because tortuosity *increases* as porosity decreases, which is
  an empirical statement (tortuosity is not known a priori);
- $a$ absorbs the geometry and the prefactor $L_r^2$.

Hence $m$ and $a$ are not constants of nature: they are fits. This is why they
should be measured on cores from the interval, not taken from a table.

The saturation exponent $n$ enters because the conducting water occupies only a
fraction $S_w$ of the pore space, and its distribution changes the tortuosity
path further — again empirically.

## 4. Assumptions and their violations

| Assumption | Violated by |
|---|---|
| Conduction only through pore water | clay, sulphides, graphite, metallic minerals |
| No surface conduction | clay-bearing sands and shales (largest effect) |
| Water is the only fluid conducting | oil/gas are insulators (consistent) |
| Uniform, non-patchy saturation | patchy saturation; also affects the exponent $n$ |
| Porosity is intergranular and connected | vuggy, fractured, or isolated porosity |
| $m$, $a$, $n$ known for this rock | almost always the weakest link |
| Isotropic | anisotropic shale fabrics |

This is a long list, and it is honest: Archie's law works extremely well in
clean, high-porosity sandstones and poorly elsewhere.

## 5. Parallel conduction and the shaly-sand model

With two conduction paths, total conductivity is the sum:

$$\sigma_t = \sigma_\text{Archie} + \sigma_\text{clay}
= \frac{\phi^mS_w^n}{aR_w} + \text{(clay term)}.$$

The clay term is often written as proportional to $S_w$ or to the cation
exchange capacity per unit pore volume (Waxman–Smits). The exact form differs
between models; the *structure* — an additive term that Archie ignores — is the
essential point.

## 6. Worked example (measured): Archie inverted on clay-contaminated data

Stated SYNTHETIC inputs: $a = 1$, $m = 2$, $n = 2$, $R_w = 0.5$ Ω·m, and an
added clay conduction of $0.02$ S/m in parallel. True saturation
$S_w = 0.40$ in every case.

| $\phi$ | $S_w$ true | $S_w$ from Archie | error |
|---|---|---|---|
| 0.05 | 0.40 | **1.3266** | $+0.9266$ |
| 0.10 | 0.40 | 0.7483 | $+0.3483$ |
| 0.20 | 0.40 | 0.5099 | $+0.1099$ |
| 0.30 | 0.40 | 0.4522 | $+0.0522$ |

Two things to notice. First, the bias is **always positive**: the extra
conductivity is read as extra water. Second, at $\phi = 0.05$ the inversion
returns $S_w = 1.33$ — **greater than one**, which is physically impossible.
A bound being violated is the clearest possible signal that the model is
outside its assumptions, and it should be reported as such rather than clipped
to 1.0 silently.

The bias is worst at low porosity because the Archie term
$\propto\phi^m$ is then smallest relative to the fixed clay term.

## 7. Practical guidance

1. **Measure $m$, $a$, $n$** on cores from the interval where possible; report
   them with the saturation.
2. **Check for clay** independently (gamma log, cation exchange capacity,
   mineralogy) before trusting an Archie saturation.
3. **Watch for $S_w > 1$** — it means the model, not the data, is wrong.
4. **Report a range**: the uncertainty in $m$ alone can dominate the
   uncertainty in $S_w$.
5. **Remember what is measured**: $R_t$ is a bulk property, an average over a
   volume far larger than a pore, and it depends on the fluid, the geometry and
   any conducting minerals.

## 8. Python demonstration

`code/petrophysics_demo.py` Section 4. It computes the table above, including
the impossible saturation, and prints the diagnostic conclusion. Change the
clay conduction term to zero and confirm that Archie becomes exact — a check
that the forward model and the inversion are self-consistent.

## 9. Exercises, mistakes, applications

Exercises: [`exercises/07-electrical-properties-exercises.md`](./exercises/07-electrical-properties-rock-exercises.md).

**Common mistakes.** (1) Using a handbook $m$ for a different lithology.
(2) Silently clipping $S_w > 1$. (3) Treating an apparent resistivity from a
surface survey as a formation resistivity. (4) Ignoring temperature and salinity
dependence of $R_w$. (5) Reporting saturation without the exponents used.

**Applications.** Formation evaluation from resistivity logs; groundwater
salinity estimation; contaminant mapping (the contrast is in the pore fluid);
mineral exploration for sulphides (where Archie's assumptions fail in the
opposite direction — the conduction is through the *solid*); geothermal
reservoir characterisation.

## Extended worked example: a two-term model versus Archie, done in full

Take the stated synthetic rock of Section 6, at $\phi = 0.10$,
$S_w = 0.4$, $a = 1$, $m = 2$, $n = 2$, $R_w = 0.5$ Ω·m, and a clay conduction
path contributing $S_w\cdot 0.02$ S/m.

**Pore-water conduction.** $\sigma_\text{Archie} = \phi^mS_w^n/(aR_w)
= 0.01\cdot0.16/0.5 = 3.2\times10^{-3}$ S/m, so the Archie-only bulk
resistivity is $R_t = 1/\sigma = 312.5$ Ω·m.

**Clay conduction.** $\sigma_\text{clay} = S_w\cdot0.02 = 8.0\times10^{-3}$ S/m.

**Total.** Conductivities in parallel add:
$\sigma_t = 3.2\times10^{-3}+8.0\times10^{-3} = 1.12\times10^{-2}$ S/m, so

$$R_t = 1/1.12\times10^{-2} = 89.3\ \Omega\cdot\mathrm{m}.$$

**What Archie makes of it.** Inverting the Archie model on
$R_t = 89.3$ Ω·m:

$$S_w^\text{Archie} = \left(\frac{aR_w}{\phi^mR_t}\right)^{1/n}
= \left(\frac{0.5}{0.01\cdot89.3}\right)^{1/2} = (0.5600)^{1/2} = 0.7483.$$

The true saturation is 0.40 and Archie returns 0.7483 — an overestimate of 87%
relative. (This value, 0.7483, is exactly what the demonstration prints at
$\phi = 0.10$, which is the cross-check that the hand calculation and the code
agree.)

**Why the clay term dominates here.** At $\phi = 0.10$ the pore-water
conductivity is $3.2\times10^{-3}$ S/m while the clay term is
$8.0\times10^{-3}$ S/m: the clay path carries **71%** of the current. Archie
attributes all of it to water and therefore demands more water than exists.

**The sensitivity that matters.** Doubling the assumed clay conductivity to
0.04 S/m gives $\sigma_t = 0.0032+0.016 = 0.0192$ S/m, $R_t = 52.1$ Ω·m, and
$S_w^\text{Archie} = (0.5/0.5208)^{1/2} = 0.9798$ — approaching the impossible
$S_w = 1$. So the *conclusion* "Archie fails badly at low porosity in clay-
bearing rock" is robust, while the *corrected saturation* is strongly dependent
on the clay conductivity, which is why shaly-sand models must calibrate that
term rather than assume it.

**The general lesson.** A model that has the wrong *structure* fails in a
way that is diagnosable (here, $S_w>1$ at the lowest porosity in the
demonstration's table) and not fixable by tuning its parameters. That is the
signature of an assumption being violated rather than a fit being imperfect.

## 10. Further reading

- **Archie, G. E. (1942).** The electrical resistivity log as an aid in
  determining some reservoir characteristics. *Trans. AIME* 146, 54–62.
- **Waxman, M. H. & Smits, L. J. M. (1968).** Electrical conductivities in
  oil-bearing shaly sands. *SPE Journal* 8, 107–122. Level: graduate. The
  canonical shaly-sand model.
- **Schön, J. H. *Physical Properties of Rocks* (2nd ed.).** Chapter 8. Level:
  graduate. Ranges of $m$ and $n$ with provenance.
- **09-01-02 Archie's Law** in the electrical methods module:
  [09-01-02 Archie's Law](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md).

## 11. Related lessons

- [05-04-04 Velocity-Porosity-Clay Models](./04-velocity-porosity-clay.md)
- [09-01-01 Resistivity and Conductivity](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
- [09-01-04 Clay and Surface Conduction](../../09-electrical-em-methods/01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)

## Self-assessment checklist

- [ ] I can derive Archie's scaling form and explain what $a$ and $m$ absorb.
- [ ] I can list six assumptions and a rock type that violates each.
- [ ] I can demonstrate and quantify the clay-induced bias.
- [ ] I can explain why $S_w > 1$ indicates a model failure.
- [ ] I can state what a resistivity measurement actually averages over.
