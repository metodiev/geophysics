---
id: 02-04-05
title: "Elastodynamic Equation of Motion and Wave Speeds"
level: graduate
prereqs: ["02-04-03", "02-04-04", "01-06-07"]
estimated_minutes: 90
tags: [elasticity, wave-speeds, p-wave, s-wave, elastodynamics]
---

# Elastodynamic Equation of Motion and Wave Speeds

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Navier–Cauchy elastodynamic equation
   $\rho\ddot{\mathbf u} = (\lambda+\mu)\nabla(\nabla\cdot\mathbf u) +
   \mu\nabla^2\mathbf u$ from the equation of motion, the strain–displacement
   relation and the isotropic constitutive law, with every step shown.
2. **Derive** the P- and S-wave speeds

   $$v_p = \sqrt{\frac{\lambda+2\mu}{\rho}}, \qquad v_s = \sqrt{\frac{\mu}{\rho}}$$

   both by Helmholtz decomposition and by direct plane-wave substitution.
3. **Verify** numerically that the Christoffel eigenvalues are the squared wave
   speeds, that the plane-wave residual of the full elastodynamic equation is
   zero, and that a finite-difference simulation propagates at those speeds.
4. **Use** the results to explain why the liquid outer core transmits no S waves,
   why $v_p > v_s$ always, and what happens to both speeds as a rock becomes
   partially fluid-saturated.
5. **State** every approximation in the derivation and the observation that would
   falsify each.

> **This lesson is the mastery checkpoint of the physics folder.** The derivation
> in §3 is required, in full, and the checklist at the end is written to it.

## Prerequisites

- [02-04-03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md)
  — $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}$.
- [02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants](./04-elastic-moduli.md)
  — $M = \lambda+2\mu$, $K = \lambda+2\mu/3$, and the bounds on $v_p/v_s$.
- [01-06-07 Vector Identities and Their Role in Geophysics](../../01-mathematics/06-multivariable-calculus/07-vector-identities.md)
  — $\nabla\times\nabla f = \mathbf{0}$, $\nabla\cdot(\nabla\times\mathbf v) = 0$
  and the vector Laplacian identity.

## 1. What is being derived, and why it is the centre of the subject

A seismogram is a recording of ground motion produced by two kinds of elastic
wave that travel at speeds fixed by the rock's stiffness and density. Those speeds
are not measured constants of nature: they are consequences of Newton's second law
applied to an elastic continuum. Deriving them does four things at once:

- it identifies what a seismic velocity *measures* (a ratio of stiffness to
  density, not a temperature or a composition);
- it explains why there are exactly two body waves in an isotropic solid, and why
  their polarisations differ;
- it shows why a fluid transmits one and not the other, which is how the liquid
  outer core was discovered;
- it provides the forward model for every inversion in seismology.

The derivation is short — three equations combine in about a page — but each step
carries an assumption, and the lesson is written so that the assumptions are
visible at every line.

## 2. The three ingredients

**Ingredient 1: the equation of motion (from stress).** From the balance of
momentum on an arbitrary volume, with the divergence theorem (lesson 02-04-01
§3.3),

$$\partial_j\sigma_{ij} + \rho g_i = \rho\,\ddot u_i , \tag{1}$$

where $\mathbf g$ is the body force per unit mass (gravity) and the dots are
material time derivatives. This is Newton's second law for a continuum.

**Ingredient 2: the strain–displacement relation (kinematics).** For infinitesimal
strain (lesson 02-04-02),

$$\varepsilon_{ij} = \tfrac12\left(u_{i,j}+u_{j,i}\right) . \tag{2}$$

**Ingredient 3: the constitutive law (material).** For a homogeneous, isotropic,
linear elastic solid (lesson 02-04-03),

$$\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij} . \tag{3}$$

Nothing else is used. In particular, no assumption has yet been made about waves,
frequencies, or the existence of two speeds — all of that emerges.

## 3. The derivation, step by step

### Step 1: substitute the constitutive law into the equation of motion

$$\rho\ddot u_i = \partial_j\sigma_{ij} + \rho g_i
= \partial_j\left(\lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}\right)
+ \rho g_i . \tag{4}$$

### Step 2: assume the material is homogeneous

For a *homogeneous* medium, $\lambda$ and $\mu$ are constants and can be taken
through the derivatives. (Their gradients give the scattering terms of a
heterogeneous medium; that case is treated in §7.) Then

$$\rho\ddot u_i = \lambda\,\partial_j\left(\varepsilon_{kk}\delta_{ij}\right)
+ 2\mu\,\partial_j\varepsilon_{ij} + \rho g_i . \tag{5}$$

### Step 3: expand the first term

The first term: $\partial_j(\varepsilon_{kk}\delta_{ij}) =
\partial_i\varepsilon_{kk} = \partial_i u_{k,k}$. So

$$\lambda\partial_i u_{k,k} = \lambda\,\partial_i(\nabla\cdot\mathbf u)
\qquad\text{i.e.}\qquad
\lambda\,\nabla(\nabla\cdot\mathbf u) \ \text{in vector form.} \tag{6}$$

The mean strain (the dilatation) drives a gradient of stress: a compressed region
pushes its neighbours away.

### Step 4: expand the second term

$$
\begin{aligned}
2\mu\,\partial_j\varepsilon_{ij}
&= \mu\,\partial_j\left(u_{i,j}+u_{j,i}\right) \\
&= \mu\left(\partial_j\partial_j u_i + \partial_i\partial_j u_j\right) \\
&= \mu\left(\nabla^2u_i + \partial_i(\nabla\cdot\mathbf u)\right) ,
\end{aligned} \tag{7}
$$

using the commutation of partial derivatives and the definitions
$\partial_j\partial_j = \nabla^2$ and $u_{j,j} = \nabla\cdot\mathbf u$.

### Step 5: combine

Adding equations (6) and (7):

$$\rho\ddot u_i = \lambda\,\partial_i(\nabla\cdot\mathbf u)
+ \mu\left[\nabla^2u_i + \partial_i(\nabla\cdot\mathbf u)\right] + \rho g_i ,$$

and collecting the divergence terms:

$$\boxed{\ \rho\,\ddot{\mathbf u} = (\lambda+\mu)\,\nabla(\nabla\cdot\mathbf u)
+ \mu\,\nabla^2\mathbf u + \rho\,\mathbf g\ } \tag{8}$$

This is the **Navier–Cauchy elastodynamic equation**. It is the complete linear
elastodynamic equation for a homogeneous isotropic solid: a vector equation for a
vector unknown, which is why an elastic solid supports more than one wave type.

Setting $\mathbf g = \mathbf 0$ (taking the gravity field as a static pre-stress,
which it is to the accuracy of the linear theory) leaves the equation used from
here on:

$$\rho\,\ddot{\mathbf u} = (\lambda+\mu)\,\nabla(\nabla\cdot\mathbf u)
+ \mu\,\nabla^2\mathbf u . \tag{9}$$

### Step 6: separate the two modes — the Helmholtz decomposition

Any smooth vector field can be written as the sum of a gradient and a curl
(Helmholtz's theorem):

$$\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi , \qquad
\nabla\cdot\boldsymbol\psi = 0 , \tag{10}$$

where $\phi$ is a scalar potential and $\boldsymbol\psi$ a vector potential with an
arbitrary gauge fixed by the divergence-free condition. Substituting into
equation (9) requires two identities:

$$\nabla\cdot\mathbf u = \nabla^2\phi + \underbrace{\nabla\cdot(\nabla\times
\boldsymbol\psi)}_{=\,0} = \nabla^2\phi , \tag{11}$$

$$\nabla^2\mathbf u = \nabla(\nabla^2\phi) + \nabla\times(\nabla^2\boldsymbol\psi)
\qquad\text{(the vector Laplacian commutes with both operators).} \tag{12}$$

Therefore

$$\nabla(\nabla\cdot\mathbf u) = \nabla(\nabla^2\phi) ,$$

and equation (9) becomes

$$\rho\left[\nabla\ddot\phi + \nabla\times\ddot{\boldsymbol\psi}\right]
= (\lambda+\mu)\nabla(\nabla^2\phi) + \mu\nabla(\nabla^2\phi)
+ \mu\nabla\times(\nabla^2\boldsymbol\psi) .
\tag{13}$$

The two terms on the right with $\nabla(\nabla^2\phi)$ combine with coefficient
$(\lambda+\mu)+\mu = \lambda+2\mu$. Collecting everything on one side:

$$\nabla\left[\rho\ddot\phi - (\lambda+2\mu)\nabla^2\phi\right]
+ \nabla\times\left[\rho\ddot{\boldsymbol\psi} -
\mu\nabla^2\boldsymbol\psi\right] = \mathbf 0 . \tag{14}$$

The two bracketed quantities have *independent* characters: the first is the
gradient of a scalar, the second the curl of a vector, and a field that is
simultaneously a pure gradient and a pure curl of a *localised* field can be
separated by taking the divergence and the curl of equation (14). Taking the
divergence kills the curl term and leaves

$$\nabla^2\left[\rho\ddot\phi - (\lambda+2\mu)\nabla^2\phi\right] = 0
\quad\Longrightarrow\quad
\nabla^2\phi = \frac{1}{v_p^2}\ddot\phi ,
\qquad
\boxed{\ v_p^2 = \frac{\lambda+2\mu}{\rho}\ } \tag{15}$$

(the integration constants are set to zero because the equation must hold
pointwise and independently of the particular solution). Taking the curl kills the
gradient term and leaves

$$\nabla^2\boldsymbol\psi = \frac{1}{v_s^2}\ddot{\boldsymbol\psi} ,
\qquad
\boxed{\ v_s^2 = \frac{\mu}{\rho}\ } \tag{16}$$

**The two wave equations have fallen out of one vector equation.** The scalar
potential obeys a wave equation with speed $v_p$; the vector potential obeys one
with speed $v_s$. Their physical identities, however, are better read from
$\mathbf u$ itself:

- the **gradient part** $\nabla\phi$ has $\nabla\times(\nabla\phi) = \mathbf 0$: it
  is **curl-free**, travels at $v_p$, and carries the dilatation $\nabla\cdot
  \mathbf u = \nabla^2\phi$ — it is the **P (compressional) wave**;
- the **curl part** $\nabla\times\boldsymbol\psi$ has $\nabla\cdot(\nabla\times
  \boldsymbol\psi) = 0$: it is **divergence-free**, travels at $v_s$, and carries
  the rotation — it is the **S (shear) wave**.

### Step 7: verification by direct substitution (the plane-wave check)

The derivation is complete, but a direct check is worth doing because it verifies
both the equation and the solution at once. Substitute a **P wave**

$$\mathbf u = A\,\hat{\mathbf k}\,e^{i(\mathbf k\cdot\mathbf x - \omega t)} ,
\qquad \mathbf k = k\hat{\mathbf k} , \tag{17}$$

so that $\nabla\cdot\mathbf u = i k A e^{i(\cdot)}$ and
$\nabla\times\mathbf u = \mathbf 0$. Then

$$\nabla(\nabla\cdot\mathbf u) = -k^2A\hat{\mathbf k}e^{i(\cdot)} , \qquad
\nabla^2\mathbf u = -k^2A\hat{\mathbf k}e^{i(\cdot)} , \qquad
\ddot{\mathbf u} = -\omega^2A\hat{\mathbf k}e^{i(\cdot)} . \tag{18}$$

Substituting into equation (9) and cancelling the common factor
$-A\hat{\mathbf k}e^{i(\cdot)}$:

$$\rho\omega^2 = (\lambda+\mu)k^2 + \mu k^2 = (\lambda+2\mu)k^2
\quad\Longrightarrow\quad
\omega^2 = \frac{\lambda+2\mu}{\rho}k^2
\quad\Longrightarrow\quad
v_p = \frac{\omega}{k} = \sqrt{\frac{\lambda+2\mu}{\rho}} . \tag{19}$$

Now substitute an **S wave**

$$\mathbf u = A\,\hat{\mathbf e}_s\,e^{i(\mathbf k\cdot\mathbf x-\omega t)} ,
\qquad \hat{\mathbf e}_s\cdot\hat{\mathbf k} = 0 , \tag{20}$$

so that $\nabla\cdot\mathbf u = 0$ (the first term of equation (9) vanishes
identically) and $\nabla^2\mathbf u = -k^2\mathbf u$:

$$\rho\omega^2 = \mu k^2 \quad\Longrightarrow\quad
v_s = \sqrt{\frac{\mu}{\rho}} . \tag{21}$$

**Both derivations agree, and the second is the reason the S speed depends only on
the shear modulus: the longitudinal term is switched off by the polarisation.** The
demo verifies this numerically: the residual of the full elastodynamic equation for
a P or S plane wave is $10^{-16}$ relative to the size of the terms.

### Step 8: the equivalent forms

$$v_p^2 = \frac{M}{\rho} = \frac{K+\frac43\mu}{\rho},
\qquad
v_s^2 = \frac{\mu}{\rho} ,
\qquad
\frac{v_p^2}{v_s^2} = \frac{K}{\mu}+\frac43
= \frac{\lambda+2\mu}{\mu}
= \frac{2(1-\nu)}{1-2\nu} . \tag{22}$$

The form $v_p = \sqrt{M/\rho}$ with $M = \lambda+2\mu$ the **constrained
modulus** is the one to remember: in a P wave the material is in uniaxial strain
at every point (adjacent material prevents lateral expansion), so the relevant
stiffness is the uniaxial-strain modulus, not $E$ and not $K$. This is the
warning of lesson 02-03-05 §3.3, and it is the single most common source of
tens-of-per-cent errors in velocity calculations.

## 4. What the formulas explain

### 4.1 Why $v_p > v_s$ always

$$v_p^2-v_s^2 = \frac{\lambda+\mu}{\rho} = \frac{K+\frac13\mu}{\rho}
> 0 \quad\text{for every stable elastic solid} \tag{23}$$

because stability requires $\mu>0$ and $K>0$ (lesson 02-04-03 §3.3). So

$$\frac{v_p}{v_s} = \sqrt{\frac{K}{\mu}+\frac43} > \frac{2}{\sqrt3} = 1.154701
\qquad\text{unconditionally,} \tag{24}$$

and if $\lambda\ge0$ (equivalently $\nu\ge0$), $v_p/v_s\ge\sqrt2$. The sharpest
statement is equation (23), and it is worth memorising: **adding shear stiffness
raises $v_s$ by more than it raises $v_p$**, because $v_s^2$ contains all of $\mu$
while $v_p^2$ divides $\mu$'s contribution between the two terms — which is why a
material with a large $K/\mu$ ratio (a compliant, high-porosity rock) has a high
$v_p/v_s$ (table in lesson 02-04-04).

### 4.2 Why the liquid outer core transmits no S waves

In a fluid $\mu = 0$. Then

$$v_s = \sqrt{\frac{0}{\rho}} = 0 , \qquad
v_p = \sqrt{\frac{\lambda+2\mu}{\rho}} = \sqrt{\frac{K}{\rho}} . \tag{25}$$

Three consequences, in increasing order of geological importance:

1. **No propagating shear solution exists.** With $\mu = 0$, equation (16)
   becomes $\nabla^2\boldsymbol\psi = 0$ with $\ddot{\boldsymbol\psi}$ unconstrained —
   there is no restoring force, so no wave. The demo's numerical experiment makes
   this concrete: a shear pulse in a medium with $c = 0$ is frozen, its field
   differing from the initial condition by $1.4\times10^{-11}$ after 500 steps.
2. **The P speed measures the bulk modulus and density alone**, so P-wave travel
   times through a fluid region constrain $K/\rho$ without any ambiguity from
   shear.
3. **The S-wave shadow is a material-symmetry observation.** Seismograms beyond
   about 103° from an earthquake show no direct S arrival; the only explanation
   consistent with equations (25) is a region of zero shear modulus along the S
   path — the liquid outer core. This is one of the great observational
   inferences of twentieth-century geophysics, and it is a direct reading of
   $v_s = \sqrt{\mu/\rho}$.

Numerically, for water ($K = 2.2$ GPa, $\rho = 1000$ kg m⁻³) the formulas give
$v_p = 1483.2397$ m s⁻¹ and $v_s = 0$; the demo prints exactly that. For the outer
core the same formula with the appropriate $K$ and $\rho$ gives $v_p$ of order
8–10 km s⁻¹ (the value depends on the Earth model used; quote your source rather
than a remembered number), and $v_s = 0$ exactly.

### 4.3 Polarisation, and why there are two S waves and only one P

For a given propagation direction $\hat{\mathbf k}$, the P displacement is parallel
to $\hat{\mathbf k}$ (one independent direction, hence one P wave), while the S
displacement lies in the plane perpendicular to $\hat{\mathbf k}$ (two independent
directions). In an **isotropic** solid the two S polarisations have the *same*
speed $v_s$ — they are degenerate — which is why the Christoffel eigenvalues are
$v_p^2$ once and $v_s^2$ twice. In an anisotropic solid the symmetry is broken and
the two S speeds differ: that splitting is the subject of lesson 02-04-06 and one
of the standard observations of mantle anisotropy.

The demo's Christoffel check makes the degeneracy explicit: for six different
propagation directions the eigenvalues are $5610.8361$, $3333.3333$,
$3333.3333$ m s⁻¹, with a maximum deviation from the formulas of
$9.1\times10^{-13}$ m s⁻¹.

### 4.4 What happens on partial fluid saturation

Changing the pore fluid changes *two* of the three inputs:

- **$\mu$ is unchanged**, because a fluid cannot support shear stress. Therefore
  $v_s = \sqrt{\mu/\rho}$ changes only through the density term, and since adding
  fluid raises $\rho$, **$v_s$ always decreases** as saturation increases,
  whatever the fluid and whatever the fluid distribution. This is the robust
  statement.
- **$K$ changes**, through the fluid's bulk modulus. For a gas-to-water
  substitution in a sandstone the effect is large and non-monotonic in the
  low-frequency (Gassmann) regime. In the worked example of lesson 02-04-04
  ($\phi = 0.2$, $K_{\text{dry}} = 10$ GPa, $K_{\min} = 36$ GPa, $G = 10$ GPa,
  $K_w = 2.2$ GPa, $K_g = 10$ MPa): $v_s$ falls monotonically from 2171.74 to
  2076.14 m s⁻¹ (4.4 per cent), while $v_p$ falls from 3319.24 to a minimum of
  3201.96 m s⁻¹ and only returns to the dry value at $S_w = 0.9935$. Under
  **patchy** saturation the same model predicts $v_p$ rising above the Gassmann
  value and exceeding the dry value at intermediate saturations (3437.69 m s⁻¹ at
  $S_w = 0.8$, against 3207.75 for the uniform case).

So the complete answer to "what happens on partial saturation" is:

| Quantity | Uniform saturation, low frequency | Uniform saturation, high frequency (squirt) | Patchy saturation |
|---|---|---|---|
| $v_s$ | decreases monotonically with added fluid | decreases (density only; $\mu$ and the fluid distribution do not enter) | decreases identically |
| $v_p$ | falls initially, then rises; minimum in between | laboratory data commonly show a fall at the first few per cent | rises above the Gassmann value; no dip |

and the universal part of the answer — the part that needs no model — is the
$v_s$ column, with the **$v_p$ behaviour depending on frequency and on the fluid
distribution, and therefore requiring measurement**.

## 5. Physical interpretation

**A wave speed is a stiffness-to-density ratio, and nothing else.** $v_p^2 = M/\rho$
and $v_s^2 = \mu/\rho$: no temperature, no pressure, no composition appears. Those
quantities influence the speed only through their effect on the moduli and the
density, which is why interpreting a seismic velocity as a rock property requires a
rock-physics model linking the two (see
[05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).

**The two speeds measure two different moduli.** $v_p$ measures $M$ (or $K$ plus
$\mu$), $v_s$ measures $\mu$. Having both is what allows the elastic constants to
be separated from density, and it is why a survey that records S waves as well as
P waves can do rock physics that a P-only survey cannot.

**The vector equation is the origin of mode conversion.** Because the P and S
parts are independent only in a homogeneous medium, any heterogeneity or boundary
couples them (lesson 02-03-08). This is why an S wave can appear on a vertical
component, and why the elastic reflection problem at an interface needs four
waves.

## 6. Assumptions and regime of validity

| Assumption | Where it entered | What breaks outside it |
|---|---|---|
| Continuum | Ingredient 1 (invoking a stress field) | Microstructure comparable to the wavelength; effective-medium and scattering descriptions |
| Infinitesimal strain | Ingredient 2 | Nonlinear elasticity, harmonic generation; and finite rotation (lesson 02-04-02 §3.4) |
| Linear isotropic elasticity | Ingredient 3 | Anisotropy (lesson 02-04-06); anelasticity (lesson 02-04-07); poroelasticity (two-phase behaviour) |
| Homogeneity | Step 2 (constants through the derivatives) | Heterogeneous media give scattering terms $\nabla\lambda$ and $\nabla\mu$; reflection and refraction (02-03-08) |
| No body force | Step 5 (setting $\mathbf g = 0$) | Gravity acts as a static pre-stress; its dynamic effect is small but nonzero for long-period modes |
| No initial stress | Implicit | A pre-stressed medium has an effective stiffness modified by the stress: the origin of stress-induced anisotropy in the crust |
| Lossless medium | Ingredient 3 (real $\lambda$, $\mu$) | Attenuation and its dispersion (02-03-10, 02-04-07) |

## 7. Units and dimensional analysis

- $[(\lambda+2\mu)/\rho] = \mathrm{Pa/(kg\,m^{-3})} = \mathrm{m^2\,s^{-2}}$ ✓ for
  both speeds.
- Both terms of equation (9) are forces per unit volume:
  $[\rho\ddot u] = \mathrm{kg\,m^{-3}\times m\,s^{-2}} = \mathrm{kg\,m^{-2}\,s^{-2}}$;
  $[\mu\nabla^2u] = \mathrm{Pa\,m^{-1}} = \mathrm{kg\,m^{-1}\,s^{-2}\times m^{-1}}$,
  the same ✓. This check catches a missing factor of $\rho$ — the most common slip
  in the derivation.
- Equation (22): each form of $v_p^2/v_s^2$ must be dimensionless; check
  $K/\mu+4/3$ ✓ and $2(1-\nu)/(1-2\nu)$ ✓ (the numerator and denominator are both
  dimensionless).
- A useful anchor: granite-like $\lambda = 25$ GPa, $\mu = 30$ GPa,
  $\rho = 2700$: $v_p = \sqrt{(25+60)\times10^9/2700} = \sqrt{3.148\times10^7} =
  5610.84$ m s⁻¹, $v_s = \sqrt{30\times10^9/2700} = \sqrt{1.111\times10^7} =
  3333.33$ m s⁻¹, $v_p/v_s = 1.6833$. The demo reproduces these to nine figures.
  Real granite P speeds are typically 5.5–6.0 km s⁻¹, which is consistent with
  this parameter set — the model is a plausible rock, which is why it is used
  throughout this module.

## 8. Python demonstration

[`code/elastodynamics_demo.py`](./code/elastodynamics_demo.py) verifies every
claim above numerically. Observed output:

```text
granite-like model: rho = 2700 kg/m^3, lambda = 25 GPa, mu = 30 GPa
  v_p = sqrt((lambda + 2 mu)/rho) = sqrt((25 + 2*30)e9/2700) = 5610.8361 m/s
  v_s = sqrt(mu/rho)             = sqrt(30e9/2700)          = 3333.3333 m/s
  v_p/v_s = 1.683251
Poisson solid (lambda = mu = 30 GPa): v_p = 5773.5027 m/s, v_s = 3333.3333 m/s, v_p/v_s = 1.732050808 (sqrt(3) = 1.732050808)
water (K = 2.2 GPa, mu = 0, rho = 1000 kg/m^3): v_p = 1483.2397 m/s, v_s = 0 by inspection
```

```text
predicted eigenvalues of Gamma: v_p^2 = 3.148148e+07, v_s^2 = 1.111111e+07 m^2/s^2
               direction n                  sqrt(eigenvalues) (m/s)   max error
                   (1,0,0)          5610.8361, 3333.3333, 3333.3333   0.000e+00
                   (1,1,0)          5610.8361, 3333.3333, 3333.3333   9.095e-13
                   (1,1,1)          5610.8361, 3333.3333, 3333.3333   9.095e-13
```

```text
residual of rho u_i,tt = C_ijkl u_k,lj for u_i = A_i cos(k.x - omega t)
            wave                   vector   max |residual|/rho    relative
       P along x (+1.0000, +0.0000, +0.0000)         0.000000e+00   0.000e+00
   S (y) along x (+0.0000, +1.0000, +0.0000)         2.910383e-11   1.659e-16
 P along (1,1,1) (+0.5774, +0.5774, +0.5774)         5.820766e-11   2.028e-16
 S along (1,1,1) (+0.7071, -0.7071, +0.0000)         2.910383e-11   2.346e-16
```

```text
      P (u = (cos kx, 0, 0)): div =    -0.030257, |curl| =     0.000000
      S (u = (0, cos kx, 0)): div =     0.000000, |curl| =     0.030257
                 mixed field: div =    -0.030257, |curl| =     0.021913
analytic: div of the P field = -k sin(kx) = -0.030257; expected for the S field is 0
```

```text
domain 0 to 3000 m, dx = 1.0 m, source at 300 m, receivers at 900 and 2100 m
  wave   c formula (m/s)   arrival 1 (s)   arrival 2 (s)   c measured (m/s)  rel. error
     P         5610.8361        0.106808        0.320779          5608.2328   4.640e-04
     S         3333.3333        0.179784        0.539951          3331.7867   4.640e-04
```

```text
water: lambda = K = 2.2 GPa, mu = 0, rho = 1000 kg/m^3
  v_p = sqrt((K + 2*0)/rho) = 1483.2397 m/s
  v_s = sqrt(0/rho) = 0 m/s: no restoring force against shear
  a shear pulse with c = 0 advected for 500 steps: the displacement
  field differs from its initial state by 1.389e-11 m, i.e. it never
  leaves the source region
```

### What to observe

| Observation | Consequence |
|---|---|
| The Christoffel eigenvalues are $v_p^2$ once and $v_s^2$ twice for every direction, with errors $\le10^{-12}$ | The formulas are the eigenvalues of the elastic wave operator; the two-fold degeneracy of $v_s$ is the isotropy statement |
| The plane-wave residual of the full fourth-rank elastodynamic equation is $10^{-16}$ relative | The plane-wave solutions satisfy the equation the derivation produced; this is the numerical check of §3 Step 7 |
| The P field has divergence $-0.030257$ and zero curl; the S field the reverse | The Helmholtz separation is physical: $\nabla\cdot\mathbf u$ isolates P and $\nabla\times\mathbf u$ isolates S |
| A finite-difference simulation, which knows only the scalar wave equation with a given $c$, reproduces $v_p$ and $v_s$ to 4.6 parts in $10^4$ | The speeds measured from a propagating pulse agree with the derived formulas; the residual is the grid dispersion and the peak picker |
| With $\mu = 0$ the shear pulse is frozen, differing from its initial state by $1.4\times10^{-11}$ m | $v_s = 0$ is not a small speed: there is no shear wave at all, which is the S-wave shadow of the outer core |
| Water gives $v_p = 1483.2397$ m s⁻¹ and $v_s = 0$ | The same formula covers fluids and solids; the difference is entirely in $\mu$ |

> **Breaking exercise.** Set $\mu = 1$ MPa (nearly fluid) and predict, before
> running, the S speed and whether the numerical scheme's peak picker can still
> measure it with $\Delta x = 1$ m. Then increase $\mu$ by factors of ten until the
> measurement succeeds, and explain the resolution condition you have found.

## 9. Common mistakes

1. **Using $v_p = \sqrt{E/\rho}$ or $\sqrt{K/\rho}$ in a solid.** The first is the
   bar speed (uniaxial *stress*), the second is the fluid speed ($\mu = 0$); the
   solid P wave uses $M = \lambda+2\mu$.
2. **Dropping the $\rho$ in the equation of motion.** Equation (9) is an equation
   for acceleration; the density must appear on the left.
3. **Assuming the S speed depends on $K$.** It depends only on $\mu$ and $\rho$,
   which is why $v_s$ is the preferred porosity and fluid indicator in many
   rock-physics workflows.
4. **Forgetting the polarisation condition.** Forgetting $\nabla\cdot\mathbf u = 0$
   for the S wave makes the first term of equation (9) non-zero and gives a wrong
   speed.
5. **Treating the two S polarisations as always degenerate.** They are degenerate
   only in an isotropic medium; in an anisotropic one they split (lesson 02-04-06).
6. **Assuming that a fluid with a small but non-zero shear modulus has $v_s = 0$.**
   A measured $v_s$ in a "liquid" means either a mistake or a solid-like
   microstructure (a partially molten rock, an emulsion); the formula is exact, so
   the inference is about the medium.
7. **Believing that partial saturation must raise $v_p$.** The Gassmann dip of
   §4.4 shows it need not; only the $v_s$ behaviour is unconditional.
8. **Using $v_p$ and $v_s$ to infer all six elastic constants.** They determine
   $M$ and $\mu$; $K$ follows only under the isotropy assumption, and $\lambda$ is
   a poorly constrained difference.

## 10. Real-world applications

- **Earthquake location and tomography.** Every travel-time inversion is a
  statement about $v_p$ and $v_s$ structure, and the two are inverted jointly
  precisely because they constrain different moduli
  ([06-seismology](../../06-seismology/README.md)).
- **Lithology and fluid discrimination.** $v_p/v_s$ separates sand from shale,
  gas from brine, and (with rock-physics templates) quantifies porosity
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Discovery of the outer core.** The S-wave shadow, interpreted through
  $v_s = \sqrt{\mu/\rho}$, established the liquid outer core; the same formula
  underpins every modern Earth model
  ([12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)).
- **Mantle anisotropy.** The splitting of the S wave into two polarisations with
  different speeds is the standard probe of olivine lattice-preferred orientation
  and of mantle flow (lesson 02-04-06).
- **Seismic monitoring of reservoirs and volcanoes.** Time-lapse changes in $v_p$
  and $v_s$ separate saturation changes (mostly $v_p$) from pressure or
  crack-density changes (which affect $\mu$ and hence $v_s$).
- **Rock-mechanics and wellbore acoustics.** Sonic logs measure $v_p$ and $v_s$
  and convert them to dynamic elastic moduli, which are then corrected to static
  values for engineering design.
- **Numerical modelling.** Every elastic finite-difference or finite-element
  solver implements equation (9), and its stability and accuracy conditions are
  the scalar ones of lesson 02-03-05 applied to the faster of the two speeds.

## 11. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Chapter 2 derives the elastodynamic equation and the
  two speeds; this lesson is a guided version of that derivation with the
  numerical checks added. Level: advanced.
- **Lay, T., & Wallace, T. C. *Modern Global Seismology* (Academic Press, 1995).**
  The P, S and surface waves and their observational consequences, including the
  S-wave shadow. Level: intermediate.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** The clearest undergraduate route from
  the wave equation to the observed two-wave structure of the Earth. Level:
  intermediate.
- **Landau, L. D., & Lifshitz, E. M. *Theory of Elasticity* (Pergamon).** The
  classical derivation, including the thermodynamic refinements and the
  anisotropic generalisation. Level: graduate.
- **Fung, Y. C. *A First Course in Continuum Mechanics* (Prentice-Hall).** The
  careful version of the Helmholtz decomposition and the separation argument.
  Level: advanced.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** Travel times, ray theory and the observational use of $v_p$ and
  $v_s$. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md) —
  the material assumption used in Step 1.
- [04 Young's Modulus, Poisson's Ratio and the Elastic Constants](./04-elastic-moduli.md)
  — the modulus algebra behind equation (22).
- [06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](./06-anisotropic-elasticity.md)
  — the same problem with the Christoffel matrix in its general form.
- [07 Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md) —
  complex moduli, and why the speeds become frequency-dependent.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the scalar version, including the bar-speed warning.
- [01-06-07 Vector Identities and Their Role in Geophysics](../../01-mathematics/06-multivariable-calculus/07-vector-identities.md)
  — the identities used in Steps 4 and 6.
- [06-seismology](../../06-seismology/README.md) — the discipline built on these
  two formulas.

Exercises:
[`exercises/05-elastodynamics-exercises.md`](./exercises/05-elastodynamics-exercises.md)
and
[`exercises/05-elastodynamics-solutions.md`](./exercises/05-elastodynamics-solutions.md).

## Self-assessment checklist

Work through this without notes. This is the physics folder's mastery checkpoint;
every item should be a clear "yes".

- [ ] I can write the three ingredients (equation of motion, strain–displacement,
      constitutive law) and say what each assumes. (Section 2)
- [ ] I can derive the Navier–Cauchy equation, showing the expansion of both terms
      of the constitutive law. (Section 3, Steps 1–5)
- [ ] I can define the Helmholtz decomposition and state the gauge condition.
      (Section 3, Step 6)
- [ ] I can show that the gradient part is curl-free and obeys a wave equation
      with $v_p^2 = (\lambda+2\mu)/\rho$, and that the curl part is
      divergence-free with $v_s^2 = \mu/\rho$. (Section 3, Step 6)
- [ ] I can verify both speeds by direct plane-wave substitution into the full
      elastodynamic equation. (Section 3, Step 7)
- [ ] I can explain why the P polarisation is longitudinal and the S polarisations
      transverse, and why there are two S polarisations and one P. (Section 4.3)
- [ ] I can prove $v_p > v_s$ for any stable isotropic elastic solid, with the
      exact bound. (Section 4.1)
- [ ] I can explain why the outer core transmits no S waves, from $\mu = 0$, and
      what the S-wave shadow therefore proves. (Section 4.2)
- [ ] I can state what happens to $v_p$ and $v_s$ under partial fluid saturation,
      distinguishing the robust statement from the model-dependent one.
      (Section 4.4)
- [ ] I can list five assumptions of the derivation and name an observation that
      would falsify each. (Section 6)
- [ ] I can verify the speeds numerically by three independent routes (Christoffel
      eigenvalues, plane-wave residual, finite-difference propagation).
      (Section 8)
