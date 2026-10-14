---
id: 01-06-04
title: "Divergence, Curl and Physical Meaning"
level: intermediate
prereqs: ["01-05-03", "01-06-01"]
estimated_minutes: 90
tags: [multivariable-calculus, divergence, curl, gauss-law, ampere-law]
---

# Divergence, Curl and Physical Meaning

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the divergence and curl of a vector field, both by coordinate
   formulas and by their coordinate-free limits as flux and circulation
   densities.
2. **Interpret** divergence as source strength per unit volume and curl as twice
   the local angular velocity, and give a geophysical example of each.
3. **Recognise** the two identities that constrain every field built from a
   potential: $\nabla\cdot(\nabla\times\mathbf{F}) = 0$ and
   $\nabla\times\nabla f = \mathbf{0}$.
4. **State** Gauss's law for gravity, Gauss's law for magnetism and Ampère's law
   in both differential and integral form, and derive the differential form from
   the integral one.
5. **Decompose** a vector field into a divergence-free and a curl-free part, and
   explain why geophysics is full of scalar and vector potentials.
6. **Explain** what a conservation law written in divergence form asserts, and
   why the differential form fails at a surface of discontinuity where the
   integral form still holds.

## Prerequisites

- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md)
  — the divergence and curl are built from partial derivatives, and the gradient
  is the third operator with the same $\nabla$ symbol.
- [01-05-03 Differentiation Rules and Implicit Differentiation](../05-single-variable-calculus/03-differentiation-rules.md)
  — the product rules used in the derivations.
- [01-07-01 Vectors, Vector Spaces and Basis](../07-linear-algebra/01-vectors-and-spaces.md) —
  dot and cross products, without which $\nabla\cdot$ and $\nabla\times$ are
  meaningless.
- [02-07-02 Magnetostatics, Biot–Savart and Ampère's Law](../../02-physics/07-electromagnetism/02-magnetostatics.md)
  — useful in parallel; this lesson is the mathematical side of the same laws.

## 1. Intuition: two independent ways a field can vary

A vector field assigns an arrow to every point. Compare three situations.

- **A spring gushing water outward.** More flows out of any small closed surface
  than flows in. The field has **positive divergence** there.
- **A whirlpool.** Nothing accumulates, but a small paddle wheel placed in the
  flow spins. The field has **nonzero curl** there.
- **A river in steady, uniform flow.** Nothing accumulates and nothing spins.
  Divergence and curl both vanish; the field is constant.

Divergence and curl are *independent*. A field can have either, both or neither.
That independence is not an accident of how the operators are defined: it is a
structural fact about vector fields, and it is why the whole of potential-field
geophysics can be organised around two potentials.

| Operator | Measures | Units | Geophysical example | Law |
|---|---|---|---|---|
| $\nabla\cdot\mathbf{F}$ | Net outflow per unit volume | field $\times$ length$^{-1}$ | Mass source: rock that is denser than its surroundings | $\nabla\cdot\mathbf{g} = -4\pi G\rho$ |
| $\nabla\times\mathbf{F}$ | Twice local angular velocity | field $\times$ length$^{-1}$ | Vorticity of ocean or mantle flow | $\omega = \nabla\times\mathbf{v}$ |

Read that table once more and note where the two classic laws sit. **Gauss's law
for gravity is a statement about divergence. Ampère's law is a statement about
curl.** The first says that mass is the source of the gravitational field; the
second says that current is the source of the magnetic field's circulation. Both
are statements about the same two operators, and neither is a coincidence.

## 2. Precise definitions

### 2.1 The del operator

$$\nabla = \left(\frac{\partial}{\partial x},\,
\frac{\partial}{\partial y},\, \frac{\partial}{\partial z}\right).$$

It is an operator, so it must act on something. Acting on a scalar with the dot
product gives the gradient of
[01-06-01](./01-partial-derivatives.md); acting on a vector with the dot product
gives the divergence; acting with the cross product gives the curl. Those are
the only three first-order combinations, and geophysics uses all three.

### 2.2 Divergence

For a vector field $\mathbf{F} = (F_x, F_y, F_z)$,

$$\nabla\cdot\mathbf{F}
= \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y}
+ \frac{\partial F_z}{\partial z}.$$

The result is a **scalar field**. The coordinate-free definition, which is the
one that carries the physics, is

$$\nabla\cdot\mathbf{F}(\mathbf{p})
= \lim_{V\to 0}\frac{1}{V}\oint_{\partial V}\mathbf{F}\cdot d\mathbf{A},$$

the net flux out of a small closed surface, divided by the volume it encloses.
The coordinate formula is what you compute with; this limit is what it means.

### 2.3 Curl

$$\nabla\times\mathbf{F} =
\begin{vmatrix}
\hat{x} & \hat{y} & \hat{z}\\[1mm]
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z}\\[2mm]
F_x & F_y & F_z
\end{vmatrix}
= \left( \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z},\;
\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x},\;
\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right).$$

The determinant is a mnemonic for the three components, not a real determinant
(a determinant cannot contain derivatives and be evaluated literally), but it is
a reliable one provided the row order is remembered: $\partial/\partial y$ pairs
with $F_z$. The result is a **vector field**. Its coordinate-free definition is

$$\left(\nabla\times\mathbf{F}\right)\cdot\hat{n}(\mathbf{p})
= \lim_{A\to 0}\frac{1}{A}\oint_{\partial A}\mathbf{F}\cdot d\mathbf{l},$$

the circulation around a small loop perpendicular to $\hat{n}$, divided by the
enclosed area. The component of the curl along any direction is a circulation
density in that direction.

### 2.4 The Laplacian

$$\nabla^2 f = \nabla\cdot\nabla f
= \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}
+ \frac{\partial^2 f}{\partial z^2}.$$

Divergence of the gradient: the net outflow of a gradient field. It is the
operator of Laplace's and Poisson's equations, and therefore of the whole of
Lesson 08.

## 3. Derivations

### 3.1 Divergence is a flux density

Take a small axis-aligned box of side lengths $h_x, h_y, h_z$ centred on
$\mathbf{p}$, and compute the flux out of it. Consider only the two faces
perpendicular to $x$. The outward normals are $\pm\hat{x}$, and the flux through
them is approximately

$$h_y h_z\left[F_x\left(x + \tfrac{h_x}{2}\right) - F_x\left(x - \tfrac{h_x}{2}\right)\right]
\approx h_y h_z\, h_x \frac{\partial F_x}{\partial x}.$$

Adding the three pairs and dividing by the volume $h_x h_y h_z$ gives
$\nabla\cdot\mathbf{F}$ to leading order. Every term of the coordinate formula is
therefore the contribution of one pair of opposite faces, and
$\partial F_x/\partial x \neq 0$ means that $F_x$ changes across the box, so the
outflow on one face does not match the inflow on the other. $\square$

This is the first half of the divergence theorem of Lesson 06, obtained on a box
rather than a general region. It is also the reason the divergence has units of
field per length and not field times length.

### 3.2 Curl components are circulation densities

Apply the same box argument to the work done around a small loop in the
$xy$-plane. Traversing the rectangle counterclockwise, the integrals along the
two segments at fixed $x$ differ by
$-\frac{\partial F_y}{\partial x}h_x h_y$ and those along the two segments at
fixed $y$ differ by $+\frac{\partial F_x}{\partial y}h_x h_y$. Dividing by the
area $h_x h_y$ gives

$$\frac{1}{A}\oint \mathbf{F}\cdot d\mathbf{l}
= \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}
= (\nabla\times\mathbf{F})_z .$$

The cyclic permutations give the other two components. $\square$

### 3.3 The two structural identities

**First identity.** For any $C^2$ scalar field $f$,

$$\nabla\times\nabla f = \mathbf{0}.$$

*Proof.* The $z$ component is
$\partial(\partial f/\partial y)/\partial x - \partial(\partial f/\partial x)/\partial y
= f_{yx} - f_{xy} = 0$ by the Clairaut–Schwarz theorem from
[01-06-01](./01-partial-derivatives.md). $\square$

**Consequence.** Every gradient field is **irrotational**: it has no circulation
around any closed loop, so line integrals of it are path-independent. This is
what makes a potential well defined in the first place — Section 3.6 returns to
it.

**Second identity.** For any $C^2$ vector field $\mathbf{F}$,

$$\nabla\cdot(\nabla\times\mathbf{F}) = 0.$$

*Proof.* Expand:

$$\frac{\partial}{\partial x}\!\left(\frac{\partial F_z}{\partial y}
- \frac{\partial F_y}{\partial z}\right)
+ \frac{\partial}{\partial y}\!\left(\frac{\partial F_x}{\partial z}
- \frac{\partial F_z}{\partial x}\right)
+ \frac{\partial}{\partial z}\!\left(\frac{\partial F_y}{\partial x}
- \frac{\partial F_x}{\partial y}\right),$$

and every mixed partial appears twice with opposite signs. $\square$

**Consequence.** Every curl field is **solenoidal**: $\nabla\cdot\mathbf{B} = 0$
holds automatically for any $\mathbf{B} = \nabla\times\mathbf{A}$. This is why
the absence of magnetic monopoles can be written as a vector-potential
statement.

**Where these identities fail.** Both proofs use $C^2$ smoothness. Neither holds
pointwise at a source, which is exactly why the field of a point mass has
$\nabla\cdot\mathbf{g} = 0$ everywhere it can be evaluated and yet a nonzero flux
through every closed surface (Sections 3.4 and 5). The integral form survives
what the differential form cannot.

### 3.4 Gauss's law for gravity, differential form

With the convention of this module, $V = G\int\rho/D\,dV$, $\mathbf{g} = \nabla V$
and $\nabla^2 V = -4\pi G\rho$ (derived in [01-06-08](./08-potential-theory.md)).
Since $\mathbf{g} = \nabla V$,

$$\nabla\cdot\mathbf{g} = \nabla\cdot\nabla V = \nabla^2 V = -4\pi G\rho .$$

In words: **the divergence of the gravitational field is proportional to the local
mass density.** Away from all mass it vanishes, which is Laplace's equation
$\nabla\cdot\mathbf{g} = 0$.

Integrating over a volume and applying the divergence theorem of Lesson 06 turns
this into

$$\oint_{\partial\Omega}\mathbf{g}\cdot d\mathbf{A} = -4\pi G M_{\text{enc}},$$

the flux form. Two features are worth stating immediately, because they are the
reason this pair of equations is more useful than either one alone.

- The flux depends only on the **enclosed mass**, not on its distribution. This
  is Newton's shell theorem in another dress, and Section 5 verifies it for a
  cube-shaped surface — a shape for which no elementary theorem exists — as well
  as for a sphere.
- The differential form requires $\rho$ to be defined pointwise. Real density
  contrasts are discontinuities, across which $\rho$ is undefined. The flux form
  remains exactly valid. **Prefer the integral form when the model has sharp
  boundaries.**

### 3.5 Ampère's and Faraday's laws, and why magnetics has a potential

In magnetostatics, Ampère's law is

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J},$$

so the curl of the magnetic field is proportional to the current density that
drives it. Integrating over a surface and applying Stokes' theorem (Lesson 06)
gives

$$\oint_{\partial S}\mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{\text{enc}}.$$

Faraday's law, which is the engine of every electromagnetic method in
[08-04 Electromagnetic Induction in the Earth](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md), is

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}.$$

The minus sign is Lenz's law: the induced current opposes the change that
produced it.

Finally, $\nabla\cdot\mathbf{B} = 0$ everywhere, by the second identity of
Section 3.3 together with the existence of a vector potential. Integrating,

$$\oint_{\partial\Omega}\mathbf{B}\cdot d\mathbf{A} = 0
\qquad\text{for every closed surface,}$$

which is the mathematical statement that magnetic monopoles do not exist.

Now the payoff. In a region with no current and no time variation, both
$\nabla\cdot\mathbf{B} = 0$ and $\nabla\times\mathbf{B} = \mathbf{0}$ hold. A
curl-free field is a gradient (Section 3.6), so there exists a scalar function
$V_m$ with $\mathbf{B} = -\mu_0\nabla V_m$. **The entire scalar-potential
machinery of magnetic interpretation rests on two facts from this lesson: a
curl-free field is a gradient, and a divergence-free field is a curl.** Section 5
checks the scalar-potential representation numerically to three parts in
$10^{10}$.

### 3.6 Curl-free fields, potentials and simply connected domains

The statement "$\nabla\times\mathbf{F} = \mathbf{0}$ implies
$\mathbf{F} = \nabla\phi$" is true on any **simply connected** region — one in
which every closed loop can be contracted to a point without leaving the region.

It is *false* in general. The standard counterexample is

$$\mathbf{F} = \left(\frac{-y}{x^2+y^2},\ \frac{x}{x^2+y^2},\ 0\right),$$

which is smooth and curl-free everywhere except the $z$ axis, yet
$\oint\mathbf{F}\cdot d\mathbf{l} = 2\pi$ around any loop encircling the axis.
The region is not simply connected, the circulation is nonzero, and no
single-valued potential exists.

**Why this matters in geophysics.** A borehole is a hole in the domain. A
long conductor — a pipeline, a railway, a mineralised shear zone — is a
topological obstruction. Fields defined in such domains can have nonzero
circulations that no potential can reproduce. When a magnetotelluric or
controlled-source result refuses to be fitted by a potential, the first thing to
check is not the inversion but the topology of the domain. The mathematical
statement is developed in
[01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md)
and appears in practice as the distinction between fields produced by currents
and fields produced by magnetisation.

### 3.7 The Helmholtz decomposition

Any sufficiently smooth vector field that decays fast enough at infinity can be
written, uniquely up to boundary conditions, as

$$\mathbf{F} = \nabla\phi + \nabla\times\mathbf{A},$$

a curl-free part plus a divergence-free part. Taking the divergence gives
$\nabla^2\phi = \nabla\cdot\mathbf{F}$, so the scalar part is determined by the
sources; taking the curl gives the vector part.

Geophysics uses this constant decomposition without always naming it:

| Field | Curl-free part | Divergence-free part |
|---|---|---|
| Gravity | $\mathbf{g} = \nabla V$ (everywhere) | none: $\mathbf{g}$ has sources at mass |
| Magnetic anomaly outside source | $\mathbf{H} = -\nabla V_m$ | (the field of currents, if any) |
| Fluid velocity | irrotational flow $\mathbf{v} = \nabla\varphi$ | solenoidal flow $\mathbf{v} = \nabla\times\psi$ |
| Electromagnetic fields | the electrostatic part | the inductive part |

In a genuinely source-free, current-free region both statements hold at once: the
field is harmonic. That is the situation in Lesson 08.

## 4. Physical interpretation

**Divergence is the bookkeeping of conservation.** A conserved quantity with
density $u$ carried by a flux $\mathbf{J}$ satisfies

$$\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{J} = 0,$$

the **continuity equation**. In words: the amount of $u$ in a small box changes
only by what crosses its boundary, so any local loss must show up as a
divergence. Mass conservation in a deforming Earth, charge conservation in an
induced-polarisation survey, and the diffusion equation for temperature are all
this one statement. Note that the divergence here is of a *flux*, not of a field,
and the distinction matters: in a steady state $\nabla\cdot\mathbf{J} = 0$ even
though heat may be flowing vigorously.

**Divergence of a field is not the same as a source of the field.** Two traps.

1. In a region containing no mass, $\nabla\cdot\mathbf{g} = 0$ — but $\mathbf{g}$
   itself is not small. The field of a point mass has zero divergence everywhere
   away from the mass while decaying only as $1/r^2$.
2. A uniform field has zero divergence and zero curl but is not "nothing". A
   uniform magnetic field has no monopoles and no currents, and it still exerts
   force on a compass.

**Curl is rotation, and it survives without any rotation of the observer.**
Solid-body rotation with angular velocity $\boldsymbol{\Omega}$ gives
$\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r}$ and

$$\nabla\times\mathbf{v} = 2\boldsymbol{\Omega}.$$

Every parcel is being *sheared* — neighbouring parcels move at different
velocities — and it is the shear, not the rotation of the whole body, that the
curl detects. The classic consequence: a paddle wheel drifting in a rotating
ocean would not spin if the fluid rotated rigidly with the Earth, but it does
spin in a shear flow, and the vorticity $\boldsymbol{\omega}=\nabla\times\mathbf{v}$
is the field that measures it. In geophysical fluid dynamics, potential vorticity
is conserved in the absence of forcing, and that conservation is what organises
ocean gyres and weather systems.

**Sharp boundaries favour the integral form.** Where a density or conductivity
contrast exists, the differential form is undefined on the boundary but the flux
across it is perfectly determined. Practical consequence: forward-modelling codes
compute flux balances, and inversion codes that assemble the differential
operator must use a discretisation consistent with the integral form (a
staggered grid), or they will produce artefacts at contrasts.
[05-03-04 Numerical Forward Modelling and Discretisation](../../05-core-geophysics/03-forward-modelling-principles/04-numerical-forward-modelling.md)
takes this up.

## 5. Python demonstration

The companion script
[`code/divergence_curl_demo.py`](./code/divergence_curl_demo.py) computes the
divergence and the curl of four fields with central differences, using only the
standard library. The bodies, currents and masses are synthetic.

### 5.1 Divergence-free and curl-free outside a point source

Mass $10^{12}$ kg at the origin, evaluated at $(700, 400, -900)$ m,
$\lvert\mathbf{r}\rvert = 1216$ m:

```text
h =  1.0 m:  div g = -7.597997e-14 1/s^2   |curl g| = 6.858352e-14 1/s^2
h =  0.1 m:  div g = -7.597970e-16 1/s^2   |curl g| = 6.858249e-16 1/s^2
scale for comparison: |g|/r = 3.783179e-08 1/s^2
```

Both quantities fall by a factor of 100 when $h$ falls by 10, so both are
$O(h^2)$ truncation error against a scale of $3.8\times10^{-8}$: relative
residuals of $2\times10^{-6}$ and $2\times10^{-8}$. **The field of a point mass
is exactly solenoidal and exactly irrotational where it is defined.** The
nonzero numbers in the demo are the finite-difference scheme talking, not the
physics.

### 5.2 The flux of a point-mass field is a constant

```text
n_theta = 100: surface integral = -838.714065 m^3/s^2   relative error = 4.112e-05
n_theta = 400: surface integral = -838.681730 m^3/s^2   relative error = 2.570e-06
exact -4*pi*G*M = -838.679575 m^3/s^2
```

The surface integral was built from the explicit field $-GM\hat{r}/r^2$ on a
grid, not from the formula being tested. It converges to
$-4\pi GM = -838.6796\ \mathrm{m^3\,s^{-2}}$ as the grid is refined. Compare this
with Section 5.1: the *pointwise* divergence is zero and the *integral* of the
flux is not. Both statements are correct, and together they say that the source
is a singularity, not a region of nonzero divergence.

### 5.3 Solid-body rotation has vorticity and no divergence

```text
at (2000000.0, 1000000.0, 500000.0) m:  div v =  0.000000e+00 1/s
curl v = ( 0.000000e+00,  0.000000e+00,  1.458420e-04) 1/s
2*Omega = 1.458420e-04 1/s
```

With $\Omega = 7.2921\times10^{-5}$ rad/s — the Earth's mean rotation rate, a
standard published constant — the curl is exactly $2\Omega\hat{z}$, both in
magnitude and in direction. The divergence is zero to the last digit, because
rigid rotation neither compresses nor expands.

### 5.4 Ampère's law around a current-carrying wire

Current 5 kA along the $z$ axis, loop of radius 50 m:

```text
loop integral of B . dl around a circle of radius 50 m = 6.283185307e-03 T m
mu0 * I                                                  = 6.283185307e-03 T m
relative error                                           = 2.337e-13
curl B away from the wire at (30.0, 40.0, 12.0): ( 0.000e+00,  0.000e+00,  2.702e-16) 1/s
```

$\mu_0$ here is the conventional rounded value $4\pi\times10^{-7}$ H/m; since the
2019 redefinition of the SI it is a measured quantity rather than a defined one,
with a relative uncertainty of order $10^{-10}$, far below the quadrature error
of the loop integral. Two facts to take away: the circulation equals $\mu_0 I$
regardless of the loop's radius and shape, and the curl is zero at every point
off the wire, even though the field itself is not zero there.

### 5.5 A magnetic dipole: divergence-free, curl-free, and a gradient

Moment of the order of the Earth's dipole moment, evaluated at
$\lvert\mathbf{r}\rvert = 7.071$ Mm:

```text
at |r| = 7.071 Mm:  div B =  5.175003e-19 T/m
                       |curl B| = 9.654622e-19 T/m
scale |B|/r = 4.480000e-12 T/m
-grad V = ( 2.715290e-05,  1.629174e-05, -9.050967e-07) T
B       = ( 2.715290e-05,  1.629174e-05, -9.050967e-07) T
relative difference = 2.723e-10
```

Against a scale of $4.5\times10^{-12}$ T/m, both the divergence and the curl are
zero to a relative accuracy of about $10^{-7}$, and the scalar potential
$V_m = \frac{\mu_0}{4\pi}\mathbf{m}\cdot\hat{r}/r^2$ reproduces $\mathbf{B}$ to
three parts in $10^{10}$. This is Section 3.5 in numbers: outside the magnetised
body the field is both divergence-free and curl-free, hence a gradient of a
harmonic scalar potential, which is the entire basis of magnetic interpretation.

> **Breaking exercise.** In Section 5.1, change the observation point to
> $(100, 100, 100)$ m and shrink $r$ by a factor of 10 in stages. Predict whether
> the pointwise divergence will stay zero. Then explain what you see: the
> singularity is at the origin, and the stencil cannot resolve a field that
> varies on a scale comparable to $h$.

## 6. Exercises

Ten graded exercises are in
[`exercises/04-divergence-and-curl-exercises.md`](./exercises/04-divergence-and-curl-exercises.md)
and worked solutions in
[`exercises/04-divergence-and-curl-solutions.md`](./exercises/04-divergence-and-curl-solutions.md).

## 7. Common mistakes

1. **Writing $\nabla\cdot\mathbf{F} = 0$ and concluding $\mathbf{F} = \mathbf{0}$.**
   The point-mass field is the counterexample, and it is in Section 5.1.
2. **Thinking divergence-free means "no flow through any surface".** It means
   equal flux in and out of every *closed* surface; flux through an open surface
   is generally nonzero.
3. **Forgetting that curl-free implies a potential only on a simply connected
   domain.** Section 3.6 gives the counterexample that a borehole or a
   conductor makes relevant.
4. **Assuming the differential form is always the more fundamental one.** At a
   density or conductivity contrast the differential form is undefined and the
   integral form is exact.
5. **Mixing up the two identities.** $\nabla\times\nabla f = \mathbf{0}$ is about
   gradients; $\nabla\cdot(\nabla\times\mathbf{F}) = 0$ is about curls. Writing
   "$\nabla\cdot\nabla f = 0$" as an identity is wrong: that is Laplace's
   equation, a *condition* on $f$, not a theorem about all $f$.
6. **Sign errors in the physics.** With the potential convention of this module,
   $\nabla\cdot\mathbf{g} = -4\pi G\rho$. With the physics convention
   $\Phi = -V$ it is $+4\pi G\rho$. State the convention.
7. **Treating vorticity as "the fluid is rotating".** Rigid-body rotation of the
   *observer's* frame produces no vorticity of the flow; it is spatial shear that
   vorticity measures.
8. **Applying the maximum-principle intuition to a divergence.** Divergence
   tells you about sources, not about extrema; those are different theorems.

## 8. Real-world applications

- **Gravity and magnetics.** $\nabla\cdot\mathbf{g} = -4\pi G\rho$ and
  $\nabla\cdot\mathbf{B} = 0$ are the two constraints that every potential-field
  inversion must satisfy, and the reason both are solved in terms of a potential
  rather than a field. See
  [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md).
- **Electromagnetic induction.** Faraday's law in curl form is the governing
  equation of magnetotellurics and of every controlled-source EM method. Combine
  it with Ampère's law and the divergence condition and you obtain the diffusion
  equation for the fields; see
  [08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md)
  and [02-07-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md).
- **Geophysical fluid dynamics.** Vorticity is the central variable of
  rotating-fluid theory; the vorticity equation is obtained by taking the curl of
  the momentum equation, which is why the curl is the first operator taught in
  dynamical meteorology and physical oceanography. See
  [02-06-07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](../../02-physics/06-fluid-mechanics/07-geophysical-fluids.md).
- **Mantle convection.** The Stokes equations are solved in a
  divergence-free velocity basis; a nonzero divergence of velocity would mean
  mass is being created, and the residual divergence is a standard convergence
  diagnostic for any convection solver.
- **Seismic wave propagation.** The elastodynamic equation separates into a
  curl-free (P) part and a divergence-free (S) part of the displacement field
  under the Helmholtz decomposition, which is why $\nabla\cdot\mathbf{u}$ measures
  P-wave content and $\nabla\times\mathbf{u}$ measures S-wave content in an
  isotropic medium. See
  [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md).
- **Continuity and conservation.** Mass conservation in subsidence, salt
  diapirism and glaciology is written in the divergence form of Section 4; the
  discretisation choice determines whether the model conserves mass exactly.

## 9. Further reading

- **Schey, H. M. *Div, Grad, Curl, and All That.* W. W. Norton.** The most
  readable treatment of exactly the material in Sections 1–3, with careful
  physics. Level: beginner to intermediate.
- **Marsden, J. E., & Tromba, A. *Vector Calculus.* W. H. Freeman.** Rigorous
  treatment of the operators, the identities and the Helmholtz decomposition.
  Level: intermediate.
- **Griffiths, D. J. *Introduction to Electrodynamics.* Cambridge University
  Press.** Chapters 1–2 and 5–6 present divergence, curl, Gauss's law and
  Ampère's law in the least painful order; the physics is exactly what Section
  3.4–3.5 uses. Level: intermediate. Any recent edition.
- **Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for
  Physicists.* Academic Press.** A compact reference for the operator algebra,
  product rules and the vector potential. Level: advanced. Any recent edition.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** How the source
  relationships are used in survey design and interpretation. Level:
  intermediate.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** Chapter 1 for the source
  relations in the notation of applied potential fields, including the reasons a
  scalar potential exists in the source-free region. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md) —
  the first operator, and the source of the identities in Section 3.3.
- [05 Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) —
  the integrals whose limits define divergence and curl.
- [06 Gauss, Stokes and Green Theorems](./06-integral-theorems.md) — the
  theorems that convert Section 3 between integral and differential form.
- [07 Vector Identities and Their Role in Geophysics](./07-vector-identities.md) —
  the algebra these operators obey, verified numerically.
- [08 Potential Fields, Laplace and Poisson Equations](./08-potential-theory.md) —
  what happens when both divergence and curl vanish.
- [02-07-03 Maxwell's Equations and Their Physical Meaning](../../02-physics/07-electromagnetism/03-maxwell-equations.md) —
  the physics course's four equations, in the language of this lesson.

## Self-assessment checklist

- [ ] I can compute the divergence and curl of a given field in Cartesian
      coordinates without looking up the formulas. (Sections 2.2–2.3)
- [ ] I can state the coordinate-free limit definitions and say what the
      denominator means in each. (Sections 2.2–2.3)
- [ ] I can derive the two structural identities and state the smoothness they
      need. (Section 3.3)
- [ ] I can write Gauss's law for gravity in differential and integral form and
      derive one from the other. (Section 3.4)
- [ ] I can state Ampère's law, Faraday's law and $\nabla\cdot\mathbf{B}=0$, and
      explain why magnetics has a scalar potential in source-free regions.
      (Section 3.5)
- [ ] I can explain why curl-free does not always imply a potential, and name a
      geophysical domain where the difference matters. (Section 3.6)
- [ ] I can write a conservation law in divergence form and interpret each term.
      (Section 4)
- [ ] I can explain what the Helmholtz decomposition gives to gravity, magnetics
      and seismology. (Section 3.7)
- [ ] I can say why the integral form of a source law is preferable at a sharp
      material boundary. (Sections 3.4, 4)
