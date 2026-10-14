---
id: 01-09-02
title: "The Diffusion/Heat Equation and Diffusive Timescales"
level: advanced
prereqs: ["01-09-01", "01-06-07"]
estimated_minutes: 90
tags: [partial-differential-equations, diffusion, heat-flow, hydraulic-diffusivity, skin-depth]
---

# The Diffusion/Heat Equation and Diffusive Timescales

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the diffusion equation from a conservation law plus a constitutive
   flux law, and state the physical assumption that makes the derivation valid.
2. **Verify by substitution** that a Gaussian and that a single Fourier mode
   solve the equation, and use that check to derive the spreading law
   $s^2 = \sigma_0^2 + 4\kappa t$.
3. **Derive** the diffusive timescale $\tau \sim L^2/\kappa$, distinguish it
   from a velocity, and compute the diffusion length $\ell = \sqrt{\kappa t}$.
4. **Name all four geophysical subdisciplines governed by this equation** —
   heat flow and palaeoclimate, pore-pressure diffusion and induced seismicity,
   groundwater and aquifer response, and electromagnetic induction — and compute
   a timescale for each.
5. **Compute** the electromagnetic skin depth
   $\delta = \sqrt{2/(\omega\mu\sigma)}$ from the diffusion equation and use it
   to choose a frequency for a target depth.
6. **State** the one property of the equation that is unphysical (infinite
   propagation speed), explain why it survives in practice, and recognise when
   the diffusive approximation itself breaks down.

## Prerequisites

- [01-09-01 Classification of PDEs](./01-classification.md) — the parabolic
  class and the meaning of the discriminant.
- [01-06-07 Vector Identities and Their Role in Geophysics](../06-multivariable-calculus/07-vector-identities.md)
  — the derivation of the electromagnetic diffusion equation from Maxwell's
  equations.
- [01-06-06 Gauss, Stokes and Green Theorems](../06-multivariable-calculus/06-integral-theorems.md)
  — the divergence theorem, which turns the integral conservation statement into
  a PDE.
- [01-05-xx Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  the chain rule and ordinary differential equations, used in the substitution
  checks.

## 1. Intuition: diffusion is smoothing, and smoothing has no speed

Put a drop of dye in still water. It spreads. Nothing about the spreading has a
front: at any time after the drop is placed, there is a nonzero (if tiny)
concentration arbitrarily far away. Diffusion is the physics of *graceful
spreading*, not of travel.

Every geophysical problem of this kind has the same shape. Some quantity $u$ —
temperature, pore pressure, hydraulic head, a magnetic field component — moves
down a gradient. The flux is proportional to the gradient (a *constitutive law*),
and the quantity is conserved. Combine the two and you get

$$\frac{\partial u}{\partial t} = \kappa \nabla^2 u ,$$

one first derivative in time and two in space. The asymmetry between time and
space is the whole story: the equation is not invariant under $t \to -t$, so
diffusion has an arrow of time, and it is the reason the problem needs an
initial condition and boundary conditions.

The single number that comes out of the equation, and the single number a
geophysicist actually uses, is the **diffusive timescale**

$$\tau \sim \frac{L^2}{\kappa}, \qquad \kappa = \text{diffusivity, units }
\mathrm{m^2\,s^{-1}} .$$

Note the units immediately: $\kappa$ has units of area per time, *not* of speed.
This is the formal expression of the fact that diffusion has no velocity, and it
is why every sentence of the form "the heat front advanced at 5 cm/yr" is
muddled. What is true is that the characteristic distance reached in time $t$ is
$\sqrt{4\kappa t}$, so the apparent rate collapses as the front advances.

## 2. Derivation from conservation and a constitutive law

### 2.1 One dimension

Let $u(x,t)$ be a density (energy per volume, mass of fluid per volume, and so
on), and let $q(x,t)$ be the flux (per unit area per unit time, positive in the
$+x$ direction). Conservation over an interval $[a,b]$ says that the rate of
change of the contents equals the flux in minus the flux out:

$$\frac{d}{dt}\int_a^b u\,dx = q(a,t) - q(b,t) = -\int_a^b \frac{\partial
q}{\partial x}\,dx .$$

Since the interval is arbitrary, the integrands must agree:

$$u_t + q_x = 0 . \tag{1}$$

This is exact and requires no physics beyond conservation. The physics enters
through the constitutive law, and the classical choice is **Fourier's law** (for
heat; Darcy's law for groundwater, Fick's law for solute, Ohm's law for
current):

$$q = -\kappa\, u_x . \tag{2}$$

The minus sign is the statement that the flux is down-gradient: heat flows from
hot to cold. Substituting (2) into (1):

$$u_t = \kappa\, u_{xx} . \tag{3}$$

In three dimensions the same two steps give $u_t = \nabla\cdot(\kappa\nabla u)$,
which is $\kappa \nabla^2 u$ when $\kappa$ is constant. If $\kappa$ varies —
across a sediment/basement contact, say — the equation must be written in
divergence form, $u_t = \nabla\cdot(\kappa\nabla u)$, and the interface conditions
are continuity of $u$ and of the normal flux $-\kappa \partial_n u$. Getting this
wrong at a layer boundary is one of the commonest errors in geothermal and
groundwater modelling.

### 2.2 What the derivation assumes

Equation (2) is a **constitutive assumption**, not a theorem. It asserts that the
flux at a point depends on the gradient *at that same point and at the same
instant*. That local-in-time dependence is what makes the equation parabolic and
therefore what gives it infinite propagation speed: if the gradient changes
here, the flux changes here immediately, and conservation then propagates the
effect everywhere in the next instant. Real heat transport has a finite speed
(a phonon or photon speed, or at least the speed of a pressure wave in the
medium); the diffusion equation is the limit in which that speed is large
compared with every other rate in the problem. The correction that restores
finite speed is a **telegraph** (relaxation) term, and the effect on the class is
the subject of exercise ★★8 of [01-09-01](./01-classification.md).

This is worth stating plainly because it is the honest answer to a question every
careful student asks: the diffusion equation is an approximation, extraordinarily
good in the regimes geophysics actually measures, and recognisably wrong if you
push it to very short times or very high frequencies.

## 3. Solutions, verified by substitution

### 3.1 A single Fourier mode

Try $u(x,t) = \mathrm{e}^{-\lambda t}\sin(kx)$ on the line. Then $u_t = -\lambda u$
and $u_{xx} = -k^2 u$, so (3) holds if and only if

$$\lambda = \kappa k^2 . \tag{4}$$

This one line contains most of the physics of the equation:

- every mode decays, none grows (the equation is dissipative);
- the decay rate grows like $k^2$, so **short wavelengths die first**;
- a spatial scale $L$ corresponds to $k \sim 1/L$, so the decay time is
  $\tau \sim 1/(\kappa k^2) \sim L^2/\kappa$.

On a bounded interval $0<x<L$ with $u(0,t) = u(L,t) = 0$, the admissible
wavenumbers are $k = n\pi/L$ and the eigenvalues are

$$\lambda_n = \kappa\frac{n^2\pi^2}{L^2}, \qquad
u_n(x,t) = \sin\!\left(\frac{n\pi x}{L}\right)\mathrm{e}^{-\lambda_n t},
\tag{5}$$

which is the eigenfunction basis that [01-09-05](./05-separation-of-variables.md)
uses for real boundary-value problems. A numerical check of (5) is given in
Section 7: a pure third mode decays at the measured rate $88.832$ per unit time
against the analytic $\kappa(3\pi)^2 = 88.826$.

### 3.2 The fundamental solution, verified by substitution

The solution of (3) on the whole line with the localised initial condition
$u(x,0) = \mathrm{e}^{-x^2/\sigma_0^2}$ is a Gaussian of growing width:

$$u(x,t) = \frac{\sigma_0}{s(t)}\exp\!\left(-\frac{x^2}{s(t)^2}\right),
\qquad s(t)^2 = \sigma_0^2 + 4\kappa t . \tag{6}$$

Let us verify (6) rather than assert it. Write $a = 1/s^2$, so that
$u = \sigma_0\sqrt{a}\,\mathrm{e}^{-ax^2}$. Differentiating,

$$u_t = \frac{\sigma_0}{\sqrt a}\left(\frac{\dot a}{2}\right)
\left(1 - 2ax^2\right)\mathrm{e}^{-ax^2}, \qquad
u_{xx} = -2a\left(1 - 2ax^2\right)\frac{\sigma_0}{\sqrt a}
\mathrm{e}^{-ax^2}.$$

Substituting both into $u_t = \kappa u_{xx}$ and cancelling the common factor
$\dfrac{\sigma_0}{\sqrt a}(1 - 2ax^2)\mathrm{e}^{-ax^2}$ gives

$$\frac{\dot a}{2} = -2\kappa a \qquad\Longrightarrow\qquad
\dot a = -4\kappa a .$$

With $a = s^{-2}$ we have $\dot a = -2s^{-3}\dot s$, so $-2s^{-3}\dot s =
-4\kappa s^{-2}$, i.e. $s\dot s = 2\kappa$, hence

$$\tfrac{1}{2}\frac{d}{dt}s^2 = 2\kappa \qquad\Longrightarrow\qquad
s^2 = \sigma_0^2 + 4\kappa t ,$$

which is exactly (6). The substitution check thus does two jobs at once: it
confirms the solution, and it *derives* the spreading law rather than guessing
it. The demonstration in Section 7 confirms the same statement numerically by
measuring $d\langle x^2\rangle/dt = 2.000000$ where the analytic value is
$2\kappa = 2$.

### 3.3 Three equivalent statements of the timescale

From (6), three quantities agree on the same scaling:

| Statement | Expression | What it measures |
|---|---|---|
| Diffusion length | $\ell = \sqrt{4\kappa t}$ | the distance reached in time $t$ |
| Diffusive time | $\tau = L^2/(4\kappa) \sim L^2/\kappa$ | the time to cross a distance $L$ |
| Variance growth | $d\langle x^2\rangle/dt = 2\kappa$ | the spreading rate, measured in a simulation |

All three say the same thing: **the square of a length grows linearly with
time**, not the length itself. A front that has reached 1 km in 1 Myr reaches
only 2 km in 4 Myr. This is the single most useful scaling law in
solid-Earth geophysics, and the four subsections of Section 4 are four
applications of it.

Two remarks on the numerical factor. The factor 4 belongs to the Gaussian
problem and depends on the convention chosen for $s$; what is robust is
$\tau \sim L^2/\kappa$, and any quotation of a specific number must state
whether it used $\sqrt{\kappa t}$, $\sqrt{4\kappa t}$ or $\sqrt{\pi\kappa t}$.
The demonstration reports $\tau$ computed as $L^2/\kappa$ and says so.

## 4. The four geophysical problems governed by this equation

The table is the point of the lesson. Each row is a different subdiscipline,
a different name for $\kappa$, and the same mathematics.

| Subdiscipline | Quantity $u$ | Diffusivity | Diagnostic $\tau \sim L^2/\kappa$ | Where it appears |
|---|---|---|---|---|
| Heat flow, palaeoclimate | temperature $T$ | thermal diffusivity $\kappa = k/(\rho c)$ | lithospheric and intrusion cooling times | geotherm modelling, borehole palaeoclimate, basin thermal history |
| Pore pressure, induced seismicity | pore pressure $p$ | hydraulic diffusivity $D = k/(\mu S_s)$ | delay between injection and triggered events | reservoir triggering, fluid-induced seismicity, aftershock migration |
| Hydrology | hydraulic head $h$ | aquifer diffusivity $D = T/S$ | aquifer response to pumping or recharge | well tests, recharge estimation, baseflow |
| Electromagnetics | $\mathbf{E}$ or $\mathbf{B}$ | $1/(\mu\sigma)$, no separate name | skin depth $\delta$ and the diffusion time across it | magnetotellurics, transient EM, airborne EM |

### 4.1 Heat flow and palaeoclimate

The thermal diffusivity follows from three measured rock properties,

$$\kappa = \frac{k}{\rho c} ,$$

with $k$ the thermal conductivity, $\rho$ the density and $c$ the specific heat
capacity. Taking an illustrative set, $k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$,
$\rho = 2700\ \mathrm{kg\,m^{-3}}$ and $c = 900\ \mathrm{J\,kg^{-1}K^{-1}}$:

$$\rho c = 2.43\times10^{6}\ \mathrm{J\,m^{-3}K^{-1}}, \qquad
\kappa = \frac{2.5}{2.43\times10^{6}} = 1.03\times10^{-6}\ \mathrm{m^2\,s^{-1}} .$$

Rock thermal diffusivities cluster near $10^{-6}\ \mathrm{m^2\,s^{-1}}$ because
$\rho c$ for silicates varies far less than $k$ does. Using
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and $\tau = L^2/\kappa$:

| Depth scale $L$ | $\tau = L^2/\kappa$ | In years |
|---|---|---|
| 1 km | $1.00\times10^{12}$ s | $3.17\times10^{4}$ yr |
| 10 km | $1.00\times10^{14}$ s | $3.17\times10^{6}$ yr (3.17 Myr) |
| 100 km | $1.00\times10^{16}$ s | $3.17\times10^{8}$ yr (317 Myr) |

Three consequences that are used constantly:

- **Borehole palaeoclimate.** A temperature perturbation at the surface takes of
  order $L^2/\kappa$ to reach depth $L$; a 100 m borehole therefore records the
  last few centuries, and a 1 km borehole records the last glaciation. The
  inversion of a borehole temperature profile for a surface history is a
  *backward parabolic* problem, and [01-09-07](./07-boundary-value-problems.md)
  shows exactly how ill posed that is.
- **Lithospheric thermal structure.** A 100 km thick thermal boundary layer
  needs ~300 Myr to equilibrate, comparable to the age of oceanic lithosphere,
  so a steady geotherm is an assumption to be tested rather than a default.
- **Intrusion cooling.** A 1 km dyke cools on a timescale of about
  $(10^3)^2/10^{-6} = 10^{12}$ s ≈ 32 kyr, which is why contact metamorphic
  aureoles record brief thermal pulses and why magma chambers of 10 km scale
  need millions of years to solidify.

### 4.2 Pore pressure and induced seismicity

The pore-pressure diffusion equation is

$$\frac{\partial p}{\partial t} = D\nabla^2 p, \qquad
D = \frac{k}{\mu S_s},$$

with $k$ the permeability, $\mu$ the fluid viscosity and $S_s$ the specific
storage. $S_s$ is the one that surprises people, so derive its magnitude rather
than quote it:

$$S_s = \rho_w g\left(\alpha + n\beta\right),$$

where $\alpha$ is the compressibility of the rock skeleton, $\beta$ the
compressibility of the pore fluid and $n$ the porosity. With
$\rho_w g \approx 9.81\times10^{3}\ \mathrm{Pa\,m^{-1}}$,
$\alpha = 1.0\times10^{-10}\ \mathrm{Pa^{-1}}$ (a stiff crystalline rock),
$n = 0.01$ and $\beta = 4.5\times10^{-10}\ \mathrm{Pa^{-1}}$ (water):

$$S_s \approx 9.81\times10^{3}\left(1.0\times10^{-10}
+ 0.01\times4.5\times10^{-10}\right) = 1.03\times10^{-6}\ \mathrm{m^{-1}} .$$

So $S_s \sim 10^{-6}\ \mathrm{m^{-1}}$ for stiff rock, and it is the *inverse*
of this quantity that enters $D$. With $\mu = 10^{-3}\ \mathrm{Pa\,s}$ (water at
room conditions) and $k = 10^{-15}\ \mathrm{m^2}$ — about 1 mD, a plausible
matrix permeability — the demonstration computes

$$D = \frac{10^{-15}}{10^{-3}\times10^{-6}} = 1.0\times10^{-6}\ \mathrm{m^2\,s^{-1}} ,$$

and $\tau = (5\times10^3)^2/D = 2.5\times10^{13}$ s ≈ 0.79 Myr to diffuse 5 km.
The demonstration's table spans $k = 10^{-15}$ to $10^{-13}\ \mathrm{m^2}$ and
$S_s = 10^{-6}$ to $10^{-7}\ \mathrm{m^{-1}}$, i.e. $D$ from $10^{-6}$ to
$10^{-3}\ \mathrm{m^2\,s^{-1}}$, giving $\tau$ at $L = 5$ km between
$7.9\times10^{5}$ yr and 792 yr.

Now the awkward part, stated as a computation rather than an opinion. A
triggered event a year after injection, 5 km away, requires

$$D = \frac{L^2}{\tau} = \frac{2.5\times10^{7}}{3.156\times10^{7}}
= 0.792\ \mathrm{m^2\,s^{-1}} ,$$

and at $S_s = 10^{-6}\ \mathrm{m^{-1}}$ that implies
$k = D\mu S_s = 7.9\times10^{-10}\ \mathrm{m^2}$ — near 1 Darcy, high for intact
rock, though not impossible in a fractured or fault-damaged volume. Hydraulic
diffusivities inferred from migration of seismicity in the literature span a
wide range and depend on the assumed storage and on whether the migration is
genuinely pressure-controlled; **treat any single quoted $D$ as a model
assumption, and check the storage it implies against the geology.** What the
calculation demonstrates beyond doubt is the sensitivity: $D$ is *linear* in $k$
and *inverse* in $S_s$, so a factor of ten error in storage is a factor of ten
error in the inferred triggering time.

### 4.3 Hydrology: aquifer and reservoir response

For a confined aquifer, the same equation governs the hydraulic head with

$$D = \frac{T}{S} ,$$

$T$ the transmissivity ($\mathrm{m^2\,s^{-1}}$) and $S$ the dimensionless
storativity. With illustrative values $T = 10^{-2}\ \mathrm{m^2\,s^{-1}}$ and
$S = 10^{-3}$, $D = 10\ \mathrm{m^2\,s^{-1}}$, so

$$\tau(1\ \mathrm{km}) \approx 1.16\ \mathrm{d}, \qquad
\tau(10\ \mathrm{km}) \approx 116\ \mathrm{d}, \qquad
\tau(50\ \mathrm{km}) \approx 7.9\ \mathrm{yr} .$$

This is why a pumping test reaches pseudo-steady state in hours to days over
hundreds of metres, why the pressure response to a distant recharge event is
delayed by weeks, and why regional-scale aquifer response takes years. Note that
$D$ here is six orders of magnitude larger than the thermal diffusivity: water
pressure equilibrates far faster than heat, so **in any coupled problem the
pore pressure is quasi-static while the temperature is not.** Getting that
ordering right is what makes coupled thermo-hydro-mechanical models tractable.

### 4.4 Electromagnetic induction and the skin depth

In a conductor at low frequency, the electric field obeys the same equation.
Take the time-harmonic form $\mathbf{E} = \mathbf{E}_0\mathrm{e}^{i(kz -
\omega t)}$ for a plane wave travelling in the $+z$ direction. Then
$\partial_t \to -i\omega$ and $\nabla^2 \to -k^2$, so
$\nabla^2\mathbf{E} = \mu\sigma\,\partial_t\mathbf{E}$ becomes

$$-k^2 = -i\omega\mu\sigma \qquad\Longrightarrow\qquad
k^2 = i\omega\mu\sigma .$$

Taking the square root of $i\omega\mu\sigma$ gives $k = (1+i)/\delta$ with the
**skin depth**

$$\delta = \sqrt{\frac{2}{\omega\mu\sigma}} = \sqrt{\frac{1}{\pi f \mu\sigma}}
\tag{7}$$

(the second form follows from $\omega = 2\pi f$). The field decays as
$\mathrm{e}^{-z/\delta}$: one skin depth of rock attenuates it by $1/e$, and
the diffusion time across one skin depth is

$$\mu\sigma\delta^2 = \frac{1}{\pi f},$$

which is *exactly* one radian of the driving period — a clean check that $\delta$
is the right length scale, and one the demonstration verifies numerically. With
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{T\,m\,A^{-1}}$:

| Conductivity $\sigma$ (S/m) | Frequency $f$ | Skin depth $\delta$ | Diffusion time across $\delta$ |
|---|---|---|---|
| $10^{-4}$ | $10^{-3}$ Hz | 1592 km | 0.0884 h |
| $10^{-4}$ | 1 Hz | 50.3 km | 0.318 s |
| $10^{-4}$ | $10^{3}$ Hz | 1.59 km | $3.18\times10^{-4}$ s |
| $10^{-2}$ | $10^{-3}$ Hz | 159 km | 0.0884 h |
| $10^{-2}$ | 1 Hz | 5.03 km | 0.318 s |
| $10^{-2}$ | $10^{3}$ Hz | 159 m | $3.18\times10^{-4}$ s |
| $1.0$ | 1 Hz | 503 m | 0.318 s |

Read the middle column down: **lower frequency sounds deeper, higher conductivity
sounds shallower.** Those two sentences are the design rule for every
electromagnetic depth-sounding method. They are also the reason
magnetotellurics uses periods of seconds to thousands of seconds (to reach the
mantle) while a metal detector uses kilohertz (to see the top metre).

The demonstration's third section confirms (7) numerically, including the
$\mu\sigma\delta^2 = 1/(\pi f)$ relation for every entry in the table.

## 5. What the equation does to data, and what it destroys

Because the decay rate is $\kappa k^2$, the equation is a **low-pass filter
applied to the source**. Two consequences matter for interpretation.

**Resolution is lost with distance and time.** A sharp source feature of
wavelength $\Lambda$ is attenuated by $\exp(-4\pi^2\kappa t/\Lambda^2)$. Put in
a 10 m anomaly at depth in a diffusion problem and, by the time the signal has
diffused 100 m, only the longest wavelengths survive. This is the mathematical
reason that the potential-field "smoothing with altitude" of
[01-06-08](../06-multivariable-calculus/08-potential-theory.md) has a
time-dependent twin here.

**Inversion is a backward diffusion.** Recovering the initial condition from a
diffused observation means multiplying by $\exp(+\lambda_n t)$, which amplifies
noise without bound. [01-09-07](./07-boundary-value-problems.md) measures this: a
wavenumber-20 noise mode of amplitude $10^{-6}$ needs an amplification of
$5.3\times10^{85}$, so an error of $10^{-6}$ in the data becomes an error of
$10^{79}$ in the answer. Regularisation is not a refinement of the method here;
it is the only possibility.

**The equation never creates a singularity.** Diffusion smooths everything. A
discontinuous initial condition is instantly smoothed (in fact the solution is
analytic for all $t>0$), and a point source produces the fundamental solution

$$\Phi(x,t) = \frac{1}{\sqrt{4\pi\kappa t}}\,\mathrm{e}^{-x^2/(4\kappa t)} ,$$

which is the Green's function of the operator and the kernel of every linear
superposition used in practice. Compare the nonlinear first-order equations of
[01-09-06](./06-characteristics.md), which manufacture discontinuities.

## 6. Physical interpretation, and where the model fails

| Feature of the mathematics | Physical statement | Where it is tested |
|---|---|---|
| $\lambda = \kappa k^2$ | fine structure decays fastest | seismic attenuation, thermal aureoles, EM resolution |
| $\ell = \sqrt{4\kappa t}$ | spreading, not travel | palaeoclimate depth of penetration, EM sounding depth |
| $d\langle x^2\rangle/dt = 2\kappa$ | mean square displacement grows linearly | measured in the demonstration to 3 significant figures |
| infinite propagation speed | unphysical; consequence of local Fourier's law | relevant only at very short times |
| analytic smoothing | no shocks, ever | contrasts with [01-09-06](./06-characteristics.md) |
| time-irreversibility | an arrow of time, unlike the wave equation | backward problems are ill posed |

The last row is worth a sentence of physical reading. The wave equation is
symmetric in time; the diffusion equation is not. If the theory were exactly
faithful to the microscopic physics, the arrow of time would have to come from
somewhere — statistical mechanics supplies it through the second law. Geophysics
inherits the arrow as an empirical fact: heat flows downhill.

## 7. Python demonstration

The script `code/diffusion_timescales.py` computes the timescale table of
Section 4, verifies the numerical solution against the exact Gaussian, verifies
the variance law, and measures the infinite propagation speed directly.

**Verification against the exact solution.** For $u_t = u_{xx}$ on $(-1,1)$ with
$u(\pm1) = 0$ and the initial Gaussian of width $\sigma_0 = 0.05$ at time
$t = 0.02$, the exact width is $s = \sqrt{\sigma_0^2 + 4\kappa t} = 0.287228$:

```text
     N         dx    max error   order
    50   3.92e-02    1.073e-03        
   100   1.98e-02    2.789e-04    1.94
   200   9.95e-03    7.066e-05    1.98
   400   4.99e-03    1.780e-05    1.99
   800   2.50e-03    4.464e-06    2.00
```

The observed order is 2, as the second-order space discretisation requires. The
script also reports the exact value at the boundary, $9.5\times10^{-7}$, to show
that imposing $u(\pm1) = 0$ is consistent with the Gaussian to that accuracy —
checking the geometry and boundary conditions the formula requires, rather than
assuming them.

**The variance law.** Measuring the second central moment of the numerical
solution:

```text
  delta t                    = 0.049875
  <x^2> at t=0               = 0.00125000   (exact sigma0^2/2 = 0.00125000)
  <x^2> at t=delta t         = 0.10100047
  measured d<x^2>/dt         = 2.000000
  2 kappa                    = 2.000000
  relative difference        = 0.000 %
```

This is the cleanest possible confirmation that the timescale $\tau \sim
L^2/\kappa$ is a statement about variance growth, and that the numerical scheme
reproduces it rather than merely resembling it. An earlier version of the
experiment used a domain too short for the pulse and gave $1.939$ against
$2.000$ — a $3\,\%$ error caused entirely by mass leaking through the boundary,
which is why the reported run uses a domain three times wider than the pulse.
The lesson generalises: **before trusting any measured scaling, check that the
boundary is not participating.**

**Infinite propagation speed.** Starting from a compactly supported pulse and
asking for the largest value outside its original support:

```text
  initial pulse support: |x| <= 0.1  (zero outside)
  after   1 step(s): max |u| outside original support = 6.138e-06
  after   5 step(s): max |u| outside original support = 5.175e-03
  after  50 step(s): max |u| outside original support = 7.737e-02
```

Compare the wave demonstration of [01-09-03](./03-wave-equation.md), where the
same test gives exactly $0.000\times10^{0}$. Diffusion has no light cone; waves
have nothing else.

**The timescale table.** Sample output, with all parameters as stated in
Section 4:

```text
(a) Heat / palaeoclimate: thermal diffusivity
    assumed kappa = 1.0e-06 m^2/s
      L =    1.0 km  ->  tau = 1.000e+12 s = 3.17e+04 yr
      L =   10.0 km  ->  tau = 1.000e+14 s = 3.17 Myr
      L =  100.0 km  ->  tau = 1.000e+16 s = 317 Myr

(b) Pore pressure / induced seismicity: hydraulic diffusivity
       k (m^2)   S_s (1/m)   D (m^2/s)     tau, L=5 km
       1.0e-15     1.0e-06   1.000e-06     7.92e+05 yr
       1.0e-14     1.0e-06   1.000e-05     7.92e+04 yr
       1.0e-13     1.0e-07   1.000e-03          792 yr
    A 1-year delay over 5 km needs D = 0.792 m^2/s.

(c) Hydrology: aquifer diffusivity D = T / S
    D = 10 m^2/s
      L =   1.0 km  ->  tau = 1.16 d
      L =  10.0 km  ->  tau = 116 d
      L =  50.0 km  ->  tau = 7.92 yr

(d) Electromagnetics: skin depth delta = sqrt(1 / (pi f mu0 sigma))
      sigma (S/m)    f (Hz)     delta (m)
          1.0e-02   1.0e+00          5033
          1.0e-02   1.0e+03         159.2
          1.0e-04   1.0e-03     1.592e+06
```

> **Breaking exercise.** Decide, with numbers, whether a 1 Hz magnetotelluric
> sounding in a $0.01\ \mathrm{S\,m^{-1}}$ half-space can detect a target at
> 15 km depth, given that a body must lie within about one skin depth to be
> resolved. Then change the conductivity to $10^{-3}\ \mathrm{S\,m^{-1}}$ (a
> resistive shield) and repeat. Predict both answers before computing.

## 8. Common mistakes

1. **Treating $\tau \sim L^2/\kappa$ as a speed.** It is not. Doubling the
   distance quadruples the time. Writing "the front velocity is $L/\tau$" is
   wrong twice over: $\tau$ is a scale, not a period, and the front slows as it
   advances.
2. **Confusing conductivity with diffusivity.** $k$ in
   $\mathrm{W\,m^{-1}K^{-1}}$ is a property of the material's ability to conduct;
   $\kappa = k/(\rho c)$ in $\mathrm{m^2\,s^{-1}}$ is what appears in the
   equation. They differ by $\rho c \approx 2.4\times10^{6}$ for rock, so
   mixing them up changes every timescale by six orders of magnitude.
3. **Quoting a single $\kappa$ for rock.** Because $\rho c$ varies little,
   $\kappa$ is approximately $10^{-6}\ \mathrm{m^2\,s^{-1}}$ for most silicates,
   but porous, water-saturated or organic-rich sediments can differ by a factor
   of several. State the value used.
4. **Ignoring the storage term in $D = k/(\mu S_s)$.** The inferred hydraulic
   diffusivity is inversely proportional to $S_s$, which is rarely measured
   directly.
5. **Assuming compact support.** Diffusion gives nonzero values everywhere for
   any $t>0$. A code that assumes a sharp front will disagree with the exact
   solution at the level of the tail, which matters when the tail *is* the
   signal (as in EM sounding at depth).
6. **Using the parabolic skin-depth equation outside its regime.** Equation (7)
   assumes $\sigma \gg \omega\epsilon$. Ground-penetrating radar violates it, and
   GPR must be modelled with the hyperbolic (wave) form; see
   [01-09-01](./01-classification.md) §4.4.
7. **Forgetting that the equation is a low-pass filter when interpreting
   amplitudes.** An attenuation observed in diffusive data may be a property of
   the frequency, not of a material contrast.
8. **Solving the steady-state problem when the timescale exceeds the age of the
   system.** A pre-condition for $\nabla\cdot(k\nabla T) = 0$ is $t \gg L^2/\kappa$;
   check it.

## 9. Real-world applications

- **Borehole climatology.** Surface temperature histories are recovered from
  borehole profiles by inverting a backward diffusion problem; the depth of
  penetration and the ill-posedness both follow from $\tau \sim L^2/\kappa$.
- **Reservoir-induced seismicity.** Triggering delays, migration of hypocentres
  and the spatial extent of seismicity are all read through
  $D = k/(\mu S_s)$; the four-row table above is the framework of that reading,
  together with an honest statement about the required permeability.
- **Aquifer management.** Well tests are analysed with the diffusion equation;
  $D = T/S$ determines whether a distant river or recharge area will affect a
  well within the planning horizon.
- **Magnetotellurics and transient EM.** The skin depth is the design equation:
  frequency for depth, and conductivity for resolution. Time-domain systems
  exploit the same diffusion by measuring the decay of the transient, whose late
  times carry the deep information.
- **Thermal history of sedimentary basins.** Maturity of hydrocarbons depends on
  a time–temperature integral, so the basin must be modelled with the
  *time-dependent* heat equation; the steady geotherm is the wrong tool.
- **Meteorite and magma-body cooling.** Cooling times of
  $L^2/\kappa$ set the sizes of bodies that can retain a remanent magnetisation,
  and hence what palaeomagnetic records are possible.

## 10. Further reading

- **Carslaw, H. S., & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** Level: graduate. The encyclopaedic
  reference for analytic solutions of the heat equation, including the
  superposition and Green's-function machinery of Section 5.
- **Crank, J. (1975). *The Mathematics of Diffusion* (2nd ed.). Oxford
  University Press.** Level: graduate. The standard companion volume, stronger
  on boundary conditions and on diffusive problems in porous media.
- **Turcotte, D. L., & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Level: advanced undergraduate upward. Chapters on heat
  transfer and on thermal structure that apply $\tau \sim L^2/\kappa$ to the
  lithosphere, the mantle and magmatic systems.
- **Ingebritsen, S. E., Sanford, W. E., & Neuzil, C. E. (2006). *Groundwater in
  Geologic Processes*. Cambridge University Press.** Level: graduate. Hydraulic
  diffusivity, specific storage and their role in crustal fluid flow; the
  practical counterpart of Section 4.2 and 4.3.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Level: intermediate.
  The skin-depth formula in its survey context and the frequency ranges used by
  real instruments.
- **Nabighian, M. N. (Ed.) (1988–1991). *Electromagnetic Methods in Applied
  Geophysics*, Vols. 1–3. SEG.** Level: graduate. The standard reference for the
  diffusive electromagnetic regime.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Solutions are in
[`exercises/02-heat-equation-solutions.md`](./exercises/02-heat-equation-solutions.md).

**★1.** Compute $\kappa = k/(\rho c)$ for (a) granite with
$k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$, $\rho = 2650\ \mathrm{kg\,m^{-3}}$,
$c = 800\ \mathrm{J\,kg^{-1}K^{-1}}$; (b) water-saturated sand with
$k = 1.8\ \mathrm{W\,m^{-1}K^{-1}}$, $\rho = 2100\ \mathrm{kg\,m^{-3}}$,
$c = 1400\ \mathrm{J\,kg^{-1}K^{-1}}$. Which cools faster, and by what factor?

**★2.** Using $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, find the time for a
surface temperature perturbation to reach (a) 50 m, (b) 500 m, (c) 2 km. Convert
each to years and state which is relevant to a borehole climate study.

**★3.** Verify by substitution that
$u(x,t) = \mathrm{e}^{-\kappa n^2\pi^2 t}\sin(n\pi x/L)$ solves
$u_t = \kappa u_{xx}$ on $(0,L)$ and satisfies $u(0,t) = u(L,t) = 0$.

**★4.** Derive the skin depth from $k^2 = i\omega\mu\sigma$ by writing
$k = \alpha + i\beta$ and solving for $\alpha$ and $\beta$. Show that
$\delta = 1/\beta$ and confirm $\mu\sigma\delta^2 = 1/(\pi f)$.

**★★5.** A confined aquifer has $T = 0.02\ \mathrm{m^2\,s^{-1}}$ and
$S = 2\times10^{-4}$. Compute $D$. How long until a pressure change 20 km away
is observable? State why the answer is an order-of-magnitude statement and not a
prediction.

**★★6.** The half-width of a cooling dyke of thickness $b$ is often quoted as
cooling on the timescale $b^2/\kappa$. For $b = 500$ m and
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, compute it in years. Then compute the
time for the *centre* to cool, and explain why the two differ by a modest factor
rather than a large one.

**★★7.** An injection well produces a pore-pressure front. Using
$D = 0.5\ \mathrm{m^2\,s^{-1}}$, compute the distance reached in 30 days and in
365 days, and the ratios of those distances to the square roots of the times.
Explain why the ratio of distances is not the ratio of times.

**★★8.** Show that the operator $\partial_t - \kappa\partial_x^2$ is linear and
that the fundamental solution $\Phi$ satisfies
$\int_{-\infty}^{\infty}\Phi\,dx = 1$ for all $t > 0$. What does conservation of
that integral mean physically, and which boundary condition at infinity does it
require?

**★★★9.** Take $u_t = \kappa u_{xx}$ on $(0,1)$ with $u(0,t) = 1$,
$u(1,t) = 0$ and the step initial condition $u = 1$ for $x<0.5$, $u = 0$ for
$x>0.5$. Subtract the steady profile $1-x$ so that the boundary data for the
remaining part are homogeneous, and use its Fourier sine series (with enough terms)
as the reference solution. Measure the observed convergence order in the maximum
norm at $t = 10^{-2}$, $10^{-3}$ and $10^{-4}$ on a sequence of grids. Report the
orders, state whether they are stable, and identify the dimensionless quantity that
controls when the order degrades. Explain the finding physically: the operator
smooths instantly, so what is it that the grid still has to resolve?

**★★★10.** Write a short critical note on the following sentence, as if
reviewing a paper: "The 5 km migration of seismicity in 12 months implies a
hydraulic diffusivity of $0.7\ \mathrm{m^2\,s^{-1}}$, hence a permeability of
about $10^{-9}\ \mathrm{m^2}$, consistent with a fractured reservoir." State
every assumption the inference requires, give the storage value it implies, and
say what independent measurement would test it. Use the numbers derived in
Section 4.2.

## 12. Self-assessment checklist

- [ ] I can derive the diffusion equation from conservation plus a constitutive
      flux law and state the assumption that makes it parabolic.
- [ ] I can verify a Gaussian and a Fourier mode by substitution and derive
      $s^2 = \sigma_0^2 + 4\kappa t$.
- [ ] I can compute $\tau \sim L^2/\kappa$ for rock, water and an aquifer, and
      say why the aquifer responds a million times faster than the rock heats.
- [ ] I can name the four subdisciplines and the name of the diffusivity in each.
- [ ] I can derive the skin depth and use it to choose a frequency for a target
      depth.
- [ ] I can state the one unphysical feature of the equation and explain why it
      does no harm in practice.
- [ ] I can explain why inverting diffusive data is a backward parabolic problem
      and why regularisation is unavoidable.

## Related lessons

- [01-09-01 Classification of PDEs](./01-classification.md) — why this equation
  is the parabolic prototype, and what that buys and costs.
- [01-09-03 The Wave Equation and Its Physical Content](./03-wave-equation.md) —
  the finite-speed counterpart, and the contrast that makes both clearer.
- [01-09-05 Separation of Variables and Boundary Conditions](./05-separation-of-variables.md)
  — where the eigenfunctions (5) are used on real problems, including heat
  conduction in a layered Earth.
- [01-09-07 Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md)
  — why the backward version of this equation is ill posed.
- [06-seismology](../../06-seismology/README.md) — aftershock migration and
  poroelastic triggering, read through this equation.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation, the
  answer to the backward-diffusion problem.
