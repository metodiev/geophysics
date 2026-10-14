---
id: 02-05-04
title: "Heat Conduction, Fourier's Law and Thermal Diffusivity"
level: advanced
prereqs: ["02-05-02", "01-06-01", "01-05-04"]
estimated_minutes: 90
tags: [heat-conduction, thermal-diffusivity, diffusion-equation, palaeoclimate]
---

# Heat Conduction, Fourier's Law and Thermal Diffusivity

This is the module's mastery lesson. It contains the equation that generates more
geophysical numbers than any other in thermal geophysics — the diffusion
equation — and the two constants that must never be confused:

$$\underbrace{k}_{\text{conductivity, W m}^{-1}\text{K}^{-1}}\ \text{versus}\
\underbrace{\kappa = \frac{k}{\rho c_p}}_{\text{diffusivity, m}^2\text{s}^{-1}} .$$

For crustal rock $k \approx 2.5$ and $\kappa \approx 1.2\times10^{-6}$; the two
differ by a factor of about $10^6$ and they answer different questions.
**Conductivity sets the flux a given gradient can carry; diffusivity sets the
speed at which a temperature disturbance spreads.** Every error of the form "the
heat took ten years to reach 1 km" traces back to using one where the other was
needed. The exercises test that confusion deliberately and three times.

The lesson ends with the timescale $\tau \sim L^2/\kappa$ applied to the two cases
the module requires: how long a surface temperature change takes to reach 100 m
and 1 km. That calculation is the entire physics of borehole palaeoclimatology.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Fourier's law and explain, with the sign convention, what the minus
   sign means and what observation falsifies the law.
2. **Derive** $\partial T/\partial t = \kappa\nabla^2T$ from Fourier's law and
   conservation of energy, stating every assumption.
3. **Compute** $\kappa$ from $k$, $\rho$ and $c_p$, keep the two apart, and state
   the unit of each in words.
4. **Solve** the half-space step-change problem, obtain
   $T = \Delta T\,\mathrm{erfc}(z/2\sqrt{\kappa t})$, and use it to compute the
   surface heat-flow perturbation $k\Delta T/\sqrt{\pi\kappa t}$.
5. **Compute** the diffusion time for 100 m and 1 km under two stated
   conventions, and explain why both appear in the literature.
6. **Verify** a finite-difference diffusion solver against the analytic solution,
   report the measured error, and demonstrate the observed convergence order.
7. **Apply** the periodic solution to diurnal and annual surface forcing, and
   explain why a borehole temperature log is a low-pass filtered climate record.
8. **State** the steady-state and transient limits, and say which applies to a
   given problem.

## Prerequisites

- [02-05-02 First Law, Work and Energy Balances](./02-first-law.md) — the energy
  balance that, with Fourier's law, gives the diffusion equation.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md)
  — gradient, divergence and the Laplacian.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — the discretisation that underlies the finite-difference solver.

## 1. Fourier's law

For a medium in which heat is carried only by molecular or lattice conduction,

$$\mathbf{q} = -k\nabla T , \qquad [\mathbf{q}] = \mathrm{W\,m^{-2}} . \tag{1}$$

Three things to say about equation (1):

- **The minus sign is the second law.** Heat flows down the gradient. A measured
  flux with the opposite sign in an isotropic medium means either the
  temperature gradient is mis-signed or the flux has an advective component.
- **It is a constitutive relation, not a conservation law.** It is a material
  property, established by measurement (lesson [05-09/02](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/02-thermal-conductivity.md)),
  and it is valid for rock over the whole range of geophysical interest.
- **It says nothing about where the heat goes next.** That requires the first
  law.

**Regime of validity.** Fourier's law assumes (i) local thermodynamic
equilibrium, so that a temperature is defined at every point, (ii) isotropy, so
that a scalar $k$ suffices, (iii) a linear response, and (iv) a timescale long
compared with the molecular collision time. All four hold for rock, water and
air in geophysical settings. They fail for rarefied gases, for ballistic phonon
transport in very cold solids, and for strongly anisotropic layered media where a
tensor $k_{ij}$ is required.

## 2. Derivation of the diffusion equation

### 2.1 From conservation and the constitutive law

Take a fixed control volume $V$ with surface $S$. Conservation of energy with a
distributed source $A$ W m⁻³:

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_V \rho c_p T\,\mathrm{d}V
= -\oint_S \mathbf{q}\cdot\hat{\mathbf{n}}\,\mathrm{d}S + \int_V A\,\mathrm{d}V .
\tag{2}$$

Apply the divergence theorem to the surface term and shrink the volume to a point:

$$\rho c_p\frac{\partial T}{\partial t} = -\nabla\cdot\mathbf{q} + A . \tag{3}$$

Substitute equation (1):

$$\boxed{\ \rho c_p\frac{\partial T}{\partial t} = \nabla\cdot(k\nabla T) + A\ }
\tag{4}$$

and, for constant $k$,

$$\boxed{\ \frac{\partial T}{\partial t} = \kappa\nabla^2T + \frac{A}{\rho c_p}\ }
\qquad \kappa \equiv \frac{k}{\rho c_p} . \tag{5}$$

**Assumptions, stated:** fixed control volume (no material motion, so no
advection term — this is the big one and it is what breaks in the mantle);
local equilibrium; a scalar $k$; only conduction and internal generation carry
energy. Every departure from these is a term in equation (4) that has been
dropped, and the reason the geotherm is not a straight line is usually one of
them.

### 2.2 The two limits

- **Steady state** ($\partial T/\partial t = 0$): $\nabla\cdot(k\nabla T) + A = 0$.
  With constant $k$ and no sources this is Laplace's equation and the geotherm is
  linear, $T = T_0 + (q_0/k)z$ with $q_0$ the surface heat flux. A *steady*
  geotherm takes a time of order $L^2/\kappa$ to establish, which for the
  lithosphere is $10^8$ yr — so real geotherms are only approximately steady.
- **No sources**: the pure diffusion equation
  $\partial T/\partial t = \kappa\nabla^2T$, which is the problem solved below.

### 2.3 Dimensional analysis before any algebra

The only combination of $\kappa$ (m² s⁻¹) and a length $L$ (m) that gives a time
is

$$\tau \sim \frac{L^2}{\kappa} , \tag{6}$$

and the only combination that gives a length for a time $t$ is the **diffusion
length**

$$\ell \sim \sqrt{\kappa t} . \tag{7}$$

Equations (6) and (7) contain the whole qualitative content of the diffusion
equation, and they should be quoted before any solution is attempted. Diffusion
has *no characteristic velocity*: the distance travelled goes as the square root
of time, so a disturbance has no speed, only a spreading.

## 3. Solutions

### 3.1 The half-space step change

Initial condition $T(z,0) = 0$ for all $z \ge 0$; boundary conditions
$T(0,t) = \Delta T$ for $t > 0$ and $T \to 0$ as $z \to \infty$. Because the
problem has no intrinsic length or time scale, the solution depends only on the
dimensionless combination

$$\eta = \frac{z}{2\sqrt{\kappa t}} . \tag{8}$$

Substituting $T = \Delta T\,f(\eta)$ into $\partial T/\partial t =
\kappa\,\partial^2T/\partial z^2$ reduces the PDE to

$$f'' + 2\eta f' = 0 \quad\Longrightarrow\quad f' = C e^{-\eta^2}
\quad\Longrightarrow\quad
f(\eta) = \frac{2}{\sqrt\pi}\int_\eta^\infty e^{-u^2}\mathrm{d}u
= \mathrm{erfc}(\eta) , \tag{9}$$

and therefore

$$\boxed{\ T(z,t) = \Delta T\,\mathrm{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right)\ }
\tag{10}$$

which satisfies both boundary conditions and the initial condition.

### 3.2 The surface heat flow of that solution

Differentiating equation (10) at $z = 0$:

$$\left.\frac{\partial T}{\partial z}\right|_{z=0}
= -\frac{\Delta T}{\sqrt{\pi\kappa t}} , \qquad
q(0,t) = -k\left.\frac{\partial T}{\partial z}\right|_{z=0}
= \frac{k\Delta T}{\sqrt{\pi\kappa t}} . \tag{11}$$

The surface perturbation decays as $t^{-1/2}$ — slowly. A 10 K surface step
2500 years ago still contributes

$$q = \frac{2.5\times10}{\sqrt{\pi\times1.157\times10^{-6}\times7.89\times10^{10}}}
= 4.67\times10^{-2}\ \mathrm{W\,m^{-2}} = 46.7\ \mathrm{mW\,m^{-2}} \tag{12}$$

against a continental background of about 65 mW m⁻². That is a 72 per cent
perturbation on a "measurement", which is precisely why borehole heat-flow
series must be corrected for surface temperature history and why the correction
is not a minor adjustment.

### 3.3 The diffusion time, and the two conventions

Equation (6) gives an order-of-magnitude time. Two precise conventions are in
common use, and they differ by a factor of about three:

| Convention | Definition | Basis |
|---|---|---|
| Characteristic diffusion time | $\tau = L^2/\kappa$ | Dimensional analysis; the time for the profile to be substantially rearranged |
| 10 per cent arrival time | $\mathrm{erfc}(x) = 0.10 \Rightarrow x = 0.9062$, so $t_{10} = L^2/(4x^2\kappa) = 0.304\,L^2/\kappa$ | Time for a step to register 10 per cent of its amplitude at depth $L$ |

Both are legitimate; neither is "the" answer. Quoting one without naming it is
the error. With $\kappa = 1.157\times10^{-6}$ m² s⁻¹:

| $L$ | $\tau = L^2/\kappa$ | $t_{10}$ |
|---|---|---|
| 10 m | 2.7 yr | 0.8 yr |
| **100 m** | **274 yr** | **83 yr** |
| **1 km** | **2.74 × 10⁴ yr** | **8.3 × 10³ yr** |
| 10 km | 2.74 × 10⁶ yr | 8.3 × 10⁵ yr |

**The required calculation.** A surface temperature change reaches 100 m on a
timescale of **2.7 × 10² years** (or 83 years to 10 per cent), and 1 km on a
timescale of **2.7 × 10⁴ years** (or 8.3 × 10³ years). The ratio of the two is
100, exactly as $L^2$ requires.

That factor of 100 is the whole basis of borehole palaeoclimatology. A 100 m
borehole is a thermometer with a century-scale response: it records the Little Ice
Age, land-use change and twentieth-century warming. A 1 km borehole is a
thermometer with a $10^4$–$10^5$ yr response: it records the last glacial
termination. Nothing deeper is useful, because the signal has been attenuated
below the noise and because sediment blanketing, fluid advection and long-term
tectonic change all corrupt it.

### 3.4 Diffusion lengths

The same numbers read as lengths instead of times:

$$\sqrt{\kappa t}:\quad 1\ \text{ka} \to 191\ \text{m}, \quad
1\ \text{Ma} \to 6.04\ \text{km}, \quad 1\ \text{Ga} \to 191\ \text{km}. \tag{13}$$

Over the age of the Earth, conduction alone would move a temperature disturbance
a couple of hundred kilometres. The mantle is 2900 km deep. Therefore conduction
**cannot** be the transport mechanism in the mantle, and this is the argument for
mantle convection in its simplest form. Lesson [05](./05-convection-radiation.md)
supplies the dimensionless number that makes the argument quantitative.

### 3.5 Periodic surface forcing

For $T(0,t) = T_0 + \Delta T\cos\omega t$ on a half-space, the solution is

$$T(z,t) = T_0 + \Delta T\,e^{-z/\delta}\cos(\omega t - z/\delta), \qquad
\delta = \sqrt{\frac{2\kappa}{\omega}} = \sqrt{\frac{\kappa P}{\pi}} , \tag{14}$$

where $P = 2\pi/\omega$ is the period. $\delta$ is the **thermal skin depth**:
the depth over which the amplitude falls by $e$, and the phase lag accumulates
exactly one radian per skin depth. The 1 per cent amplitude depth is
$\delta\ln 100 = 4.605\delta$.

| Cycle | Period (s) | $\delta$ (m) | Depth for 1 % amplitude (m) |
|---|---|---|---|
| Diurnal | 8.64 × 10⁴ | 0.178 | 0.82 |
| Annual | 3.156 × 10⁷ | 3.410 | 15.7 |
| 100 ka | 3.156 × 10¹² | 1078 | 4966 |
| 1 Ma | 3.156 × 10¹³ | 3410 | 15 702 |

For the annual cycle specifically:

| Depth | Amplitude (fraction of surface) | Phase lag |
|---|---|---|
| 1 m | 0.746 | 17.0 d |
| 3 m | 0.415 | 51.1 d |
| 5 m | 0.231 | 85.2 d |
| 10 m | 0.053 | 170.5 d |

The diurnal wave is gone by a metre; the annual wave by 15 m; everything shallower
than that is weather, not climate. Such is the filter that the rock imposes for
free.

### 3.6 Beyond one dimension: what changes

In three dimensions the same equation holds with $\nabla^2$ in place of
$\partial^2/\partial z^2$, and for a body of size $L$ the characteristic time is
again $L^2/\kappa$ with a geometric prefactor of order unity. For a sphere of
radius $a$ whose surface temperature is fixed, the slowest-decaying mode is

$$\tau_{\text{sphere}} = \frac{a^2}{\pi^2\kappa} , \tag{15}$$

so a spherical magma body relaxes about ten times faster than a slab of
thickness equal to its diameter. The prefactor matters for a quantitative
answer; the $L^2/\kappa$ scaling does not change.

## 4. Physical interpretation

**Diffusion has no wavefront.** Equation (10) is non-zero at every $z$ for every
$t > 0$, however small. A step at the surface is felt, infinitesimally, at
infinite depth instantaneously. What is finite is the depth at which it exceeds
some threshold, and that is what $\sqrt{\kappa t}$ measures. Contrast this with
the wave equation of lesson [02-03-05](../03-oscillations-and-waves/05-wave-equation-derivation.md),
where a disturbance has a genuine front travelling at a finite speed. Diffusion
and wave propagation produce qualitatively different records, and the
distinction is worth keeping firm.

**Steady conduction is a limit, not a state.** Equation (2) is a balance of
fluxes; the steady geotherm requires those fluxes to balance everywhere for a
time long compared with $L^2/\kappa$. At 100 km, that is $2.7\times10^8$ yr. Any
thermal event younger than that — a rifting episode, a magmatic underplate —
is transient by construction, and a steady model of it is wrong.

**Conductivity is a property; diffusivity is a property divided by two others.**
The reason $k$ and $\kappa$ are so easy to confuse is that both are called
"thermal" something and both have plausible rock values of order unity. The unit
is the only reliable discriminator: a number of order 1 is $k$; a number of order
$10^{-6}$ is $\kappa$.

**The skin depth is the reason palaeoclimate works at all.** Because the
attenuation is exponential in period, the deep record is band-passed: the annual
cycle is removed by 15 m, but the 100 ka cycle is still at 40 per cent amplitude
at 1 km. A borehole temperature profile is therefore not a blur, it is a
*filtered* record, and the filter is exactly known.

## 5. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Pure conduction | No advection | Mantle, hydrothermal systems, and any aquifer with flowing groundwater; a Péclet number decides |
| Local equilibrium | A temperature exists at every point | Ultrashort times and rarefied media; not relevant in rock |
| Constant $k$ | Analytic solutions available | $k$ rises with $T$ by a factor of ~2 across the lithosphere; solve numerically |
| Constant $\rho c_p$ | $\kappa$ is a constant | Phase changes (latent heat) and pore-fluid vaporisation; use an effective heat capacity |
| No internal heat generation | Equations (10), (14) | Radiogenic heating is O(1) in the crust; see lesson [06](./06-geotherms.md) |
| Half-space geometry | Equations (10), (14) | Finite plates, layering, sediment cover: each changes the profile and must be modelled |
| Isothermal surface (step or sinusoid) | Boundary condition | Real surface temperature histories are neither; they are convolved with the impulse response |
| Scalar $k$ | Isotropic medium | Layered and anisotropic media require $k_{ij}$ |

## 6. Units and dimensional analysis

- $q$: W m⁻². $k$: W m⁻¹ K⁻¹. $\nabla T$: K m⁻¹. Check (1):
  $\mathrm{W\,m^{-1}K^{-1}}\cdot\mathrm{K\,m^{-1}} = \mathrm{W\,m^{-2}}$ ✓.
- $\kappa$: $\mathrm{W\,m^{-1}K^{-1}}/(\mathrm{kg\,m^{-3}}\cdot
  \mathrm{J\,kg^{-1}K^{-1}}) = \mathrm{m^2\,s^{-1}}$ ✓.
- $\nabla^2T$: K m⁻². Then $\kappa\nabla^2T$: $\mathrm{m^2\,s^{-1}}\cdot
  \mathrm{K\,m^{-2}} = \mathrm{K\,s^{-1}}$ ✓, matching $\partial T/\partial t$.
- Equation (10): the argument of erfc must be dimensionless.
  $z/\sqrt{\kappa t}$: $\mathrm{m}/(\mathrm{m\,s^{-1/2}}\cdot\mathrm{s^{1/2}})$
  ✓ dimensionless — a good check that $\kappa$ and not $k$ belongs there.
- Equation (11): $k\Delta T/\sqrt{\pi\kappa t}$:
  $\mathrm{W\,m^{-1}K^{-1}}\cdot\mathrm{K}/(\mathrm{m\,s^{-1/2}}\cdot
  \mathrm{s^{1/2}}) = \mathrm{W\,m^{-2}}$ ✓. Note that it is $k$ in the numerator
  and $\kappa$ under the root — mixing them produces a result wrong by
  $(\rho c_p)^{1/2}$, a factor of ~1500.
- Skin depth: $\sqrt{\kappa P/\pi}$: $\mathrm{m\,s^{-1/2}}\cdot\mathrm{s^{1/2}}
  = \mathrm{m}$ ✓.
- **A useful anchor**: for crustal rock, $\kappa \approx 10^{-6}$ m² s⁻¹, so
  $\sqrt{\kappa t}$ in metres is about $1.8\sqrt{t/\text{yr}}$ — the annual skin
  depth is a few metres and the kiloyear diffusion length is a few hundred
  metres. Every number in §3.3 and §3.5 follows from that single anchor.

## 7. Python demonstration

[`code/heat_conduction_demo.py`](./code/heat_conduction_demo.py) tabulates $k$ and
$\kappa$, computes the diffusion times, solves the step-change problem by
explicit finite differences *and* by equation (10), reports the measured
discrepancy and the observed convergence order, and computes the skin depths.
This is the module's numerical-verification script.

```text
medium           k (W/m/K)  rho (kg/m3)  c_p (J/kg/K)    kappa (m2/s)
rock                 2.500       2700.0         800.0    1.157407e-06
oceanic              3.200       3300.0        1250.0    7.757576e-07
water                0.600       1000.0        4186.0    1.433349e-07
air                  0.026          1.2        1005.0    2.111890e-05
```

```text
         L     L (m)   tau = L^2/kappa     tau (a)    t(10% of dT) (a)
        10        10        8.6400e+07         2.7                 0.8
       100       100        8.6400e+09       273.8                83.4
      1000      1000        8.6400e+11     27378.5              8335.0
     10000     10000        8.6400e+13   2737850.8            833503.8
```

```text
  Diffusion length sqrt(kappa t) in 1 ka = 191.12 m;
  in 1 Ma = 6043.6 m;
  in 1 Ga = 191.1 km.
```

```text
   z (m)    T_num/dT   T_erfc/dT     abs err     rel err
       0    1.000000    1.000000   0.000e+00   0.000e+00
      50    0.906862    0.906859   3.269e-06   3.604e-06
     100    0.814990    0.814983   6.345e-06   7.785e-06
     200    0.639793    0.639781   1.125e-05   1.758e-05
     300    0.482689    0.482675   1.376e-05   2.851e-05
     400    0.349282    0.349269   1.367e-05   3.914e-05
     600    0.160323    0.160315   8.204e-06   5.118e-05
     800    0.061206    0.061204   1.911e-06   3.123e-05
    1000    0.019282    0.019283   1.010e-06   5.240e-05

  max |T_num - T_erfc| = 1.3759e-05  (in units of dT)
  rms error over points with signal = 8.3381e-06  (in units of dT)
  i.e. a worst-case temperature error of 1.3759e-04 K for a 10 K step,
  or 0.0014 per cent of the step amplitude.

  surface flux, analytic k dT/sqrt(pi kappa t) = 0.046677 W/m2 (46.6767 mW/m2)
  surface flux, finite difference k (T0-T1)/dz  = 0.046674 W/m2 (46.6740 mW/m2)
  relative difference = 5.8175e-05
```

```text
  dz (m)      dt (s)     steps     Linf err/dT     ratio
    40.0  5.4410e+08        29      4.3946e-03       nan
    20.0  1.3841e+08       114      1.1212e-03      3.92
    10.0  3.4527e+07       457      2.7988e-04      4.01
     5.0  8.6412e+06      1826      7.0127e-05      3.99
```

```text
cycle         period (s)   omega (rad/s)   delta (m)  depth for 1% amp (m)
diurnal     8.640000e+04    7.272205e-05      0.1784                 0.822
annual      3.155760e+07    1.991021e-07      3.4097                15.702
100 ka      3.155760e+12    1.991021e-12   1078.2518              4965.533
1 Ma        3.155760e+13    1.991021e-13   3409.7315             15702.394

  annual wave at z =  1.0 m: amplitude 0.7458 of surface, phase lag   17.0 days
  annual wave at z =  3.0 m: amplitude 0.4149 of surface, phase lag   51.1 days
  annual wave at z =  5.0 m: amplitude 0.2308 of surface, phase lag   85.2 days
  annual wave at z = 10.0 m: amplitude 0.0532 of surface, phase lag  170.5 days
```

### What to observe

| Observation | Consequence |
|---|---|
| $k = 2.5$ but $\kappa = 1.157\times10^{-6}$ | The factor of $10^6$ is the $\rho c_p$ divisor, and it is why the two must be labelled |
| Rock conducts 4.17× better than water but diffuses 8.08× faster | The two ratios differ; neither can be inferred from the other |
| $\tau$(1 km) = 27 379 yr against $\tau$(100 m) = 274 yr | Exactly the $L^2$ law; this is the borehole-palaeoclimate timescale |
| Maximum FD error $1.38\times10^{-5}$ of the step | The scheme reproduces the exact solution to 0.0014 per cent of the amplitude |
| Surface-flux agreement to 5.8 × 10⁻⁵ relative | The flux, not just the profile, is verified — the harder test |
| Convergence ratio 3.92, 4.01, 3.99 | Second-order in the grid spacing, as theory requires with the cell Courant number held fixed |
| Diurnal $\delta$ = 0.178 m against annual 3.41 m | Skin depth scales as $\sqrt{P}$; a factor of 31 in period gives a factor of 5.6 in depth |
| Annual amplitude 5.3 per cent at 10 m, lag 170 d | The "thermal memory" of the ground is about half a year at 10 m |

> **Breaking exercise.** Change the cell Courant number $r$ from 0.4 to 0.49 —
> just below the explicit stability limit of 0.5 — and predict, before running,
> the new error and whether the ratio column changes. Then set $r = 0.55$ and
> explain the failure mode you observe in terms of the von Neumann condition
> $r \le 1/2$ for this scheme.

## 8. Common mistakes

1. **Using $k$ where $\kappa$ belongs.** The argument of erfc, the skin depth and
   the diffusion time all need $\kappa$; the flux needs $k$. Mixing them is wrong
   by $(\rho c_p)$ or its square root — a factor of 2000 or 45, not a few per
   cent.
2. **Quoting a diffusion time without its convention.** $L^2/\kappa$ and the
   10 per cent time differ by 3.3.
3. **Assuming a finite speed of propagation.** Diffusion has none. "The heat
   front reached 1 km" is loose language for "the perturbation exceeded the
   detection threshold at 1 km".
4. **Applying a steady geotherm to a young thermal event.** The steady state takes
   $L^2/\kappa$.
5. **Forgetting the sign in Fourier's law.** $q = -k\nabla T$; a measured positive
   upward flux with a downward-increasing gradient is consistent, not
   contradictory.
6. **Treating $\kappa$ as constant when a phase change is present.** Latent heat
   makes the effective heat capacity much larger inside the transition interval
   and slows the diffusion there.
7. **Ignoring advection.** A Péclet number $vL/\kappa$ above about 1 means
   groundwater flow, not conduction, controls the temperature field. For $v$ of
   mm yr⁻¹ and $L = 1$ km, $vL/\kappa \approx 27$ — advection wins outright.
8. **Using the half-space solution for a layered or finite medium.** A sediment
   layer of different $k$ changes the surface flux and the depth of the profile;
   the half-space solution is the starting point, not the answer.
9. **Reading a borehole log as a temperature history.** It is a *filtered*,
   attenuated, phase-shifted history; §3.5 is the filter.
10. **Assuming the explicit scheme is stable at any $\Delta t$.** It is not; the
    condition is $\kappa\Delta t/\Delta z^2 \le 1/2$ in one dimension.

## 9. Real-world applications

- **Borehole palaeoclimatology.** The single most important application of
  §3.3–§3.5. A temperature log to a few hundred metres, inverted for surface
  temperature history, yields a record of the last few centuries at a location
  where no instrumental record exists. The inversion is non-unique in detail and
  is stabilised by prior information; the forward physics, however, is exactly
  equation (10).
- **Heat-flow measurement.** The measured gradient must be corrected for
  topography, palaeoclimate, sedimentation and advection before it can be called
  heat flow ([05-09/01](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)).
  Equation (12) shows why the palaeoclimate correction matters.
- **Permafrost and ground temperature.** The annual skin depth and the latent heat
  of the ice–water transition together determine the active-layer thickness, which
  is the standard cryospheric indicator.
- **Geothermal reservoir recharge.** Whether a resource is renewable depends on
  whether conduction from the surrounding rock can resupply heat on the
  extraction timescale — an $L^2/\kappa$ question with $L$ the inter-well spacing.
- **Magma body solidification.** $\tau \sim L^2/\kappa$ gives 2.7 × 10² yr for a
  100 m dyke, 2.7 × 10⁴ yr for a 1 km sill and 2.7 × 10⁶ yr for a 10 km pluton.
  These are the numbers that set the duration of contact metamorphism and
  hydrothermal ore deposition.
- **Thermal conductivity logging.** The same equation inverted: a known heat
  pulse in a borehole gives $\kappa$ from the temperature decay, which is a
  standard in-situ method ([05-09/02](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/02-thermal-conductivity.md)).
- **Engineering ground modelling.** Buried cable ratings, foundation design in
  permafrost, and seasonal thermal storage all use the same equation with the
  same constants.

## 10. Further reading

- **Carslaw, H. S., & Jaeger, J. C. *Conduction of Heat in Solids* (2nd ed.,
  Oxford University Press, 1959).** The definitive source for every analytic
  solution used here, including the erfc and periodic solutions and the
  cylindrical and spherical counterparts. Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** The geophysical setting of the diffusion equation, the
  half-space cooling model, and the correct treatment of advection. Level:
  graduate.
- **Jaupart, C., & Mareschal, J.-C. *Heat Generation and Transport in the Earth*
  (Cambridge University Press, 2011).** The borehole and heat-flow-measurement
  perspective, including the palaeoclimate correction in full. Level: graduate.
- **Incropera, F. P., & DeWitt, D. P. *Fundamentals of Heat and Mass Transfer*
  (Wiley).** Conduction, the explicit finite-difference scheme, the von Neumann
  stability condition, and the convection and radiation material of lesson 05.
  Level: intermediate.
- **Fowler, C. M. R. *The Solid Earth* (2nd ed., Cambridge University Press,
  2005).** A compact treatment of thermal structure that connects this lesson to
  the geotherm construction of lesson 06. Level: intermediate to graduate.
- **Bodri, L., & Čermák, V. *Borehole Climatology* (Elsevier).** The inversion of
  borehole temperature profiles for surface history, with the assumptions stated
  explicitly. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Second Law, Entropy and Irreversibility](./03-second-law.md) — why the
  minus sign in Fourier's law is not a convention.
- [05 Convection, Radiation and Combined Heat Transfer](./05-convection-radiation.md)
  — what replaces conduction when the Péclet or Rayleigh number is large.
- [06 Geotherms, Heat Flow and the Earth's Thermal Budget](./06-geotherms.md) —
  the steady solutions with internal heat production.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the other second-order PDE built from a constitutive law, and the contrast
  between wave propagation and diffusion.
- [01-08-01 First-Order ODEs: Separation of Variables and Integrating Factors](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)
  — the mathematics of the similarity solution.
- [05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — the measurement of $k$, $\kappa$ and $q$.
- [12-global-geophysics-interior/03 Geotherms and Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md)
  — the global context.

Exercises:
[`exercises/04-heat-conduction-exercises.md`](./exercises/04-heat-conduction-exercises.md)
and
[`exercises/04-heat-conduction-solutions.md`](./exercises/04-heat-conduction-solutions.md).

## Self-assessment checklist

- [ ] I can state Fourier's law, explain the minus sign, and state its regime of
      validity. (§1)
- [ ] I can derive equation (5) from conservation of energy and Fourier's law,
      naming every assumption. (§2.1)
- [ ] I can compute $\kappa$ and state the unit of $k$ and of $\kappa$ in words
      without confusing them. (§6)
- [ ] I can derive $T = \Delta T\,\mathrm{erfc}(z/2\sqrt{\kappa t})$ by the
      similarity substitution. (§3.1)
- [ ] I can compute the surface heat-flow perturbation from a step change and
      compare it with a background value. (§3.2)
- [ ] I can compute the diffusion time for 100 m and 1 km under both conventions
      and say which I used. (§3.3)
- [ ] I can verify a numerical diffusion solution against the analytic solution
      and report the measured error and convergence order. (§7)
- [ ] I can compute a skin depth, an amplitude and a phase lag for a periodic
      surface forcing. (§3.5)
- [ ] I can explain why the mantle cannot transport its heat by conduction, using
      $\sqrt{\kappa t}$ at 1 Ga. (§3.4)
- [ ] I can state at least three approximations of §5 with their regimes and what
      breaks outside them. (§5)
