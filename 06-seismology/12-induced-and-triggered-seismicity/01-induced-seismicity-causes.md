---
id: 06-12-01
title: "Causes of Induced Seismicity: Injection, Extraction, Reservoirs"
level: doctoral
prereqs: ["06-03-01", "02-04-08"]
tags: [induced-seismicity, coulomb-stress, effective-stress, poroelasticity, reservoir]
---

# Causes of Induced Seismicity: Injection, Extraction, Reservoirs

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the effective-stress law $\sigma' = \sigma - \alpha p$ from the
   poroelastic constitutive relations, and state the two limits in which the
   Biot coefficient $\alpha$ is 0 or 1 and why neither is universal.
2. **Derive** the Coulomb failure function $CFS = \tau - \mu_f(\sigma_n - p)$
   with a stated sign convention, and state explicitly that $\mu_f$ (friction,
   dimensionless) is not the shear modulus $\mu$ (Pa).
3. **Classify** the mechanisms by which human operations change the state of
   stress on a fault — pore-pressure change, poroelastic strain, volumetric
   compaction, thermoelastic contraction, mass loading — and say for each which
   term in the Coulomb function it modifies and with what sign.
4. **Compute** the Coulomb stress change produced by a pressure change at a
   receiver of stated orientation, and state the sensitivity of the answer to
   the receiver plane.
5. **Explain** why a Coulomb stress change of either sign is not by itself
   evidence that an earthquake was induced.
6. **Verify** a point-double-couple static stress field against its closed-form
   displacement, its $1/r^3$ decay and its vanishing dilatation.

## Prerequisites

- [06-03-01 Faulting and Slip](../03-earthquake-sources/01-faulting-and-slip.md)
  — fault geometry, slip, and the stress on a fault plane.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  — Mohr–Coulomb failure, the friction envelope and the status of Byerlee's law.
- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  — the traction vector and the resolution of stress onto a plane.

## 1. Intuition: what a human operation can possibly change

An earthquake happens when the shear traction on a fault exceeds what friction
can hold. Nothing a well can do changes the rock's friction or its elastic
moduli appreciably. So the only lever available is the *state of stress* on the
fault, and the only useful question is: **which term in the failure criterion did
the operation change, at the fault, and by how much?**

There are exactly five answers, and every claimed case of induced seismicity is
one or a combination of them.

| Mechanism | What the operation does | Which term moves | Typical sign effect |
|---|---|---|---|
| Pore-pressure change | Fluid injected or withdrawn changes $p$ | $-\mu_f(\sigma_n - p)$, through $p$ | Injection destabilises; extraction stabilises the reservoir itself |
| Poroelastic strain | The rock around the pressured volume deforms | $\tau$ and $\sigma_n$ away from the reservoir | Either sign; dies off with distance |
| Volumetric compaction | Reservoir compacts as $p$ falls | $\sigma_n$ and $\tau$ at the reservoir margin | Destabilising at the margin, stabilising inside |
| Thermoelastic contraction | Cooled rock contracts | $\tau$ and $\sigma_n$ | Either sign; largest around a cooled volume |
| Mass loading | Water or waste piles on the surface | $\sigma_n$ mostly | Usually stabilising directly beneath the load, destabilising at its edges |

The essential structural point is that the *first* row is local and isotropic,
while the rest are tensorial and decay with distance. That is why the phrase
"induced seismicity" covers physically different processes that are often
treated as one, and why the same operation can stabilise one fault and
destabilise another.

Numbers in this lesson are **SYNTHETIC**: every figure quoted below is printed
by `code/coulomb_sign_flip_demo.py`, or is an exact standard constant stated with
its units. No real field, well or catalogue is measured, and no published number
is quoted.

## 2. Precise definitions

### 2.1 Stress, pressure and the effective stress

Let $\boldsymbol\sigma$ be the total Cauchy stress tensor in the porous rock
(tension positive in this lesson, and this convention is stated again wherever a
sign matters). Let $p$ be the pore-fluid pressure. Let $\mathbf{n}$ be the unit
normal to a fault plane and $\mathbf{t} = \boldsymbol\sigma\,\mathbf{n}$ the
traction on it. Then

$$\sigma_n = \mathbf{n}\cdot\mathbf{t} = n_i\sigma_{ij}n_j
\qquad\text{(normal traction, tension positive)},$$

$$\tau = |\mathbf{t} - \sigma_n\mathbf{n}|
\qquad\text{(shear traction magnitude)}.$$

**Pressure and stress have the same dimension**, $[\sigma] = [p] =
\mathrm{Pa} = \mathrm{kg\,m^{-1}\,s^{-2}}$. This is not a coincidence: pore
pressure is a stress carried by the fluid, and it enters the failure criterion on
the same footing as the normal stress. Writing "stress in MPa and pressure in
bar" invites factor-of-ten errors, and the units must be carried explicitly.

The **effective normal stress** is defined by

$$\sigma_n' = \sigma_n - \alpha p,$$

where $\alpha$ is the **Biot coefficient**, dimensionless, $0 \le \alpha \le 1$.
With the sign convention above (tension positive), compressive $\sigma_n$ is
negative; in the seismological literature compression is usually taken positive,
in which case $\sigma_n' = \sigma_n - \alpha p$ with both terms positive in
compression. **The two conventions give the same physics and opposite signs**;
what matters is that one convention is fixed and used consistently.

### 2.2 The Coulomb failure function

With compression positive for both $\sigma_n$ and $p$, and $\tau$ the shear
traction resolved in the fault's slip direction,

$$CFS = \tau - \mu_f(\sigma_n - p).$$

Failure is favoured when $CFS \ge 0$. Here $\mu_f$ is the **coefficient of
sliding friction**, dimensionless. It is *not* the shear modulus $\mu$ (Pa) that
appears in seismic wave speeds and in elastic Green's functions. Both appear in
this lesson; $\mu_f$ always carries the subscript.

> **A named trap.** In papers on induced seismicity, "$\mu$" is friction and the
> shear modulus is written $G$; in papers on elasticity, "$\mu$" is the shear
> modulus and friction is written $f$. Reading a stress-transfer paper with the
> elasticity convention produces values wrong by $10^{10}$ in the wrong units and
> is a genuine, published source of confusion.

Taking a change $\Delta$ of every quantity (total stress, pore pressure, and the
receiver geometry held fixed) gives

$$\Delta CFS = \Delta\tau - \mu_f\left(\Delta\sigma_n - \Delta p\right)
= \Delta\tau - \mu_f\Delta\sigma_n + \mu_f\Delta p.$$

Three independent terms. A **pressure-only** change with no total-stress
change gives the simplest and most quoted result:

$$\boxed{\ \Delta CFS = \mu_f\,\Delta p\ }\qquad(\Delta\boldsymbol\sigma =
\mathbf{0}).$$

### 2.3 The five mechanisms in terms of the three terms

- **Pore pressure** acts only through $\mu_f\Delta p$.
- **Poroelastic strain** and **thermoelastic contraction** act through
  $\Delta\tau$ and $\Delta\sigma_n$, with coefficients that depend on the
  receiver plane.
- **Compaction** and **mass loading** act primarily through $\Delta\sigma_n$.

## 3. Derivations

### 3.1 The Biot coefficient from the constitutive law

Model the porous rock as a linear isotropic poroelastic solid. Partition the
total stress into a part carried by the solid skeleton and a part carried by the
fluid:

$$\sigma_{ij} = \underbrace{2G\,\varepsilon_{ij} + \lambda\,\varepsilon_{kk}
\delta_{ij}}_{\text{skeleton}} - \alpha\,p\,\delta_{ij},
\qquad \alpha = 1 - \frac{K}{K_s},$$

where $K$ is the drained bulk modulus of the rock, $K_s$ the bulk modulus of the
solid grains, $G$ the shear modulus, and $\lambda$ a Lamé parameter. Check the
two limits:

- **Incompressible grains** ($K_s \to \infty$, e.g. quartz with $K_s$ of order
  $10^{11}$ Pa while a porous sandstone has $K$ of order $10^{10}$ Pa):
  $K/K_s \to 0$ and $\alpha \to 1$. This is **Terzaghi's** effective stress
  $\sigma' = \sigma - p$.
- **No connected porosity** ($K \to K_s$, a tight crystalline rock):
  $\alpha \to 0$ and pore pressure does nothing to the skeleton.

Neither is universal. For a rock with 10 % porosity, $K/K_s$ is commonly in the
range 0.3 to 0.8, so $\alpha$ is commonly 0.2 to 0.7 — a range, not a constant.
**Any calculation of pressure-induced failure that silently sets $\alpha = 1$
overstates the effect by a factor $1/\alpha$, up to 5.**

### 3.2 A pressure change and the Coulomb function: the isotropic result

Suppose a pressure change $\Delta p$ occurs over a region small compared with the
distance to the receiver, and suppose the total stress at the receiver is
unchanged (an idealisation, discussed in §5). Then

$$\Delta CFS = \mu_f\Delta p.$$

For a **1 MPa** pressure increase and $\mu_f = 0.6$:

$$\Delta CFS = 0.6 \times 10^{6}\ \mathrm{Pa} = 6\times10^{5}\ \mathrm{Pa}
= 0.6\ \mathrm{MPa}.$$

Because the result is independent of the receiver plane, the pressure term is the
*only* part of the problem that is not degenerate. That is why pressure diffusion
is the mechanism that is easiest to argue and why the argument is usually made
with the front and not with the stress.

### 3.3 The static stress change of a point double couple

For the tensorial mechanisms the receiver-plane dependence is unavoidable, and it
is worth deriving the source field so that the dependence can be seen rather than
asserted. In an infinite, homogeneous, isotropic elastic medium the displacement
from a point force is Kelvin's solution,

$$G_{ij}(\mathbf{r}) = \frac{1}{16\pi\mu(1-\nu)}
\left[(3-4\nu)\delta_{ij} + \frac{r_ir_j}{r^2}\right]\frac{1}{r},$$

with $\mu$ the **shear modulus** here. A double couple with moment tensor
$M_{jk} = M_0(d_jn_k + n_jd_k)$ (with $M_0$ in N·m) then gives

$$u_i(\mathbf{x}) = -M_{jk}\,\partial_k G_{ij} = -M_{jk}H_{ijk},$$

$$H_{ijk} = \frac{\phi}{r^2}\Big[-(3-4\nu)\delta_{ij}\hat r_k
+ (\delta_{ik}\hat r_j + \delta_{jk}\hat r_i) - 3\hat r_i\hat r_j\hat r_k\Big],
\qquad \phi = \frac{1}{16\pi\mu(1-\nu)}.$$

Note the $1/r^2$ prefactor: every term carries one power of $\hat r$, so
$H_{ijk} \sim 1/r^2$ and $u \sim 1/r^2$. Differentiating once more for the strain
gives $\varepsilon \sim 1/r^3$, hence

$$\Delta\sigma \sim \frac{M_0}{r^3}\,\times\,\text{(angular function)}.$$

Then $\Delta\tau$ and $\Delta\sigma_n$ are obtained by projecting the tensor:

$$\Delta\tau = \mathbf{d}\cdot\Delta\boldsymbol\sigma\,\mathbf{n},
\qquad
\Delta\sigma_n = \mathbf{n}\cdot\Delta\boldsymbol\sigma\,\mathbf{n}
= n_i\Delta\sigma_{ij}n_j .$$

(With tension positive, $n_i\Delta\sigma_{ij}n_j$ *is* the normal-stress change;
converting to the compression-positive form used in §2.2 flips its sign and
therefore the sign of the $\mu_f$ term. In the demonstration below the
compression-positive form is used, $\Delta CFS = \Delta\tau + \mu_f
n_i\Delta\sigma_{ij}n_j$.)

**Three exact consequences** of the above, each of which the demo verifies
numerically:

1. $\mathrm{tr}\,\Delta\boldsymbol\varepsilon = 0$: a double couple in a
   homogeneous medium changes no volume.
2. $\Delta\boldsymbol\sigma$ is symmetric and decays as $1/r^3$.
3. The static stress field is **even** under $\mathbf{r} \to -\mathbf{r}$, even
   though the displacement is odd there. Consequence: two receivers on opposite
   sides of the source, in the same relative orientation, feel the *same* stress
   change. This is the geometric origin of the four-lobed Coulomb pattern.

There is no simplification that removes the receiver orientation. For a point
receiver with a stress tensor $\Delta\boldsymbol\sigma$, the value of
$\Delta CFS$ depends on both $\mathbf{n}$ and $\mathbf{d}$, and the demonstration
measures exactly how much.

### 3.4 Compaction and the extraction case: both signs at once

Withdrawing fluid reduces $p$, which *increases* the effective normal stress and
therefore stabilises the reservoir faults — the sign is opposite to injection.
But the same withdrawal compacts the reservoir, and the resulting strain field is
not isotropic. Write the reservoir as a flat inclusion of thickness $h$ whose
thickness changes by $\Delta h < 0$ because the pore pressure fell. The
uniaxial-strain relation gives

$$\Delta h = \frac{h}{K + \tfrac43 G}\,(\Delta\sigma_v - \alpha\Delta p),$$

whose sign is fixed by $\Delta p$. Its consequences are (i) a subsidence bowl at
the surface, of magnitude $\Delta h$ times a geometric kernel, and (ii) a shear
stress concentration at the reservoir **margin**, where the compaction of the
reservoir meets the non-compacting rock outside. The margin effect is
destabilising; the reservoir interior effect is stabilising. That is a physical
statement about *where* the events go, and it is why extraction-induced
seismicity clusters at the edges of a compacting reservoir rather than within it.

## 4. Physical interpretation

Four statements are worth separating, because they are routinely conflated:

1. **A stress change is calculable.** Given a source model and an elastic
   structure, $\Delta CFS$ is a number. That number is a *model output*.
2. **A positive $\Delta CFS$ means "closer to failure".** It does not mean the
   fault fails. If the fault is 5 MPa from failure and the change is 0.05 MPa,
   nothing happens this century.
3. **A negative $\Delta CFS$ does not mean "no earthquake".** It means further
   from failure, on that plane, under that assumption. Change the assumed plane
   and the sign can change.
4. **A correlation in time and space is not a mechanism.** It is a reason to
   build the model of (1) and to test it against the observation.

The demonstration below measures the size of the gap between (1) and (4): over
the space of plausible receiver orientations at one position, half the
orientations give $\Delta CFS > 0$ and half give $\Delta CFS < 0$, at every
friction coefficient tested.

## 5. Assumptions and their consequences

| Assumption | What it buys | What it costs |
|---|---|---|
| Isotropic, homogeneous, linearly elastic medium | A closed-form stress field | Real basins are layered and anisotropic; layer-boundary stress changes are missed |
| Infinite medium (no free surface) | Kelvin's solution applies | Near-surface stress changes are wrong; the free surface matters within a few source depths |
| Point source ($r \gg$ source dimension) | The $1/r^3$ form | Fails exactly where $\Delta CFS$ is largest |
| Receiver plane known | $\Delta CFS$ is a number | The sign-flip measurement shows the answer is a coin flip when the plane is not known |
| $\sigma_n$ and $p$ independent | The three-term split | In a deforming porous medium the two are coupled through the poroelastic constitutive law |
| Elastic response | Instantaneous stress change | Real rocks creep, so the *time* dependence needs rate-and-state (lesson 3) |

## 6. Units and dimensional analysis

| Quantity | Symbol | SI unit | Notes |
|---|---|---|---|
| Total stress, pore pressure | $\boldsymbol\sigma$, $p$ | Pa | **Same dimension** |
| Biot coefficient | $\alpha$ | dimensionless | $0 \le \alpha \le 1$ |
| Friction coefficient | $\mu_f$ | dimensionless | Not the shear modulus |
| Shear modulus | $\mu$ or $G$ | Pa | Attention: symbol clash |
| Poisson's ratio | $\nu$ | dimensionless | $0 \le \nu < 0.5$ |
| Moment | $M_0$ | N·m | $= \mathrm{Pa\,m^3}$ |
| Coulomb stress change | $\Delta CFS$ | Pa | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |

Two checks that catch most errors:

- $[\mu_f \Delta p] = 1 \times \mathrm{Pa} = \mathrm{Pa}$, so $\Delta CFS$ has
  stress units. A friction coefficient carrying units is a mistake.
- $[M_0/r^3] = \mathrm{N\,m\,m^{-3}} = \mathrm{N\,m^{-2}} = \mathrm{Pa}$, so
  the $1/r^3$ stress decay is dimensionally forced.

The standard crustal unit is **1 MPa $= 10^{6}$ Pa $= 10$ bar**; 1 bar $=
10^{5}$ Pa. Converting between MPa and bar changes the number by a factor of ten
and nothing else, which is exactly why the factor is so easy to lose.

## 7. Worked examples

### 7.1 Pressure-induced Coulomb change with a stated $\alpha$

**Problem.** An injection raises the pore pressure at a fault by
$\Delta p = 2.5\ \mathrm{MPa}$. The fault is sandstone with $K = 8\ \mathrm{GPa}$
and grains with $K_s = 36\ \mathrm{GPa}$. Take $\mu_f = 0.6$. Compute
$\Delta CFS$, first with $\alpha = 1$ and then with the correct $\alpha$, and
state the ratio.

**Step 1 — Biot coefficient.**
$$\alpha = 1 - \frac{K}{K_s} = 1 - \frac{8}{36} = 1 - 0.2222 = 0.7778.$$

**Step 2 — effective pressure change.** $\alpha\Delta p = 0.7778 \times
2.5\ \mathrm{MPa} = 1.944\ \mathrm{MPa}$.

**Step 3 — Coulomb change.** $\Delta CFS = \mu_f\alpha\Delta p = 0.6 \times
1.944\ \mathrm{MPa} = \mathbf{1.167\ MPa}$.

**Step 4 — the naive value.** With $\alpha = 1$: $\Delta CFS = 0.6 \times 2.5 =
1.5\ \mathrm{MPa}$.

**Step 5 — the ratio.** $1.5/1.167 = 1.286$, i.e. assuming Terzaghi overstates
the pressure effect by **29 %** here. The error grows as $K/K_s$ grows; for a
stiff, low-porosity rock with $K/K_s = 0.8$ it is a factor of five.

### 7.2 The same pressure change on two receiver planes

**Problem.** At a receiver the total-stress change is negligible but the pressure
change is $\Delta p = 1\ \mathrm{MPa}$. Two faults pass through it: fault A is
optimally oriented and fault B is 30° off. Does the orientation matter?

**Solution.** For the pressure-only case, $\Delta CFS = \mu_f\alpha\Delta p$ for
*every* plane, because $\Delta p$ enters the criterion through the scalar
$p$ and not through the tensor $\boldsymbol\sigma$. So the orientation is
irrelevant — **as long as the pressure change really is uniform and the total
stress really does not change.** Both caveats are substantial in a real
reservoir, where the pressure change is spatially variable and where the
poroelastic strain it drives produces a tensorial stress change. The
pressure-only result is the starting idealisation, not the answer.

### 7.3 Where the tensorial term dominates: the measured demonstration

Run the module demonstration:

```text
<repo>/.venv/bin/python code/coulomb_sign_flip_demo.py
```

with its stated MODEL inputs: $M_w = 4$ ($M_0 = 1.259\times10^{15}$ N·m), source
depth 5 km, receiver 3 km horizontally away at the same depth, $\mu = 30$ GPa,
$\nu = 0.25$. The measured outputs are:

| Measured quantity | Value |
|---|---|
| Peak $|\Delta\sigma|$ component at the receiver | **0.0062 MPa** (6184 Pa) |
| Decay exponent $\mathrm{d}\ln(\max|\Delta\sigma|)/\mathrm{d}\ln r$ | **−3.0000** |
| Closed-form check, $u_y = 2M_0\phi(1-2\nu)/r^2$ | agreement to **0.0000 %** |
| Dilatation $\mathrm{div}\,\mathbf{u}$ | 0 (to double precision) |
| Fraction of 23 328 receiver orientations with $\Delta CFS > 0$ | **0.500** (every $\mu_f$) |
| Sign-flip rate for $\pm15°$ receiver-plane perturbation | 0.073 |
| Sign-flip rate for $\pm45°$ | 0.174 |
| Sign-flip rate for $\pm90°$ (i.e. unconstrained) | 0.514 |
| Fraction of orientations with $|\Delta CFS| < 0.10\times\max$ | 0.206 |

Three numbers deserve comment.

1. **0.0062 MPa is small.** A $M_w$ 4 source 3 km away changes the Coulomb stress
   by about 6 kPa, whereas the pressure term in §7.1 was 1.2 MPa — two orders of
   magnitude larger. For small induced events the pressure term is the dominant
   physical effect, and stress transfer between the induced events themselves is
   a second-order correction.
2. **The sign-flip rate grows with receiver uncertainty and reaches 0.5** at
   $\pm 90°$. That is the quantitative core: an unmapped receiver plane gives
   literally no information about the sign of $\Delta CFS$.
3. **$|\Delta\sigma| \propto M_0/r^3$.** The demo's magnitude sweep gives peak
   values of 0.0002, 0.0062, 0.1956 and 1.0997 MPa at $r = 3$ km for $M_w$ 3, 4,
   5 and 5.5 — a factor of 5.6 per half magnitude unit, as
   $10^{1.5\times0.5} = 5.62$ requires.

## 8. Python demonstration

`code/coulomb_sign_flip_demo.py`. Read the module docstring first: it states the
frame ($x$ north, $y$ east, $z$ down), the moment-tensor convention, and the sign
convention for $\sigma_n$ and $p$.

The script:

1. builds a moment tensor from strike, dip and rake using the standard
   (Aki & Richards) fault-normal and slip-vector expressions;
2. evaluates the displacement field from the analytic $H_{ijk}$ above;
3. obtains the strain by central differences of that analytic displacement and
   the stress from Hooke's law;
4. **validates**: a closed-form displacement check, symmetry, zero dilatation,
   the $-3$ decay exponent, the $\mathbf{r}\to-\mathbf{r}$ symmetry, and two
   derivative step sizes;
5. sweeps 23 328 receiver orientations and reports the sign statistics;
6. measures the sign-flip rate against the perturbation angle;
7. measures the magnitude scaling.

Exercises to run against the output: change `NU` from 0.25 to 0.4 and predict,
before running, whether the peak stress rises or falls. Change `MW` to 5.5 and
check the factor against $10^{1.5\Delta M_w}$.

## 9. Exercises

### ★ Foundational

**★1.** State the dimensions of $\alpha$, $\mu_f$, $M_0$ and $\Delta CFS$, and
show that $\mu_f\Delta p$ has stress dimensions.

**★2.** A fault has $\sigma_n = 40$ MPa (compression positive), $p = 15$ MPa and
$\mu_f = 0.6$. Compute $CFS = \tau - \mu_f(\sigma_n - p)$ for $\tau = 12$ MPa.
Is the fault closer to failure than one with $CFS = 0$?

**★3.** Compute $\alpha$ for $K = 20$ GPa, $K_s = 40$ GPa. Then compute it for
$K = 4$ GPa, $K_s = 40$ GPa, and say in one sentence why the second rock is more
sensitive to pore pressure.

### ★★ Applied

**★★4.** An injection raises $p$ by 3 MPa at a fault in a rock with
$K = 12$ GPa, $K_s = 45$ GPa, $\mu_f = 0.55$. Compute $\Delta CFS$. Then compute
the injection pressure change that would be needed to produce
$\Delta CFS = 0.1$ MPa, and comment on whether that is a large or small change
relative to the 3 MPa in the first part.

**★★5.** Using the demo's magnitude table, compute the peak $|\Delta\sigma|$ at
5 km from an $M_w$ 4.5 source by scaling the $r = 3$ km value, and compare with
the pressure term for a 0.5 MPa pressure change with $\mu_f = 0.6$. Which
dominates?

**★★6.** The demo measures a sign-flip rate of 0.073 for a $\pm15°$
receiver-plane perturbation and 0.514 for $\pm90°$. Sketch (by hand, on a log
axis) the growth, and state the perturbation angle at which roughly a quarter of
cases flip.

### ★★★ Research

**★★★7.** Derive, from the poroelastic constitutive law
$\sigma_{ij} = 2G\varepsilon_{ij} + \lambda\varepsilon_{kk}\delta_{ij} -
\alpha p\delta_{ij}$, the stress change produced by a spherical pressurised
inclusion of radius $a$ at distance $r \gg a$ in an infinite medium, in the
undrained limit (no fluid flow). Show that it decays as $1/r^3$ and state the
undrained Poisson ratio $\nu_u$ in terms of $\nu$, $\alpha$ and the Skempton
coefficient $B$.

**★★★8.** The demo neglects the free surface. Argue, using the $1/r^3$ decay
and the method of images, at what source-to-receiver distance the free surface
changes the answer by more than 20 % for a source at depth $z_s$.

**★★★9.** A colleague reports "the earthquake was induced: the Coulomb stress
change at the hypocentre was $+0.05$ MPa". Write the four questions you must ask
before accepting the claim, and state for each what the answer could do to the
sign or magnitude of the result.

## 10. Common mistakes

1. **Using $\mu$ for friction and the shear modulus in the same paragraph.** Name
   them $\mu_f$ and $G$.
2. **Assuming Terzaghi ($\alpha = 1$).** The error is a factor of $1/\alpha$,
   up to five for stiff, low-porosity rock.
3. **Reporting $\Delta CFS$ without the receiver plane.** The demo measures a
   sign-flip rate of 0.51 when the plane is unconstrained.
4. **Forgetting that pressure and stress share a dimension.** A pressure in bar
   and a stress in MPa differ by a factor of ten.
5. **Assuming a stress change is a failure.** $\Delta CFS = +0.05$ MPa against a
   fault 5 MPa from failure is a negligible nudge.
6. **Treating a positive Coulomb change as proof of causation.** It is a model
   output. The data are a catalogue.
7. **Forgetting that the elastic solution is instantaneous.** A creep or
   poroelastic response continues for months after the pressure change.
8. **Applying an infinite-medium solution near the surface.** The free surface
   and the layered structure change both the sign and the magnitude.
9. **Quoting Byerlee's law as a physical constant.** It is an empirical fit to
   laboratory data under stated conditions; treat it as such.
10. **Ignoring the pre-existing stress state.** $\Delta CFS$ is a change, not a
    level. Whether a fault is near failure is a separate, usually unknown,
    question.

## 11. Real-world applications

- **Regulatory review of a project.** The five-mechanism checklist is the
  structure of a quantitative screening study: which mechanism, which term,
  which faults, what magnitude of change.
- **Reservoir management.** Because the pressure term is isotropic and the
  compaction term is not, extraction and injection are not symmetric operations
  even where the volumes are equal.
- **Geothermal systems.** Thermoelastic contraction adds a term that injection
  alone does not have, and it grows as the reservoir cools.
- **Underground storage.** The same calculations govern gas storage, CO₂ storage
  and waste disposal, where the regulatory question is the maximum permitted
  pressure change.
- **Earthquake catalogues.** The events themselves are retrieved from services
  such as the [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/query)
  and [ComCat](https://earthquake.usgs.gov/data/comcat/), or through the
  [ObsPy FDSN client](https://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.html);
  the catalogue is the *observation* against which the model of §3 is tested.

## 12. Further reading

- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Blackwell).** The definitive treatment of effective stress, the
  Biot coefficient and poroelasticity. Level: graduate.
- **Segall, P. *Earthquake and Volcano Deformation* (Princeton University
  Press).** The source theory of §3.3 and the poroelastic inclusion problems of
  the exercises. Level: doctoral.
- **Scholz, C. H. *The Mechanics of Earthquakes and Faulting* (Cambridge
  University Press).** Friction, the state of stress on faults and the
  observational case for low crustal shear stress. Level: graduate.
- **Dieterich, J. *A constitutive law for rate of earthquake production and its
  application to earthquake clustering*, J. Geophys. Res. (1994).** The paper
  that turns a stress change into a rate change; it is the basis of lesson 3.
- **Kanamori, H., & Brodsky, E. E. *The physics of earthquakes*, Rep. Prog.
  Phys. (2004).** A readable survey connecting source physics to observable
  quantities. Level: graduate.
- **USGS Earthquake Hazards Program at <https://earthquake.usgs.gov>.** The
  authoritative source for catalogues, magnitude conventions and their
  revisions. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [06-12-02 Pore-Pressure Diffusion and Triggering Mechanisms](./02-pore-pressure-triggering.md)
  — the spatially variable pressure field that §7.2 assumes constant.
- [06-12-03 Rate-and-State Friction and the Dieterich Seismicity Model](./03-rate-state-triggering.md)
  — how a stress change becomes a rate change.
- [06-12-05 Documented Case Studies](./05-case-studies-induced.md) — the
  observational counterpart of this lesson's mechanisms.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  — Mohr–Coulomb, Byerlee's law and the rate-and-state law in full.
- [06-03-02 The Double Couple and Fault Geometry](../03-earthquake-sources/02-double-couple.md)
  — the source representation used in §3.3.

Exercises:
[`exercises/01-induced-seismicity-causes-exercises.md`](./exercises/01-induced-seismicity-causes-exercises.md)
and
[`exercises/01-induced-seismicity-causes-solutions.md`](./exercises/01-induced-seismicity-causes-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\alpha = 1 - K/K_s$ and state both of its limits. (§3.1)
- [ ] I can write $CFS = \tau - \mu_f(\sigma_n - p)$ with a stated sign
      convention and say that $\mu_f$ is not the shear modulus. (§2.2)
- [ ] I can list the five mechanisms and name the term each one moves. (§1, §2.3)
- [ ] I can compute $\Delta CFS$ for a pressure change with a stated $\alpha$.
      (§7.1)
- [ ] I can explain why the pressure-only result is orientation-independent and
      why that is an idealisation. (§7.2)
- [ ] I can state the $1/r^3$ decay and the number it gives for a stated source
      and distance. (§7.3)
- [ ] I can quote the measured sign-flip rate and say what it implies for
      attribution. (§7.3, §4)
- [ ] I can list the assumptions of the elastic calculation and one consequence
      of each. (§5)
- [ ] I can say why extraction has both a stabilising and a destabilising part.
      (§3.4)
- [ ] I can state what a Coulomb stress change is and is not evidence for. (§4)
