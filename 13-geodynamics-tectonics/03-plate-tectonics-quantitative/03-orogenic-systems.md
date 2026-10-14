---
id: 13-03-03
title: "Orogenic Systems, Crustal Thickening and Collapse"
level: research
prereqs: ["13-01-04", "13-06-01", "04-04-01"]
tags: [geodynamics, tectonophysics, orogeny, isostasy, buoyancy, crustal-thickening, collapse]
---

# Orogenic Systems, Crustal Thickening and Collapse

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Airy relation between crustal thickness and elevation for an
   air-loaded column, and **compute** the elevation and Moho depth of a
   thickened crust.
2. **Convert** an elevation to the shortening required by volume conservation,
   and **state** the assumptions that make the conversion unique.
3. **Derive** the buoyancy force per unit length between two columns as an exact
   integral of the lithostatic pressure difference, and **compare** it with the
   commonly quoted scale $g\rho_c(t^{2}-t_0^{2})/2$.
4. **Build** the dimensionless group that controls gravitational collapse and
   **compute** the collapse time and the effective viscosity it implies.
5. **Quantify** the isostatic rebound amplification of erosion and **explain**
   why removing topography by erosion is slow.
6. **Demonstrate** quantitatively that an elevation cannot be inverted for a
   crustal thickness without an independent constraint, using the
   mantle-lithosphere alternative.
7. **State** the regime of validity of the thin, isostatic, Newtonian picture and
   the observations that break each assumption.

## Prerequisites

- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](../01-geodynamic-principles/04-forces-and-stresses.md) —
  the stress balance that a buoyancy force has to be entered into.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the full isostasy and flexure framework, of which Airy is the local limit.
- [04-04-01 Stress, Strain and Brittle vs Ductile Deformation](../../04-earth-science-geology/04-structural-geology/01-stress-strain-rocks.md) —
  how the deformation is actually accommodated.

All models and data in this module are **SYNTHETIC**. The numbers below are
model outputs of `code/orogenic_systems_demo.py` for a chosen teaching
lithosphere, not measurements of any real orogen. The exact constant used is
$g = 9.81\ \mathrm{m\,s^{-2}}$.

## 1. Elevation is a buoyancy measurement, not a thickness measurement

An orogen is a region where the crust has been thickened and the surface has
risen. To first order the rise is an isostatic response, and the arithmetic of
that response is worth deriving once, slowly, because almost every number in
this lesson descends from it.

Take a reference crustal column of thickness $t_{c0}$ whose surface is at sea
level, and a thickened column of thickness $t_c$ whose surface is a height $e$
above it. Both are underlain by the same mantle and both are compensated at a
depth below the deepest Moho. Equal pressure at that depth gives

$$
\rho_c t_{c0} + \rho_m (D - t_{c0}) = \rho_c t_c + \rho_m (D + e - t_c),
$$

which simplifies to the **Airy relation**

$$
\boxed{\;e = (t_c - t_{c0})\,\frac{\rho_m - \rho_c}{\rho_m}\;}
\qquad (\text{air-loaded, local compensation}).
$$

Every consequence of this lesson follows from that single factor

$$
\frac{\rho_m - \rho_c}{\rho_m} =
\frac{3330 - 2800}{3330} = 0.1592 .
$$

**One kilometre of crustal thickening buys $0.1592\ \mathrm{km}$ of elevation**,
equivalently $6.28\ \mathrm{km}$ of crust per kilometre of topography. The
demonstration's table for the SYNTHETIC densities:

| $t_c$ (km) | 35 | 40 | 50 | 60 | 70 | 80 |
|---|---|---|---|---|---|---|
| $e$ (km) | 0.000 | 0.796 | 2.387 | 3.979 | 5.571 | 7.162 |
| Moho depth $e+t_c$ (km) | 35.0 | 40.8 | 52.4 | 64.0 | 75.6 | 87.2 |

A $70\ \mathrm{km}$ crust stands $5.57\ \mathrm{km}$ above the reference. That
is the right order for the highest plateaux and it is a pure ratio of densities:
the number is a model result with stated densities, not a measurement of any
particular mountain belt.

### 1.1 Shortening, and the first assumption that bites

If crustal material is conserved and the deformation is plane strain, thickening
to $t_c$ requires a stretching factor $\beta = t_c/t_{c0}$ and a horizontal
shortening

$$
\text{shortening} = 1 - \frac{1}{\beta} = 1 - \frac{t_{c0}}{t_c}.
$$

| $t_c$ (km) | $\beta$ | shortening |
|---|---|---|
| 40 | 1.143 | 12.5% |
| 50 | 1.429 | 30.0% |
| 60 | 1.714 | 41.7% |
| 70 | 2.000 | 50.0% |

Doubling the crustal thickness requires $50\%$ shortening. That is an enormous
number, and it is the reason large orogens are wide: the shortening has to be
distributed over hundreds of kilometres, or accommodated by processes the
volume-conservation argument does not include (crustal flow out of the section,
underthrusting, or the removal of material by erosion). Only one of those
assumptions is testable from the elevation alone, and none of them is: the same
$5.57\ \mathrm{km}$ can be reached with different combinations.

## 2. The buoyancy force, derived exactly

Elevation differences imply horizontal forces. The force per unit length that
tends to spread a thickened column is the depth integral of the difference in
lithostatic pressure between the two columns:

$$
\Gamma = \int_{0}^{\infty}\bigl[P(z) - P_{\text{ref}}(z)\bigr]\,\mathrm dz
\qquad (\mathrm{N\,m^{-1}}),
$$

where the integral converges because the columns are compensated: below both
Mohos the integrand is identically zero. Evaluating the integral in the two
regions where it is non-zero — inside the reference crust and between the two
Moho levels — gives, with $E$ the elevation in metres and
$\bar u = t_c - t_{c0} + E$,

$$
\Gamma = \rho_c g E\,t_{c0}
+ g\!\left[\frac{(\rho_c-\rho_m)\bar u^{2}}{2}
+ \rho_c(t_{c0}+E)\bar u\right] .
$$

The demonstration evaluates this exactly and compares it with the scale

$$
\Gamma_{\text{scale}} = \frac{g\rho_c}{2}\left(t_c^{2} - t_{c0}^{2}\right),
$$

| $t_c$ (km) | $\Gamma$ exact ($10^{12}\ \mathrm{N\,m^{-1}}$) | $\Gamma_{\text{scale}}$ | ratio |
|---|---|---|---|
| 40 | 4.853 | 5.150 | 0.942 |
| 50 | 14.834 | 17.511 | 0.847 |
| 60 | 25.183 | 32.618 | 0.772 |
| 70 | 35.900 | 50.473 | 0.711 |
| 80 | 46.984 | 71.073 | 0.661 |

The two agree in sign and in order of magnitude and disagree by up to about
$50\%$ at the largest tabulated thickening (the scale is $1/0.661 = 1.51$ times
the exact value at $t_c = 80\ \mathrm{km}$). The difference has a physical
name: **the isostatic root**. Part of a thickened column replaces mantle rather
than adding mass above the Moho, so the buoyancy force is smaller than a naive
"column height squared" estimate. Using
$\Gamma_{\text{scale}}$ in a force balance therefore biases the implied
stresses upward by a factor of $1.5$ at $\Delta t_c = 45\ \mathrm{km}$ and by
$12\%$ at $\Delta t_c = 10\ \mathrm{km}$.

**Conversion to stress.** Dividing a force per unit length by a length gives a
stress. Across a belt of width $L = 250\ \mathrm{km}$,
$\Gamma/L = 3.59\times10^{13}/2.5\times10^{5} =
1.4\times10^{8}\ \mathrm{Pa} = 0.14\ \mathrm{GPa}$ of mean deviatoric stress is
available to drive spreading. That is the number to compare with rock strength.

## 3. Collapse: the dimensionless group that decides

Balance the buoyancy stress against a viscous stress for a body of thickness $H$
deforming at strain rate $\dot\varepsilon = V/L$:

$$
\rho_m\text{-buoyancy}:\ \tau_b \sim \rho_c g\,\Delta e,
\qquad
\text{viscous}:\ \tau_v \sim \frac{\eta V}{H}.
$$

Setting them equal gives the Stokes velocity and the collapse (spreading) time

$$
V = \frac{\rho_c g\,\Delta e\,H}{\eta}, \qquad
\boxed{\;\tau_c = \frac{L}{V} = \frac{\eta L}{\rho_c g\,\Delta e\,H}\;}
$$

and the dimensionless group is their ratio

$$
\Pi \equiv \frac{\tau_b}{\tau_v} = \frac{\rho_c g\,\Delta e\,H}{\eta V}.
$$

$\Pi = 1$ defines the boundary: if the buoyancy stress exceeds what the viscosity
can sustain at the imposed deformation rate, the belt spreads. Because $V$ is
itself determined by the balance, the more useful form is the time
$\tau_c$: a belt spreads if the available geological time exceeds it.

For the SYNTHETIC plateau ($\Delta e = 5.571\ \mathrm{km}$,
$H = 70\ \mathrm{km}$, $L = 250\ \mathrm{km}$):

| $\eta$ (Pa s) | $10^{20}$ | $10^{21}$ |
|---|---|---|
| $\tau_c$ (Myr) | 0.07 | 0.74 |

and the viscosity required for a chosen collapse time is

| collapse time (Myr) | 1 | 10 | 50 | 100 |
|---|---|---|---|---|
| required $\eta$ (Pa s) | $1.35\times10^{21}$ | $1.35\times10^{22}$ | $6.76\times10^{22}$ | $1.35\times10^{23}$ |

**Read those numbers carefully.** A geologically slow collapse —
tens of millions of years — requires an effective viscosity of
$10^{22}$–$10^{23}\ \mathrm{Pa\,s}$, two to three orders of magnitude above the
$10^{19}$–$10^{20}\ \mathrm{Pa\,s}$ inferred for lower-crustal channel flow. The
gap is not a nuisance: it is the observation that a plateau like the SYNTHETIC
one is not a viscous blob cooling and spreading, because the strong upper crust
and the mantle lithosphere carry the load. Any model that assigns the whole
plateau the channel viscosity predicts its destruction in
$\lesssim 10^5\ \mathrm{yr}$, which is falsified by the existence of the
topography. The honest statement is that $\tau_c$ is a **scale**, and its
usefulness is that it identifies which parameter the answer is most sensitive
to.

## 4. Erosion and isostatic rebound

Erosion removes rock from the top. Isostasy then compensates, so the surface
falls by much less than the thickness removed:

$$
\Delta e = h\left(1 - \frac{\rho_c}{\rho_m}\right) = 0.1592\,h,
$$

where $h$ is the eroded thickness. Only $15.9\%$ of the erosion becomes net
elevation loss; the rest is cancelled by the root rising. Equivalently, to level
a plateau standing $e$ above the reference requires

$$
h = \frac{e}{1 - \rho_c/\rho_m} = 6.28\,e ,
$$

which the demonstration confirms: a $5.571\ \mathrm{km}$ plateau needs
$35.0\ \mathrm{km}$ of erosion. The amplification factor
$\rho_m/(\rho_m-\rho_c) = 6.283$ is the reason erosion is a weak way to destroy
topography and the reason thermochronology is needed to measure exhumation
rates independently of the elevation record. Erosion of $1\ \mathrm{km}$ lowers
the surface by only $0.159\ \mathrm{km}$ while the Moho rises by
$1.159\ \mathrm{km}$, because the Moho depth changes by
$-\Delta e - h = -(0.1592 + 1)\,h$.

## 5. Why elevation alone cannot give a crustal thickness

Elevation responds to *any* density anomaly in the lithospheric column, not just
to crustal thickness. The cheapest alternative is the mantle lithosphere.
Removing a cold lid of thickness $L_{\text{lid}}$ with a mean temperature
deficit $T_m/2$, and replacing it with asthenosphere, raises the surface by

$$
\Delta e = \frac{\rho_m\alpha (T_m/2) L_{\text{lid}}}
{\rho_m - \rho_w} = 0.0282\,L_{\text{lid}} .
$$

| lid removed (km) | uplift (km) | equivalent crustal thickening (km) |
|---|---|---|
| 25 | 0.706 | 4.43 |
| 50 | 1.412 | 8.87 |
| 100 | 2.823 | 17.74 |
| 150 | 4.235 | 26.61 |

**Removing $100\ \mathrm{km}$ of cold mantle lithosphere explains
$2.8\ \mathrm{km}$ of elevation with no crustal thickening at all.** Since
$2.8\ \mathrm{km}$ is half the height of the SYNTHETIC plateau, the ambiguity is
not a technicality: the same topography can be produced by thickening the crust,
by thinning the mantle lithosphere, or by any convex combination. Breaking the
degeneracy needs an independent measurement of crustal thickness — receiver
functions, wide-angle refraction, or gravity modelling with an assumed density
contrast.

## 6. Assumptions and regime of validity

1. **Local (Airy) compensation.** A lithosphere with finite elastic thickness
   supports part of a load regionally, so the elevation for a given thickening
   is smaller and the transition is smoothed over the flexural wavelength. Airy
   is the $T_e \to 0$ limit
   ([13-06-01](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md)).
2. **Constant crustal and mantle densities.** A real crust densifies with depth
   and with metamorphic grade; the elevation-to-thickness factor $0.1592$ is
   then a weighted average, not a constant.
3. **Plane strain and volume conservation.** Shortening is recovered from
   thickening only in a closed 2-D section. Out-of-section flow and erosion
   violate it. In the SYNTHETIC numbers, $50\%$ shortening for a $70\
   \mathrm{km}$ crust is a model result under those assumptions.
4. **A Newtonian, spatially uniform viscosity.** Real lithospheres are
   power-law, layered (strong mantle lithosphere, weak lower crust) and
   transiently elastic. Using one $\eta$ in $\tau_c$ is a scaling argument, not a
   solution of the momentum equation; the demonstration's numbers show how
   sensitively the conclusion depends on it.
5. **No magmatism, no phase changes, no crustal flow into or out of the
   section.** Lower-crustal flow is exactly the mechanism invoked for plateau
   margins, and it violates the closed-section assumption.
6. **Erosion rate constant in time.** Real erosion decays as relief is consumed,
   which makes the rebound feedback self-limiting.
7. **The buoyancy force is computed from a 1-D column comparison.** The
   horizontal force in a real belt also depends on the along-strike geometry,
   and a 2-D balance in the horizontal plane is needed to convert it into a
   spreading rate.

## 7. Worked example — from elevation to force to collapse time

Take a SYNTHETIC plateau with $t_c = 70\ \mathrm{km}$ and $e = 5.571\ \mathrm{km}$.

1. **Root.** Moho depth $= e + t_c = 75.6\ \mathrm{km}$; the crustal root below
   the reference Moho is $75.6 - 35.0 = 40.6\ \mathrm{km}$.
2. **Shortening.** $\beta = 70/35 = 2.0$, so $50\%$ shortening — if the section
   is closed.
3. **Buoyancy force.** $\Gamma = 3.590\times10^{13}\ \mathrm{N\,m^{-1}}$
   (demonstration). Across $L = 250\ \mathrm{km}$ the mean available deviatoric
   stress is $0.14\ \mathrm{GPa}$.
4. **Collapse time.** With $H = 70\ \mathrm{km}$ and
   $\eta = 10^{21}\ \mathrm{Pa\,s}$:
   $\rho_c g\,\Delta e\,H = 2800\times9.81\times5571\times7\times10^{4}
   = 1.071\times10^{13}\ \mathrm{Pa\,m}$, and
   $\tau_c = 10^{21}\times2.5\times10^{5}/1.071\times10^{13}
   = 2.33\times10^{13}\ \mathrm{s} = 0.74\ \mathrm{Myr}$.
5. **Viscosity for a $50\ \mathrm{Myr}$ collapse.**
   $\eta = \tau_c\,\rho_c g\,\Delta e\,H/L
   = 1.578\times10^{15}\times1.071\times10^{13}/2.5\times10^{5}
   = 6.8\times10^{22}\ \mathrm{Pa\,s}$.

The fifth number is the one to carry away: it is what the SYNTHETIC geometry
requires, and it is two to three orders of magnitude above crustal-channel
viscosities. A model that closes that gap by lowering the viscosity must then
explain why the topography still exists.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC plateau has $t_c = 60\ \mathrm{km}$ over a $35\ \mathrm{km}$
> reference crust, with the lesson's densities. **(a)** Compute $e$ and the Moho
> depth. **(b)** Compute the shortening required under volume conservation.
> **(c)** Estimate the collapse time for $L = 200\ \mathrm{km}$,
> $H = 60\ \mathrm{km}$ and $\eta = 10^{21}\ \mathrm{Pa\,s}$, and state what
> viscosity a $30\ \mathrm{Myr}$ lifetime would require. **(d)** An independent
> receiver-function study reports a Moho at $52\ \mathrm{km}$. Using the
> mantle-lithosphere alternative, explain how much cold lithosphere would have
> to have been removed to reconcile the same elevation with a $50\
> \mathrm{km}$ crust. **(e)** State one observation that would break the
> degeneracy.

## Common pitfalls

1. **Reading crustal thickness from elevation.** Half of a SYNTHETIC
   plateau's $5.6\ \mathrm{km}$ is explicable by a mantle-lithosphere effect
   alone (Section 5).
2. **Using $\Gamma_{\text{scale}} = g\rho_c(t^{2}-t_0^{2})/2$ in a stress
   balance.** It overestimates the buoyancy force by up to a factor $1.5$ at
   $\Delta t_c = 45\ \mathrm{km}$ ($12\%$ at $\Delta t_c = 10\ \mathrm{km}$),
   because it ignores the isostatic root.
3. **Quoting a collapse time without the viscosity.** $\tau_c \propto \eta$;
   the demonstration spans three orders of magnitude in $\tau_c$ over three in
   $\eta$.
4. **Forgetting the rebound factor.** Levelling $5.57\ \mathrm{km}$ requires
   $35\ \mathrm{km}$ of erosion, not $5.57\ \mathrm{km}$.
5. **Assuming the shortening is unique.** Volume conservation in a closed
   section is an assumption; out-of-section flow and erosion both change the
   answer, and neither is visible in the elevation.
6. **Treating a 1-D column balance as a 2-D force balance.** The force per unit
   length is a boundary condition for a spreading model, not the model itself.

## Related modules

- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  why local isostasy is an approximation.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md).
- [13-07-01 Erosion, Uplift and Thermochronology](../07-geomorphology-tectonics-climate/01-erosion-and-uplift.md) —
  the measurement that replaces the rebound argument.
- [13-03-04 Basin Formation and Subsidence Modelling](04-basin-geodynamics.md) —
  where the eroded material ends up.
- [04-04-03 Folds](../../04-earth-science-geology/04-structural-geology/03-folds.md) —
  how shortening is accommodated in the brittle upper crust.
- [12-03-01 Radiogenic Heat](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md) —
  what sets the temperature, and therefore the viscosity, that appears in
  $\tau_c$.
