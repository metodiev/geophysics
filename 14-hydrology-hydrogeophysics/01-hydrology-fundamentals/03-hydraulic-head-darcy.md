---
id: 14-01-03
title: "Hydraulic Head, Darcy's Law and Groundwater Flow"
level: advanced
prereqs: ["14-01-02", "02-06-05", "01-05-02"]
tags: [hydrology, hydrogeophysics, hydraulic-head, darcy, groundwater-flow, dupuit, diffusivity]
---

# Hydraulic Head, Darcy's Law and Groundwater Flow

Two ideas carry all of groundwater hydrology. The first is that water flows
because of a **difference in head**, not because of a difference in depth or
pressure alone. The second is that the flux is **proportional to the gradient** —
Darcy's law, a phenomenological relation with a stated regime of validity that
this lesson actually measures.

Everything after this lesson in the folder is a consequence: well hydraulics
([04](04-well-hydraulics.md)) solves the flow equation with a pumping boundary
condition; contaminant transport adds advection to the velocity derived here;
every hydrogeophysical method in
[module 14-02](../02-hydrogeophysics-methods/README.md) is used to estimate $K$,
$S$ or their spatial distribution, precisely because head data alone cannot.

**All models and data in this module are SYNTHETIC.** The wells, heads,
conductivities, recharge rates and column tests below are invented teaching
values. Physical constants of water are listed with units where used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** hydraulic head from Bernoulli's equation and **compute** it from a
   measured pressure and elevation.
2. **Derive** Darcy's law in both conductivity and intrinsic-permeability forms,
   and **convert** between specific discharge and average linear velocity.
3. **Test** the validity of Darcy's law with a grain-scale Reynolds number, and
   **quantify** where a quadratic (Forchheimer) correction exceeds a stated error.
4. **Apply** the tangent law for flow refraction at a conductivity contrast and
   **explain** the direction of refraction.
5. **Derive** the transient groundwater flow equation and **compute** the
   hydraulic diffusivity $D = T/S$, with the timescale to a stated distance.
6. **Solve** the Dupuit water-table problem analytically and **verify** the
   solution against a finite-difference solution to machine precision.
7. **Demonstrate** that a head field constrains only the ratio $R/K$ and **state**
   what additional measurement breaks the ambiguity.

## Prerequisites

- [14-01-02 Aquifers, Porosity, Permeability and Storativity](02-aquifer-types-and-properties.md)
  — $K$, $k$, $T$, $S$ and their definitions.
- [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md)
  — viscous flow through a granular medium, from which Darcy's law is motivated.
- [01-05-02 Derivatives](../../01-mathematics/05-single-variable-calculus/02-derivatives.md)
  — the gradient and the linearisation used throughout.

---

## 1. Hydraulic head: one number that decides everything

Water in a porous medium moves from where its mechanical energy per unit weight is
high to where it is low. Bernoulli's equation for a fluid element gives that
energy per unit weight as

$$h = z + \frac{p}{\rho_w g} + \frac{v^{2}}{2g},$$

with $z$ the elevation above a datum, $p$ the pressure, $\rho_w$ the density,
$g$ gravity and $v$ the speed. In groundwater the kinetic term is negligible:

$$v \sim 10^{-6}\ \mathrm{m\,s^{-1}} \;\Longrightarrow\;
\frac{v^{2}}{2g} \sim \frac{10^{-12}}{2 \times 9.81} \approx 5 \times 10^{-14}\
\mathrm{m},$$

thirteen orders of magnitude below a head difference of a metre. Hence the working
definition:

$$\boxed{\;h = z + \frac{p}{\rho_w g}\qquad \text{[m of water]}.}$$

**Synthetic example.** A piezometer is screened at $z = -30.0\ \mathrm{m}$ (below
the datum) and reads $p = 4.00 \times 10^{5}\ \mathrm{Pa}$:

$$\frac{p}{\rho_w g} = \frac{4.00 \times 10^{5}}{1000 \times 9.81}
= 40.775\ \mathrm{m}, \qquad h = -30.0 + 40.775 = +10.775\ \mathrm{m}.$$

The head is *higher than the ground surface datum*, so water would rise 10.8 m
above the datum if the piezometer were open — the point is confined and artesian.
Two more readings from the same synthetic borehole illustrate the point that head
is not depth: at $z = -30.0\ \mathrm{m}$ with $p = 3.00 \times 10^{5}\ \mathrm{Pa}$,
$h = 0.581\ \mathrm{m}$; at $z = -10.0\ \mathrm{m}$ with
$p = 5.00 \times 10^{4}\ \mathrm{Pa}$, $h = -4.903\ \mathrm{m}$; and at
$z = -5.0\ \mathrm{m}$ in the saturated zone at atmospheric pressure (a water
table), $h = -5.000\ \mathrm{m} = z$. **At a water table the head equals the
elevation**, because $p = 0$ gauge.

### 1.1 What a head measurement requires

Head is a *potential* only for the connected water at the measurement point. Three
failure modes recur:

- **Mixed water.** A screen spanning two aquifers with different heads records a
  weighted average, which is not the head of either.
- **Unsaturated or disconnected water.** Water held by suction above the water
  table has $p < 0$; the formula still returns a number, but it is not a potential
  driving regional flow (see [06 The Unsaturated Zone](06-unsaturated-zone.md)).
- **Density variations.** $h$ assumes a single $\rho_w$. Where salinity varies, the
  correct potential is a freshwater head or a pressure potential:
  $p/\rho(z) g$ with the local density, or the equivalent-freshwater head
  $h_f = z + p/(\rho_f g)$ (see [05 Groundwater Chemistry and Salinity](05-groundwater-chemistry.md)).

## 2. Darcy's law, in the two forms you will need

In one dimension, over a column of cross-sectional area $A$ carrying a volumetric
flow rate $Q$ under a head gradient $\mathrm{d}h/\mathrm{d}x$:

$$Q = -K A \frac{\mathrm{d}h}{\mathrm{d}x}
\qquad\Longleftrightarrow\qquad
q \equiv \frac{Q}{A} = -K\frac{\mathrm{d}h}{\mathrm{d}x},$$

where $q$ is the **specific discharge** (also called the Darcy flux or Darcy
velocity) [m s$^{-1}$]. The minus sign says flow is down-gradient. Written with
fluid properties exposed and using intrinsic permeability $k$:

$$q = -\frac{k}{\mu_w}\left(\frac{\partial p}{\partial x} + \rho_w g
\frac{\partial z}{\partial x}\right),$$

with $\mu_w$ the dynamic viscosity. Comparing with the head form gives the
conversion derived in
[02](02-aquifer-types-and-properties.md): $K = k\rho_w g/\mu_w$.

**Specific discharge is not a particle velocity.** $q$ is the volume crossing a
unit *total* area per unit time, including the area occupied by solids. A
conservative tracer moves through the pores, so its **average linear velocity** is

$$v = \frac{q}{n_e},$$

with $n_e$ the effective porosity. With $q = 3.0 \times 10^{-7}\
\mathrm{m\,s^{-1}}$ and $n_e = 0.25$, $v = 1.2 \times 10^{-6}\ \mathrm{m\,s^{-1}}$
— four times faster than $q$, and still a *mean* over a pore network in which
individual pathways differ by orders of magnitude.

**Synthetic well pair, worked.** Two piezometers 100 m apart read
$h_1 = 32.00$ m and $h_2 = 31.40$ m, in a unit with
$K = 5.0 \times 10^{-5}\ \mathrm{m\,s^{-1}}$, $n_e = 0.25$:

$$i = \frac{h_1 - h_2}{L} = \frac{0.60}{100} = 0.00600 \ \text{(dimensionless)},$$
$$q = K i = 5.0 \times 10^{-5} \times 0.00600 = 3.00 \times 10^{-7}\
\mathrm{m\,s^{-1}} = 0.0259\ \mathrm{m\,d^{-1}},$$
$$v = \frac{q}{n_e} = 1.20 \times 10^{-6}\ \mathrm{m\,s^{-1}}
= 0.1037\ \mathrm{m\,d^{-1}},$$
$$t = \frac{L}{v} = \frac{100}{0.1037} = 964\ \mathrm{d} = 2.64\ \mathrm{yr}.$$

Through a $10\ \mathrm{m} \times 5\ \mathrm{m}$ cross-section, the volumetric rate
is $q A = 3.0 \times 10^{-7} \times 50 = 1.50 \times 10^{-5}\
\mathrm{m^3\,s^{-1}} = 1.296\ \mathrm{m^3\,d^{-1}}$. Note how modest these numbers
are: a metre per day of *specific discharge* is enormous for natural groundwater,
and the tracer velocity — the one that matters for contamination — is larger still.

## 3. When is Darcy's law valid? A measured criterion

Darcy's law is not a law of nature; it is the laminar limit of flow through a
granular medium. The standard test is a **grain-scale Reynolds number**

$$\mathrm{Re} = \frac{\rho_w\, q\, d}{\mu_w},$$

with $d$ a representative grain diameter. For $d = 0.30\ \mathrm{mm}$ and water at
$20\ ^\circ\mathrm{C}$:

| $q$ (m s$^{-1}$) | $q$ (m d$^{-1}$) | Re | Darcy valid ($\mathrm{Re} < 1$)? |
|---|---|---|---|
| $3.0 \times 10^{-7}$ | 0.0259 | $8.98 \times 10^{-5}$ | yes |
| $1.0 \times 10^{-5}$ | 0.864 | $2.99 \times 10^{-3}$ | yes |
| $3.0 \times 10^{-4}$ | 25.9 | $8.98 \times 10^{-2}$ | yes |
| $1.0 \times 10^{-3}$ | 86.4 | $2.99 \times 10^{-1}$ | yes |
| $3.34 \times 10^{-3}$ | 288.6 | $1.00$ | no |
| $1.0 \times 10^{-2}$ | 864 | $2.99$ | no |

$\mathrm{Re} = 1$ occurs at $q = \mu_w/(\rho_w d) = 3.34 \times 10^{-3}\
\mathrm{m\,s^{-1}}$, which for this sand requires a gradient
$i = q/K = 3.34 \times 10^{-3}/5.0 \times 10^{-5} = 66.8$ — larger than 1, i.e.
physically impossible over any natural distance. **For fine and medium sands,
natural groundwater flow is always in the Darcy regime.** The regime is reached in
coarse gravel ($d = 10\ \mathrm{mm}$ reaches $\mathrm{Re} = 1$ at
$q = 1.0 \times 10^{-4}\ \mathrm{m\,s^{-1}}$, a realistic gravel flux), in karst
conduits, in fractures, and in the immediate vicinity of a pumped well.

### 3.1 The Forchheimer correction and where linearity actually breaks

A widely used extension adds a quadratic term:

$$i = \frac{\mu_w}{k \rho_w g} q + c\, q^{2}.$$

With synthetic values $k = 1.0 \times 10^{-11}\ \mathrm{m^2}$ and
$c = 2.0 \times 10^{5}\ \mathrm{s^2\,m^{-2}}$, the excess of the true gradient over
the linear prediction is 0.0% at $q = 10^{-5}$, 1.0% at
$5 \times 10^{-4}$, 3.9% at $2 \times 10^{-3}$ and 9.8% at
$5 \times 10^{-3}\ \mathrm{m\,s^{-1}}$ (441 m d$^{-1}$). The 10% threshold is
reached at $\mathrm{Re} = 1.53$: **within a factor of two of the $\mathrm{Re} = 1$
rule, but not equal to it.** The honest statement therefore names both the
criterion and the error it buys, because the criterion is a convention. $c$ is a
model parameter, not a universal constant, and must be stated.

## 4. Refraction of flow at a conductivity contrast

At a boundary between two layers, the component of $q$ normal to the boundary is
continuous (water is conserved) and the head is continuous. Writing both
requirements in terms of the tangential components gives a **tangent law**, the
analogue of Snell's law in optics:

$$\frac{\tan\theta_2}{\tan\theta_1} = \frac{K_2}{K_1},$$

with $\theta$ measured from the boundary normal. For a synthetic sand
($K_1 = 5.0 \times 10^{-4}\ \mathrm{m\,s^{-1}}$) over a silt
($K_2 = 1.0 \times 10^{-6}\ \mathrm{m\,s^{-1}}$, a 500-fold contrast):

| $\theta_1$ (deg) | $\theta_2$ (deg) |
|---|---|
| 5.0 | 0.010 |
| 15.0 | 0.031 |
| 45.0 | 0.115 |
| 75.0 | 0.428 |

Flow entering the low-conductivity layer is turned **towards the normal**, so an
almost horizontal flow in the sand becomes essentially vertical across the silt.
The reverse case (flow leaving a silt into a sand) turns flow towards the
boundary — which is why a permeable sand layer under a silty cover gathers
recharge over a wide area and transmits it along its length.

This refraction is the physical basis of two practical facts: a low-conductivity
clay layer spreads and delays recharge (its vertical $K$ controls leakage), and a
high-conductivity channel focuses flow, so head contours in a heterogeneous aquifer
are not the flow lines of a homogeneous one.

## 5. The flow equation and hydraulic diffusivity

Combine three statements over a control volume: Darcy's law gives the flux,
conservation of mass gives $\nabla \cdot \mathbf{q} = -S_s \partial h/\partial t +
W$ (with $W$ a source per unit volume), and the two together give the transient
groundwater flow equation. In the depth-integrated form used in hydrogeology,

$$S\frac{\partial h}{\partial t} = \nabla \cdot \left(T \nabla h\right) + W',
\qquad T = Kb, \quad S = S_s b \ \text{(confined)} \ \text{or} \ S_y\
\text{(unconfined)}.$$

For uniform $T$ this is a diffusion equation with **hydraulic diffusivity**

$$D = \frac{T}{S}\ [\mathrm{m^2\,s^{-1}}],$$

and the characteristic distance a head change has reached after time $t$ is
$L \sim \sqrt{4Dt}$, so $t \sim L^{2}/(4D)$.

**Synthetic comparison, same transmissivity $T = 198.7\ \mathrm{m^2\,d^{-1}}$:**

| Case | $S$ | $D$ (m$^2$ d$^{-1}$) | time to 1 km | time to 10 km |
|---|---|---|---|---|
| confined, stiff rock | $3.267 \times 10^{-4}$ | $6.08 \times 10^{5}$ | 0.411 d | 41.1 d |
| confined, soft rock | $1.504 \times 10^{-3}$ | $1.32 \times 10^{5}$ | 1.89 d | 189 d |
| unconfined | $0.20$ | $993.5$ | 252 d | 25,164 d (69 yr) |

The confined aquifer transmits a head change 600 times faster than the unconfined
one *with the same transmissivity and the same geometry*, because a confined
response requires almost no water to move. This is why confined aquifers show
seasonal pressure responses to distant recharge and to earth tides, while an
unconfined water table responds locally and slowly. It is also why a $1\ \mathrm{km}$
drawdown radius in a confined aquifer is not evidence of a $1\ \mathrm{km}$
disturbance of the water resource.

## 6. Worked example — the Dupuit water table, solved and verified

For steady one-dimensional unconfined flow with uniform recharge $R$, the
depth-averaged (Dupuit) equation is

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(K h \frac{\mathrm{d}h}{\mathrm{d}x}\right)
+ R = 0.$$

Since $h\,\mathrm{d}h/\mathrm{d}x = \tfrac{1}{2}\mathrm{d}(h^{2})/\mathrm{d}x$,
the equation is **linear in** $u = h^{2}$:

$$\frac{\mathrm{d}^{2}u}{\mathrm{d}x^{2}} = -\frac{2R}{K},
\qquad
u(x) = h_1^{2} + \frac{R}{K}x(L - x) \quad \text{for } h(0) = h(L) = h_1.$$

**Synthetic numbers.** $K = 5.0 \times 10^{-5}\ \mathrm{m\,s^{-1}}$,
$R = 1.00\ \mathrm{mm\,d^{-1}} = 1.157 \times 10^{-8}\ \mathrm{m\,s^{-1}}$,
$L = 1000$ m, $h_1 = 20.0$ m:

$$\frac{R}{K} = 2.3148 \times 10^{-4},$$
$$u_{\text{mid}} = 20.0^{2} + 2.3148 \times 10^{-4}(500)(500)
= 400 + 57.87 = 457.87\ \mathrm{m^2},$$
$$h_{\text{mid}} = \sqrt{457.87} = 21.398\ \mathrm{m}, \qquad
\text{rise} = 1.398\ \mathrm{m}.$$

The common small-rise approximation, obtained by linearising
$\sqrt{h_1^2 + \Delta u} \approx h_1 + \Delta u/(2h_1)$ and using
$\Delta u = RL^{2}/(4K)$, is

$$\Delta h \approx \frac{R L^{2}}{8 K h_1}
= \frac{1.157 \times 10^{-8} \times 10^{6}}{8 \times 5.0 \times 10^{-5} \times 20}
= 1.447\ \mathrm{m},$$

$3.5\%$ **high** relative to the exact $1.398\ \mathrm{m}$. The approximation is
excellent for a small rise and degrades as the rise becomes comparable with $h_1$;
state which form you used.

**Verification.** A finite-difference solution of $u'' = -2R/K$ on 201 nodes with
$h$ fixed at both ends gives a maximum deviation from the analytic parabola of
$6.4 \times 10^{-14}\ \mathrm{m}$ — machine precision — and closes the budget to
$3.5 \times 10^{-14}$ relative: total recharge across the section
($1.000\ \mathrm{m^2\,d^{-1}}$) equals the sum of the two boundary outflows. The
verification validates the **discretisation**, not Dupuit's assumptions.

### 6.1 The non-uniqueness you must not hide

Look again at the solution: it depends on $R$ and $K$ **only through the ratio**
$R/K$. The demonstration evaluates four parameter pairs with
$R/K = 2.3148 \times 10^{-4}$ ($K$ from $10^{-5}$ to $5 \times 10^{-4}\
\mathrm{m\,s^{-1}}$, $R$ from 0.2 to 10 mm d$^{-1}$). Every pair reproduces the
same water table to $0\ \mathrm{m}$ — to machine precision — while the discharge
across the section differs by a **factor of 50**.

This is the central inverse-theory fact of groundwater hydrology: **a head field
does not determine the conductivity and the recharge separately.** What breaks the
ambiguity is a flux measurement (streamflow gain between two gauges fixes $R$), or
an independent $K$ (a pumping test — [04](04-well-hydraulics.md)), or a geophysical
estimate of $K$ or of the water content ([module 14-02](../02-hydrogeophysics-methods/README.md)).
Any model calibrated on heads alone is calibrated on $R/K$ and should say so.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| head | $h$ | m | $z$ + pressure head |
| pressure head | $p/(\rho_w g)$ | m | Pa / (kg m$^{-3}$ · m s$^{-2}$) |
| gradient | $i$ | – | m/m |
| specific discharge | $q$ | m s$^{-1}$ | $K i$ |
| average linear velocity | $v$ | m s$^{-1}$ | $q/n_e$ |
| transmissivity | $T$ | m$^2$ s$^{-1}$ | $Kb$ |
| storativity | $S$ | – | |
| diffusivity | $D$ | m$^2$ s$^{-1}$ | $T/S$ |
| Reynolds number | Re | – | $\rho_w q d/\mu_w$ |

The one that catches people: $T/S$ is m$^2$ s$^{-1}$ because $S$ is dimensionless.
Reporting $D$ in m s$^{-1}$ (forgetting that $S$ is a ratio) makes every diffusion
time wrong by the value of $S$ itself — a factor of $3 \times 10^{-4}$ or $0.2$,
six orders of magnitude apart.

## 8. Python demonstration

`code/hydraulic_head_darcy_demo.py` prints all of the above with units. It:

1. computes head for four pressure/elevation pairs, including a water table and an
   artesian case;
2. converts a head gradient into $q$, $v$ and a travel time, and computes a
   volumetric flux;
3. tabulates $\mathrm{Re}$ over six decades of $q$ and locates $\mathrm{Re} = 1$;
4. fits a Forchheimer model and finds the flux at which the excess over linearity
   reaches 10% ($5.107 \times 10^{-3}\ \mathrm{m\,s^{-1}}$, 441 m d$^{-1}$,
   $\mathrm{Re} = 1.53$);
5. applies the tangent law across a 500-fold conductivity contrast;
6. tabulates hydraulic diffusivity and diffusion times for three storage cases;
7. verifies a Dupuit water table against a finite-difference solution
   ($6.4 \times 10^{-14}\ \mathrm{m}$ maximum deviation, closure
   $3.5 \times 10^{-14}$);
8. demonstrates the $R/K$ non-uniqueness: identical heads, outflows differing by
   50×.

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydraulic_head_darcy_demo.py
```

## 9. Assumptions and regime of validity

1. **Laminar flow.** $q$ small enough that $\mathrm{Re} \ll 1$ at the grain scale.
   Fails in gravel, karst, fractures, and near a pumping well.
2. **Constant density and viscosity.** Non-vertical salinity gradients in
   [05](05-groundwater-chemistry.md) and temperature gradients in a geothermal
   setting both break the simple head potential.
3. **Saturated, connected pore water.** Above the water table the same formula
   gives a number, not a potential.
4. **Isotropic $K$ (or an explicitly anisotropic tensor).** For a layered aquifer,
   the effective conductivity depends on flow direction (see
   [02](02-aquifer-types-and-properties.md) §3.5); a scalar $K$ is a modelling
   decision.
5. **Rigid, non-deforming matrix over the timescale of interest.** Subsidence,
   compaction and poroelastic coupling break the simple relation between storage
   change and head change ($\alpha$ is then stress-path dependent).
6. **Dupuit assumptions** (Section 6): the water table is gently sloping, vertical
   flow is neglected, and there is no seepage face at the outlet. The larger the
   rise relative to the saturated thickness, the worse the approximation — the
   small-rise form was already 3.5% high at a 1.4 m rise on a 20 m thickness.
7. **Continuum representation.** $K$ is defined on a representative elementary
   volume. In a fractured rock, "the" conductivity may not exist at the scale of a
   borehole.

## Mastery checkpoint

A synthetic confined unit has $K = 2.0 \times 10^{-5}\ \mathrm{m\,s^{-1}}$,
$b = 20\ \mathrm{m}$, $S = 5.0 \times 10^{-4}$, and two piezometers 500 m apart read
$h_1 = 45.00$ m and $h_2 = 44.20$ m.

**(a)** Compute the gradient, specific discharge in m d$^{-1}$, and the average
linear velocity for $n_e = 0.20$. **(b)** Compute the travel time over the 500 m.
**(c)** Check Darcy's validity with $d = 0.4\ \mathrm{mm}$. **(d)** Compute $T$ and
the hydraulic diffusivity in m$^2$ d$^{-1}$, and the time for the head disturbance
to reach 5 km. **(e)** A colleague reports a recharge rate of 5 mm yr$^{-1}$
inferred from these two heads. What is wrong with the claim, and what would you
request?

## Common pitfalls

1. **Reading a gradient from depths instead of heads.** Two wells of different
   depth with the same water level have a head difference, and it is not related to
   the depth difference.
2. **Treating $q$ as the velocity of a contaminant.** Divide by $n_e$, and remember
   that even $v$ is an average over a distribution of pathways.
3. **Applying Darcy's law everywhere.** In gravel, karst and near a well, the
   quadratic correction matters; measure which regime you are in.
4. **Quoting $D$ in the wrong units.** $T/S$ is m$^2$ s$^{-1}$; $S$ is
   dimensionless.
5. **Reading a head field as a conductivity.** The head solution depends on $R/K$;
   the whole family in Section 6.1 is consistent with the same data.
6. **Ignoring density.** A fresh-water head computed in a saline aquifer can be
   wrong by metres; use an equivalent-freshwater head.
7. **Trusting a Dupuit solution with a large rise.** The approximation degrades
   exactly where it is most tempting (a large recharge mound).

## Related modules

- [04 Well Hydraulics and Pumping Tests](04-well-hydraulics.md) — the flow equation
  with a pumping well, and the measurement that breaks the $R/K$ ambiguity.
- [06 The Unsaturated Zone](06-unsaturated-zone.md) — the same physics with
  $p < 0$, where conductivity depends on the head itself.
- [02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — how $K$,
  $S$ and their variability are estimated where head data are silent.
- [02 Hydrogeophysical Methods: Borehole Geophysics](../02-hydrogeophysics-methods/07-borehole-hydrogeophysics.md)
  — the measurements that supply local $K$.
- [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md) —
  the continuum-mechanics derivation this lesson applies.

## Code and exercises

- Demonstration: [`code/hydraulic_head_darcy_demo.py`](code/hydraulic_head_darcy_demo.py)
- Exercises: [`exercises/03-hydraulic-head-darcy-exercises.md`](exercises/03-hydraulic-head-darcy-exercises.md)
- Worked solutions: [`exercises/03-hydraulic-head-darcy-solutions.md`](exercises/03-hydraulic-head-darcy-solutions.md)
