---
id: 06-04-07
title: "Focal Mechanisms from First Motions and Waveform Inversion"
level: graduate
prereqs: ["06-03-02", "06-02-01", "06-04-01"]
tags: [seismology, focal-mechanism, first-motion, moment-tensor, beachball]
---

# Focal Mechanisms from First Motions and Waveform Inversion

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the P-wave first-motion polarity from the moment tensor as the
   sign of $\mathbf{n}^{T}\mathbf{M}\mathbf{n}$, and explain why a single station
   supplies one bit.
2. **Construct** the double-couple moment tensor from strike, dip and rake, and
   **verify** it with the two defining properties: zero trace and eigenvalues
   $(+M_0, 0, -M_0)$.
3. **Explain** why $(s, d, r)$ and $(s \pm 180^\circ, 180^\circ - d, -r)$ name the
   same mechanism, and why a comparison of parameters can therefore report
   disagreement between two identical answers.
4. **Quantify** the non-uniqueness of a first-motion inversion: how many
   mechanisms reproduce a given polarity set exactly, and how far apart they are
   in tensor terms.
5. **Decompose** a moment tensor into isotropic, double-couple and CLVD parts,
   **verify** the decomposition by reconstruction, and state the interpretation
   caution that belongs with a large CLVD percentage.
6. **Compare** polarity-only inversion with waveform inversion and state what
   each can and cannot determine.

## Prerequisites

- [06-03-02 The Double-Couple Source and Radiation Patterns](../03-earthquake-sources/02-double-couple.md).
- [06-02-01 Eikonal Equation, Rays and Fermat's Principle](../02-ray-theory-and-travel-times/01-eikonal-and-rays.md).
- [01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md) —
  the geometry-dependent inversion and its misfit language.

## 1. Intuition: one bit per station

The first motion of a P wave is either up (compression) or down (dilatation). A
station therefore contributes **one bit**, and a network of $N$ stations
contributes $N$ bits, while a focal mechanism (restricted to a double couple) is
described by three continuous angles. Two consequences follow immediately, and
they are the whole content of this lesson.

- **Polarity data are coarse.** A mechanism that reproduces every sign is not
  unique; the demonstration finds 20 grid mechanisms that reproduce all 24
  polarities of a synthetic event *exactly*, with tensor differences up to
  0.171 in units of the largest eigenvalue.
- **The parameters are not the mechanism.** $(s, d, r)$ has a symmetry
  $(s, d, r) \leftrightarrow (s \pm 180^\circ, 180^\circ - d, -r)$, so the same
  physical mechanism can be printed with a strike differing by 180°.

None of this makes first-motion inversion useless; it makes it a *constraint*
that must be reported with its alternatives. Waveform inversion replaces each bit
with a real-valued residual and shrinks the admissible set, but it does not
abolish the geometry.

## 2. Definitions

### 2.1 The moment tensor and the P radiation

For a point source the far-field P-wave displacement is proportional to

$$
A_P(\mathbf{n}) = \mathbf{n}^{T}\mathbf{M}\,\mathbf{n}
= n_i M_{ij} n_j ,
$$

where $\mathbf{n}$ is the unit vector from the source to the station (the takeoff
direction) and $\mathbf{M}$ is the symmetric moment tensor. The first-motion
polarity is $\operatorname{sign}\big(\mathbf{n}^{T}\mathbf{M}\mathbf{n}\big)$:
positive for compression, negative for dilatation. This is the only relation the
polarity inversion needs, and it is worth deriving once rather than trusting.

A double couple with scalar moment $M_0$ has eigenvalues $(+M_0, 0, -M_0)$: the
$+M_0$ eigenvector is the **tension (T) axis**, the $-M_0$ eigenvector the
**pressure (P) axis**, and the $0$ eigenvector is the **null axis**, which is the
intersection of the two nodal planes.

### 2.2 Strike, dip, rake

A fault plane is described by its strike $\phi$, its dip $\delta$ and the rake
$\lambda$ of the slip vector in that plane. The moment tensor components in a
(north, east, up) system follow from these three angles; the convention used in
the demonstration is the standard one for a double couple, and its correctness is
checked in Section 4 rather than assumed.

## 3. Derivations

### 3.1 Why the polarity is the sign of a quadratic form

Write the far-field P displacement of a point source as
$u_i \propto (\lambda + 2\mu)^{-1}\,M_{jk}\,\partial_j\partial_k(\cdot)$, or
equivalently recall the standard result that for a ray leaving the source in
direction $\mathbf{n}$ the far-field P amplitude is

$$
u_P \propto \frac{1}{4\pi\rho v_p^{3}R}\,n_i M_{ij} n_j .
$$

The factor $n_i M_{ij} n_j$ is a scalar. It changes sign when the ray direction
crosses a nodal plane, where it vanishes; hence the two nodal planes are the set
of directions satisfying $\mathbf{n}^{T}\mathbf{M}\mathbf{n} = 0$, and the
pattern of compressions and dilatations on the focal sphere is a **beachball**
divided by those two planes. Everything the first-motion method measures is the
sign of that scalar, which is why a station sitting on or near a nodal plane is
useless: its amplitude is near zero and its sign is noise.

### 3.2 The moment tensor of a double couple, and the two checks

For strike $\phi$, dip $\delta$ and rake $\lambda$, the components used here are
the standard ones; for example

$$
M_{xx} = -M_0\left(\sin\delta\cos\lambda\sin2\phi
+ \sin2\delta\sin\lambda\sin^{2}\phi\right),
$$

$$
M_{yy} = M_0\left(\sin\delta\cos\lambda\sin2\phi
- \sin2\delta\sin\lambda\cos^{2}\phi\right),
\qquad
M_{zz} = M_0\sin2\delta\sin\lambda .
$$

Adding the first two,

$$
M_{xx} + M_{yy}
= -M_0\sin2\delta\sin\lambda\left(\sin^{2}\phi + \cos^{2}\phi\right)
= -M_0\sin2\delta\sin\lambda = -M_{zz} ,
$$

so the trace vanishes identically:

$$
\operatorname{tr}\mathbf{M} = M_{xx} + M_{yy} + M_{zz} = 0 .
$$

A zero trace is exactly the statement that the source creates no volume change.
The second check, that the eigenvalues are $(+M_0, 0, -M_0)$, follows from the
double-couple geometry. Both are verified numerically in the demonstration — the
printed trace is $0.0000\times10^{0}\ \mathrm{N\,m}$ and
$\sum_k|\lambda_k|/(2M_0) = 1.000000$.

### 3.3 The inversion as a misfit over a grid

For a candidate mechanism, the predicted polarity at station $i$ is
$\operatorname{sign}(\mathbf{n}_i^{T}\mathbf{M}\mathbf{n}_i)$, and the natural
misfit is the fraction of stations whose sign is wrong:

$$
\Phi(\phi, \delta, \lambda) = \frac{1}{N}\sum_{i=1}^{N}
\left[\operatorname{sign}\big(\mathbf{n}_i^{T}\mathbf{M}\mathbf{n}_i\big)
\neq \sigma_i\right] ,
$$

with $\sigma_i = \pm 1$ the observed polarity. This objective is *combinatorial*:
it is piecewise constant, so it has no gradient and the inversion is a search.
The admissible set is

$$
\mathcal{S} = \{\,(\phi, \delta, \lambda) : \Phi \le \Phi_{\min} + \epsilon\,\} ,
$$

and the honest answer to a first-motion inversion is the *set*, not its minimiser.
The demonstration reports both: 20 mechanisms with $\Phi = 0$ on exact data, and
16 mechanisms within 0.04 of the best on data with two flipped polarities.

### 3.4 Why two parameter triples describe one mechanism

A double couple is defined by its four nodalless directions: the P axis, the T
axis and the two null directions (the nodal-plane normals). The two null
directions are the normals of the two nodal planes, each of which is a valid
fault plane with a slip direction. Writing the mechanism with the *other* nodal
plane as the fault gives

$$
(\phi, \delta, \lambda)
\;\longleftrightarrow\;
(\phi \pm 180^\circ,\ 180^\circ - \delta,\ -\lambda) ,
$$

which is the same tensor. The demonstration verifies this for the synthetic
mechanism: $(225^\circ, 45^\circ, -90^\circ)$ and $(45^\circ, 135^\circ, 90^\circ)$
have a tensor difference of $3.14\times10^{-16}$ after normalising both to unit
moment, i.e. they are identical to round-off. Consequences:

- comparing two published mechanisms by the difference of their strike angles is
  meaningless unless the equivalence has been resolved;
- the comparison must use a tensor rotation angle (or any parameterisation-
  independent distance), as the demonstration does with
  $\max_{ij}|M^{(1)}_{ij} - M^{(2)}_{ij}|$ after normalisation.

### 3.5 The ISO/DC/CLVD decomposition

Every symmetric tensor splits uniquely into an isotropic part and a traceless
part, and every traceless symmetric tensor is a unique combination of two basis
tensors. In the eigenvector basis, with sorted eigenvalues $(d_1, d_2, d_3)$ and
$\sum_k d_k = 0$, write

$$
\mathbf{d} = a\,(1, 0, -1) + b\,(2, -1, -1) .
$$

Solving the three component equations gives $b = -d_2$ and $a = d_1 + 2d_2$,
which satisfies the third equation automatically because the sum is zero. The
first basis tensor is a **double couple**, the second a **compensated linear
vector dipole** (CLVD), and the isotropic part is $\operatorname{tr}\mathbf{M}/3$.
Reporting the three parts as percentages of the sum of Frobenius lengths,
$\sqrt{2}|a|$, $\sqrt{6}|b|$ and $\sqrt{3}|\operatorname{tr}\mathbf{M}|/3$, gives a
complete and reversible description: the demonstration's reconstruction error is
$1.83\times10^{-16}$ for a pure double couple and $7.18\times10^{-16}$ for a
mixed tensor.

The sign of the CLVD percentage records which eigenvector the CLVD part is
aligned with; the demonstration prints $-21.71\ \%$ for a test tensor built with
a positive CLVD contribution in a different orientation, which is the kind of
detail that is meaningless without the convention written down.

## 4. Worked examples

All numbers are printed by `code/focal_mechanisms_demo.py`. The synthetic event
has $M_0 = 3.5\times10^{17}\ \mathrm{N\,m}$, strike $225^\circ$, dip $45^\circ$,
rake $-90^\circ$ (so $M_w = 5.63$), recorded at 24 stations distributed uniformly
over the focal sphere.

### Example 1 — the tensor by hand

With $\phi = 225^\circ$ ($\sin2\phi = 1$, $\cos2\phi = 0$,
$\sin\phi = -0.7071$), $\delta = 45^\circ$
($\sin\delta = \cos\delta = 0.7071$, $\sin2\delta = 1$, $\cos2\delta = 0$) and
$\lambda = -90^\circ$ ($\sin\lambda = -1$, $\cos\lambda = 0$):

$$
M_{xx} = -M_0\left(0 + 1\cdot(-1)\cdot0.5\right) = +0.5M_0
= +1.7500\times10^{17}\ \mathrm{N\,m},
$$

$$
M_{yy} = M_0\left(0 - 1\cdot(-1)\cdot0.5\right) = +0.5M_0
= +1.7500\times10^{17}\ \mathrm{N\,m},
$$

$$
M_{zz} = M_0\cdot1\cdot(-1) = -M_0 = -3.5000\times10^{17}\ \mathrm{N\,m},
$$

$$
M_{xy} = M_0\left(0 + 0.5\cdot1\cdot(-1)\cdot1\right) = -0.5M_0
= -1.7500\times10^{17}\ \mathrm{N\,m},
$$

all of which match the printed tensor, and the trace is
$0.5M_0 + 0.5M_0 - M_0 = 0$ exactly. The printed $M_{xz}$ and $M_{yz}$ are
$-4.4238\times10^{1}$ and $-6.5669\times10^{1}\ \mathrm{N\,m}$ — not zero, but
$10^{-16}$ of $M_0$, because $\cos2\delta$ is $6.1\times10^{-17}$ in floating
point rather than exactly zero. **A near-zero component is not a measurement of
a small component**; it is round-off, and recognising that is part of using these
formulas correctly.

### Example 2 — polarities, and how little they say

At the 24 synthetic stations the first motions split 11 compression and 13
dilatation. Searching the grid of 72 strikes × 17 dips × 71 rakes = 86 904
mechanisms:

| quantity | value |
|---|---|
| grid-best mechanism | strike 45°, dip 40°, rake $-90^\circ$ |
| misfit of the grid best | 0.000 |
| misfit of the true mechanism (also on the grid) | 0.000 |
| grid mechanisms that reproduce all 24 polarities | 20 |
| tensor distance from the truth over that family | 0.000 to 0.171 (mean 0.101) |
| tensor distance of the grid best from the truth | 0.121 |

Two facts are visible at once. The grid best and the truth are **different
tensors** 0.121 apart in unit-moment terms, and both fit every polarity exactly;
and the true tensor itself appears in the family with distance 0.000. So the data
admit at least 20 mechanisms, one of which is right — and the data cannot say
which. Any single-mechanism answer from polarity data alone is a choice, not a
measurement.

### Example 3 — with two polarities wrong

Flipping 2 of the 24 polarities (8 per cent) gives a best misfit of 0.042
(1 station in 24) and a tensor distance from the truth of 0.1516 — worse than
the exact-data case but still small, because the inversion can satisfy one of the
flipped polarities by rotating slightly. Accepting every mechanism within 0.04 of
the best misfit gives a family of 16 mechanisms spanning tensor distances 0.1516
to 0.3745, with strikes from 55° to 240°, dips 40° to 55° and rakes $-135^\circ$
to $-55^\circ$.

### Example 4 — the cost of fewer stations

With 8 stations instead of 24, the best misfit rises to 0.125 (1 station in 8) and
the accepted family contains 3217 mechanisms — 3.7 per cent of the grid — with
tensor distances from the truth running from 0.0000 to 1.4809. In unit-moment
terms a distance of 1.48 is a *different mechanism*, not a refinement of the same
one. The lesson is quantitative: sparse networks do not give focal mechanisms,
they give constraints on them.

### Example 5 — the decomposition, checked by reconstruction

| tensor | ISO (%) | DC (%) | CLVD (%) | rebuild error |
|---|---|---|---|---|
| the synthetic double couple | $+0.00$ | $100.00$ | $-0.00$ | $1.83\times10^{-16}$ |
| $0.55\,\text{DC} + 0.30\,\text{CLVD} + 0.15\,\mathbf{I}$ | $+17.49$ | $60.79$ | $-21.71$ | $7.18\times10^{-16}$ |

The second row's input was deliberate, and its percentages are not the input
coefficients: percentages are Frobenius-length fractions, not the weights used to
build the tensor. The round-trip error shows the decomposition is complete and
reversible, which is what makes the three percentages a legitimate description of
a tensor — and nothing more than a description.

## 5. Assumptions and regime of validity

1. **A point source.** A source large compared with the station distance — a
   great earthquake seen regionally — has a mechanism that varies over the fault,
   and one beachball is then an average.
2. **Takeoff directions from a known velocity model.** $\mathbf{n}$ comes from the
   hypocentre and the 1-D model, so a wrong depth or model tilts the nodal planes
   and rotates the mechanism. This is the same dependency as in lesson
   [02](02-velocity-model-dependence.md), now acting on angles rather than
   kilometres.
3. **The first motion is the direct P.** A nodal station, a shallow event with a
   depth phase, or a converted arrival misidentified as P all corrupt the bits.
4. **The source is a double couple.** The polarity inversion *assumes* this, so
   it cannot detect a CLVD or isotropic component; those need waveform or
   amplitude data.
5. **The station distribution is adequate.** The demonstration uses a uniform
   focal-sphere coverage, which is the *best* case. A real network lies on one
   side of the focal sphere and clusters in azimuth, so real admissible sets are
   larger than the ones measured here.
6. **Errors are sign errors only.** Real polarity errors are concentrated near
   nodal planes, which biases the misfit in a way that uniform flipping does not
   represent.
7. **The equivalence rule is resolved.** Reporting $(s, d, r)$ without checking
   it against the alternative nodal plane invites false disagreement.

## 6. The demonstration

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python focal_mechanisms_demo.py
```

It builds the tensor from $(s, d, r)$ and checks the trace and the eigenvalues,
computes the polarities and their counts, runs the grid search with and without
flipped polarities, measures the admissible family with a parameter-free tensor
distance, repeats the experiment with 8 stations, and decomposes a pure and a
mixed tensor with a round-trip check.

Exercises:
[`exercises/07-focal-mechanisms-exercises.md`](exercises/07-focal-mechanisms-exercises.md)
and
[`exercises/07-focal-mechanisms-solutions.md`](exercises/07-focal-mechanisms-solutions.md).

> All models and data in this module are **SYNTHETIC**. The mechanism, the
> station distribution and the polarity errors are teaching values. The moment
> tensor formulas are standard and are verified numerically in the demonstration.

## Mastery checkpoint

Without notes:

1. Derive that the nodal planes are the directions with
   $\mathbf{n}^{T}\mathbf{M}\mathbf{n} = 0$.
2. Show from the component formulas that the trace vanishes.
3. Explain the equivalence $(s,d,r) \leftrightarrow (s\pm180^\circ, 180^\circ-d, -r)$
   and state the practical consequence for comparing mechanisms.
4. State how many mechanisms reproduced all 24 exact polarities and why the
   number is not one.
5. Derive $a = d_1 + 2d_2$ and $b = -d_2$ in the ISO/DC/CLVD split.
6. State two things a polarity inversion cannot determine that a waveform
   inversion can.

## Common pitfalls

1. **Reporting one beachball with no admissible set.** The data determine a set;
   quoting one member hides the uncertainty.
2. **Comparing mechanisms by strike difference.** The parameterisation is not
   unique, and a 180° difference can be agreement.
3. **Reading a near-zero tensor component as a real one.** With exact geometry
   those components are round-off at the $10^{-16}$ level of $M_0$.
4. **Trusting polarities near nodal planes.** The amplitude vanishes there and
   the sign is noise.
5. **Interpreting a large CLVD as a physical source.** It is far more often a
   velocity-model, location or noise artefact.
6. **Forgetting that the inversion assumed a double couple.** It cannot find
   what it has excluded from the search.

## Related modules

- [06-03-02 The Double-Couple Source and Radiation Patterns](../03-earthquake-sources/02-double-couple.md).
- [06-03-03 Moment Tensors, Decomposition and Physical Meaning](../03-earthquake-sources/03-moment-tensors.md).
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  where mechanisms feed stress-transfer calculations.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of admissible sets behind Section 3.3.
