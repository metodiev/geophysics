---
id: 05-04-01
title: "Porosity, Density and Velocity Relationships"
level: advanced
prereqs: ["05-01-01", "04-01-05"]
tags: [porosity, density, mixing-laws, saturation, rock-physics]
---

# Porosity, Density and Velocity Relationships

## Learning objectives

1. **Define** porosity, saturation and bulk density, and derive the density
   mixing law from a control volume.
2. **State** the range over which each rock property varies and why a single
   "typical" value is not a scientific statement.
3. **Derive** the relation between pore-fluid substitution and bulk density, and
   quantify its effect on seismic velocity.
4. **Explain** why density is the best-known rock property and velocity the
   least well predicted.
5. **Check** a rock-physics relation for its limits.

## Prerequisites

- [05-01-01 The Central Idea](../01-what-geophysics-measures/01-physical-property-contrast.md)
- [04-01-05 Rock Physics Basics](../../04-earth-science-geology/01-earth-structure/05-rock-physics-basics.md)

## 1. Intuition

Density is arithmetic: the mass of a rock is the sum of the masses of its parts.
Velocity is not arithmetic: it depends on how the parts are arranged, on the
stiffness of the frame, and on whether the pore fluid can move. That asymmetry —
density predictable, velocity not — drives the entire structure of rock physics.

## 2. Definitions

**Porosity** $\phi = V_\text{pore}/V_\text{total}$, dimensionless, $0 \le \phi <
1$. **Effective porosity** counts only connected pores, which is what matters
for flow and for most elastic behaviour.

**Saturation** $S_w = V_\text{water}/V_\text{pore}$, and for two phases
$S_w + S_h = 1$.

**Bulk density** $\rho_b = (1-\phi)\rho_m + \phi\rho_f$, where $\rho_m$ is the
mineral (grain) density and $\rho_f$ the fluid density.

**Variability.** Every property below spans a wide range, and any number quoted
without a range and a source is a mistake:

| Property | Order of magnitude of variability | Dominated by |
|---|---|---|
| Porosity | $10^{-3}$ to $0.5$ (fractured to unconsolidated) | deposition, diagenesis |
| Grain density | a factor of ~1.5 (e.g. quartz-rich to heavy-mineral-rich) | mineralogy |
| Fluid density | a factor of ~2–3 for water/gas | fluid type, salinity |
| $V_p$ | a factor of 2–4 in crustal rocks | porosity, mineralogy, fluid |
| $V_s$ | a factor of 2–5 | porosity, mineralogy, fluid (weakly) |

None of these numbers is a rock property; each is a *range*, and the honest way
to use them is to compute a bound or to cite a measured value with its
provenance.

## 3. Derivations

### 3.1 Density mixing law

Take a control volume $V$. Mass $= (1-\phi)V\rho_m + \phi V\rho_f$. Divide by
$V$: $\rho_b = (1-\phi)\rho_m + \phi\rho_f$. Dimensions: both terms are
kg/m³. ✓

With two fluids present, $\rho_f = S_w\rho_w + (1-S_w)\rho_h$ by the same
argument, so

$$\rho_b = (1-\phi)\rho_m + \phi\left[S_w\rho_w + (1-S_w)\rho_h\right].$$

### 3.2 Density change on fluid substitution

Replacing fluid 1 with fluid 2 at constant $\phi$:

$$\Delta\rho_b = \phi(\rho_2 - \rho_1).$$

This is exact and requires no assumptions. For $\phi = 0.2$ and water
($\rho = 1000$ kg/m³) replaced by a light gas ($\rho = 200$ kg/m³),
$\Delta\rho_b = 0.2(-800) = -160$ kg/m³.

### 3.3 The effect on velocity: two parts, one arithmetic and one not

$V_p = \sqrt{(K + \frac43 G)/\rho}$. The density change is known exactly
(Section 3.2). The modulus change is *not*: it depends on the frame, the fluid
compressibility and the frequency, and requires an effective-medium theory
([05-04-02](./02-effective-medium-theory.md), [05-04-03](./03-gassmann-fluid-substitution.md)).

A purely kinematic consequence worth knowing: if the shear modulus is unchanged
(Gassmann's prediction), then $V_s$ changes *only* through density:

$$\frac{V_s^\text{sat}}{V_s^\text{dry}} = \sqrt{\frac{\rho_\text{dry}}
{\rho_\text{sat}}}.$$

This is a testable claim, and its violation points to a mechanism Gassmann
excludes. The module demonstration measures, for a stated synthetic case,
$\rho_\text{dry} = 2120$ kg/m³ and $\rho_\text{sat} = 2320$ kg/m³ giving
$V_s^\text{sat}/V_s^\text{dry} = 0.955925$.

### 3.4 Limits

- $\phi \to 0$: $\rho_b \to \rho_m$, and the fluid has no effect on any
  property. Correct.
- $\phi \to 1$: $\rho_b \to \rho_f$; there is no rock. Correct but
  unphysical (no load-bearing frame).
- Fluid substitution at constant $\phi$ changes density exactly and modulus
  approximately.

### 3.5 Porosity from a mass balance, and how badly it amplifies errors

The density law of Section 3.1 is usually used in reverse: measure $\rho_b$,
assume $\rho_m$ and $\rho_f$, and solve for $\phi$. The inversion is trivial and
the error propagation is not.

$$\rho_b = (1-\phi)\rho_m + \phi\rho_f
\qquad\Longrightarrow\qquad
\boxed{\;\phi = \frac{\rho_m - \rho_b}{\rho_m - \rho_f}\;}$$

Dimensional check: numerator and denominator are both kg m⁻³, so $\phi$ is
dimensionless ✓ — and note that the *result* is a ratio of density differences,
which is exactly where the sensitivity comes from.

**Sensitivity.** Differentiate with respect to the measured quantity:

$$\frac{\partial\phi}{\partial\rho_b} = -\frac{1}{\rho_m-\rho_f},
\qquad
\frac{\partial\phi}{\partial\rho_m} = \frac{\rho_b-\rho_f}{(\rho_m-\rho_f)^2},
\qquad
\frac{\partial\phi}{\partial\rho_f} = \frac{\rho_m-\rho_b}{(\rho_m-\rho_f)^2}.$$

With $\rho_m = 2650$, $\rho_f = 1020$ kg/m³ the denominator is 1630 kg/m³, so:

| error in the input | resulting error in $\phi$ |
|---|---|
| $\rho_b$ known to $\pm10$ kg/m³ | $\pm0.0061$ |
| $\rho_m$ assumed wrong by $\pm30$ kg/m³ | $\pm0.018$ |
| $\rho_f$ assumed wrong by $\pm50$ kg/m³ | $\pm0.009$ |

**Physical interpretation.** The *grain density* is the dominant error source,
and it is the one usually assumed. A 30 kg/m³ error in $\rho_m$ — about 1.1%,
easily produced by getting the clay fraction or the heavy-mineral content wrong —
costs 1.8 porosity units. Since typical porosities are 0.05–0.35, that is a
5–36% relative error in porosity from an assumption rather than a measurement.
**The grain density is measurable (on cuttings or by pycnometry) and should be
measured**, and its provenance reported with any porosity derived this way.

### 3.6 Three phases, and the bound-water trap

Clay-bearing rocks have a third component that is not free fluid: water bound to
clay surfaces. It contributes to the total mass and to the total porosity, but it
does not behave as a free fluid for flow *or* for most elastic purposes.

Write total porosity as $\phi_t = \phi_\text{eff} + \phi_\text{bw}$ and include
bound water in the solid (since it moves with the frame):

$$\rho_b = (1-\phi_t)\rho_m + \phi_\text{bw}\rho_\text{bw}
+ \phi_\text{eff}\rho_f .$$

Rearranged, this is the *same* two-phase law with an effective grain density

$$\rho_m^\text{eff} = \rho_m + \frac{\phi_\text{bw}}{1-\phi_t}
\left(\rho_\text{bw} - \rho_m\right),$$

and a density *below* $\rho_m$ because $\rho_\text{bw}<\rho_m$. **The trap:** an
analyst who uses $\rho_m = 2650$ kg/m³ on a clay-rich rock is implicitly using a
value too high, and by the table of Section 3.5 that error propagates directly
into porosity. With $\phi_\text{bw}/(1-\phi_t) = 0.05$ and
$\rho_\text{bw} = 1000$ kg/m³, $\rho_m^\text{eff} = 2650 - 0.05(1650) =
2567.5$ kg/m³ — a 82.5 kg/m³ reduction, giving a porosity error of
$0.05$ by the sensitivity above. **Bound water is not a refinement; it is a
first-order term in shaly rocks.**

### 3.7 Impedance, and how much it moves with porosity

The seismic observable at normal incidence depends on the acoustic impedance
$Z = \rho_bV_p$. Its porosity sensitivity is the sum of a density part and a
velocity part:

$$\frac{\partial\ln Z}{\partial\phi}
= \frac{1}{\rho_b}\frac{\partial\rho_b}{\partial\phi}
+ \frac{1}{V_p}\frac{\partial V_p}{\partial\phi}
= \frac{\rho_f-\rho_m}{\rho_b}
+ \frac{1}{V_p}\frac{\partial V_p}{\partial\phi} .$$

The first term is known exactly:

$$\frac{\rho_f-\rho_m}{\rho_b}
= \frac{1020-2650}{2237.5} = -0.7285\ \text{per unit } \phi
\quad\text{(using Section 6.1's values)} .$$

So **each unit of porosity costs 73% of the impedance through density alone**.
The second (velocity) term requires a rock-physics model
([05-04-02](./02-effective-medium-theory.md),
[05-04-03](./03-gassmann-fluid-substitution.md)) and is typically of the same
magnitude, which is why impedance is such a sensitive porosity indicator and
such a poor *uniquely interpretable* one: two terms of comparable size, one
known and one modelled.

### 3.8 The impedance sensitivity, with the measured velocity term

Section 3.7 separated the impedance sensitivity into a known density term and a
modelled velocity term. The demonstration supplies the second.

$$\frac{\partial\ln Z}{\partial\phi}
= \underbrace{\frac{\rho_f-\rho_m}{\rho_b}}_{\text{known: }-0.7285}
+ \underbrace{\frac{1}{V_p}\frac{\partial V_p}{\partial\phi}}_{\text{modelled}} .$$

Evaluating the velocity term from the stated synthetic frame law
($K_\text{dry} = K_\text{min}(1-\phi/\phi_c)$, $\phi_c = 0.40$, fluid A) and
Gassmann, the measured impedances are
$Z(0.10) = 1.3470\times10^{7}$, $Z(0.20) = 1.0809\times10^{7}$ and
$Z(0.30) = 7.7267\times10^{6}$ kg m⁻² s⁻¹, so the central difference at
$\phi = 0.20$ gives

$$\frac{\partial\ln Z}{\partial\phi} = \frac{\ln Z(0.10)-\ln Z(0.30)}
{0.10-0.30} = -2.779 .$$

Splitting it with the density term evaluated at the same state
($\rho_b = 2320$ kg m⁻³, so $(\rho_f-\rho_m)/\rho_b = -0.7112$):

| contribution | value | share |
|---|---|---|
| density, $(\rho_f-\rho_m)/\rho_b$ | $-0.7112$ | 26% |
| velocity, $(1/V_p)\,\partial V_p/\partial\phi$ | $-2.068$ | 74% |
| total $\partial\ln Z/\partial\phi$ | $-2.779$ | 100% |

with $\partial V_p/\partial\phi = -9175$ m s⁻¹ per unit porosity
(central difference, same states).

**Read that as a design conclusion — and note it is the opposite of the intuitive
guess.** The **velocity term dominates the impedance sensitivity by a factor of
2.9**. An impedance-derived porosity is therefore *mostly a rock-physics model
result*, not a density measurement, and it inherits the frame-law uncertainty
rather than the grain-density uncertainty of Section 3.5. The intuition that
"density is the well-known part, so impedance is mostly density" is exactly
backwards here, and only the arithmetic shows it.

**The caveat that keeps this honest.** The split depends on the frame law, which
is a stated *synthetic* choice. A different frame law changes the velocity term
markedly — that is the point: **the dominant term is the modelled one**, so the
conclusion's uncertainty is dominated by the rock-physics model, not by the
density measurement.

### 3.9 Why density cannot give velocity: the counting argument

Count the unknowns and the observables, because the reason is structural and not
a matter of cleverness.

| quantity | status |
|---|---|
| $\phi$ | unknown |
| $\rho_m$, $\rho_f$ | mineralogy and fluid — partly independent |
| $K_\text{dry}$, $G_\text{dry}$ | **not observable in density** |
| $K_\text{min}$, $K_\text{fl}$ | constituent moduli |
| $S_w$ | unknown |

Measuring $\rho_b$ gives **one** number, and it constrains only the combination
$(1-\phi)\rho_m + \phi\rho_f$. Velocity depends on $\phi$, on the *frame*
moduli $K_\text{dry}$ and $G_\text{dry}$, on $K_\text{min}$ and on $K_\text{fl}$.
The frame moduli are a function of the pore *geometry* — crack-like versus
equidimensional pores stiffen a rock completely differently at the same porosity
— and geometry leaves no trace in density at all. **Two rocks with identical
porosity, mineralogy and saturation can have velocities differing by tens of
percent; they necessarily have identical densities.** That is the whole
justification for the effective-medium machinery of the next two lessons.

## 4. Units and dimensional analysis

| Quantity | Symbol | Unit |
|---|---|---|
| porosity, saturation | $\phi$, $S$ | dimensionless |
| density | $\rho_m, \rho_f, \rho_b$ | kg m⁻³ (or g cm⁻³, ×10³) |
| velocity | $V_p, V_s$ | m s⁻¹ (or km s⁻¹, ×10³) |
| moduli | $K, G$ | Pa |

Check: $\sqrt{\mathrm{Pa}/(\mathrm{kg\,m^{-3}})} = \sqrt{\mathrm{m^2s^{-2}}} =
\mathrm{m\,s^{-1}}$. ✓

## 5. Assumptions

1. **Volume additivity.** True for porosity, porosity of disconnected pores
   included.
2. **Grain density is known.** It is measured on cuttings or from a mineral
   model; assuming a value introduces a systematic error of up to ~100 kg/m³.
3. **The fluid density is known** with its salinity, pressure and temperature.
4. **The velocity relation** additionally needs a modulus model — not implied by
   the density law, and not derivable from it.

## 6. Worked examples

**6.1 Density from porosity.** $\phi = 0.25$, $\rho_m = 2650$,
$\rho_w = 1000$: $\rho_b = 0.75(2650)+0.25(1000) = 1987.5+250 = 2237.5$ kg/m³.

**6.2 Partial saturation.** $\phi = 0.25$, $S_w = 0.4$, $\rho_w = 1000$,
$\rho_h = 200$: $\rho_f = 0.4(1000)+0.6(200) = 520$ kg/m³, so
$\rho_b = 1987.5 + 0.25(520) = 2117.5$ kg/m³.

**6.3 Velocity is not density.** Two rocks with the same density can have
different velocities: a porous quartz rock and a less porous rock with denser
minerals can both reach 2400 kg/m³, while the frame stiffnesses, and hence
$V_p$, differ. Measured in the module demonstration for a stated synthetic
frame law: changing the pore fluid from a stated fluid A
($K = 2.2$ GPa, $\rho = 1000$ kg/m³) to fluid B ($K = 0.05$ GPa,
$\rho = 200$ kg/m³) at $\phi = 0.20$ changed $V_p$ by $+1.07\%$ and $V_s$ by
$+3.64\%$ — **with the same sign and different magnitudes**, because $V_p$ also
depends on the bulk modulus while $V_s$ does not.

**6.4 Porosity sensitivity.** At $\phi = 0.02$ the same substitution changed
$V_p$ by $+0.17\%$; at $\phi = 0.35$ by $-7.70\%$. The fluid effect grows steeply
with porosity — and changes sign for $V_p$ at high porosity, because there the
density reduction outweighs the modulus reduction.

### 6.5 Extended worked example: a complete 4-D feasibility calculation

This is the calculation that decides whether time-lapse seismic could monitor a
fluid change, and it uses every part of this lesson.

**Stated inputs (all SYNTHETIC, chosen for the exercise).** Porosity
$\phi = 0.25$; mineral density $\rho_m = 2650$ kg/m³; fluid A is brine with
$\rho_A = 1050$ kg/m³; fluid B is a light hydrocarbon with
$\rho_B = 350$ kg/m³. Baseline saturation $S_w = 1.0$; monitor saturation
$S_w = 0.5$. Bulk modulus inputs (needed for the velocity step) are
$K_\text{min} = 37$ GPa, $K_A = 2.2$ GPa, $K_B = 0.15$ GPa.

**Step 1 — fluid density.** Wood's-style volume average of density is exact:
$\rho_f = S_w\rho_w + (1-S_w)\rho_h$.
Baseline: $\rho_f = 1050$ kg/m³. Monitor: $\rho_f = 0.5(1050)+0.5(350)
= 700$ kg/m³.

**Step 2 — bulk density.** $\rho_b = (1-\phi)\rho_m + \phi\rho_f$.
Baseline: $\rho_b = 0.75(2650)+0.25(1050) = 1987.5+262.5 = 2250.0$ kg/m³.
Monitor: $\rho_b = 1987.5+175.0 = 2162.5$ kg/m³.
Change: $\Delta\rho_b = \phi(\rho_f^\text{mon}-\rho_f^\text{base})
= 0.25(-350) = -87.5$ kg/m³, a $3.89\%$ reduction. Note this is *exact* — no
assumptions beyond the volume additivity of the mixing law.

**Step 3 — fluid bulk modulus.** $1/K_f = S_w/K_w + (1-S_w)/K_h$. Baseline
$K_f = 2.2$ GPa. Monitor:
$1/K_f = 0.5/2.2 + 0.5/0.15 = 0.22727 + 3.3333 = 3.5606$ GPa⁻¹, so
$K_f = 0.2809$ GPa — much softer, because the gas-like phase dominates the
harmonic average even at 50% saturation.

**Step 4 — saturated modulus.** Applying Gassmann from a stated dry frame
$K_\text{dry} = 18.5$ GPa gives $K_\text{sat} = 20.5765$ GPa for the baseline
and $K_\text{sat} = 18.7787$ GPa for the monitor. The shear modulus is
unchanged at $G = 22.0$ GPa. (Note this is the $\phi = 0.25$ case; the
$\phi = 0.20$ worked value of 21.0248 GPa in
[05-04-03](./03-gassmann-fluid-substitution.md) is a different porosity.)

**Step 5 — velocities and impedance.** Baseline: the bracket is
$K_\text{sat}+\frac43G = 20.5765+29.333 = 49.9095$ GPa, so
$V_p = \sqrt{49.9095\times10^9/2250} = \sqrt{2.2182\times10^7} =
4709.8$ m/s.
$V_s = \sqrt{22\times10^9/2250} = \sqrt{9.7778\times10^6} = 3126.9$ m/s.
Impedance $Z = \rho_bV_p = 2250(4709.8) = 1.0597\times10^7$
kg m⁻² s⁻¹.

Monitor: bracket $= 18.7787+29.333 = 48.1120$ GPa, so
$V_p = \sqrt{48.1120\times10^9/2162.5} = \sqrt{2.2248\times10^7} = 4716.8$
m/s; $V_s = \sqrt{22\times10^9/2162.5} = \sqrt{1.0173\times10^7} = 3189.6$
m/s. Impedance $Z = 2162.5(4716.8) = 1.0200\times10^7$ kg m⁻² s⁻¹.

**Step 6 — the answer.** $\Delta Z/Z = -3.746\%$. Reflection-coefficient change
against a stated overburden of $Z_1 = 1.2\times10^7$: baseline
$R = (1.0597-1.2)/(1.0597+1.2) = -0.0621$; monitor
$R = (1.0200-1.2)/(1.0200+1.2) = -0.0811$. The reflection amplitude changes by
$|\Delta R| = 0.0190$, i.e. by 31% of the baseline value — large, and readily
detectable against typical seismic noise.

**Step 7 — what would break it.** Note the sign structure: $V_p$ *increased* by
only 0.15%, $V_s$ *increased* by 2.0%, and density fell by 3.9%. The impedance
change is a near-cancellation between a density term and a modulus term, so its
*relative uncertainty* exceeds that of any individual term. If $\phi$ were
uncertain by $\pm0.02$, the density term alone would be uncertain by
$\pm7$ kg/m³ ($0.3\%$), while the fluid-modulus term is far more sensitive,
because $1/K_f$ depends almost linearly on the gas saturation for a soft phase:
$K_f$ fell from 2.2 GPa to 0.2809 GPa on going from $S_w = 1.0$ to 0.5.
**The conclusion "the impedance change is detectable" survives a plausible
uncertainty budget; the conclusion "the saturation change is exactly 0.5" does
not**, and a real study must report the two statements separately.

### 6.6 Worked arithmetic: the same rock, three assumed grain densities

Take a measured bulk density $\rho_b = 2237.5$ kg/m³ and a fluid density of
1020 kg/m³, and compute porosity under three assumptions.

| assumed $\rho_m$ (kg/m³) | $\phi = (\rho_m-\rho_b)/(\rho_m-\rho_f)$ |
|---|---|
| 2650 (quartz-rich) | $(2650-2237.5)/1630 = 0.2531$ |
| 2750 (heavy minerals) | $(2750-2237.5)/1730 = 0.2962$ |
| 2567.5 (clay-corrected, Section 3.6) | $(2567.5-2237.5)/1547.5 = 0.2132$ |

**The spread is 0.213 to 0.296 — a factor of 1.39 in porosity — from an
assumption about mineralogy, with the density measurement held fixed.** Any
interpretation that depends on porosity (permeability, flow, velocity) inherits
that factor. This is the concrete form of Section 3.5's sensitivity table, and it
is why a petrophysical report must state the grain density *and its provenance*
alongside the porosity.

**Cross-check with the direct calculation.** Section 6.1 computed
$\rho_b = 2237.5$ kg/m³ from $\phi = 0.25$, $\rho_m = 2650$,
$\rho_f = 1000$ kg/m³. Inverting with the same inputs:
$(2650-2237.5)/(2650-1000) = 412.5/1650 = 0.2500$ ✓ — the round trip is exact,
which checks the algebra but not the assumptions. **A round trip with the same
assumed inputs always returns the same answer; that is what makes it necessary
and not sufficient.**

### 6.7 A shortcut that fails: "porosity follows from density"

**The shortcut.** Report a porosity log computed from a density log using a
literature grain density, and treat it as a measurement.

**Why it fails, in three ways.**

1. **It is not a measurement.** It is an *inversion* of a measurement under two
   assumptions ($\rho_m$, $\rho_f$), and the sensitivity table of Section 3.5
   shows the assumptions can dominate. The correct description is "porosity
   inferred from bulk density assuming $\rho_m = 2650$ and $\rho_f = 1020$
   kg/m³", and the uncertainty must be carried through.
2. **It ignores bound water.** Section 3.6: in shaly rock the effective grain
   density can be 80 kg/m³ below the mineral value, worth 5 porosity units.
3. **It is unfalsifiable as stated.** Nothing in the density measurement tests
   the mineralogy assumption, so the error is invisible in the report unless an
   independent porosity measurement (NMR, neutron, core) is compared.

**What to do instead.** Measure $\rho_m$ where possible (cores, cuttings,
mineralogy from XRD); where not, quote a *range* of grain densities, carry the
resulting porosity range, and report the sensitivity
$\partial\phi/\partial\rho_m = (\rho_b-\rho_f)/(\rho_m-\rho_f)^2$ so a reader can
recompute it for their own assumptions.

## 7. Python demonstration

`code/gassmann_demo.py` (Sections 2, 3 and 5) and `code/petrophysics_demo.py`
(Section 1) provide the numbers above. All inputs are labelled SYNTHETIC.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/01-porosity-density-velocity-exercises.md`](./exercises/01-porosity-density-velocity-exercises.md).

**Common mistakes.** (1) Quoting a "typical" porosity, density or velocity
without a range. (2) Using total porosity where effective porosity is required.
(3) Ignoring fluid density dependence on pressure and temperature. (4) Assuming
that a density change implies a proportional velocity change. (5) Using grain
density as a fitted parameter when it can be measured.

**Applications.** Density logs and their interpretation; synthetic seismogram
generation (acoustic impedance = $\rho V_p$); 4-D seismic feasibility, where the
$\phi(\rho_2-\rho_1)$ term sets the amplitude; gravity modelling with a
petrophysically constrained density.

## 9. Further reading

- **Mavko, Mukerji & Dvorkin, *The Rock Physics Handbook*.** Chapters 1–2.
  Level: graduate.
- **Schön, J. H. *Physical Properties of Rocks: Fundamentals and Principles of
  Petrophysics* (2nd ed.).** Level: graduate. Ranges with provenance.
- **Bourbié, Coussy & Zinszner, *Acoustics of Porous Media*.** Level: graduate.

## 10. Related lessons

- [05-04-02 Effective-Medium Theories](./02-effective-medium-theory.md)
- [05-04-03 Gassmann Fluid Substitution](./03-gassmann-fluid-substitution.md)
- [04-01-05 Rock Physics Basics](../../04-earth-science-geology/01-earth-structure/05-rock-physics-basics.md)

## Self-assessment checklist

- [ ] I can derive the density mixing law and check its units.
- [ ] I can compute $\Delta\rho = \phi(\rho_2-\rho_1)$ for a substitution.
- [ ] I can state the variability of each property as a range.
- [ ] I can explain why velocity is not a function of density.
- [ ] I can state which rock properties are measured and which are modelled.
