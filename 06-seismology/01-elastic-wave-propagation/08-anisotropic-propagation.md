---
id: 06-01-08
title: "Wave Propagation in Anisotropic Media"
level: doctoral
prereqs: ["06-01-01", "06-01-02", "06-01-04"]
tags: [seismology, anisotropy, christoffel, thomsen, shear-wave-splitting, vti]
---

# Wave Propagation in Anisotropic Media

Every derivation so far has assumed that a rock's elastic response depends only
on how much it is strained, not on the direction in which it is strained. That
assumption is called isotropy, and it is false for most rocks that matter: shales
are layered, crystalline rocks carry lattice-preferred orientation, and any
rock with a systematic set of aligned cracks or fractures is directional. When
the assumption fails, the two comfortable statements of this module — "the S
wave travels at $v_s$" and "the P polarisation follows the ray" — both stop being
true.

This lesson builds the machinery that replaces them: the **Christoffel
equation**, whose three eigenvalues are the speeds of the three body-wave
branches in any direction, and whose eigenvectors are their polarisations. The
symmetry treated in detail is **transverse isotropy** (TI) — the symmetry of a
layered or crack-aligned medium — because it is both the most common in the
Earth and the only one with a compact parameterisation, the **Thomsen
parameters** $\varepsilon$, $\delta$, $\gamma$.

The honest difficulty of the lesson is the following. In an anisotropic medium
the quantity a seismologist measures is a travel time (a *group* property),
while the quantity theory naturally predicts is a *phase* speed. The two differ,
the difference is direction-dependent, and it is not small: in the demonstration
below the ray direction deviates from the phase direction by up to about
$10^\circ$. Every inversion for anisotropy has to choose how to handle that, and
saying which choice was made is part of the measurement.

All models and data in this module are **SYNTHETIC**. The stiffness tensor below
is built from stated Thomsen parameters chosen for teaching, not measured from
any rock or region, and every number quoted is printed by
`code/anisotropic_propagation_demo.py` or is an exact constant with units.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Christoffel equation from the elastodynamic equation and a
   plane-wave ansatz, and **state** what its eigenvalues and eigenvectors mean.
2. **Construct** a VTI stiffness tensor from $(\alpha_0,\beta_0,\rho,
   \varepsilon,\delta,\gamma)$ and **verify** the reconstruction of $\delta$ from
   the tensor.
3. **Derive** the exact SH speed in a VTI medium, and the axis values
   $\alpha_0$, $\alpha_0\sqrt{1+2\varepsilon}$, $\beta_0$, $\beta_0\sqrt{1+2\gamma}$.
4. **Compute** the Thomsen weak-anisotropy approximations and **quantify** their
   error against the exact solution at a stated anisotropy strength.
5. **Explain** why the polarisation of qP and qSV is not parallel or
   perpendicular to the propagation direction, while qSH remains exactly
   horizontal in a VTI medium.
6. **Distinguish** phase velocity from group velocity, **derive** the relation
   between them, and **measure** the ray–phase angle split.
7. **Explain** why a shear-wave splitting measurement is a statement about
   direction as much as about magnitude, and **state** the symmetry assumptions
   it requires.

## Prerequisites

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic Equation](01-wave-equation-elastic.md) —
  the equation being solved, and the elastic tensor it contains.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](02-p-and-s-waves.md) —
  the isotropic limits this lesson must reproduce exactly.
- [06-01-04 Reflected, Refracted and Converted Body Waves](04-body-wave-arrivals.md) —
  mode conversion and the boundary conditions where anisotropy is most easily
  mistaken for structure.

## 1. Intuition: a directional spring

Replace the isotropic spring of [01](01-wave-equation-elastic.md) — one stiffness
for compression, one for shear — by a spring that is stiffer along the bedding
normal than along the bedding. Physically this is what layering does: a stack of
thin stiff and soft layers is, in the long-wavelength limit, a homogeneous
medium with a *different* stiffness for compression along the stack from
compression across it. Aligned cracks do the same thing: a rock full of
vertical, parallel cracks is soft for horizontal shear across the cracks and
stiff along them.

Three observable consequences follow immediately and are the working content of
this lesson:

- a P wave's speed depends on the angle between the ray and the symmetry axis;
- the two S waves travel at *different* speeds in almost every direction
  (**shear-wave splitting**);
- a wave's polarisation is no longer exactly parallel (P) or perpendicular (S)
  to its direction of travel, so "P" and "S" become quasi-P and quasi-S.

The last point is the one that breaks naive processing codes, and it has no
counterpart in the isotropic theory of lessons 01–05.

## 2. Precise definitions

**Stiffness tensor.** $C_{ijkl}$ with the symmetries
$C_{ijkl} = C_{jikl} = C_{ijlk} = C_{klij}$, so that at most 21 independent
constants survive. $[\mathbf{C}] = \mathrm{Pa}$.

**Voigt notation.** Pairs of indices are collapsed: $11\to1$, $22\to2$, $33\to3$,
$23\to4$, $13\to5$, $12\to6$. Then $C_{ijkl} \to C_{mn}$ with
$m,n \in \{1,\dots,6\}$, a $6\times6$ symmetric matrix.

**VTI (transversely isotropic with a vertical symmetry axis).** The symmetry of
horizontal layering: properties are the same for every azimuth and vary only
with the angle from the vertical. Five independent constants.

**HTI.** The same medium with a *horizontal* symmetry axis — the symmetry of a
set of aligned vertical cracks. It is a VTI medium seen from the side (§9).

**Thomsen parameters.** Dimensionless combinations that vanish for an isotropic
medium:

$$\varepsilon = \frac{C_{11}-C_{33}}{2C_{33}},\qquad
\gamma = \frac{C_{66}-C_{44}}{2C_{44}},\qquad
\delta = \frac{(C_{13}+C_{44})^2 - (C_{33}-C_{44})^2}
{2C_{33}(C_{33}-C_{44})}.$$

$\varepsilon$ measures P-wave anisotropy, $\gamma$ shear-wave anisotropy, and
$\delta$ — the awkward one — controls the P speed at intermediate angles.

**qP, qSV, qSH.** The three body-wave branches, named for their polarisation in
the *limit* of a symmetry direction. In a VTI medium with the ray in the $x$–$z$
plane, qSH is polarised exactly along $y$; qP and qSV are the faster and slower
of the remaining two.

**Phase velocity.** The speed of a surface of constant phase, $v = \omega/k$.
**Group velocity.** The speed at which energy travels, $\mathbf{v}_g =
\partial\omega/\partial\mathbf{k}$. In an anisotropic medium these are different
vectors, not just different magnitudes.

## 3. Derivation: the Christoffel equation

Start from the elastodynamic equation of [01](01-wave-equation-elastic.md), here
for a homogeneous medium:

$$\rho\,\ddot{u}_i = C_{ijkl}\,\partial_j\partial_l u_k .$$

Insert a plane wave with unit polarisation $U_k$ and wavevector
$\mathbf{k} = k\mathbf{n}$, $u_k = U_k\exp\!\left[\mathrm{i}(k n_j x_j - \omega
t)\right]$. Each derivative brings down a factor $\mathrm{i}k n$:

$$-\rho\omega^2 U_i = -k^2 C_{ijkl}n_j n_l U_k
\quad\Longrightarrow\quad
\boxed{\;\rho v^2 U_i = \Gamma_{ik}U_k,\qquad
\Gamma_{ik} \equiv C_{ijkl}\,n_jn_l,\qquad v = \omega/k.\;}$$

$\Gamma$ is the **Christoffel tensor**: symmetric, real, and positive definite
for a stable medium. Its eigenvalues are $\rho v^2$ for the three branches and
its eigenvectors are their polarisations. Two immediate consequences:

- **Three branches always**, for any direction, whatever the symmetry. Anisotropy
  does not create new wave types; it splits and renames the three we already had.
- **Polarisations are eigenvectors, not geometric constructions.** In an
  isotropic medium $C_{ijkl} = \lambda\delta_{ij}\delta_{kl} +
  \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$ makes $\Gamma =
  (\lambda+\mu)\mathbf{n}\mathbf{n}^{\!\top} + \mu\mathbf{I}$, whose eigenvectors
  are $\mathbf{n}$ (one) and the plane perpendicular to it (two, degenerate).
  That is precisely where "P is parallel, S is perpendicular" comes from — and it
  is a property of the isotropic tensor, not a law of nature.

## 4. Derivation: the VTI tensor and the Thomsen parameterisation

In Voigt notation a VTI medium has the form

$$
\mathbf{C} =
\begin{pmatrix}
C_{11} & C_{12} & C_{13} & 0 & 0 & 0\\
C_{12} & C_{11} & C_{13} & 0 & 0 & 0\\
C_{13} & C_{13} & C_{33} & 0 & 0 & 0\\
0 & 0 & 0 & C_{44} & 0 & 0\\
0 & 0 & 0 & 0 & C_{44} & 0\\
0 & 0 & 0 & 0 & 0 & C_{66}
\end{pmatrix},
\qquad C_{12} = C_{11} - 2C_{66},
$$

with five independent constants: $C_{11}, C_{33}, C_{13}, C_{44}, C_{66}$. The
inversion of the definitions in §2 gives the standard construction

$$C_{33} = \rho\alpha_0^2,\qquad C_{44} = \rho\beta_0^2,\qquad
C_{11} = C_{33}(1+2\varepsilon),\qquad C_{66} = C_{44}(1+2\gamma),$$

$$C_{13} = \sqrt{2C_{33}(C_{33}-C_{44})\delta + (C_{33}-C_{44})^2} - C_{44}.$$

Here $\alpha_0$ and $\beta_0$ are the P and S speeds along the symmetry axis
(vertical), and $\rho$ the density. Check the isotropic limit: $\varepsilon =
\delta = \gamma = 0$ gives $C_{11} = C_{33}$, $C_{66} = C_{44}$,
$C_{13} = C_{33} - 2C_{44}$, which is exactly Lamé form.

### 4.1 Numerical construction (SYNTHETIC model of the demonstration)

$\alpha_0 = 4000\ \mathrm{m\,s^{-1}}$, $\beta_0 = 2400\ \mathrm{m\,s^{-1}}$,
$\rho = 2600\ \mathrm{kg\,m^{-3}}$, $\varepsilon = 0.20$, $\delta = 0.15$,
$\gamma = 0.20$. Then

$$C_{33} = \rho\alpha_0^2 = 2600 \times 1.6\times10^{7}
= 4.160\times10^{10}\ \mathrm{Pa} = 41.6000\ \mathrm{GPa},$$

$$C_{44} = 2600 \times 5.76\times10^{6} = 1.4976\times10^{10}\ \mathrm{Pa}
= 14.9760\ \mathrm{GPa},$$

$$C_{11} = 41.6(1.4) = 58.2400\ \mathrm{GPa},\qquad
C_{66} = 14.976(1.4) = 20.9664\ \mathrm{GPa},$$

$$C_{12} = C_{11} - 2C_{66} = 58.2400 - 41.9328 = 16.3072\ \mathrm{GPa},$$

$$C_{13} = \sqrt{2(41.6)(26.624)(0.15) + (26.624)^2} - 14.976
= 17.2902\ \mathrm{GPa},$$

all of which are printed by the demonstration. Feeding the tensor back into the
definition of $\delta$ returns $0.1500000000$, matching the input to the printed
precision: the tensor and the parameter set are the same object written two
ways.

## 5. Derivation: the exact SH speed, and the axis checks

For VTI, the $y$-polarised (SH) mode decouples because no entry of the tensor
couples $y$ motion to the $x$–$z$ plane. With $\mathbf{n} =
(\sin\theta, 0, \cos\theta)$ the Christoffel equation for $U_y$ alone reads
$\rho v^2 = C_{66}\sin^2\theta + C_{44}\cos^2\theta$, so

$$\boxed{\;v_{SH}(\theta) =
\sqrt{\frac{C_{66}\sin^2\theta + C_{44}\cos^2\theta}{\rho}}
= \beta_0\sqrt{1 + 2\gamma\sin^2\theta}.\;}$$

This is one of the few exact closed forms in anisotropic wave propagation, and it
is the reason SH is the cleanest observable: its polarisation is exactly
horizontal for every $\theta$, so a horizontally oriented sensor can record it
without contamination.

Evaluating at the axes gives the four speeds the demonstration checks:

| Direction | Branch | Speed formula | Value (SYNTHETIC) |
|---|---|---|---|
| vertical | qP | $\alpha_0$ | $4000.0000\ \mathrm{m\,s^{-1}}$ |
| vertical | qS (both) | $\beta_0$ | $2400.0000\ \mathrm{m\,s^{-1}}$ |
| horizontal | qP | $\alpha_0\sqrt{1+2\varepsilon}$ | $4732.8638\ \mathrm{m\,s^{-1}}$ |
| horizontal | qSH | $\sqrt{C_{66}/\rho} = \beta_0\sqrt{1+2\gamma}$ | $2839.7183\ \mathrm{m\,s^{-1}}$ |
| horizontal | qSV | $\sqrt{C_{44}/\rho} = \beta_0$ | $2400.0000\ \mathrm{m{\,}s^{-1}}$ |

The demonstration prints each of these, and the equality
$\sqrt{C_{66}/\rho} = \beta_0\sqrt{1+2\gamma}$ is the quantitative statement that
$\gamma$ is the shear-anisotropy parameter. **Shear-wave splitting** is now a
number, not a slogan: along the horizontal direction the two S branches differ by
$2839.7183 - 2400.0000 = 439.72\ \mathrm{m\,s^{-1}}$, which is $18.3\%$ of
$2400\ \mathrm{m\,s^{-1}}$; along the symmetry axis they are **degenerate** and
the splitting is exactly zero.

That last sentence is the whole measure-theoretic difficulty of shear-wave
splitting: a splitting observation with a ray along a symmetry axis records
nothing, however anisotropic the rock.

### 5.1 The sweep

Speeds from the eigenproblem, and the SH closed form for comparison:

| $\theta$ (deg) | qP (m/s) | qSV (m/s) | qSH (m/s) | qSH exact (m/s) | $\lvert$diff$\rvert$ |
|---|---|---|---|---|---|
| 0 | 4000.0000 | 2400.0000 | 2400.0000 | 2400.0000 | $0$ |
| 15 | 4041.2693 | 2420.0952 | 2431.9414 | 2431.9414 | $4.5\times10^{-13}$ |
| 30 | 4163.4830 | 2454.6708 | 2517.1412 | 2517.1412 | $0$ |
| 45 | 4346.0321 | 2464.1439 | 2629.0683 | 2629.0683 | $0$ |
| 60 | 4537.9393 | 2442.7663 | 2736.4210 | 2736.4210 | $0$ |
| 75 | 4680.5841 | 2413.1751 | 2812.4120 | 2812.4120 | $4.5\times10^{-13}$ |
| 90 | 4732.8638 | 2400.0000 | 2839.7183 | 2839.7183 | $4.5\times10^{-13}$ |

Note the shape of the qSV curve: $2400 \to 2464 \to 2400$, with a maximum near
$45^\circ$. An S-wave speed that *decreases* with angle beyond $45^\circ$ is
impossible in an isotropic medium and is a robust anisotropy diagnostic in a
direction sweep.

## 6. Derivation: the weak-anisotropy approximations, and their measured error

Expanding the Christoffel eigenvalues to first order in
$(\varepsilon,\delta,\gamma)$ gives the Thomsen approximations

$$v_{qP} \approx \alpha_0\left(1 + \delta\sin^2\theta\cos^2\theta
+ \varepsilon\sin^4\theta\right),$$

$$v_{qSV} \approx \beta_0\left(1 +
\frac{\alpha_0^2}{\beta_0^2}(\varepsilon-\delta)\sin^2\theta\cos^2\theta\right),$$

with the exact $v_{SH}$ of §5 unchanged (it is already first order in $\gamma$
in an exact sense). At $\theta = 30^\circ$ with the model of §4.1:

- $\sin^2 30^\circ = 0.25$, $\cos^2 30^\circ = 0.75$, $\sin^4 30^\circ = 0.0625$;
- $v_{qP} \approx 4000(1 + 0.15(0.1875) + 0.20(0.0625))
  = 4000(1.040625) = 4162.5\ \mathrm{m\,s^{-1}}$ against the exact
  $4163.4830\ \mathrm{m\,s^{-1}}$;
- $v_{qSV} \approx 2400\left(1 + (4000/2400)^2(0.05)(0.1875)\right)
  = 2400(1.0260417) = 2462.5\ \mathrm{m\,s^{-1}}$ against the exact
  $2454.6708\ \mathrm{m\,s^{-1}}$.

The measured errors the demonstration reports are the honest part of the story:

| $\theta$ (deg) | qP error (%) | qSV error (%) |
|---|---|---|
| 15 | 0.0044 | 0.0305 |
| 30 | 0.0236 | 0.3179 |
| 45 | 0.0912 | 0.7727 |
| 60 | 0.5383 | 0.8014 |
| 75 | 1.1265 | 0.3163 |

At $\varepsilon = 0.20$ — strong anisotropy — the approximation is excellent
within $15^\circ$ of an axis and degrades to a percentage at mid-angles. The
error is not a property of the anisotropy alone: it is the size of a truncated
series, and it must be *reported* whenever the approximation is used. A useful
sanity rule from the same numbers: the weak-anisotropy expressions are
indicative, not quantitative, at this anisotropy strength.

## 7. Derivation: polarisation is not locked to the ray

Because polarisation is an eigenvector of $\Gamma$, it is parallel to $\mathbf{n}$
only if $\mathbf{n}$ is an eigenvector — true for isotropic media, false in
general. The demonstration measures the deviation:

| $\theta$ (deg) | angle$(v_{qP},\mathbf{n})$ | angle$(v_{qSH},\hat y)$ | angle$(v_{qSV},\hat n) - 90^\circ$ |
|---|---|---|---|
| 0 | 0.000000 | $0$ | 0.000000 |
| 20 | 4.173320 | $0$ | $-4.173320$ |
| 40 | 7.026955 | $0$ | $-7.026955$ |
| 60 | 6.353684 | $0$ | $-6.353684$ |
| 80 | 2.494939 | $0$ | $-2.494939$ |
| 90 | 0.000000 | $8.5\times10^{-7}$ | 0.000000 |

Three statements follow, all of them consequences of the eigenstructure:

1. qP is tilted off the propagation direction by up to $\approx 7^\circ$ at this
   anisotropy, and qSV by the same amount in the opposite sense.
2. The tilt **vanishes on the symmetry axes** and on the horizontal plane — the
   directions where the isotropic intuition is accidentally right.
3. qSH is exactly horizontal to machine precision ($8.5\times10^{-7}$ degrees at
   $\theta = 90^\circ$, which is round-off in the $y$-component), which is why SH
   is used for anisotropy measurements whenever a horizontally polarised source
   or a suitable conversion is available.

## 8. Derivation: phase versus group velocity

Phase velocity moves surfaces of constant phase; energy moves along the ray.
Write $v(\theta)$ for the phase speed, with angle $\theta$ from the axis. For a
locally smooth dispersion surface,

$$\mathbf{v}_g = \frac{\partial\omega}{\partial\mathbf{k}}
= v\,\hat n + \frac{\mathrm{d}v}{\mathrm{d}\theta}\,\hat\theta ,$$

which says the group-velocity vector is the phase vector plus a tangential
correction proportional to the angular gradient of the phase speed. Its
magnitude and direction can be computed independently by differentiating
$\omega(\mathbf{k})$ numerically, and the demonstration does both:

| $\theta$ (deg) | phase $v$ (m/s) | $\lvert\mathbf{v}_g\rvert$ (m/s) | ray–phase angle (deg) | $\lvert$formula $-$ numeric$\rvert$ |
|---|---|---|---|---|
| 10 | 4018.3148 | 4023.8100 | 2.994747 | $4.076\times10^{-4}$ |
| 30 | 4163.4830 | 4207.3397 | 8.279983 | $1.233\times10^{-3}$ |
| 45 | 4346.0321 | 4410.9927 | 9.845299 | $1.146\times10^{-3}$ |
| 60 | 4537.9393 | 4587.5410 | 8.433117 | $6.494\times10^{-4}$ |
| 80 | 4709.3346 | 4716.8935 | 3.244119 | $1.548\times10^{-4}$ |

Two measured facts matter for data analysis. First, the ray deviates from the
phase normal by up to about $9.8^\circ$, so a phase-speed model applied to a
travel time (which is a group quantity) introduces a geometry error of that
order. Second, the deviation **vanishes on the symmetry axis and in the plane
perpendicular to it**, which is why a horizontal-layer assumption survives
vertical-incidence work and fails at mid-angles.

## 9. Rotation, HTI, and the isotropic limit

**HTI is VTI rotated.** Build a VTI tensor and rotate it by $90^\circ$ about the
$y$-axis; rotate the propagation direction with it. Every speed must be
unchanged, because space is isotropic under rotation. The demonstration measures
a maximum difference of $0$ (exactly) for the tabulated directions and
$4.5\times10^{-13}\ \mathrm{m\,s^{-1}}$ at the $90^\circ$ row — floating-point
round-off. This is a *check on the implementation*, but it is also the physical
statement that a medium with vertical cracks is, from the point of view of an
appropriately oriented coordinate system, a medium with horizontal layering.
Two structural interpretations, one tensor.

**The isotropic limit.** Setting $\varepsilon = \delta = \gamma = 0$ gives a
maximum departure of any speed from $\alpha_0 = 4000\ \mathrm{m\,s^{-1}}$ or
$\beta_0 = 2400\ \mathrm{m\,s^{-1}}$ of $4.547\times10^{-13}\ \mathrm{m\,s^{-1}}$
over all directions. The anisotropic solver therefore collapses exactly onto the
isotropic one — the sharpest available test of the Voigt-to-tensor mapping, and
the reason this lesson can claim to *generalise* lessons 01–05 rather than
replace them.

## 10. Assumptions and regime of validity

1. **Homogeneous, single-symmetry medium.** No variation of the symmetry axis
   with position, no spatial gradients. A dipping or tilted symmetry axis (TTI)
   is not treated here, and it changes the geometry of every diagnostic above.
2. **Linear elasticity, infinitesimal strain.** The stiffness tensor is a
   fourth-order constant; nonlinear elasticity is out of scope.
3. **No attenuation and no dispersion.** In a real medium $C$ is complex and
   frequency-dependent, which is the subject of
   [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md).
4. **Transverse isotropy only.** Thomsen parameters describe VTI/HTI. An
   orthorhombic or monoclinic medium — which fractured rock at reservoir scale
   often is — needs more parameters and does not have a compact weak-anisotropy
   form.
5. **Weak-anisotropy expressions only where stated.** They are used in §6 with
   measured errors up to 1.13% (qP) and 0.80% (qSV) at $\varepsilon = 0.20$; they
   are not used anywhere else in the lesson.
6. **A plane wave in an infinite medium.** Free-surface effects, and the
   anisotropy of the near-surface layer itself, are not in the model; a
   free-surface Rayleigh wave in an anisotropic half space is also
   direction-dependent.
7. **The polarisation angles are in the $x$–$z$ plane.** They are not a general
   statement about azimuth for a symmetry axis that is not aligned with a
   coordinate axis.

## 11. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| stiffness | $C_{ij}$ | Pa | $\rho v^2$ |
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | |
| speed | $v$ | $\mathrm{m\,s^{-1}}$ | $\sqrt{[\mathrm{Pa}]/[\mathrm{kg\,m^{-3}}]}$ |
| Thomsen parameters | $\varepsilon,\delta,\gamma$ | – | ratio of stiffnesses |
| phase | $2\omega\tau$ | rad | $\mathrm{s^{-1}}\times\mathrm{s}$ |

The dimensionality of the eigenvalue equation is the single most useful check
available: $\rho v^2$ must be a stiffness, so a stiffness divided by density is
a squared speed. Concretely,
$2600 \times (4000)^2\ \mathrm{kg\,m^{-3}\,m^2\,s^{-2}} = 4.16\times10^{10}
\ \mathrm{Pa}$, which is the $C_{33}$ of §4.1.

## 12. Worked examples

### 12.1 Building the tensor by hand

From $\rho = 2600$, $\alpha_0 = 4000$, $\beta_0 = 2400$:

$$C_{33} = 2600(4000)^2 = 4.16\times10^{10}\ \mathrm{Pa},\qquad
C_{44} = 2600(2400)^2 = 1.4976\times10^{10}\ \mathrm{Pa},$$
$$C_{11} = C_{33}(1+2(0.20)) = 5.824\times10^{10}\ \mathrm{Pa},\qquad
C_{66} = C_{44}(1+2(0.20)) = 2.09664\times10^{10}\ \mathrm{Pa},$$
$$C_{12} = C_{11} - 2C_{66} = 1.63072\times10^{10}\ \mathrm{Pa},$$
$$C_{13} = \sqrt{2(4.16\times10^{10})(2.6624\times10^{10})(0.15)
+ (2.6624\times10^{10})^2} - 1.4976\times10^{10}
= 1.72902\times10^{10}\ \mathrm{Pa}.$$

Converted to GPa these are the six printed values $58.2400$, $41.6000$,
$17.2902$, $14.9760$, $20.9664$, $16.3072$.

### 12.2 The splitting, as a number and as a caveat

Along the horizontal direction in the $x$–$z$ plane:

$$v_{SH} = \sqrt{C_{66}/\rho} = \sqrt{2.09664\times10^{10}/2600}
= 2839.7183\ \mathrm{m\,s^{-1}},$$
$$v_{SV} = \sqrt{C_{44}/\rho} = \sqrt{1.4976\times10^{10}/2600}
= 2400.0000\ \mathrm{m\,s^{-1}},$$

$$\text{split} = 439.72\ \mathrm{m\,s^{-1}} = 18.3\%\ \text{of } v_{SV}.$$

Along the symmetry axis both are $2400.0000\ \mathrm{m\,s^{-1}}$: split $= 0$,
exactly, by degeneracy. Any splitting interpretation must therefore state the
propagation direction, not just the magnitude.

### 12.3 Ray–phase split

At $\theta = 45^\circ$ the phase speed is $4346.0321\ \mathrm{m\,s^{-1}}$, the
group speed is $4410.9927\ \mathrm{m\,s^{-1}}$, and the group-velocity direction
is $9.845299^\circ$ away from the phase direction. Using the phase speed to
predict an arrival time over a path of length $L$ along the ray therefore
introduces a relative time error of order
$1 - \cos(9.845^\circ) = 1.47\times10^{-2}$, i.e. about 1.5% — larger than the
weak-anisotropy approximation error of §6, and in the opposite direction from
the temptation to ignore it.

## 13. Python demonstration

[`code/anisotropic_propagation_demo.py`](./code/anisotropic_propagation_demo.py)
is print-only, seeded with a fixed generator where randomness is used, and exits
0. It:

1. builds the VTI stiffness tensor from the Thomsen parameters and reconstructs
   $\delta$ from the tensor;
2. solves the Christoffel eigenproblem over a direction sweep, identifies the
   three branches physically, and compares qSH with the exact closed form;
3. compares the Thomsen weak-anisotropy approximations with the exact solution
   and prints the error;
4. prints the polarisation angles, showing that qSH is exactly horizontal and
   qP/qSV are not locked to the ray;
5. computes the group velocity by the gradient formula and by numerical
   differentiation of $\omega(\mathbf{k})$, and reports the ray–phase split;
6. rotates the tensor to HTI and verifies that all speeds are unchanged;
7. verifies that the solver collapses exactly onto isotropy when
   $\varepsilon = \delta = \gamma = 0$.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    06-seismology/01-elastic-wave-propagation/code/anisotropic_propagation_demo.py
```

## 14. Exercises

Full sets with worked solutions are in
[`exercises/08-anisotropic-propagation-exercises.md`](./exercises/08-anisotropic-propagation-exercises.md)
and
[`exercises/08-anisotropic-propagation-solutions.md`](./exercises/08-anisotropic-propagation-solutions.md).
They cover building a tensor from Thomsen parameters, using the exact SH formula,
evaluating and bounding the weak-anisotropy error, computing the shear-wave
splitting for a stated direction, and a research-level question on why a
splitting measurement cannot be inverted for crack density without an
assumption about crack orientation.

## Mastery checkpoint

Without notes:

**(a)** Derive the Christoffel equation and say what its eigenvalues are, with
units.
**(b)** For $\alpha_0 = 4000\ \mathrm{m\,s^{-1}}$, $\beta_0 = 2400\ \mathrm{m\,s^{-1}}$,
$\rho = 2600\ \mathrm{kg\,m^{-3}}$, compute $C_{33}$ and $C_{44}$ in GPa.
**(c)** State the exact $v_{SH}(\theta)$ formula and evaluate it at
$\theta = 0^\circ$ and $90^\circ$ for $\gamma = 0.20$.
**(d)** Compute the shear-wave splitting along the horizontal direction for
$\gamma = 0.20$ and express it as a percentage of $\beta_0$.
**(e)** At $45^\circ$ the phase speed is $4346.0321\ \mathrm{m\,s^{-1}}$ and the
group speed $4410.9927\ \mathrm{m\,s^{-1}}$. Explain in three sentences why these
differ and what a travel-time inversion that ignores the difference gets wrong.
**(f)** State two independent checks the demonstration performs that the physics
requires, and say what each would catch.

A worked version of (a)–(d) is in
[`exercises/08-anisotropic-propagation-solutions.md`](./exercises/08-anisotropic-propagation-solutions.md).

## Common pitfalls

1. **Treating $\gamma$ as "the splitting".** Splitting depends on direction;
   along a symmetry axis it is exactly zero whatever $\gamma$ is.
2. **Using weak-anisotropy formulas for strong anisotropy without printing the
   error.** At $\varepsilon = 0.20$ the qP error reaches 1.13% and the qSV error
   0.80%; the approximation is a series truncation, not a definition.
3. **Reporting a phase speed as if it were a ray speed.** They differ in both
   magnitude and direction (up to $9.8^\circ$ here), and the geometry error can
   exceed the anisotropy signal being measured.
4. **Assuming the P polarisation is along the ray.** It is tilted by up to
   $7^\circ$ in this model, which breaks three-component sensor rotations that
   assume parallelism.
5. **Reading anisotropy as structure.** A dipping interface and an anisotropic
   layer can produce similar travel-time patterns; distinguishing them needs
   azimuthal coverage, not more offsets in one direction.

## Self-assessment checklist

- [ ] I can derive the Christoffel equation and interpret its eigenvalues and eigenvectors.
- [ ] I can build a VTI tensor from $(\alpha_0,\beta_0,\rho,\varepsilon,\delta,\gamma)$ and check $\delta$.
- [ ] I can derive and evaluate the exact $v_{SH}(\theta)$.
- [ ] I can compute the Thomsen approximations and state their measured error.
- [ ] I can explain why qP/qSV polarisations are not locked to the ray while qSH is.
- [ ] I can compute the group velocity from the phase speed and report the ray–phase split.
- [ ] I can state the symmetry assumptions behind a shear-wave splitting measurement.

## Related modules

- [06-01 Elastic Wave Propagation](README.md) — the isotropic theory this
  lesson generalises, and its four earlier lessons.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  delaying anisotropy-aware travel-time computation to a ray framework that can
  carry a direction-dependent speed.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — where
  anisotropy shows up as non-hyperbolic moveout and as an amplitude-versus-offset
  effect.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) — the
  micromechanics that produces $\varepsilon$, $\delta$ and $\gamma$ from layering
  and cracks, in
  [05 Anisotropy in Rocks](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md).
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  a single station cannot separate anisotropy from a dipping interface.
