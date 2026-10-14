---
id: 16-03-03
title: "Cyclones, Fronts and Severe Weather Dynamics"
level: doctoral
prereqs: ["16-03-01", "16-01-04", "02-06-07"]
tags: [atmosphere, climate, cyclones, fronts, baroclinic-instability, cape, severe-weather]
---

# Cyclones, Fronts and Severe Weather Dynamics

Midlatitude weather is not imposed on the atmosphere; it **grows out of the
mean state**. The mean state has a horizontal temperature gradient, and by the
thermal wind relation (Section 5) that gradient *is* a vertical shear of the
zonal wind. A perturbation that tilts the temperature field into the shear can
convert the available potential energy of the mean state into its own kinetic
energy — and it does so at a rate that the geometry of the problem fixes
almost completely. Baroclinic instability is what makes a weather forecast
possible at all: it selects a preferred wavelength of about
$3.8\times10^3$ km and gives the disturbance an e-folding time of 1.8 days in
the demonstration's synthetic mean state, so an error in a synoptic map doubles
roughly every two days and a forecast has a finite horizon.

This lesson carries the calculation three scales further in: **fronts**, where
a passive scalar sharpens exponentially at the deformation rate until either a
secondary circulation balances it or the grid gives up; **deep convection**,
where CAPE measures the buoyant energy available to a lifted parcel and
$\sqrt{2\,\text{CAPE}}$ bounds the updraft; and the **tornado**, where the
relevant balance is cyclostrophic rather than geostrophic, and the Coriolis
term is smaller than the centrifugal term by about four orders of magnitude.

All models and data in this module are **SYNTHETIC**. The stratification,
shear, sounding and vortex parameters below are chosen teaching values printed
by [`code/storms_and_fronts_demo.py`](code/storms_and_fronts_demo.py), not
measurements, and are not fitted to any named storm. Standard constants
($\Omega$, $g$) are used as constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Eady normal-mode problem for baroclinic instability, including
   the two rigid-lid conditions, and **obtain** the condition
   $\coth\mu/\mu - 1/\mu^2 > 1/4$ for growth.
2. **Compute** the growth rate and the most unstable wavelength from $N$, $H$,
   $f$ and the shear, and **verify** the numerical maximum against the standard
   form $\sigma_{\max} = 0.31 f\,\mathrm{Ri}^{-1/2}$.
3. **Explain** why the unstable band is finite at both ends and what sets each
   cutoff.
4. **Derive** the thermal-wind relation from geostrophy and hydrostatics, and
   **state** precisely what a check against an analytic state does and does not
   test.
5. **Derive** the frontogenesis function for a pure deformation field, **compute**
   the doubling time of the front's gradient, and **identify** the resolution
   limit at which the numerical experiment stops measuring the physics.
6. **Compute** CAPE from a sounding and the buoyancy-based upper bound on updraft
   speed, and **state** the idealisation that makes the sensitivity to surface
   temperature as large as it is.
7. **Compute** the cyclostrophic pressure deficit of a Rankine vortex and
   **justify** neglecting the Coriolis term at that scale.

## Prerequisites

- [16-03-01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) —
  the thermal wind relation and the eddy fluxes that maintain the midlatitude
  jet, which is the mean state this lesson perturbs.
- [16-01-04 Moisture, Humidity Variables and Cloud Formation](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md) —
  the moist processes behind the CAPE calculation of Section 7.
- [02-06-07 Geophysical Fluids](../../02-physics/06-fluid-mechanics/07-geophysical-fluids.md) —
  rotating-fluid kinematics: the Rossby and Richardson numbers, and the
  geostrophic and thermal-wind balances used throughout.

## 1. Intuition: weather as an instability, not as an event

A pile of heavy fluid on top of light fluid falls over. The midlatitude
atmosphere is in an analogous state, but tilted rather than inverted: the
temperature decreases poleward along a sloping surface, and the thermal wind
relation converts that meridional contrast into vertical shear. A disturbance
that lifts warm air poleward and lowers cold air equatorward converts the mean
available potential energy into kinetic energy. The result is an amplifying wave
whose phase tilts westward with height — the signature of a baroclinic wave, and
the reason the trough axis of a surface low leans back toward the cold air.

Nothing in that picture needs an initial "storm". A small perturbation suffices,
and the mean state does the rest. The linear theory of Section 3 answers three
quantitative questions: how fast, at what size, and why those values and not
others.

## 2. Definitions

| Term | Meaning used here |
|---|---|
| QG | Quasigeostrophic: leading-order balance in $\mathrm{Ro}$, dynamics reduces to vorticity and thermodynamic budgets |
| Eady problem | Baroclinic instability on an $f$-plane with uniform $N$, constant shear, rigid lids and zero perturbation PV |
| $\mu = kNH/f$ | Nondimensional zonal wavenumber, the Eady control parameter |
| Deformation | A strain field with $\partial u/\partial x = -\partial v/\partial y$; it sharpens gradients without spinning them |
| Frontogenesis | The rate of increase of the horizontal potential-temperature gradient, following the flow |
| CAPE | Convective available potential energy: the depth integral of positive parcel buoyancy |
| LFC / EL | Level of free convection / equilibrium level: where parcel buoyancy changes sign |
| Cyclostrophic | Balance of pressure gradient against centrifugal acceleration; Coriolis omitted |
| Gradient wind | Pressure gradient balanced by Coriolis plus centrifugal acceleration |

## 3. Baroclinic instability: the Eady problem

### 3.1 Setting up

Take an $f$-plane with constant buoyancy frequency $N$, a zonal wind
$u = \Lambda z$ with constant shear $\Lambda = U_s/H$ over a layer of depth $H$,
rigid lids at $z = 0$ and $z = H$, and a perturbation with zero potential
vorticity. Quasigeostrophic theory gives

$$q' = \left(\frac{\partial^2}{\partial x^2}
+ \frac{f^2}{N^2}\frac{\partial^2}{\partial z^2}\right)\psi' = 0
\quad\Longrightarrow\quad
\psi' = \left(A\cosh\frac{\mu z}{H} + B\sinh\frac{\mu z}{H}\right)
\mathrm{e}^{\mathrm{i}kx},$$

with $\mu = kNH/f$ and $k$ the zonal wavenumber.

### 3.2 The two lid conditions

At each rigid lid $w' = 0$, so the thermodynamic equation reduces to

$$\left(\frac{\partial}{\partial t} + u(z)\frac{\partial}{\partial x}\right)
\frac{\partial\psi'}{\partial z} - \frac{\partial u}{\partial z}
\frac{\partial\psi'}{\partial x} = 0 .$$

Writing $\psi' = \phi(z)\mathrm{e}^{\mathrm{i}k(x-ct)}$ and substituting
$u = \Lambda z$:

$$z = 0:\quad -c\,\phi'(0) = \Lambda\,\phi(0),
\qquad
z = H:\quad (U_s - c)\,\phi'(H) = \Lambda\,\phi(H).$$

Eliminating the amplitudes gives a quadratic for the complex phase speed
$\hat c = c/U_s$:

$$\hat c^2 - \hat c + \left(\frac{\coth\mu}{\mu} - \frac{1}{\mu^2}\right) = 0,
\qquad
\hat c = \tfrac{1}{2}\left[1 \pm
\sqrt{1 - 4\left(\frac{\coth\mu}{\mu}-\frac{1}{\mu^2}\right)}\right].$$

Growth requires the discriminant to be negative:

$$\boxed{\;\chi(\mu) \equiv \frac{\coth\mu}{\mu} - \frac{1}{\mu^2} > \frac{1}{4}\;}$$

The most unstable mode has $\chi$ as large as possible; the growth rate is

$$\sigma = k\,U_s\,\mathrm{Im}(\hat c)
= \frac{\mu f}{NH}U_s\sqrt{\chi - \tfrac14}.$$

### 3.3 Numbers

The demonstration evaluates $\chi$ and $\sigma$ for a synthetic mean state at
$45^\circ$ with $N = 10^{-2}\ \mathrm{s^{-1}}$, $H = 10$ km,
$U_s = 20\ \mathrm{m\,s^{-1}}$ and $f = 1.03126\times10^{-4}\ \mathrm{s^{-1}}$:

| $\mu$ | $\chi$ | $\sigma/(fU_s/NH)$ |
|---|---|---|
| 0.25 | 0.33195 | 0.07157 |
| 0.50 | 0.32791 | 0.13956 |
| 0.80 | 0.31993 | 0.21155 |
| 1.00 | 0.31304 | 0.25107 |
| 1.20 | 0.30517 | 0.28186 |
| 1.40 | 0.29658 | 0.30215 |
| 1.606 | 0.28722 | 0.30982 |
| 1.80 | 0.27813 | 0.30188 |
| 2.00 | 0.26866 | 0.27318 |
| 2.20 | 0.25923 | 0.21140 |
| 2.399 | 0.25002 | 0.00970 |
| 2.60 | 0.24095 | 0.0 |

Measured results: the maximum is $\sigma/\text{scale} = 0.3098$ at
$\mu = 1.606$; the cutoff is at $\mu_c = 2.399$, exactly where
$\chi = 1/4$; the internal Rossby radius is $NH/f = 970$ km; the most unstable
zonal wavelength is

$$\lambda_{\max} = \frac{2\pi NH}{\mu_{\max}f} = 3794\ \mathrm{km},$$

and the e-folding time is $1.81$ days. The standard form
$\sigma_{\max} = 0.31\,fU_s/(NH)$ evaluates to $6.394\times10^{-6}\
\mathrm{s^{-1}}$, which is $1.0006\times$ the measured maximum: the famous
constant $0.31$ is nothing but the numerical maximum of
$\mu\sqrt{\chi - 1/4}$.

### 3.4 Why the unstable band is finite

Both ends are physical, not artefacts.

- **Small $\mu$ (long waves):** $\chi\to1/3$ as $\mu\to0$, so long waves are
  *stable* in the Eady model. The reason is that the two lid conditions couple
  only through the interior PV, which is zero: as the wavelength grows, the
  upper and lower boundary waves decouple, and the instability of one boundary
  alone disappears.
- **Large $\mu$ (short waves):** instability requires $\chi>1/4$, which fails
  for $\mu > 2.399$. Physically, a wave shorter than the depth it must
  communicate across cannot feel the shear coherently, and the two boundary
  waves get out of phase.

The result is that baroclinic instability **selects a size**: about
$3.8\times10^3$ km in this mean state. That selection is why synoptic charts
have a characteristic scale and why a forecast model's grid can be coarser than
the atmosphere's smallest motions.

## 4. What sets the size and the speed?

Two scaling laws fall out of Section 3.3:

$$\lambda_{\max} \propto \frac{NH}{f},
\qquad
\sigma_{\max} = 0.31\,\frac{fU_s}{NH}
= 0.31\,f\,\mathrm{Ri}^{-1/2},
\qquad
\mathrm{Ri} = \left(\frac{NH}{U_s}\right)^2 .$$

Because the growth rate collapses onto $\mathrm{Ri}$, shear and stratification
enter only through their ratio. The demonstration's synthetic survey (one
parameter changed per row) shows both trends:

| case | $\lambda_{\max}$ (km) | e-fold (d) |
|---|---|---|
| reference | 3794 | 1.81 |
| weaker stratification ($N = 7\times10^{-3}$) | 2656 | 1.27 |
| deeper layer ($H = 12$ km) | 4552 | 2.17 |
| shallow layer ($H = 8$ km) | 3035 | 1.45 |
| stronger shear ($U_s = 30$ m/s) | 3794 | 1.21 |
| weaker shear ($U_s = 12$ m/s) | 3794 | 3.02 |
| higher latitude ($60^\circ$) | 3098 | 1.48 |

Read the first two rows together: a *decrease* in stratification shortens the
most unstable wavelength **and** speeds up growth. A warmer, moister
troposphere has a smaller $N$, so this theory predicts both longer storms
(through $NH/f$) and faster growth (through $1/(NH)$) — two effects that push
against each other in any practical statement about future storminess. That is
a model prediction about a model quantity, not a forecast of storm frequency,
and it is stated here as a scaling only.

## 5. Thermal wind: derivation and what a verification tests

### 5.1 Derivation

Geostrophic balance in the meridional direction and hydrostatic balance are

$$fu = -\frac{1}{\rho}\frac{\partial p}{\partial y},
\qquad
\frac{\partial p}{\partial z} = -\rho g .$$

Differentiating the first with respect to $z$, substituting the second, and
using $p = \rho RT$ eliminates the density:

$$\frac{\partial u}{\partial z}
= \frac{R}{fp}\frac{\partial T}{\partial y}
= -\frac{g}{f\theta_0}\frac{\partial\theta}{\partial y}
\quad (\text{potential-temperature form}).$$

The relation gives the **shear**, never the wind: an additive constant must come
from a wind observation.

### 5.2 What a check proves

The demonstration takes $u = \Lambda z$ and
$\theta(y) = \theta_0 - (f\theta_0\Lambda/g)y$, which satisfies the relation
identically, and then differentiates $\theta$ numerically on a 10 km grid:

| quantity | value |
|---|---|
| $f\,\mathrm{d}u/\mathrm{d}z$ | $2.062522\times10^{-7}\ \mathrm{s^{-1}}$ |
| $-(g/\theta_0)\,\mathrm{d}\theta/\mathrm{d}y$ | $2.062522\times10^{-7}\ \mathrm{s^{-1}}$ |
| relative error of the numerical $\mathrm{d}\theta/\mathrm{d}y$ | $2.98\times10^{-13}$ |

The residual is round-off. **That check tests the algebra and the differencing
stencil, not the atmosphere.** Testing the thermal-wind relation against data
requires independent wind and temperature measurements, and then the error
budget belongs to the instruments, not to the identity. Saying which of the two
you have done is part of doing it.

## 6. Frontogenesis: sharpening a front

### 6.1 The frontogenesis function

Define $F = \mathrm{d}|\nabla_h\theta|/\mathrm{d}t$ following the flow.
Expanding the material derivative of $|\nabla_h\theta|$ gives the
**frontogenesis function**

$$F = -\frac{1}{|\nabla_h\theta|}\left[
\left(\frac{\partial\theta}{\partial x}\right)^2\frac{\partial u}{\partial x}
+ \left(\frac{\partial\theta}{\partial y}\right)^2\frac{\partial v}{\partial y}
+ \frac{\partial\theta}{\partial x}\frac{\partial\theta}{\partial y}
\left(\frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}\right)\right].$$

For a pure deformation field $u = -Dx$, $v = +Dy$ and a front whose gradient
lies along $x$, only the first term survives:

$$F = -\frac{1}{|\nabla_h\theta|}\left(\frac{\partial\theta}{\partial x}\right)^2
(-D) = D\,|\nabla_h\theta|
\quad\Longrightarrow\quad
|\nabla_h\theta| \propto \mathrm{e}^{Dt}.$$

So the *deformation rate* sets the sharpening rate, and the doubling time is
$\ln 2/D$. A front not aligned with the axis of contraction sharpens more
slowly; alignment matters.

### 6.2 The numerical experiment

The demonstration advects a passive potential-temperature front of initial width
200 km and amplitude $\pm10$ K in the strain field with
$D = 10^{-5}\ \mathrm{s^{-1}}$, using centered differences and a fourth-order
Runge–Kutta step (the strain field makes the problem one-dimensional, so no
dynamical closure is assumed). Measured gradient ratios:

| time (d) | ratio to $t=0$ | $\mathrm{e}^{Dt}$ | front width (km) |
|---|---|---|---|
| 0.23 | 1.221 | 1.221 | 164 |
| 0.93 | 2.225 | 2.226 | 90 |
| 1.85 | 4.952 | 4.953 | 40 |
| 2.78 | 11.007 | 11.023 | 18 |
| 3.70 | 24.353 | 24.533 | 8.2 |
| 4.63 | 52.802 | 54.598 | 3.8 |
| 5.32 | 90.567 | 99.484 | 2.2 |

The fitted growth rate over the first 4.4 days is
$9.960\times10^{-6}\ \mathrm{s^{-1}}$, i.e. $0.996\,D$: the kinematics is
reproduced to half a per cent. The doubling time is $\ln2/D = 0.80$ d, so the
200 km front is 100 km wide after 0.8 d and about 25 km after 2.4 d.

Past about 4 days the front is a few grid cells wide and the measured ratio
falls behind the analytic $\mathrm{e}^{Dt}$: at 5.3 d the exact value is 99×
while the model resolves 91×, and the gap widens. **The experiment has run out
of resolution, not of physics.** Nothing in the kinematics stops the collapse —
the exact solution reaches zero width in a finite time. Real fronts stop when
the ageostrophic circulation forced by the front itself (the secondary
circulation of the omega equation) reaches a balance with the deformation, and
that feedback is exactly what a passive-scalar experiment omits.

## 7. Severe convection: CAPE

### 7.1 Definition and the updraft bound

For a parcel rising without entraining environmental air, the vertical momentum
equation with buoyancy alone gives $\mathrm{d}w^2/\mathrm{d}z = 2b$, with
$b = g(T_{v,p}-T_{v,e})/T_{v,e}$. Integrating over the layers where the parcel
is buoyant,

$$\text{CAPE} = \int_{\text{LFC}}^{\text{EL}} g\,\frac{T_{v,p}-T_{v,e}}
{T_{v,e}}\,\mathrm{d}z,
\qquad
w_{\max} = \sqrt{2\,\text{CAPE}} .$$

CAPE is an energy per unit mass (J kg⁻¹) and $w_{\max}$ is the speed a parcel
would reach if all of that energy became kinetic energy.

### 7.2 A synthetic sounding

Environment: $T_e = 300\ \mathrm{K} - 6.5\ \mathrm{K\,km^{-1}}\,z$, **held
fixed**. Parcel starts at the surface temperature, follows a dry adiabat
(9.8 K km⁻¹) to the LCL at 1 km, then a moist adiabat (5.0 K km⁻¹).

| $T_\text{surf}$ (K) | CAPE (J kg⁻¹) | LFC (km) | $w_{\max}$ (m s⁻¹) |
|---|---|---|---|
| 296 | 2152.6 | 5.87 | 65.6 |
| 300 | 3709.0 | 3.21 | 86.1 |
| 304 | 5712.7 | 0.00 | 106.9 |
| 308 | 7894.6 | 0.00 | 125.7 |

Raising the parcel's surface temperature by 12 K raises CAPE by a factor of
3.7 and the updraft bound by 92%. **The sensitivity is strong because buoyancy
is a difference of two nearly equal profiles**: a few kelvin at every level is a
large change in their difference. Two caveats have to be stated with it. First,
the environment does *not* stay fixed as the surface warms — the idealisation
exaggerates the response, so this table is a mechanism and a ceiling, not a
projection. Second, $w_{\max} = \sqrt{2\,\text{CAPE}}$ is an **upper bound**: it
ignores entrainment of environmental air, water loading, and the reduction of
buoyancy by the dynamic pressure perturbation, each of which cuts a real updraft
substantially. Also note that for the two warm cases the LFC is zero, i.e. the
parcel is buoyant at the surface, and the equilibrium level lies above the
14 km domain, so it is not resolved.

## 8. Tornado-scale balance: cyclostrophic, not geostrophic

At a radius of 100 m with a 100 m s⁻¹ wind, the Rossby number is enormous, so
the Coriolis term is irrelevant and the radial balance is

$$\frac{\partial p}{\partial r} = \rho\frac{v^2}{r}.$$

For a **Rankine vortex** ($v = v_{\max}r/r_0$ inside the core of radius $r_0$,
$v = v_{\max}r_0/r$ outside), integrating gives results that do not depend on
$r_0$ at all:

$$\Delta p\big|_{\text{far field}\to\text{core edge}} = \tfrac{1}{2}\rho v_{\max}^2,
\qquad
\Delta p\big|_{\text{far field}\to\text{centre}} = \rho v_{\max}^2 .$$

With $\rho = 1.2\ \mathrm{kg\,m^{-3}}$:

| $v_{\max}$ (m s⁻¹) | to core edge (hPa) | total central (hPa) | $fr_0/v_{\max}$ |
|---|---|---|---|
| 30 | 5.4 | 10.8 | $2.79\times10^{-4}$ |
| 60 | 21.6 | 43.2 | $1.39\times10^{-4}$ |
| 100 | 60.0 | 120.0 | $8.37\times10^{-5}$ |
| 140 | 117.6 | 235.2 | $5.98\times10^{-5}$ |

At $v_{\max} = 100\ \mathrm{m\,s^{-1}}$ the total central deficit is 120 hPa
and the deficit to the core edge is 60 hPa; both scale as $v_{\max}^2$, so
halving the wind removes three quarters of the deficit. The last column is the
ratio of the Coriolis term $fv$ to the centrifugal term $v^2/r_0$ at the core
edge, $8.4\times10^{-5}$: **that is the quantitative justification for
cyclostrophic balance at this scale, and the exact opposite of the situation in
Section 3**, where geostrophy was the leading balance. The same atmosphere
supports both, on scales that differ by four orders of magnitude.

## 9. Assumptions and regime of validity

1. **Eady's idealisations**: constant $N$, constant shear, $f$-plane, rigid
   lids, zero perturbation PV. Relaxing any changes the numbers; the existence
   of a preferred scale survives, the value does not.
2. **Linear theory.** Section 3 gives growth rates of infinitesimal
   disturbances. It says nothing about amplitude, saturation, or the mature
   cyclone's structure.
3. **No moisture.** The Eady model is dry. Latent heating in a real cyclone
   increases both growth rate and amplitude, and is one route to the rapid
   deepening called explosive cyclogenesis. Neither the size nor the magnitude
   of that effect is computed here.
4. **Section 6 is kinematic.** No dynamics, no frontogenesis feedback, no
   friction, and an explicit resolution limit at a few grid cells.
5. **Section 7 holds the environment fixed.** That single idealisation is
   responsible for the size of the quoted sensitivity.
6. **$w_{\max} = \sqrt{2\,\text{CAPE}}$ is an upper bound** for the reasons in
   Section 7.2, and CAPE itself is a single-number summary of a vertical
   profile: two very different soundings can share a CAPE.
7. **Cyclostrophic balance** requires $\mathrm{Ro}\gg1$ and no significant
   radial inflow; it fails at the radius where the flow becomes
   rotation-dominated.

## 10. Worked examples

### Example 1 — size and speed of a baroclinic wave

Given $N = 10^{-2}\ \mathrm{s^{-1}}$, $H = 10^4$ m, $U_s = 20\
\mathrm{m\,s^{-1}}$, $f = 1.03126\times10^{-4}\ \mathrm{s^{-1}}$
($45^\circ$):

$$L_d = \frac{NH}{f} = \frac{10^{-2}\times10^4}{1.03126\times10^{-4}}
= 9.697\times10^5\ \mathrm{m} = 970\ \mathrm{km},$$

$$\lambda_{\max} = \frac{2\pi L_d}{1.606} = \frac{6.2832\times9.697\times10^5}
{1.606} = 3.794\times10^6\ \mathrm{m} = 3794\ \mathrm{km},$$

$$\sigma_{\max} = \frac{0.31\,fU_s}{NH}
= \frac{0.31\times1.03126\times10^{-4}\times20}{100}
= 6.394\times10^{-6}\ \mathrm{s^{-1}}
\;\Rightarrow\; \tau = \frac{1}{\sigma} = 1.81\ \mathrm{d}.$$

Note also $\mathrm{Ri} = (NH/U_s)^2 = (100/20)^2 = 25$, so
$\sigma_{\max} = 0.31 f/\sqrt{25} = 0.062\,f$, i.e.
$6.4\times10^{-6}\ \mathrm{s^{-1}}$: the same number a third way.

### Example 2 — frontogenesis doubling time

With $D = 10^{-5}\ \mathrm{s^{-1}}$,
$t_{2} = \ln 2/D = 0.69315/10^{-5} = 6.93\times10^4$ s $= 0.80$ d. In two
doubling times (1.6 d) the gradient is $4\times$ larger and the front half as
wide again: $200\to100\to50$ km. The measured ratio at 1.85 d — slightly more
than two doubling times — is 4.95 against $\mathrm{e}^{Dt} = 4.95$. ✔

### Example 3 — CAPE and the updraft bound

Take the strongest layer of the $T_\text{surf}=300$ K sounding. At $z = 6$ km
the parcel is at $300 - 9.8 - 5.0\times5 = 265.2$ K and the environment at
$300 - 6.5\times6 = 261.0$ K, so $b = 9.81\times4.2/261 = 0.158\
\mathrm{m\,s^{-2}}$. Over a 100 m slab that contributes
$0.158\times100 = 15.8\ \mathrm{J\,kg^{-1}}$. The full integral over the
buoyant depth gives 3709 J kg⁻¹, dominated by the mid-troposphere where the
parcel is warmer by several kelvin. Then $w_{\max} = \sqrt{2\times3709} = 86.1\
\mathrm{m\,s^{-1}}$.

## 11. Python demonstration

[`code/storms_and_fronts_demo.py`](code/storms_and_fronts_demo.py) prints every
number above in six labelled sections: the Eady dispersion relation and its
maximum; the sensitivity survey; the thermal-wind verification with its
numerical-differentiation error; the frontogenesis experiment with its fitted
growth rate and resolution limit; CAPE versus surface parcel temperature; and
the Rankine-vortex pressure deficit with the Coriolis ratio. It prints no
figures, needs no network, runs in a fraction of a second, and exits 0.

## 12. Exercises

Full sets with worked solutions are in
[`exercises/03-storms-and-fronts-exercises.md`](exercises/03-storms-and-fronts-exercises.md)
and
[`exercises/03-storms-and-fronts-solutions.md`](exercises/03-storms-and-fronts-solutions.md).

- **★** Compute $\chi(\mu)$ for $\mu = 1.0$ and $\mu = 2.5$ and state which is
  unstable, with the criterion.
- **★★** Derive $\sigma = (\mu f/(NH))U_s\sqrt{\chi-1/4}$ from
  $\hat c = \tfrac12[1\pm\sqrt{1-4\chi}]$.
- **★★** Compute $\lambda_{\max}$ and the e-folding time for a mean state with
  $N = 8\times10^{-3}\ \mathrm{s^{-1}}$, $H = 9$ km, $U_s = 25\
  \mathrm{m\,s^{-1}}$ at $55^\circ$.
- **★★★** The frontogenesis experiment saturates because of resolution. Design
  a numerical experiment that measures the fitted growth rate as a function of
  grid spacing and demonstrates convergence to $D$; state what quantity you
  would plot and what the plot would show.

## 13. Common mistakes

1. **Treating a check of an identity as a test of the atmosphere.** Section 5.2
   is the worked example of the distinction.
2. **Quoting a growth rate without its wavelength.** Baroclinic growth is a
   function of $\mu$; the pair $(\sigma,\lambda)$ is the result.
3. **Forgetting that $0.31$ is empirical.** It is the maximum of a
   one-dimensional function, not a physical constant of the atmosphere.
4. **Attributing the resolution-limited front to physics.** A model that stops
   sharpening because its grid is coarse has not discovered a brake.
5. **Using $\sqrt{2\,\text{CAPE}}$ as a forecast updraft.** It is an upper
   bound, and a loose one.
6. **Applying geostrophic reasoning at tornado scales** (or cyclostrophic
   reasoning at synoptic scales). Section 8 prints the ratio that decides.
7. **Reading the CAPE-versus-temperature sensitivity as a projection.** The
   environment is held fixed, which is the whole source of the large number.

## Mastery checkpoint

Complete this without notes.

> A midlatitude mean state has $N = 1.0\times10^{-2}\ \mathrm{s^{-1}}$,
> $H = 10$ km, $U_s = 20\ \mathrm{m\,s^{-1}}$ at $45^\circ$, and a front is
> being sharpened by a deformation field with $D = 1.0\times10^{-5}\
> \mathrm{s^{-1}}$. **(a)** Compute $\mathrm{Ri}$, the internal Rossby radius,
> and the most unstable wavelength. **(b)** Compute $\sigma_{\max}$ two ways and
> the e-folding time. **(c)** State why the Eady model has an *upper* cutoff in
> wavenumber but not an unbounded lower one. **(d)** Compute the time for the
> front's gradient to increase by a factor of 8 and the front width at that
> time. **(e)** At $v_{\max} = 100\ \mathrm{m\,s^{-1}}$, compute the central
> pressure deficit of a Rankine vortex and the ratio of the Coriolis to
> centrifugal term at a 100 m core radius.

A worked version of (a), (b) and (d) appears in the lesson-03
[solutions](exercises/03-storms-and-fronts-solutions.md).

## Common pitfalls

- **Confusing growth with genesis.** Linear theory gives a rate; it does not
  predict that a storm forms, only how fast a perturbation would amplify.
- **Reporting a wavelength without stating the mean state's $N$, $H$ and $f$.**
- **Forgetting the factor of 2 in the height-averaged shear** when converting
  thermal wind into a temperature structure (see [16-03-01](01-global-circulation.md) §4).
- **Mixing up the two cutoffs.** Long waves are stable because the lids
  decouple; short waves are stable because they cannot resolve the shear.
- **Treating CAPE as a property of the atmosphere rather than of a chosen
  parcel.**

## Related modules

- [01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) —
  the mean state this lesson destabilises.
- [02 Monsoons, Regional Circulation and Teleconnections](02-monsoons-and-regional.md) —
  regional circulations and the stationary waves that steer these systems.
- [04 Atmospheric Waves: Rossby, Kelvin, Gravity Waves](04-atmospheric-waves.md) —
  the wave dynamics behind the cutoff wavenumbers of Section 3.4.
- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  stability, available potential energy and latent heating.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) —
  why a model's grid and parameterisations matter at storm scale.
- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  what can and cannot be said about trends in severe weather.
- [19-02 Finite-Difference Methods](../../19-numerical-modeling-hpc/02-finite-difference-methods/README.md) —
  why the frontogenesis experiment saturates at the grid scale.
