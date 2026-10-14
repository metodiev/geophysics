---
id: 09-06-01
title: "Cross-Hole and Borehole-to-Surface Tomography"
level: doctoral
prereqs: ["09-02-04", "09-02-06", "09-02-07"]
tags: [electrical-methods, borehole, tomography, sensitivity-kernel, nonuniqueness]
---

# Cross-Hole and Borehole-to-Surface Tomography

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the whole-space Green's function $\phi = I\rho/(4\pi r)$ from charge
   conservation, and use it to **compute** the geometric factor of a cross-hole
   quadrupole and to check a forward model against a known resistivity.
2. **Derive** the adjoint (reciprocity) sensitivity kernel
   $\partial\phi_A(M)/\partial\sigma = -\nabla\phi_A\cdot\nabla\phi_M$, and
   **explain** why cross-hole sensitivity is a broad, sign-changing distribution
   rather than a ray.
3. **Verify** a kernel numerically against the exact response to a uniform
   perturbation, and **state** precisely what that check proves and what it
   leaves untested.
4. **Build** the tomographic Jacobian of a bipole-bipole survey, **compute** its
   singular spectrum, and **read** a resolution matrix rather than an image.
5. **Quantify** how resolution grows towards the electrodes and decays between
   them, and **explain** why a cross-hole survey illuminates a body rather than a
   block model.
6. **Construct** a second model that fits the data as well as the inversion
   result while sitting measurably further from the truth, and **report** it as
   the uncertainty of the answer.
7. **State** the assumptions of the method — whole space, isotropic conduction,
   no steel casing, first-order perturbation — and the regime in which each
   fails.

## Prerequisites

- [09-02-04 Vertical Electrical Sounding vs Profiling](../02-dc-resistivity/04-sounding-profiling.md) —
  what a sounding measures and what a profile measures.
- [09-02-06 Forward Modelling Resistivity Data](../02-dc-resistivity/06-resistivity-forward-modelling.md) —
  apparent resistivity, geometric factors, numerical forward modelling.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](../02-dc-resistivity/07-resistivity-inversion.md) —
  regularisation and the language of the resolution matrix.
- [05-08-01 The Borehole Environment](../../05-core-geophysics/08-geophysical-logging/01-borehole-environment.md) —
  what a borehole does to the medium around it.

## 1. Intuition: what a cross-hole survey adds

A surface resistivity survey puts current into the ground and measures a
potential difference on the same surface. Its resolution falls off with depth
because the sensitivity is concentrated near the electrodes, and it cannot see
*through* anything: a conductive layer spreads the current and hides what lies
beneath it.

A cross-hole survey places the electrodes in two or more boreholes. Current
enters in one hole and the potential difference is measured in another, so the
current path is forced through the material *between* the holes. One borehole
gives a one-dimensional log; two boreholes give a two-dimensional image of the
plane between them, which is what the word **tomography** (a slice) means here.

The method's promise and its central difficulty are both visible in a single
number. Between two holes 20 m apart, an array with a metre of electrode
separation is sensitive to a whole *volume*, not to a point; the sensitivity has
positive and negative parts; and a large fraction of it lies near the electrodes,
where nobody cares about the answer. This lesson derives that sensitivity,
measures it, and then uses it to explain why a cross-hole tomogram is a
statement about a body of rock, not a picture of a structure.

All models and data in this module are **SYNTHETIC**. The well pair, the
electrode depths and the conductivity anomaly used below are chosen teaching
values, not measurements from a site.

## 2. The forward problem in a whole space

### 2.1 The Green's function

Let a current $I$ be injected at a point in a homogeneous, isotropic medium of
conductivity $\sigma$. Steady current conservation gives

$$\nabla\cdot\mathbf{J} = I\,\delta(\mathbf{r}-\mathbf{r}_A),
\qquad \mathbf{J} = -\sigma\nabla\phi .$$

By spherical symmetry $\phi = \phi(r)$ and the flux through a sphere of radius
$r$ is $4\pi r^{2}\,\sigma\,(-\mathrm{d}\phi/\mathrm{d}r) = I$, so

$$\frac{\mathrm{d}\phi}{\mathrm{d}r} = -\frac{I}{4\pi\sigma r^{2}}
\quad\Longrightarrow\quad
\boxed{\;\phi(r) = \frac{I}{4\pi\sigma r} = \frac{I\rho}{4\pi r}\;}
\qquad [\mathrm{V}],$$

with $\rho = 1/\sigma$ in $\Omega\,\mathrm{m}$ and $r$ in metres. This is the
whole-space Green's function. It is the right model for a survey deep enough
that the ground surface is far compared with the hole separation, and it is the
model used throughout this lesson. (Compare the half-space result of module
09-02, where the same construction gives $I\rho/(2\pi r)$: the factor of two is
the image of the source in the surface.)

### 2.2 A four-electrode measurement

Four electrodes: current $+I$ at $A$, $-I$ at $B$, potential measured between
$M$ and $N$. Superposition gives the transfer resistance

$$\frac{\Delta V}{I} = \frac{\rho}{4\pi}
\left[\frac{1}{r_{AM}} - \frac{1}{r_{BM}} - \frac{1}{r_{AN}} + \frac{1}{r_{BN}}\right]
\qquad [\Omega].$$

Define the **geometric factor**

$$K = \frac{4\pi}{\dfrac{1}{r_{AM}} - \dfrac{1}{r_{BM}}
- \dfrac{1}{r_{AN}} + \dfrac{1}{r_{BN}}}
\qquad [\mathrm{m}],$$

so that in a homogeneous medium the apparent resistivity is exactly the true
resistivity:

$$\rho_a \equiv K\,\frac{\Delta V}{I} = \rho .$$

The prefactor is easy to get wrong by $4\pi$; the check is always the same, that
$K$ times the measured transfer resistance returns the model resistivity. The
demonstration prints that check.

### 2.3 Worked example: the numbers of the demonstration

Boreholes at $x=0$ and $x=20\ \mathrm{m}$; a source bipole in the first hole
between $z=10$ and $z=12\ \mathrm{m}$ (so $A=(0,0,10)$, $B=(0,0,12)$); a receiver
bipole in the second between $z=9$ and $z=11\ \mathrm{m}$ ($M=(20,0,9)$,
$N=(20,0,11)$). Model: $\rho_0 = 20.000\ \Omega\,\mathrm{m}$
($\sigma_0 = 0.050\ \mathrm{S\,m^{-1}}$).

The four distances and their reciprocals:

| pair | separation | $1/r$ (m$^{-1}$) |
|---|---|---|
| $A\!-\!M$ | $\sqrt{20^{2}+1^{2}}=\sqrt{401}=20.024984$ | $0.04993752$ |
| $B\!-\!M$ | $\sqrt{20^{2}+3^{2}}=\sqrt{409}=20.223748$ | $0.04944682$ |
| $A\!-\!N$ | $\sqrt{20^{2}+1^{2}}=\sqrt{401}=20.024984$ | $0.04993752$ |
| $B\!-\!N$ | $\sqrt{20^{2}+1^{2}}=\sqrt{401}=20.024984$ | $0.04993752$ |

The bracket is $0.04993752-0.04944682-0.04993752+0.04993752
= 4.9070\times10^{-4}\ \mathrm{m^{-1}}$, so

$$K = \frac{4\pi}{4.9070\times10^{-4}} = 25603.89\ \mathrm{m},$$

$$\frac{\Delta V}{I} = \frac{20.000 \times 4.9070\times10^{-4}}{4\pi}
= 7.8113\times10^{-4}\ \Omega,
\qquad
\rho_a = 25603.89 \times 7.8113\times10^{-4} = 20.000\ \Omega\,\mathrm{m}.$$

The forward model returns the model resistivity exactly. Every later statement in
this lesson is built on a forward model that has passed this check.

## 3. The sensitivity kernel

### 3.1 Derivation by the adjoint identity

How much does the measured potential change if the conductivity changes by
$\delta\sigma(\mathbf{r})$ somewhere? Let the source be at $A$ with $I=1$ and the
receiver at $M$; write $\phi_X(P) = 1/(4\pi\sigma_0|\mathbf{P}-\mathbf{X}|)$ for
the field of a unit point source.

Perturbing $\nabla\cdot(\sigma\nabla\phi) = -\delta_A$ gives, to first order,
$\nabla\cdot(\sigma_0\nabla\delta\phi) = -\nabla\cdot(\delta\sigma\nabla\phi_A)$.
Multiply by $G_M = \phi_M$ (the Green's function of the receiver), integrate over
the volume, and use Green's second identity with the operator $\nabla\cdot(\sigma\nabla\,\cdot)$;
the surface term vanishes because both fields decay. Then

$$\delta\phi_A(M) = -\int_V \delta\sigma(\mathbf{r})\,
\nabla\phi_A(\mathbf{r})\cdot\nabla G_M(\mathbf{r})\,\mathrm{d}V .$$

With $\nabla\phi_A = -\mathbf{u}_A/(4\pi\sigma_0 r_A^{2})$ and
$\nabla G_M = -\mathbf{u}_M/(4\pi\sigma_0 r_M^{2})$, where $\mathbf{u}_A$ is the
unit vector from $A$ to $\mathbf{r}$, the kernel of a point-pair (pole-pole)
measurement is

$$\boxed{\;J_{A\to M}(\mathbf{r}) \equiv
\frac{\partial\phi_A(M)}{\partial\sigma(\mathbf{r})}
= -\,\frac{\mathbf{u}_A\cdot\mathbf{u}_M}
{16\pi^{2}\sigma_0^{2}\,r_A^{2}\,r_M^{2}}\;}
\qquad [\Omega^{2}\,\mathrm{m^{-2}}].$$

For a four-electrode measurement the four contributions combine with the signs of
the two bipoles:

$$J = J_{A\to M} - J_{B\to M} - J_{A\to N} + J_{B\to N}.$$

### 3.2 What the kernel looks like

The demonstration evaluates $J$ for the quadrupole of §2.3 on the plane between
the holes. Three features matter, and all three contradict a ray picture:

- **It is broad.** On the line $z = 10.5\ \mathrm{m}$ the kernel takes the values
  $+4.59\times10^{-6}$, $+5.88\times10^{-6}$, $-9.39\times10^{-6}$,
  $+3.19\times10^{-6}$, $+5.73\times10^{-6}\ \Omega^{2}\mathrm{m^{-2}}$ at
  $x = 2.5, 6, 10, 14, 17.5\ \mathrm{m}$. A ray model would place all the
  sensitivity on one line and zero elsewhere.
- **It changes sign.** $29.4\%$ of the sampled plane has $J<0$. A negative
  sensitivity means that *adding* conductivity in that region *lowers* the
  measured potential difference. No weighting scheme can represent this as a
  ray.
- **It grows towards the electrodes.** The largest values on the plane sit within
  a couple of metres of the bipoles, because $J$ diverges as $1/r^{2}$ as
  $r\to 0$ at a current electrode (the volume integral still converges). This is
  why the near-electrode region dominates a cross-hole survey and why real
  surveys either parameterise it coarsely, exclude it, or accept it as a
  systematic error.

The word *banana* is often used for the doubly-curved high-sensitivity region of
a cross-hole pair of dipoles. It is a useful shape mnemonic, but the measured
kernel of a four-electrode measurement is not a thin curved ribbon: it is a
diffuse, two-lobed distribution whose sign structure is as important as its
magnitude.

### 3.3 Dimensional check

$\phi$ is measured in volts and has units $\Omega$ per unit current; $\sigma$ has
units $\mathrm{S\,m^{-1}} = \Omega^{-1}\mathrm{m^{-1}}$; so
$\partial\phi/\partial\sigma$ per unit volume has units
$\Omega^{2}\mathrm{m^{-2}}$, and multiplying by a cell volume gives
$\Omega^{2}\mathrm{m}$. Multiplying by a conductivity perturbation in
$\mathrm{S\,m^{-1}}$ gives $\Omega$, which is the unit of the data. If a kernel
comes out with any other unit, a factor of $r$ or $\sigma$ has been misplaced.

## 4. Verification: the normalisation identity

A kernel is only useful if it is correctly normalised, and there is an identity
that tests exactly that. Take a spatially **uniform** perturbation
$\delta\sigma$; the exact response follows from $\phi = I/(4\pi\sigma r)$:

$$\frac{\partial\phi_A(M)}{\partial\sigma}\bigg|_{\text{uniform}}
= -\frac{1}{4\pi\sigma_0^{2}\,r_{AM}} .$$

The kernel must reproduce this when integrated over all space:

$$\int_V J_{A\to M}(\mathbf{r})\,\mathrm{d}V
= -\int_V \frac{\mathbf{u}_A\cdot\mathbf{u}_M}
{16\pi^{2}\sigma_0^{2}r_A^{2}r_M^{2}}\,\mathrm{d}V
= -\frac{1}{4\pi\sigma_0^{2}r_{AM}} .$$

The demonstration evaluates the integral numerically for
$r_{AM} = 6.0\ \mathrm{m}$, $\sigma_0 = 0.050\ \mathrm{S\,m^{-1}}$ and finds

$$\int_V \frac{\mathbf{u}_A\cdot\mathbf{u}_M}{r_A^{2}r_M^{2}}\,\mathrm{d}V
= 2.094787\ \mathrm{m^{-1}}
\quad\text{against}\quad
\frac{4\pi}{r_{AM}} = 2.094395\ \mathrm{m^{-1}},$$

an agreement of $0.0187\%$ (the residual is the quadrature error of the radial
tail). The integrated kernel is $-5.3062\ \Omega^{2}\mathrm{m}$ against the exact
$-5.3052\ \Omega^{2}\mathrm{m}$.

**What this proves.** That the prefactor, the signs and the $1/r^{2}$ decay of
the kernel are right: a uniform perturbation is the one case where the true
answer is known in closed form, and the kernel reproduces it.

**What it does not prove.** That a *localised* perturbation is handled correctly.
The identity is a single scalar condition; a kernel with the same integral and
the wrong spatial shape would pass it. Local accuracy is what the discretised
Jacobian is checked against in practice, by inverting synthetic data from a
forward model that does not use the kernel at all — here, by the exact
whole-space formula and by the ray-based check of module 09-06-02.

## 5. The tomographic system

### 5.1 Discretisation

Parameterise the inter-hole volume as $N$ cells. The linearised problem is

$$\mathbf{d} = \mathbf{J}\,\mathbf{m}, \qquad
d_i = \frac{\Delta V_i}{I} - \left(\frac{\Delta V_i}{I}\right)_0,
\qquad m_j = \frac{\delta\sigma_j}{\sigma_0},$$

where $\mathbf{m}$ is dimensionless and $J_{ij} = \sigma_0\int_{\text{cell }j}
J_i\,\mathrm{d}V$ has the units of the data, $\Omega$.

The demonstration uses $4\times6 = 24$ cells spanning $x\in[2,18]$ m,
$z\in[2,18]$ m, one cell thick in $y$ with half-width 8 m, and 36 quadrupoles
(six source bipole depths × six receiver bipole depths). The regions within 2 m
of each hole are **not** parameterised: that choice is part of the model, and it
is a real source of model error, not a technicality.

### 5.2 Spectrum, resolution and damping

With a $+50\%$ conductivity anomaly injected into a $2\times3$ block and Gaussian
noise of $\sigma_d = 3.99\times10^{-7}\ \Omega$ ($0.5\%$ of the largest datum),
the Jacobian has singular values from $5.93\times10^{-4}$ down to
$1.96\times10^{-7}\ \Omega$ — a condition number of $3.0\times10^{3}$ — and a
numerical rank of 24 of 24. Tikhonov damping with
$\alpha = (0.1\,s_{\max})^{2}$ gives a relative data misfit of $4.94\%$ and the
following recoveries (a selection of the 24 cells):

| cell | $x$ (m) | $z$ (m) | true $m$ | estimate | resolution diagonal |
|---|---|---|---|---|---|
| 0 | 4.00 | 3.33 | 0.00 | $+0.077$ | 0.787 |
| 1 | 4.00 | 6.00 | 0.00 | $+0.213$ | 0.761 |
| 7 | 8.00 | 6.00 | $+0.50$ | $+0.152$ | 0.168 |
| 8 | 8.00 | 8.67 | $+0.50$ | $+0.268$ | 0.186 |
| 11 | 8.00 | 16.67 | 0.00 | $-0.067$ | 0.142 |
| 18 | 16.00 | 3.33 | 0.00 | $+0.077$ | 0.787 |

Three honest statements follow, and each of them is a *measurement* from the
demonstration rather than a caveat:

1. **The peak amplitude is recovered at about half its true value** ($0.268$
   against $0.50$). Damping buys stability by shrinking the model; the misfit is
   therefore not zero even though the true model lies inside the
   parameterisation.
2. **Resolution is not uniform.** The resolution diagonal is $0.12$ in the cells
   midway between the holes and $0.79$ beside the electrodes — a factor of 6.6.
   Cells that are far from every electrode are smeared.
3. **The model standard errors mirror that.** From the linearised covariance the
   smallest standard error is $0.086$ (upper corners beside the electrodes) and
   the largest is $1.145$, a factor of 13.3, in cells that no electrode
   approaches.

### 5.3 Coverage

Counting, per cell, the number of quadrupoles with above-threshold sensitivity to
that cell gives $13$ of 36 for the shallow corner cells and $31$ of 36 for the
central cells. Coverage is a *count*, not a resolution: a cell crossed by many
quadrupoles can still be poorly resolved if all the paths through it are
parallel (module 09-06-02 makes this explicit for ray tomography).

## 6. Borehole-to-surface geometry

A **borehole-to-surface** survey puts one electrode set in a hole and the rest on
the surface. Its sensitivity is asymmetric: it resolves the region around the
borehole well, and it degrades towards the surface where the current spreads
laterally. The practical consequence is that a borehole-to-surface data set *adds
constraints* to a cross-hole data set rather than replacing it: the cross-hole
paths run nearly along one direction in the vertical plane, and the surface paths
run across it, so the two together fill in the null space that neither fills
alone. The same argument is made quantitatively for ray tomography in
[09-06-02 Borehole Radar and Directional Probing](02-borehole-radar.md), where
adding oblique rays is shown to raise the rank of the system and cut the model
error.

## 7. Equivalence: a second model that fits equally well

The inversion returns *one* model. The honest question is what other models fit
the data equally well. Take the right-singular vector $\mathbf{v}$ of
$\mathbf{J}$ with the smallest singular value ($1.97\times10^{-7}\ \Omega$),
which is a direction in model space that the data barely detect, and add a
multiple of it to the estimate:

$$\mathbf{m}_{\text{alt}} = \mathbf{m}_{\text{est}} + t\,\mathbf{v},
\qquad t \text{ chosen so that } \|\mathbf{J}(\mathbf{m}_{\text{alt}}-\mathbf{m}_{\text{est}})\|
\approx \sigma_d .$$

The demonstration finds

$$\|\mathbf{d}-\mathbf{J}\mathbf{m}_{\text{est}}\| = 1.5320\times10^{-5}\ \Omega,
\qquad
\|\mathbf{d}-\mathbf{J}\mathbf{m}_{\text{alt}}\| = 1.5341\times10^{-5}\ \Omega,$$

a ratio of $1.0014$: the two models are indistinguishable in the data. Their
difference is $\|\mathbf{m}_{\text{alt}}-\mathbf{m}_{\text{est}}\| = 7.04$
(dimensionless), and $\mathbf{m}_{\text{alt}}$ is $7.8\times$ further from the
true model than $\mathbf{m}_{\text{est}}$ is. **The data cannot choose between
them.** Any statement of the form "the inversion found $X$" therefore has to be
accompanied by the set of models that fit, or it is a statement about the
regularisation rather than about the Earth.

## 8. Assumptions and regime of validity

1. **Whole space.** The surface is ignored, so this model applies to a survey
   deep relative to the hole separation, or to a borehole below a conducting
   overburden. Near the surface the factor $1/(4\pi r)$ becomes $1/(2\pi r)$ and
   the image series of module 09-02 applies.
2. **Isotropic, frequency-independent conduction.** Induction and
   polarisation are neglected: the model is the DC limit. At the frequencies
   where IP or EM coupling appears, the transfer resistance acquires a
   quadrature component (module 09-03) and this model no longer describes it.
3. **No steel casing.** A steel-cased hole is a conductor of enormous
   conductivity contrast; its effect is not a perturbation and cannot be treated
   by the kernel above.
4. **First-order (Born) linearisation.** $\delta\sigma$ must be small enough that
   the perturbed field does not significantly change the sensitivity. The
   demonstration uses $\pm50\%$, which is *not* small; the linearised Jacobian is
   a working approximation there, and the equivalence demonstration inherits its
   error. A full non-linear inversion re-computes the Jacobian at the current
   model.
5. **Known electrode positions.** A 0.3 m error in electrode depth at 20 m offset
   behaves like a small model change; in a deep hole, depth control is often the
   largest single error term.
6. **Known background conductivity.** The Jacobian is built at $\sigma_0$; using
   the wrong background biases the anomaly amplitudes and, through them, the
   apparent geometry.

## 9. Further worked examples

### Example 1 — a uniform perturbation, by hand

A cross-hole survey in a medium of $\sigma_0 = 0.050\ \mathrm{S\,m^{-1}}$ is
repeated after the conductivity is raised everywhere by $1\%$. What fraction of
the transfer resistance changes, for the quadrupole of §2.3?

Uniform response: $(\Delta V/I) = \rho_{\text{bracket}}/(4\pi)$, so a $1\%$
change in $\sigma$ is a $-1\%$ change in $\rho$ and therefore a $-1\%$ change in
$\Delta V/I$: $-7.81\times10^{-6}\ \Omega$. The kernel integral confirms this
independently, since it reproduces exactly this uniform-response derivative
(§4). Note that the answer is *not* the same as $1\%$ of the anomalous response
of a local anomaly: the two are related only through the kernel.

### Example 2 — the anomaly amplitude of a block

If a $2\times3$-cell block has its conductivity raised by $50\%$, how large is the
largest change in a datum? The demonstration prints
$\max|\mathbf{d}| = 7.98\times10^{-5}\ \Omega$ against a transfer resistance of
$\sim 8\times10^{-4}\ \Omega$: about $10\%$ of the background datum. The
signal-to-noise ratio per datum is then $200$ at $0.5\%$ noise, which looks
comfortable — and the model error is still $7.8\times$ the anomaly for a
non-unique alternative. **A high signal-to-noise ratio is not a guarantee of
model resolution**; it guarantees only that the data were measured well.

### Example 3 — why the near-electrode cells dominate

Take the pole-pole kernel
$J = -\mathbf{u}_A\cdot\mathbf{u}_M/(16\pi^{2}\sigma_0^{2}r_A^{2}r_M^{2})$ with
$\mathbf{u}_A\cdot\mathbf{u}_M\approx-1$ (a perturbation between the two
electrodes), $\sigma_0 = 0.05\ \mathrm{S\,m^{-1}}$, $r_A = 0.5\ \mathrm{m}$
and $r_M = 20\ \mathrm{m}$:

$$|J| = \frac{1}{16\pi^{2}\times0.0025\times0.25\times400}
= \frac{1}{39.478} = 2.53\times10^{-2}\ \Omega^{2}\mathrm{m^{-2}} .$$

The four-electrode kernel at the mid-plane is
$9.39\times10^{-6}\ \Omega^{2}\mathrm{m^{-2}}$ (measured, §3.2) — some
$2700$ times smaller, because the four terms of the quadrupole cancel heavily
away from the electrodes. Both numbers are real sensitivity; the difference is
what makes the near-electrode zone the hardest part of the model to state
honestly.

## 10. Python demonstration

[`code/cross_hole_tomography_demo.py`](./code/cross_hole_tomography_demo.py)
runs the whole calculation and prints labelled results with units:

1. the whole-space Green's function, the geometric factor, and the forward check
   that $K(\Delta V/I)$ returns $\rho_0 = 20.000\ \Omega\,\mathrm{m}$;
2. the four-electrode kernel on the plane, its sign structure and the fraction of
   the plane that is negative;
3. the normalisation identity of §4, verified to $0.02\%$;
4. the Jacobian, its singular spectrum, condition number and resolution
   diagonal, with the recovered anomaly per cell;
5. the equivalence demonstration of §7;
6. the per-cell coverage counts and the linearised model standard errors.

Run it with

```bash
cd 09-electrical-em-methods/06-borehole-electrical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_hole_tomography_demo.py
```

It takes about a fifth of a second, requires no network, uses a fixed seed
(`np.random.default_rng(20261014)`) and exits 0.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-cross-hole-tomography-exercises.md`](./exercises/01-cross-hole-tomography-exercises.md)
and
[`exercises/01-cross-hole-tomography-solutions.md`](./exercises/01-cross-hole-tomography-solutions.md).

- **★** Compute the geometric factor and the transfer resistance for a
  cross-hole quadrupole at your own electrode depths, and check the forward
  model.
- **★★** Compute the pole-pole kernel at three points and identify where the
  sign changes; explain the sign physically.
- **★★** Given the singular spectrum of the demonstration, estimate how many
  independent model numbers the survey measures and justify the number.
- **★★★** Design a survey (electrode depths, number of quadrupoles) whose
  Jacobian has a specified condition number, and defend the design in terms of
  the resolution you need rather than the noise you can tolerate.

## 12. Common mistakes

1. **Reading a tomogram as a picture.** The image is $\mathbf{J}^{+}\mathbf{d}$
   with a chosen damping, not the Earth.
2. **Reporting a single model.** Print the admissible set, or report the
   resolution matrix beside the image.
3. **Ignoring the near-electrode volume.** It carries most of the sensitivity and
   is usually outside the parameterisation.
4. **Calling the sensitivity a ray.** It is broad, signed and diffuse; ray
   language is for the radar-frequency limit of module 09-06-02, not for DC.
5. **A misplaced $4\pi$.** Always check $K(\Delta V/I)=\rho$ in a homogeneous
   medium.

## Mastery checkpoint

Complete this without notes.

> A cross-hole survey uses two holes 15 m apart in a whole space of
> $\sigma_0 = 0.020\ \mathrm{S\,m^{-1}}$. **(a)** Write down the Green's function
> and compute the geometric factor of the quadrupole
> $A=(0,0,5)$, $B=(0,0,7)$, $M=(15,0,5)$, $N=(15,0,7)$ (all in metres).
> **(b)** Compute the transfer resistance and confirm that $\rho_a$ equals
> $1/\sigma_0$. **(c)** Write the pole-pole sensitivity kernel and state its
> units, and say where on the plane a positive perturbation *reduces* the
> measured potential difference. **(d)** State the normalisation identity that a
> correct kernel must satisfy and explain what it does not test. **(e)** Your
> inversion reports a $+40\%$ conductivity body between the holes. Give two
> reasons why the amplitude may be wrong, and name the quantity you would report
> alongside it.

A worked version of (a)–(c) appears in the lesson-01
[solutions](./exercises/01-cross-hole-tomography-solutions.md).

## Common pitfalls

1. **Confusing sensitivity with resolution.** Sensitivity says the data depend
   on a cell; resolution says they can separate it from its neighbours.
2. **Trusting the misfit.** A damped inversion of a model inside the
   parameterisation still leaves a residual, and it is not all noise.
3. **Forgetting the linearisation.** At $\pm50\%$ conductivity changes the
   kernel itself moves; the Born approximation is a convenience, not a
   property.
4. **Assuming uniform resolution across the image.** It varies by a factor of
   $6.6$ in the demonstration, and worse in a real survey.
5. **Treating the null space as a technicality.** A second model of the same
   data amplitude, $7.8\times$ further from the truth, exists in this
   demonstration's own numbers.

## Related modules

- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) — the
  surface-geometry parent of this method.
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — what the
  quadrature component of the same measurement contains.
- [09-06-02 Borehole Radar and Directional Probing](02-borehole-radar.md) — the
  wave-regime counterpart, and ray tomography with its own null space.
- [05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md) —
  what a single hole can say without tomography.
