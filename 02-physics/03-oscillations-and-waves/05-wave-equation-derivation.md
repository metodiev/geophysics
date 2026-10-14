---
id: 02-03-05
title: "Deriving the Wave Equation from Continuum Physics"
level: advanced
prereqs: ["02-03-03", "01-06-07", "01-06-04"]
estimated_minutes: 90
tags: [wave-equation, derivation, continuum-mechanics, finite-difference]
---

# Deriving the Wave Equation from Continuum Physics

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the one-dimensional wave equation from Newton's second law applied
   to a continuum element, for a string, an elastic rod and an acoustic medium,
   and state the speed that emerges in each case.
2. **Derive** the three-dimensional scalar wave equation and the divergence form
   $u_{tt} = c^2\nabla^2u$, and say which physical assumption makes a vector
   problem scalar.
3. **Distinguish** the bar speed $\sqrt{E/\rho}$ from the three-dimensional
   P-wave speed $\sqrt{(\lambda+2\mu)/\rho}$ and explain, physically, why the
   geometry changes the answer.
4. **Recognise** the same template in electromagnetism, in heat-diffusion
   (where it fails), and in the elastodynamic equation of module 04.
5. **Write and validate** an explicit finite-difference solver: measure its
   convergence order, verify the Courant stability limit, and compare its output
   with d'Alembert's analytic solution.
6. **Explain** the difference between the dispersion of a lattice and the
   dispersionlessness of the continuum equation.

## Prerequisites

- [02-03-03 Coupled Oscillators and Normal Modes](./03-coupled-oscillators.md)
  — the discrete chain whose continuum limit is taken here.
- [01-06-07 Vector Identities and Their Role in Geophysics](../../01-mathematics/06-multivariable-calculus/07-vector-identities.md)
  — the identities used in the vector derivation.
- [01-06-04 Divergence, Curl and Physical Meaning](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md)
  — the divergence as a source law.

## 1. Why this derivation is the centre of gravity of the module

Everything in seismology, from a refraction survey to a global tomographic model,
is a solution — analytic or numerical — of a wave equation. The equation itself
is not an axiom: it is a consequence of Newton's second law applied to a solid
that resists deformation. Getting the derivation right does three things at once:

- it identifies the **speed** with a ratio of stiffness to density;
- it exposes which **assumptions** are being made, and therefore what a wave
  equation *cannot* describe (dispersion, attenuation, nonlinearity, anisotropy,
  coupling to other fields);
- it shows why the same second-order operator appears in optics, acoustics and
  electromagnetism, so that intuition transfers.

Module 04 completes the programme for a three-dimensional elastic solid and
produces the two seismic speeds. This lesson establishes the machinery on
one-dimensional and scalar problems where every step is visible.

## 2. The continuum hypothesis and the material derivative

The **continuum hypothesis** asserts that the properties of interest vary over
length scales much larger than the microscopic one, so that a density
$\rho(\mathbf{x},t)$ and a displacement field $\mathbf{u}(\mathbf{x},t)$ can be
defined at a point. Its quantitative form in this lesson is

$$\lambda_{\text{wave}} \gg a_{\text{microstructure}} , \tag{1}$$

where $a$ is a lattice spacing, a grain size, or a pore size. When equation (1)
fails the medium is *effectively* dispersive: the wave samples the microstructure
and its speed depends on wavelength. The discrete lattice of lesson 02-03-03 is
the model problem in which equation (1) can be violated at will, and its
dispersion relation quantifies the cost.

In the **Lagrangian** description used here, each material point is labelled by
its rest position $\mathbf{X}$, and

$$\mathbf{u}(\mathbf{X},t) = \mathbf{x}(\mathbf{X},t) - \mathbf{X} , \qquad
\mathbf{a} = \frac{\partial^2\mathbf{u}}{\partial t^2} . \tag{2}$$

Because $\mathbf{X}$ is a label, $\partial/\partial t$ at fixed $\mathbf{X}$ is
the material derivative along the particle path, and it is the ordinary time
derivative in the linearised setting of this module.

## 3. Derivations

### 3.1 Transverse waves on a string

Let a string of linear density $\mu$ be under tension $T$ and let $y(x,t)$ be its
transverse displacement. Two assumptions: the slope is small ($|y_x| \ll 1$) and
the tension is constant to first order in the slope.

Consider the element between $x$ and $x+\Delta x$. Its mass is $\mu\Delta x$ and
its transverse acceleration $y_{tt}$. The transverse force is the difference of
the vertical components of tension at the two ends. For a small angle
$\theta$, $\sin\theta \approx y_x$, so

$$T\left[y_x(x+\Delta x) - y_x(x)\right] \approx T\,y_{xx}\,\Delta x
= \mu\Delta x\,y_{tt} . \tag{3}$$

Dividing by $\Delta x$ and taking the limit,

$$\boxed{\ \mu\,y_{tt} = T\,y_{xx}\ }
\qquad\Longrightarrow\qquad
y_{tt} = c^2y_{xx}, \qquad c = \sqrt{\frac{T}{\mu}} . \tag{4}$$

Three features of this derivation generalise:

1. **The restoring mechanism.** The restoring force came from the *gradient of the
   gradient* of displacement — a second spatial derivative — because the tension
   is nearly constant and only its direction changes.
2. **The speed is a ratio.** $c^2 = T/\mu$: stiffness (tension) over inertia
   (linear density). Every wave speed in physics has this form.
3. **The approximation is explicit.** The step
   $\sin\theta\approx\theta$ is the small-slope condition, and it is exactly the
   small-strain assumption that module 04 makes in the elastic case; its failure
   produces nonlinear waves and shocks.

### 3.2 The divergence form and the non-uniform string

If $\mu$ and $T$ vary with $x$, equation (3) becomes
$\partial_x(Ty_{x}) = \mu y_{tt}$, which is the **divergence form** of the wave
equation. The flux $T y_x$ is the transverse force transmitted across a section.
In three dimensions the corresponding statement is that the time derivative of
the momentum density equals the divergence of a flux — and the divergence
theorem then guarantees that momentum is conserved across any interface, which is
why boundaries and material contrasts can be handled without introducing extra
physics (compare lesson 02-03-08).

### 3.3 Longitudinal waves in a thin rod

Let a rod of cross-section $A$, density $\rho$ and Young's modulus $E$ carry a
longitudinal displacement $u(x,t)$. The strain is $\varepsilon = u_x$ and the
stress is $\sigma = E\varepsilon = Eu_x$ (this is Hooke's law for *uniaxial
stress*, the assumption that the rod is free to contract laterally). The net
force on the element between $x$ and $x+\Delta x$ is
$A[\sigma(x+\Delta x) - \sigma(x)] \approx A E u_{xx}\Delta x$, so Newton's second
law for mass $\rho A\Delta x$ gives

$$\rho\,u_{tt} = E\,u_{xx}
\qquad\Longrightarrow\qquad
c_{\text{bar}} = \sqrt{\frac{E}{\rho}} . \tag{5}$$

**This is not the seismic P-wave speed.** For the granite-like model of lesson
02-04-04 ($\lambda = 25$ GPa, $\mu = 30$ GPa, $E = 73.636$ GPa,
$\rho = 2700$ kg m⁻³) the bar speed is

$$c_{\text{bar}} = \sqrt{\frac{73.636\times10^9}{2700}} = 5222.33\
\mathrm{m\,s^{-1}} , \qquad\text{against}\qquad
v_p = \sqrt{\frac{\lambda+2\mu}{\rho}} = 5610.84\ \mathrm{m\,s^{-1}} . \tag{6}$$

The ratio is $v_p/c_{\text{bar}} = \sqrt{M/E} = 1.0744$, where
$M = \lambda + 2\mu = 85$ GPa is the **constrained** (uniaxial-strain) modulus.
The physical reason is that the rod is allowed to contract laterally, so lateral
inertia is irrelevant and the relevant stiffness is $E$. In a three-dimensional
P wave, the material is *not* free to contract laterally: adjacent material
blocks it, and the lateral stress develops and adds to the restoring force. The
correct modulus is therefore $M = \lambda + 2\mu$, and the speed is higher.

> **Rule to carry forward.** Before using a wave-speed formula, ask what the
> geometry permits. The same material has several "sound speeds"
> ($\sqrt{E/\rho}$ for a bar, $\sqrt{K/\rho}$ for a fluid,
> $\sqrt{(\lambda+2\mu)/\rho}$ and $\sqrt{\mu/\rho}$ in a solid,
> $\sqrt{M/(\rho(1-\nu^2))}$ for a plate), and choosing the wrong one is a
> quantitative error of tens of per cent.

### 3.4 Acoustic waves in a fluid

For a fluid with bulk modulus $K$ and density $\rho$, consider a small element.
Mass conservation and the linearised momentum equation
$\rho\mathbf{v}_t = -\nabla p$ combine with the pressure–density relation
$p = K\rho_1/\rho_0$ (with $\rho_1$ the density perturbation) to give

$$p_{tt} = c^2\nabla^2p, \qquad c = \sqrt{\frac{K}{\rho}} , \tag{7}$$

or, in the divergence form that survives a variable density,

$$\frac{1}{K}p_{tt} = \nabla\cdot\left(\frac{1}{\rho}\nabla p\right) . \tag{8}$$

For water with $K = 2.2$ GPa and $\rho = 1000$ kg m⁻³,
$c = 1483.24$ m s⁻¹ — the familiar sound speed, and the same number that appears
in the elastodynamic treatment when $\mu = 0$. A fluid cannot support shear, so
it has only this one elastic wave.

### 3.5 The three-dimensional scalar wave equation

Combining the divergence form with a constitutive law linear in the field gives

$$\boxed{\ u_{tt} = c^2\nabla^2u\ } , \tag{9}$$

which is the same operator in any number of dimensions. In three dimensions the
spherically symmetric solution is

$$u(r,t) = \frac{1}{r}f(r-ct) + \frac{1}{r}g(r+ct) , \tag{10}$$

and the $1/r$ amplitude decay is a *geometric* statement: the energy in a shell of
radius $r$ is spread over an area $4\pi r^2$, so $u^2r^2$ is constant. In two
dimensions the decay is $1/\sqrt r$, and in one dimension there is no decay at
all. This difference between dimensions is why a borehole sonic log and a
laboratory ultrasonic measurement see different attenuation from the same rock.

### 3.6 d'Alembert's solution and characteristics

Any function of $x - ct$ alone solves equation (9) in one dimension, because
$\partial_t = -c\,\partial_x$ acting on it gives $(\partial_t^2 - c^2\partial_x^2)f
= 0$. The general solution is therefore

$$u(x,t) = f(x-ct) + g(x+ct) , \tag{11}$$

a right-going and a left-going wave that pass through each other without
interaction. Lines of constant $x \pm ct$ are the **characteristics**: information
travels along them at exactly $c$, never faster. For the initial-value problem
with displacement $u(x,0) = \phi(x)$ and velocity $u_t(x,0) = \psi(x)$,

$$u(x,t) = \tfrac12\left[\phi(x-ct) + \phi(x+ct)\right]
+ \frac{1}{2c}\int_{x-ct}^{x+ct}\psi(s)\,ds , \tag{12}$$

which shows explicitly that the value at $(x,t)$ depends only on the initial data
within the interval $[x-ct, x+ct]$ — the **domain of dependence** — and that a
point disturbance influences only the cone $|x-x_0| \le ct$. This is the origin of
the finite speed of information in physics and, numerically, of the Courant
condition (§3.7).

### 3.7 The explicit finite-difference scheme and the Courant condition

The natural discretisation of $u_{tt} = c^2u_{xx}$ is

$$u_j^{n+1} = 2u_j^n - u_j^{n-1} + r^2\left(u_{j+1}^n - 2u_j^n + u_{j-1}^n\right),
\qquad r = \frac{c\,\Delta t}{\Delta x} , \tag{13}$$

which is second order in both variables. Its stability is exactly the statement
that the numerical domain of dependence must contain the physical one: substituting
$u_j^n = \lambda^n e^{ij\theta}$ gives the amplification roots of
$\lambda^2 - 2(1-2r^2\sin^2(\theta/2))\lambda + 1 = 0$, and $|\lambda| = 1$ for all
$\theta$ if and only if

$$\boxed{\ r = \frac{c\,\Delta t}{\Delta x} \le 1\ } . \tag{14}$$

For $r = 1$ the scheme is *exact* for this equation when the initial data are
sampled on the grid. For $r > 1$ the Nyquist component grows by
$\left|2r^2-1\right| + \sqrt{(2r^2-1)^2-1}$ per step. In two and three dimensions
the same argument gives $r \le 1/\sqrt2$ and $r \le 1/\sqrt3$ for this
five-point stencil, because the diagonal of the grid is the longest path
information can take.

## 4. Physical interpretation

**The wave equation is a statement about curvature.** The left side is the
acceleration of a material point; the right side is the difference between the
forces pulled by its two neighbours, i.e. the second spatial derivative of the
displacement. A wave is the medium's way of resolving that mismatch, and the
speed is set by how stiff and how heavy the medium is.

**Non-dispersive by construction.** Equation (9) admits
$u = A\cos(kx-\omega t)$ for every $k$ with $\omega = ck$, so the phase and group
velocities are both $c$. The equation therefore cannot describe a medium whose
speed depends on frequency — including the lattice of lesson 02-03-03, a layered
medium, a viscoelastic solid, or a surface wave. Dispersion in a real medium is
either a microstructure effect (equation (1) failing) or a constitutive effect
(hysteresis and attenuation, lesson 02-04-07).

**Energy flux.** Multiplying equation (9) by $u_t$ and rearranging gives a
continuity equation for energy density
$\tfrac12(u_t^2 + c^2|\nabla u|^2)$ with flux $-c^2u_t\nabla u$. Energy is
transported, not created: the same statement as the interference bookkeeping of
lesson 02-03-06.

## 5. Assumptions and regime of validity

| Assumption | Written form | What fails outside it |
|---|---|---|
| Continuum | $\lambda \gg a$ | Lattice/effective-medium dispersion, scattering |
| Small strain | $|\nabla\mathbf{u}| \ll 1$ | Nonlinear wave steepening, shock formation, harmonic generation |
| Linear, instantaneous stress–strain | $\sigma = C\varepsilon$ | Anelasticity, hysteresis, attenuation and its dispersion (02-04-07) |
| Homogeneous, isotropic body | constant $c$ | Reflection and refraction (02-03-08), anisotropy (02-04-06) |
| Infinite medium | no boundaries | Standing waves, waveguides, surface waves (02-03-06) |
| Scalar field | one component | Vector elasticity: two speeds, mode conversion (02-04-05) |
| No body force | $F=0$ | Source radiation, seismic moment (06-seismology) |

Two of these deserve emphasis because they are *not* small corrections in the
field. First, "homogeneous" fails at every geological interface: the velocity
contrast between shale and limestone is 30–50 per cent, and the reflection
coefficient is measured in tens of per cent. Second, "scalar" fails wherever a
shear modulus exists: the same equation appears twice in module 04 with two
different speeds, and mode conversion at an interface is not a correction but a
first-order effect.

## 6. Units and dimensional analysis

- Equation (4): $[T/\mu] = \mathrm{(kg\,m\,s^{-2})/(kg\,m^{-1})} =
  \mathrm{m^2\,s^{-2}}$ ✓.
- Equation (5): $[E/\rho] = \mathrm{Pa/(kg\,m^{-3})} = \mathrm{m^2\,s^{-2}}$ ✓.
- Equation (7): $[K/\rho]$ has the same units ✓.
- $c\,u_{xx}$: $\mathrm{m\,s^{-1}\times m^{-1}} = \mathrm{s^{-2}}$, matching
  $u_{tt}$ ✓. The wave equation is dimensionally transparent: both sides are
  accelerations.
- The Courant number is dimensionless: $\mathrm{m\,s^{-1}\times s/m}$ ✓. Any
  numerical condition stated as "$\Delta t < \text{something}$" without
  $\Delta x$ is wrong; any condition stated as a dimensionless number is
  checkable.

## 7. Python demonstration

[`code/wave_equation_derivation_demo.py`](./code/wave_equation_derivation_demo.py)
verifies the lattice limit, the continuum solution, the convergence order, the
Courant condition and the measured speed. Observed output:

```text
lattice spacing a = 1.0 m, continuum speed c = 1.0 m/s
    k a     v_ph/c      v_g/c    omega/(c k) - 1
  0.010   0.999996   0.999988         -4.167e-06
  0.100   0.999583   0.998750         -4.166e-04
  1.000   0.958851   0.877583         -4.115e-02
  3.142   0.636620   0.000000         -3.634e-01
```

```text
   k0 a  v_g formula  v_g measured  rel. error   envelope width (a)
  0.100     0.998750      0.999780   1.031e-03   314.32 ->  316.39
  0.500     0.968912      0.971240   2.402e-03    62.87 ->   73.05
  1.000     0.877583      0.905175   3.144e-02    31.43 ->   47.64
```

```text
   dx (m)     dt (s)   steps   max|error|   order
  0.05000   0.025000      60    1.833e-03     nan
  0.02500   0.012500     120    4.570e-04   2.004
  0.01250   0.006250     240    1.144e-04   1.998
  0.00625   0.003125     480    2.859e-05   2.000
  0.00313   0.001563     960    7.148e-06   2.000
```

```text
     r    dt (s)  max|u| at t=0  max|u| after 200 steps  growth/step       theory
  0.50   0.01000       0.841970            2.065588e-01     0.992999     1.000000
  0.90   0.01800       0.487982            2.503193e-01     0.996668     1.000000
  1.00   0.02000       0.509158            5.000000e-01     0.999909     1.000000
  1.05   0.02100       0.523639            3.165698e+52     1.836146     1.877328
  1.20   0.02400       0.571320            2.022006e+106     3.409923     3.471980
```

```text
right-going pulse peak at x = 5.999925 m after t = 1.000000 s
speed = (x_peak - 5)/t = 0.999924806 m/s (input c = 1.000000000 m/s, error 7.52e-05)
    k =    1.0 1/m: u_tt =      -1.000000, c^2 u_xx =      -1.000000, ratio = 1.000000000000
    k =  100.0 1/m: u_tt =  -10000.000000, c^2 u_xx =  -10000.000000, ratio = 1.000000000000
```

### What to observe

| Observation | Consequence |
|---|---|
| At $ka = 0.01$ the lattice phase velocity is $c$ to $4\times10^{-6}$ | The continuum equation is the long-wavelength limit, and the error is $O((ka)^2)$ |
| At $ka = \pi$ the group velocity is exactly zero | The lattice cannot transport energy at a wavelength of two spacings: the short-wavelength cut-off is physical, not numerical |
| The measured packet speed agrees with $d\omega/dk$ to 0.1 % at $ka = 0.1$ and 3 % at $ka = 1.0$, where the packet spreads by 50 % | Measuring a group velocity assumes a narrow band; where the packet spreads, the measurement itself must be qualified |
| The convergence order is 2.004, 1.998, 2.000, 2.000 | The scheme is second order; quoting the measured rate rather than the textbook value is the discipline that catches coding errors |
| At $r = 1$ the scheme is exact (the maximum is unchanged at 0.500000, and the pulse arrives with the right amplitude); at $r = 1.05$ it grows by 1.836 per step against the predicted 1.877 | The Courant condition is a hard stability boundary, and the predicted growth factor matches to 2 % |
| The pulse speed measured from the numerical solution is 0.999924806c (error $7.5\times10^{-5}$) | The discretisation preserves causality and speed; the small error is the grid dispersion of a finite-bandwidth pulse |
| For a plane wave the ratio $u_{tt}/(c^2u_{xx})$ is 1 to twelve digits for every $k$ | The equation is non-dispersive *by construction*, as §3.6 asserts |

> **Breaking exercise.** Set `r = 1.5` in part 4 and predict, before running,
> how many steps it takes for the maximum to exceed $10^{10}$. Then check whether
> the observed growth factor matches $\left|2r^2-1\right|+\sqrt{(2r^2-1)^2-1}$.

## 8. Common mistakes

1. **Using the bar speed for a three-dimensional wave (or vice versa).** The
   granite example above is a 7 per cent error, and in soft rock the difference
   can be larger; always state the geometry the formula assumes.
2. **Forgetting the small-strain assumption.** Equation (4) is linear only for
   small slopes; a breaking wave, a shock in air, and nonlinear site response all
   sit outside it.
3. **Believing the wave equation is derivable without a constitutive law.**
   Newton's second law alone gives an equation containing stress; the *material*
   enters through the relation between stress and strain. That is exactly where
   anisotropy, anelasticity and nonlinearity are introduced, and module 04 does it
   properly.
4. **Assuming a scalar equation describes a vector field.** The elastic problem
   is a vector equation; the scalar wave equation is a *model* for it, valid for
   one polarisation in a homogeneous medium.
5. **Choosing $\Delta t$ from accuracy alone.** Stability constrains it first;
   a scheme can be accurate and unstable.
6. **Confusing numerical dispersion with physical dispersion.** A second-order
   scheme *is* dispersive; the measured pulse-speed error above is a numerical
   artefact, and it must be shown to be smaller than the physical effect being
   studied.
7. **Ignoring the dimensional dependence of amplitude decay.** A $1/r$ law in
   three dimensions is geometric, not attenuative; fitting it as attenuation
   would overestimate $Q$'s inverse.

## 9. Real-world applications

- **Seismic forward modelling.** Every finite-difference seismic code is
  equation (13) in more dimensions, with the elastic right-hand side of module 04
  and with absorbing boundaries; the grid dispersion and the Courant limit are
  the first two things checked in any modelling study.
- **Borehole and laboratory acoustics.** A sonic log measures $v_p$ in a geometry
  close to a fluid-filled borehole, where the relevant speed is not simply
  $\sqrt{(\lambda+2\mu)/\rho}$; the geometry check of §3.3 is exactly the issue.
- **Ultrasonic testing.** Bar and plate speeds $\sqrt{E/\rho}$ and
  $\sqrt{M/(\rho(1-\nu^2))}$ are the ones measured in a laboratory specimen,
  which is why a laboratory velocity must be converted before it is compared with
  a seismic one.
- **Tsunami propagation.** Long gravity waves in shallow water obey
  $c = \sqrt{gh}$ with $h$ the water depth — a wave equation with a speed set by
  the depth, and the basis of tsunami travel-time charts.
- **GPR and electromagnetic diffusion.** In a low-loss dielectric the GPR
  equation is a wave equation with $c = 1/\sqrt{\mu\varepsilon}$; in a conductive
  ground the same equation acquires a first-derivative term and becomes a
  *diffusion* equation, which is a different physical regime entirely. The
  mathematics module's partial-differential-equations sequence treats the
  diffusion and wave equations side by side; in this curriculum the physical
  distinction is made in [02-07 Electromagnetism](../07-electromagnetism/README.md).
- **Numerical modelling practice.** [PyGMT](https://pygmt.org) and
  [ObsPy](https://docs.obspy.org) are used to visualise and compare modelled and
  observed waveforms, which is how the validation in §7 is done in practice.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Chapter 2 derives the elastodynamic equation and the
  wave equation from continuum mechanics; the scalar case treated here is its
  one-component shadow. Level: advanced.
- **Lay, T., & Wallace, T. C. *Modern Global Seismology* (Academic Press, 1995).**
  The wave equation and its solutions, at the level of this lesson. Level:
  intermediate.
- **Gubbins, D. *Seismology and Plate Tectonics* (Cambridge University Press,
  1990).** A concise derivation of the wave equation from a string and a rod,
  exactly as here, and a clear statement of the geometry dependence of the speed.
  Level: intermediate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** Propagation in field terms:
  wavelengths, resolution and the practical consequences. Level: intermediate.
- **LeVeque, R. J. *Finite Difference Methods for Ordinary and Partial
  Differential Equations* (SIAM, 2007).** The convergence and stability analysis
  of §3.7, done rigorously. Level: graduate.
- **Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on
  Physics*, Vol. I, Chapters 47–49.** The physical origin of waves, with an
  emphasis on why the second derivative appears. Level: beginner to intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Coupled Oscillators and Normal Modes](./03-coupled-oscillators.md) — the
  discrete chain whose limit this lesson takes.
- [04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](./04-wave-basics.md)
  — the kinematic vocabulary used here.
- [06 Superposition, Interference and Standing Waves](./06-superposition-interference.md)
  — the linearity that equation (9) guarantees.
- [07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md) —
  what the continuum equation cannot describe.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the three-dimensional vector version, and the P and S speeds.
- The mathematics module's partial-differential-equations sequence treats the
  wave equation mathematically: separation of variables, well-posedness and
  uniqueness. It is written as part of
  [01-mathematics](../../01-mathematics/README.md) and is the natural companion
  to this lesson.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — how
  the solvers are built at scale.

Exercises:
[`exercises/05-wave-equation-derivation-exercises.md`](./exercises/05-wave-equation-derivation-exercises.md)
and
[`exercises/05-wave-equation-derivation-solutions.md`](./exercises/05-wave-equation-derivation-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\mu y_{tt} = Ty_{xx}$ for a string from a free-body diagram
      and identify every approximation used. (Section 3.1)
- [ ] I can derive the bar speed $\sqrt{E/\rho}$ and explain why it is not the
      P-wave speed. (Section 3.3)
- [ ] I can state the constrained modulus $M$ and why lateral inertia raises the
      three-dimensional speed. (Section 3.3)
- [ ] I can derive the acoustic wave equation and its speed $\sqrt{K/\rho}$.
      (Section 3.4)
- [ ] I can write d'Alembert's solution and use it to state the domain of
      dependence. (Section 3.6)
- [ ] I can explain why the continuum wave equation is non-dispersive and why a
      lattice is not. (Section 4, §7)
- [ ] I can write the explicit scheme, derive the Courant condition and explain
      it as a domain-of-dependence statement. (Section 3.7)
- [ ] I can measure the convergence order of a scheme and state why the measured
      value matters more than the theoretical one. (Section 7)
- [ ] I can list the five assumptions of the wave equation and name a phenomenon
      that violates each. (Section 5)
