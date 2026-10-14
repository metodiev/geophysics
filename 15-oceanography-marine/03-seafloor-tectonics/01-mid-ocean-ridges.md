---
id: 15-03-01
title: "Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems"
level: doctoral
prereqs: ["15-01-01", "15-02-01", "15-02-05", "13-03-01"]
tags: [oceanography, marine-geophysics, seafloor-tectonics, mid-ocean-ridges, hydrothermal-circulation, heat-flow]
---

# Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems

> **All models and data in this module are SYNTHETIC.** The ridge, the crust and
> the fluid circulation described here are teaching models built from the stated
> standard material constants. No real ridge segment, vent field, cruise or
> station is used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the half-space-cooling subsidence law $d(t)=d_r+a\sqrt{t}$ from
   isostatic thermal contraction, and **compute** the coefficient
   $a=373.2\ \mathrm{m\,(Myr)^{-1/2}}$ from stated mantle constants.
2. **Predict** surface heat flow $q(t)$ versus age and **explain**, with numbers,
   why the observed young-crust heat flow falls far below the prediction.
3. **Compute** the Rayleigh number for porous convection in a permeable crustal
   layer, **find** the critical permeability for onset, and **state** the regime.
4. **Convert** a heat-flow deficit into the volume flux of hydrothermal fluid
   required to remove it, and **state** the assumptions that make the number a
   lower bound.
5. **Quantify** the axial thermal structure from the $\mathrm{erf}$ solution and
   **relate** the depth of the brittle–ductile transition to spreading rate.
6. **Separate** what a ridge observatory measures (depth, heat flow, seismicity,
   vent temperature) from what it models (melt supply, permeability, fluid flux).
7. **State** the non-uniqueness of any fluid-flux estimate derived from a heat
   budget, and **name** the independent measurement that would constrain it.

## Prerequisites

- [15-01-01 Seawater Properties](../01-physical-oceanography/01-seawater-properties.md) —
  the density, heat capacity and thermal expansion of seawater used throughout.
- [15-02-01 Marine Seismic Reflection](../02-marine-geophysics-methods/01-marine-seismic-reflection.md) —
  how the axial magma lens and the crustal layering are imaged.
- [15-02-05 Marine Gravity and Magnetic Surveys](../02-marine-geophysics-methods/05-marine-gravity-magnetics.md) —
  the shipboard measurements that constrain crustal thickness and the magnetic
  timescale.
- [13-03-01 Plate Kinematics Models](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  the spreading rate as a rigid-plate quantity.

## 1. Intuition: the ridge is a heat engine that has been running for 180 Myr

A mid-ocean ridge is the surface expression of two coupled processes. Cold
mantle rises, decompresses and melts; the melt is extracted, freezes and builds
oceanic crust; the newly formed plate moves away, cools and contracts. The first
process is a problem in petrology. The second is a problem in **heat conduction
with a moving boundary**, and it is the part that marine geophysics measures,
because thermal contraction of the plate makes the seafloor subside and makes it
lose heat at a known, calculable rate.

That calculation has an unusually clean outcome. Isostasy plus heat conduction
predict that depth should grow as the square root of crustal age and that heat
flow should fall as its inverse square root. Both predictions are testable with a
bathymetric map and a heat-flow probe. Both are confirmed in their *shape* over
wide age ranges, and one of them is spectacularly wrong in its *magnitude* on
young crust.

The failure is the interesting part. On crust younger than a few million years,
the measured conductive heat flow is far below the prediction, and the missing
energy reappears as hot springs on the seafloor. The ridge is a heat engine, and
the coolant is seawater circulating through fractured basalt. That circulation is
what this lesson is really about: the temperature of the fluid, the volume flux
required, and the physical property — permeability — that decides whether
circulation happens at all.

**Non-uniqueness appears immediately.** A heat-flow deficit can be explained by
(a) a large volume of cool fluid, (b) a small volume of very hot fluid, (c) a
conductivity structure differing from the assumed value, or (d) a crustal
thickness and lithology differing from the assumed model. The heat budget fixes a
*product*, not the individual factors, and every fluid-flux number below must be
read as conditional on the stated end-member. That is why real estimates of
ridge-axis fluid flux span more than an order of magnitude.

## 2. Precise definitions

**Half-spreading rate** $u$: the speed at which one plate moves away from the
axis, $\mathrm{m\,s^{-1}}$ (usually quoted in $\mathrm{cm\,yr^{-1}}$;
$1\ \mathrm{cm\,yr^{-1}} = 3.1688\times10^{-10}\ \mathrm{m\,s^{-1}}$). The full
rate is $2u$.

**Lithospheric age** $t$: time since the crust left the axis, so $t=x/u$ for
distance $x$ from the axis. This identification is a *model*: it assumes the
axis has stayed put, that spreading was steady, and that there has been no
ridge jump.

**Half-space cooling.** The model treats the asthenosphere as a semi-infinite
solid, initially at $T_m$, whose surface is suddenly held at $0\ ^\circ\mathrm{C}$
(seafloor temperature). The solution of the heat equation is

$$T(z,t)=T_m\,\mathrm{erf}\!\left(\frac{z}{2\sqrt{\kappa t}}\right),$$

with $\kappa$ the thermal diffusivity. The plate is not a half-space at large
$t$ — heat reaches the base and the model over-cools the old plate — so the law
is valid for young to intermediate ages and fails for the oldest seafloor.

**Rayleigh number.** For a permeable layer of thickness $H$ saturated with
water, held between temperatures differing by $\Delta T$, the dimensionless
number governing the onset of convection is

$$\mathrm{Ra}=\frac{\rho_w\,g\,\alpha_w\,\Delta T\,k\,H}{\mu\,\kappa},$$

where $\rho_w$ is fluid density, $\alpha_w$ the fluid's thermal expansion
coefficient, $k$ the **permeability** ($\mathrm{m^2}$, not hydraulic
conductivity), $\mu$ the dynamic viscosity and $\kappa$ the thermal diffusivity
of the rock. For a porous layer with impermeable, isothermal boundaries the
critical value is

$$\mathrm{Ra}_c=4\pi^2=39.478\ \text{(dimensionless)}.$$

**Permeability versus hydraulic conductivity.** $k$ (m²) is a property of the
rock; hydraulic conductivity $K=\rho_w g k/\mu$ (m/s) is a property of rock *and*
fluid, so it changes with temperature. Ridge-crust work is done in $k$ because
the fluid properties vary enormously between $2\ ^\circ\mathrm{C}$ and
$400\ ^\circ\mathrm{C}$.

**Nusselt number.** $\mathrm{Nu}=q_{\text{convective}}/q_{\text{conductive}}$,
the factor by which flow enhances heat transfer. $\mathrm{Nu}=1$ means pure
conduction.

## 3. Derivations

### 3.1 Subsidence from thermal contraction

Let the rock have density $\rho_m$ at temperature $T_m$ above the seafloor
temperature and let it contract linearly with cooling:

$$\rho(T)=\rho_m\left[1-\alpha_v\left(T_m-T\right)\right],$$

with $\alpha_v$ the volumetric thermal expansion coefficient. The column contracts
by

$$\Delta H=\int_0^\infty \alpha_v\left[T_m-T(z,t)\right]\mathrm{d}z .$$

Substituting the $\mathrm{erf}$ solution and using
$\int_0^\infty \mathrm{erfc}(u)\,\mathrm{d}u=1/\sqrt{\pi}$ with
$u=z/(2\sqrt{\kappa t})$:

$$\int_0^\infty\left[T_m-T(z,t)\right]\mathrm{d}z
= T_m\,\frac{2\sqrt{\kappa t}}{\sqrt{\pi}}.$$

Airy isostasy converts the contraction into seafloor depth: the subsidence is the
contraction amplified by the density contrast between mantle and water, that is
by $\rho_m/(\rho_m-\rho_w)$. Therefore

$$\boxed{\;d(t)=d_r+\underbrace{\frac{\rho_m}{\rho_m-\rho_w}\alpha_v T_m
\frac{2\sqrt{\kappa}}{\sqrt{\pi}}}_{a}\sqrt{t}\;}$$

With $\rho_m=3300$, $\rho_w=1030\ \mathrm{kg\,m^{-3}}$,
$\alpha_v=3\times10^{-5}\ \mathrm{K^{-1}}$, $T_m=1350\ \mathrm{K}$ and
$\kappa=10^{-6}\ \mathrm{m^2\,s^{-1}}$:

$$\frac{\rho_m}{\rho_m-\rho_w}=\frac{3300}{2270}=1.45374,\qquad
\alpha_vT_m=4.0500\times10^{-2},$$

$$2\sqrt{\kappa/\pi}=1.12838\times10^{-3}\ \mathrm{m\,s^{-1/2}},$$

$$a=6.64352\times10^{-5}\ \mathrm{m\,s^{-1/2}}
=373.2\ \mathrm{m\,(Myr)^{-1/2}}.$$

The demonstration prints exactly these four lines. Note what has happened: a
coefficient that is usually fitted to bathymetry has been **predicted** from
mantle constants, and it comes out of the right size. That agreement is the
strongest single piece of evidence that plates cool conductively.

### 3.2 Heat flow and the shape of the ridge flank

The surface heat flow follows from the same solution:

$$q(t)=-k\left.\frac{\partial T}{\partial z}\right|_{z=0}
=\frac{k\,T_m}{\sqrt{\pi\kappa t}} .$$

With $k=3.2\ \mathrm{W\,m^{-1}\,K^{-1}}$ and the same constants,
$kT_m=4320$ and $\pi\kappa=3.1416\times10^{-6}$, giving the demonstration's
table: $1372\ \mathrm{mW\,m^{-2}}$ at $0.1\ \mathrm{Ma}$, $433.9$ at $1\ \mathrm{Ma}$,
$137.2$ at $10\ \mathrm{Ma}$, $43.4$ at $100\ \mathrm{Ma}$. The ratio
$q(1)/q(10)=3.162=\sqrt{10}$, the signature of the $\sqrt{t}$ law.

Differentiating the depth law gives the ridge-flank gradient. At $10\ \mathrm{Ma}$
with a half-rate of $5\ \mathrm{cm\,yr^{-1}}$ the demonstration measures
$1.18\ \mathrm{mm\,m^{-1}} = 1.18\ \mathrm{m\,km^{-1}}$, i.e. a slope of about
$0.07^\circ$. Ridge flanks are among the gentlest large slopes on Earth:
subsidence from 1 to 4 Ma is only 373 m, and the average rate over that interval
is $0.12\ \mathrm{mm\,yr^{-1}}$.

### 3.3 The young-crust heat-flow deficit and convection onset

The prediction at $1\ \mathrm{Ma}$ is $433.9\ \mathrm{mW\,m^{-2}}$. The
demonstration's convection model asks whether the crust can carry that heat
advectively. Using $\alpha_w=5\times10^{-4}\ \mathrm{K^{-1}}$ (hot water expands
much more than cold water), $\Delta T=200\ \mathrm{K}$, $\mu=2\times10^{-4}\ \mathrm{Pa\,s}$
and a permeable layer $H=1000\ \mathrm{m}$ thick:

$$\mathrm{Ra}(k=10^{-14}\ \mathrm{m^2})
=\frac{1030\times9.81\times5\times10^{-4}\times200\times10^{-14}\times1000}
{2\times10^{-4}\times10^{-6}}=50.5,$$

which exceeds $\mathrm{Ra}_c=39.478$ by a factor $1.28$, so the layer convects.
At $k=10^{-15}\ \mathrm{m^2}$ the number is $5.1$, i.e. $0.13\,\mathrm{Ra}_c$, and
the layer conducts. The onset permeability solves
$\mathrm{Ra}(k_{\min})=\mathrm{Ra}_c$:

$$k_{\min}=\frac{\mathrm{Ra}_c\,\mu\,\kappa}{\rho_w g\alpha_w\Delta T H}
=\frac{39.478\times2\times10^{-4}\times10^{-6}}
{1030\times9.81\times5\times10^{-4}\times200\times1000}
=7.81\times10^{-15}\ \mathrm{m^2}=7.9\ \mathrm{mD},$$

using the exact conversion $1\ \mathrm{mD}=9.869\times10^{-16}\ \mathrm{m^2}$.

The strength of the conclusion depends on $H$ and $\Delta T$, which are chosen,
not measured: $k_{\min}\propto(H\Delta T)^{-1}$, so doubling either halves the
threshold. The honest statement is therefore: *if* the permeable layer is
kilometres thick and the temperature drop is hundreds of kelvin, *then*
permeabilities of a few millidarcies — routinely measured in fractured basalt —
are enough to convect. The model does not prove that the crust convects; it shows
that it does not need unusual permeability to do so.

Adopting the simple closure $\mathrm{Nu}=\max(1,\mathrm{Ra}/\mathrm{Ra}_c)$ (exact
only near onset, and an underestimate at high $\mathrm{Ra}$), the demonstration
reports $\mathrm{Nu}=1.3$ at $k=10^{-14}\ \mathrm{m^2}$ and $\mathrm{Nu}=12.8$ at
$k=10^{-13}\ \mathrm{m^2}$, on top of a conductive flux of $0.640\ \mathrm{W\,m^{-2}}$.

### 3.4 From a heat deficit to a fluid flux

Integrate the half-space heat flow over the first $t_1$:

$$\int_0^{t_1}\frac{kT_m}{\sqrt{\pi\kappa t}}\,\mathrm{d}t
=\frac{2kT_m\sqrt{t_1}}{\sqrt{\pi\kappa}}
=8.659\times10^{13}\ \mathrm{J\,m^{-2}}$$

for $t_1=10\ \mathrm{Ma}$ (the demonstration's value). If a fraction $f$ of that
energy is carried away by fluid that enters cold and leaves at
$T_{\text{out}}$, then per unit seafloor area the water volume required is

$$V=\frac{f}{(\rho c_p \Delta T)}\int_0^{t_1}q\,\mathrm{d}t,$$

with $\Delta T=T_{\text{out}}-T_{\text{in}}$. With $f=0.30$,
$\rho c_p\Delta T = 1030\times5000\times350 = 1.802\times10^{9}\ \mathrm{J\,m^{-3}}$:

$$V=\frac{0.30\times8.659\times10^{13}}{1.802\times10^{9}}
=1.44\times10^{4}\ \mathrm{m^3\,m^{-2}},$$

that is, a water column of $14\,412\ \mathrm{m}$ passing through every square
metre of crust younger than $10\ \mathrm{Ma}$ in a $100\ \mathrm{km}\times100\
\mathrm{km}$ patch, or $1.441\times10^{14}\ \mathrm{m^3}$ in total. Spread evenly
over the $10\ \mathrm{Myr}$ interval this is an average Darcy flux of
$4.567\times10^{-11}\ \mathrm{m\,s^{-1}} = 1.44\ \mathrm{mm\,yr^{-1}}$, which is
$1.441\times10^{9}\ \mathrm{m^3}$ per metre of ridge line.

**Every factor in $V$ is a choice.** $f=0.30$, $c_p=5000\ \mathrm{J\,kg^{-1}\,K^{-1}}$
and $\Delta T=350\ \mathrm{K}$ are model values; $V\propto f$ and
$V\propto1/\Delta T$. A model that vents $100\ \mathrm{K}$ fluid instead of
$350\ \mathrm{K}$ fluid needs 3.5 times the volume. This is why a fluid-flux
number from a heat budget is a bound, not a measurement, and why the two
independent fluid-flux measurements — a heat-budget inversion and a direct
current-meter or tracer estimate at a vent field — rarely agree to better than a
factor of a few.

### 3.5 Axial thermal structure

The same $\mathrm{erf}$ solution gives the depth to any isotherm. With
$T=600\ ^\circ\mathrm{C}$ and $T_m=1350\ \mathrm{K}$,

$$\mathrm{erf}(u)=\frac{600}{1350}=0.4444 \;\Rightarrow\; u=0.41681,\qquad
z_{600}=2u\sqrt{\kappa t}=0.83362\sqrt{\kappa t}.$$

Using the age-distance identity $t=x/u_{\text{half}}$:

| half-rate (cm/yr) | $z_{600}$ at 2 km | at 5 km | at 10 km |
|---|---|---|---|
| 1 | 2094 m | 3311 m | 4683 m |
| 5 | 937 m | 1481 m | 2094 m |
| 10 | 662 m | 1047 m | 1481 m |

These are the demonstration's values. The depth grows as $\sqrt{x/u}$, so a slow
ridge buries its brittle–ductile transition several kilometres deep within 10 km
of the axis while a fast ridge keeps it near 1 km. This is the standard
explanation for the first-order correlation between spreading rate and axial
morphology: fast axes are hot, weak and stand as axial highs; slow axes are cold,
strong and sit in rifted valleys. The model ignores the latent heat of the axial
magma body and the hydrothermal heat loss, both of which *shallower* the real
isotherms.

## 4. Physical interpretation

- **Subsidence is a thermometer.** The $373.2\ \mathrm{m\,(Myr)^{-1/2}}$
  coefficient is a prediction from $\alpha_v$, $T_m$ and $\kappa$, not a fit. A
  measured coefficient that differs from it by much means one of those constants
  is wrong, or that the depth is being influenced by something else — a mantle
  temperature anomaly, a sediment load, or dynamic topography.
- **The heat flow disagrees with the model where it matters most.** The
  half-space prediction at 100 Ma ($43.4\ \mathrm{mW\,m^{-2}}$) is close to what
  is measured on old crust, while at 1 Ma ($433.9\ \mathrm{mW\,m^{-2}}$) it is far
  above it. The large young-crust discrepancy and the small old-crust
  discrepancy are both explained by the same process: seawater removes heat from
  young, permeable crust, and the permeability is sealed by hydrothermal
  alteration within a few million years.
- **Convection is not a switch.** $\mathrm{Ra}$ is a smooth function of $k$, $H$
  and $\Delta T$, and the crust is heterogeneous. The homogeneous-layer
  calculation gives an onset threshold; the real crust has convection in some
  places and conduction in others, and the transition is spatially patchy.
- **The lesson is about the exponent, not the constant.** $\sqrt{t}$ behaviour
  is robust, because it follows from diffusion. The amplitude is where the
  assumptions live.

## 5. Assumptions and regime of validity

1. **Half-space, not plate.** Valid for $t$ small compared with the plate
   thermal time $\sim L^2/\kappa$; the model over-predicts depth and heat flow for
   the oldest crust, and no age-dependence is valid for ages beyond the point
   where the lithosphere reaches the base of the convecting layer.
2. **One-dimensional conduction, no advection by the plate's motion across the
   axis** — valid for ages greater than a few $u^{-1}$-scale times, not at the
   axis.
3. **Constant $k$, $\kappa$, $\alpha_v$, $\rho$.** Real rock properties vary with
   temperature, porosity and alteration; the temperature dependence of $k$ alone
   changes the computed heat flow at the tens-of-percent level.
4. **Airy isostasy with a constant water density.** Sediment and seamount loads
   violate this; sedimented ridge flanks are shallower than the prediction.
5. **Uniform permeable layer of constant thickness.** Real permeability is
   log-normally distributed over several orders of magnitude and decays with
   depth and age.
6. **Steady spreading and a fixed axis.** Ridge jumps and propagating segments
   break $t=x/u$; this is a common failure in real data and shows up as scatter
   about the $\sqrt{t}$ law that no amount of noise modelling removes.
7. **The heat-budget inversion assumes a single $\Delta T$ and a single $f$.**
   Both are model quantities, and the result is inversely proportional to the
   first and proportional to the second.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| half-rate | $u$ | $\mathrm{m\,s^{-1}}$ | $1\ \mathrm{cm\,yr^{-1}}=3.1688\times10^{-10}$ |
| age | $t$ | s | |
| depth | $d$ | m | |
| subsidence coefficient | $a$ | $\mathrm{m\,s^{-1/2}}$ | $373.2\ \mathrm{m\,(Myr)^{-1/2}}$ |
| thermal diffusivity | $\kappa$ | $\mathrm{m^2\,s^{-1}}$ | |
| heat flow | $q$ | $\mathrm{W\,m^{-2}}$ | |
| permeability | $k$ | $\mathrm{m^2}$ | $1\ \mathrm{mD}=9.869\times10^{-16}$ |
| Rayleigh number | $\mathrm{Ra}$ | dimensionless | check numerator/denominator |

The dimensional check that matters: $a\sqrt{t}$ must be a length, so $a$ must
carry $\mathrm{m\,s^{-1/2}}$. In the derivation
$(\kappa/\pi)^{1/2}$ supplies $\mathrm{m\,s^{-1/2}}$ and every other factor is
dimensionless — a good way to catch a forgotten factor of $\alpha_v$ or a
substituted $\kappa$ in the wrong units.

## 7. Worked examples

All numbers below are printed by `code/mid_ocean_ridges_demo.py`.

### Example 1 — depth and heat flow of 4 Myr crust

$d = 2500 + 373.2\sqrt{4} = 2500 + 746.4 = 3246\ \mathrm{m}$, so the crust has
subsided $746\ \mathrm{m}$ since it left the axis. Its predicted conductive heat
flow is

$$q=\frac{4320}{\sqrt{3.1416\times10^{-6}\times4\times3.15576\times10^{13}}}
=216.9\ \mathrm{mW\,m^{-2}}.$$

Compare with the same model at 25 Ma: $86.8\ \mathrm{mW\,m^{-2}}$. A factor of
2.5 in heat flow corresponds to a factor of 6.25 in age, as $\sqrt{t}$ requires.

### Example 2 — is hydrothermal convection possible?

With $k=10^{-14}\ \mathrm{m^2}$, $H=1000\ \mathrm{m}$, $\Delta T=200\ \mathrm{K}$,
the demonstration computes $\mathrm{Ra}=50.5$ against $\mathrm{Ra}_c=39.478$:
convecting, with $\mathrm{Ra}/\mathrm{Ra}_c=1.28$. The onset permeability is
$7.81\times10^{-15}\ \mathrm{m^2}=7.9\ \mathrm{mD}$. If the permeable layer were
only 300 m thick, $\mathrm{Ra}$ would fall by a factor 3.33 to $15.2$, below
onset — so the *thickness* of the permeable zone, not the permeability alone,
decides the regime.

### Example 3 — measuring $a$ from noisy bathymetry

The demonstration generates 60 synthetic depths on 1–60 Ma crust with
$\sigma=60\ \mathrm{m}$ of scatter and fits $d=d_r+a\sqrt{t}$ by least squares:

$$d_r = 2509\pm25\ \mathrm{m},\qquad a=370.9\pm4.5\ \mathrm{m\,(Myr)^{-1/2}},$$

against a true $a=373.2$. The residual rms is $62.1\ \mathrm{m}$, consistent with
the injected scatter, and the discrepancy is $-0.51\sigma$ — i.e. the fit
recovers the physics. Note the fitted $d_r$ is 9 m off the true 2500 m: **the
intercept and the slope are correlated**, because both control the depth at the
mean age. This is the reason published subsidence coefficients are quoted with
their reference intercept.

### Example 4 — the axial thermal structure

At $x=5\ \mathrm{km}$ and a half-rate of $5\ \mathrm{cm\,yr^{-1}}$, the crust is
$0.1\ \mathrm{Ma}$ old and

$$z_{600}=0.83362\sqrt{10^{-6}\times0.1\times3.15576\times10^{13}}=1481\ \mathrm{m}.$$

At $1\ \mathrm{cm\,yr^{-1}}$ the same distance gives $3311\ \mathrm{m}$. The
predicted axial magma-lens depth and the predicted brittle–ductile transition are
therefore expected to differ by more than 2 km between fast and slow ridges — a
prediction that seismic reflection imaging tests directly
([15-02-01](../02-marine-geophysics-methods/01-marine-seismic-reflection.md)).

## 8. Python demonstration

`code/mid_ocean_ridges_demo.py` runs in well under a second and prints, with
units:

1. the four factors of the subsidence coefficient and the resulting
   $a=373.2\ \mathrm{m\,(Myr)^{-1/2}}$;
2. a synthetic noisy bathymetry and the fitted slope $370.9\pm4.5$, with the
   significance of the difference;
3. the heat-flow table, the $\sqrt{t}$ ratio test, and the ridge-flank slope;
4. the Rayleigh-number table, the onset permeability $7.9\ \mathrm{mD}$ and the
   Nusselt numbers;
5. the integrated heat deficit and the fluid volume $1.441\times10^{14}\ \mathrm{m^3}$;
6. the $600\ ^\circ\mathrm{C}$ depth for three spreading rates and three
   distances;
7. the worked-example values of Section 7.

Run it with the project environment:

```bash
cd 15-oceanography-marine/03-seafloor-tectonics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mid_ocean_ridges_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/01-mid-ocean-ridges-exercises.md`](./exercises/01-mid-ocean-ridges-exercises.md)
and
[`exercises/01-mid-ocean-ridges-solutions.md`](./exercises/01-mid-ocean-ridges-solutions.md).

## 10. Real-world applications

- **Age–depth curves.** Bathymetric grids are routinely converted to "crustal
  age" through $d=d_r+a\sqrt{t}$ with the coefficient derived here. Every
  age map of the seafloor carries $d_r$, $a$ and the assumption of steady
  spreading.
- **Hydrothermal resource and ecology.** Vent fields sit where fluid pathways
  reach the seafloor; the heat budget sets the total energy available to them and
  the fluid flux sets the chemical budget of the ocean.
- **Ocean chemistry.** The magnesium and sulphate budgets of seawater are set by
  hydrothermal exchange at ridges, which is why the fluid-flux number matters
  beyond geophysics.
- **Astrobiology and planetary analogues.** The same conduction-plus-convection
  arithmetic is applied to ice-covered ocean worlds, where the fluid is water and
  the "rock" is ice.
- **Survey design.** Deciding where to run a heat-flow transect is a
  ridge-flank-slope problem: the gradient at 10 Ma is
  $1.18\ \mathrm{m\,km^{-1}}$, so a 50 km transect spans only ~59 m of depth and
  is far below the resolution of shipboard echo sounding.

## 11. Further reading

- **Turcotte, D. L., & Schubert, G., *Geodynamics*, Cambridge University
  Press.** Level: graduate textbook. The standard derivation of half-space
  cooling, subsidence and the plate model.
- **Stein, C. A., & Stein, S., "A model for the global variation in oceanic
  depth and heat flow with lithospheric age", *Nature*.** Level: research. The
  reference for where the half-space law works and where it must be replaced.
- **The repository's own thermal-material constants** are listed in
  [26-reference-library/03-formula-handbook](../../26-reference-library/03-formula-handbook/README.md)
  and the units convention in
  [26-02-01 Symbol Handbook](../../26-reference-library/02-symbols-and-units/01-symbol-handbook.md).

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can derive $a$ from $\rho_m$, $\rho_w$, $\alpha_v$, $T_m$ and $\kappa$.
- [ ] I can state why $d\propto\sqrt{t}$ and $q\propto1/\sqrt{t}$ are the same
      physics.
- [ ] I can compute $\mathrm{Ra}$ and the onset permeability and say what each
      model parameter does to the answer.
- [ ] I can convert a heat deficit to a fluid volume and name every assumption.
- [ ] I can explain the young-crust heat-flow deficit in one sentence.
- [ ] I can compute $z_{600}$ for a given spreading rate and distance.
- [ ] I can name one independent measurement that would test the fluid-flux
      estimate.
## Common pitfalls
1. **Quoting a fluid flux without its $\Delta T$.** The heat budget fixes
   $\rho c_p \Delta T \cdot V$; the flux alone is not a result.
2. **Treating $\sqrt{t}$ subsidence as valid everywhere.** It fails on the
   oldest crust and at the axis; depth–age curves should be shown with their
   fitted range.
3. **Confusing permeability with hydraulic conductivity.** One has units of
   area, the other of velocity, and only the first is a rock property.
4. **Using a room-temperature viscosity in a $400\ ^\circ\mathrm{C}$ problem.**
   $\mu$ changes by an order of magnitude over the temperature range of ridge
   circulation, and $\mathrm{Ra}\propto1/\mu$.
5. **Reading the convection threshold as a prediction of vent locations.**
   $\mathrm{Ra}_c$ says whether a homogeneous layer would convect; it says
   nothing about where a vent is.
6. **Comparing a heat-flow measurement to the half-space model without
   subtracting the hydrothermal deficit.** The disagreement is the measurement.

## Related modules
- [15-03-02 Oceanic Crust Structure and Ophiolites](02-oceanic-crust-structure.md) —
  what the crust built at the ridge looks like in a seismic section.
- [15-03-03 Marine Subduction Zones, Trenches and Accretionary Prisms](03-subduction-zones-marine.md) —
  where the plate created here is consumed.
- [15-03-04 Fracture Zones, Transform Faults and Oceanic Anomalies](04-fracture-zones.md) —
  the age steps that make the $\sqrt{t}$ law measurable.
- [15-04-02 Gas Hydrates](../04-seafloor-mapping-and-habitats/02-gas-hydrates.md) —
  the same conductive geotherm applied where the fluid is methane.
- [12-03-01 Radiogenic Heat and the Geotherm](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md) —
  the continental-side counterpart of this heat budget.
- [13-01-03 Lithospheric Strength](../../13-geodynamics-tectonics/01-geodynamic-principles/03-lithospheric-strength.md) —
  how the $600\ ^\circ\mathrm{C}$ depth becomes a mechanical thickness.
