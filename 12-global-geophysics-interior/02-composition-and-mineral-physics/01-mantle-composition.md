---
id: 12-02-01
title: "Mantle Composition and Peridotite Models"
level: doctoral
prereqs: ["12-01-01", "12-01-04", "02-04-05", "05-04-02"]
tags: [global-geophysics, earth-interior, mantle-composition, peridotite, mineral-physics, mixing-laws]
---

# Mantle Composition and Peridotite Models

> **All models and data in this module are SYNTHETIC.** Mineral elastic
> properties, densities, modes and the Fe-substitution slopes used here are chosen
> teaching values, selected so that the aggregates land in a plausible range. They
> are not measurements, and no published rock or mineral property is reproduced.
> "Peridotite", "harzburgite" and "lherzolite" are used as rock names only.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** an aggregate density and elastic moduli from mineral modes and
   end-member properties, and **state** every piece of input that was assumed.
2. **Derive** the Voigt and Reuss bounds and **explain** why the Hashin–Shtrikman
   brackets lie *inside* them, not outside.
3. **Validate** a mixing calculation with the ordering test
   $\text{Reuss} \le \text{HS}^- \le \text{Hill} \le \text{HS}^+ \le \text{Voigt}$,
   and **explain** what a violation would mean.
4. **Compute** $v_p$, $v_s$, $v_p/v_s$ and $\nu$ for an aggregate, and
   **quantify** the sensitivity to olivine mode and to Mg#.
5. **Formulate** the inverse problem — which compositions fit a measured
   $(\rho, v_p, v_s)$ — and **show** how much a density constraint adds.
6. **Compare** thermal and compositional anomalies and **explain** why the *sign*
   of the density anomaly, not its size, is the discriminator.
7. **State** why a velocity anomaly alone cannot decide between a hot and a fertile
   mantle, and what observation can.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  the radial model whose velocities these aggregates must reproduce.
- [12-01-04 Lower-Mantle Heterogeneity and LLSVPs](../01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md) —
  the velocity anomalies that need a mineralogical interpretation.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md) —
  where $v_p$ and $v_s$ come from in $K$, $G$ and $\rho$.
- [05-04-02 Effective Medium Theory](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) —
  the general theory of bounds and mixing laws used here.

## 1. The problem: velocities are integrals, compositions are discrete

Seismology delivers $\rho$, $v_p$ and $v_s$ (with the caveat that $\rho$ is the
least directly measured of the three). Mineralogy delivers a *discrete* description:
which minerals are present, in what proportions, with which Fe/Mg ratios. Going from
one to the other requires an averaging theory, and every such theory is:

- **a bound, not an equation**, because the elastic response of a mixture depends on
  the geometry of the phases, which seismology does not measure;
- **linear in the volume fractions for the density** (an exact statement, since mass
  adds), but **nonlinear in the fractions for the moduli**;
- **sensitive to which knobs are turned**, because different compositions change
  $v_p$, $v_s$ and $\rho$ in correlated ways.

This lesson builds the machinery, computes an aggregate, validates it, and then
turns it around to ask the question that matters: *given a measured rock, what
compositions are admissible?* The answer is a family, and the interesting part is
how much of the family a density measurement removes.

## 2. Density: the exact part

If phase $i$ occupies volume fraction $f_i$ with density $\rho_i$, the aggregate
density is exactly

$$\rho = \sum_i f_i \rho_i,$$

because mass is additive and volumes add in the composite. The demonstration's
SYNTHETIC end members at Mg# = 0.90 are

| mineral | $\rho$ (g cm$^{-3}$) | $K$ (GPa) | $G$ (GPa) |
|---|---|---|---|
| olivine | 3.22 | 129.0 | 82.0 |
| orthopyroxene | 3.21 | 105.0 | 77.0 |
| clinopyroxene | 3.28 | 113.0 | 67.0 |
| garnet | 3.58 | 175.0 | 94.0 |

with a chosen lherzolite mode of 57 % olivine, 17 % orthopyroxene, 12 %
clinopyroxene and 14 % garnet. That gives $\rho = 3.276\ \mathrm{g\,cm^{-3}}$.
Nothing about this step is uncertain except the inputs.

## 3. Moduli: bounds, and what they mean

### 3.1 Voigt and Reuss

The **Voigt** average assumes uniform *strain* through the aggregate, so every phase
strains identically and the stiffness adds:

$$K_V = \sum_i f_i K_i, \qquad G_V = \sum_i f_i G_i .$$

The **Reuss** average assumes uniform *stress*:

$$\frac{1}{K_R} = \sum_i \frac{f_i}{K_i}, \qquad
\frac{1}{G_R} = \sum_i \frac{f_i}{G_i} .$$

These are the extremes: no microstructure can produce a mixture stiffer than Voigt
or softer than Reuss. Their mean,

$$K_\text{Hill} = \tfrac12\left(K_V + K_R\right),$$

is a convenient estimate with **no physical status** — it is not a bound and not a
theory. For the demonstration's mode: $K_V = 129.44$, $K_R = 126.59$,
$K_\text{Hill} = 128.01$ GPa; $G_V = 81.03$, $G_R = 80.39$, $G_\text{Hill} = 80.71$
GPa.

### 3.2 Hashin–Shtrikman

The HS bounds are obtained by imagining the stiffest phase as an inclusion in the
softest (the lower bound) or the softest in the stiffest (the upper bound), using
the exact two-phase result for a spherical inclusion in a host:

$$K_\text{HS} = K_1 + \frac{f_2}{\dfrac{1}{K_2-K_1}
+ \dfrac{1-f_2}{K_1 + \frac{4}{3}G_1}},$$

$$G_\text{HS} = G_1 + \frac{f_2}{\dfrac{1}{G_2-G_1}
+ \dfrac{2(1-f_2)\left(K_1+2G_1\right)}{5G_1\left(K_1+\frac{4}{3}G_1\right)}} .$$

With $K_2 > K_1$ these give the **lower** bound; swapping host and inclusion gives
the upper. Applied with the matrix of the remaining phases collapsed at its Reuss
limit (low side) and its Voigt limit (high side), the demonstration obtains
$K = 126.62$–$129.44$ GPa and $G = 80.41$–$81.02$ GPa, and the ordering test passes:

$$\text{Reuss} \; (126.59) \le \text{HS}^- \; (126.62) \le \text{Hill} \; (128.01)
\le \text{HS}^+ \; (129.44) \le \text{Voigt} \; (129.44).$$

Two remarks that matter more than the numbers:

- **The HS brackets are INSIDE the Voigt–Reuss range.** Getting this backwards is
  the commonest error in hand-written mixing code; the ordering test above is the
  cheapest possible check, and a violation means the recursion is wrong.
- **The exact multi-phase HS bounds require the incremental construction** (each
  phase added as an inclusion in the running composite, with relative fractions).
  The pair printed here is an *inner* bracket built from the exact two-phase formula
  and a collapsed matrix; it is a legitimate consistency check, not the rigorous
  bound. The general construction is in
  [05-04-02](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md).

### 3.3 Velocities

With the moduli and the density in consistent units,

$$v_p = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}, \qquad v_s = \sqrt{\frac{G}{\rho}},$$

($K$, $G$ in GPa and $\rho$ in g cm$^{-3}$ returns km s$^{-1}$), and for the
aggregate:

| scheme | $\rho$ (g cm$^{-3}$) | $v_p$ (km s$^{-1}$) | $v_s$ (km s$^{-1}$) | $v_p/v_s$ | $\nu$ |
|---|---|---|---|---|---|
| Voigt | 3.276 | 8.514 | 4.973 | 1.712 | 0.2410 |
| Hill | 3.276 | 8.481 | 4.964 | 1.709 | 0.2395 |
| Reuss | 3.276 | 8.448 | 4.954 | 1.705 | 0.2379 |

The spread is 0.8 % in $v_p$ and 0.4 % in $v_s$ — the largest single uncertainty in
any mineralogical interpretation of a velocity, and it is *not* reduced by better
seismology. This is the point of reporting bounds: the mixing model contributes an
uncertainty of the same order as the seismic one.

## 4. Sensitivity: which knob does what

### 4.1 Olivine content

Holding the other three phases in their original ratio and varying the olivine
fraction:

| $f_\text{ol}$ | $\rho$ (g cm$^{-3}$) | $v_p$ (km s$^{-1}$) | $v_s$ (km s$^{-1}$) | $\Delta v_s$ (%) |
|---|---|---|---|---|
| 0.40 | 3.298 | 8.434 | 4.932 | — |
| 0.50 | 3.285 | 8.461 | 4.950 | +0.38 |
| 0.57 | 3.276 | 8.481 | 4.964 | +0.65 |
| 0.65 | 3.266 | 8.503 | 4.979 | +0.96 |
| 0.75 | 3.252 | 8.532 | 4.998 | +1.35 |
| 0.85 | 3.239 | 8.560 | 5.017 | +1.74 |

Increasing olivine content *raises both velocities* and *lowers the density*,
because the pyroxenes and garnet in this chosen parameter set are softer or denser
than olivine. The trend over the full range is a few per cent in $v_s$ — large
enough to matter, and comparable to the velocity anomalies seismology reports.

### 4.2 Fe content (Mg#)

Replacing Mg by Fe in every mineral (per the chosen slopes: density +3.2 % per unit
decrease of Mg#, bulk modulus −4.5 %, shear modulus −6.5 %):

| Mg# | $\rho$ (g cm$^{-3}$) | $v_p$ (km s$^{-1}$) | $v_s$ (km s$^{-1}$) | $\Delta v_s$ (%) |
|---|---|---|---|---|
| 0.95 | 3.271 | 8.499 | 4.976 | — |
| 0.90 | 3.276 | 8.481 | 4.964 | −0.24 |
| 0.86 | 3.280 | 8.466 | 4.954 | −0.44 |
| 0.82 | 3.284 | 8.452 | 4.944 | −0.63 |
| 0.78 | 3.288 | 8.437 | 4.935 | −0.82 |

Iron-rich mantle is **denser and slower** — the two effects reinforce each other
because the moduli fall while the density rises.

### 4.3 The crucial asymmetry

Both knobs move $v_s$. The difference is in the **sign of the density change
relative to the velocity change**:

- more Fe (more fertile): $v_s \downarrow$, $\rho \uparrow$;
- more pyroxene/garnet: $v_s \downarrow$, $\rho \uparrow$;
- hotter: $v_s \downarrow$, $\rho \downarrow$.

Two compositional changes and one thermal change all lower $v_s$, but the thermal one
has the opposite density signature. **That is the whole game**: a velocity anomaly is
ambiguous, a velocity-plus-density anomaly is not.

## 5. The inverse problem: admissible compositions

Now the mining-and-mineralogy direction. Take a SYNTHETIC "measured" rock —
$f_\text{ol} = 0.60$, Mg# = 0.89, giving $\rho = 3.2730\ \mathrm{g\,cm^{-3}}$,
$v_p = 8.4858$, $v_s = 4.9669\ \mathrm{km\,s^{-1}}$ — and search a grid of
compositions, keeping those within a stated tolerance:

| constraint | compositions retained | $f_\text{ol}$ range | Mg# range |
|---|---|---|---|
| $v_p$, $v_s$ to ±0.5 % | 3142 | 0.38 – 0.85 | 0.76 – 0.96 |
| $v_p$, $v_s$ (±0.5 %) and $\rho$ (±0.2 %) | 1226 | 0.49 – 0.75 | 0.76 – 0.96 |

Reading:

- **Velocity alone admits almost everything.** The admissible set spans the whole
  olivine range of the grid — a *ridge* in composition space, exactly the same
  trade-off as the depth–velocity problem in
  [12-01-02](../01-seismic-structure-of-the-earth/02-crustal-structure.md), in
  compositional clothing. A velocity anomaly maps to a curve of compositions.
- **The density cuts the ridge**, removing about two thirds of the admissible
  compositions and, much more importantly, removing the *ends* of the ridge
  ($f_\text{ol}$ from 0.38–0.85 down to 0.49–0.75).
- The Mg# range is barely affected (0.76–0.96 in both), because Mg# trades almost
  perfectly against the mode: a more Fe-rich olivine is slower, so a more Fe-rich
  rock needs less olivine to reach the same velocity, and the density changes little
  along that ridge.

**The general lesson**, and it is the reason geodesy matters to mineralogy: where
velocities give a ridge, densities give a cut, because the density depends on the
mode and on Mg# through *different* combinations than the velocities do. The
quantitative version — 3142 compositions down to 1226 — is what "worth more than a
better velocity" means here.

## 6. Thermal versus compositional anomalies

The demonstration compares three anomalies of comparable velocity signature:

| anomaly | $\mathrm{d}\ln v_s$ (%) | $\mathrm{d}\ln\rho$ (%) | correlation |
|---|---|---|---|
| +100 K | −0.120 | −0.250 | same sign |
| +300 K | −0.360 | −0.750 | same sign |
| +5 % olivine mode | +0.192 | −0.199 | opposite |
| Mg# −0.03 (more Fe) | −0.146 | +0.096 | opposite |

(with the chosen sensitivities $\partial\ln v_s/\partial T = -1.2\times10^{-5}\
\mathrm{K^{-1}}$ and $\alpha = 2.5\times10^{-5}\ \mathrm{K^{-1}}$).

A hot anomaly lowers both $v_s$ and $\rho$; a more Fe-rich anomaly lowers $v_s$ and
*raises* $\rho$. Seismic velocity alone cannot separate them, and no amount of
additional velocity measurement will: they are degenerate in velocity by
construction. What breaks the degeneracy is an **independent density** — from
normal modes, from the free-air/Bouguer gravity field, or from the moment of inertia
(lesson [12-01-01 §6](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md)) —
or from a *third* observable that responds differently, such as attenuation or
anisotropy.

This is also why the temperature inferred from a tomographic anomaly in
[12-01-04](../01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md) is
a *conditional* statement: if the anomaly is compositional, the temperature
conversion is invalid, and the density is the only thing that says so.

## 7. Assumptions and regime of validity

1. **Elastic, isotropic, isotropic-material phases.** Each mineral is treated as
   elastically isotropic. Real olivine is strongly anisotropic, and an aligned
   aggregate inherits that (lessons
   [06](../01-seismic-structure-of-the-earth/06-outer-and-inner-core.md) and
   [12-02-03](03-ab-initio-mineral-physics.md)).
2. **No pressure or temperature correction.** The end-member properties are
   ambient-condition values. Applying them at 200 km depth ignores the 1–3 %
   velocity increase from compression — which is comparable to the composition
   differences being resolved. Real work must carry $P$–$T$ derivatives.
3. **One mode, one Mg#.** The grid assumes all minerals share a single Mg#;
   in reality garnet and pyroxene partition Fe differently from olivine.
4. **Volume fractions known exactly.** In practice modes come from petrology or
   from forward modelling, with their own uncertainties.
5. **Single-phase minerals.** No melt, no hydrous phases, no exsolution.
6. **Mixing model.** The Voigt–Reuss spread (0.8 % in $v_p$) is the model error;
   the true value lies between the HS bounds, whose exact multi-phase form needs the
   incremental construction.
7. **The density is measured.** Section 5's conclusion rests on a density known to
   0.2 %; if the density is itself inferred from the same velocities (e.g. through
   an assumed velocity–density scaling), the constraint is circular.

## 8. Worked examples

### Example 1 — the aggregate density and the exact part of the calculation

With modes $f = (0.57, 0.17, 0.12, 0.14)$ and densities
$(3.22, 3.21, 3.28, 3.58)$:

$$\rho = 0.57(3.22) + 0.17(3.21) + 0.12(3.28) + 0.14(3.58)
= 1.8354 + 0.5457 + 0.3936 + 0.5012 = 3.2759\ \mathrm{g\,cm^{-3}},$$

matching the printed 3.276. Note that this step has no model error at all: given the
modes and the mineral densities, the aggregate density is *defined*, not estimated.
Every subsequent step (moduli and therefore velocities) is a model.

### Example 2 — a Voigt average by hand, and its bound status

$K_V = 0.57(129) + 0.17(105) + 0.12(113) + 0.14(175) = 73.53 + 17.85 + 13.56 +
24.50 = 129.44$ GPa ✓ matches. Now perturb the mode, keeping the density fixed: move
0.05 from garnet to clinopyroxene. Then
$K_V = 0.57(129)+0.17(105)+0.17(113)+0.09(175) = 73.53+17.85+19.21+15.75 = 126.34$
GPa — a 2.4 % change in $K_V$ from a mode change that *lowers* the garnet content.
The Reuss average moves in the same direction by a similar amount, so the velocity
change is a few tenths of a per cent. **A mode change large enough to be petrologically
significant is worth only a fraction of a per cent in velocity** — one of the reasons
mantle composition is hard to infer from velocities alone.

### Example 3 — the degeneracy in numbers

From Section 5, a rock with $f_\text{ol} = 0.60$, Mg# = 0.89 and one with
$f_\text{ol} = 0.72$, Mg# = 0.84 both fit $v_p$ and $v_s$ within 0.5 %. Compute the
density difference using the trends of Section 4: raising $f_\text{ol}$ by 0.12
lowers $\rho$ by $0.12 \times 0.131 = 0.0157\ \mathrm{g\,cm^{-3}}$ (the slope is
$(3.239-3.298)/0.45 = -0.131$ per unit $f$); lowering Mg# by 0.05 raises $\rho$ by
$0.05 \times 0.100 = 0.0050$ (the slope is $(3.288-3.271)/0.17 = 0.100$ per unit
Mg#). Net: $-0.0107\ \mathrm{g\,cm^{-3}}$, i.e. **0.33 %** — larger than the 0.2 %
density tolerance used in Section 5. So the two compositions are separated by the
density alone, and that is exactly why the density constraint cut the admissible set
from 3142 to 1226 members. **The discriminator is a 0.3 % density difference.**

## 9. Python demonstration

`code/mantle_composition_demo.py` builds the end members, computes the aggregate
density, the Voigt, Reuss and Hill averages and the HS two-phase brackets with the
ordering test, then the velocities; runs the sensitivity studies for olivine content
and Mg#; searches composition space for the set consistent with a synthetic
"measured" rock with and without a density constraint; and compares thermal and
compositional anomalies. It prints labelled results with units and runs in about
0.2 s:

```bash
cd 12-global-geophysics-interior/02-composition-and-mineral-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mantle_composition_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/01-mantle-composition-exercises.md`](exercises/01-mantle-composition-exercises.md)
and
[`exercises/01-mantle-composition-solutions.md`](exercises/01-mantle-composition-solutions.md).

- **★** Compute an aggregate density and a Voigt modulus from a stated mode.
- **★★** Verify the ordering test and explain what a violation means.
- **★★** Compute the $v_s$ and $\rho$ signatures of a mode change and an Mg# change.
- **★★★** Design an observation set that would separate a thermal from a
  compositional anomaly at 1500 km depth, with a predicted resolution.

## Mastery checkpoint

Without notes:

> A rock has modes 0.62 olivine, 0.20 orthopyroxene, 0.10 clinopyroxene, 0.08 garnet
> with $\rho = (3.24, 3.22, 3.29, 3.60)$ and $G = (82, 77, 67, 94)$ GPa.
> **(a)** Compute the aggregate density and the Voigt and Reuss shear moduli, and
> the Hill value.
> **(b)** Compute $v_s$ from the Hill average.
> **(c)** A seismic study reports $v_s = 4.90\ \mathrm{km\,s^{-1}}$ for this rock and
> a density 1 % higher than your answer. Using the demonstration's Fe slopes
> ($\mathrm{d}\ln\rho/\mathrm{d}\text{Mg\#} = -0.032$ per unit and
> $\mathrm{d}\ln v_s = -0.049$ per unit) and its olivine-mode slopes
> ($\mathrm{d}\ln\rho = -0.040$ per unit $f_\text{ol}$,
> $\mathrm{d}\ln v_s = +0.039$ per unit $f_\text{ol}$), decide whether a *single*
> Fe-content change can explain both, and show the arithmetic. If it cannot, solve
> for the pair of changes that does.
> **(d)** State what additional measurement would most tighten the composition.

A worked version appears in the lesson-01
[solutions](exercises/01-mantle-composition-solutions.md).

## Common pitfalls

1. **Treating the Hill average as a bound.** It is a mean; the brackets are the
   HS pair, and they lie inside Voigt–Reuss.
2. **Using $K_V \le K_{HS}^+$.** The ordering is
   Reuss ≤ HS⁻ ≤ Hill ≤ HS⁺ ≤ Voigt; writing it the other way is a sign of a
   broken recursion or a confused derivation.
3. **Ignoring the mixing-model spread.** 0.8 % in $v_p$ is comparable to the
   anomalies being interpreted.
4. **Comparing a $P$–$T$ corrected seismic velocity with an ambient-condition
   mineral property.** The correction is of the same order as the signal.
5. **Believing a velocity anomaly implies a temperature.** Section 6: hot and
   Fe-rich have the same $v_s$ signature and opposite density signatures.
6. **Reporting a composition without the tolerance that produced it.** The output of
   Section 5 is a *set*, and its size is the honest measure of what is known.
7. **Forgetting that density is the least directly measured seismic quantity.** If
   the density came from a velocity–density scaling, using it to constrain velocity
   is circular.

## Related modules

- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  the target velocities and the moment-of-inertia constraint.
- [12-01-04 Lower-Mantle Heterogeneity and LLSVPs](../01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md) —
  where the velocity anomalies come from, and how well they are resolved.
- [02 Mantle Composition and Mineral Physics](README.md) — the module this lesson
  opens.
- [02 High-Pressure Experiments and Diamond Anvil Cells](02-high-pressure-experiments.md) —
  where the end-member properties are actually measured.
- [03 Ab Initio Mineral Physics and Elastic Constants](03-ab-initio-mineral-physics.md) —
  where the elastic tensors come from, including anisotropy.
- [04 Core Composition, Light Elements and the Geodynamo](04-core-composition.md) —
  the same logic applied to the core.
- [05-04-02 Effective Medium Theory](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) —
  the rigorous multi-phase bounds.

## Self-assessment checklist

- [ ] I can compute an aggregate density from modes and mineral densities.
- [ ] I can compute Voigt, Reuss and Hill moduli.
- [ ] I can apply the two-phase HS formula and state which bound it gives.
- [ ] I can run the ordering test and interpret a failure.
- [ ] I can compute $v_p$, $v_s$, $v_p/v_s$ and $\nu$ from $K$, $G$, $\rho$.
- [ ] I can quantify the velocity and density signatures of a mode and an Mg# change.
- [ ] I can explain why a density constraint cuts a compositional ridge.
- [ ] I can state why a velocity anomaly alone implies no temperature.
