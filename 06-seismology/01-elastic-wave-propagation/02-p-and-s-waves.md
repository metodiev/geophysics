---
id: 06-01-02
title: "P and S Waves: Particle Motion, Speeds and Polarisation"
level: advanced
prereqs: ["06-01-01", "02-04-04"]
tags: [seismology, p-wave, s-wave, polarisation, wave-speeds, vp-vs-ratio]
---

# P and S Waves: Particle Motion, Speeds and Polarisation

Lesson [06-01-01](./01-wave-equation-elastic.md) produced two wave equations.
This lesson asks what the two solutions look like: which way the particles move,
how the two speeds are related to one another and to the moduli, what bounds
hold on the ratio, and how a seismologist tells the two apart in a real record.

```
.venv/bin/python 06-seismology/01-elastic-wave-propagation/code/p_s_waves_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** the vector wave equation into scalar and vector potentials and
   **classify** solutions as P (curl-free) and S (divergence-free).
2. **Derive** the polarisation of each mode from the plane-wave ansatz and
   **explain** why S motion has two orthogonal polarisation directions, giving
   SV and SH.
3. **Derive** $v_p/v_s=\sqrt{2+\lambda/\mu}=\sqrt{K/\mu+4/3}=
   \sqrt{2(1-\nu)/(1-2\nu)}$ and **state** which bounds follow from which
   assumption about the moduli.
4. **Distinguish** the observable consequences of $v_p/v_s$ lying near
   $\sqrt2$, near $\sqrt3$ and far above both.
5. **Measure** polarisation from a synthetic three-component record by
   covariance analysis, and state what the measurement can and cannot decide.

## Prerequisites

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic
  Equation](./01-wave-equation-elastic.md) — equations (12), (17), (18) and
  (19) are used throughout.
- [02-04-04 Young's Modulus, Poisson's Ratio and the Elastic
  Constants](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  — the conversion table between modulus pairs.
- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase
  Velocity](../../02-physics/03-oscillations-and-waves/04-wave-basics.md) —
  phase velocity, wavelength and the meaning of a plane wave.

## 1. Intuition: two ways for a rock to move

Push a rock and it has two choices. It can compress the material ahead of the
push — particles move *along* the direction of travel — or it can slide the
material sideways out of the way — particles move *across* the direction of
travel. The first needs resistance to volume change; the second needs resistance
to shear. Because both resistances exist, both motions propagate, at different
speeds, and they do not mix in a homogeneous medium.

The single most useful mental picture: **P motion is like a queue of people
shuffling forward and back along the line; S motion is like a wave travelling
down a rope that is being shaken sideways.** The P queue needs people to be
willing to be pushed closer together (a bulk modulus); the rope needs to be
stiff against sideways displacement (a shear modulus).

## 2. Precise definitions

### 2.1 Scalar and vector potentials

With the Helmholtz decomposition (see
[06-01-05](./05-wavefield-potentials.md)) written as
$\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi$, the two potentials
satisfy the decoupled equations derived in
[06-01-01](./01-wave-equation-elastic.md):

$$\ddot\phi = v_p^2\nabla^2\phi, \qquad
\ddot{\boldsymbol\psi} = v_s^2\nabla^2\boldsymbol\psi, \qquad
\nabla\cdot\boldsymbol\psi=0. \tag{1}$$

- **P wave**: $\phi\ne0$, $\boldsymbol\psi=0$. Then
  $\nabla\times\mathbf u = 0$ (**irrotational**) and
  $\nabla\cdot\mathbf u=\nabla^2\phi\ne0$ (**dilatational**).
- **S wave**: $\boldsymbol\psi\ne0$, $\phi=0$. Then
  $\nabla\cdot\mathbf u = 0$ (**equivoluminal**) and
  $\nabla\times\mathbf u = -\nabla^2\boldsymbol\psi\ne0$ (**rotational**).

The two descriptions — "irrotational/dilatational" and
"equivoluminal/rotational" — are the operational definitions. They are
verifiable by differentiation, which is exactly what §6 does.

### 2.2 Plane waves and polarisation

A **plane wave** is a solution of the form

$$\mathbf u(\mathbf x,t) = \mathbf a\,f\!\left(\mathbf n\cdot\mathbf x - ct\right),
\tag{2}$$

where $\mathbf n$ is the unit **propagation direction**, $c$ the **phase
velocity** and $\mathbf a$ the **polarisation vector**, the direction the
particles move. Substituting (2) into (12) of
[06-01-01](./01-wave-equation-elastic.md) with $f$ having a nonzero second
derivative forces, for every direction $\mathbf n$,

$$\rho c^2\,\mathbf a = (\lambda+\mu)(\mathbf n\cdot\mathbf a)\mathbf n
+ \mu\,\mathbf a. \tag{3}$$

Equation (3) is an eigenvalue problem for `a` with eigenvalue $\rho c^2$. It has
**two distinct solutions**, and their polarisations are what distinguishes P
from S. Deriving the polarisation from (3) rather than asserting it is the point
of §3.

### 2.3 SV and SH

Any S polarisation is perpendicular to $\mathbf n$; the plane perpendicular to
$\mathbf n$ is two-dimensional, so there are two independent S polarisations at
every direction. Conventionally they are split into:

- **SH**: polarised horizontally, i.e. $\mathbf a$ has no vertical component;
- **SV**: polarised in the vertical plane that contains $\mathbf n$.

The split is not arbitrary. In a horizontally layered Earth, SH and SV **decouple
completely**: SH sees only the horizontal shear modulus at each interface, while
SV couples to P at every interface. This is why SH is the mode of choice for
measuring shear anisotropy, and why SV and P must be modelled together in
reflection seismology.

## 3. Derivation of the polarisations

**Step 1 — dot (3) with $\mathbf n$.** Writing
$(\mathbf n\cdot\mathbf a)=a_\parallel$ for the longitudinal component,

$$\rho c^2 a_\parallel = (\lambda+\mu)a_\parallel + \mu a_\parallel
= (\lambda+2\mu)a_\parallel. \tag{4}$$

**Step 2 — read off the first solution.** Equation (4) has the solution
$a_\parallel\ne0$ with

$$c^2 = \frac{\lambda+2\mu}{\rho} \equiv v_p^2, \qquad
\mathbf a \parallel \mathbf n. \tag{5}$$

Polarisation along the propagation direction: a **P wave**.

**Step 3 — look for a transverse solution.** Now require
$a_\parallel = 0$. Equation (3) becomes

$$\rho c^2\mathbf a_\perp = \mu\,\mathbf a_\perp
\quad\Longrightarrow\quad c^2 = \frac{\mu}{\rho}\equiv v_s^2, \qquad
\mathbf a\perp\mathbf n. \tag{6}$$

Any vector perpendicular to $\mathbf n$ solves it, so the S polarisation is
two-dimensional and **degenerate**: both S polarisations travel at the same
speed in an isotropic medium. That degeneracy is broken by anisotropy, which is
the subject of [06-01-08](./08-anisotropic-propagation.md).

**Step 4 — confirm the divergence and curl statements.** For a P plane wave
$\mathbf u = a_\parallel\mathbf n\,f(\mathbf n\cdot\mathbf x - ct)$:
$\nabla\cdot\mathbf u = a_\parallel f''$ (nonzero) and
$\nabla\times\mathbf u = a_\parallel\,(\nabla f)\times\mathbf n = 0$ because
$\nabla f$ is parallel to $\mathbf n$. For S, $\nabla\cdot\mathbf u=0$ because
$\mathbf a\perp\mathbf n$, and $\nabla\times\mathbf u\ne0$ in general. The
algebra matches the words of §2.1.

## 4. The ratio $v_p/v_s$

Dividing (5) by (6):

$$\frac{v_p}{v_s} = \sqrt{\frac{\lambda+2\mu}{\mu}} = \sqrt{2+\frac{\lambda}{\mu}}.
\tag{7}$$

Three equivalent forms follow from the modulus identities of
[02-04-04](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md);
each is worth deriving once.

**From $K$ and $\mu$.** With $K=\lambda+\tfrac23\mu$,

$$\lambda+2\mu = K+\tfrac43\mu
\;\Longrightarrow\;
\frac{v_p}{v_s}=\sqrt{\frac{K}{\mu}+\frac43}. \tag{8}$$

**From $\nu$.** Poisson's ratio is $\nu=\lambda/\big(2(\lambda+\mu)\big)$, so
$\lambda/\mu = 2\nu/(1-2\nu)$ and

$$\frac{v_p}{v_s} = \sqrt{2+\frac{2\nu}{1-2\nu}}
= \sqrt{\frac{2(1-\nu)}{1-2\nu}}. \tag{9}$$

**The bounds, and the assumption each needs.** Equation (7) is the sharpest
form, because it involves only one ratio:

- if $\lambda\ge0$ then $v_p/v_s\ge\sqrt2 = 1.414214$;
- if $K\ge0$, which is the weaker requirement
  $\lambda\ge-\tfrac23\mu$, then (8) gives
  $v_p/v_s\ge2/\sqrt3 = 1.154701$;
- if $\lambda=\mu$ (Poisson solid, $\nu=1/4$) then $v_p/v_s=\sqrt3=1.732051$;
- as $\lambda/\mu\to\infty$ the ratio diverges; as $\lambda/\mu\to0$ it tends to
  $\sqrt2$ from above.

**A negative $\lambda$ is physically admissible**, which is why the two bounds
differ. $\lambda = -\tfrac23\mu$ corresponds to $K=0$: a material that resists
shear but not volume change. Such a material is a mathematical limit rather than
a rock, but the bound it produces is the correct one for the weaker assumption,
and conflating the two bounds is a common error.

## 5. Physical interpretation

- **Why is $v_p > v_s$ always?** Because $\lambda+2\mu>\mu$ whenever
  $\lambda+2\mu>0$, i.e. whenever $K+\tfrac43\mu>0$. The P mode draws on both
  the bulk and shear resistance; the S mode draws on shear alone. The first
  arrival at any receiver is therefore almost always a P wave, which is why
  early warning systems count on it.
- **Why can $v_s$ be very small?** In a fluid or a very soft material $\mu\to0$
  and $v_s\to0$. A large $v_p/v_s$ therefore means low shear stiffness — not
  high P stiffness.
- **Why does the ratio matter?** It is a rock property that is insensitive to
  porosity alone but sensitive to the *fluid* and to the *frame*. A gas-filled
  rock has a low $v_p$ at nearly constant $v_s$, so a low $v_p/v_s$ indicates gas.
  This follows from equations (7)–(9) plus Gassmann substitution
  ([05-04-03](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md)),
  not from a look-up table.

## 6. Units and dimensional analysis

With $[\lambda]=[\mu]=\mathrm{Pa}=\mathrm{kg\,m^{-1}\,s^{-2}}$ and
$[\rho]=\mathrm{kg\,m^{-3}}$:

$$\left[\frac{\lambda+2\mu}{\rho}\right] =
\frac{\mathrm{kg\,m^{-1}\,s^{-2}}}{\mathrm{kg\,m^{-3}}}
= \mathrm{m^2\,s^{-2}} \;\Rightarrow\; [v_p] = \mathrm{m\,s^{-1}}.$$

The ratio (7) is the square root of a ratio of two moduli: dimensionless, as a
ratio of speeds must be. The polarisation vector $\mathbf a$ in (2)–(3) is a unit
vector and carries no units; the amplitude $f$ carries the units of displacement.

## 7. Worked examples

### 7.1 The ratio for four SYNTHETIC materials

All four rows below are computed from the moduli stated in the first three
columns; nothing is quoted.

| material | $\lambda$ (GPa) | $\mu$ (GPa) | $\rho$ (kg/m³) | $v_p$ (m/s) | $v_s$ (m/s) | $v_p/v_s$ |
|---|---|---|---|---|---|---|
| base model | 25 | 30 | 2700 | 5610.84 | 3333.33 | 1.683251 |
| Poisson solid | 30 | 30 | 2600 | 5883.48 | 3396.83 | 1.732051 |
| stiff, $\lambda\gg\mu$ | 200 | 10 | 3000 | 8563.49 | 1825.74 | 4.690416 |
| $\mu\to0$ limit | 20 | 0.05 | 1000 | 4483.30 | 223.61 | 20.049938 |

For each row the three routes (7), (8) and (9) agree to at least seven
significant figures; the demonstration prints all three columns side by side.

### 7.2 The bounds, swept

**Sweep A**: fix $\lambda=25$ GPa and let $\mu$ run from 0.01 to 60 GPa. The
ratio falls monotonically from 50.019996 ($\mu=0.01$ GPa) to 1.554563
($\mu=60$ GPa) and approaches $\sqrt2=1.414214$ as $\mu\to\infty$ without
reaching it on any finite sweep.

**Sweep B**: fix $\mu=30$ GPa and let $\lambda$ run over its admissible range
from $-20$ GPa (where $K=0$) to 200 GPa. The ratio rises from
$2/\sqrt3=1.154701$, through $\sqrt2=1.414214$ at $\lambda=0$, to 2.943920 at
$\lambda=200$ GPa. **The smallest ratio the model admits is $2/\sqrt3$, and it
requires $K=0$, i.e. a negative $\lambda$.** If you also insist on $\lambda\ge0$
the floor is $\sqrt2$.

### 7.3 Arithmetic by hand

For the base model, $\lambda/\mu = 25/30 = 0.833333$ and
$\sqrt{2+0.833333} = \sqrt{2.833333} = 1.683251$. Equivalently
$K = 25+\tfrac23(30) = 45$ GPa, so
$\sqrt{K/\mu+4/3} = \sqrt{1.5+1.333333} = \sqrt{2.833333}$, the same.
And $\nu = 25/(2\cdot55) = 0.2272727$, so
$\sqrt{2(1-0.2272727)/(1-0.4545455)} = \sqrt{1.5454545/0.5454545} = \sqrt{2.833333}$.
Three formulas, one number: the workbook is closed.

## 8. The Python demonstration

`p_s_waves_demo.py` has three parts.

**Part 1 — the ratio by three routes.** The table of §7.1, with all three
formulas evaluated for each row, and the two sweeps of §7.2. This is the
arithmetic check.

**Part 2 — divergence and curl, measured.** A synthetic displacement field is
built from $\partial_i\phi$ only (P) and from the curl of a vector potential only
(S) on a $128^3$ periodic grid, and the two diagnostics are evaluated by
central differences:

| field | angle between $\mathbf u$ and $\mathbf k$ | $\lVert\nabla\cdot\mathbf u\rVert_{\rm rms}$ (normalised) | $\lVert\nabla\times\mathbf u\rVert_{\rm rms}$ (normalised) | ratio |
|---|---|---|---|---|
| P | $0.0000°$ | 1.712518 | 0.010302 | $1.66\times10^{2}$ |
| S | $90.0000°$ | 0.004622 | 0.988773 | $4.68\times10^{-3}$ |

The leakage in the small column is second-order truncation of the central
differences, not physics. The measured statement is that the P field has **166
times** more divergence than curl and the S field **214 times** more curl than
divergence, on a grid where the theoretical values are $\infty$ and $0$.

**Part 3 — polarisation from a synthetic three-component record.** Three
in-memory ObsPy `Trace` objects (100 Hz, 400 samples, 3-component station
"SYN") are built for three injected polarisations, with seeded Gaussian noise at
2 per cent of the peak (seed 20261014). The principal eigenvector of the
$3\times3$ covariance matrix recovers:

| injected case | injected (E,N,Z) | recovered (E,N,Z) | angle error |
|---|---|---|---|
| P, steep incidence | (+0.200, +0.100, +0.975) | (+0.196, +0.106, +0.975) | 0.42° |
| S (SV), steep | (+0.980, 0.000, −0.201) | (+0.983, −0.002, −0.184) | 0.98° |
| S (SH), horizontal | (0.000, +1.000, 0.000) | (+0.001, +1.000, −0.002) | 0.14° |

The recovery is limited by the injected noise, which is the honest statement:
polarisation analysis inherits the noise level of the record. **What the method
cannot do** is distinguish a P arrival from an S arrival without an assumption
about the ray direction: the covariance gives a direction, and labelling it
requires knowing where the wave came from.

## 9. Exercises

**★1.** Derive equation (3) by substituting (2) into the Navier–Cauchy equation.
State which term of the Navier–Cauchy equation becomes
$(\lambda+\mu)(\mathbf n\cdot\mathbf a)\mathbf n$ and which becomes
$\mu\mathbf a$.

**★2.** For a material with $\lambda=18$ GPa, $\mu=24$ GPa, $\rho=2400\
\mathrm{kg\,m^{-3}}$, compute $v_p$, $v_s$, $v_p/v_s$, $K$, $\nu$ and $E$, and
verify (7), (8) and (9) numerically.

**★3.** Show that $\mathbf u = \mathbf a\,f(\mathbf n\cdot\mathbf x - ct)$ with
$\mathbf a\perp\mathbf n$ has $\nabla\cdot\mathbf u=0$. Then show that the same
field has $\nabla\times\mathbf u\ne0$ unless $f$ is constant.

**★4.** State the two bounds on $v_p/v_s$ and the assumption each requires.

**★★5.** A three-component record gives a principal polarisation direction of
$(0.30, 0.10, 0.95)$ and the station is 40 km from the source. Compute the
apparent incidence angle at the surface and state whether the arrival is more
likely to be P or S. What additional information would settle it?

**★★6.** Run `p_s_waves_demo.py` and edit the noise level from 0.02 to 0.10.
Report the new angle errors and state the trend. Then state how many samples
would be needed to hold the angle error fixed as the noise rises by the same
factor.

**★★7.** Show that $v_p/v_s = \sqrt{2}$ requires $\lambda=0$ and hence
$K = \tfrac23\mu$. Compute what fraction of a rock's P stiffness would then come
from its shear resistance.

**★★★8.** A rock is fully saturated with a fluid of bulk modulus $K_f$ and
zero shear modulus. Using
[05-04-03](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md),
show that $v_s$ depends on the fluid only through $\rho$, and hence that a
$v_p/v_s$ anomaly can distinguish a fluid change from a lithology change, but
only if the density is constrained independently.

**★★★9.** In a VTI medium the two S polarisations travel at different speeds
and their polarisations are not perpendicular to $\mathbf n$ in the usual sense.
Read [06-01-08](./08-anisotropic-propagation.md) §4, and state precisely which
of the statements in §2.3 above survive.

## 10. Common mistakes

1. **Saying "S waves have no compression".** A pure S wave has
   $\nabla\cdot\mathbf u=0$, i.e. no *volume* change. The strain tensor of a
   shear wave has nonzero diagonal components in general; what vanishes is the
   trace, not the deformation.
2. **Writing $v_p=\sqrt{\lambda/\rho}$.** The $\lambda$ that enters is
   $\lambda+2\mu$.
3. **Confusing the two lower bounds on $v_p/v_s$.** $2/\sqrt3$ needs only
   $K\ge0$; $\sqrt2$ needs $\lambda\ge0$.
4. **Believing "SV" and "SH" are physical modes in an isotropic medium.** They
   are bookkeeping: the S polarisation is degenerate and any orthogonal pair
   works. They become physically distinct when layering or anisotropy breaks
   the symmetry.
5. **Inferring the polarisation of an arrival from a compressional-arrival
   position.** Polarisation analysis and arrival-time analysis are independent
   evidence; using one to define the other is circular.
6. **Assuming the ratio is a constant of the Earth.** It ranges from about
   $1.15$ (the $K=0$ limit, not a rock) to more than 20 (a soft, water-saturated
   sediment), and this is a *derived* range, from (7).

## 11. Real-world applications

- **Earthquake early warning.** Because $v_p>v_s$ always, the first P arrival
  precedes the damaging S motion by $\Delta(1/v_s-1/v_p)$, which for a
  $v_p/v_s$ of 1.73 and a 50 km epicentral distance is seconds — derived from
  (7), not assumed.
- **Lithology and fluid discrimination.** $v_p/v_s$ separates sand from shale
  and gas from brine in reservoir seismology, and the mechanism is in §5 and
  §7.1.
- **Shear-wave splitting.** A polarised S wave entering an anisotropic rock
  splits into two arrivals with orthogonal polarisations; the delay is a
  measure of anisotropy. This is the observational basis of
  [06-01-08](./08-anisotropic-propagation.md).
- **The liquid outer core.** With $\mu=0$ in a fluid, $v_s=0$ and no S wave can
  propagate; the observation that S waves do not appear beyond a certain
  distance is the classical evidence for a liquid core.
- **Site characterisation.** $v_s$ in the top 30 m controls ground-motion
  amplification, and it is measured directly by the S-wave methods whose
  physics is equations (5)–(6).

## 12. Further reading

- [02-04-04 Elastic
  Moduli](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  — every conversion used in §4, derived rather than tabulated.
- [02-04-05 Elastodynamic Equation of Motion and Wave
  Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the companion derivation, with a worked Gassmann example.
- [05-04-01 Porosity, Density and Velocity
  Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md)
  — why real rocks do not sit on the $\sqrt3$ line.
- [03-10-07 Cross-Correlation, Polarisation and Array
  Processing](../../03-scientific-computing/10-obspy-and-seismic-data/07-obspy-advanced.md)
  — the ObsPy tools for the operation performed in §8.
- [https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html](https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html)
  — the `Trace` object used to build the synthetic three-component record.

## 13. Related lessons

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic
  Equation](./01-wave-equation-elastic.md) — where (1) comes from.
- [06-01-05 Helmholtz Decomposition and Wavefield
  Potentials](./05-wavefield-potentials.md) — the decomposition in full.
- [06-01-08 Wave Propagation in Anisotropic
  Media](./08-anisotropic-propagation.md) — where the S degeneracy is lifted.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time
  Curve](../02-ray-theory-and-travel-times/02-snell-and-layering.md) — how the
  two speeds separate in time at a distance.

## 14. Self-assessment

- [ ] Derive (3) from the Navier–Cauchy equation in two lines.
- [ ] Write the P and S polarisation conditions and the divergence/curl
      statement each implies.
- [ ] Derive (7), (8) and (9) from one another.
- [ ] State both lower bounds on $v_p/v_s$ with the assumption each needs.
- [ ] Compute $v_p$, $v_s$ and the ratio for a modulus triple of your own
      choosing, three ways, and get the same number.
- [ ] Explain why a fluid transmits no S wave using the equation, not the word
      "fluid".
- [ ] Describe what the covariance polarisation measurement determines and what
      it needs from outside to be interpretable.
- [ ] Name one observation that would falsify "$\lambda\ge0$ in crustal rocks".
