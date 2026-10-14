---
id: 11-05-01
title: "Geophysical Signatures of Aquifers and Saline Interfaces"
level: advanced
prereqs: ["11-01-01", "09-01-01", "05-04-07"]
tags: [exploration-geophysics, groundwater, aquifers, salinity, archie, gassmann, ghyben-herzberg]
---

# Geophysical Signatures of Aquifers and Saline Interfaces

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Ghyben-Herzberg relation for a sharp fresh/salt interface from
   hydrostatic equilibrium, and **compute** the interface depth for a stated
   fresh-water head and density contrast.
2. **Apply** Archie's law to a saturated or partially saturated aquifer and
   **show** that one measured bulk conductivity is consistent with a family of
   (salinity, porosity, saturation, clay content) combinations.
3. **Derive** the Gassmann saturated bulk modulus and **compute** the P- and
   S-wave speeds on both sides of a water table from a dry frame.
4. **Explain** why $v_p$ responds strongly to saturation while $v_s$ responds
   only weakly, and **state** the measurement consequence for seismic methods.
5. **Compute** the gravity effect of a saturated layer with the Bouguer slab
   formula and **state** why it measures saturated mass rather than water-table
   depth.
6. **State** which physical property carries the signature of each aquifer
   element (saturation, salinity, lithology) and which method could see it.

## Prerequisites

- [11-01-01 Exploration Lifecycle: Reconnaissance to Reserve Definition](../01-exploration-workflow/01-exploration-lifecycle.md)
  — the framing of a survey as an answer to a question.
- [09-01-01 Resistivity, Conductivity and Ohm's Law in the Ground](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the electrical property this lesson relates to water.
- [05-04-07 Electrical Properties of Rocks](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md)
  — porosity-conductivity relations and the role of clay.
- [05-04-03 Gassmann Fluid Substitution](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md)
  — the fluid-substitution algebra used in Section 3.3.

> All models and data in this module are **SYNTHETIC**. No real aquifer, site or
> water sample is used, and no water chemistry or depth is quoted from a
> published measurement.

## 1. Intuition: an aquifer is not a material, it is a state

An aquifer is not a rock type. It is a *rock plus a fluid plus a geometry*: a
porous or fractured medium whose pores are connected and whose pores contain
water that can be pumped. That definition contains no bulk property at all. What
a geophysical survey measures is a bulk property — conductivity, acoustic
velocity, density — and the aquifer is one of several combinations of rock and
fluid that produce it.

This is the central difficulty of groundwater geophysics. Water is not detected.
A *contrast in a bulk property that correlates with water* is detected, and the
correlation is never unique:

- **Conductivity** responds to the conductivity of the pore water (salinity), to
  the volume fraction of water (porosity and saturation), and to clay. A
  conductive zone can be a saline aquifer, a clay aquitard, or a fresh aquifer
  with unusually abundant clay.
- **$v_p$** responds to the pore fluid's bulk modulus through Gassmann, so the
  water table is often a good seismic refractor — but only if drying the rock
  changes its elastic moduli enough.
- **$v_s$** responds only to the density change, so it is a weak water indicator
  and a strong lithology-and-porosity indicator.
- **Density** responds to the mass of water present, so gravity sees saturated
  *mass*, not saturation.

Every section below derives one link in that chain and then measures how
ambiguous the link is. The lesson is deliberately written so that the
non-uniqueness arrives with the physics rather than as a caveat at the end.

## 2. Precise definitions

### 2.1 Porosity and saturation

**Porosity** $\phi$ is the connected void fraction available to fluid:
$\phi = V_{\text{pore}}/V_{\text{total}}$ (dimensionless, or %). **Water
saturation** $S_w = V_{\text{water}}/V_{\text{pore}}$ is the fraction of the pore
space filled with water, so $1 - S_w$ is the air (or hydrocarbon) fraction. The
**volumetric water content** is the product $\theta = \phi S_w$, and it is
$\theta$ — not $\phi$ and not $S_w$ alone — that many measurements respond to.

The **water table** is the level at which pore pressure equals atmospheric
pressure and below which $S_w$ is effectively 1 (the capillary fringe aside). It
is a *surface of constant saturation state*, not a lithological boundary, which
is why it can appear on a seismic section and be absent from a resistivity
section.

### 2.2 Bulk conductivity and Archie's law

For a clean (clay-free) water-saturated sand, Archie's empirical relation is

$$ \sigma_b = \frac{1}{a}\,\sigma_w\,\phi^{m}\,S_w^{n}, $$

with $\sigma_b$ the bulk conductivity and $\sigma_w$ the pore-water
conductivity, both in $\mathrm{S\,m^{-1}}$. The exponents $a$, $m$ (cementation)
and $n$ (saturation) are *empirical fits*, not constants: this lesson takes
$a = 1$, $m = 2$, $n = 2$ as stated teaching values. In clay-bearing rock a
parallel conduction path through the clay surface adds a term that is nearly
independent of $\sigma_w$, which is exactly why a clay-rich fresh aquifer and a
clean saline aquifer can look the same.

### 2.3 Acoustic properties: Gassmann fluid substitution

The saturated bulk modulus $K_{\text{sat}}$ of a rock with dry-frame modulus
$K_{\text{dry}}$, mineral modulus $K_{\text{min}}$, porosity $\phi$ and fluid
modulus $K_{\text{fl}}$ is

$$ K_{\text{sat}} = K_{\text{dry}} + \frac{(1 - K_{\text{dry}}/K_{\text{min}})^2}
{\dfrac{\phi}{K_{\text{fl}}} + \dfrac{1-\phi}{K_{\text{min}}} - \dfrac{K_{\text{dry}}}{K_{\text{min}}^2}}. $$

The **shear modulus is unchanged** by the pore fluid ($\mu_{\text{sat}} =
\mu_{\text{dry}}$), because a fluid at rest cannot support shear. The bulk
density is $\rho = (1-\phi)\rho_{\text{min}} + \phi \rho_{\text{fl}}$, and the
speeds are $v_p = \sqrt{(K + \tfrac{4}{3}\mu)/\rho}$ and
$v_s = \sqrt{\mu/\rho}$.

Replacing air ($K_{\text{air}} \approx 10^{5}\ \mathrm{Pa}$) with water
($K_{\text{water}} = 2.2\ \mathrm{GPa}$) raises $K$ by four orders of magnitude
in the fluid term, so $K_{\text{sat}}$ rises substantially while $\mu$ does not.
That asymmetry is the whole basis of using $v_p$ as a saturation indicator.

### 2.4 Density

Saturation adds the mass of water and removes the mass of air:
$\Delta\rho = \phi(\rho_w - \rho_{\text{air}})$. With $\rho_w \approx 1000\
\mathrm{kg\,m^{-3}}$ and $\rho_{\text{air}} \approx 1.2\
\mathrm{kg\,m^{-3}}$ this is $\Delta\rho \approx \phi \times 10^{3}\
\mathrm{kg\,m^{-3}}$ — a large change for a porous rock, and the one the
gravimeter weighs.

## 3. Derivations

### 3.1 The Ghyben-Herzberg relation

Consider a coastal aquifer with fresh water of density $\rho_f$ sitting above
saline water of density $\rho_s > \rho_f$, with a *sharp* interface. Let $h$ be
the fresh-water head **above sea level** and $z$ the interface depth **below sea
level**. At the interface, hydrostatic equilibrium requires equal pressure from
both sides along a connected path to the sea:

$$ \rho_f g (h + z) = \rho_s g z
\quad\Longrightarrow\quad
\boxed{\;z = h\,\frac{\rho_f}{\rho_s - \rho_f}\;}. $$

For sea water with $\rho_f = 1000$ and $\rho_s = 1025\ \mathrm{kg\,m^{-3}}$ the
ratio is exactly $1000/25 = 40$: every metre of fresh-water head holds 40 m of
fresh water below sea level. The demonstration prints 41.0 for a rounded
$\rho_s = 1025$ and 101 for a brackish $\rho_s = 1010$ (teaching values), because
the ratio is $(\rho_s/\rho_f)/(\rho_s/\rho_f - 1)$ and is *very* sensitive to a
small density contrast: halving the contrast doubles the ratio.

Two consequences follow, and both are honest rather than convenient:

- The relation is a **sharp-interface** idealisation. Real interfaces are
  transition zones tens of metres wide because dispersion mixes the water.
- Because $z/h$ is large, a small head measurement error is multiplied. A
  $0.1\ \mathrm{m}$ head error is a $4\ \mathrm{m}$ interface error at the sea
  water ratio. The relation does not need a geophysical survey at all; a
  piezometer plus a density estimate does the work. The geophysical survey's
  job is to find where the *interface actually is*, including where the
  sharp-interface model fails.

### 3.2 Archie's law and the ambiguity of one conductivity

Solve Archie for the pore-water conductivity needed to explain a measured bulk
value:

$$ \sigma_w = \frac{\sigma_b}{\phi^{m} S_w^{n}}. $$

Because $\phi$ and $S_w$ enter as powers, one measurement of $\sigma_b$
constrains only the *product* $\phi^{m}S_w^{n}\sigma_w$. With the teaching
exponents $m = n = 2$ and a target $\sigma_b = 0.05\ \mathrm{S\,m^{-1}}$:

| Hypothesised water | $\sigma_w$ (S/m) | Required $\phi$ at $S_w = 1$ |
|---|---|---|
| brackish | 0.5 | 0.316 |
| saline | 4.0 | 0.112 |
| saline, half-saturated ($S_w = 0.5$) | 4.0 | 0.224 |

All three are plausible aquifers. The first is a brackish aquifer of normal
porosity; the second is a saline aquifer with low porosity; the third is a
partially saturated saline aquifer. **The three rows cannot be separated by any
amount of conductivity data at that one location**, because Archie's law is a
single equation in three unknowns. Separation requires an independent
constraint: a water sample, a porosity log, or a second method that responds to
$\phi$ without responding to $\sigma_w$ (for example seismic $v_p$).

### 3.3 Gassmann fluid substitution and the $v_p$/$v_s$ asymmetry

With the demonstration's synthetic frame ($K_{\text{dry}} = 1.0\
\mathrm{GPa}$, $\mu_{\text{dry}} = 3.0\ \mathrm{GPa}$, $\phi = 0.30$,
$K_{\text{min}} = 37\ \mathrm{GPa}$), the Gassmann formula gives:

$$ K_{\text{sat}}^{\text{air}} = 1.000\ \mathrm{GPa}, \qquad
K_{\text{sat}}^{\text{water}} = 7.125\ \mathrm{GPa}. $$

The fluid term adds about $6.1\ \mathrm{GPa}$ of incompressibility. The measured
result (printed by `code/aquifer_signatures_demo.py`) is

| State | $\rho$ (kg/m³) | $v_p$ (m/s) | $v_s$ (m/s) |
|---|---|---|---|
| unsaturated (pores = air) | 1855.4 | 1642 | 1272 |
| saturated (pores = water) | 2155.0 | 2272 | 1180 |
| change | $+16.1\%$ | $+38.4\%$ | $-7.2\%$ |

The asymmetry is the point. $v_p$ rises by a third because $K$ rises while
$\rho$ rises by only a sixth; $v_s$ *falls* because $\mu$ is unchanged and
$\rho$ increased. So the water table is a strong $v_p$ contrast and a weak (and
opposite-signed) $v_s$ contrast. A method that measures $v_p$ (refraction) can
find the water table; a method that measures $v_s$ (surface waves) largely
cannot, and will instead map the porosity and lithology change that often
coincides with it.

### 3.4 Gravity effect of a saturated layer

The attraction of an infinite uniform slab of density contrast $\Delta\rho$ and
thickness $h$ is the **Bouguer slab** result

$$ \Delta g = 2\pi G \Delta\rho\,h, $$

with $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$. In survey
units ($\Delta\rho$ in $\mathrm{g\,cm^{-3}}$, $h$ in m, $\Delta g$ in mGal):

$$ 2\pi G = 4.193\times10^{-10}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}
\;\Longrightarrow\;
\Delta g\ [\mathrm{mGal}] = 0.04194\,\Delta\rho\,h. $$

With $\Delta\rho = \phi(\rho_w - \rho_{\text{air}}) = 0.2996\
\mathrm{g\,cm^{-3}}$ for $\phi = 0.30$:

| Saturated thickness (m) | $\Delta g$ (mGal) |
|---|---|
| 5 | 0.063 |
| 20 | 0.251 |
| 100 | 1.257 |

These are large by microgravity standards — a $5\ \mu\mathrm{Gal}$ ($= 0.005\
\mathrm{mGal}$) survey noise is exceeded once the saturated thickness is about
$0.4\ \mathrm{m}$. The catch is what the number means: the slab formula depends
on the *product* $\phi h$ (mass per unit area), not on $\phi$ or $h$ separately.
A 20 m fully saturated layer and a 40 m half-saturated layer are identical to
the gravimeter. Gravity measures saturated mass; it does not locate a water
table.

## 4. What each method sees

| Method | Physical property | What it responds to | What it cannot separate |
|---|---|---|---|
| ERT / DC resistivity | $\sigma_b$ | salinity $\times$ porosity $\times$ saturation, plus clay | salinity from porosity from clay |
| FDEM / TDEM | $\sigma_b$ (inductive) | same, with a depth weighting | thickness from conductivity (conductance equivalence) |
| Seismic refraction ($v_p$) | $K$, $\mu$, $\rho$ | pore-fluid modulus via Gassmann | saturation from lithology without calibration |
| Surface waves / MASW ($v_s$) | $\mu$, $\rho$ | porosity, cementation, stress | water content (nearly blind to it) |
| Gravity | $\rho$ | saturated mass per area | thickness from porosity |
| Magnetics | not sensitive to water | — | — |

The last row is worth stating explicitly: **there is no magnetic signature of
water**, only of magnetite, so magnetics in a groundwater survey either maps
the geology that controls the aquifer or does nothing.

## 5. Worked examples

### Example 1 — interface depth and its sensitivity

A coastal borehole shows $1.2\ \mathrm{m}$ of fresh-water head above sea level.
Take $\rho_f = 1000$, $\rho_s = 1025\ \mathrm{kg\,m^{-3}}$.

$$ z = 1.2 \times \frac{1000}{25} = 48\ \mathrm{m}. $$

Now suppose the salinity is lower than sea water, $\rho_s = 1010$:

$$ z = 1.2 \times \frac{1000}{10} = 120\ \mathrm{m}. $$

A $1.5\%$ change in the assumed density more than doubles the predicted interface
depth. The demonstration prints the same effect as $z/h_f = 41$ versus $101$.
The lesson: **quote the density you assumed**, because the interface depth is a
*divided* difference of two nearly equal numbers and is therefore ill-conditioned.

### Example 2 — how many aquifers does one conductivity allow?

A single ERT sounding reads $\sigma_b = 0.05\ \mathrm{S\,m^{-1}}$
($20\ \Omega\,\mathrm{m}$). Using $m = n = 2$:

- brackish water, $\sigma_w = 0.5\ \mathrm{S\,m^{-1}}$, requires
  $\phi = \sqrt{0.05/0.5} = 0.316$;
- saline water, $\sigma_w = 4.0\ \mathrm{S\,m^{-1}}$, requires
  $\phi = \sqrt{0.05/4.0} = 0.112$;
- saline water at $S_w = 0.5$ requires $\phi = \sqrt{0.05/(4.0 \times 0.25)}
  = 0.224$.

If a porosity log later shows $\phi = 0.32$, the salinity is brackish. Without
the log, the interpretation is a *family*, and the report must say so.

### Example 3 — a water-table refraction, and a case where there is none

From the synthetic Gassmann model, unsaturated $v_p = 1642\
\mathrm{m\,s^{-1}}$ and saturated $v_p = 2272\ \mathrm{m\,s^{-1}}$, a contrast of
$1.384$. The critical angle is

$$ \theta_c = \arcsin\!\left(\frac{v_1}{v_2}\right)
= \arcsin(0.7226) = 46.3^\circ, \qquad \cos\theta_c = 0.691. $$

For a two-layer head-wave survey the crossover distance is

$$ x_c = 2z\sqrt{\frac{v_2 + v_1}{v_2 - v_1}}, $$

so a water table at $5\ \mathrm{m}$ gives $x_c = 24.9\ \mathrm{m}$, and at
$10\ \mathrm{m}$ it gives $49.8\ \mathrm{m}$ (printed by the seismic demo). If
the unsaturated and saturated velocities were equal, no head wave would exist at
any offset, and the water table would be seismically invisible however well it
is picked.

## 6. Assumptions and regime of validity

1. **Archie's law** requires a clay-free, fairly clean granular rock. With clay,
   the conductivity contains a surface-conduction term nearly independent of
   salinity, the $m$ exponent is not a rock property, and the ambiguity widens.
2. **Gassmann** assumes a homogeneous, isotropic, monomineralic frame, low
   frequency (pore pressure equilibrated), and a single pore fluid. At seismic
   frequencies in a soft, high-permeability sand the dispersion between the
   Gassmann (low-frequency) and Biot-Gassmann-Hill (high-frequency) limits can
   matter; the dry-frame moduli must be measured or modelled, not guessed.
3. **The Ghyben-Herzberg relation** assumes a sharp interface, hydrostatic
   conditions, and a steady state. A pumping well changes all three, and the
   interface rises (up-coning) as the head falls.
4. **The Bouguer slab** assumes an infinite, uniform, flat layer. Finite extent,
   terrain and deeper structures contaminate the residual, and the *difference*
   between two saturation states is what the method actually needs.
5. **Sharp-interface elastic models** ignore the capillary transition zone,
   which for a fine sand can be several metres thick and grade the $v_p$
   contrast.

A number computed in this lesson is valid only inside these assumptions; outside
them it is an order-of-magnitude estimate at best.

## 7. Python demonstration

`code/aquifer_signatures_demo.py` is print-only and computes all of the numbers
quoted above:

1. the Ghyben-Herzberg ratio and interface depth for two density contrasts;
2. the Archie table and the three-way ambiguity at $\sigma_b = 0.05\
   \mathrm{S\,m^{-1}}$;
3. Gassmann fluid substitution and the $v_p$/$v_s$ asymmetry;
4. the Bouguer slab and the detection limit of a microgravity survey.

Run it with:

```bash
cd 11-exploration-geophysics/05-groundwater-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_signatures_demo.py
```

The exercises extend each section; the worked answers are in
[`exercises/01-aquifer-signatures-solutions.md`](./exercises/01-aquifer-signatures-solutions.md).

## Common pitfalls

1. **Reading a conductive anomaly as saline water.** Clay, sulphide and
   mineralised rock all lower resistivity; in a catchment survey the base of the
   weathered zone is often the conductive feature.
2. **Quoting an interface depth without the density contrast.** The
   Ghyben-Herzberg ratio is a divided difference and is ill-conditioned; the
   assumed salinity is part of the answer.
3. **Treating the water table as a reflector for $v_s$.** $v_s$ barely changes
   at saturation; a surface-wave "water table" is usually a lithological or
   porosity boundary that happens to coincide with it.
4. **Forgetting that gravity weighs mass.** A thick unsaturated layer and a thin
   saturated one produce the same anomaly.
5. **Using $m$ or $n$ as universal constants.** They are site-fitted. Quote the
   values you used, as this lesson does.

## Mastery checkpoint

Complete this without notes:

> A coastal survey finds a fresh-water head of $1.0\ \mathrm{m}$ above sea level,
> a bulk conductivity of $0.02\ \mathrm{S\,m^{-1}}$ in the saturated zone, and a
> refraction velocity of $2270\ \mathrm{m\,s^{-1}}$ below a $6\ \mathrm{m}$
> water table over $1640\ \mathrm{m\,s^{-1}}$ above it. **(a)** Compute the
> sharp-interface depth for $\rho_s = 1025\ \mathrm{kg\,m^{-3}}$ and give one
> reason it is a lower bound on the *toe* of a real transition zone. **(b)** With
> $m = n = 2$, list two (salinity, porosity) combinations that explain the
> conductivity. **(c)** Compute the crossover distance of the water-table head
> wave. **(d)** State the single additional measurement that would most reduce
> the ambiguity in (b), and justify it in one sentence.

A worked version of (a)-(c) is in the lesson-05-01
[solutions](./exercises/01-aquifer-signatures-solutions.md).

## Related modules

- [11-05-02 EM and ERT for Groundwater Mapping](./02-em-and-ert-groundwater.md) —
  the two methods that measure the conductivity discussed here.
- [11-05-03 Seismic Refraction and Surface Waves for Aquifers](./03-seismic-groundwater.md) —
  the $v_p$/$v_s$ contrast used in Section 3.3.
- [11-05-04 Airborne EM for Regional Aquifer Mapping](./04-airborne-groundwater.md) —
  the same conductivity at regional scale, and its ambiguity.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) — the
  full theory of the electrical methods.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  groundwater as a physical and management problem.
- [05-core-geophysics](../../05-core-geophysics/README.md) — property contrasts
  and rock physics.

## Self-assessment checklist

- [ ] I can derive $z = h\rho_f/(\rho_s-\rho_f)$ from hydrostatic equilibrium.
- [ ] I can explain the three-way Archie ambiguity with an equation.
- [ ] I can compute $v_p$ and $v_s$ on both sides of a water table.
- [ ] I can state which method sees saturation and which sees mass.
- [ ] I can compute a Bouguer slab anomaly and its detection limit.
- [ ] I can quote the assumptions of each relation without notes.
