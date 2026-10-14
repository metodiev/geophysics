---
id: 13-03-02
title: "Rifting, Break-Up and Passive Margin Formation"
level: doctoral
prereqs: ["13-01-02", "13-06-01", "04-02-02"]
tags: [geodynamics, tectonophysics, rifting, passive-margins, subsidence, isostasy, heat-conduction]
---

# Rifting, Break-Up and Passive Margin Formation

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the stretching factor $\beta$ and **derive** the kinematics of
   uniform (pure shear) extension, including the relation
   $\beta = e^{\dot\varepsilon t}$.
2. **Derive** the water-loaded subsidence of a stretched lithospheric column
   from isostasy, and **show** that for uniform stretching the whole pre-rift
   density deficit is divided by $\beta$ at the moment stretching stops.
3. **Derive** the post-rift subsidence from the heat equation, **obtain** the
   decay constant $\tau = a^{2}/(\pi^{2}\kappa)$, and **measure** how well a
   single exponential describes the real curve.
4. **Quantify** the sensitivity of total subsidence to $\beta$ and **explain**
   why it saturates.
5. **Distinguish** which features of a margin record the stretching factor,
   which record the rift duration, and which record neither.
6. **State** the assumptions of the uniform-stretching model and **identify**
   the observations (non-uniform thinning, magmatism, syn-rift structure) that
   violate them.

## Prerequisites

- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  what a lithosphere can and cannot do when pulled.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the isostatic machinery used here.
- [04-02-02 Plate Boundaries](../../04-earth-science-geology/02-plate-tectonics/02-plate-boundaries.md) —
  where rifts sit in the plate-tectonic framework.

All models and data in this module are **SYNTHETIC**. The numbers below are
model outputs from `code/rift_and_breakup_demo.py` for a chosen teaching
lithosphere; they are not measurements of any margin. The exact constants used
are standard gravity $g = 9.81\ \mathrm{m\,s^{-2}}$ and the conversion
$1\ \mathrm{Myr} = 3.1558\times10^{13}\ \mathrm{s}$.

## 1. The stretching factor and what it does to a column

Uniform (pure shear) extension assumes that every horizontal element of the
lithosphere is extended by the same factor $\beta = L_{\text{final}}/L_{0}$, and
that material moves only within the vertical plane of section, so volume is
conserved by **vertical thinning**:

$$
t_c = \frac{t_{c0}}{\beta}, \qquad a = \frac{a_0}{\beta},
$$

for the crustal thickness $t_c$ and the whole lithospheric thickness $a$.

If the extension is at a constant strain rate $\dot\varepsilon$ for a time $t$,
then $\beta = e^{\dot\varepsilon t}$ and the natural strain is
$\ln\beta$; the engineering extension is $(\beta-1)$, which is the number
usually quoted as a percentage. The two differ: at $\beta = 2$ the extension is
$100\%$ but the natural strain is $0.693$. Confusing them is a factor-of-two
error in any strain-rate calculation, so state which one you mean.

The teaching lithosphere in this lesson is

$$
a = 125\ \mathrm{km},\quad t_{c0} = 35\ \mathrm{km},\quad
T_m = 1300\ ^\circ\mathrm{C},\quad \alpha = 3\times10^{-5}\ \mathrm{K^{-1}},
$$
$$
\rho_m = 3330,\quad \rho_c = 2800,\quad \rho_w = 1030\
\mathrm{kg\,m^{-3}},\quad \kappa = 1\times10^{-6}\ \mathrm{m^{2}\,s^{-1}} .
$$

$\kappa$ is converted once and for all:

$$
\kappa = 1\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}
\times \frac{3.1558\times10^{13}\ \mathrm{s\,Myr^{-1}}}{10^{6}\
\mathrm{m^{2}\,km^{-2}}}
= 31.558\ \mathrm{km^{2}\,Myr^{-1}} .
$$

## 2. Isostasy of a stretched column

Define the **density deficit** of a column, per unit area, relative to pure
asthenosphere:

$$
\Phi \equiv \int_0^{a}\bigl[\rho(z) - \rho_m\bigr]\,\mathrm dz
\qquad (\mathrm{kg\,m^{-2}}),
$$

with $\rho(z) = \rho_c$ in the crust and
$\rho(z) = \rho_m\left[1 + \alpha(T_m - T(z))\right]$ in the mantle
lithosphere, so that cold mantle is denser than asthenosphere. Requiring equal
pressure at the depth of the base of the lithosphere, and filling any gap with
water, gives the water-loaded subsidence relative to the pre-rift column:

$$
S = \frac{\Phi_{\text{stretched}} - \Phi_{\text{reference}}}{\rho_m - \rho_w}
\qquad (\mathrm{km\ of\ water}) .
$$

**At the instant stretching stops**, uniform thinning divides every part of the
deficit by $\beta$:

$$
\Phi_{\text{stretched}}(0) = \frac{\Phi_{\text{reference}}}{\beta}
\qquad\text{(exact for uniform thinning)} ,
$$

because both the crustal term $(\rho_c-\rho_m)t_{c0}$ and the mantle term
$\rho_m\alpha T_m (a-t_{c0})^{2}/(2a)$ carry the same factor $1/\beta$. Hence

$$
\boxed{\;S(0) = \left(1 - \frac{1}{\beta}\right)\bigl(A - B\bigr)\;}
$$

$$
A = \frac{(\rho_m - \rho_c)t_{c0}}{\rho_m - \rho_w}, \qquad
B = \frac{\rho_m\alpha T_m (a - t_{c0})^{2}}{2a\,(\rho_m - \rho_w)} .
$$

For the teaching lithosphere, $A = 8.065\ \mathrm{km}$ and
$B = 1.829\ \mathrm{km}$, so $A - B = 6.236\ \mathrm{km}$. The two terms have
clear physical identities: $A$ is what the thinned crust alone would produce,
$B$ is the contribution of the cold pre-rift mantle lithosphere, which the
freshly stretched column does not yet have. Both scale with $(1-1/\beta)$,
which is why the initial subsidence is a remarkably clean function of $\beta$.

### 2.1 Worked example at $\beta = 2$

1. Thinning: $t_c = 17.50\ \mathrm{km}$, $a = 62.50\ \mathrm{km}$.
2. $S(0) = (1 - 0.5)(8.065 - 1.829) = 0.5\times6.236 =
   3.118\ \mathrm{km}$.
3. The demonstration's finite-difference isostasy integral gives
   $S(0) = 3.118\ \mathrm{km}$, a difference of $0.0\ \mathrm{m}$.
4. At equilibrium (infinite cooling time) the closed form gives
   $S(\infty) = 4.813\ \mathrm{km}$, so the thermal part adds
   $1.695\ \mathrm{km}$.

The agreement in step 3 is not automatic: with a coarse grid it fails by
hundreds of metres. Using $\mathrm dz = 0.5\ \mathrm{km}$ places both $t_{c0}$
and $a/\beta$ exactly on nodes; with $\mathrm dz = 1.0\ \mathrm{km}$ the same
calculation was short by $\sim 135\ \mathrm{m}$ at $t=0$, because the crust was
rounded to $17\ \mathrm{km}$ instead of $17.5\ \mathrm{km}$. That is a
discretisation error masquerading as a physical result, and the only way to see
it is to compare against a closed form.

## 3. Post-rift cooling and the decay constant

After stretching stops, the column cools. With a fixed surface temperature
$T(0,t) = 0$ and $T(a,t) = T_m$, the heat equation
$T_t = \kappa T_{zz}$ has eigenmodes $\sin(n\pi z/a)$ decaying as
$\exp(-n^{2}\pi^{2}\kappa t/a^{2})$. The slowest surviving mode sets

$$
\boxed{\;\tau = \frac{a^{2}}{\pi^{2}\kappa}\;}
$$

For the teaching lithosphere $\tau = 125^{2}/(\pi^{2}\times31.558) =
50.17\ \mathrm{Myr}$.

The demonstration solves the heat equation on a $251$-node grid with
$\mathrm dz = 0.5\ \mathrm{km}$, $\mathrm dt = 0.0025\ \mathrm{Myr}$ and
explicit-scheme parameter
$r = \kappa\,\mathrm dt/\mathrm dz^{2} = 0.316$ (stable, since $r \le 0.5$).
It then integrates the isostasy relation at each time. The SYNTHETIC $\beta=2$
column subsides as

| $t$ (Myr) | 0 | 5 | 10 | 25 | 50 | 100 | 200 |
|---|---|---|---|---|---|---|---|
| $S$ (km) | 3.118 | 3.260 | 3.399 | 3.759 | 4.172 | 4.575 | 4.779 |
| rate ($\mathrm{mm\,yr^{-1}}$) | — | 28.5 | 27.8 | 24.0 | 16.5 | 8.1 | 2.0 |

Total post-rift subsidence to $200\ \mathrm{Myr}$: $1.661\ \mathrm{km}$.

### 3.1 Is a single exponential enough?

Fitting $S(t) = S_0 + S_{th}\left[1 - e^{-t/\tau}\right]$ to the whole curve
gives

$$
S_0 = 3.107\ \mathrm{km},\quad S_{th} = 1.712\ \mathrm{km},\quad
\tau_{\text{fit}} = 51.77\ \mathrm{Myr} ,
$$

which is $+3.2\%$ against $\tau = 50.17\ \mathrm{Myr}$, with an rms residual of
$6.30\ \mathrm{m}$ ($\max 10.7\ \mathrm{m}$). Refitting only after $25\
\mathrm{Myr}$ — by which time the higher modes have decayed — gives
$\tau = 50.20\ \mathrm{Myr}$, $+0.1\%$.

The lesson is quantitative and general: a single exponential is a *good but not
exact* description, and the bias is largest when the fit includes the earliest
times, because the initial condition is a piecewise-linear geotherm with a kink,
not the first eigenmode. The bias is in the direction that matters for
interpretation — a shorter apparent $\tau$ means an inferred viscosity that is
too low, or a lithosphere that is too thin. If a study fits a single exponential
from $t=0$, its $\tau$ should not be compared with $a^{2}/(\pi^{2}\kappa)$ at
better than a few per cent.

## 4. How much does $\beta$ matter?

Using the closed forms (which the demonstration verifies against the numerical
solution):

| $\beta$ | crust (km) | $S(0)$ (km) | $S(\infty)$ (km) | thermal part (km) |
|---|---|---|---|---|
| 1.00 | 35.00 | 0.000 | 0.000 | 0.000 |
| 1.25 | 28.00 | 1.247 | 1.909 | 0.662 |
| 1.50 | 23.33 | 2.079 | 3.193 | 1.115 |
| 2.00 | 17.50 | 3.118 | 4.813 | 1.695 |
| 3.00 | 11.67 | 4.157 | 6.448 | 2.291 |
| 5.00 | 7.00 | 4.989 | 7.768 | 2.779 |
| 10.00 | 3.50 | 5.612 | 8.763 | 3.151 |

Both terms saturate. The crustal term is proportional to $(1-1/\beta)$, which
approaches $1$ quickly; the thermal term grows as the thinned lithosphere's heat
content changes, which also saturates because a thinner lithosphere has less
material to cool. The observable consequence is a **strongly non-linear**
inverse problem: from $S(0)$ alone, subsidence of $3\ \mathrm{km}$ implies
$\beta \approx 1.9$, while $4\ \mathrm{km}$ implies $\beta \approx 2.7$. Depth
errors of a few hundred metres move $\beta$ by tens of per cent.

### 4.1 Strain rate, rift duration and what the record cannot tell you

Writing $\beta = e^{\dot\varepsilon t}$ gives the strain rate implied by a rift
of a given duration:

| $\beta$ | duration (Myr) | $\dot\varepsilon$ ($\mathrm{Myr^{-1}}$) | (nanostrain/yr) |
|---|---|---|---|
| 1.5 | 30 | 0.0135 | 13.5 |
| 2.0 | 20 | 0.0347 | 34.7 |
| 2.0 | 5 | 0.1386 | 138.6 |
| 3.0 | 10 | 0.1099 | 109.9 |

The unit conversion is exact: $10^{-6}\ \mathrm{Myr^{-1}} = 10^{-6}/10^{6}\
\mathrm{yr^{-1}} = 10^{-12}\ \mathrm{yr^{-1}} = 1$ nanostrain per year.

The same final geometry therefore corresponds to strain rates that differ by an
order of magnitude depending on how long rifting took. Since the thermal
subsidence depends on $\beta$ and on $\tau$ (fixed by $\kappa$ and $a$), and
**not** on the rift duration in this model, the post-rift subsidence curve
cannot recover the strain rate. That information lives in the syn-rift record:
fault growth, syn-rift sediment thickness and thermochronology.

## 5. Assumptions and regime of validity

1. **Instantaneous stretching.** The model has one $\beta$ and one rifting
   instant. A rift lasting $\gtrsim 20\ \mathrm{Myr}$ cools and subsides as it
   stretches, smearing the syn-rift and post-rift signals. Two-stage and
   depth-dependent stretching models exist precisely for this.
2. **Uniform thinning in depth.** Every layer is thinned by $\beta$. Real rifts
   show depth-dependent stretching: the upper crust may extend on faults by
   $\beta_f = 1.3$ while the lithospheric mantle thins by $\beta_m = 2$. When
   $\beta_f \neq \beta_m$, the clean result
   $\Phi_{\text{stretched}}(0) = \Phi_{\text{reference}}/\beta$ fails and the
   initial subsidence must be computed layer by layer.
3. **Local (Airy) isostasy.** Flexural strength suppresses short-wavelength
   compensation and changes the shape of the margin. Both this model and the
   flexural alternative must be tested against gravity and topography
   ([13-06-01](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md)).
4. **A uniform, temperature-independent thermal expansion coefficient** and
   temperature-independent mantle density. Real $\alpha$ falls with temperature;
   the effect on the thermal subsidence amplitude is of order the variation of
   $\alpha$.
5. **No magmatism, no phase changes, no crustal flow.** Volcanic margins add
   igneous material, which adds mass and reduces subsidence; serpentinisation
   and eclogitisation change density at depth.
6. **Constant $\kappa$ and no radiogenic heating.** Heat production in the crust
   perturbs the geotherm and hence $B$.
7. **Water loading.** The water-loaded convention assumes the basin fills to sea
   level. Sediment loading (denser than water) produces more total subsidence,
   which is exactly what backstripping undoes
   ([13-03-04](04-basin-geodynamics.md)).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC margin has a crustal thickness of $17.5\ \mathrm{km}$ interpreted
> as uniform stretching of a $35\ \mathrm{km}$ crust, and a rifted
> lithosphere of $125\ \mathrm{km}$. **(a)** Compute $\beta$ and the water-loaded
> initial subsidence with $A = 8.065\ \mathrm{km}$, $B = 1.829\ \mathrm{km}$.
> **(b)** Compute $\tau$ for $a = 125\ \mathrm{km}$ and
> $\kappa = 31.558\ \mathrm{km^{2}\,Myr^{-1}}$ and state how much of the
> equilibrium thermal subsidence remains after $50\ \mathrm{Myr}$.
> **(c)** The interpreted crustal thickness is revised to $21\ \mathrm{km}$.
> Recompute $\beta$ and $S(0)$ and state the percentage change in $\beta$ and in
> $S(0)$. **(d)** A colleague quotes $\dot\varepsilon = 35$ nanostrain per year
> for $\beta = 2$. What rift duration have they assumed, and why can the
> post-rift subsidence curve not check it?

## Common pitfalls

1. **Reading $\beta$ off a subsidence that is not water-loaded.** Sediment
   loading dominates; backstrip first.
2. **Confusing extension $(\beta-1)$ with strain $\ln\beta$.** At $\beta = 2$
   that is a factor $1.44$.
3. **Fitting a single exponential from $t = 0$ and comparing $\tau$ with
   $a^{2}/(\pi^{2}\kappa)$.** The demonstration measures a $+3.2\%$ bias, which
   is one order of magnitude larger than the internal precision of the data.
4. **Assuming $\beta_f = \beta_m$ because the model does.** Depth-dependent
   stretching is the rule, not the exception, and it is detectable in the
   mismatch between observed and predicted initial subsidence.
5. **Ignoring the grid.** A $1\ \mathrm{km}$ grid gave $\sim 135\ \mathrm{m}$ of
   spurious initial subsidence; always check an integral against a closed form.
6. **Treating the subsidence rate as constant.** It falls from
   $28.5\ \mathrm{mm\,yr^{-1}}$ at $5\ \mathrm{Myr}$ to
   $2.0\ \mathrm{mm\,yr^{-1}}$ at $200\ \mathrm{Myr}$: accommodation space is
   created fastest immediately after break-up.

## Related modules

- [13-03-04 Basin Formation and Subsidence Modelling](04-basin-geodynamics.md) —
  what happens when the water is replaced by sediment.
- [13-06-03 Glacial Isostatic Adjustment](../06-crustal-and-lithospheric-dynamics/03-glacial-isostatic-adjustment.md) —
  the same isostasy and relaxation mathematics under an ice load.
- [13-01-03 Lithospheric Strength and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md).
- [13-01-02 Rheology of the Earth](../01-geodynamic-principles/02-rheology-of-earth.md) —
  why a lithosphere can be thinned at all, and at what stress.
- [13-07-01 Erosion, Uplift and Thermochronology](../07-geomorphology-tectonics-climate/01-erosion-and-uplift.md) —
  the record that does constrain rift timing.
- [04-03-04 Sedimentary Basins](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/04-sedimentary-basins.md) —
  the geological description of the same objects.
