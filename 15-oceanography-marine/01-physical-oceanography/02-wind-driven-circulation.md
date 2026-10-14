---
id: 15-01-02
title: "Wind-Driven Circulation, Ekman Transport and Gyres"
level: advanced
prereqs: ["02-02-05", "02-06-02", "02-06-01"]
tags: [oceanography, marine-geophysics, wind-driven-circulation, coriolis, ekman, sverdrup, gyres]
---

# Wind-Driven Circulation, Ekman Transport and Gyres

> **All models and data in this module are SYNTHETIC.** The wind-stress field
> used here is a chosen teaching function, printed by the demonstration in
> `code/`. It is not a reanalysis, a buoy record or a satellite product, and no
> observed gyre, current or transport is reproduced.

A wind blowing across the sea surface pushes water. That much is obvious. What is
not obvious is that, on a rotating planet, the water does not move in the
direction of the wind, that the *depth-integrated* transport is exactly
perpendicular to the wind, and that the resulting ocean-wide circulation is
closed by a narrow, fast current on one side of the basin and a broad, slow drift
on the other.

Wind-driven circulation is the cleanest example in geophysics of a result that
follows from a single conserved quantity — the planetary vorticity $f$ — and the
reason it belongs in a curriculum about *measurement* is that almost none of it
is measured directly. What is measured are winds, sea-surface heights and
occasional hydrographic sections. Transports of tens of Sverdrups
($1\ \mathrm{Sv} = 10^{6}\ \mathrm{m^{3}\,s^{-1}}$) are inferred from a balance
of terms, and the inference carries every assumption that produced it.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $f = 2\Omega\sin\phi$ and $\beta = 2\Omega\cos\phi/R$ by
   differentiating the vertical component of the planetary vorticity, and
   **evaluate** both at a stated latitude with units.
2. **Derive** the Ekman transport $M = \tau/(\rho f)$ by integrating the
   momentum balance over the Ekman layer, and **state** the 90-degree rule and
   the hemisphere in which it reverses.
3. **Compute** the Ekman depth $D=\sqrt{2A_v/f}$ and the surface current of a
   constant-viscosity Ekman spiral, and **explain** why both depend on $A_v$
   while the transport does not.
4. **Derive** the Sverdrup balance $\beta V = (1/\rho)\,\mathrm{curl}_z\,\tau$
   from the depth-integrated vorticity equation, and **compute** the meridional
   transport from a stated wind-stress curl.
5. **Compute** the Stommel and Munk western-boundary-layer widths and **explain**
   why the boundary must be on the western side.
6. **Estimate** the Rossby-wave adjustment time for a basin and **state** why a
   wind-driven gyre is not in instantaneous equilibrium with the wind.
7. **Quantify** the error of the $\beta$-plane approximation over a stated
   meridional extent.

## Prerequisites

- [02-02-05 Rotational Dynamics and Angular Momentum](../../02-physics/02-classical-mechanics/05-rotation.md) —
  rotating frames and why a rotating frame produces apparent forces.
- [02-06-02 Conservation Laws in Fluids](../../02-physics/06-fluid-mechanics/02-conservation-fluid.md) —
  mass and momentum conservation in a continuum, and the vorticity equation.
- [02-06-01 Fluid Statics and Pressure](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  hydrostatic balance and the conversion of depth to pressure.

## 1. Why rotation changes the answer

Consider a wind stress $\tau$ applied to a homogeneous, non-rotating ocean. The
layer accelerates downwind until friction balances the stress; the transport is
downwind. That is not what the ocean does.

The reason is the **Coriolis acceleration** $-f\hat{z}\times\mathbf{u}$, which
acts perpendicular to the velocity. It cannot do work, and it cannot be switched
off: it sits in the momentum equation as an acceleration per unit mass of
magnitude $f|\mathbf{u}|$. For a current of $0.1\ \mathrm{m\,s^{-1}}$ at
$30^\circ$N, $f|\mathbf{u}| = 7.29\times10^{-6}\ \mathrm{m\,s^{-2}}$, which is
$7\times10^{-7}\,g$: three orders of magnitude below gravity, but *steady*, and
over the weeks an ocean responds on, it dominates everything except pressure.

Two consequences organise the whole lesson.

- **In the interior**, where friction is negligible, the momentum balance is
  between Coriolis and pressure: **geostrophy**. The flow is along contours of
  constant pressure and therefore nearly along contours of constant sea-surface
  height.
- **Near the surface**, where the wind stress acts, the balance is between
  Coriolis and the vertical divergence of stress: the **Ekman layer**, in which
  the transport is perpendicular to the wind.

## 2. The Coriolis parameter and its gradient

The planetary vorticity is the vertical component of the Earth's rotation vector:
$f = 2\Omega\sin\phi$, where $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$ is
the rotation rate and $\phi$ is latitude. Differentiating along a meridian of
length $y = R\phi$ (with $R$ the Earth radius),

$$\beta \equiv \frac{\partial f}{\partial y}
= 2\Omega\cos\phi\,\frac{\mathrm{d}\phi}{\mathrm{d}y}
= \frac{2\Omega\cos\phi}{R},$$

with units $\mathrm{m^{-1}\,s^{-1}}$. The demonstration prints, with
$R = 6.371\times10^{6}\ \mathrm{m}$:

| latitude | $f$ (s$^{-1}$) | $\beta$ (m$^{-1}$ s$^{-1}$) | inertial period $2\pi/|f|$ (h) |
|---|---|---|---|
| $0^\circ$ | 0 | $2.289\times10^{-11}$ | – |
| $15^\circ$ | $3.775\times10^{-5}$ | $2.211\times10^{-11}$ | 46.24 |
| $30^\circ$ | $7.292\times10^{-5}$ | $1.982\times10^{-11}$ | 23.93 |
| $45^\circ$ | $1.031\times10^{-4}$ | $1.619\times10^{-11}$ | 16.92 |
| $60^\circ$ | $1.263\times10^{-4}$ | $1.145\times10^{-11}$ | 13.82 |
| $75^\circ$ | $1.409\times10^{-4}$ | $5.925\times10^{-12}$ | 12.39 |

Two features of this table are the content of the lesson. First, at $30^\circ$N
the Coriolis parameter is *numerically equal to* $\Omega$
($f = 2\Omega\sin30^\circ = \Omega$); this makes $30^\circ$ the convenience
latitude of textbook arithmetic. Second, $\beta$ is **largest at the equator and
zero at the poles**: the equator is the one place where the variation of $f$ is
not a small correction to $f$ but the entire dynamics.

## 3. The Ekman layer

### 3.1 Derivation of the transport

Take the horizontal momentum balance for steady, homogeneous, horizontally
uniform flow driven by a surface stress $\tau$, with vertical eddy viscosity
$A_v$ (a turbulent closure, not a molecular property):

$$-fv = \frac{1}{\rho}\frac{\partial \tau_x}{\partial z}, \qquad
fu = \frac{1}{\rho}\frac{\partial \tau_y}{\partial z}.$$

Integrate from the surface $z=0$ downward past the layer where the stress
vanishes:

$$\int_{-\infty}^{0}\frac{\partial\tau_x}{\partial z}\,\mathrm{d}z
= \tau_x(\infty) - \tau_x(0) = -\tau_x(0).$$

Hence, writing $M_y = \int u\,\mathrm{d}z$ and $M_x = \int v\,\mathrm{d}z$ for the
depth-integrated transports (units $\mathrm{m^{2}\,s^{-1}}$):

$$-fM_y = -\frac{\tau_x(0)}{\rho} \;\Rightarrow\; M_y = \frac{\tau_x}{\rho f},
\qquad
fM_x = -\frac{\tau_y(0)}{\rho} \;\Rightarrow\; M_x = -\frac{\tau_y}{\rho f}.$$

In vector form the depth-integrated Ekman transport is

$$\boxed{\;\mathbf{M} = \frac{1}{\rho f}\,\hat{z}\times\boldsymbol{\tau}\;}$$

which is $\boldsymbol{\tau}$ rotated by $90^\circ$ to the **right** in the
northern hemisphere ($f>0$) and to the **left** in the southern hemisphere
($f<0$). With $\rho = 1025\ \mathrm{kg\,m^{-3}}$ and
$\tau = 0.10\ \mathrm{N\,m^{-2}}$:

| latitude | $f$ (s$^{-1}$) | $\tau$ (N m$^{-2}$) | $M$ (m$^{2}$ s$^{-1}$) | over 1000 km (Sv) |
|---|---|---|---|---|
| $30^\circ$N | $7.292\times10^{-5}$ | 0.10 | 1.338 | 1.34 |
| $45^\circ$N | $1.031\times10^{-4}$ | 0.10 | 0.946 | 0.95 |
| $30^\circ$S | $-7.292\times10^{-5}$ | 0.10 | $-1.338$ | $-1.34$ |
| $30^\circ$N | $7.292\times10^{-5}$ | $-0.10$ | $-1.338$ | $-1.34$ |

Transport over a coast is what drives upwelling: $1.34\ \mathrm{Sv}$ per
1000 km of coastline is a large coastal signal, and it changes sign with the
hemisphere for the same wind. That sign change is the reason eastern boundary
upwelling exists on both sides of the equator.

### 3.2 The spiral, the depth, and what $A_v$ controls

With constant $A_v$ the same balance has an explicit solution whose surface
value is at $45^\circ$ to the wind:

$$u + \mathrm{i}v = \frac{\tau}{\rho\sqrt{A_v f}}
\exp\!\left[(1+\mathrm{i})\frac{z}{D}\right], \qquad
D = \sqrt{\frac{2A_v}{f}},$$

where $D$ is the **e-folding depth** and the spiral has effectively died out by
$z \approx \pi D$. The surface speed is
$V_0 = \tau/(\rho\sqrt{A_v f})$. With $A_v = 0.010\ \mathrm{m^{2}\,s^{-1}}$ and
$\tau = 0.10\ \mathrm{N\,m^{-2}}$:

| latitude | $f$ (s$^{-1}$) | $D$ (m) | $\pi D$ (m) | $V_0$ (m s$^{-1}$) |
|---|---|---|---|---|
| $15^\circ$N | $3.775\times10^{-5}$ | 23.02 | 72.31 | 0.1588 |
| $30^\circ$N | $7.292\times10^{-5}$ | 16.56 | 52.03 | 0.1142 |
| $45^\circ$N | $1.031\times10^{-4}$ | 13.93 | 43.75 | 0.0961 |
| $60^\circ$N | $1.263\times10^{-4}$ | 12.58 | 39.53 | 0.0868 |

**The transport is independent of $A_v$.** The viscosity sets the depth and the
speed, and the three conspire so that $\int u\,\mathrm{d}z$ does not change.
This is a general and useful pattern: an integral of a balance is often more
robust than any of its terms. It is also a trap, because a wrong $A_v$ produces a
wrong *surface current* while leaving the transport — the quantity that matters
for basin-scale budgets — untouched. The demonstration verifies
$|M|_{\text{definition}} = |\tau|/(\rho|f|)$ to $0.00\times10^{0}$.

## 4. The Sverdrup balance

### 4.1 Derivation

Take the depth-integrated momentum equations for the interior with a wind-stress
forcing, cross-differentiate to eliminate pressure, and use continuity:

$$\frac{\partial V}{\partial y} = \frac{1}{\rho}\,\mathrm{curl}_z\,\boldsymbol{\tau}
\quad\text{combined with}\quad
\frac{\partial f}{\partial y}V + f\left(\frac{\partial U}{\partial x}
+ \frac{\partial V}{\partial y}\right) = \frac{1}{\rho}\,
\mathrm{curl}_z\,\boldsymbol{\tau},$$

and continuity removes the stretching term, leaving the **Sverdrup balance**

$$\boxed{\;\beta V = \frac{1}{\rho}\,\mathrm{curl}_z\,\boldsymbol{\tau}
= \frac{1}{\rho}\left(\frac{\partial \tau_y}{\partial x}
- \frac{\partial \tau_x}{\partial y}\right).\;}$$

The physics is a vorticity budget: the wind adds vorticity at the rate
$\mathrm{curl}_z\tau/\rho$, and a meridional flow moves water into latitudes where
the planetary vorticity differs, changing the column's vorticity at the rate
$\beta V$. In steady state the two must balance.

### 4.2 Numerical example — a synthetic gyre

Let $\tau_x(y) = \tau_0\cos(\pi y/L)$ with $\tau_0 = 0.10\ \mathrm{N\,m^{-2}}$ and
$L = 3000\ \mathrm{km}$, and let $\tau_y = 0$. Then
$\mathrm{curl}_z\tau = -\partial\tau_x/\partial y
= \tau_0(\pi/L)\sin(\pi y/L)$, and at $y = L/2$,

$$\mathrm{curl}_z\tau = 0.10 \times \frac{\pi}{3.0\times10^{6}}
= 1.047\times10^{-7}\ \mathrm{N\,m^{-3}},$$

$$V = \frac{1.047\times10^{-7}}{1025 \times 1.982\times10^{-11}}
= 5.153\ \mathrm{m^{2}\,s^{-1}}.$$

Across a $5000\ \mathrm{km}$ basin that is $25.8\ \mathrm{Sv}$ — the right order
for a subtropical gyre, obtained from a wind stress and a latitude. The
demonstration checks the analytic curl against a finite-difference estimate and
finds a maximum discrepancy of $3.3\times10^{-10}\ \mathrm{N\,m^{-3}}$, i.e.
$0.3\,\%$ of the curl, which is grid truncation error and decreases with spacing.

**The zero of the curl is as informative as its maximum.** Where
$\sin(\pi y/L) = 0$, at $y = 0$ and $y = L$, the meridional transport vanishes:
those are the latitudes where the interior flow must reverse. A gyre is therefore
two counter-rotating cells, not one, and the boundary between them is set by the
wind pattern, not by the bathymetry.

## 5. Western intensification

The Sverdrup balance gives the interior flow but not the return flow. The return
cannot be a mirror image of the interior, because $\beta$ is nonzero and the
vorticity budget is antisymmetric in $x$: friction must be invoked, and it
supplies a boundary layer whose thickness is set by which friction is used. In
this model

$$\delta_{\text{Stommel}} = \frac{r}{\beta} = 50.4\ \mathrm{km},
\qquad
\delta_{\text{Munk}} = \left(\frac{A_H}{\beta}\right)^{1/3} = 63.2\ \mathrm{km},$$

for bottom-drag coefficient $r = 1.0\times10^{-6}\ \mathrm{s^{-1}}$ and
horizontal viscosity $A_H = 5.0\times10^{3}\ \mathrm{m^{2}\,s^{-1}}$ at
$30^\circ$N. Both are tens of kilometres, against a basin of thousands: the
return flow is a narrow western boundary current. The **western** side is forced
by the sign of $\beta$: the boundary layer is only exponentially decaying on the
western margin, and on the eastern margin the same balance gives a growing
solution, which is rejected.

The practical consequence is worth stating plainly. The *width* of a western
boundary current is a property of the friction parameterisation, not of the wind,
and it is therefore one of the least robust outputs of a wind-driven model —
while the total interior transport is one of the most robust.

## 6. Adjustment: why the gyre is a slow response

The steady balances above describe an equilibrium that the ocean reaches through
long **Rossby waves**. The relevant speed is

$$c_R = \beta L_d^{2}, \qquad L_d = \frac{NH}{f},$$

with $N$ the buoyancy frequency, $H$ the depth and $L_d$ the Rossby radius. With
$N = 0.010\ \mathrm{rad\,s^{-1}}$, $H = 500\ \mathrm{m}$ and $f$ at $30^\circ$N:
$L_d = 68.6\ \mathrm{km}$, $c_R = 9.32\ \mathrm{cm\,s^{-1}}$, and the time to
cross a $5000\ \mathrm{km}$ basin is $1.70$ years.

Wind-driven gyres are therefore *not* in instantaneous equilibrium with the wind.
A change in the wind field is felt in the interior only after years, and a
"steady-state" gyre description is an average over that adjustment. This is the
measured reason to be careful with the word "steady".

## 7. Assumptions and regime of validity

1. **$\beta$-plane, and how good it is.** Replacing $f(y)$ by
   $f_0 + \beta y$ is a Taylor expansion valid for small meridional excursions.
   The demonstration measures the error over $\pm1500\ \mathrm{km}$ about
   $30^\circ$N: a maximum of $2.286\times10^{-6}\ \mathrm{s^{-1}} = 3.14\,\%$ of
   $f_0$. A $1\,\%$ error in $f$ is a $1\,\%$ error in Ekman transport, so a
   $3\,\%$ $f$-error is not negligible; the $\beta$-plane is a small-angle
   approximation in *latitude* and must not be used from pole to equator.
2. **Constant eddy coefficients.** $A_v$ and $A_H$ are closures. The
   demonstration shows the transport to be independent of $A_v$ and the boundary
   width to depend on both $A_v$ and $A_H$; any quantity that depends on them is
   model-dependent.
3. **Homogeneous (barotropic) interior.** No density stratification is carried.
   Real gyres are baroclinic, and the vertical structure of the transport is not
   given by this model.
4. **Linearised balance, small Rossby number.** Inertial terms $\mathbf{u}\cdot
   \nabla\mathbf{u}$ are dropped. The Rossby number
   $U/(fL) = 0.1/(7.3\times10^{-5}\times10^{5}) = 1.4\times10^{-2}$ for
   $U = 0.1\ \mathrm{m\,s^{-1}}$, $L = 100\ \mathrm{km}$ — small, so the
   approximation is good in the interior and fails in the boundary current.
5. **Steady or slowly varying.** The adjustment time of 1.7 years quantifies what
   "slowly" means.
6. **Closed basin with a rigid lid.** Sea-surface height is used diagnostically;
   there is no barotropic gravity-wave mode in the model.

## 8. Worked examples

### Example 1 — Ekman pumping from a wind curl

The vertical velocity at the base of the Ekman layer is
$w_E = \mathrm{curl}_z(\boldsymbol{\tau}/\rho f)$. At $30^\circ$N take
$f$ constant and $\mathrm{curl}_z\tau = 1.047\times10^{-7}\ \mathrm{N\,m^{-3}}$:

$$w_E = \frac{1}{1025 \times 7.292\times10^{-5}}
= 1.400\times10^{-6}\ \mathrm{m\,s^{-1}} = 1.40\times10^{-6}\ \mathrm{m\,s^{-1}}.$$

In metres per year: $1.400\times10^{-6}\times3.156\times10^{7} =
44.2\ \mathrm{m\,yr^{-1}}$. A wind-stress curl of $0.1\ \mathrm{N\,m^{-2}}$ over
$3000\ \mathrm{km}$ therefore drives tens of metres per year of Ekman pumping —
enough to displace the thermocline substantially over a decade, and the reason
wind curl maps onto the shape of the gyre's thermocline.

### Example 2 — Ekman transport at two latitudes

A wind stress of $0.20\ \mathrm{N\,m^{-2}}$ directed eastward:

- at $20^\circ$N, $f = 2\Omega\sin20^\circ = 4.987\times10^{-5}\ \mathrm{s^{-1}}$,
  $M = 0.20/(1025\times4.987\times10^{-5}) = 3.914\ \mathrm{m^{2}\,s^{-1}}$
  northward;
- at $50^\circ$N, $f = 2\Omega\sin50^\circ = 1.117\times10^{-4}\ \mathrm{s^{-1}}$,
  $M = 1.747\ \mathrm{m^{2}\,s^{-1}}$ northward.

Same wind, **2.2 times** the transport at the lower latitude. Since $\phi$ enters
through $\sin\phi$, the Ekman response is largest where $f$ is small — and
becomes infinite at the equator, where the approximation fails and a different
dynamics applies.

### Example 3 — how much does $A_v$ move the surface current?

Doubling $A_v$ from $0.010$ to $0.020\ \mathrm{m^{2}\,s^{-1}}$ at $45^\circ$N:
$D = \sqrt{2\times0.020/1.031\times10^{-4}} = 19.7\ \mathrm{m}$ (up from 13.9 m,
a factor $\sqrt{2}$), and
$V_0 = \tau/(\rho\sqrt{A_v f}) = 0.10/(1025\times\sqrt{0.020\times1.031\times10^{-4}})
= 0.10/(1025\times1.436\times10^{-3}) = 0.0680\ \mathrm{m\,s^{-1}}$, i.e.
$1/\sqrt{2}$ of the earlier value. Both move by $\sqrt{2}$; the transport
$0.946\ \mathrm{m^{2}\,s^{-1}}$ is unchanged.

## 9. Python demonstration

`code/wind_driven_circulation_demo.py` prints all of the above with units. It:

1. tabulates $f$, $\beta$ and the inertial period against latitude;
2. computes the Ekman transport for four wind-latitude combinations, including
   the hemisphere and wind-sign changes;
3. tabulates $D$, $\pi D$ and the surface speed against latitude;
4. builds a synthetic wind-stress curl, converts it to a Sverdrup transport, and
   checks the analytic curl against a finite difference
   ($3.3\times10^{-10}\ \mathrm{N\,m^{-3}}$ maximum discrepancy);
5. computes the Stommel and Munk boundary-layer widths;
6. measures the $\beta$-plane error against the spherical $f$ ($3.14\,\%$ over
   $\pm1500\ \mathrm{km}$), verifies that the Ekman transport is independent of
   $A_v$ (difference $0.00\times10^{0}$), and computes the Rossby adjustment
   time (1.70 years).

Run it with

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wind_driven_circulation_demo.py
```

It is print-only, needs no network, uses the fixed seed
`np.random.default_rng(20261014)` and exits 0 in well under a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-wind-driven-circulation-exercises.md`](exercises/02-wind-driven-circulation-exercises.md)
and
[`exercises/02-wind-driven-circulation-solutions.md`](exercises/02-wind-driven-circulation-solutions.md).

- ★ Compute $f$ and $\beta$ at $25^\circ$S and state the units and the sign of
  $\beta$ there.
- ★★ Derive $\mathbf{M} = \hat{z}\times\boldsymbol{\tau}/(\rho f)$ from the
  momentum equations, and say which step assumes the stress vanishes at depth.
- ★★ Given $\tau_x(y)$ of Section 4.2, compute the Sverdrup transport at
  $y = 750\ \mathrm{km}$ and the basin-integrated transport.
- ★★★ Design an observational test of the Sverdrup balance, stating what is
  measured, what is inferred, and which term you would expect to be violated
  first.

## Mastery checkpoint

Without notes, and showing your arithmetic:

> A synthetic basin lies between $15^\circ$N and $45^\circ$N with a zonal wind
> stress $\tau_x(y) = \tau_0\cos(2\pi (y - y_0)/L)$ and $\tau_y = 0$, with
> $\tau_0 = 0.12\ \mathrm{N\,m^{-2}}$, $L = 2000\ \mathrm{km}$ and $y_0 =
> 15^\circ$N. Use $R = 6.371\times10^{6}\ \mathrm{m}$,
> $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$,
> $\rho = 1025\ \mathrm{kg\,m^{-3}}$.
> **(a)** Compute $f$ at $30^\circ$N and state the inertial period there.
> **(b)** Compute $\mathrm{curl}_z\tau$ at $30^\circ$N and the resulting Sverdrup
> transport $V$ in $\mathrm{m^{2}\,s^{-1}}$.
> **(c)** State the direction of the transport and justify the sign from the
> vorticity budget.
> **(d)** Estimate the western boundary current width using the Munk scale with
> $A_H = 5.0\times10^{3}\ \mathrm{m^{2}\,s^{-1}}$, and say what additional
> information you would need to quote a *volume* transport for the boundary
> current.

A worked version of (a)–(d) appears in the lesson-02
[solutions](exercises/02-wind-driven-circulation-solutions.md).

## Common pitfalls

1. **Applying the 90-degree rule without the hemisphere.** The transport is to
   the right of the wind for $f>0$ and to the left for $f<0$. The sign of $f$
   is part of the formula, not a convention to be memorised separately.
2. **Using the Ekman transport at the equator.** $M = \tau/(\rho f)$ diverges as
   $f\to0$; within a few degrees of the equator the balance that produced it
   fails, and the correct treatment is different.
3. **Treating $A_v$ as a measured quantity.** It is a closure. Section 3.2 shows
   it sets the surface current and the layer depth but not the transport; any
   result that depends on it inherits its uncertainty.
4. **Extending the $\beta$-plane too far.** A $3.1\,\%$ error in $f$ at
   $\pm1500\ \mathrm{km}$ about $30^\circ$N is a $3.1\,\%$ error in Ekman
   transport. The approximation is local.
5. **Confusing "steady" with "instantaneous".** The Rossby adjustment time is
   1.7 years for the demonstration basin. A gyre is a multi-year average.
6. **Quoting a boundary current width as a measurement.** It is a function of the
   friction parameterisation; see Section 5.

## Related modules

- [01 Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) —
  the density field that geostrophy refers to.
- [03 Thermohaline Circulation and Deep Water Formation](03-thermohaline-circulation.md) —
  the buoyancy-driven half of the circulation, which the wind-driven half
  interacts with.
- [05 Sea Level, Tides and Harmonic Analysis](05-sea-level-and-tides.md) —
  sea-surface height, the observable that geostrophy turns into a current.
- [06 Ocean-Atmosphere Coupling and ENSO](06-ocean-atmosphere-coupling.md) —
  what happens when the wind itself responds to the ocean's temperature.
- [Module 15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  how sea-surface height and gravity are actually measured.
- [02-06-02 Conservation Laws in Fluids](../../02-physics/06-fluid-mechanics/02-conservation-fluid.md) —
  the vorticity equation used in Section 4.1.

## Self-assessment checklist

- [ ] I can derive $f$ and $\beta$ from the rotation vector and evaluate them.
- [ ] I can derive the Ekman transport and state the 90-degree rule with signs.
- [ ] I can compute an Ekman depth and explain what $A_v$ does and does not set.
- [ ] I can write the Sverdrup balance and convert a wind-stress curl to a
      transport, with units.
- [ ] I can compute a western-boundary width and explain why it is on the west.
- [ ] I can estimate a Rossby adjustment time and say why it matters.
- [ ] I can quote the measured $\beta$-plane error over a stated extent.
