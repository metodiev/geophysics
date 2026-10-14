---
id: 12-02-03
title: "Ab Initio Mineral Physics and Elastic Constants"
level: research
prereqs: ["12-02-01", "12-02-02", "02-04-06", "06-01-08"]
tags: [global-geophysics, earth-interior, ab-initio, elastic-tensor, anisotropy, christoffel, stability]
---

# Ab Initio Mineral Physics and Elastic Constants

> **All models and data in this module are SYNTHETIC.** The elastic-constant
> tensors, densities and texture fractions used here are chosen teaching values,
> picked to lie in the range of dense oxides and metals at high pressure. They are
> not computed results, not measurements, and no published tensor is reproduced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the elastic tensor in full and in Voigt form, and **explain** how crystal
   symmetry reduces 21 independent constants to 3 (cubic) or 5 (hexagonal).
2. **Compute** the Voigt, Reuss and Hill isotropic moduli of a single crystal from its
   tensor, and **state** when $K_V = K_R$ is an identity (cubic) and when it is not
   (a general hexagonal crystal).
3. **Solve** the Christoffel equation for a given direction, obtaining $v_p$, $v_{s1}$
   and $v_{s2}$, and **explain** why the polarisations are the eigenvectors.
4. **Quantify** the directional anisotropy of a crystal in two different ways (the
   extremal measure $AV_P$ and the axis-to-basal-plane difference) and **explain** why
   they differ.
5. **State** the Born stability criteria and **demonstrate** what a violation means
   physically.
6. **Compute** the aggregate anisotropy of a textured polycrystal and **explain** the
   product degeneracy between crystal anisotropy and alignment.
7. **Connect** a crystal's S anisotropy to a seismic splitting measurement, and
   **state** why a small observed splitting implies either very weak alignment or a
   different mechanism.

## Prerequisites

- [12-02-01 Mantle Composition and Peridotite Models](01-mantle-composition.md) —
  where an aggregate of crystals is built from isotropic phases.
- [12-02-02 High-Pressure Experiments and Diamond Anvil Cells](02-high-pressure-experiments.md) —
  the experimental route to the same constants.
- [02-04-06 Anisotropic Elasticity](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md) —
  the general theory of the stiffness tensor.
- [06-01-08 Anisotropic Propagation](../../06-seismology/01-elastic-wave-propagation/08-anisotropic-propagation.md) —
  how anisotropy appears in a seismogram.

## 1. The elastic tensor

Hooke's law in a general elastic solid is

$$\sigma_{ij} = C_{ijkl}\,\varepsilon_{kl},$$

with $C_{ijkl}$ a fourth-rank tensor. The symmetries
$C_{ijkl} = C_{jikl} = C_{ijlk} = C_{klij}$ reduce 81 components to **21 independent
constants** — the maximum for a crystal. Crystal symmetry reduces them further:

| symmetry | independent constants |
|---|---|
| isotropic | 2 ($K$, $G$) |
| cubic | 3 ($C_{11}$, $C_{12}$, $C_{44}$) |
| hexagonal (transverse isotropy) | 5 ($C_{11}$, $C_{12}$, $C_{13}$, $C_{33}$, $C_{44}$) |
| orthorhombic | 9 |
| monoclinic | 13 |
| triclinic | 21 |

The demonstration's SYNTHETIC tensors are

$$C^\text{cubic} = \begin{pmatrix}
294 & 93 & 93 & 0 & 0 & 0\\
93 & 294 & 93 & 0 & 0 & 0\\
93 & 93 & 294 & 0 & 0 & 0\\
0 & 0 & 0 & 155 & 0 & 0\\
0 & 0 & 0 & 0 & 155 & 0\\
0 & 0 & 0 & 0 & 0 & 155
\end{pmatrix}\ \mathrm{GPa},\quad \rho = 3.58\ \mathrm{g\,cm^{-3}},$$

$$C^\text{hex} = \begin{pmatrix}
280 & 160 & 140 & 0 & 0 & 0\\
160 & 280 & 140 & 0 & 0 & 0\\
140 & 140 & 300 & 0 & 0 & 0\\
0 & 0 & 0 & 110 & 0 & 0\\
0 & 0 & 0 & 0 & 110 & 0\\
0 & 0 & 0 & 0 & 0 & 60
\end{pmatrix}\ \mathrm{GPa},\quad \rho = 9.00\ \mathrm{g\,cm^{-3}},$$

where the hexagonal entry $C_{66} = (C_{11}-C_{12})/2 = 60$ GPa follows from the
symmetry rather than being independent, and the c-axis is along $[001]$.

**What an ab initio calculation delivers is exactly this matrix.** Every velocity,
anisotropy and splitting in the rest of the lesson is a *consequence* of it, obtained
by a deterministic calculation — which is why the validation steps below matter so
much: a wrong tensor produces plausible-looking numbers.

## 2. From the tensor to isotropic moduli

### 2.1 Voigt and Reuss for a single crystal

The Voigt averages use the stiffnesses directly:

$$K_V = \frac{C_{11}+C_{22}+C_{33}+2\left(C_{12}+C_{13}+C_{23}\right)}{9},$$
$$G_V = \frac{C_{11}+C_{22}+C_{33}-\left(C_{12}+C_{13}+C_{23}\right)
+ 3\left(C_{44}+C_{55}+C_{66}\right)}{15},$$

and the Reuss averages use the compliances $S = C^{-1}$:

$$K_R = \frac{1}{S_{11}+S_{22}+S_{33}+2\left(S_{12}+S_{13}+S_{23}\right)},$$
$$G_R = \frac{15}{4\left(S_{11}+S_{22}+S_{33}\right)
- 4\left(S_{12}+S_{13}+S_{23}\right)+3\left(S_{44}+S_{55}+S_{66}\right)} .$$

For the demonstration's tensors:

| crystal | $K_V$ | $K_R$ | $K_\text{Hill}$ | $G_V$ | $G_R$ | $G_\text{Hill}$ |
|---|---|---|---|---|---|---|
| cubic | 160.0 | 160.0 | 160.0 | 133.2 | 127.4 | 130.3 |
| hexagonal | 193.3 | 193.3 | 193.3 | 84.0 | 78.1 | 81.1 |

Two identities are visible, and they are not the same kind of statement:

- **$K_V = K_R$ for cubic symmetry is an identity**, because the bulk modulus of a cubic
  crystal is $K = (C_{11}+2C_{12})/3$ under hydrostatic strain whatever the averaging
  scheme — there is no hydrostatic-strain anisotropy left to bound.
- **$K_V = K_R$ for this hexagonal tensor is a coincidence.** For hexagonal (transverse
  isotropic) symmetry the two differ by
  $$K_V - K_R = \frac{2\left(C_{11}+C_{12}-C_{33}-C_{13}\right)^{2}}
  {9\left(C_{11}+C_{12}+2C_{33}-4C_{13}\right)},$$
  which vanishes **only** when $C_{11}+C_{12} = C_{33}+C_{13}$. The demonstration's
  tensor satisfies $280+160 = 300+140 = 440$ GPa by construction, and a second
  SYNTHETIC hexagonal tensor with $C_{11} = 290$, $C_{12} = 230$, $C_{13} = 110$,
  $C_{33} = 280$, $C_{44} = 95$ GPa gives $K_V = 195.5556$ against
  $K_R = 189.6875$ GPa — a 5.87 GPa spread. The demo prints both cases.
- The *shear* modulus, by contrast, has a genuine bracket **in every symmetry, cubic
  included**: 84.0 against 78.1 GPa here, a 7 % spread; and 133.2 against 127.4 GPa for
  the cubic crystal.

That asymmetry of behaviour — bulk modulus determined, shear modulus bracketed — is
the reason $v_s$ is a more sensitive probe of anisotropy and texture than $v_p$.

### 2.2 Isotropic-equivalent velocities

With the Hill averages:

| crystal | $v_p$ (km s$^{-1}$) | $v_s$ (km s$^{-1}$) | $v_p/v_s$ |
|---|---|---|---|
| cubic | 9.655 | 6.033 | 1.600 |
| hexagonal | 5.787 | 3.001 | 1.929 |

and the classical single-crystal anisotropy measures:

$$A = \frac{2C_{44}}{C_{11}-C_{12}} = \frac{2(155)}{294-93} = 1.542$$

for the cubic crystal ($A = 1$ means elastically isotropic), and
$C_{33}/C_{11} = 1.071$, $C_{44}/C_{11} = 0.393$ for the hexagonal one. These ratios
are *diagnostics*, not physical predictions: they say how far the crystal is from
isotropy, in the way a single number can.

## 3. Wave speeds in a crystal: the Christoffel equation

### 3.1 Derivation

Insert a plane wave $\mathbf{u} = \mathbf{a}\,e^{i(\mathbf{k}\cdot\mathbf{x} -
\omega t)}$ into the equation of motion
$\rho \ddot{u}_i = C_{ijkl}\,\partial_j\partial_l u_k$. The result is the
**Christoffel equation**

$$\rho v^{2} a_i = C_{ijkl}\,n_j n_l\, a_k
\qquad\Longrightarrow\qquad
\left[\mathbf{M} - \rho v^{2}\mathbf{I}\right]\mathbf{a} = 0,$$

with $\mathbf{n}$ the unit wave normal and

$$\boxed{\;M_{ik} = C_{ijkl}\,n_j n_l.\;}$$

The eigenvalues are $\rho v^{2}$ — three of them for each direction — and the
eigenvectors are the polarisations. Two consequences follow immediately:

- **Velocity depends on direction**, so a measurement along one axis does not
  determine another.
- **The three waves are not in general P and S.** They are a *quasi*-P and two
  *quasi*-S waves; only along symmetry directions are the polarisations purely
  longitudinal or transverse. Calling them "P" and "S" is a habit that is exactly
  right along the axes and approximately right elsewhere.

### 3.2 Computed speeds

For the two crystals, along four directions:

| direction | cubic $v_p$ | cubic $v_{s1}$ | cubic $v_{s2}$ | hex $v_p$ | hex $v_{s1}$ | hex $v_{s2}$ |
|---|---|---|---|---|---|---|
| [100] | 9.062 | 6.580 | 6.580 | 5.578 | 3.496 | 2.582 |
| [110] | 9.866 | 6.580 | 5.298 | 5.578 | 3.496 | 2.582 |
| [111] | 10.120 | 5.757 | 5.757 | 5.952 | 2.941 | 2.919 |
| [001] | 9.062 | 6.580 | 6.580 | 5.774 | 3.496 | 3.496 |

(all in km s$^{-1}$). Read the symmetry:

- **Cubic.** Along $[100]$ the shear splitting vanishes and equals along $[111]$; it
  is largest along $[110]$ (1.282 km s$^{-1}$). This is a *symmetry* statement: along
  $[100]$ the two shear polarisations are equivalent by the four-fold rotation.
- **Hexagonal.** The shear splitting vanishes along the c-axis $[001]$ and is largest
  in the basal plane (0.914 km s$^{-1}$). The P velocity is fastest along the c-axis
  in this tensor, so the crystal is "fast along the axis".

The S splitting matters because it is directly measurable with polarised shear waves:
a splitting time is a path length divided by the two velocities.

## 4. Quantifying the anisotropy — and the definition problem

Scanning the hexagonal crystal from the c-axis to the basal plane:

| angle from c-axis (deg) | $v_p$ (km s$^{-1}$) | fast $v_s$ | slow $v_s$ | splitting (s per 100 km) |
|---|---|---|---|---|
| 0 | 5.774 | 3.496 | 3.496 | 0.000 |
| 15 | 5.852 | 3.442 | 3.341 | 0.879 |
| 30 | 5.979 | 3.291 | 3.042 | 2.496 |
| 45 | 6.010 | 3.073 | 2.885 | 2.125 |
| 60 | 5.896 | 3.020 | 2.838 | 2.123 |
| 75 | 5.693 | 3.327 | 2.653 | 7.634 |
| 90 | 5.578 | 3.496 | 2.582 | 10.126 |

The splitting column is $100\,\mathrm{km}\times\left(1/v_\text{slow} -
1/v_\text{fast}\right)$, i.e. the delay per 100 km of propagation.

**Two definitions of "the anisotropy", both in use:**

$$AV_P = 200\,\frac{v_p^\text{max}-v_p^\text{min}}{v_p^\text{max}+v_p^\text{min}}
= 200\,\frac{6.010-5.578}{6.010+5.578} = 7.46\ \%$$

uses the *extremal* P velocities over all directions, whereas the frequently quoted
"fast along the axis" number is the axis-to-basal-plane difference,

$$200\,\frac{5.774-5.578}{5.774+5.578} = 3.45\ \%.$$

Both describe the same crystal. **The extremal measure is more than twice the axial
measure**, so an anisotropy quoted as a percentage is meaningless without the
definition. (The extremal direction here is at 45° to the c-axis, not along an axis —
which is itself a useful reminder that "anisotropy" is a property of the tensor, not
of a symmetry axis.)

## 5. Stability: the Born criteria

An elastic tensor is physical only if the strain-energy density
$W = \frac12 C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}$ is positive definite. The
resulting **Born stability criteria** for a cubic crystal are

$$C_{11} - C_{12} > 0,\qquad C_{11} + 2C_{12} > 0,\qquad C_{44} > 0,$$

and for a hexagonal crystal

$$C_{44} > 0,\qquad C_{11} > \left|C_{12}\right|,\qquad
\left(C_{11}+C_{12}\right)C_{33} > 2C_{13}^{2}.$$

The demonstration's tensors satisfy all of them (201, 480, 155 GPa for the cubic).
Now watch what a violation does. Setting $C_{44} < 0$:

| $C_{44}$ (GPa) | $\rho v^{2}$ along $[100]$ (GPa) | shear speed (km s$^{-1}$) |
|---|---|---|
| 155 | 155.00 | 6.580 |
| 50 | 50.00 | 3.737 |
| 1 | 1.00 | 0.529 |
| −1 | −1.00 | **imaginary: unstable** |
| −20 | −20.00 | **imaginary: unstable** |

A negative eigenvalue of the Christoffel matrix means **no real wave speed exists**:
the material would lower its energy by shearing, so it cannot exist at zero stress.
The velocity is not small, it is imaginary — a qualitative failure, not a
quantitative one.

Why this matters for ab initio work: a computed tensor that violates a Born criterion
usually indicates a calculation that has converged to the wrong structure, an
insufficient basis, or a phase that is only stable under pressure or temperature.
The criterion is one line of code and it catches errors that a plausible-looking
velocity table will not.

## 6. From crystal to aggregate: texture

A seismic wave never samples one crystal. It samples an aggregate, and the aggregate's
anisotropy depends on how the crystals are oriented. The demonstration models a
textured aggregate as a simple Voigt-style mixture of an aligned single crystal and an
isotropic aggregate of the same crystals:

$$C_\text{eff} = f\,C_\text{aligned} + \left(1-f\right)C_\text{isotropic},$$

with $C_\text{isotropic}$ built from the crystal's own Hill moduli. The resulting
P anisotropy between the c-axis and the basal plane:

| alignment $f$ | $v_p$ along c | $v_p$ in basal plane | $AV_P$ (%) |
|---|---|---|---|
| 0.00 | 5.787 | 5.787 | 0.00 |
| 0.10 | 5.786 | 5.766 | 0.33 |
| 0.25 | 5.784 | 5.735 | 0.84 |
| 0.50 | 5.780 | 5.683 | 1.69 |
| 0.75 | 5.777 | 5.631 | 2.56 |
| 1.00 | 5.774 | 5.578 | 3.45 |

**The aggregate anisotropy is the product of the crystal anisotropy and the degree of
alignment.** The consequence is a degeneracy with no way out from seismology alone:

- a measured 1 % aggregate anisotropy can mean a strongly anisotropic crystal with
  30 % alignment, or a weakly anisotropic crystal with 100 % alignment;
- the *observed* quantity is the product, so neither factor is determined by the
  seismic data;
- mineral physics supplies one factor (through experiments or computation), and the
  other is a statement about *deformation* — which is why anisotropy measurements are
  interpreted geodynamically (see
  [12-01-06](../01-seismic-structure-of-the-earth/06-outer-and-inner-core.md), where
  the same product structure appears in the inner core).

## 7. Assumptions and regime of validity

1. **Linear elasticity, small strain.** The tensor is the second derivative of the
   energy at a specific structure; at large strain (near a phase transition, or very
   deep) it changes and the whole calculation must be redone at the new conditions.
2. **Zero temperature, static lattice.** An ab initio tensor is computed at $T = 0$
   unless thermal effects are added; the temperature dependence of the constants is
   typically several per cent over mantle temperatures.
3. **Known structure and composition.** If the structure is wrong, everything
   downstream is wrong and still plausible. This is what the Born criteria catch
   sometimes, and only sometimes.
4. **Voigt-style texture averaging.** The demonstration's $C_\text{eff}$ is a simple
   mixing; real aggregates require an orientation-distribution function and a proper
   average (Voigt, Reuss, Hill, or a self-consistent scheme), which changes the
   numbers by a few per cent — comparable to the effect being measured.
5. **Single-phase aggregate.** No melt, no second phase, no exsolution.
6. **The isotropic reference matters.** $C_\text{isotropic}$ is built from the same
   crystal's Hill moduli; using Reuss or Voigt instead shifts the anisotropy by
   hundreds of a per cent, which matters at the 1 % level seismology usually reaches.
7. **The 21-constant limit.** Real minerals are often monoclinic or triclinic at high
   pressure, with 13 or 21 independent constants; assuming hexagonal symmetry when it
   does not hold biases both the magnitude and the orientation of the inferred
   anisotropy.

## 8. Worked examples

### Example 1 — the cubic bulk modulus, by hand and by two routes

$$K_V = \frac{C_{11}+C_{22}+C_{33}+2\left(C_{12}+C_{13}+C_{23}\right)}{9}
= \frac{3(294)+2(3)(93)}{9} = \frac{882+558}{9} = \frac{1440}{9} = 160.0\ \mathrm{GPa}.$$

The Reuss route needs the compliances, but the identity $K_V = K_R$ for cubic symmetry
means the answer is already known: $K_R = 160.0$ ✓ matching the demonstration. No such
identity holds in hexagonal symmetry in general — it holds only when
$C_{11}+C_{12} = C_{33}+C_{13}$, which the demonstration's hexagonal tensor happens to
satisfy ($K = 193.3$ GPa by either scheme) but the second tensor in section 2 does not
($195.56$ against $189.69$ GPa). **For a cubic tensor, $K_V = K_R$ is the cheapest
validation available for a tensor-processing code**: if $K_V \neq K_R$ there, the code
has a bug,
because the mathematics forbids it.

### Example 2 — the Christoffel equation along a symmetry axis

For a cubic crystal with $\mathbf{n} = [100]$,

$$M_{ik} = C_{i1k1} = \begin{pmatrix} C_{11} & 0 & 0\\ 0 & C_{44} & 0\\ 0 & 0 & C_{44}
\end{pmatrix} = \begin{pmatrix} 294 & 0 & 0\\ 0 & 155 & 0\\ 0 & 0 & 155
\end{pmatrix}\ \mathrm{GPa}.$$

The eigenvalues are read off:

$$\rho v_p^{2} = 294 \Rightarrow v_p = \sqrt{\frac{294}{3.58}}
= \sqrt{82.12} = 9.062\ \mathrm{km\,s^{-1}},$$
$$\rho v_s^{2} = 155 \Rightarrow v_s = \sqrt{\frac{155}{3.58}}
= \sqrt{43.30} = 6.580\ \mathrm{km\,s^{-1}},$$

both matching the printed table. The polarisations are the coordinate directions: the
longitudinal wave polarises along $[100]$, and the two transverse waves are degenerate
along $[010]$ and $[001]$ — which is why the splitting is exactly zero along an axis
of four-fold symmetry. **Doing this one direction by hand is the best way to be sure
an eigenvalue routine is returning what you think it is.**

### Example 3 — how much alignment does 1 % of anisotropy require?

From the texture table, the anisotropy grows almost linearly with $f$ at small
alignment: 0.33 % at $f = 0.10$ and 0.84 % at $f = 0.25$. Interpolating,

$$f(1\ \%) \approx 0.25 + 0.25 \times \frac{1.00 - 0.84}{1.69 - 0.84}
= 0.25 + 0.047 = 0.30.$$

So **1 % of aggregate P anisotropy requires about 30 % lattice alignment** of a
crystal whose own anisotropy is 3.45 % (axis-to-basal) or 7.46 % (extremal). Now do
the same for the *shear* splitting, which is the more sensitive measurement: the
single crystal splits shear waves by 10.126 s per 100 km at 90°, so a 30 % alignment
gives ~3.0 s per 100 km. For a path of 3000 km in the aggregate, the splitting would
be ~90 s — vastly larger than any observed inner-core splitting. **Conclusion:** for
the inner core, either the alignment is far weaker than 30 %, or the mechanism is not
simple lattice alignment of a strongly anisotropic phase. That is precisely why the
inner core's small S splitting alongside a few per cent P anisotropy is treated as a
constraint on the *mechanism*, not merely on the magnitude (lesson
[12-01-06](../01-seismic-structure-of-the-earth/06-outer-and-inner-core.md)).

### Example 4 — the sensitivity of a splitting measurement

The splitting time over a path of length $L$ through a medium with shear velocities
$v_1, v_2$ is

$$\delta t = L\left(\frac{1}{v_2} - \frac{1}{v_1}\right)
\approx \frac{L\,\Delta v_s}{v_s^{2}}.$$

For $L = 500$ km, $v_s = 3.0\ \mathrm{km\,s^{-1}}$ and $\Delta v_s/v_s = 0.5\ \%$
(i.e. $\Delta v_s = 0.015\ \mathrm{km\,s^{-1}}$):

$$\delta t = \frac{500 \times 0.015}{9.0} = 0.83\ \mathrm{s}.$$

So a 0.5 % shear anisotropy over a 500 km path gives a splitting of 0.83 s, comfortably
measurable. **Splitting is a long lever**: it is proportional to the path length, so
stations recording the same phase along different azimuths can map anisotropy without
any absolute velocity determination at all.

## 9. Python demonstration

`code/ab_initio_mineral_physics_demo.py` builds the cubic and hexagonal Voigt
matrices, expands them to full tensor form with an explicit index table, computes the
Voigt, Reuss and Hill moduli (with the cubic $K_V = K_R$ identity, and the hexagonal
counter-example, as internal checks),
solves the Christoffel equation along symmetry axes and as a function of angle,
quantifies the anisotropy by two different definitions, demonstrates the Born
stability criteria by violating one, and models a textured aggregate. It prints
labelled results with units and runs in about 0.1 s:

```bash
cd 12-global-geophysics-interior/02-composition-and-mineral-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ab_initio_mineral_physics_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/03-ab-initio-mineral-physics-exercises.md`](exercises/03-ab-initio-mineral-physics-exercises.md)
and
[`exercises/03-ab-initio-mineral-physics-solutions.md`](exercises/03-ab-initio-mineral-physics-solutions.md).

- **★** Compute $K_V$, $K_R$ and $G_V$ for a given tensor.
- **★★** Solve the Christoffel equation along $[110]$ and compare with an axis.
- **★★** Compute a splitting time and the alignment it implies.
- **★★★** Design a computation-to-seismology workflow for a candidate lower-mantle
  phase, stating every validation step.

## Mastery checkpoint

Without notes:

> A cubic crystal has $C_{11} = 250$, $C_{12} = 120$, $C_{44} = 100$ GPa and
> $\rho = 4.00\ \mathrm{g\,cm^{-3}}$.
> **(a)** Check the Born stability criteria.
> **(b)** Compute $K$, the Zener factor $A$, and the Hill shear modulus.
> **(c)** Compute $v_p$ and $v_s$ along $[100]$ from the Christoffel equation by hand.
> **(d)** Compute the splitting per 100 km along $[110]$, and state what an observed
> splitting of 2 s over a 400 km path would imply about the alignment.

A worked version appears in the lesson-03
[solutions](exercises/03-ab-initio-mineral-physics-solutions.md).

## Common pitfalls

1. **Quoting an anisotropy percentage without its definition.** Extremal (7.46 %) and
   axial (3.45 %) measures of the *same* crystal differ by a factor of 2.2.
2. **Forgetting the Voigt index mapping.** The tensor expansion needs an explicit
   table; the shortcut $\text{index} = 3 + (3-i-j)$ is wrong for the $(1,2)$ and
   $(0,1)$ pairs and produces plausible but incorrect tensors.
3. **Treating the three Christoffel solutions as P and S.** Away from symmetry
   directions they are quasi-P and quasi-S, and the polarisations are not pure.
4. **Skipping the Born check.** A violating tensor still fits a structure and still
   returns velocities; the failure shows up as an imaginary speed only if you look.
5. **Using $G_V$ instead of $G_R$ (or vice versa) without saying which.** For the
   hexagonal tensor the two differ by 7 %, more than most observational errors.
6. **Assuming hexagonal symmetry because it is convenient.** Real high-pressure
   phases are often monoclinic; assuming higher symmetry biases both the magnitude and
   the orientation of the anisotropy.
7. **Forgetting that anisotropy is a product.** Seismology measures (crystal
   anisotropy) × (alignment); reporting one without the other is an overclaim in
   either direction.

## Related modules

- [01 Mantle Composition and Peridotite Models](01-mantle-composition.md) — isotropic
  aggregates built from the same kinds of inputs.
- [02 High-Pressure Experiments and Diamond Anvil Cells](02-high-pressure-experiments.md) —
  the experimental measurement of the same constants.
- [04 Core Composition, Light Elements and the Geodynamo](04-core-composition.md) —
  where an anisotropic tensor of a core phase becomes an observable.
- [12-01-06 Outer Core, Inner Core Anisotropy and Rotation](../01-seismic-structure-of-the-earth/06-outer-and-inner-core.md) —
  the seismic side of the product this lesson decomposes.
- [06-01-08 Anisotropic Propagation](../../06-seismology/01-elastic-wave-propagation/08-anisotropic-propagation.md) —
  the general wave-propagation theory.
- [02-04-06 Anisotropic Elasticity](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md) —
  the continuum-mechanics foundation.

## Self-assessment checklist

- [ ] I can write a cubic and a hexagonal Voigt matrix and expand to tensor form.
- [ ] I can compute $K_V$, $K_R$, $G_V$, $G_R$ and state which symmetries give $K_V = K_R$.
- [ ] I can solve the Christoffel equation by hand along a symmetry axis.
- [ ] I can compute and compare the two anisotropy definitions.
- [ ] I can check Born stability and interpret a violation.
- [ ] I can compute an aggregate anisotropy from an alignment fraction, and invert.
- [ ] I can convert an S anisotropy into a splitting time for a stated path length.
- [ ] I can state the product degeneracy and what resolves it.
