---
id: 01-09-06
title: "Method of Characteristics and First-Order PDEs"
level: graduate
prereqs: ["01-09-01"]
estimated_minutes: 90
tags: [partial-differential-equations, characteristics, first-order, conservation-laws, weak-solutions]
---

# Method of Characteristics and First-Order PDEs

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a first-order linear or quasilinear PDE into a system of ordinary
   differential equations along its characteristics, and use that system to write
   the general solution.
2. **Solve** $u_t + c u_x = 0$ and a variable-coefficient example
   $u_t + x u_x = 0$ by characteristics, and verify each by substitution.
3. **Derive** the breaking time $t_s = -1/\min u_0'$ at which the characteristics
   of $u_t + u u_x = 0$ cross, and compute the gradient
   $u_x = u_0'(x_0)/(1 + u_0'(x_0)t)$ before and after breaking.
4. **Explain** why a classical solution ceases to exist at $t_s$ and what a weak
   (shock) solution is, including the Rankine–Hugoniot speed.
5. **Distinguish** the upwind scheme's first-order error from physical diffusion by
   deriving the modified equation and predicting the numerical spreading rate.
6. **Recognise** kinematic-wave problems in geophysics and state which physical
   assumption makes the first-order reduction legitimate.

## Prerequisites

- [01-09-01 Classification of PDEs](./01-classification.md) — why the discriminant
  test does not apply to first-order equations, and the Kramers–Wagner notion of a
  characteristic.
- [01-05-xx Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  first-order ODEs, the chain rule, and the method of solving $dy/dx = f(x)g(y)$.
- [01-06-01 Partial Derivatives and the Chain Rule](../06-multivariable-calculus/01-partial-derivatives.md)
  — the multivariable chain rule, which is the engine of the whole method.

## 1. Intuition: first-order means information travels one way

The second-order equations of the previous lessons carry two characteristic
families (hyperbolic), one (parabolic) or none (elliptic). A first-order equation
carries exactly one, and that simplicity is not a loss of interest: it is the
reason first-order equations describe *transport*, and transport is the mechanism
behind fronts, kinematic waves and shocks.

The equation

$$u_t + c\,u_x = 0 \tag{1}$$

says that the rate of change of $u$ following a point moving at speed $c$ is zero.
Nothing else. Its solution is a rigid translation, $u(x,t) = f(x - ct)$, and every
geophysical phenomenon that is "carried along" at a speed — a flood wave on a
river, a sediment pulse in a distributary, a contaminant front, a glacier surge —
is a version of it, possibly with $c$ replaced by a function of $u$ itself.

The essential contrast with the diffusion equation of
[01-09-02](./02-heat-equation.md) is that (1) introduces **no smoothing and no
loss of shape**, while adding nonlinearity introduces the opposite of smoothing:
**steepening into a discontinuity.** Diffusion rounds every corner; transport
sharpens them. Real geophysical fronts generally show both, which is why the
Burgers equation $u_t + uu_x = \nu u_{xx}$ is the standard model for a shock that
is smoothed by viscosity over a finite width.

## 2. The method, derived

### 2.1 From a PDE to a system of ODEs

Consider the general first-order linear equation in two independent variables,

$$a(x,t)\,u_x + b(x,t)\,u_t = c(x,t) , \tag{2}$$

and ask for curves $x(s), t(s)$ along which (2) becomes an ordinary differential
equation for $u$. Along such a curve, the chain rule gives

$$\frac{du}{ds} = u_x\frac{dx}{ds} + u_t\frac{dt}{ds} .$$

Comparing this with (2), the curve must satisfy

$$\frac{dx}{ds} = a(x,t), \qquad \frac{dt}{ds} = b(x,t), \qquad
\frac{du}{ds} = c(x,t) . \tag{3}$$

The first two equations define the **characteristics** — a family of curves in the
$(x,t)$ plane, obtained by solving an ODE that does not involve $u$. The third
equation then advances $u$ along each curve. This is the entire method:

> Solve the characteristic ODEs, label each characteristic by where it started,
> and carry the initial data along it.

For the **quasilinear** case where $c$ depends on $u$ — equation (2) with
$c = c(x,t,u)$ — the same construction works, with the essential difference that
the characteristics now depend on the solution. That feedback is what produces
nonlinear steepening, and Section 4 is about its consequences.

### 2.2 Conservation form

Many first-order equations arrive in **conservation form**

$$u_t + \left(f(u)\right)_x = 0 , \qquad\text{equivalently}\qquad
u_t + f'(u)\,u_x = 0 , \tag{4}$$

which is the differential version of the integral statement that the total of $u$
in any interval changes only by flux through its ends. The two forms are
equivalent wherever $u$ is smooth; they are **not** equivalent across a
discontinuity, and (4) is the correct statement to discretise, because it is the
one that conserves. Almost every numerical scheme for first-order problems is
built on this distinction, and Section 5 returns to it.

## 3. Two solved examples, verified

### 3.1 Constant velocity: $u_t + c u_x = 0$

From (3) with $a = c$, $b = 1$, $c_{\text{rhs}} = 0$:

$$\frac{dx}{ds} = c, \qquad \frac{dt}{ds} = 1, \qquad \frac{du}{ds} = 0 .$$

Take $s = t$: then $x = x_0 + ct$ and $u$ is constant along each characteristic.
Therefore $u$ depends only on the label $x_0 = x - ct$, i.e.

$$u(x,t) = f(x - ct) , \tag{5}$$

where $f$ is the initial condition. No integration of a PDE was required.

The demonstration verifies (5) by central differences, using *different* step
sizes in space and time so that the two difference operators do not coincide:

```text
          hx        ht     |u_t + c u_x|   order
    1.00e-02  7.00e-03         1.003e-05        
    5.00e-03  3.50e-03         2.508e-06    2.00
    2.50e-03  1.75e-03         6.269e-07    2.00
    1.25e-03  8.75e-04         1.567e-07    2.00

  With ht = hx = 1e-02 the residual is exactly 0.0e+00
```

Order 2, confirming the solution, and the last line records a special fact:
with equal steps and $c = 1$, both differences sample the *same points* along the
characteristic and the residual vanishes identically. That alignment is the same
one that makes the leapfrog scheme exact at Courant number 1
([01-09-03](./03-wave-equation.md) §5.3), and the same one that lets a first-order
scheme be exact when $\Delta x = c\,\Delta t$ — the reason the upwind scheme is
exact at Courant number 1 in one dimension.

A first-order equation needs **one** initial or boundary condition, not a pair,
and not a closed curve: the characteristic family is a single one-parameter
family, so data on a curve that crosses every characteristic once determine the
solution. Data on a curve that is itself parallel to a characteristic determine
nothing along it and produce a contradiction elsewhere.

### 3.2 Variable coefficient: $u_t + x u_x = 0$

Here $a = x$ and $b = 1$, so $dx/dt = x$, giving $x = x_0\mathrm{e}^{t}$, and $u$
is constant on each characteristic. Solving for the label,
$x_0 = x\mathrm{e}^{-t}$, so

$$\boxed{\ u(x,t) = f\!\left(x\mathrm{e}^{-t}\right)\ } \tag{6}$$

The demonstration verifies (6) to order 2:

```text
           h     |u_t + x u_x|   order
    1.00e-03         2.727e-07        
    5.00e-04         6.817e-08    2.00
    2.50e-04         1.704e-08    2.00
    1.25e-04         4.260e-09    2.00
```

Three physical points, none of them obvious from the equation:

- **For $x > 0$ the characteristics diverge.** An initial feature at $x_0$
  appears later at $x_0\mathrm{e}^t$, so the observable is a *stretched* version of
  the input. Reading the equation as a model, one measures a stretched signal and
  must un-stretch it to recover the source — the same logic as a rarefaction fan
  in gas dynamics or a dispersing flood wave.
- **Nothing crosses $x = 0$.** The coefficient vanishes there, so $x = 0$ is a
  characteristic and the left and right halves of the domain never exchange
  information.
- **The shape is preserved in the characteristic coordinate.** This is the
  defining property of a transport equation and the reason kinematic-wave models
  are useful at all: the transformation from measurement to source is a change of
  variable, not an inversion.

## 4. Nonlinearity, steepening and shocks

### 4.1 Characteristics of $u_t + u u_x = 0$

For the inviscid Burgers equation $u_t + uu_x = 0$ (conservation form
$u_t + (\tfrac12u^2)_x = 0$), equation (3) gives

$$\frac{dx}{dt} = u, \qquad \frac{du}{dt} = 0
\qquad\Longrightarrow\qquad
x = x_0 + u_0(x_0)\,t, \qquad u = u_0(x_0) . \tag{7}$$

Each point of the initial profile travels at its own speed, equal to its own
value. If $u_0$ decreases with $x$, the faster-moving data on the left catch up
with the slower data on the right, and the profile steepens. The map $x_0\mapsto x$
has derivative

$$\frac{dx}{dx_0} = 1 + u_0'(x_0)\,t , \tag{8}$$

so it stops being invertible at the earliest time

$$t_s = -\frac{1}{\min u_0'} , \tag{9}$$

and the gradient, obtained by differentiating $u = u_0(x_0)$ with respect to the
physical coordinate, is

$$u_x = \frac{u_0'(x_0)}{1 + u_0'(x_0)\,t} . \tag{10}$$

**This is the cleanest diagnostic in the whole lesson.** The formula is exact,
elementary, and immediately falsifiable: for $u_0 = \sin x$ on $[0,2\pi)$,
$\min u_0' = -1$ at $x_0 = \pi$, so $t_s = 1$ and the largest slope is

$$\max\lvert u_x\rvert = \frac{1}{1 - t} , \qquad\text{attained at } x = \pi ,
\tag{11}$$

because the characteristic starting at $x_0 = \pi$ has $u_0(\pi) = 0$ and
therefore does not move. The demonstration solves the equation upwind and
measures the maximum slope:

```text
        t   exact 1/(1-t)    scheme max|u_x|     ratio
     0.20        1.250000           1.249067    0.9993
     0.40        1.666667           1.662893    0.9977
     0.60        2.500000           2.484579    0.9938
     0.80        5.000000           4.886867    0.9774
     0.90       10.000000           9.290199    0.9290
     0.95       20.000000          16.097461    0.8049
```

The scheme reproduces the divergence to within 0.1 % at early times and
under-predicts it as $t\to1$, by 20 % at $t = 0.95$. That degradation is
numerical, not physical: the scheme's own viscosity smooths the peak over a few
cells, so the sharper the true feature the larger the relative shortfall. An
analyst who reported the numerical value as the physical gradient would report a
finite slope where the exact solution has none.

### 4.2 Why the classical solution ends, and what replaces it

At $t = t_s$ the map (8) has a vanishing derivative: two different initial points
arrive at the same $x$, and $u$ would have to take two values there. Beyond it the
characteristic map is many-to-one and $u$ is **multivalued**. The PDE in its
differential form has no solution at all.

The resolution is to go back to the integral (conservation) statement, which
remains meaningful across a discontinuity. A **weak solution** is a function that
satisfies

$$\frac{d}{dt}\int_{x_1}^{x_2} u\,dx + f(u(x_2,t)) - f(u(x_1,t)) = 0
\qquad\text{for all intervals} , \tag{12}$$

which is the statement that $u$ is conserved in the presence of a jump. Across a
discontinuity with left and right states $u_L$, $u_R$, this forces the jump to
travel at the **Rankine–Hugoniot speed**

$$s = \frac{f(u_R) - f(u_L)}{u_R - u_L} . \tag{13}$$

For Burgers, $f(u) = \tfrac12u^2$, so $s = \tfrac12(u_L + u_R)$: the shock speed
is the average of the states, not either value. Two further points complete the
picture:

- **Weak solutions are not unique.** Multiple candidate discontinuities satisfy
  (12); the physically relevant one is selected by an **entropy condition**, which
  for a convex flux says $u_L > u_R$ (compression, not expansion). A rarefaction —
  an expansion fan — spreads continuously instead.
- **Smoothing restores uniqueness.** Adding $\nu u_{xx}$ with $\nu > 0$ makes the
  problem parabolic, uniqueness is restored, and the shock has a finite width of
  order $\nu/[u]$. Real geophysical fronts are of this kind: there is no true
  discontinuity, only one that is thin compared with the scale of interest.

This structure — classical solution up to $t_s$, weak solution afterwards, entropy
selection, viscous regularisation — is the template for the weak formulations of
[01-09-08](./08-weak-solutions.md), and it is why a numerical scheme that
converges to the wrong weak solution is a real risk rather than a technicality.

## 5. Numerical solution, and why upwind *looks* like diffusion

### 5.1 The upwind scheme is first order

For $u_t + cu_x = 0$ with $c > 0$, the upwind scheme uses the information from
upstream:

$$u^{n+1}_j = u^n_j - \nu\left(u^n_j - u^n_{j-1}\right), \qquad
\nu = \frac{c\Delta t}{\Delta x} , \tag{14}$$

stable for $0 \le \nu \le 1$, and exact at $\nu = 1$. Measured against the exact
translation of a Gaussian on $\lvert x\rvert \le 2$ with periodic boundaries,
fixed $\nu = 0.8$:

```text
     N         dx  L-infinity error   order
   100   2.00e-02         2.122e-01        
   200   1.00e-02         1.254e-01    0.76
   400   5.00e-03         7.002e-02    0.84
   800   2.50e-03         3.691e-02    0.92
  1600   1.25e-03         1.898e-02    0.96
```

First order — one power of $\Delta x$, not two. The error does not come from a
mistake in the scheme; it comes from the scheme's leading truncation term.

### 5.2 The modified equation: error as diffusion

Expand (14) in Taylor series and eliminate the time derivatives using the PDE:

```text
  u_t + c u_x = (c dx / 2)(1 - nu) u_xx + higher order
```

so the scheme solves an advection–diffusion equation with **numerical diffusion
coefficient**

$$D_{\text{num}} = \frac{c\,\Delta x}{2}(1 - \nu) . \tag{15}$$

This is a *prediction*, not an explanation: a pulse's variance about its own
centre must grow at rate $2D_{\text{num}}$. The demonstration measures it:

```text
    grid N = 200, dx = 0.0100, nu = 0.8
    measured d(variance)/dt          = 2.005220e-03
    predicted 2D = c dx (1 - nu)      = 2.000000e-03
    relative difference               = 0.26 %
```

Three things follow, and they matter beyond this example:

- **A first-order scheme adds physical-looking diffusion.** An "attenuation" seen
  in an upwind advection model is not attenuation; it is (15).
- **The scheme can be made non-dissipative at $\nu = 1$**, where $D_{\text{num}}$
  vanishes and the scheme is exact for constant $c$ — the same alignment of
  stencil and characteristic seen in Section 3.1. But $\nu = 1$ is a knife edge,
  and for variable or nonlinear problems it is unavailable.
- **Refinement eventually pays off, but perversely.** The dissipation
  $\propto\Delta x$ shrinks, so the error shrinks — but the *order* stays 1 until
  the scheme is replaced by a higher-order or (for smooth data) a spectral method.
- **A caution about noise.** A grid-alternating (Nyquist) perturbation is
  *invisible* to a central difference on the same grid, because the two sampled
  neighbours carry the same sign. Testing a differentiation or advection operator
  with alternating noise therefore measures nothing; use random or broadband
  perturbations. This was discovered while checking the differentiation operator in
  [01-09-08](./08-weak-solutions.md), and it is a general trap.

### 5.3 Finite propagation speed

For a compactly supported initial condition, the exact solution of (1) is zero
outside the moving support, and it never widens:

```text
        t                   exact support  exact max outside cone
     0.10                [0.4500, 0.5500]               0.000e+00
     0.25                [0.6000, 0.7000]               0.000e+00
     0.40                [0.7500, 0.8500]               0.000e+00
```

Compare the diffusion equation, where the same compact pulse is nonzero
*everywhere* for any $t > 0$ ([01-09-02](./02-heat-equation.md) measures
$6.1\times10^{-6}$ of leakage after a single step). The three canonical classes of
[01-09-01](./01-classification.md) are thus also three statements about how far a
measurement can constrain a source: a finite cone, a decaying tail, or a global
constraint with no cone at all.

## 6. Kinematic waves in geophysics

The **kinematic wave** approximation replaces a full momentum balance by an
empirical relation between flux and storage, $q = q(u)$, leaving exactly (4). The
governing equation is then first order, and everything in Section 4 applies. It is
used when the flow is dominated by translation and the momentum balance
equilibrates much faster than the wave evolves.

| System | $u$ | Flux relation $q(u)$ | What the characteristics predict |
|---|---|---|---|
| Flood wave in a channel | water depth or discharge | from a rating curve or Manning's law, $q \propto u^{5/3}$ | flood peaks steepen downstream and travel at $q'(u)$, faster than the mean flow |
| Sediment transport | bed elevation | transport rate increasing with shear, often strongly nonlinear | erosion fronts and bedform migration |
| Glacier surge | ice flux | highly nonlinear in thickness | surge fronts and rapid advance |
| Traffic flow | density | $q = u v(u)$ with a maximum | shock waves at congestion, solved numerically everywhere |
| Contaminant transport with sorption | concentration | retarded flux, $q = u/(1 + K_d)$ | fronts travel at the retarded speed, with sharpening for favourable isotherms |
| Waterflood in a reservoir | saturation | fractional-flow curve | Buckley–Leverett fronts, with a shock followed by a rarefaction |

Two modelling cautions that this table makes concrete:

- **The nonlinearity decides whether a feature steepens or spreads.** A convex
  flux with a decreasing profile gives a shock; the same flux with an increasing
  profile gives a rarefaction. Reporting "a front passed" is a statement about
  $q''(u)$, not about the observations alone.
- **The kinematic reduction discards the momentum balance, so it cannot produce
  anything the momentum balance alone would produce.** It will not give a
  backwater curve, a roll wave, or a supercritical-to-subcritical transition,
  because those are momentum effects. Stating the approximation explicitly is
  what distinguishes a kinematic-wave model from a wrong one.

Beyond the kinematic wave, first-order nonlinear PDEs in geophysics include the
**eikonal equation**

$$\lvert\nabla T\rvert = \frac{1}{v(\mathbf{x})} ,$$

which is the high-frequency limit of the wave equation and is itself solved by
characteristics (the rays). It is first order and nonlinear, so the discriminant
classification of [01-09-01](./01-classification.md) does not apply, and
[06-seismology](../../06-seismology/README.md) treats it as the foundation of ray
theory.

## 7. Common mistakes

1. **Applying the discriminant test to a first-order equation.** There is no
   principal part to test. $u_t + cu_x = 0$ is not parabolic; it is a transport
   equation with a single characteristic family.
2. **Solving $dx/dt = c$ but forgetting to carry $u$ along it.** The method has
   two parts: the curve, and the advance of $u$ along it. Half the method gives
   half the answer.
3. **Assuming the classical solution exists for all time.** For nonlinear
   problems it does not. Compute $t_s$ from (9) before interpreting a nonlinear
   simulation beyond it.
4. **Discretising the differential form across a shock.** Use the conservation
   form (4). Non-conservative schemes converge to the wrong weak solution — the
   most consequential failure in the numerical treatment of conservation laws.
5. **Reporting the numerical gradient as the physical gradient near a shock.**
   Section 4.1 shows a 20 % shortfall at $t = 0.95$ that is entirely the scheme's
   viscosity.
6. **Mistaking numerical diffusion for physical attenuation.** Quantify (15)
   before attributing a decay to the medium.
7. **Using one boundary condition at an outflow boundary.** The information
   travels one way, so the outflow boundary needs no condition in the continuous
   problem; imposing one by habit over-specifies the problem and can generate a
   spurious reflection.
8. **Using alternating noise to test a grid operator.** It is in the null space of
   central differences and of many stencils. Use broadband noise.
9. **Forgetting that $\nu \le 1$ is a stability limit that depends on
   $\max\lvert u\rvert$ in the nonlinear case.** With $u_t + uu_x = 0$ the time step
   must satisfy $\Delta t \le \Delta x/\max\lvert u\rvert$ at every step.

## 8. Real-world applications

- **Flood forecasting.** The kinematic wave is the backbone of many operational
  river models; the characteristics give the travel time of a flood peak and the
  nonlinearity explains why a hydrograph steepens downstream.
- **Reservoir engineering.** Buckley–Leverett theory predicts the frontal advance
  of a water flood, with a shock at the front and a rarefaction behind it. The
  Rankine–Hugoniot speed (13) is the design equation for breakthrough time.
- **Contaminant hydrology.** Retarded fronts, ion-exchange chromatography and
  reactive transport all reduce to first-order conservation laws with a nonlinear
  flux; the shape of the isotherm decides shock versus spreading.
- **Sedimentology.** Bedform migration and the formation of sharp erosional
  contacts are kinematic-wave phenomena, and the steepening criterion predicts
  which bed features sharpen and which disperse.
- **Glaciology.** Surge fronts and the seasonal propagation of thickness
  perturbations are modelled as kinematic waves with a strongly nonlinear flux.
- **Seismic ray theory.** The eikonal equation is a first-order nonlinear PDE
  solved by characteristics; travel-time tomography inverts its solution.
- **Numerical weather and ocean modelling.** Advection schemes inherit the
  properties of Section 5: first-order upwind is diffusive, and the amount can be
  predicted from (15) before the model is run.

## 9. Further reading

- **Whitham, G. B. (1974). *Linear and Nonlinear Waves*. Wiley.** Level:
  graduate. The canonical treatment of characteristics, kinematic waves and shock
  formation; Chapter 2 alone justifies this lesson.
- **Lighthill, M. J., & Whitham, G. B. (1955). On kinematic waves I. Flood
  movement in long rivers. *Proceedings of the Royal Society A*, 229, 281–316.**
  Level: graduate. The paper that introduced the kinematic wave; the origin of the
  method in hydrology.
- **LeVeque, R. J. (2002). *Finite Volume Methods for Hyperbolic Problems*.
  Cambridge University Press.** Level: graduate. Conservation forms, weak
  solutions, entropy conditions, Riemann problems, and the numerical schemes of
  Section 5.
- **Evans, L. C. (2010). *Partial Differential Equations* (2nd ed.). AMS.**
  Level: graduate. Chapter 3 is the rigorous treatment of characteristics and of
  shock formation; the theory behind Section 4.
- **Buckley, S. E., & Leverett, M. C. (1942). Mechanism of fluid displacement in
  sands. *Transactions of the AIME*, 146, 107–116.** Level: graduate. The
  classical application of a first-order conservation law to two-phase flow.
- **Toro, E. F. (2009). *Riemann Solvers and Numerical Methods for Fluid
  Dynamics* (3rd ed.). Springer.** Level: graduate. The reference for numerical
  methods that get the weak solution right.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Solutions are in
[`exercises/06-characteristics-solutions.md`](./exercises/06-characteristics-solutions.md).

**★1.** Solve $u_t + 3u_x = 0$ with $u(x,0) = \mathrm{e}^{-x^2}$ by
characteristics, and state the value at $x = 10$, $t = 2$.

**★2.** For $u_t + x u_x = 0$ with $u(x,0) = \sin(\pi x)$, compute the solution
at $x = 1$, $t = 1$ and at $x = 2$, $t = \ln 2$. State where the initial feature
at $x_0 = 0.5$ ends up after $t = 1$.

**★3.** Verify by substitution that $u = f(x - ct)$ solves $u_t + cu_x = 0$ for
any differentiable $f$, and state what happens if $f$ has a jump.

**★4.** For $u_t + uu_x = 0$ with $u_0(x) = \sin x$, compute $t_s$ and the
location where the shock first forms. Justify both answers from (9).

**★★5.** For $u_0(x) = 1 - \tanh(x)$, compute $t_s$ from (9) and the profile at
$t = 0.4t_s$ at $x = 0$ and $x = \pm1$. (You may compute the profile
parametrically.)

**★★6.** Derive (10) from (7) and (8). Then show that for
$u_0 = \sin x$ the maximum gradient is $1/(1-t)$, attained at $x = \pi$, and
evaluate it at $t = 0.5$, $0.9$ and $0.99$.

**★★7.** For the upwind scheme with $c = 1$, $\Delta x = 0.01$ and
$\nu = 0.6$, compute $D_{\text{num}}$ from (15) and predict the variance growth
rate of a pulse. Then state the sign of the error you would make if you omitted
the scheme's diffusion when interpreting a measured spread.

**★★8.** Derive the Rankine–Hugoniot speed (13) for $f(u) = \tfrac12u^2$ by
integrating the conservation law over a small box straddling the discontinuity,
and compute the shock speed for $u_L = 1$, $u_R = -0.5$.

**★★★9.** Implement the upwind scheme for $u_t + uu_x = 0$ with
$u_0(x) = \sin x$ on $[0,2\pi)$ and measure the maximum gradient at
$t = 0.3,\ 0.6,\ 0.9$ for three grids. Report the observed convergence of the
gradient to $1/(1-t)$, state how the required grid scales with $t$, and state
which part of your result is a numerical artefact.

**★★★10.** A river reach is modelled with the kinematic wave equation and a
Manning-type flux $q = Ku^{5/3}$. Derive the kinematic wave speed, show that the
nonlinearity is convex, and predict whether a flood hydrograph steepens or spreads
as it travels downstream. Then state two physical effects that the kinematic
reduction cannot represent, and describe a field observation that would falsify
your prediction.

## 11. Self-assessment checklist

- [ ] I can convert a first-order PDE into its characteristic ODE system and solve
      both the linear and the variable-coefficient case.
- [ ] I can verify a characteristic solution by substitution and explain why the
      residual can vanish identically when the steps are equal.
- [ ] I can derive the breaking time and the gradient formula for a nonlinear
      conservation law, and compute them for a given initial profile.
- [ ] I can state why a classical solution ends at $t_s$ and how a weak solution is
      selected.
- [ ] I can derive the modified equation of a first-order scheme and predict its
      numerical diffusion.
- [ ] I can name four geophysical kinematic-wave systems and the assumption the
      reduction makes.
- [ ] I can explain why the first-order problem has one characteristic family and
      therefore needs one initial condition.

## Related lessons

- [01-09-01 Classification of PDEs](./01-classification.md) — why first-order
  equations fall outside the discriminant classification, and what a
  characteristic is.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the smoothing counterpart: the same compact pulse, but with no cone.
- [01-09-03 The Wave Equation and Its Physical Content](./03-wave-equation.md) —
  finite propagation speed and the CFL condition, which this lesson meets again
  through the upwind scheme.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](./08-weak-solutions.md)
  — the weak formulation that makes the shock solutions of Section 4 rigorous.
- [02-physics/04-elasticity-and-continuum-mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — conservation laws in a continuum, in their physical setting.
- [06-seismology](../../06-seismology/README.md) — the eikonal equation and ray
  theory, which are characteristics applied to the high-frequency wave equation.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  kinematic waves in rivers, aquifers and contaminant transport.
