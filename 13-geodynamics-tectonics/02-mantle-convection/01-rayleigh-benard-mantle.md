---
id: 13-02-01
title: "Rayleigh-Benard Convection Applied to the Mantle"
level: research
prereqs: ["13-01-01", "13-01-02", "02-06-06"]
tags: [geodynamics, tectonophysics, mantle-convection, rayleigh-number, boundary-layer-theory, stagnant-lid]
---

# Rayleigh-Benard Convection Applied to the Mantle

> All models and data in this module are **SYNTHETIC**. Every parameter set below
> is a chosen teaching model and every number quoted is printed by
> `code/rayleigh_benard_mantle_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Rayleigh number by nondimensionalising the Boussinesq
   equations, and **state** the physical meaning of each factor in it.
2. **Compute** $Ra$ for several planetary parameter sets and **interpret** the
   supercriticality $Ra/Ra_c$.
3. **Derive** the critical Rayleigh number $Ra_c = 27\pi^{4}/4$ for free-slip
   boundaries from the linearised marginal-stability problem, and **verify** it
   numerically by shooting on the sixth-order system.
4. **Show** how boundary conditions change $Ra_c$ and the critical wavelength,
   using an independently computed no-slip value as a check on the method.
5. **Derive** the thermal boundary-layer scalings $\delta \propto Ra^{-1/3}$ and
   $Nu\propto Ra^{1/3}$, and **state** what scaling theory does *not* fix.
6. **Compute** the viscosity contrast implied by temperature-dependent viscosity
   and **explain** why it produces a stagnant lid.
7. **Estimate** a convective velocity scale and compare it with plate speeds,
   reporting the order-unity coefficient honestly.

## Prerequisites

- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](../01-geodynamic-principles/01-momentum-mass-energy.md) —
  the balances and the Péclet number.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  where a temperature-dependent $\eta$ comes from.
- [02-06-06 Mantle Convection and Rayleigh-Benard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md) —
  the fluid-dynamical setting.
- [12-03-01 Radiogenic Heat Production and Mantle Geotherms](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md) —
  the temperature differences used here.

## 1. Intuition: one number decides whether the mantle overturns

Heat a layer of fluid from below and cool it from above. For a small temperature
difference nothing moves: heat crosses by conduction and the temperature profile
is a straight line. Increase the difference past a threshold and the layer
overturns. The threshold is not a temperature but a dimensionless group, the
**Rayleigh number**, and its critical value for a layer with free-slip boundaries
is an exact number,

$$Ra_c = \frac{27\pi^{4}}{4} = 657.511\ldots$$

Everything about mantle convection follows from the fact that the Earth's value
is *not* 657.5 but of order $10^{7}$. The mantle is not marginally unstable; it is
unstable by four and a half orders of magnitude. Working out what a
$10^{4}$-fold supercriticality implies — thin boundary layers, a Nusselt number
of a few tens, a sluggish interior, a convective velocity set by boundary-layer
physics rather than by the bulk temperature difference — is the content of this
lesson.

The second theme is that the *coefficient* in the scaling laws is invisible to
scaling theory. Boundary-layer arguments give exponents ($Nu\sim Ra^{1/3}$,
$\delta\sim Ra^{-1/3}$) but leave the prefactor as an unknown $O(1)$ function of
the boundary conditions. Half of this lesson is therefore about what can be
derived exactly, and the other half about what must be measured — which is the
reason the module continues with a numerical model in
[13-02-02](02-convection-numerical.md).

## 2. The equations and the Rayleigh number

### 2.1 Boussinesq equations for a layer

Take a layer of depth $d$, heated from below with temperature difference
$\Delta T$, with constant viscosity $\eta$, thermal diffusivity $\kappa = k/(\rho
c_p)$, thermal expansivity $\alpha$ and a Stokes (infinite-Prandtl) momentum
balance:

$$\nabla\cdot\mathbf{u} = 0, \qquad
\nabla p = \eta\nabla^{2}\mathbf{u} + \rho_0 g\alpha\theta\hat{\mathbf{z}},
\qquad
\frac{\partial\theta}{\partial t} + \mathbf{u}\cdot\nabla\theta = \kappa
\nabla^{2}\theta + w\frac{\Delta T}{d}.$$

Scale lengths by $d$, temperature by $\Delta T$, velocities by $\kappa/d$, time by
$d^{2}/\kappa$ and pressure by $\eta\kappa/d^{2}$. The heat equation becomes

$$\frac{\partial\theta'}{\partial t'} + \mathbf{u}'\cdot\nabla'\theta' =
\nabla'^{2}\theta' + w' ,$$

with no free parameter at all, and the momentum equation becomes

$$\nabla' p' = \nabla'^{2}\mathbf{u}' + Ra\,\theta'\hat{\mathbf{z}},
\qquad
\boxed{\;Ra \equiv \frac{\rho_0 g\alpha\Delta T d^{3}}{\kappa\eta}\;}.$$

$Ra$ is the *only* dimensionless group left. Read its factors:

| factor | meaning |
|---|---|
| $\alpha\Delta T$ | fractional density anomaly — the buoyancy |
| $\rho_0 g\alpha\Delta T d$ | buoyancy stress scale |
| $d^{3}$ | the volume over which buoyancy acts |
| $1/\eta$ | viscous resistance |
| $1/\kappa$ | how slowly conduction removes the anomaly |

The last factor is the subtle one: $Ra$ is large not only when buoyancy is strong
but when conduction is *slow*. A highly viscous fluid can convect with a tiny
temperature difference provided the layer is thick.

### 2.2 Measured values

With SYNTHETIC $\rho_0 = 3300\ \mathrm{kg\,m^{-3}}$,
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, $\kappa = 10^{-6}\ \mathrm{m^{2}\,
s^{-1}}$ and $g = 9.81\ \mathrm{m\,s^{-2}}$:

| parameter set | $d$ (km) | $\Delta T$ (K) | $\eta$ (Pa s) | $Ra$ |
|---|---|---|---|---|
| whole mantle | 2900 | 1300 | $10^{21}$ | $3.079\times10^{7}$ |
| upper mantle | 700 | 1300 | $10^{21}$ | $4.331\times10^{5}$ |
| whole mantle | 2900 | 1300 | $10^{22}$ | $3.079\times10^{6}$ |
| Mars-like ($g = 3.71$) | 1800 | 1300 | $10^{21}$ | $2.785\times10^{6}$ |
| Venus-like ($g = 8.87$) | 3000 | 1300 | $10^{21}$ | $3.082\times10^{7}$ |

The supercriticalities are $4.68\times10^{4}$, $6.59\times10^{2}$,
$4.68\times10^{3}$, $4.24\times10^{3}$ and $4.69\times10^{4}$ respectively. The
lesson from the table is not any single value but the *insensitivity*: changing
$g$ by a factor of 2.4, $d$ by a factor of 4 or $\eta$ by a factor of 10 moves
$Ra$ by one to one-and-a-half decades, and in every case leaves the mantle
thousands of times supercritical. **No plausible planet with a silicate mantle is
near the onset of convection.** The interesting questions are always about
style — vigour, lid behaviour, planform — never about whether.

## 3. Marginal stability: deriving $Ra_c = 27\pi^{4}/4$

### 3.1 Linearisation

Perturb the conducting state $T = 1 - z + \theta$ with
$\theta = \Theta(z)\cos kx$ and $\psi = \Psi(z)\sin kx$ (the pairing that makes the
$x$-derivatives consistent). The linearised momentum balance and heat balance are

$$(D^{2} - k^{2})^{2}\Psi = k^{2}Ra\,\Theta,
\qquad
(D^{2} - k^{2})\Theta = -k\Psi ,
$$

where $D = \mathrm{d}/\mathrm{d}z$. Eliminating $\Theta$ gives a sixth-order
eigenvalue problem,

$$\boxed{\;(D^{2} - k^{2})^{3}\Psi = -k^{2}Ra\,\Psi\;}.$$

For free-slip boundaries the conditions are

$$\Psi = \Psi'' = \Theta = 0 \quad \text{at } z = 0, 1 ,$$

and the third condition follows from the momentum equation:
$(D^{2}-k^{2})^{2}\Psi = k^{2}Ra\Theta = 0$ at a boundary where $\Theta = 0$.

### 3.2 The exact solution

The functions $\Psi = \sin(n\pi z)$ satisfy all six conditions. Then

$$(D^{2}-k^{2})^{3}\Psi = -(n^{2}\pi^{2}+k^{2})^{3}\Psi ,$$

so marginal stability ($\sigma = 0$) requires

$$Ra_n(k) = \frac{(n^{2}\pi^{2} + k^{2})^{3}}{k^{2}} .$$

The most unstable mode is $n = 1$. Minimise over $k$ by setting
$\mathrm{d}Ra/\mathrm{d}k^{2} = 0$ with $a = \pi^{2}$:

$$Ra = \frac{(a+k^{2})^{3}}{k^{2}},
\qquad
\frac{\mathrm{d}Ra}{\mathrm{d}k^{2}} \propto 3(a+k^{2})^{2}k^{2} - (a+k^{2})^{3}
= 0
\;\Longrightarrow\;
k_c^{2} = \frac{\pi^{2}}{2},
\; k_c = \frac{\pi}{\sqrt{2}} ,$$

$$Ra_c = \frac{(1.5\pi^{2})^{3}}{\pi^{2}/2} = \frac{3.375\,\pi^{6}}{0.5\,\pi^{2}}
= 6.75\,\pi^{4} = \frac{27\pi^{4}}{4} = 657.511\ldots \;\; \checkmark$$

The corresponding wavelength is $2\pi/k_c = 2\sqrt{2}\,d = 2.8284\,d$. The
measured marginal curve confirms the minimum numerically:

| $k$ | 1.0 | 1.5 | 2.221 | 3.0 | 4.0 |
|---|---|---|---|---|---|
| $Ra(k)$ | 1284.23 | 791.19 | **657.51** | 746.53 | 1082.06 |

A fine grid search gives $Ra = 657.5114$ at $k = 2.2214$, a relative difference
from $27\pi^{4}/4$ of $3.37\times10^{-12}$ — the minimum is found to round-off.

### 3.3 Independent verification by shooting

An algebraic check of a closed form tests nothing new, so the demonstration also
solves the boundary-value problem numerically. Writing the linear system as six
first-order ODEs,

$$W'''' = 2k^{2}W'' - k^{4}W + k^{2}Ra\Theta,
\qquad \Theta'' = k^{2}\Theta - W ,$$

with the appropriate boundary conditions, integration from $z = 0$ to $z = 1$ of
a three-dimensional basis of admissible solutions gives a $3\times3$ determinant
whose vanishing is the eigenvalue condition. Bisecting that determinant:

| boundary conditions | $k$ | measured $Ra$ | comparison |
|---|---|---|---|
| free slip | 2.000 | 667.010 | $( \pi^{2}+k^{2})^{3}/k^{2} = 667.010$ (agreement $4\times10^{-13}$) |
| free slip | 2.221 | 657.511 | $27\pi^{4}/4 = 657.511$ ($2\times10^{-13}$) |
| free slip | 3.000 | 746.528 | closed form 746.528 ($4\times10^{-14}$) |
| no slip | 3.100 | 1707.829 | classical value 1707.76 (0.004%) |

The no-slip entry is the important one: there is *no* closed form for the
rigid-rigid case, and recovering the classical value independently is a
verification of the solver rather than of a formula. It also carries the physics
the next section needs.

### 3.4 What boundary conditions do

| boundaries | $Ra_c$ | critical wavelength |
|---|---|---|
| free slip / free slip | 657.51 | $2.828\,d$ |
| no slip / no slip | 1707.8 | $2.027\,d$ |

No-slip boundaries raise the threshold by a factor of 2.6 and make the cells
*narrower*. Both are intuitive in hindsight: a rigid lid resists horizontal
motion at the boundary, so more buoyancy is needed and the cells cannot spread.
The Earth is neither case, but a plate is much closer to no-slip than to
free-slip — which is why the *style* of mantle convection is a statement about
the surface boundary condition, not just about $Ra$.

## 4. Boundary-layer scaling

### 4.1 Deriving the exponents

At large $Ra$ the temperature field separates into two thin thermal boundary
layers of thickness $\delta$ and a nearly isothermal interior. Across the bottom
layer the local Rayleigh number based on $\delta$ must be near critical:

$$Ra_\delta \sim \frac{\rho g\alpha\Delta T \delta^{3}}{\kappa\eta} = Ra
\left(\frac{\delta}{d}\right)^{3} \sim Ra_c
\;\;\Longrightarrow\;\;
\boxed{\;\frac{\delta}{d} \sim Ra^{-1/3}\;}$$

and, since the surface flux is $q \sim k\Delta T/\delta$ against the conductive
reference $k\Delta T/d$,

$$\boxed{\;Nu \equiv \frac{q}{k\Delta T/d} = \frac{d}{\delta}
\sim \left(\frac{Ra}{Ra_c}\right)^{1/3}\;}.$$

The convective velocity follows from a local force balance inside the boundary
layer: buoyancy $\sim \rho g\alpha\Delta T$ against viscous stress
$\sim \eta u/\delta^{2}$, giving

$$u \sim \frac{\rho g\alpha\Delta T\,\delta^{2}}{\eta}
= \frac{\kappa}{d}\,Ra\left(\frac{\delta}{d}\right)^{2} .$$

### 4.2 Measured numbers for the whole-mantle set

With $Ra = 3.079\times10^{7}$, $Ra_c = 657.5$, $d = 2900$ km:

| quantity | formula | value |
|---|---|---|
| supercriticality | $Ra/Ra_c$ | $4.683\times10^{4}$ |
| boundary-layer thickness | $d(Ra_c/Ra)^{1/3}$ | 80.45 km |
| Nusselt number | $(Ra/Ra_c)^{1/3}$ | 36.05 |
| velocity scale | $(\kappa/d)Ra(\delta/d)^{2}$ | $8.172\times10^{-9}$ m s$^{-1}$ |
| in geological units | | $0.26$ m yr$^{-1}$ |
| overturn time | $d/u$ | $3.549\times10^{14}$ s $=11.2$ Myr |

Now read the last two rows carefully, because they contain the honesty of the
whole scaling approach. The predicted boundary-layer thickness, 80 km, and
Nusselt number, 36, are the right order of magnitude for the mantle. The
predicted velocity, $0.26\ \mathrm{m\,yr^{-1}}$, is about
$u/30\ \mathrm{mm\,yr^{-1}} = 9$ times larger than a synthetic reference plate
speed of 30 mm/yr — and the demonstration says so explicitly. Scaling theory
gives exponents; it gives the prefactor only as "some $O(1)$-to-$O(10)$
number". A prediction that is right to a factor of 9 is a *successful* scaling
argument in this subject and must be reported as such, not rounded into a
prediction. Nothing is learned by pretending that $u = 0.26$ m/yr is wrong while
$0.030$ m/yr is right; what is learned is that the velocity scale is set by
boundary-layer dynamics and that its coefficient requires solving the boundary
layer.

## 5. Temperature-dependent viscosity: why lids form

Real mantle viscosity is Arrhenius. Over a boundary layer with temperature drop
$\Delta T$ around $T_0$,

$$\frac{\eta(T_0-\Delta T)}{\eta(T_0)}
= \exp\!\left[\frac{E}{R}\left(\frac{1}{T_0 - \Delta T} -
\frac{1}{T_0}\right)\right]
\approx \exp\!\left[\frac{E\,\Delta T}{R\,T_0^{2}}\right] .$$

Measured with $T_0 = 1600$ K (SYNTHETIC activation energies):

| $E$ (kJ mol$^{-1}$) | $\Delta T$ (K) | viscosity contrast | effective $Ra$ factor |
|---|---|---|---|
| 350 | 200 | $2.68\times10^{1}$ | $3.73\times10^{-2}$ |
| 350 | 100 | $5.18$ | $1.93\times10^{-1}$ |
| 200 | 200 | $6.55$ | $1.53\times10^{-1}$ |

Two consequences, in order of importance:

1. **The effective Rayleigh number is reduced**, because the relevant viscosity
   is that of the cold, stiff surface layer: here by a factor of 27. Convection
   is still vigorous, but the top of the layer is effectively immobilized.
2. **A stagnant lid forms.** Once the surface is a factor of $10^{3}$–$10^{6}$
   stiffer than the interior, it cannot participate in the overturning; the
   convective flow develops beneath a rigid, conducting lid, and the surface
   heat flux is set by conduction through it rather than by the flow reaching the
   surface. The Earth has escaped this regime only because of plate tectonics:
   its lid is broken into plates that subduct.

It is worth stating the falsifiable part plainly: a planet with the same $Ra$ but
no mechanism for recycling its lid will cool less efficiently than one with
plates, and its surface will be older. That contrast — Earth versus a
single-plate planet of the same size — is one of the few places where geodynamics
makes a prediction about planetary diversity, and it is testable against
[12-07-01](../../12-global-geophysics-interior/07-planetary-interiors-comparative/01-terrestrial-planets-interiors.md).

## 6. The regime map

| parameter set | $Ra$ | $Ra/Ra_c$ | regime |
|---|---|---|---|
| whole mantle, $\eta = 10^{21}$ | $3.079\times10^{7}$ | $4.68\times10^{4}$ | vigorous convection |
| upper mantle, $d = 700$ km | $4.331\times10^{5}$ | $6.59\times10^{2}$ | convecting |
| whole mantle, $\eta = 10^{22}$ | $3.079\times10^{6}$ | $4.68\times10^{3}$ | convecting |
| Mars-like | $2.785\times10^{6}$ | $4.24\times10^{3}$ | convecting |
| Venus-like | $3.082\times10^{7}$ | $4.69\times10^{4}$ | vigorous convection |

Every entry is convective. The table is a reminder that the useful axis is not
$Ra$ but the combination $(Ra, \text{viscosity contrast}, \text{boundary
conditions})$: Venus-like and Earth-like share $Ra$ and differ in whether the
lid is recycled. Classifying planets by $Ra$ alone would put Venus and Earth in
the same box, which is exactly the box that hides the interesting physics.

## 7. Assumptions and regime of validity

| assumption | where it fails |
|---|---|
| Boussinesq, constant properties | compressibility and depth-dependent $\alpha$, $\rho$ |
| constant viscosity | the whole point of §5; real $\eta$ spans $>10^{20}$ |
| Stokes (infinite Prandtl) | correct for the mantle; wrong for the outer core |
| planar layer, uniform heating | spherical geometry, internal heating, secular cooling |
| no phase transitions | 410 and 660 km change $Ra$ locally and add latent heat |
| no melting | affects the thermal boundary layer where it matters |
| linear stability analysis for $Ra_c$ | says nothing about the finite-amplitude state |
| two equal boundary layers | an internally heated or bottom-heated-only case is asymmetric |

The last row deserves emphasis because it is where the boundary-layer scalings are
weakest. The formula $Nu\sim(Ra/Ra_c)^{1/3}$ assumes the heat flux is supplied by
bottom heating. Real mantle heat generation is distributed, which changes the
scaling exponent towards 1/4 in the strongly internally heated limit and makes the
Nusselt number a function of the distribution. Any use of these scalings for the
Earth must therefore state whether it is modelling bottom heating, internal
heating or both — and the honest expectation is that the Earth is a mixture, so
neither exponent should be claimed as the answer.

## 8. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| Rayleigh number | $Ra$ | — | $(\mathrm{kg\,m^{-3}})(\mathrm{m\,s^{-2}})(\mathrm{K^{-1}})(\mathrm{K})(\mathrm{m^{3}}) / [(\mathrm{m^{2}\,s^{-1}})(\mathrm{Pa\,s})]$ |
| thermal diffusivity | $\kappa$ | m$^{2}$ s$^{-1}$ | $(k)/(\rho c_p)$ |
| wavenumber | $k$ | — (per $d$) | $2\pi/\lambda$ |
| Nusselt number | $Nu$ | — | flux / conductive flux |
| boundary layer | $\delta$ | m | $d\,Ra^{-1/3}$ |

A useful numerical habit: $Ra$ as written is the product of a buoyancy stress
$\rho g\alpha\Delta T d$ and a volume $d^{2}$ divided by $\kappa\eta$; if you
cannot express the number you have computed as those pieces, the units are wrong.

## 9. The demonstration

`code/rayleigh_benard_mantle_demo.py` prints every number above:

```bash
cd 13-geodynamics-tectonics/02-mantle-convection/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rayleigh_benard_mantle_demo.py
```

It computes $Ra$ for five parameter sets; tabulates and minimises the marginal
curve; solves the linear stability problem by shooting for both free-slip and
no-slip boundaries and compares with $27\pi^{4}/4$ and with the classical no-slip
value; evaluates the boundary-layer scalings; and computes viscosity contrasts
from Arrhenius factors. Fixed seed, print-only, no network, exits 0.

Exercises:
[`exercises/01-rayleigh-benard-mantle-exercises.md`](exercises/01-rayleigh-benard-mantle-exercises.md)
and
[`exercises/01-rayleigh-benard-mantle-solutions.md`](exercises/01-rayleigh-benard-mantle-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC planet has $\rho_0 = 3500\ \mathrm{kg\,m^{-3}}$,
> $\alpha = 2.5\times10^{-5}\ \mathrm{K^{-1}}$,
> $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
> $d = 2000$ km, $\Delta T = 1200$ K, $\eta = 5\times10^{21}$ Pa s.
> **(a)** Compute $Ra$ and $Ra/Ra_c$. **(b)** Compute the predicted boundary-layer
> thickness and Nusselt number. **(c)** Estimate the convective velocity and the
> overturn time, and state the expected size of the error in the velocity.
> **(d)** The planet's surface is observed to be ancient and its heat flux lower
> than (b) predicts. Give the single physical modification that would explain
> both, and say what it does to the effective $Ra$.

A worked version appears in the
[solutions](exercises/01-rayleigh-benard-mantle-solutions.md).

## Common pitfalls

1. **Quoting $Ra$ without stating $d$ and $\Delta T$.** The same Earth gives
   values differing by decades depending on the layer you choose.
2. **Treating $Ra_c = 657.5$ as universal.** It is the free-slip value; no-slip
   boundaries give 1707.8 (measured here), and other boundary conditions give
   other numbers.
3. **Using the marginal wavelength in a box of a different width.** The box
   selects modes; a 2.83 $d$ box selects $k_c$, a 4 $d$ box does not.
4. **Believing $Nu = (Ra/Ra_c)^{1/3}$ as an equality.** It is a scaling with an
   $O(1)$ coefficient; the measured coefficient in
   [13-02-02](02-convection-numerical.md) is 1.88, not 1.
5. **Forgetting the Prandtl number when moving to another fluid.** The mantle is
   in the infinite-Prandtl limit; the outer core is not.
6. **Assuming a hotter planet convects harder.** Increase $\Delta T$ and $Ra$
   rises, but a hotter planet also has lower viscosity, and the two effects fight.
7. **Ignoring that $Nu$ depends on the heating mode.** Bottom-heated and
   internally heated layers scale differently.

## Related modules

- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](../01-geodynamic-principles/01-momentum-mass-energy.md) —
  the balances nondimensionalised here.
- [13-02-02 Numerical Modelling of Mantle Convection](02-convection-numerical.md) —
  the solver that measures the coefficients this lesson cannot derive.
- [13-02-03 Mantle Plumes, Hotspots and Large Igneous Provinces](03-mantle-plumes.md) —
  the same scalings applied to a discrete rising instability.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](04-subduction-dynamics.md) —
  the cold downwelling that makes the convection organised rather than chaotic.
- [12-07-01 Interiors of Mars, Venus, Mercury and the Moon](../../12-global-geophysics-interior/07-planetary-interiors-comparative/01-terrestrial-planets-interiors.md) —
  the comparative use of this regime map.
