---
id: 06-01-01
title: "From Hooke's Law and Newton to the Elastodynamic Equation"
level: graduate
prereqs: ["02-04-05", "02-04-03", "01-06-07"]
tags: [seismology, wave-equation, elastodynamics, derivation, navier-cauchy]
---

# From Hooke's Law and Newton to the Elastodynamic Equation

This is the lesson where seismology stops being a collection of formulas and
starts being one equation. Everything later in the folder — Snell's law,
Zoeppritz, surface waves, ray theory — is a consequence of what is derived
here. The derivation is therefore given in full, with the assumption that
admits each term stated at the moment the term enters, and with the result
checked against a numerical solution of the same equation.

Run the demonstration before reading the derivation, and again afterwards:

```
.venv/bin/python 06-seismology/01-elastic-wave-propagation/code/wave_equation_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** the elastodynamic equation of motion from Newton's second law,
   the strain–displacement relation and the constitutive law, stating which
   assumption each step uses.
2. **Reduce** the vector equation to the Navier–Cauchy form
   $\rho\ddot{\mathbf u} = (\lambda+\mu)\nabla(\nabla\cdot\mathbf u) +
   \mu\nabla^2\mathbf u$ and explain why the two Lamé constants enter in two
   different combinations.
3. **Identify** the $P$ and $S$ speeds
   $v_p=\sqrt{(\lambda+2\mu)/\rho}$ and $v_s=\sqrt{\mu/\rho}$ from the reduced
   equations, and say which assumption makes each one a constant.
4. **Verify** the derivation numerically: substitute an analytic plane wave
   into the full equation and measure the residual, then solve the same
   equation by finite differences and measure the propagation speed it
   produces.
5. **Distinguish** the approximations that the derivation makes from the
   approximations that it does not: small strain, linearity, isotropy,
   homogeneity, and the neglect of attenuation are five separate assumptions
   with five separate failure modes.

## Prerequisites

- [02-04-01 Stress: Traction, Cauchy Stress Tensor and
  Equilibrium](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  — traction, $\sigma_{ij}$, and the meaning of $\sigma_{ij,j}$.
- [02-04-02 Strain: Infinitesimal Strain Tensor and
  Compatibility](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md)
  — $\varepsilon_{ij} = \tfrac12(u_{i,j}+u_{j,i})$ and the small-strain
  assumption.
- [02-04-03 Constitutive Laws and Generalised Hooke's
  Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md)
  — $\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$ and the isotropic reduction.
- [01-06-07 Vector Identities and Their Role in
  Geophysics](../../01-mathematics/06-multivariable-calculus/07-vector-identities.md)
  — $\nabla\times\nabla\times\mathbf u =
  \nabla(\nabla\cdot\mathbf u)-\nabla^2\mathbf u$, which is used in §4.

[02-04-05 Elastodynamic Equation of Motion and Wave
Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
derives the same equation from the continuum-mechanics side and should be read
as the companion; this lesson re-derives it in the notation seismology uses and
adds the numerical verification.

## 1. Intuition: one vector equation, three ingredients

A rock deforms because forces act on it, and it resists deformation because it
is elastic. Write that sentence three times in mathematics and you have the
subject:

| English | Mathematics | Where it comes from |
|---|---|---|
| how fast a particle accelerates | $\rho\,\ddot u_i$ | Newton, per unit volume |
| the force per unit volume | $\sigma_{ij,j}$ | traction on the faces of a small cube |
| how much the rock strains | $\varepsilon_{ij} = \tfrac12(u_{i,j}+u_{j,i})$ | geometry only |
| how strain becomes stress | $\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$ | Hooke, materials only |

Combining them eliminates $\sigma_{ij}$ and $\varepsilon_{ij}$ and leaves a
single equation for the displacement field $\mathbf u(\mathbf x,t)$. That
equation is the whole of elastic seismology. Its one distinguishing feature,
compared with the scalar wave equation of
[02-03-05](../../02-physics/03-oscillations-and-waves/05-wave-equation-derivation.md),
is that it carries **two** wave speeds, because a solid resists both volume
change and shape change, whereas a fluid or a stretched string resists only
one.

## 2. Precise definitions and the three ingredients

### 2.1 Kinematics

The **displacement** $u_i(\mathbf x,t)$ is the vector from a particle's
reference position to its current position. The **infinitesimal strain tensor**
is

$$\varepsilon_{ij} = \tfrac12\left(\partial_j u_i + \partial_i u_j\right)
= \tfrac12\left(u_{i,j} + u_{j,i}\right), \tag{1}$$

and the **rotation tensor** is the antisymmetric remainder,

$$\omega_{ij} = \tfrac12\left(u_{i,j} - u_{j,i}\right), \qquad
u_{i,j} = \varepsilon_{ij} + \omega_{ij}. \tag{2}$$

Only $\varepsilon_{ij}$ stores energy; $\omega_{ij}$ describes a rigid rotation
of the neighbourhood. This is why $\sigma_{ij}$ may be taken symmetric and why
$\varepsilon_{ij}$ alone appears in the constitutive law.

### 2.2 Dynamics

For a volume $V$ with surface $S$, Newton's second law is

$$\int_V \rho\,\ddot u_i\,dV = \int_S \sigma_{ij}n_j\,dS + \int_V f_i\,dV, \tag{3}$$

where $f_i$ is a body force per unit volume. Using the divergence theorem on the
surface term and requiring the result for every volume gives the **equation of
motion**

$$\rho\,\ddot u_i = \sigma_{ij,j} + f_i. \tag{4}$$

Setting $\ddot u_i = 0$ and $f_i = 0$ recovers the equilibrium equations
$\sigma_{ij,j}=0$ of
[02-04-01](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md);
that is the static special case of what follows.

### 2.3 Constitutive law

For a linear elastic solid, $\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$ with
$C_{ijkl}=C_{jikl}=C_{klij}$. **Isotropy** — the assumption that the material
behaves identically in every direction — leaves only two independent constants:

$$C_{ijkl} = \lambda\,\delta_{ij}\delta_{kl} + \mu\left(\delta_{ik}\delta_{jl}
+ \delta_{il}\delta_{jk}\right), \tag{5}$$

and therefore

$$\sigma_{ij} = \lambda\,\varepsilon_{kk}\,\delta_{ij} +
2\mu\,\varepsilon_{ij}. \tag{6}$$

The constant $\mu$ is the **shear modulus**, the resistance to shape change at
constant volume; $\lambda$ has no such one-line physical meaning, and that is
the first sign that it will appear in an awkward combination. The combination
$K = \lambda + \tfrac23\mu$ is the **bulk modulus**, the resistance to volume
change.

## 3. Derivation, step by step

**Step 1 — eliminate the stress.** Substitute (6) into (4), taking the body
force to be zero (a seismic source is a localised condition, not a distributed
force; it re-enters as an initial or boundary condition):

$$\rho\,\ddot u_i = \partial_j\left(\lambda\,\varepsilon_{kk}\delta_{ij}\right)
+ \partial_j\left(2\mu\,\varepsilon_{ij}\right). \tag{7}$$

**Step 2 — assume homogeneity.** If $\lambda$ and $\mu$ are the same
everywhere, they pass outside the derivatives:

$$\rho\,\ddot u_i = \lambda\,\partial_i\varepsilon_{kk}
+ 2\mu\,\partial_j\varepsilon_{ij}. \tag{8}$$

This is the point where a *layered* Earth is excluded. A medium with
depth-dependent moduli needs $\partial_j\lambda$ and $\partial_j\mu$ terms; they
are what produce reflections from smooth gradients, and they are dropped here
and restored in [06-01-04](./04-body-wave-arrivals.md).

**Step 3 — substitute the strain.** With (1),

$$\partial_i \varepsilon_{kk} = \partial_i \partial_k u_k
= \partial_i(\nabla\cdot\mathbf u). \tag{9}$$

For the second term write the symmetric part explicitly:

$$\partial_j\varepsilon_{ij} = \tfrac12\partial_j\left(u_{i,j}+u_{j,i}\right)
= \tfrac12\nabla^2u_i + \tfrac12\partial_i(\nabla\cdot\mathbf u), \tag{10}$$

where $\partial_j\partial_j u_i = \nabla^2 u_i$ by definition of the Laplacian
acting on a vector component. Note carefully that no assumption was needed to
swap $\partial_j\partial_i = \partial_i\partial_j$ beyond differentiability.

**Step 4 — collect.** Substituting (9) and (10) into (8),

$$\rho\,\ddot u_i = \lambda\,\partial_i(\nabla\cdot\mathbf u)
+ \mu\,\nabla^2 u_i + \mu\,\partial_i(\nabla\cdot\mathbf u), \tag{11}$$

that is

$$\boxed{\;\rho\,\ddot{\mathbf u} =
(\lambda+\mu)\,\nabla(\nabla\cdot\mathbf u) + \mu\,\nabla^2\mathbf u\;}.
\tag{12}$$

This is the **Navier–Cauchy equation**. The two Lamé constants appear in two
different combinations, and the whole of §4 is the consequence of that.

**Step 5 — an equivalent form.** Using the vector identity
$\nabla^2\mathbf u = \nabla(\nabla\cdot\mathbf u) - \nabla\times\nabla\times\mathbf u$
(derive it in components, or see
[01-06-07](../../01-mathematics/06-multivariable-calculus/07-vector-identities.md)),

$$\rho\,\ddot{\mathbf u} = (\lambda+2\mu)\nabla(\nabla\cdot\mathbf u)
- \mu\,\nabla\times\nabla\times\mathbf u. \tag{13}$$

This form is written so that the two terms are separately recognisable: the
first is the **volumetric** (dilatational) response, driven by
$\nabla\cdot\mathbf u$ and controlled by $\lambda+2\mu$; the second is the
**deviatoric** (shear) response, driven by $\nabla\times\mathbf u$ and controlled
by $\mu$ alone. Equation (12) and equation (13) are the same statement, and both
are used below.

## 4. The two wave equations

**Step 6 — decompose the field.** Write, with the Helmholtz decomposition
derived in full in [06-01-05](./05-wavefield-potentials.md),

$$\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi, \tag{14}$$

with $\nabla\cdot\boldsymbol\psi = 0$ (a gauge choice that removes the
redundancy and makes $\nabla\times\nabla\phi = 0$ the only cross term). Then

$$\nabla\cdot\mathbf u = \nabla^2\phi, \qquad
\nabla\times\mathbf u = -\nabla^2\boldsymbol\psi. \tag{15}$$

**Step 7 — separate by taking divergence and curl.** Because
$\nabla\cdot(\nabla\times\boldsymbol\psi)=0$ and
$\nabla\times(\nabla\phi)=0$, the two operations project onto different parts:

- Taking $\nabla\cdot$ of (13) kills the curl term and gives

$$\rho\,\partial_t^2(\nabla^2\phi) = (\lambda+2\mu)\nabla^2(\nabla^2\phi)
\quad\Longrightarrow\quad
\nabla^2\left[\rho\,\ddot\phi - (\lambda+2\mu)\nabla^2\phi\right] = 0. \tag{16}$$

A function whose Laplacian vanishes everywhere must be harmonic; a harmonic
field cannot be a localised wave, so the bracket must vanish, giving

$$\ddot\phi = \frac{\lambda+2\mu}{\rho}\,\nabla^2\phi
\;\equiv\; v_p^2\,\nabla^2\phi. \tag{17}$$

- Taking $\nabla\times$ of (13) kills the gradient term and gives

$$\ddot{\boldsymbol\psi} = \frac{\mu}{\rho}\nabla^2\boldsymbol\psi
\;\equiv\; v_s^2\,\nabla^2\boldsymbol\psi. \tag{18}$$

Equations (17) and (18) are the **P** and **S** wave equations, with

$$\boxed{\;v_p = \sqrt{\frac{\lambda+2\mu}{\rho}}, \qquad
v_s = \sqrt{\frac{\mu}{\rho}}\;}. \tag{19}$$

**Step 8 — why the S equation has no volumetric part.** This deserves its own
paragraph, because it is the physical heart of the derivation. The shear term
in (13) is $-\mu\nabla\times\nabla\times\mathbf u$: it contains no
$\nabla\cdot\mathbf u$ at all, by construction. The divergence of a curl is
identically zero, so $\nabla\cdot(\nabla\times\boldsymbol\psi)=0$ and therefore
$\nabla\cdot\mathbf u = \nabla^2\phi$ is a *pure P quantity*. A pure S wave has
$\phi\equiv0$, hence $\nabla^2\phi=0$, hence $\nabla\cdot\mathbf u = 0$: the S
wave changes shape at constant volume. For a fluid, $\mu=0$; equation (19) then
gives $v_s=0$ and equation (18) collapses to $\ddot{\boldsymbol\psi}=0$, which
has no wave solution at all. **A fluid transmits no shear wave because the
right-hand side of its S-wave equation is identically zero** — not because the
wave is damped, but because there is no restoring force.

## 5. Assumptions, listed separately

Each of these is used at a specific step, and each has an observable
consequence when it fails.

| Assumption | Enters at | Fails when | Where it is relaxed |
|---|---|---|---|
| Small strain, $\|u_{i,j}\|\ll1$ | (1) | near a fault, at high strain | [02-04-08](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md) |
| Linear elasticity | (6) | large amplitude, cracked rock | [05-04-02](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) |
| Isotropy (two constants) | (5) | aligned crystals or cracks | [06-01-08](./08-anisotropic-propagation.md) |
| Homogeneity ($\lambda,\mu$ constant) | (8) | any real layered Earth | [06-01-04](./04-body-wave-arrivals.md) |
| No attenuation | (6) | all real rocks, measurably | [02-04-07](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) |
| No body force | (7) | a seismic source present | §6.3 below |
| Infinitesimal rotations | (2) | rotation > a few degrees | rare in seismology |

## 6. Units and dimensional analysis

Every term of (12) is a force per unit volume. Taking
$[\rho]=\mathrm{kg\,m^{-3}}$, $[u]=\mathrm{m}$, $[t]=\mathrm{s}$:

$$[\rho\,\ddot u] = \mathrm{kg\,m^{-3}}\cdot\mathrm{m}\cdot\mathrm{s^{-2}}
= \mathrm{kg\,m^{-2}\,s^{-2}} = \mathrm{Pa\,m^{-1}},$$

$$[(\lambda+\mu)\nabla(\nabla\cdot\mathbf u)] =
\mathrm{Pa}\cdot\mathrm{m^{-1}} = \mathrm{Pa\,m^{-1}},$$

$$[\mu\nabla^2\mathbf u] = \mathrm{Pa}\cdot\mathrm{m^{-1}}
= \mathrm{Pa\,m^{-1}}.$$

All three agree, so the equation is dimensionally closed. For the speeds,
$[\lambda/\rho] = \mathrm{Pa}/(\mathrm{kg\,m^{-3}})
= \mathrm{kg\,m^{-1}\,s^{-2}}/(\mathrm{kg\,m^{-3}}) = \mathrm{m^2\,s^{-2}}$,
so $v_p$ and $v_s$ are in $\mathrm{m\,s^{-1}}$ as required. A useful check to
carry in the head: **a speed is always the square root of a modulus divided by
a density**, and a modulus divided by a density has the units of velocity
squared, always, whatever the modulus is called.

## 7. Worked examples

### 7.1 The speeds from the moduli

Take a SYNTHETIC material with $\lambda = 25$ GPa, $\mu = 30$ GPa and
$\rho = 2700\ \mathrm{kg\,m^{-3}}$. These three numbers are the entire input;
they are chosen for arithmetic convenience, not quoted from any rock.

$$\lambda+2\mu = 25 + 60 = 85\ \mathrm{GPa}, \qquad
v_p^2 = \frac{85\times10^9}{2700} = 3.148148\times10^{7}\ \mathrm{m^2\,s^{-2}},$$

$$v_p = 5610.8361\ \mathrm{m\,s^{-1}}.$$

$$v_s^2 = \frac{30\times10^9}{2700} = 1.111111\times10^{7}\ \mathrm{m^2\,s^{-2}},
\qquad v_s = 3333.3333\ \mathrm{m\,s^{-1}}.$$

The ratio is $v_p/v_s = 1.683251$. Symbolically
$v_p/v_s = \sqrt{(\lambda+2\mu)/\mu} = \sqrt{2 + \lambda/\mu}$; with
$\lambda/\mu = 0.8333$ this is $\sqrt{2.8333}=1.683251$. Agreement to all printed
digits.

### 7.2 A Poisson solid

If $\lambda=\mu$ (a **Poisson solid**, Poisson's ratio $\nu=1/4$) then
$v_p/v_s = \sqrt3$ exactly, independent of density. Take $\lambda=\mu=30$ GPa,
$\rho=2600\ \mathrm{kg\,m^{-3}}$: $v_p = \sqrt{90\times10^9/2600} =
5883.4839\ \mathrm{m\,s^{-1}}$, $v_s = \sqrt{30\times10^9/2600} =
3396.8254\ \mathrm{m\,s^{-1}}$, ratio $1.7320508 = \sqrt3$ to seven decimals.
The observed ratio for real crustal rocks is *smaller* than $\sqrt3$, which
means $\lambda/\mu<1$: real rocks are not Poisson solids, and this is a
measurable statement rather than a remembered constant.

### 7.3 Dimensional check that catches a real error

Suppose someone writes $v_p = \sqrt{E/\rho}$ where $E$ is Young's modulus.
Dimensionally that is fine — it is a modulus over a density — but it is wrong
for the same reason that $v_p=\sqrt{K/\rho}$ is wrong: both need a shear
contribution. The correct statement is
$v_p = \sqrt{(K+\tfrac43\mu)/\rho}$ (use
$\lambda+2\mu = K+\tfrac43\mu$), which reduces to $\sqrt{E/\rho}$ only in the
limit $\mu\to0$, where $v_p$ is anyway the fluid speed. **Dimensional analysis
cannot catch this error; only the algebra can.**

## 8. The Python demonstration

`wave_equation_demo.py` performs three independent checks.

**1. Dimensional accounting.** Every term of (12) is printed with its units.

**2. Residual of the full equation for an analytic plane wave.** A P-type plane
wave (polarisation along $\mathbf k$) and an S-type plane wave (polarisation
perpendicular to $\mathbf k$) are substituted into (12) with all derivatives
taken by central finite differences. The measured residuals, relative to the
largest term:

| field | grid $n$ | relative residual | ratio on halving $dx$ |
|---|---|---|---|
| P | 48 | $2.834\times10^{-2}$ | — |
| P | 96 | $6.866\times10^{-3}$ | 4.04 |
| P | 192 | $1.694\times10^{-3}$ | 4.03 |
| S | 48 | $7.525\times10^{-3}$ | — |
| S | 96 | $1.837\times10^{-3}$ | 4.07 |
| S | 192 | $4.540\times10^{-4}$ | 4.04 |

The ratio of four on halving the spacing is the signature of second-order
truncation error. The equation is satisfied; what remains is the error of the
numerical derivatives used to test it.

**3. An independent solution of the same equation.** A band-limited wavepacket
with carrier wavenumber $k_0$ is propagated with a leapfrog scheme on a grid of
spacing $\Delta x = 1000$ m (2001 nodes, CFL number 0.5, packet width 40 km).
The measured centroid speed is compared with $v_p$ from (19):

| $k_0\Delta x$ | measured (m/s) | discrete group velocity (m/s) | error vs $v_p$ |
|---|---|---|---|
| 0.6280 | 5402.1965 | 5401.2960 | 3.719 % |
| 0.3140 | 5559.8188 | 5558.8405 | 0.909 % |
| 0.1570 | 5598.8599 | 5597.8620 | 0.213 % |
| 0.0785 | 5608.5971 | 5607.5941 | 0.040 % |
| 0.0393 | 5611.0910 | 5610.0236 | 0.005 % |

The fitted exponent of the error in $k_0\Delta x$ is **2.172**, against the
prediction of 2 from the dispersion analysis of the scheme. The S branch
behaves identically: at $k_0\Delta x = 0.0785$ the measured speed is
3332.0032 m/s against 3333.3333 m/s from (19), an error of 0.040 per cent.

The point of the third check is that the derived speed is not merely written
down: it is **reproduced by a numerical solution of the same partial
differential equation**, and the difference between the two is entirely grid
dispersion, which is measured and shown to vanish at the expected rate.

## 9. Exercises

**★1.** Starting from (4) and (6), carry out Steps 1–4 yourself on paper, and
state for each line which assumption you used.

**★2.** Show that $v_p = \sqrt{(K+\tfrac43\mu)/\rho}$ and hence that
$v_p/v_s = \sqrt{K/\mu+4/3}$. Evaluate both sides for the SYNTHETIC material of
§7.1.

**★3.** Take $\nabla\cdot$ of (13) and confirm that the curl term vanishes
identically. Then take $\nabla\times$ and confirm that the gradient term
vanishes. Explain in one sentence why these two cancellations are the reason a
single vector equation splits into two scalar ones.

**★4.** A fluid has $\mu=0$. Show that (18) has no wavelike solution, and that
(19) gives $v_s=0$ rather than an imaginary speed.

**★★5.** The demonstration reports the relative residual of the Navier–Cauchy
equation for a P wave as $2.834\times10^{-2}$ at $n=48$ and
$6.866\times10^{-3}$ at $n=96$. Predict the value at $n=384$ and check it by
editing the grid list.

**★★6.** Re-run the third check with a packet whose width is halved (20 km) at
fixed $\Delta x = 1000$ m. Predict the new error at the same $k_0\Delta x$ from
the dispersion relation, and state whether the measured value agrees.

**★★7.** Derive the exact discrete group velocity used in the demonstration,
$c_g = c\cos(k\Delta x/2)/\sqrt{1-r^2\sin^2(k\Delta x/2)}$, from the dispersion
relation $\omega = (2/\Delta t)\arcsin\!\big(r\sin(k\Delta x/2)\big)$ with
$r = c\Delta t/\Delta x$.

**★★★8.** A rock is partially saturated: the pore fluid contributes a bulk
modulus $K_f$ but no shear modulus. Using
[05-04-03 Gassmann Fluid
Substitution](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md),
explain which of the two speeds changes and by how much, and state why the S
speed of an isotropic rock depends on the fluid only through the density.

**★★★9.** A medium has $\lambda(z)$ and $\mu(z)$ varying with depth. Carry the
derivatives through Steps 1–4 without assuming homogeneity and show that (12)
acquires the extra terms
$\partial_i\lambda\,\nabla\cdot\mathbf u + 2\,(\partial_j\mu)\,\varepsilon_{ij}$.
Identify the physical process that the first of these describes.

## 10. Common mistakes

1. **Using $v_p=\sqrt{E/\rho}$ or $\sqrt{K/\rho}$ for a solid.** Both are
   fluid limits; see §7.3.
2. **Believing that $\nabla^2\mathbf u$ in (12) acts on the vector, not on each
   component independently.** It does act componentwise, but only because the
   medium is isotropic and homogeneous; in a general anisotropic medium the
   operator becomes $C_{ijkl}\partial_j\partial_l u_k$ and cannot be written
   with a Laplacian at all.
3. **Treating $\lambda$ and $\mu$ as independent measurements.** They are two
   of a family of equivalent pairs; only combinations are observable. See
   [02-04-04](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md).
4. **Forgetting that the derivation used a body force of zero.** A seismic
   source is applied as an equivalent body force $f_i$ in (4); dropping it is a
   choice about where the source lives, not an approximation about the rock.
5. **Assuming that a P wave has no shear deformation.** Particle motion is
   parallel to propagation, but the strain field of a P wave has off-diagonal
   components; what vanishes is the rotation, not the shear strain. The correct
   pair of statements is: P has $\nabla\times\mathbf u = 0$ and
   $\nabla\cdot\mathbf u\ne0$; S has the reverse.
6. **Dropping the heterogeneous terms and then expecting reflections.** A
   smooth gradient reflects only because $\partial_j\mu\ne0$; see
   [06-01-07](./07-scattering-and-heterogeneity.md).

## 11. Real-world applications

- **Locating earthquakes.** The S–P time difference is
  $\Delta(1/v_s - 1/v_p)$; with a measured $v_p/v_s$ this converts a time
  difference into a distance. The ratio itself is a diagnostic of rock type,
  and is derived, not assumed, from (19).
- **Detecting the liquid outer core.** Oldham and Jeffreys used the absence of
  S arrivals beyond a distance to argue for a fluid core. Equation (19) is the
  argument in one line.
- **Full-waveform modelling.** Every finite-difference, spectral-element and
  finite-volume seismic code solves (12) — not (17) and (18) separately —
  because at a heterogeneous interface the two modes couple and the potentials
  are no longer convenient.
- **Ambient-noise interferometry.** The Green's function of (12) between two
  receivers is what noise correlation attempts to recover, which is why
  interferometry works with surface waves first: they are the modes with the
  largest amplitude at the surface.

## 12. Further reading

- [02-04-05 Elastodynamic Equation of Motion and Wave
  Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the same derivation from the mechanics side, with the conversion table
  between $(E,\nu)$, $(K,\mu)$ and $(v_p,v_s)$.
- [02-03-05 Deriving the Wave Equation from Continuum
  Physics](../../02-physics/03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the scalar analogue; read it first if vector calculus is still new.
- [03-10-06 Travel Times with TauP and Phase
  Naming](../../03-scientific-computing/10-obspy-and-seismic-data/06-taup-travel-times.md)
  — the observations that the derived speeds are used to explain, and the
  ObsPy interface used throughout this folder.
- Aki & Richards, *Quantitative Seismology*, Chapter 2 — the standard
  derivation, with the heterogeneous case done in full.
- [https://docs.obspy.org/packages/obspy.taup.html](https://docs.obspy.org/packages/obspy.taup.html)
  — the travel-time engine whose models are queried in the later lessons.

## 13. Related lessons

- [06-01-02 P and S Waves: Particle Motion, Speeds and
  Polarisation](./02-p-and-s-waves.md) — what the two solutions look like.
- [06-01-05 Helmholtz Decomposition and Wavefield
  Potentials](./05-wavefield-potentials.md) — why (14) is always possible and
  what it costs.
- [06-01-04 Reflected, Refracted and Converted Body
  Waves](./04-body-wave-arrivals.md) — what happens when homogeneity is
  dropped.
- [06-01-08 Wave Propagation in Anisotropic
  Media](./08-anisotropic-propagation.md) — what happens when isotropy is
  dropped.
- [06-02-01 Eikonal Equation, Rays and Fermat's
  Principle](../02-ray-theory-and-travel-times/01-eikonal-and-rays.md) — the
  high-frequency limit of this equation.

## 14. Self-assessment

Before moving on, check that you can do each of the following without notes.

- [ ] Write the three ingredients of the derivation from memory, with the
      assumption each carries.
- [ ] Reproduce Steps 1–4 and say where homogeneity was used.
- [ ] Derive (17) and (18) from (13) by taking divergence and curl.
- [ ] Explain in one sentence why the S wave equation has no volumetric term.
- [ ] Derive $v_p/v_s = \sqrt{2+\lambda/\mu}$ and bound it for $\lambda\ge0$.
- [ ] State the units of every term of the Navier–Cauchy equation.
- [ ] Predict what happens to both speeds when $\mu\to0$ at fixed $\rho$.
- [ ] Explain what the measured residual in the demonstration is the residual
      *of*, and why halving $dx$ reduces it by four.
- [ ] Name the five assumptions and one observable that falsifies each.
