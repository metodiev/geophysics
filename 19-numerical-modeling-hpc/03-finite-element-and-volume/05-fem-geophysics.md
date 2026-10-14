---
id: 19-03-05
title: "FEM in Geophysics: EM, Geodynamics and Seismology"
level: research
prereqs: ["19-03-01", "19-03-03", "08-04-02"]
tags: [numerical-modelling, fem, magnetotellurics, geodynamics, seismology, site-response, numerical-modelling]
---

# FEM in Geophysics: EM, Geodynamics and Seismology

**All models and data in this module are SYNTHETIC.** The conductivities,
viscosities and seismic velocities below are chosen teaching models; the
reference values are exact closed forms, and every number is printed by
[`code/fem_geophysics_demo.py`](./code/fem_geophysics_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the finite-element weak form of the magnetotelluric equation, with
   the correct sign of the radiation (admittance) boundary condition, and
   **verify** the sign by measurement.
2. **Compute** a layered-Earth impedance by the exact recursion and **compare**
   it with a finite-element impedance, stating where the residual comes from.
3. **Distinguish** an essential condition from a natural condition on a
   semi-infinite domain, and **explain** why a radiation condition is natural and
   not optional.
4. **Solve** a steady Stokes problem with a depth-dependent viscosity by finite
   elements and **verify** it against a manufactured solution and a stress
   balance.
5. **Measure** the asymmetry a variable viscosity produces in a channel flow, and
   **state** which quantity in the weak form carries the viscosity gradient.
6. **Compute** the SH transfer function of a layer over a half-space, **locate**
   its quarter-wavelength resonance by measurement, and **compare** the
   amplification with the impedance-contrast bound.
7. **State** what makes a geophysical finite-element model verifiable and what
   only makes it plausible.

## Prerequisites

- [19-03-01 Weak Formulation and the Galerkin Method](01-fem-weak-form.md) —
  essential versus natural conditions, the subject of Section 1.
- [19-03-03 Assembly, Sparsity and Linear System Structure](03-fem-assembly.md) —
  the assembly and solve used here.
- [08-04-02 Magnetotellurics](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the MT method, its impedance and its apparent resistivity. This lesson uses
  those definitions and does not re-derive them.
- [13-05-01 Finite-Element Geodynamics](../../13-geodynamics-tectonics/05-geodynamic-modelling/01-finite-element-geodynamics.md) —
  the geodynamical setting of Section 3.

## 1. Magnetotellurics: a complex Helmholtz problem with a radiation condition

In a one-dimensional Earth, with $E_x(z)$ the horizontal electric field and the
time dependence $e^{\mathrm{i}\omega t}$, Maxwell's equations reduce to

$$-\frac{\mathrm{d}}{\mathrm{d}z}\left(\frac{1}{\mathrm{i}\omega\mu_0}
\frac{\mathrm{d}E}{\mathrm{d}z}\right) + \sigma(z)E = 0, \tag{1.1}$$

with $p = 1/(\mathrm{i}\omega\mu_0)$ and $q = \sigma$. Because $p$ is constant
outside conductivity jumps, (1.1) is $E'' = \mathrm{i}\omega\mu_0\sigma E$, i.e.
$E'' = k^2E$ with

$$k = \sqrt{\mathrm{i}\omega\mu_0\sigma}, \qquad
\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}} \quad\text{(skin depth)}, \qquad
Z = \sqrt{\frac{\mathrm{i}\omega\mu_0}{\sigma}} \quad\text{(half-space
impedance)}. \tag{1.2}$$

Three exact consequences of (1.2) are checkable and the demonstration checks
them: a uniform half-space has phase $45^\circ$ and apparent resistivity
$1/\sigma$; and the field decays by $e^{-1}$ over one skin depth. Measured, with
$\sigma = 0.01$ S/m and $f = 1$ Hz: $\delta = 5032.921$ m,
$|Z| = 2.809926\times10^{-2}$ Ω, phase $= 45.000000^\circ$, apparent resistivity
$= 100.000000$ Ω·m against $1/\sigma = 100.000000$ Ω·m, and
$|E(\delta)|/|E(0)| = 0.3678794412 = e^{-1}$.

### 1.1 The weak form, and why the boundary condition's sign matters

Multiply (1.1) by a test function vanishing at the surface and integrate by
parts on $(0,L)$:

$$\int_0^L p\,\frac{\mathrm{d}E}{\mathrm{d}z}\frac{\mathrm{d}v}{\mathrm{d}z}\,\mathrm{d}z
+ \int_0^L \sigma E v\,\mathrm{d}z - \Big[p\,\frac{\mathrm{d}E}{\mathrm{d}z}v\Big]_0^L = 0.
\tag{1.3}$$

The surface value is essential: $E(0) = 1$ (a normalisation). The bottom value is
unknown, and it is replaced by the **radiation condition** — the statement that
below $L$ the field is a downgoing diffusive wave:

$$E(z) = E_0 e^{-kz} \Longrightarrow \frac{E'(L)}{E(L)} = -k
\Longrightarrow pE'(L) = -\sqrt{\frac{\sigma}{\mathrm{i}\omega\mu_0}}\,E(L). \tag{1.4}$$

The sign of the admittedance in (1.4) is negative, and it is not a convention: it
is fixed by the *decaying* branch. Getting it wrong does not give a slightly
wrong answer; the demonstration records the failure mode. With the positive sign
the relative $\mathrm{L}^2$ error against $\exp(-kz)$ was $2.203\times10^{2}$ at
50 elements and barely improved under refinement
($5.476\times10^{1}$ at 800 elements, fitted order 0.502) — the boundary was
launching an exponentially growing wave. With the correct sign:

| $n_{\rm elem}$ | $h/\delta$ | relative $\mathrm{L}^2$ error | order |
|---|---|---|---|
| 50 | 0.0800 | $1.038\times10^{-3}$ | — |
| 100 | 0.0400 | $2.597\times10^{-4}$ | 1.999 |
| 200 | 0.0200 | $6.492\times10^{-5}$ | 2.000 |
| 400 | 0.0100 | $1.623\times10^{-5}$ | 2.000 |
| 800 | 0.0050 | $4.058\times10^{-6}$ | 2.000 |

Fitted order $2.000$: the second-order rate of P1 elements on a smooth field, and
the *only* one of the two runs above that deserves to be called a convergence
study. Lesson [07](../07-verification-validation-uncertainty/README.md) makes the
general point: an order-of-accuracy test can be passed by a wrong boundary
condition only if the mesh is coarse enough, which is why the honest failure
above is instructive.

### 1.2 A layered Earth, measured against the exact recursion

For a stack of layers the impedance is built from the bottom up:

$$Z_N = \sqrt{\frac{\mathrm{i}\omega\mu_0}{\sigma_N}}, \qquad
Z_j = \zeta_j\frac{Z_{j+1} + \zeta_j\tanh(k_jh_j)}
{\zeta_j + Z_{j+1}\tanh(k_jh_j)}, \qquad
\zeta_j = \frac{\mathrm{i}\omega\mu_0}{k_j}. \tag{1.5}$$

With $\sigma_1 = 0.01$ S/m over 2 km and $\sigma_2 = 0.001$ S/m as a half-space,
the demonstration compares the exact recursion with a 600-element P1 solution
whose surface impedance is recovered from $E(0)$ and a one-sided difference for
$E'(0)$:

| $f$ (Hz) | exact $\rho_a$ (Ω·m) | FE $\rho_a$ (Ω·m) | relative error | exact phase (°) | FE phase (°) |
|---|---|---|---|---|---|
| 0.10 | 511.354 | 512.232 | $+1.72\times10^{-3}$ | 31.4949 | 31.5250 |
| 0.50 | 270.914 | 271.713 | $+2.95\times10^{-3}$ | 25.9164 | 25.9573 |
| 1.00 | 190.514 | 191.182 | $+3.51\times10^{-3}$ | 25.4830 | 25.5307 |
| 5.00 | 93.101 | 93.564 | $+4.97\times10^{-3}$ | 35.1670 | 35.2668 |

The residual is 2–5 parts in $10^3$ in resistivity and about $0.1^\circ$ in
phase, and it is attributable to the derivative recovery rather than to the
element formulation — Section 1.1 shows the same elements reaching full second
order when no derivative recovery is needed. That distinction matters when you
are debugging a code: the formulation and the post-processing are separate
sources of error, and only a test that isolates one of them can tell you which
you have.

The measured physics is the standard layered-Earth signature: at 5 Hz the
apparent resistivity is 93 Ω·m, close to the 100 Ω·m of layer 1, and it rises to
511 Ω·m at 0.1 Hz as the diffusive skin depth passes the layer and senses the
1000 Ω·m basement. **Rising $\rho_a$ with period is a conductive layer over a
resistive half-space.** The finite-element model reproduces both the number and
the trend.

## 2. Geodynamics: a steady Stokes problem by finite elements

A one-dimensional vertical channel with a depth-dependent viscosity $\nu(y)$ is
the simplest problem that contains what makes geodynamical solvers interesting:

$$-\frac{\mathrm{d}}{\mathrm{d}y}\left(\nu(y)\frac{\mathrm{d}u}{\mathrm{d}y}\right)
= f, \qquad u(0) = u(1) = 0, \tag{2.1}$$

where $u$ is the horizontal velocity, $\nu$ the viscosity (Pa s) and $f$ the
imposed body force per unit volume (Pa/m). Choose $\nu = 1 + 0.5y$ and
manufacture $u = y(1-y)$; then $\nu' = 0.5$, $u'' = -2$ and

$$-(\nu u')' = -\left[\nu'u' + \nu u''\right]
= -\left[0.5(1-2y) - 2(1+0.5y)\right] = 1.5 + 2y,
\tag{2.2}$$

so $f = 1.5+2y$ Pa/m. Measured convergence:

| $n_{\rm elem}$ | $h$ | max nodal error | $\mathrm{L}^2$ error | order |
|---|---|---|---|---|
| 8 | 0.12500 | $2.7756\times10^{-16}$ | $2.8527\times10^{-3}$ | — |
| 16 | 0.06250 | $8.3267\times10^{-17}$ | $7.1318\times10^{-4}$ | 2.000 |
| 32 | 0.03125 | $4.9960\times10^{-16}$ | $1.7830\times10^{-4}$ | 2.000 |
| 64 | 0.01562 | $4.3576\times10^{-15}$ | $4.4574\times10^{-5}$ | 2.000 |
| 128 | 0.00781 | $1.9346\times10^{-14}$ | $1.1143\times10^{-5}$ | 2.000 |
| 256 | 0.00391 | $1.0808\times10^{-13}$ | $2.7859\times10^{-6}$ | 2.000 |

Fitted $\mathrm{L}^2$ order $2.000$ and nodal errors at round-off. As in lesson
[01](01-fem-weak-form.md), the one-dimensional P1 solution is nodally exact when
the load is integrated exactly — the nodal column grows from $2.8\times10^{-16}$
to $1.1\times10^{-13}$ with mesh size, which is the round-off of the solve and
not a discretisation error.

### 2.1 A viscous flow problem is a balance statement, and that is checkable

The stress is $\tau = \nu u'$. From the manufactured solution,
$\tau(y) = (1+0.5y)(1-2y)$, so $\tau(0) = 1$ Pa and $\tau(1) = -1.5$ Pa. The
momentum balance integrated across the channel reads

$$\tau(1) - \tau(0) = -\int_0^1 f\,\mathrm{d}y . \tag{2.3}$$

Measured on the exact solution: $\tau(1)-\tau(0) = -2.500000$ Pa and
$\int_0^1(-f)\,\mathrm{d}y = -2.500000$ Pa. Any solver that reproduces the
velocity field but violates (2.3) has not solved a flow problem; it has
interpolated a field. This is the FEM analogue of the finite-volume conservation
identity of lesson [04](04-finite-volume.md), Section 1, and it is the check to
run first on a new Stokes code.

### 2.2 Where the asymmetry comes from

With constant forcing $f = 1$ Pa/m and a strongly depth-dependent viscosity
$\nu = 1+9y$ (bottom ten times stiffer than the top), there is no elementary
closed form, so the demonstration uses the same solver on 8192 elements as the
reference and compares at 256:

- peak velocity $0.029871$ m at $y = 0.3232$, not at the isoviscous $y = 0.5$;
- the 256-element solution differs from the 8192-element reference by
  $1.128\times10^{-6}$ m;
- the discrete momentum balance reproduces the imposed body force of
  $1.000000$ Pa.

The mechanism is in the weak form itself: $\int\nu u'v'\,\mathrm{d}y$ integrates
the *product* of the viscosity and the velocity gradient inside each element.
Where $\nu$ varies, the solution arranges its gradient so that the product — the
stress — stays continuous, which pushes the maximum towards the low-viscosity
side. A finite-element code does this without any special treatment; a
finite-difference code that averages $\nu$ to the faces has to be told, exactly
as in lesson [01](01-fem-weak-form.md), Section 6, and lesson
[04](04-finite-volume.md), Section 4.

## 3. Seismology: the SH transfer function of a layer over a half-space

Vertical SH incidence on a layer of density $\rho_1$, shear speed $\beta_1$ and
thickness $H$ over a half-space $(\rho_2,\beta_2)$ gives, for the layer field
$u(z)$,

$$u'' + k_1^2u = 0, \quad k_1 = \omega/\beta_1, \qquad
u(0) = 1, \qquad
\mu_1u'(H) = -\mathrm{i}\omega\rho_2\beta_2\,u(H), \tag{3.1}$$

the last being the radiation condition into the half-space. Writing
$u = \cos k_1z + A\sin k_1z$ and imposing (3.1) at $z = H$ gives

$$A = \frac{\gamma\sin k_1H - \mathrm{i}\cos k_1H}
{\gamma\cos k_1H + \mathrm{i}\sin k_1H}, \qquad
\gamma = \frac{\rho_1\beta_1}{\rho_2\beta_2}, \tag{3.2}$$

so the **transfer function** $T = u(0)/u(H) = 1/u(H)$ is fully determined. With
$\rho_1 = 2000$ kg m⁻³, $\beta_1 = 500$ m s⁻¹, $H = 100$ m,
$\rho_2 = 2500$ kg m⁻³, $\beta_2 = 1500$ m s⁻¹, the impedance ratio is
$\gamma = 0.266667$ and the quarter-wavelength frequency is
$\beta_1/(4H) = 1.2500$ Hz.

The demonstration solves (3.1) with 200 P1 elements and compares $|T|$ with the
closed form:

| $f$ (Hz) | $|T|$ exact | $|T|$ FE | relative error |
|---|---|---|---|
| 0.6250 | 2.744312 | 2.744313 | $+1.62\times10^{-7}$ |
| 1.2500 | 3.750000 | 3.750010 | $+2.57\times10^{-6}$ |
| 2.5000 | 1.000000 | 1.000000 | $+6.81\times10^{-9}$ |
| 3.7500 | 3.750000 | 3.750087 | $+2.31\times10^{-5}$ |

### 3.1 Locating the resonance by measurement

Scanning 2000 frequencies from 0.25 to 5.5 Hz and finding the local maxima of
$|T|$:

| order | measured peak (Hz) | predicted $(2n-1)\beta_1/(4H)$ (Hz) | difference (Hz) |
|---|---|---|---|
| 1 | 1.2506 | 1.2500 | $+0.0006$ |
| 2 | 3.7509 | 3.7500 | $+0.0009$ |

Both lie within one scan grid step (0.0026 Hz) of the prediction, and the
largest $|T|$ on the scan is $3.750346$ against the impedance-contrast value
$1/\gamma = 3.750000$. The number that matters physically is the amplification at
resonance: a soft layer with a factor-$\gamma$ impedance contrast amplifies
ground motion by $1/\gamma$ at odd multiples of the quarter-wavelength
frequency, and both the position and the size of that amplification are
reproduced by the finite-element model to four or five digits.

## 4. A fully worked MT impedance from the finite-element field

Using the two-layer model of Section 1.2 at $f = 1$ Hz, the interface at
$z = 2000$ m, and a 600-element mesh on $(0,6000)$ m:

1. **Field.** The solve returns $E(0) = 1.000000$ (imposed) and, from the first
   element, $E'(0)$ by one-sided difference.
2. **Impedance in the standard convention.** $H_y = -\frac{1}{\mathrm{i}\omega\mu_0}
   E'$, so $Z = E/H = -\mathrm{i}\omega\mu_0E(0)/E'(0)$. The minus sign is part of
   the convention, and it is what makes a uniform half-space come out with
   $+45^\circ$ phase (Section 1); with the other sign every phase is shifted by
   $180^\circ$, which is how the sign error in (1.4) shows itself in a
   resistivity-and-phase plot.
3. **Apparent resistivity.** $\rho_a = |Z|^2/(\omega\mu_0) = 191.182$ Ω·m against
   the exact recursion's $190.514$ Ω·m: a relative difference of
   $+3.51\times10^{-3}$.
4. **Why the two agree but not exactly.** The linear element's derivative is
   piecewise constant, so the one-sided difference $\big(E_1-E_0\big)/h$
   approximates $E'(0)$ to first order, while the field itself is second order
   accurate. The impedance inherits the weaker of the two rates. A quadratic
   element, or a weak-flux recovery, would remove precisely this residual and
   nothing else — which is how the diagnosis was confirmed.

## 5. Assumptions and regime of validity

1. **One-dimensional Earth models.** All three problems are depth-dependent
   only. In 2-D and 3-D the MT problem becomes a coupled vector Helmholtz
   problem with a much richer set of boundary conditions, and the SH problem
   acquires converted phases; none of the numbers here transfer.
2. **Semi-infinite domains truncated at finite depth.** The radiation condition
   (1.4)/(3.1) is exact whenever the datum is placed *inside* the uniform medium
   whose impedance it encodes, and then it is exact at any depth: the truncation
   depth is not a discretisation parameter, only the mesh spacing is. If the
   truncation instead cuts a layer, the datum is the wrong impedance and the
   error appears as a biased apparent resistivity — a modelling error that no
   refinement removes. The demonstration places the datum in the half-space for
   MT ($L = 4\delta$ for the uniform half-space, $L = 6$ km for the two-layer model,
   whose interface at 2 km is inside the domain) and at the interface for the SH problem.
3. **Diffusive (MT) versus propagating (SH) physics.** Both are complex
   Helmholtz problems and both are discretised identically, but MT decays
   exponentially over $\delta$ (measured $e^{-1}$ per skin depth) while SH
   oscillates over a wavelength. Mesh requirements follow the physics, not the
   discretisation.
4. **Linear, isotropic, non-dispersive constitutive laws.** Conductivity,
   viscosity and shear modulus are real scalars. Frequency-dependent
   conductivity, anisotropic viscosity and attenuation each change the weak form.
5. **Manufactured or exact references only.** Every comparison above is against
   an exact closed form or a manufactured solution. No agreement with another
   numerical code is offered as evidence, because two codes can share a mistake;
   lesson [07](../07-verification-validation-uncertainty/04-benchmark-problems.md)
   treats community benchmarks as a separate and weaker form of evidence.
6. **Explicit statement of the sign conventions.** The $\mathrm{i}\omega t$
   convention, the definition of $H$ from $E'$ and the direction of decay fix
   every sign above. A reader changing one convention must change the others, and
   the measurements in Section 1.1 show what happens otherwise.

## 6. Mastery checkpoint

Complete this without notes.

> An MT survey models a 1 km layer of 10 Ω·m over a 1000 Ω·m half-space at
> $f = 1$ Hz; a separate site-response study models a 100 m layer of
> $\beta = 500$ m s⁻¹ over a half-space with $\beta = 1500$ m s⁻¹.
>
> **(a)** Compute the MT skin depth in the layer and state whether the layer is
> thin or thick relative to it.
> **(b)** State the radiation condition for the MT problem, with its sign, and
> explain in one sentence what physical branch fixes the sign.
> **(c)** Write the weak form of the MT equation and say which boundary condition
> is essential.
> **(d)** For the site-response model, compute the quarter-wavelength frequency
> and the expected amplification for an impedance contrast of 3.75.
> **(e)** A colleague's SH solver reproduces the resonance frequency but gives an
> amplitude 20% too large. Name the most likely single cause and the measurement
> that would confirm it.

A worked version appears with the
[exercises](exercises/05-fem-geophysics-exercises.md).

## 7. Common pitfalls

1. **Choosing the radiation condition's sign by taste.** Measured: relative error
   $2.2\times10^{2}$ at 50 elements and a fitted order of 0.502 against 2.000
   with the correct sign.
2. **Reading a post-processing error as a formulation error.** The layered-MT
   residual of $2$–$5\times10^{-3}$ comes from the one-sided derivative, not from
   the elements; the uniform-half-space test isolates it.
3. **Truncating a semi-infinite domain without a radiation datum.** Without an
   impedance boundary the reflected energy returns and corrupts the solution; the
   truncation depth must be chosen against the skin depth or the wavelength.
4. **Checking only the velocity/viscosity field in a flow problem.** The balance
   (2.3) is the property that makes the solution a flow; it is cheap to check and
   is not implied by a small $\mathrm{L}^2$ error.
5. **Reporting a manufactured-solution agreement as validation.** It is
   verification: it shows the code solves the equations you wrote, not that the
   equations describe the Earth.
6. **Assuming one benchmark transfers.** The MT and SH problems share their
   discretisation and share nothing else; a mesh that is converged for one is
   silent about the other.
7. **Quoting an apparent resistivity without the period or frequency.** A
   layered-Earth $\rho_a$ is a function of frequency; a single number without it
   is not a measurement.

## 8. Related modules

- [19-03-04 Finite Volume Methods and Conservative Discretisation](04-finite-volume.md) —
  the flux-based alternative, standard for EM diffusion in 3-D.
- [19-08-03 Simulating EM Diffusion in Conductive Media](../08-geophysical-simulation-case-studies/03-simulate-em-diffusion.md) —
  a full case study in the same physics.
- [19-08-04 Simulating Mantle Convection](../08-geophysical-simulation-case-studies/04-simulate-mantle-convection.md) —
  the Stokes problem of Section 2 extended to two dimensions and to convection.
- [12-04-02 Numerical Geodynamo Models](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md) —
  where the dimensionless numbers of a geodynamical simulation are measured
  against their resolvability.
- [06-08-01 Receiver Functions: Deconvolution and Ps Conversions](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the structure that a transfer function of this kind is used to constrain.

## Materials

- Demonstration: [`code/fem_geophysics_demo.py`](./code/fem_geophysics_demo.py).
- Exercises: [`exercises/05-fem-geophysics-exercises.md`](./exercises/05-fem-geophysics-exercises.md)
  with worked [solutions](./exercises/05-fem-geophysics-solutions.md).
