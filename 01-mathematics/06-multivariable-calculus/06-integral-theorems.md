---
id: 01-06-06
title: "Gauss, Stokes and Green Theorems"
level: advanced
prereqs: ["01-06-04", "01-06-05"]
estimated_minutes: 90
tags: [multivariable-calculus, divergence-theorem, stokes-theorem, greens-identities, boundary-value]
---

# Gauss, Stokes and Green Theorems

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the divergence theorem, Stokes' theorem and Green's theorem with
   their hypotheses and their orientation conventions.
2. **Derive** each of the three from the local box or rectangle result, and
   explain the cancellation of interior faces or edges that makes the global
   statement work.
3. **Derive** Green's first and second identities from the divergence theorem,
   and explain why they are the natural tool for boundary-value problems.
4. **Obtain** Gauss's law for gravity and Ampère's law from the theorems, and
   explain what each theorem contributes to each law.
5. **Convert** a differential equation on a region into a boundary integral
   equation, and say what that buys conceptually and computationally.
6. **Recognise** why the theorems hold for regions with corners, edges and
   piecewise-smooth boundaries, and where their hypotheses genuinely fail.

## Prerequisites

- [01-06-04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) —
  the operators whose volume and surface integrals the theorems equate.
- [01-06-05 Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) —
  the integrals themselves, and the solid-angle flux argument reused here.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](./03-jacobians.md) —
  the volume element, and the orientation sign that appears in every statement.
- [01-05-06 Improper Integrals, Singularities and Convergence](../05-single-variable-calculus/06-improper-integrals.md) —
  relevant to the limiting argument that produces the delta function in
  Section 3.6.

## 1. Intuition: what is inside shows up on the boundary

Every integral theorem in vector calculus is a single idea in different
dimensions:

> **The total of a derivative over a region equals the total of the function on
> the boundary of that region.**

The fundamental theorem of calculus is the one-dimensional case:
$\int_a^b f'(x)\,dx = f(b) - f(a)$. The "boundary" of the interval $[a,b]$ is its
two endpoints. The divergence theorem is the three-dimensional case; Stokes'
theorem is the two-dimensional case for surfaces. The pattern is a theorem in
itself — the generalised Stokes theorem on manifolds — but for geophysics the
three classical forms are enough, and they are the ones that carry the names of
the physical laws.

| Theorem | Relates | Equates |
|---|---|---|
| Fundamental theorem | a function to its endpoints | $\int_a^b f'\,dx = f(b)-f(a)$ |
| Gradient theorem | a gradient to a curve's endpoints | $\int_C \nabla f\cdot d\mathbf{l} = f(\mathbf{p}_1)-f(\mathbf{p}_0)$ |
| Divergence theorem | a divergence to a closed surface | $\oint_{\partial\Omega}\mathbf{F}\cdot d\mathbf{A} = \int_\Omega \nabla\cdot\mathbf{F}\,dV$ |
| Stokes' theorem | a curl to a closed curve | $\oint_{\partial S}\mathbf{F}\cdot d\mathbf{l} = \int_S (\nabla\times\mathbf{F})\cdot d\mathbf{A}$ |
| Green's theorems | a Laplacian to a boundary | the identities of Section 3.5 |

Two features recur and are worth stating up front, because they are the reason
the integral forms are the *physical* ones.

1. **No derivative is required inside the region, only an integral.** A model
   with sharp density or conductivity contrasts has no well-defined
   $\nabla\cdot\mathbf{F}$ on the contrast surface, but its fluxes are perfectly
   well defined. The integral form survives; the differential form does not.
2. **A source inside the region cannot be hidden.** Whatever is enclosed
   contributes to the boundary integral, and only what is enclosed: Sections 3.4
   and 3.5 turn this into the law of gravitation and Ampère's law.

## 2. Precise statements

### 2.1 The divergence theorem (Gauss–Ostrogradsky)

Let $\Omega$ be a bounded region with piecewise-smooth, positively oriented
(outward) boundary $\partial\Omega$, and let $\mathbf{F}$ be continuously
differentiable on $\Omega$ and continuous up to the boundary. Then

$$\oint_{\partial\Omega}\mathbf{F}\cdot d\mathbf{A}
= \iiint_\Omega \nabla\cdot\mathbf{F}\, dV .$$

"Piecewise smooth" is not a technicality for geophysics: it is exactly the
condition that lets the region have faults, corners and material boundaries. The
theorem holds for any polyhedron and for any region with finitely many smooth
patches, provided the field is continuous up to the boundary. It does **not**
hold if the field has a singularity on the boundary.

### 2.2 Stokes' theorem

Let $S$ be an oriented piecewise-smooth surface with piecewise-smooth boundary
curve $\partial S$, oriented consistently with the surface normal by the
right-hand rule, and let $\mathbf{F}$ be continuously differentiable. Then

$$\oint_{\partial S}\mathbf{F}\cdot d\mathbf{l}
= \iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{A} .$$

The consistency condition in words: if you walk around $\partial S$ with your
head pointing along the normal, the surface is on your left. Reversing either
orientation flips the sign of both sides, so the theorem is invariant under the
pair of reversals and only meaningful when the pair is specified.

### 2.3 Green's theorem

Let $D$ be a plane region with positively oriented (counterclockwise) boundary
$\partial D$, and let $P$ and $Q$ be continuously differentiable. Then

$$\oint_{\partial D}\bigl(P\,dx + Q\,dy\bigr)
= \iint_D \left(\frac{\partial Q}{\partial x}
- \frac{\partial P}{\partial y}\right) dx\, dy .$$

Green's theorem is Stokes' theorem for the planar field $(P,Q,0)$; the term
$\partial Q/\partial x - \partial P/\partial y$ is the $z$ component of its curl.
Its two-dimensional companion, obtained instead from the divergence theorem, is

$$\oint_{\partial D}\mathbf{F}\cdot\hat{n}\,dl
= \iint_D \nabla\cdot\mathbf{F}\, dA ,$$

where $\hat{n}$ is the outward normal of the plane region. This version is the one
used in two-dimensional gravity and magnetic modelling, where the body is
invariant along one horizontal axis.

### 2.4 Hypotheses: what genuinely can fail

- **A singularity on or inside the region.** $\mathbf{F} = \hat{r}/r^2$ violates
  the hypotheses at $r=0$. Its flux through a closed surface is nevertheless
  $4\pi$, and that number is the physical content of Poisson's equation. The
  remedy is to excise a small ball around the singularity, apply the theorem on
  the rest, and take the limit — the argument in
  [01-06-05](./05-line-surface-integrals.md) Section 3.3 in integral form.
- **A non-orientable surface.** There is no consistent normal, so no flux. This
  does not arise for the surfaces of geophysics, but it is why Stokes' theorem
  is always stated for an *orientable* surface.
- **Discontinuity of the field across the boundary.** Piecewise continuity is
  enough provided the theorem is applied to each sub-region and the internal
  boundary fluxes are combined. That is how a layered Earth is handled.

## 3. Derivations

### 3.1 The divergence theorem, by patching boxes

Apply the box argument of [01-06-04](./04-divergence-and-curl.md) Section 3.1 to
an axis-aligned box $B$ of volume $V$: the flux of $\mathbf{F}$ out of $B$ equals
$(\nabla\cdot\mathbf{F})V + o(V)$, with the error uniform for smooth $\mathbf{F}$.

Now partition $\Omega$ into a family of such boxes, adapted to the boundary (in
practice, take a uniform lattice and keep the cells whose centres lie inside;
the boundary cells contribute an error that vanishes with the lattice spacing for
a piecewise-smooth boundary). Sum the identity over all boxes:

$$\sum_{\text{boxes}} \oint_{\partial B}\mathbf{F}\cdot d\mathbf{A}
= \sum_{\text{boxes}} \left[(\nabla\cdot\mathbf{F})V + o(V)\right]
\longrightarrow \iiint_\Omega \nabla\cdot\mathbf{F}\, dV .$$

On the left, every internal face is shared by two boxes and is traversed with
opposite normals. The field is continuous, so the two contributions are equal and
opposite and cancel exactly, leaving only the faces on $\partial\Omega$. Hence

$$\oint_{\partial\Omega}\mathbf{F}\cdot d\mathbf{A}
= \iiint_\Omega \nabla\cdot\mathbf{F}\, dV . \qquad\square$$

**The cancellation of interior faces is the whole content of the theorem.**
Everything else is bookkeeping. This is also why the theorem is robust to the
shape of the region: the cancellation happens wherever the boxes meet.

### 3.2 Stokes' theorem, by patching rectangles

The same argument one dimension lower. On a small planar rectangle in the plane
with unit normal $\hat{n}$, the circulation argument of
[01-06-04](./04-divergence-and-curl.md) Section 3.2 gives

$$\oint_{\partial \text{rect}}\mathbf{F}\cdot d\mathbf{l}
= (\nabla\times\mathbf{F})\cdot\hat{n}\,A + o(A).$$

Partition $S$ into small patches, apply the identity to each, and sum. Interior
edges are shared by two patches and traversed in opposite directions, so they
cancel; only $\partial S$ remains. Taking the limit of the partition,

$$\oint_{\partial S}\mathbf{F}\cdot d\mathbf{l}
= \iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{A} . \qquad\square$$

Because the argument is local and then patched, $S$ need not be flat, and
$\partial S$ need not be planar. That is the reason Stokes' theorem is stated for
curved surfaces.

### 3.3 Green's theorem from Stokes

Apply Stokes' theorem to $\mathbf{F} = (P, Q, 0)$ on the flat surface $S = D$ in
the plane $z = 0$, with upward normal $\hat{z}$. Then
$(\nabla\times\mathbf{F})_z = \partial Q/\partial x - \partial P/\partial y$, and
$(\nabla\times\mathbf{F})\cdot d\mathbf{A} = (\partial Q/\partial x - \partial
P/\partial y)\,dx\,dy$. The curve integral is
$\oint (P\,dx + Q\,dy)$ because $d\mathbf{l} = (dx, dy, 0)$. Substituting gives
Green's theorem of Section 2.3. $\square$

### 3.4 Gauss's law for gravity, and the shape-independence of flux

Apply the divergence theorem to $\mathbf{F} = \mathbf{g}$ on a region $\Omega$
that contains mass of total $M_{\text{enc}}$:

$$\oint_{\partial\Omega}\mathbf{g}\cdot d\mathbf{A}
= \iiint_\Omega \nabla\cdot\mathbf{g}\, dV
= \iiint_\Omega (-4\pi G\rho)\, dV = -4\pi G M_{\text{enc}},$$

using $\nabla\cdot\mathbf{g} = -4\pi G\rho$ from
[01-06-04](./04-divergence-and-curl.md) Section 3.4. This is **Gauss's law for
gravity**, and it is the divergence theorem applied to exactly one field.

Reading it as physics rather than as algebra:

- The **surface** may be any closed surface — sphere, cube, draped topography.
  Section 5.1 verifies the cube numerically against the sphere.
- The **value** depends only on the enclosed mass. Newton's shell theorem, and
  the non-uniqueness of potential-field inversion, both follow from this line.
- The **differential form** $\nabla\cdot\mathbf{g} = -4\pi G\rho$ is this
  statement applied to an arbitrarily small region, with the surface integral
  replaced by the divergence evaluated at a point. It is legitimate only where
  $\rho$ is defined.

### 3.5 Green's identities, and why they matter

Apply the divergence theorem to the field $\phi\nabla\psi$ for two $C^2$ scalar
fields. Since $\nabla\cdot(\phi\nabla\psi) = \nabla\phi\cdot\nabla\psi +
\phi\nabla^2\psi$,

$$\oint_{\partial\Omega}\phi\,\frac{\partial\psi}{\partial n}\, dA
= \iiint_\Omega \left(\nabla\phi\cdot\nabla\psi + \phi\,\nabla^2\psi\right) dV,
\qquad\text{(Green's first identity)}$$

where $\partial\psi/\partial n = \nabla\psi\cdot\hat{n}$ is the normal
derivative. Interchanging $\phi$ and $\psi$ and subtracting gives the symmetric
form

$$\oint_{\partial\Omega}\left(\phi\frac{\partial\psi}{\partial n}
- \psi\frac{\partial\phi}{\partial n}\right) dA
= \iiint_\Omega \left(\phi\,\nabla^2\psi - \psi\,\nabla^2\phi\right) dV,
\qquad\text{(Green's second identity)}$$

These two identities do the analytical work of the whole of potential theory, and
the reason is visible in their shape: **a Laplacian inside the region is
converted into data on the boundary.** If $\phi$ and $\psi$ are both harmonic,
the right-hand side of the second identity vanishes and the boundary expression is
also zero — a constraint relating the two functions on $\partial\Omega$ alone.

Green's first identity has an immediate corollary that Lesson 08 uses, so state
it here. Take $\phi = \psi = w$ with $\nabla^2 w = 0$ in $\Omega$ and $w = 0$ on
$\partial\Omega$. Then the boundary term is zero and

$$\iiint_\Omega \lvert\nabla w\rvert^2\, dV = 0
\quad\Longrightarrow\quad \nabla w = \mathbf{0} \text{ in } \Omega .$$

A harmonic function that vanishes on the boundary of a region vanishes
identically throughout it (on a connected region). That is the **uniqueness of
the Dirichlet problem**, and it comes from a positivity argument — the integral
of a square cannot be zero unless the integrand is.

### 3.6 The representation theorem and the equivalent-source ambiguity

Apply Green's second identity to a harmonic function $u$ and to the Green's
function $\tfrac{1}{4\pi D}$, where $D = \lvert\mathbf{r} - \mathbf{r}'\rvert$ and
$\mathbf{r}'$ is a point of $\Omega$. The function $1/D$ is singular at
$\mathbf{r}'$, so the region is first punctured by a small sphere about
$\mathbf{r}'$; the surface integral over that small sphere survives the limit and
produces $u(\mathbf{r}')$. The result, **Green's third identity**, is

$$u(\mathbf{r}') = \frac{1}{4\pi}\oint_{\partial\Omega}
\left[\frac{1}{D}\,\frac{\partial u}{\partial n}
- u\,\frac{\partial}{\partial n}\!\left(\frac{1}{D}\right)\right] dA,
\qquad \mathbf{r}' \in \Omega .$$

Stated here without the limiting argument in full — the derivation is in
Section 9's references — but the consequence must be emphasised, because it is
the theoretical root of the ambiguity in every potential-field inversion:

> **A harmonic function inside a region is entirely determined by its values and
> its normal derivative on the boundary.**

Two readings follow, and they pull in opposite directions.

1. **Existence and uniqueness on a bounded domain.** If the boundary data are
   known — potential on the surface, for example — the interior field is
   determined. This is the well-posed boundary-value problem of the Dirichlet or
   Neumann type, and it is why upward continuation has a unique answer.
2. **Non-uniqueness of the inverse problem.** In the geophysical problem the
   *boundary* is the Earth's surface and the interior contains the unknown
   sources. Different source distributions produce the same boundary data if they
   differ by a distribution whose induced boundary values and normal derivatives
   cancel. The representation theorem guarantees that the boundary data
   determine the *field above the surface*, and says nothing whatever about what
   produced it. Lesson 08 makes the ambiguity concrete; Section 5.5 of this
   lesson makes it numerical.

### 3.7 Ampère's law and the magnetic flux, from the theorems

Applying Stokes' theorem to $\mathbf{B}$ and using $\nabla\times\mathbf{B} =
\mu_0\mathbf{J}$,

$$\oint_{\partial S}\mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{\text{enc}},
\qquad\text{(Ampère's law, integral form)}$$

which is the statement verified numerically in
[01-06-05](./05-line-surface-integrals.md) Section 5.3. Applying the divergence
theorem to $\mathbf{B}$ and using $\nabla\cdot\mathbf{B} = 0$,

$$\oint_{\partial\Omega}\mathbf{B}\cdot d\mathbf{A} = 0
\qquad\text{for every closed surface,}$$

the statement that no magnetic monopole exists. Faraday's law in integral form
comes from Stokes' theorem applied to $\mathbf{E}$:

$$\oint_{\partial S}\mathbf{E}\cdot d\mathbf{l}
= -\frac{d}{dt}\iint_S \mathbf{B}\cdot d\mathbf{A},$$

and it is the equation solved, in discretised form, by every electromagnetic
forward-modelling code in
[08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md)
(see also
[08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md)).

## 4. Physical interpretation

**The theorems are why geophysics is written in terms of potentials and
fluxes.** A physical law stated as a flux through a closed surface (Gauss) or a
circulation around a loop (Ampère, Faraday) is stated in a form that needs no
differentiability of the medium and no assumption of smooth sources. The
differential forms are then derived, and they are the ones discretised for
computation — but they inherit their validity from the integral forms.

**The theorems turn a partial differential equation into a boundary integral
equation.** Take a Dirichlet problem: $\nabla^2 u = 0$ in $\Omega$, $u = f$ on
$\partial\Omega$. The representation theorem of Section 3.6 expresses $u$ inside
$\Omega$ as a boundary integral of $u$ and $\partial u/\partial n$ on
$\partial\Omega$. If one of those two boundary data is known, the other can be
solved for by taking $\mathbf{r}'$ to the boundary, which produces a **boundary
integral equation**. Two consequences of practical importance:

- The unknown lives on a surface of one dimension fewer, so the system of
  equations is far smaller than for a volume discretisation.
- The kernel is the same $1/D$ every time, so the method is independent of the
  discretisation of the interior — and this is exactly the structure of
  equivalent-source and boundary-element methods in potential-field modelling.

**A conservation law is the divergence theorem in disguise.** Integrate
$\partial u/\partial t + \nabla\cdot\mathbf{J} = 0$ over a fixed volume and apply
the divergence theorem: the rate of change of the total of $u$ inside equals minus
the flux of $\mathbf{J}$ out through the boundary. This is the form in which
conservation is actually *verified* in a numerical code, because it is a statement
about a finite volume and its faces rather than about a point.

**Corners and edges are not a problem; kinks in the field are.** The theorems
hold on polyhedra and on regions with piecewise-smooth boundaries. What they do
not tolerate is a field that is infinite on the boundary. Practical consequence:
the analytical gravity formula for a polyhedron is well behaved at a station on
an *edge*, and singular at a station *inside* or exactly on a face, and the
formulas must be arranged to reflect that.

**Every finite-difference or finite-element method is a discretised integral
theorem.** A conservative finite-volume scheme is a discretisation of the
divergence theorem face by face; a nodal finite-element scheme is a
discretisation of Green's first identity. When such a scheme conserves mass
exactly, it is because the interior-face cancellation of Section 3.1 has been
preserved by construction. When it does not, the cancellation has been broken.
See [05-03-04 Numerical Forward Modelling and Discretisation](../../05-core-geophysics/03-forward-modelling-principles/04-numerical-forward-modelling.md)
and [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md).

## 5. Python demonstration

[`code/integral_theorems_demo.py`](./code/integral_theorems_demo.py) computes
both sides of each theorem independently, with the standard library only. Two
values of the grid parameter are used throughout, because a theorem checked at
one resolution is not checked at all.

### 5.1 The divergence theorem on the unit cube

For $\mathbf{F} = (x^3y,\ y^3z,\ z^3x)$ on $[0,1]^3$, whose divergence is
$3(x^2y + y^2z + z^2x)$:

```text
n =  50:  volume integral of div F = 1.4998500000
          surface flux of F        = 1.5000000000
          exact 3/2                = 1.5000000000
n = 200:  volume integral of div F = 1.4999906250
          surface flux of F        = 1.5000000000
          exact 3/2                = 1.5000000000
```

Both sides converge to $3/2$. The surface side is exact because each face
integrand is linear in the face coordinates, so the midpoint rule integrates it
without error; the volume side has a cubic integrand and converges from below.
**That the two sides are computed by entirely different quadratures and agree is
the evidence.**

### 5.2 Gauss's law through a cube: only the enclosed mass matters

```text
n =  60:  flux of g through the cube = -838.736660 m^3/s^2   relative error = 6.807e-05
n = 240:  flux of g through the cube = -838.683143 m^3/s^2   relative error = 4.254e-06
exact -4*pi*G*M = -838.679575 m^3/s^2
```

Compare with the same number obtained from a spherical surface in
[`code/divergence_curl_demo.py`](./code/divergence_curl_demo.py):

```text
n_theta = 400: surface integral = -838.681730 m^3/s^2   relative error = 2.570e-06
exact -4*pi*G*M = -838.679575 m^3/s^2
```

A cube and a sphere, the same flux, to within each quadrature's own error. The
surface shape is irrelevant, as Section 3.4 says it must be.

### 5.3 Stokes' theorem and Green's theorem on the unit disk

```text
circulation of F on the unit circle        = 6.2831853072
m = 200:  flux of curl F over the disk = 6.2856000000
m = 800:  flux of curl F over the disk = 6.2831500000
exact 2*pi                                 = 6.2831853072
```

The circulation around the circle is computed by a line quadrature and the flux
of the curl by an area quadrature; they agree at $2\pi$ to the accuracy of the
coarser of the two. The relative errors are $3.8\times10^{-4}$ at $m = 200$ and
$5.6\times10^{-6}$ at $m = 800$: the theorem has been confirmed to four and then
six significant figures, not to machine precision. That is what a numerical check
of an integral identity looks like — the agreement is limited by the quadrature, and
reporting the residual is part of the result.

### 5.4 The mean value property: a boundary integral with content

```text
n = 100:  sphere average of V = 1.334853827e-02   V at the centre = 1.334800000e-02   rel. diff = 4.033e-05
n = 400:  sphere average of V = 1.334803364e-02   V at the centre = 1.334800000e-02   rel. diff = 2.520e-06
same test for f = x^2 + y^2 + z^2: sphere average = 1000002.570215   centre value = 0.000000
```

The first function is $GM/D$ with the source outside the test sphere; it is
harmonic on and inside the sphere, and its average over the surface equals its
centre value, at the quadrature accuracy. The second has Laplacian $6$, and the
property fails completely. **The mean value property is a boundary-integral
statement of harmonicity**, and it is the engine of the uniqueness proof in
Lesson 08.

> **Breaking exercise.** In Section 5.1, replace $\mathbf{F}$ with a field whose
> divergence has a term in $1/x$. Predict what happens to the volume quadrature
> near $x = 0$ and whether the surface side will still converge, then run it. The
> answer is the reason the hypotheses of Section 2.4 matter.

## 6. Exercises

Ten graded exercises are in
[`exercises/06-integral-theorems-exercises.md`](./exercises/06-integral-theorems-exercises.md)
and worked solutions in
[`exercises/06-integral-theorems-solutions.md`](./exercises/06-integral-theorems-solutions.md).

## 7. Common mistakes

1. **Getting the orientation wrong.** An outward normal on a closed surface, and
   a right-hand-rule convention for a curve, are part of the statement of the
   theorems. Half of all sign errors in flux arguments trace back to this.
2. **Applying the divergence theorem across a singularity.** Excision of a small
   ball is required; skipping it is how people conclude that a point mass has no
   flux.
3. **Confusing Green's *theorem* with Green's *identities*.** The first is
   Stokes' theorem in the plane; the others are consequences of the divergence
   theorem and are the tools of boundary-value problems. The names collide, the
   statements do not.
4. **Believing the differential form is always equivalent to the integral form.**
   They differ wherever a source is concentrated on a surface or a curve. Sharp
   boundaries are the norm in the Earth, not the exception.
5. **Using Green's first identity with the wrong sign for the normal.** The
   identity requires the *outward* normal, so $\partial\psi/\partial n$ is the
   derivative leaving the region.
6. **Assuming a boundary integral method has no discretisation error.** It has:
   the boundary is discretised, and the kernel $\tfrac{1}{4\pi D}$ is mildly
   singular when the evaluation point reaches the boundary, requiring a special
   treatment.
7. **Forgetting that the theorems need the field continuous up to the boundary.**
   A station exactly on the surface of a uniform polyhedron is a genuine
   singularity, not a numerical inconvenience.
8. **Treating the cancellation of interior faces as automatic in a numerical
   scheme.** It is automatic in the mathematics and optional in the code.

## 8. Real-world applications

- **Gauss's law for gravity and magnetics.** The flux form is the standard proof
  that a spherically symmetric body behaves as a point mass outside itself, and
  it underwrites the depth-density ambiguity of
  [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md).
- **Boundary-element and equivalent-source modelling.** The representation
  theorem converts a potential-field problem into an integral over a surface, the
  basis of equivalent-source techniques and of fast multipole methods.
  See [07-03-03 Forward Modelling in 2-D and 3-D](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/03-forward-modelling-2d3d.md).
- **Conservation in numerical models.** Every finite-volume scheme in
  [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) is a
  discrete divergence theorem; every conservative finite-element scheme is a
  discrete Green's identity.
- **Electromagnetic methods.** Faraday's and Ampère's laws in integral form are
  the equations discretised by every EM forward solver, and the integral form is
  what guarantees an exactly divergence-free magnetic field. See
  [08-04-04 MT Inversion](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/04-mt-inversion.md).
- **Resistivity and self-potential.** The current density field in a resistivity
  survey satisfies $\nabla\cdot\mathbf{J} = 0$ in the ground with point sources
  at the electrodes; the flux form is what fixes the source strengths. See
  [09-02-06 Forward Modelling Resistivity Data](../../09-electrical-em-methods/02-dc-resistivity/06-resistivity-forward-modelling.md).
- **Fluid mass balance.** Catchment and aquifer budgets are flux statements over
  closed surfaces; the divergence theorem is what makes them equivalent to the
  differential conservation law, and the surface choice determines which budget
  terms appear.
- **Seismic reciprocity and representation theorems.** The elastic counterpart of
  Green's second identity is the starting point for the representation theorem of
  seismology, which underlies interferometry and adjoint tomography.

## 9. Further reading

- **Marsden, J. E., & Tromba, A. *Vector Calculus.* W. H. Freeman.** The three
  theorems, their hypotheses and the patching proofs of Sections 3.1–3.2 in full.
  Level: intermediate. Check your library for the current edition.
- **Schey, H. M. *Div, Grad, Curl, and All That.* W. W. Norton.** The physical
  arguments behind the theorems, with the solid-angle and box pictures used here.
  Level: beginner to intermediate.
- **Kellogg, O. D. *Foundations of Potential Theory.* Springer.** Originally
  published in 1929 and still the standard rigorous account of Green's
  identities, the representation theorem and the boundary-value problems of
  potential theory. Level: graduate.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** The divergence theorem, Green's
  identities and the equivalent-source formulation in the notation of applied
  potential fields. Level: advanced.
- **Griffiths, D. J. *Introduction to Electrodynamics.* Cambridge University
  Press.** Chapters 1–2 give the theorems alongside the physical laws of Section
  3.7, which is the pairing in which most students first understand them. Level:
  intermediate. Any recent edition.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed.). Wiley.** The
  boundary-value problem machinery — Green's functions, Dirichlet and Neumann
  conditions — developed for exactly the equations used in electromagnetics.
  Level: graduate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) — the
  local results that these theorems patch together.
- [05 Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) —
  the integrals being equated.
- [07 Vector Identities and Their Role in Geophysics](./07-vector-identities.md) —
  the algebra used inside the derivations.
- [08 Potential Fields, Laplace and Poisson Equations](./08-potential-theory.md) —
  where Green's identities become uniqueness theorems and the ambiguity of
  inversion.
- [01-09-07 Boundary and Initial-Boundary Value Problems](../09-partial-differential-equations/07-boundary-value-problems.md) —
  the partial differential equations these theorems serve.
- [18-01-02 Hadamard's Conditions: Existence, Uniqueness, Stability](../../18-inverse-problems/01-inverse-problem-foundations/02-hadamard-well-posedness.md) —
  why the direction of the theorem matters for inverse problems.

## Self-assessment checklist

- [ ] I can state all three theorems with their orientation conventions.
      (Section 2)
- [ ] I can explain the interior-face cancellation that makes the divergence
      theorem global. (Section 3.1)
- [ ] I can derive Green's theorem from Stokes' theorem. (Section 3.3)
- [ ] I can derive both of Green's identities from the divergence theorem.
      (Section 3.5)
- [ ] I can derive Gauss's law for gravity and say which theorem did the work.
      (Section 3.4)
- [ ] I can state Ampère's law and $\nabla\cdot\mathbf{B}=0$ in integral form and
      name the theorem used for each. (Section 3.7)
- [ ] I can explain why a singularity inside the region requires excision rather
      than invalidating the theorem. (Section 2.4)
- [ ] I can explain in one paragraph how the representation theorem leads to
      both well-posedness on a bounded domain and non-uniqueness of the
      geophysical inverse problem. (Section 3.6)
- [ ] I can name one numerical scheme that is a discretised divergence theorem
      and one that is a discretised Green's identity. (Section 4)
