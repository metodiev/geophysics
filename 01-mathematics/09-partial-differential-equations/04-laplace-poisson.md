---
id: 01-09-04
title: "Laplace and Poisson Equations in Earth Systems"
level: advanced
prereqs: ["01-09-01", "01-06-08"]
estimated_minutes: 90
tags: [partial-differential-equations, laplace-equation, poisson-equation, harmonic-functions, non-uniqueness]
---

# Laplace and Poisson Equations in Earth Systems

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** Poisson's equation $\nabla^2V = -4\pi G\rho$ from Gauss's law and
   Laplace's equation as its source-free case, stating the sign convention.
2. **State and use** the defining properties of harmonic functions — the mean
   value property, the maximum principle, smoothness, and analyticity — and say
   what each one implies for a potential-field dataset.
3. **Prove** uniqueness for the Dirichlet problem, uniqueness up to a constant
   for the Neumann problem, and uniqueness for the Robin problem, using Green's
   first identity.
4. **Distinguish rigorously** two statements that are constantly confused:
   uniqueness of the boundary-value problem, and non-uniqueness of
   potential-field inversion. State exactly which failure of completeness in
   real data produces the second from the first.
5. **Exhibit** two source distributions with identical exterior fields, compute
   the relative size of the effect, and say what additional measurement would
   break the tie.
6. **Explain** why downward continuation and source inversion are ill posed while
   the Dirichlet problem is well posed, and what role prior information plays.

## Prerequisites

- [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md)
  — the prerequisite treatment of the gravitational potential, harmonic
  functions and the first version of the non-uniqueness argument.
- [01-09-01 Classification of PDEs](./01-classification.md) — why this equation
  needs only boundary data, and what "no real characteristics" means for the
  data.
- [01-06-06 Gauss, Stokes and Green Theorems](../06-multivariable-calculus/06-integral-theorems.md)
  — Green's identities, which do the work in Section 4.
- [01-06-05 Line and Surface Integrals](../06-multivariable-calculus/05-line-surface-integrals.md)
  — flux and the solid-angle argument.

## 1. Intuition: the steady equation, and why it is the hardest of the three

Elliptic problems are the ones where nothing varies in time, so the field must
be consistent everywhere at once. That "at once" is what makes them both
mathematically rigid and practically ambiguous:

- **Rigid**, because a small change in the boundary data changes the interior
  everywhere, and because the maximum principle forbids interior extremes.
- **Ambiguous**, because rigidity of the *forward* map means a great many
  different source distributions are compatible with a surface measurement.

Both features come from the same place: the absence of characteristics. There is
no direction along which information travels, so there is no direction along
which it can be tracked, timed or localised.

The two equations of the title are

$$\nabla^2 V = 0 \quad\text{(Laplace)}, \qquad
\nabla^2 V = -4\pi G\rho \quad\text{(Poisson)},$$

differing only by the source term. Outside all mass, the potential of any
distribution is harmonic; inside, the source appears. **In potential-field
geophysics the whole problem is that the measurement is made where the equation
is homogeneous, and the answer is wanted where it is not.**

## 2. Derivation of Poisson's equation

### 2.1 From Gauss's law

Newton's law of gravitation for a point mass, combined with the solid-angle
argument for the flux of an inverse-square field through a closed surface, gives
**Gauss's law**:

$$\oint_{\partial\Omega}\mathbf{g}\cdot d\mathbf{A} =
-4\pi G\,M_{\text{enc}} = -4\pi G\int_\Omega\rho\,dV , \tag{1}$$

with the sign convention that $\mathbf{g}$ points toward the mass. Writing the
potential $V$ so that $\mathbf{g} = \nabla V$ (positive potential, the convention
of [01-06-08](../06-multivariable-calculus/08-potential-theory.md)) and applying
the divergence theorem to the left-hand side:

$$\int_\Omega \nabla\cdot\mathbf{g}\,dV = \int_\Omega \nabla^2V\,dV
= -4\pi G\int_\Omega\rho\,dV .$$

Because $\Omega$ is arbitrary and the integrands are continuous,

$$\boxed{\ \nabla^2 V = -4\pi G\rho\ } \tag{2}$$

This is **Poisson's equation**. Where $\rho = 0$ it reduces to **Laplace's
equation** $\nabla^2V = 0$. Three remarks:

- The sign of (2) is tied to the convention $V > 0$ and $\mathbf{g} = \nabla V$.
  With $\Phi = -V$ and $\mathbf{g} = -\nabla\Phi$ the equation reads
  $\nabla^2\Phi = +4\pi G\rho$. Neither is wrong; mixing them is, and every sign
  error in a potential-field paper traces back to this choice.
- The derivation used a *point-mass* law plus a geometric argument, so it
  inherited an assumption: that the source is a classical mass distribution. It
  is the same equation that governs the magnetic potential outside a
  magnetised body, the electric potential in a DC survey and the hydraulic head
  in steady flow, with a different physical interpretation of the source.
- Equation (2) is **linear, second-order and elliptic**, with no preferred
  direction. Section 4 shows that this alone forces the solution to be
  determined by boundary data.

### 2.2 Green's functions in three and two dimensions

The fundamental solution of the Laplacian in three dimensions is
$-1/(4\pi r)$, so the potential of a general distribution is its convolution with
$G/r$:

$$V(\mathbf{r}) = G\int_\Omega\frac{\rho(\mathbf{r}')}
{\lvert\mathbf{r}-\mathbf{r}'\rvert}\,dV' ,$$

which is exactly Poisson's equation inverted using the free-space Green's
function. In two dimensions the Green's function is
$\frac{1}{2\pi}\ln(1/r)$ instead of $1/(4\pi r)$, so the potential of a
two-dimensional body is logarithmic. That difference is not a curiosity: a
logarithmic potential does not decay at infinity, which is why a "2-D" model
must always be interpreted with a finite strike length in mind, and why the
solution of a genuinely two-dimensional problem has no global monopole term.

## 3. Harmonic functions: the tool kit

A $C^2$ function $u$ is **harmonic** on an open set $\Omega$ if $\nabla^2u = 0$
there. Harmonic functions have four properties, and each has a direct
geophysical reading.

**1. Mean value property.** For any ball $B(\mathbf{c},R)\subset\Omega$,

$$u(\mathbf{c}) = \frac{1}{4\pi R^2}\oint_{\lvert\mathbf{r}-\mathbf{c}\rvert = R}
u\,dA .$$

The value at the centre is the average over any sphere around it. The
demonstration checks the discrete version to $8.73\times10^{-13}$: at the
converged state of a finite-difference Laplace solve, an interior node equals the
average of its four neighbours to the residual tolerance. **Reading:** a
potential-field map has no "locally anomalous" value that is not already implied
by its neighbourhood, so a spike in a map is either a source or an artefact.

**2. Maximum principle.** A non-constant harmonic function attains neither a
maximum nor a minimum in the interior; both extremes lie on the boundary. The
demonstration reports max interior $= 0.924180$ against max boundary
$= 0.961349$ for a Laplace solve on the unit square. **Reading:** an interior
extremum in a harmonic field is impossible — there must be a source (where
$\nabla^2V \ne 0$), a boundary, or noise. This is a remarkably strong and
cheaply applied consistency check.

**3. Smoothness.** Harmonic functions are $C^\infty$, and in fact real-analytic,
inside their domain. **Reading:** the field above a source is analytic, so its
values on a small patch determine the whole field above the patch by analytic
continuation. That is the theoretical basis of upward continuation, and of the
statement that measured fields carry the imprint of sources far outside the
survey area.

**4. Uniqueness and stability, with one very important exception.** Section 4
proves that a harmonic function is determined by its boundary values. Section 5
explains why this *positive* result coexists with the practitioner's experience
that potential-field inversion has no unique answer.

## 4. Uniqueness theorems, and exactly what they claim

### 4.1 Dirichlet problem

**Theorem.** Let $\Omega$ be a connected bounded region with piecewise smooth
boundary. Then there is at most one function $u$ harmonic in $\Omega$,
continuous on $\bar\Omega$, with prescribed boundary values $u = f$ on
$\partial\Omega$.

**Proof.** Let $u_1$ and $u_2$ be two solutions and set $w = u_1 - u_2$, so
$\nabla^2w = 0$ in $\Omega$ and $w = 0$ on $\partial\Omega$. Green's first
identity (from
[01-06-06](../06-multivariable-calculus/06-integral-theorems.md)) gives, for $w$
and $w$,

$$\int_\Omega w\nabla^2w\,dV + \int_\Omega \lvert\nabla w\rvert^2\,dV
= \oint_{\partial\Omega} w\,\frac{\partial w}{\partial n}\,dA .$$

The first term vanishes because $\nabla^2w = 0$, and the right-hand side vanishes
because $w = 0$ on the boundary. Hence

$$\int_\Omega\lvert\nabla w\rvert^2\,dV = 0
\quad\Longrightarrow\quad \nabla w = 0 \ \text{in }\Omega
\quad\Longrightarrow\quad w = \text{const} = 0 .$$

Uniqueness follows. $\square$

The demonstration confirms that this is not an artificial statement: solving the
same problem from two completely different initial guesses (zeros and ones on
every interior node) converges to fields that agree to $6.842\times10^{-11}$, the
residual tolerance. The iteration finds *the* solution; it does not select one.

### 4.2 Neumann problem

With the flux prescribed instead, $\partial u/\partial n = g$ on $\partial\Omega$,
the same argument gives $\nabla w = 0$, hence $w = \text{const}$: **unique up to
an additive constant.** Two consequences to carry forward:

- A gravity or magnetic dataset determines only *differences* of potential unless
  something else fixes the datum; the constant is physically meaningless, and
  reporting a potential without its datum is incomplete.
- A necessary consistency condition on the data is $\oint_{\partial\Omega} g\,dA
  = \int_\Omega \nabla^2u\,dV$. If the sources inside $\Omega$ have nonzero total
  mass, no purely Neumann problem with zero net flux can be posed: the data must
  be consistent with the enclosed sources.

### 4.3 Robin problem

If $\partial u/\partial n + h\,u = g$ with $h > 0$ (a radiating or conductive
boundary — the field is not simply fixed nor simply fluxed), then the boundary
term is $-\oint h\,w^2\,dA < 0$, which again forces $w = 0$, giving **full
uniqueness**. This combination appears when the field is damped by a conducting
layer or when a physically motivated impedance condition is imposed, and it is
the boundary condition used to truncate a numerical domain.

### 4.4 What the theorems do *not* say

Here is the sentence that matters most in this lesson:

> **Uniqueness of the Dirichlet problem says that complete boundary data
> determine the solution — and therefore, since $\rho = -\nabla^2V/(4\pi G)$,
> they also determine the source density inside the region.**

Read that carefully, because it is the opposite of the folklore. If $V$ were known
on the entire bounding surface of a region containing all the sources, then $V$
inside is unique, hence $\nabla^2V$ inside is unique, hence $\rho$ inside is
unique. The practitioner's non-uniqueness is therefore **not** a failure of the
uniqueness theorem. It is a failure of the four hypotheses that real data never
satisfy:

| Requirement for the theorem | What real data provide |
|---|---|
| Values on a closed surface surrounding all sources | values on a surface *patch* (the ground, a flight line, a satellite track) |
| Values at every point of that surface | finitely many samples, on a grid |
| Exact values | values with noise |
| All sources inside the surface | sources may lie outside the survey (deep, or beyond the edge) |

The next section turns that table into arithmetic.

## 5. Why potential-field inversion is non-unique anyway

### 5.1 The structural statement

Let $\mathcal{F}$ be the forward map from a density model $\rho$ to the exterior
data $d = \mathcal{F}\rho$. Non-uniqueness means $\ker\mathcal{F} \ne \{0\}$: some
change of model produces no change in the data at all. Two mechanisms produce such
a kernel, and the second is the one that matters in practice.

### 5.2 An exact kernel: spherical symmetry with zero total mass

By Newton's shell theorem, the exterior potential of *any* spherically symmetric
distribution is $\Phi = GM/r$ with $M$ the total mass, independent of the radial
profile. Therefore any spherically symmetric perturbation $\delta\rho$ with

$$\int\delta\rho\,dV = 0$$

changes the exterior potential by exactly **nothing**. It is an exact element of
the kernel of the forward map, whatever the data quality.

The demonstration constructs one explicitly and measures it. Inside a uniform ball
of radius $R = 30$ km and density $2800\ \mathrm{kg\,m^{-3}}$, add
$+500\ \mathrm{kg\,m^{-3}}$ on $12\ \mathrm{km}\le r < 21\ \mathrm{km}$ and a
compensating $-212.33\ \mathrm{kg\,m^{-3}}$ on $21\ \mathrm{km}\le r<30\ \mathrm{km}$:

```text
  analytic mass of the positive shell  = +1.577708e+16 kg
  analytic mass of the negative shell  = -1.577708e+16 kg
  analytic net mass of the perturbation = +0.000e+00 kg (exactly zero)

  Comparing at z0 = 2R = 6.000e+04 m:
    V(ball)                        = 3.5224634757e+02
    V(ball + positive shell)       = 3.6979575293e+02   relative change +4.982e-02
    V(ball + compensated pair)     = 3.5224630590e+02   relative change -1.183e-07
    cancellation factor            = 4.212e+05
```

The positive shell on its own would shift the exterior potential by 5 %; adding
the compensating shell removes it, leaving a residual $1.2\times10^{-7}$ that is
quadrature noise in the numerical integration (the exact value is zero). **A
500 kg m$^{-3}$ density change inside the Earth is invisible to a 1 ppm
measurement of the exterior potential.** This is not a limitation of instruments;
it is a property of the equation.

The same theorem is the reason a uniform ball and a point mass are
indistinguishable from outside, which the demonstration also confirms
(quadrature-limited agreement of $3.6\times10^{-6}$ relative — the identity is
exact, the residual is the accuracy of the numerical integration):

```text
  ball radius R = 3.000e+04 m, density = 2800.0 kg/m^3
  total mass (volume integral) = 3.166725e+17 kg

      z0 / R     V(ball), quadrature         G M / z0   relative difference
         1.5      4.696622569682e+02 4.6966056189e+02              3.61e-06
         2.0      3.522463475686e+02 3.5224542141e+02              2.63e-06
         4.0      1.761230578250e+02 1.7612271071e+02              1.97e-06
```

### 5.3 The kernel that actually bites: finite, band-limited, noisy data

Real data are not the exterior potential on a closed surface; they are a
band-limited field on a patch, with noise. So the effective kernel is enormously
larger than the exact one:

- **Truncation.** The field is measured on a patch, so the analytic continuation
  that would distinguish two models requires data that were never recorded. Two
  models can be made to agree on the patch and disagree elsewhere.
- **Band limitation.** The field above a body is analytic and its amplitude decays
  with altitude roughly as $\exp(-kz)$ in the wavenumber $k$. A perturbation whose
  signature is confined to wavenumbers above the noise level is invisible; the
  set of such perturbations is a *near*-null space of dimension comparable to the
  number of high wavenumbers.
- **Noise.** The demonstration's null vector is invisible at 1 ppm; at 1 % noise
  the invisible set is far larger, and it includes depth–density trade-offs of
  the kind that make "depth to source" ambiguous.
- **Sources outside the region.** The maximum principle and analyticity mean the
  field on a patch contains the influence of everything, including bodies beyond
  the survey boundary, and these are entirely unconstrained.

### 5.4 The correct statement, in one paragraph

Uniqueness of the elliptic boundary-value problem is the reason a
potential-field dataset is *informative*: complete, exact boundary data would
determine the source. The null space of the forward map — nontrivial even in
principle (Section 5.2) and enormous in practice (Section 5.3) — is the reason
the information is *insufficient*. Both statements are true at once, and
conflating them is the commonest conceptual error in the subject. It is also why
regularisation and prior information are not cheating: adding a model norm,
a depth weighting or a positivity constraint is the mathematically necessary
supplement that replaces the missing part of the data. The theory is developed in
[18-inverse-problems](../../18-inverse-problems/README.md).

## 6. Downward continuation: well posed forward, ill posed backward

Harmonicity gives another clean example of the same asymmetry. Suppose the field
is known on the plane $z = 0$ and wanted on a lower plane $z = -h$ (closer to the
sources). In wavenumber space, the field at height $z$ has amplitude
$A(k)\,\mathrm{e}^{-kz}$ for a source at depth, so continuing from $z=0$ down to
$z=-h$ multiplies the wavenumber-$k$ component by $\mathrm{e}^{+kh}$:

| $k$ (rad/m) | $h = 1$ km | Amplification $\mathrm{e}^{kh}$ |
|---|---|---|
| $10^{-3}$ (6.3 km wavelength) | 1 km | 2.7 |
| $10^{-2}$ (628 m) | 1 km | $2.2\times10^{4}$ |
| $10^{-1}$ (63 m) | 1 km | $2.7\times10^{43}$ |

So downward continuation is exactly a backward-diffusion problem in the depth
coordinate: the forward direction is stable and smoothing, the inverse is
explosive. The mathematics is the same as in
[01-09-02](./02-heat-equation.md) §5 and
[01-09-07](./07-boundary-value-problems.md), and it is the reason practical
downward continuation requires a low-pass filter whose cutoff is chosen from the
noise level — a regularisation in all but name.

## 7. Python demonstration

`code/laplace_poisson.py` solves the elliptic problems numerically and measures
each property asserted above.

**Convergence to an exact harmonic solution.** On the unit square with
$u(x,1) = \sin\pi x$ and $u = 0$ on the other three sides, the exact solution is
$u = \sinh(\pi y)\sin(\pi x)/\sinh\pi$. Successive over-relaxation with the
optimal factor gives

```text
      N        dx  iterations    max error   order
      9    0.1000          47    2.826e-03        
     19    0.0500          92    7.115e-04    1.99
     39    0.0250         181    1.782e-04    2.00
     79    0.0125         353    4.456e-05    2.00
```

Order 2, and the iteration count grows linearly with $N$ — the signature of an
elliptic problem whose solution is coupled in all directions at once. (Plain
Jacobi on the same problem needs about $3.7\,N^2$ iterations; over-relaxation
buys a factor of $N$.)

**The mean value property and the maximum principle.** At the converged
discrete state:

```text
  Mean value property at converged state: the largest deviation of an
  interior node from the average of its four neighbours is 8.73e-13
  (zero to the residual tolerance of 1e-11, as Laplace's equation requires).

  Maximum principle: max interior = 0.924180, max on the boundary = 0.961349
  Interior <= boundary: True.
```

**Uniqueness in practice.**

```text
  Starting from u = 0 every internal node:   137 iterations
  Starting from u = 1 every internal node:   140 iterations
  Max difference between the two converged fields: 6.842e-11
```

**Poisson's equation.** With $u = \sin\pi x\sin\pi y$ and
$f = 2\pi^2\sin\pi x\sin\pi y$, the observed convergence order is 2.01, 2.00,
2.00 on successively finer grids — the source term changes nothing about the
accuracy of the elliptic solve.

**The non-uniqueness experiments** are quoted in Section 5.2 above. One detail of
the numerical work is worth recording as a caution: the residual difference
$1.2\times10^{-7}$ between the compensated and uncompensated models is *not* the
size of a physical effect; the exact effect is zero. It is the quadrature error of
two numerical integrations. A demonstration that reported "$1.2\times10^{-7}$ of
remaining signal" without that caveat would be misusing its own numerics, and the
script prints both the analytic mass balance (exactly zero) and the numerical
integral so that the distinction is visible.

> **Breaking exercise.** The demonstration's null-space perturbation is
> spherically symmetric. Before running anything, predict whether a *non*-spherical
> perturbation with zero total mass also has zero exterior potential. Then test
> your prediction by computing the exterior potential of a zero-total-mass
> perturbation that is not spherical, and explain the result in terms of multipole
> moments. (Hint: the exterior field of a general body is a multipole expansion;
> which moment does the total mass control?)

## 8. Common mistakes

1. **Confusing the two uniqueness statements.** "The Dirichlet problem has a
   unique solution" and "potential-field inversion has no unique solution" are
   both true and are about different things. Section 4.4 and Section 5 are the
   resolution.
2. **Reporting a potential without its datum.** The Neumann problem determines
   $V$ only up to a constant. Fix and state a reference.
3. **Sign conventions.** $\nabla^2V = -4\pi G\rho$ with $V$ positive and
   $\mathbf{g} = \nabla V$; flip either convention and flip the sign in (2).
4. **Using the $1/r$ kernel in a two-dimensional model.** The 2-D Green's
   function is $\ln(1/r)/2\pi$, and its potential does not decay at infinity.
   Mixing the two kernels produces errors that look like "deep structure".
5. **Interpreting an interior extremum as a target.** The maximum principle
   forbids it for a harmonic field. Find the source, the boundary or the noise.
6. **Downward continuing without a filter.** The amplification is
   $\exp(kh)$ — astronomical for short wavelengths. The filter cutoff must be tied
   to the noise level, and that choice is the regularisation.
7. **Believing that more precise data removes the non-uniqueness.** Precision
   shrinks the effective null space; it cannot remove the exact one of Section
   5.2, and the trade-off between resolution and uniqueness is intrinsic.
8. **Treating steady state as given.** An elliptic model asserts that time
   derivatives vanish. Where the process is diffusive, that asserts
   $t \gg L^2/\kappa$; check it, as
   [01-09-02](./02-heat-equation.md) §4.1 does for the lithosphere.

## 9. Real-world applications

- **Gravity and magnetics.** Depth–density (or depth–magnetisation) trade-offs,
  equivalent layers, and the need for a regularised inversion with a model norm.
  All of it follows from Sections 5.2 and 5.3.
- **Geoid and satellite gravimetry.** The geoid is a harmonic function of position
  outside the masses; global models are spherical-harmonic expansions, that is,
  the multipole expansion of Section 5.3 truncated at a maximum degree, with the
  truncation setting the resolution.
- **DC resistivity and self-potential.** The potential is harmonic outside the
  current sources; the survey geometry determines which part of the boundary data
  is available, and therefore which parts of the model are constrained.
- **Steady groundwater flow.** $\nabla\cdot(K\nabla h) = 0$; with variable $K$ this
  is not Laplace's equation but the same elliptic structure applies, including the
  maximum principle for the head (which is why heads interpolate between
  boundaries and why a "local high" implies recharge).
- **Isostasy and flexure.** The governing equations are fourth-order elliptic
  problems; uniqueness and the maximum principle have analogues, though not the
  exact form proved here.
- **Geodesy and reference frames.** The harmonicity of the disturbing potential is
  the reason the geoid can be continued, and the reason the continuation is
  unstable — the practical reason that gravity data are always filtered before
  use.

## 10. Further reading

- **Kellogg, O. D. (1953). *Foundations of Potential Theory*. Springer.** Level:
  graduate. The classical rigorous treatment of harmonic functions, the mean value
  property and boundary-value theory.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Level: advanced undergraduate
  upward. The standard applied reference; the link from Sections 4 and 5 to actual
  survey practice is made explicitly throughout.
- **Axler, S., Bourdon, P., & Ramey, W. (2001). *Harmonic Function Theory* (2nd
  ed.). Springer.** Level: graduate. A clean, modern account of the mean value
  property, the maximum principle and the Dirichlet problem.
- **Gilbarg, D., & Trudinger, N. S. (2001). *Elliptic Partial Differential
  Equations of Second Order*. Springer.** Level: doctoral. The reference for
  existence, regularity and the general maximum principle for variable-coefficient
  elliptic operators.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Level: graduate. The non-uniqueness of potential-field inversion, the
  null space, and the role of prior information, developed from exactly the
  examples in Section 5.
- **Zhdanov, M. S. (2002). *Geophysical Inverse Theory and Regularization
  Problems*. Elsevier.** Level: graduate. Regularisation as the practical answer
  to the ill-posedness of Sections 5 and 6.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Solutions are in
[`exercises/04-laplace-poisson-solutions.md`](./exercises/04-laplace-poisson-solutions.md).

**★1.** A uniform sphere has radius 1.2 km and density
$3000\ \mathrm{kg\,m^{-3}}$. Compute its mass, its exterior potential at
$r = 5$ km, and the surface gravity. State the value of $\nabla^2V$ in each of
the three regions $r<a$, $r=a$, $r>a$.

**★2.** State the mean value property and verify it for $V = GM/r$ on the sphere
of radius $R$ centred at a point $\mathbf{c}$ with $\lvert\mathbf{c}\rvert > R$.

**★3.** For the Dirichlet problem on the unit square with
$u(x,1) = \sin\pi x$ and $u = 0$ elsewhere, compute the value at the centre. Using
the exact solution, decide whether it exceeds the interior maximum reported in the
demonstration, and explain.

**★4.** Derive the 2-D Green's function $\ln(1/r)/2\pi$ by solving
$\nabla^2u = \delta$ in polar coordinates, and state why the additive constant is
irrelevant.

**★★5.** Prove uniqueness for the Neumann problem and state the compatibility
condition that the boundary flux must satisfy when sources are present.

**★★6.** The maximum principle forbids interior extrema. A gravity map shows a
local maximum 3 km from the nearest boundary. Write the shortest possible argument
that something in the interpretation is wrong, then list the three explanations
that are consistent with the mathematics.

**★★7.** Two density models of a 30 km-radius ball produce exterior potentials
that differ by 1 part in $10^{7}$ at $r = 60$ km. Using the demonstration's
cancellation factor of $4.2\times10^{5}$, estimate the largest density
perturbation that such a measurement cannot detect, and state the assumptions of
your estimate.

**★★8.** Show that downward continuation from $z=0$ to $z=-h$ amplifies the
wavenumber-$k$ component by $\mathrm{e}^{kh}$, and compute the cutoff wavenumber
above which a continuation of 1 km amplifies a 0.1 % data error by more than a
factor of 100.

**★★★9.** Construct, and verify numerically, a *non-spherical* zero-total-mass
density perturbation and compute its exterior potential at two heights. Report
whether it is a null vector, and explain the result using the multipole expansion.
State clearly what your computation does and does not establish.

**★★★10.** Critically evaluate two published-style claims using only the
mathematics of this lesson: (a) "the anomaly requires a body at 4 km depth";
(b) "the potential-field data rule out a body deeper than 8 km". In each case
state which part of the data would have to be complete and noise-free for the
claim to be valid, and what prior information the claim is silently using.

## 12. Self-assessment checklist

- [ ] I can derive Poisson's equation from Gauss's law and state my sign
      convention before using it.
- [ ] I can state the four properties of harmonic functions and give a
      geophysical reading of each.
- [ ] I can prove Dirichlet uniqueness, and state the Neumann and Robin results
      with their differences.
- [ ] I can explain why uniqueness of the BVP does *not* contradict
      non-uniqueness of inversion, naming the four hypotheses real data violate.
- [ ] I can exhibit a null vector of the forward map and quantify how invisible it
      is.
- [ ] I can explain why downward continuation is ill posed and how
      regularisation relates to the data noise level.
- [ ] I can state why the 2-D kernel differs from the 3-D kernel and what breaks
      if they are confused.

## Related lessons

- [01-09-01 Classification of PDEs](./01-classification.md) — why this equation
  is elliptic, and what "no characteristics" implies for the data.
- [01-09-05 Separation of Variables and Boundary Conditions](./05-separation-of-variables.md)
  — the machinery for solving these problems on finite domains.
- [01-09-07 Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md)
  — well-posedness in general and the backward problems that fail it.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](./08-weak-solutions.md)
  — the variational formulation, and why the elliptic problem is the model case
  for Lax–Milgram.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md)
  — the prerequisite treatment, with the equivalence classes.
- [02-physics/08-potential-theory](../../02-physics/08-potential-theory/README.md)
  — the physical derivation of the potential, the field and Gauss's law.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the measurements and
  the interpretation to which this equation is applied.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the null space,
  regularisation and the resolution trade-off.
