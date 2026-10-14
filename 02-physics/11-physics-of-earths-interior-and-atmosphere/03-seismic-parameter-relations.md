---
id: 02-11-03
title: "Seismic Velocities, Elastic Moduli and Mineralogy"
level: graduate
prereqs: ["02-04-04", "02-11-01", "02-05-07"]
estimated_minutes: 90
tags: [seismic-velocities, elastic-moduli, poisson-ratio, mantle-discontinuities]
---

# Seismic Velocities, Elastic Moduli and Mineralogy

A seismogram is a pressure record. Everything the Earth's interior is known to
be composed of has been inferred from such records, and the chain of reasoning
that gets from a wiggle on a drum to the statement "the outer core is liquid
iron alloy" has four links:

1. **Travel times and waveforms give $v_p(r)$ and $v_s(r)$**, by
   elastodynamics — the forward problem of seismology
   ([06-seismology](../../06-seismology/README.md)).
2. **The wave speeds give the moduli**, through
   $$v_p = \sqrt{\frac{K+\tfrac{4}{3}\mu}{\rho}}, \qquad v_s = \sqrt{\frac{\mu}{\rho}},$$
   which is the subject of §1–§2 of this lesson.
3. **Density comes from somewhere else** — free oscillations, the moment of
   inertia, or a mineral-physics equation of state. Speeds alone cannot supply
   it, and §3 shows exactly why, with numbers.
4. **Mineral physics supplies the moduli of candidate assemblages** at the same
   pressure and temperature, and the comparison either works or does not. §4
   and §5 are about what that comparison has produced: the 410 km and 660 km
   discontinuities, the liquid outer core, and the solid inner core.

The single sentence that summarises the whole method is this: **what makes the
inference possible is not that velocity correlates with density, but that one
specific combination of the two velocities — $\phi = v_p^2-\tfrac43v_s^2$ —
equals $K/\rho$, which is the inverse compressibility per unit mass.** That is an
identity of elastodynamics, not an empirical trend. Lesson
[02](./02-equations-of-state.md) §3 derived the consequences; this lesson
confronts them with the observations.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $v_p$ and $v_s$ from the elastodynamic equations for an isotropic
   solid, and identify which modulus each one measures.
2. **Invert** the two relations for $K$, $\mu$ and Poisson's ratio, and state
   the exact relation $K/\mu = (v_p/v_s)^2-\tfrac43$.
3. **Demonstrate**, with numbers, that $(v_p,v_s)$ alone does not determine
   $\rho$, and explain what additional information breaks the degeneracy.
4. **Fit** Birch's law to a set of velocity–density pairs, report the residuals,
   and explain why it must not be extrapolated across the core–mantle boundary.
5. **Compute** normal-incidence reflection coefficients from acoustic impedance
   at the Moho, the 410 km discontinuity, the core–mantle boundary and the
   inner-core boundary, and explain why the CMB is a *weak* P reflector.
6. **Explain** why $v_s = 0$ in the outer core follows from $\mu = 0$, and
   describe the observational signature that established it.
7. **Connect** the 410 km and 660 km discontinuities to specific mineral phase
   changes and to their Clapeyron slopes' signs.

## Prerequisites

- [02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants](../04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  — the elastic constants and their interrelations.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the reference model, the density jumps, and the seismic parameter.
- [02-05-07 Thermodynamic Phase Equilibria and Mantle Mineralogy](../05-thermodynamics/07-phase-equilibria.md)
  — Clapeyron slopes and why the mantle has discontinuities.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the derivation of equations (1) and (2) in full.

## 1. The two body waves and the two moduli

### 1.1 Where the two speeds come from

For a homogeneous, isotropic, linearly elastic solid of density $\rho$, bulk
modulus $K$ and shear modulus $\mu$, the elastodynamic equation of motion
admits exactly two body-wave solutions. Writing the displacement as the sum of a
curl-free part and a divergence-free part — the Helmholtz decomposition — the two
parts decouple and propagate independently:

$$v_p = \sqrt{\frac{K+\tfrac{4}{3}\mu}{\rho}} \qquad (1)$$

$$v_s = \sqrt{\frac{\mu}{\rho}}. \qquad (2)$$

The derivation is in
[02-04-05](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md); what
matters here is the structure.

**$v_s$ measures shear alone.** It depends on $\mu$ and $\rho$ and on nothing
else. Nothing in equation (2) involves $K$; a material can be arbitrarily
incompressible and still transmit shear waves slowly if $\mu$ is small. This is
why $v_s$ is a direct measurement of the shear modulus.

**$v_p$ mixes the two moduli**, and mixes them in a way that cannot be undone
without $v_s$. The combination $K + \tfrac43\mu$ has its own name — the *P-wave
modulus*, sometimes written $M$ — and a measurement of $v_p$ alone gives only
$M/\rho$.

**Together they separate the moduli**, which is the reason seismology measures
both. Two equations, two unknowns given $\rho$: that is the entire content of §2.

### 1.2 The elastic constant that is not there

Notice what is absent: the Lamé parameter $\lambda$. It appears in the usual
form $v_p = \sqrt{(\lambda+2\mu)/\rho}$, and since
$K = \lambda + \tfrac23\mu$, the two forms are identical. Writing the relation in
terms of $K$ and $\mu$ rather than $\lambda$ and $\mu$ is a deliberate choice: $K$
is what an equation of state predicts and what high-pressure experiments measure,
while $\lambda$ is not measured by any independent experiment at all. Deep-Earth
work is almost always done in $(K,\mu)$.

## 2. Inverting for $K$, $\mu$ and Poisson's ratio

### 2.1 The inversion

Given $\rho$, $v_p$ and $v_s$:

$$\mu = \rho v_s^2, \qquad K = \rho\left(v_p^2 - \tfrac43 v_s^2\right),
\qquad \phi = \frac{K}{\rho} = v_p^2 - \tfrac43 v_s^2. \qquad (3)$$

Applying equation (3) to the handbook's rounded velocity and density anchors
(lesson [01](./01-pressure-density-depth.md) §3.1) gives:

| Layer | $\rho$ (kg/m³) | $v_p$ (km/s) | $v_s$ (km/s) | $K$ (GPa) | $\mu$ (GPa) | $K/\mu$ | $\nu$ | $\phi$ (km² s⁻²) |
|---|---|---|---|---|---|---|---|---|
| Crust | 2750 | 6.15 | 3.45 | 60.4 | 32.7 | 1.84 | 0.270 | 21.95 |
| Upper mantle | 3300 | 8.10 | 4.50 | 127.4 | 66.8 | 1.91 | 0.277 | 38.61 |
| Transition zone | 4000 | 9.70 | 5.30 | 226.5 | 112.4 | 2.02 | 0.287 | 56.64 |
| Lower mantle | 4985 | 12.00 | 6.45 | 441.3 | 207.4 | 2.13 | 0.297 | 88.53 |
| Outer core | 11050 | 9.15 | 0.00 | 925.1 | 0.0 | — | 0.500 | 83.72 |
| Inner core | 12950 | 11.15 | 3.60 | 1386.2 | 167.8 | 8.26 | 0.442 | 107.04 |

Read down the $K$ column: **$K$ rises by a factor of 23** from crust to inner
core. Read down the $\mu$ column: **$\mu$ rises by a factor of 5** and then
vanishes. The two moduli do not rise together, and that difference is
information.

### 2.2 $K/\mu$ and Poisson's ratio

Two mutually consistent ways to express the ratio.

From equations (1)–(2), dividing:

$$\left(\frac{v_p}{v_s}\right)^2 = \frac{K+\tfrac43\mu}{\mu}
= \frac{K}{\mu} + \frac{4}{3}
\quad\Longrightarrow\quad
\frac{K}{\mu} = \left(\frac{v_p}{v_s}\right)^2 - \frac{4}{3}. \qquad (4)$$

So a $v_p/v_s$ ratio *is* a $K/\mu$ ratio. Check it on the crust: $(6.15/3.45)^2
= 3.179$, and $3.179 - 1.333 = 1.846$, against 1.84 in the table ✓.

Poisson's ratio follows from

$$\nu = \frac{v_p^2 - 2v_s^2}{2\left(v_p^2 - v_s^2\right)}
= \frac{3K/\mu - 2}{2\left(3K/\mu + 1\right)}
= \frac{\tfrac{3}{2}K/\mu - 1}{3K/\mu + 1}. \qquad (5)$$

Again the crust: $K/\mu = 1.846 \to (2.769-1)/(5.538+1) = 0.271$ ✓, and the
consistency of the two forms is a useful self-check.

The two limits worth memorising:

- **$\nu = 0.25$ and $v_p/v_s = \sqrt{3} = 1.732$** is the *Poisson solid*,
  with $\lambda = \mu$ and $K/\mu = 5/3$. It is the value for a material whose
  energy goes equally into volume change and shape change.
- **$\nu \to 0.5$ and $v_p/v_s \to \infty$** as $\mu/K \to 0$: a fluid. The
  outer core's row, with $\nu$ reported as 0.500, is the statement
  $\mu = 0$; the value 0.5 is not so much a measurement as a limit, and it is the
  reason a liquid cannot transmit shear.

The mantle's $\nu$ climbs slowly from 0.270 to 0.297 — a *very* weak trend. The
inner core then jumps to 0.442, which is unusually high: relative to its
resistance to compression, the inner core resists shear poorly. That is a real
and diagnostic property, and it is why $v_p/v_s$ inside the inner core is near 3
rather than near 1.8. It follows from the same physics that gives iron a high
$K_0'$ in lesson [02](./02-equations-of-state.md) §2.3.

## 3. The density–velocity ambiguity

### 3.1 The degeneracy, demonstrated

Take one velocity pair, $v_p = 9.15$ km/s and $v_s = 5.00$ km/s, and three
densities:

| $\rho$ (kg/m³) | $K$ (GPa) | $\mu$ (GPa) | $\phi$ (km² s⁻²) |
|---|---|---|---|
| 4000 | 201.6 | 100.0 | 50.39 |
| 6000 | 302.3 | 150.0 | 50.39 |
| 9900 | 498.9 | 247.5 | 50.39 |

**Every entry in the $\phi$ column is identical, because $\phi$ depends only on
the velocities.** Multiplying $\rho$ by a factor multiplies both $K$ and $\mu$ by
the same factor and leaves $v_p$ and $v_s$ untouched. There is no way to tell,
from a seismogram alone, whether you are looking at a stiff light material or a
soft heavy one.

This is not a subtlety of the arithmetic; it is the fundamental non-uniqueness of
seismic composition inference, and it is worth stating plainly: **velocity is one
number per mode, density is another, and seismology measures the first two.**
Only the combination $K/\rho$ is observed.

### 3.2 What breaks the degeneracy

Four independent sources of density, in roughly descending order of precision:

- **Free oscillations.** The Earth's normal modes depend on the density
  distribution through integrals weighted by the mode shapes, so a sufficiently
  large set of observed mode frequencies constrains $\rho(r)$ — this is how PREM
  was constructed (see
  [12-global-geophysics-interior/01-01](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/01-prem-and-reference-models.md)).
- **Mass and moment of inertia.** Two integral constraints, coarse but
  independent, as used in lesson [01](./01-pressure-density-depth.md) §3.4.
- **Mineral physics.** An equation of state supplies $\rho(P,T)$ for a candidate
  composition, converting the question from "what is the density?" to "which
  composition gives this density?".
- **Laboratory elasticity.** Once the density is *assumed* from a candidate
  composition, mineral physics predicts $K$ and $\mu$, and the test becomes
  whether the predicted $v_p$ and $v_s$ match.

### 3.3 Birch's law: the empirical version, and its limits

Birch observed that within a family of rocks of similar mean atomic weight,
$v_p$ is nearly linear in $\rho$. Fitting that to the four silicate anchors in
the table of §2.1:

$$v_p\ (\text{km/s}) = -0.6258 + 2.5576\,\rho\ (\text{g/cm}^3),$$

with $r^2 = 0.99064$ over the four silicates, and residuals

| Layer | $\rho$ | $v_p$ observed | $v_p$ from the fit | Residual | Residual % |
|---|---|---|---|---|---|
| Crust | 2750 | 6.15 | 6.41 | $-0.26$ | $-4.19$ |
| Upper mantle | 3300 | 8.10 | 7.81 | $+0.29$ | $+3.53$ |
| Transition zone | 4000 | 9.70 | 9.60 | $+0.10$ | $+0.98$ |
| Lower mantle | 4985 | 12.00 | 12.12 | $-0.12$ | $-1.03$ |
| Outer core | 11050 | 9.15 | 27.64 | $-18.49$ | $-202$ |
| Inner core | 12950 | 11.15 | 32.49 | $-21.34$ | $-191$ |

The law describes the mantle well — a straight line through four rounded anchors
with $r^2 = 0.99$ and residuals of a few per cent. **It predicts
27.6 km/s for the outer core, where 9.15 km/s is observed.** That absurd
extrapolation is the point of the exercise.

Two things follow.

**The law is local and empirical.** It is a correlation at nearly constant mean
atomic weight. Across the CMB the mean atomic weight changes from about 20 to
about 50, and the correlation has no reason to survive. Treating it as a physical
law and extrapolating it is a category error.

**The size of the failure is itself the evidence.** A metal-rich material at
$\rho = 11\,050$ kg m⁻³ has a far lower $v_p$ than a silicate at the same density.
That is *expected*: at fixed density, a higher mean atomic weight means fewer
atoms per unit volume and a smaller elastic response per unit mass, so $v_p$ falls.
The observation matches the direction of this expectation, and the mismatch is a
quantitative measure of how much heavier the core's atoms are. This is the
argument of lesson [01](./01-pressure-density-depth.md) §4.2, seen from the
empirical side.

## 4. Mineralogy: what the velocities say about the mantle

### 4.1 The two discontinuities

The upper mantle's seismic structure has two sharp features, and both are mineral
phase changes rather than chemical boundaries. The thermodynamics is in
[02-05-07](../05-thermodynamics/07-phase-equilibria.md); the seismological
consequences are here.

| Depth | Transition | Pressure | Clapeyron slope $\mathrm{d}P/\mathrm{d}T$ | Seismic signature |
|---|---|---|---|---|
| ~410 km | olivine → wadsleyite ($\alpha \to \beta$) | 13.5–14 GPa | $+2$ to $+3$ MPa/K | A velocity step of order 10 per cent |
| ~520 km | wadsleyite → ringwoodite ($\beta \to \gamma$) | ~17–18 GPa | small | Diffuse; often hard to detect |
| ~660 km | ringwoodite → bridgmanite + ferropericlase | ~23–24 GPa | $-2$ to $-3$ MPa/K | The largest velocity and density step in the mantle |

The pressure and Clapeyron ranges are the adopted values of
[02-05-07](../05-thermodynamics/07-phase-equilibria.md) §3, taken there from the
mineral-physics literature; they are nominal anchors for the transitions rather
than measured properties of a specific rock volume.

The rounded handbook characteristics give a velocity step at 410 km from
$v_p = 8.1$ to 9.1 km/s and $v_s = 4.5$ to 5.0 km/s — about 12 and 11 per cent,
with the density continuous in that rounding. They are also continuous at 660 km
(transition zone base 10.3 km/s, lower mantle top 10.3 km/s), which is an artifact
of the rounding and not a statement about the Earth. The real 660 km
discontinuity is the larger of the two in both velocity and density; see
[12-global-geophysics-interior/01-03](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/03-upper-mantle-discontinuities.md).

**Why the slopes matter.** Because the 410 has a positive Clapeyron slope and the
660 a negative one, a hot mantle deepens the 410 and shallows the 660. That
anti-correlated shift is an observable: a subducting slab, being cold, does the
opposite, and the deflections of the two discontinuities are used to measure
slab temperature. The prediction preceded the observation, which is about as
strong as evidence gets in the deep Earth.

**Why the 660 is sharp.** It is a decomposition into two phases —
ringwoodite into bridgmanite plus ferropericlase — rather than a single-phase
transformation, so the transition interval is narrow, and the discontinuity is
seismically sharp. The 520 km transition, by contrast, is a single-phase
transformation with a small volume change and is correspondingly diffuse.

### 4.2 Why the outer core transmits no S waves

From equation (2), $v_s = \sqrt{\mu/\rho}$. In a fluid at rest there is no
resistance to shear, so $\mu = 0$ and $v_s = 0$ *exactly*, not approximately.
Three consequences:

- **S waves cannot cross the core.** A shear wave incident on the CMB from the
  mantle meets a medium that cannot carry shear, so there is no transmitted S
  wave and the boundary is a perfect reflector for shear: $R_S = -1$ at normal
  incidence.
- **An S-wave shadow appears beyond about 103°** of epicentral distance. If a
  shear wave could cross a 2891 km liquid outer core at $v_s = 7.3$ km/s it would
  take $2891/7.3 = 396$ s and appear in the arrivals. It does not. The shadow is
  not an absence of signal but a *hard edge* in the travel-time curve, and it was
  recognised as such before the liquid-core interpretation was accepted.
- **P waves convert at the boundary.** An incident P wave generates a reflected
  P, a reflected S and a transmitted P, with amplitudes that depend on the angle
  of incidence as well as on the impedances. That is why PKP branches exist and
  why the inner core was discovered from a P-wave phase (PKIKP) rather than an S
  phase.

### 4.3 The inner core

The inner core is solid — it transmits shear waves at
$v_s \approx 3.6$ km/s — while being *hotter* than the liquid above it. That
apparent paradox is resolved entirely by the pressure dependence of the melting
temperature: $(\mathrm{d}T_m/\mathrm{d}P)$ is large enough that $T_m$ at
330 GPa exceeds the adiabat, whereas at 135 GPa the adiabat exceeds $T_m$. The
Clausius–Clapeyron relation and the arithmetic are in
[02-05-07](../05-thermodynamics/07-phase-equilibria.md) §5, and the adiabat it is
compared against is in lesson [02](./02-equations-of-state.md) §4.4.

The inner core's high Poisson ratio (0.442) is the seismological fingerprint of
this unusual material state.

## 5. Impedance contrasts at the major boundaries

Acoustic impedance is $Z = \rho v_p$, and the normal-incidence reflection
coefficient for a plane wave is

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1}. \qquad (6)$$

Using the handbook's rounded densities and velocities on both sides of each
boundary:

| Boundary | $Z_1$ ($10^3$ kg m⁻² s⁻¹) | $Z_2$ | $R$ | $R$ (%) |
|---|---|---|---|---|
| Moho | 18.850 | 26.730 | 0.1729 | 17.29 |
| 410 km | 29.160 | 32.760 | 0.0581 | 5.81 |
| Core–mantle boundary | 76.309 | 79.200 | 0.0186 | 1.86 |
| Inner-core boundary | 125.660 | 140.800 | 0.0568 | 5.68 |

The result is counter-intuitive and worth dwelling on. **The core–mantle
boundary, with a 78 per cent density jump — by far the largest of the four —
reflects less than one-third as much P-wave energy at normal incidence as the
410 km discontinuity, where this rounded model has no density step at all.** The
reason is that $Z = \rho v_p$ and the two factors move in opposite directions:
density rises by 78 per cent while $v_p$ falls by 42 per cent, and they nearly
cancel.

Three lessons follow.

- **A big density contrast does not make a strong reflector.** Impedance, not
  density, controls reflection.
- **The Moho is the strongest reflector of the four**, which is why controlled-source
  crustal seismology can map it with modest sources, and why "PmP" is a standard
  phase.
- **The CMB is nonetheless a decisive boundary for shear.** $R_P = 0.019$;
  $R_S = -1$. The same boundary is nearly transparent to P and perfectly opaque
  to S, and it is the second property that made it famous.

## 6. Physical interpretation

**The moduli are the physical quantities; velocity is what we measure.** It is
worth restating the table of §2.1 as a mineral physicist would: $K$ doubles from
the upper mantle to the lower mantle and doubles again into the inner core, while
$\mu$ grows only modestly and then collapses in the outer core. Pressure
destroys the distinction between compression and shear — it stiffens both, but
stiffens compression far more — and that is why the deep Earth has an unusually
high $v_p/v_s$.

**The discontinuities are thermodynamics seen acoustically.** A phase change with
a volume change makes a velocity step; the sign of its Clapeyron slope makes the
step move with temperature. There is nothing else in the mantle that makes a
sharp, laterally coherent velocity step at a fixed depth, which is why the 410
and 660 are unambiguously mineralogical.

**The core is the one place where a single observation settles a question.** The
S-wave shadow is not an inference from a model; it is the direct observation that
shear cannot propagate, and hence that the region is liquid. Every other
conclusion in this module is model-dependent to some degree. This one is not.

## 7. Assumptions and regime of validity

| Assumption | Where used | Regime of validity | What breaks it |
|---|---|---|---|
| Isotropic elasticity | Equations (1)–(2) | The mantle is weakly anisotropic; a reference model reports an isotropic average | The lowermost mantle (transverse isotropy) and the inner core (up to several per cent); anisotropy is a separate observable |
| Linearly elastic, infinitesimal strain | Equations (1)–(2) | Valid for seismic strains of $10^{-6}$ | Nothing at seismic amplitudes; nonlinearity matters for shock experiments |
| $\rho$ known independently | §2.1 | Requires a reference model or an EOS | The degeneracy of §3.1 |
| Birch's law at constant mean atomic weight | §3.3 | Excellent within the mantle; the fit here gives $r^2 = 0.99$ | Any change of composition, especially across the CMB |
| Plane wave, normal incidence | Equation (6) | An approximation for real arrivals | Most seismic observations are *not* at normal incidence; amplitudes vary strongly with angle, and converted phases appear |
| Sharp boundary | §5 | The 410 and 660 are sharp on a seismic wavelength (tens of kilometres) | Gradual transitions (the 520) reflect differently; the reflection coefficient of a gradient must be computed from the impedance gradient |
| $\mu = 0$ exactly in the outer core | §4.2 | Exact for a Newtonian fluid at rest | A very small viscosity does give a negligible but nonzero $\mu$; the effect is unobservable, but "exactly zero" is a statement about the model |

## 8. Units and dimensional analysis

- **Equations (1)–(2).** $\sqrt{\mathrm{Pa}/(\mathrm{kg\,m^{-3}})}
  = \sqrt{\mathrm{m^2\,s^{-2}}} = \mathrm{m\,s^{-1}}$ ✓.
- **$\phi$.** (km/s)² = km² s⁻² = $10^6$ m² s⁻². Then $\rho\phi$ in kg m⁻³ ×
  m² s⁻² = Pa ✓. **Do not forget the $10^6$.**
- **$K/\mu$.** Both in GPa, so the ratio is dimensionless ✓. Equation (4) is a
  useful consistency check on any velocity table: it must hold to the rounding.
- **Poisson's ratio.** Dimensionless; both formulae (5) are consistent, and both
  must lie in $[-1, 0.5]$. A computed $\nu$ outside that range means an
  arithmetic or input error, never new physics.
- **Impedance.** kg m⁻³ × km s⁻¹ = $10^3$ kg m⁻² s⁻¹, which is the unit used in
  the table of §5. That is not an SI unit; it is a working unit. If you convert to
  SI, $Z_{1,\text{CMB}} = 7.6309\times10^7$ kg m⁻² s⁻¹.
- **Reflection coefficient.** A ratio of impedances, so dimensionless; $R = 0.0186$
  is 1.86 per cent of amplitude. **Energy reflection is $R^2$**, i.e. 0.035 per
  cent — a trap when comparing with an energy budget.
- **Useful anchor.** For a Poisson solid, $v_p/v_s = \sqrt3 = 1.732$; a measured
  ratio below 1.7 indicates a low $\mu/K$, i.e. a material that is easy to shear
  and hard to compress. Almost nothing in the mantle is in that regime; the
  inner core, with a ratio near 3, is at the other extreme.

## 9. Python demonstration

[`code/velocity_moduli_demo.py`](./code/velocity_moduli_demo.py) performs the
inversion, demonstrates the degeneracy, fits Birch's law, and computes the
impedance contrasts. The blocks below are the script's actual output, **abridged
by omission** where a block would otherwise repeat rows already tabulated above;
every line shown is reproduced verbatim.

```text
layer               rho    v_p    v_s   K (GPa)  mu (GPa)   K/mu     nu  phi km2/s2
crust              2750   6.15   3.45      60.4      32.7   1.84  0.270       21.95
upper mantle       3300   8.10   4.50     127.4      66.8   1.91  0.277       38.61
transition zone    4000   9.70   5.30     226.5     112.4   2.02  0.287       56.64
lower mantle       4985  12.00   6.45     441.3     207.4   2.13  0.297       88.53
outer core        11050   9.15   0.00     925.1       0.0    inf  0.500       83.72
inner core        12950  11.15   3.60    1386.2     167.8   8.26  0.442      107.04
```

```text
     rho   K (GPa)  mu (GPa)   phi km2/s2
    4000     201.6     100.0        50.39
    6000     302.3     150.0        50.39
    9900     498.9     247.5        50.39
```

```text
  Least-squares fit v_p = a + b rho over the four silicate layers:
    v_p (km/s) = -0.6258 + 2.5576 x rho (g/cm3)
  r^2 over the silicates = 0.99064, so a straight line in the
  (rho, v_p) plane describes the mantle well. Published Birch-law
  slopes are of the order of 3 km/s per g/cm3; the fitted value is of
  that order, which is all that is claimed here, since the fit is to
  four rounded anchors and not to data.
layer               rho  v_p obs  v_p fit    resid  resid %
crust              2750     6.15     6.41    -0.26    -4.19
upper mantle       3300     8.10     7.81     0.29     3.53
transition zone    4000     9.70     9.60     0.10     0.98
lower mantle       4985    12.00    12.12    -0.12    -1.03
outer core        11050     9.15    27.64   -18.49  -202.03
inner core        12950    11.15    32.49   -21.34  -191.43
```

```text
boundary                   Z1 (1e6)   Z2 (1e6)        R     R %
Moho                         18.850     26.730   0.1729   17.29
410 km                       29.160     32.760   0.0581    5.81
core-mantle boundary         76.309     79.200   0.0186    1.86
inner-core boundary         125.660    140.800   0.0568    5.68
```

### What to observe

| Observation | Consequence |
|---|---|
| $K$ rises 60 → 1386 GPa, $\mu$ rises 33 → 168 GPa | Pressure stiffens compression far more than shear; the deep Earth is incompressible but not shear-rigid |
| $K/\mu$ climbs 1.84 → 2.13 in the mantle, then 8.26 in the inner core | A weak $v_p/v_s$ trend in the mantle, and an abrupt one at the inner-core boundary |
| $\nu = 0.270 \to 0.297$ in the mantle, 0.442 in the inner core | Poisson's ratio is nearly constant in the mantle; the inner core is different physics |
| $\phi$ identical at three different densities | The degeneracy is exact, not approximate |
| $r^2 = 0.99$ for Birch's law in the mantle | The correlation is real within a family of similar materials |
| Birch's law predicts 27.6 km/s in the outer core against 9.15 observed | The law is empirical and must not cross the CMB; the size of the failure measures the change in mean atomic weight |
| Moho $R = 17.3\%$ despite the smallest density contrast | Impedance, not density, controls reflection |
| CMB $R = 1.86\%$ despite a 78 per cent density jump | $\rho$ up and $v_p$ down nearly cancel in $Z = \rho v_p$ |
| CMB $R_S = -1$ | The same boundary is a perfect shear reflector |

> **Breaking exercise.** The reflection coefficient in §5 is computed at normal
> incidence. Add an angle to the calculation conceptually: at an incidence angle
> $\theta$ in the mantle, Snell's law relates the transmitted ray to
> $\sin\theta/v_p$, and the transmitted P ray in the outer core is *refracted
> towards the boundary* because $v_p$ drops. Predict, before doing any algebra,
> whether the P-wave reflection coefficient at a given angle increases or
> decreases relative to the normal-incidence value, and then consider the
> consequence: there is a critical distance inside which the boundary behaves one
> way and beyond which it behaves another, and that is the origin of the PKP
> caustic structure near 145°.

## 10. Common mistakes

1. **Forgetting the $\tfrac43$ in $v_p$.** Using $v_p = \sqrt{K/\rho}$ gives $K$
   too small by a factor of $(1+\tfrac43\mu/K)$ — about 30 per cent in the
   mantle.
2. **Reporting $\phi$ in km² s⁻² and then multiplying by $\rho$ in kg m⁻³.**
   The result is $10^6$ times too small. This is the module's most frequent
   arithmetic error.
3. **Believing that a velocity anomaly implies a density anomaly of the same
   sign.** The degeneracy of §3.1 says otherwise, and at the CMB the signs are
   opposite for a reason.
4. **Extrapolating a $v_p$–$\rho$ regression across a composition change.** §3.3
   is a deliberately absurd demonstration of what that costs.
5. **Reading a large density contrast as a strong reflector.** Compute $Z$ and
   then $R$; the CMB is the counter-example.
6. **Confusing amplitude and energy reflection coefficients.** $R$ is amplitude;
   energy is $R^2$.
7. **Attributing the S-wave shadow to attenuation.** It is a consequence of
   $\mu = 0$. Attenuation would smear arrivals, not remove them beyond a sharp
   distance.
8. **Treating the handbook's rounded velocity ranges as measurements of a
   place.** They are nominal anchors for a global average.
9. **Assuming mineral boundaries are always chemical boundaries.** The 410 and
   660 are phase changes in a mantle of constant bulk composition; the CMB is
   the chemical one.
10. **Taking $v_p/v_s$ as a fixed 1.732.** That is the Poisson solid. The mantle
    is nearer 1.8 and the inner core is near 3.

## 11. Real-world applications

- **Reference-model construction.** Every published model is a tabulated set of
  $v_p$, $v_s$ and $\rho$; the derivations in §2 are used constantly in
  reproducing their derived quantities and in checking a new model against an
  old one.
- **Compositional inversion of the mantle.** The misfit pattern between a
  candidate assemblage's predicted velocities and the observed profile is the
  primary tool of mantle mineralogy.
- **Core composition.** The same logic applied to the outer core, where the
  question is which light elements, and in what proportions, close the density
  deficit against pure iron.
- **Reservoir and rock-physics calibration.** In the crust, where $K$, $\mu$ and
  $\rho$ are affected by porosity and fluids, the same equations connect seismic
  velocity to lithology and saturation
  ([05-core-geophysics/04 rock physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Amplitude-versus-offset analysis.** In exploration seismology, the
  angle-dependence of the P reflection coefficient (the extension of equation (6)
  to non-normal incidence) is inverted for density and shear properties.
- **Discriminating a phase boundary from a chemical boundary.** The test is
  whether the boundary's depth tracks temperature with the sign that the
  Clapeyron slope predicts, which is how the 410 and 660 were established as
  mineralogical.

## 12. Further reading

- **Poirier, J.-P. *Introduction to the Physics of the Earth's Interior* (2nd ed.,
  Cambridge University Press, 2000).** The elastic moduli, the wave speeds and
  their mineralogical interpretation, in one short book. Level: graduate.
- **Anderson, D. L. *Theory of the Earth* (Blackwell, 1989).** The fullest
  development of inferring mineralogy from seismic velocities, by the author who
  did most of it.
- **Dziewonski, A. M., & Anderson, D. L. (1981).** "Preliminary reference Earth
  model." *Physics of the Earth and Planetary Interiors* **25**, 297–356. The
  reference model, including the anisotropy and attenuation parameters.
- **Jackson, I. *The Earth's Mantle* (Cambridge University Press, 1998).** The
  mineral physics behind the moduli of §2.1.
- **Ringwood, A. E. *Composition and Petrology of the Earth's Mantle*
  (McGraw-Hill, 1975).** The classic statement of the mineralogical model the
  discontinuities support. Historical and foundational.
- **Kennett, B. L. N. *The Seismic Wavefield*, vol. 1 (Cambridge University
  Press, 2001).** The forward problem: how travel times and waveforms actually
  yield the profiles this lesson treats as given.
- **Birch, F. (1952).** "Elasticity and constitution of the Earth's interior."
  *Journal of Geophysical Research* **57**, 227–286. The origin of the
  velocity–density relation of §3.3, and of the finite-strain equation of state.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the reference model and the density jump this lesson interprets.
- [02 Equations of State and High-Pressure Mineral Physics](./02-equations-of-state.md)
  — where the moduli come from, and the thermal corrections that shift them.
- [05 Comparative Planetary Physics and Interiors](./05-planetary-physics.md)
  — the same diagnostics applied where the seismic coverage is thin or absent.
- [02-04-04 Elastic Moduli](../04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  and [02-04-05 Elastodynamics](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the derivations of equations (1)–(2).
- [02-05-07 Phase Equilibria and Mantle Mineralogy](../05-thermodynamics/07-phase-equilibria.md)
  — the Clapeyron slopes behind the 410 and 660.
- [06-seismology/01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md)
  — how the velocities are measured in practice.

Exercises:
[`exercises/03-seismic-parameter-relations-exercises.md`](./exercises/03-seismic-parameter-relations-exercises.md)
and
[`exercises/03-seismic-parameter-relations-solutions.md`](./exercises/03-seismic-parameter-relations-solutions.md).

## Self-assessment checklist

- [ ] I can derive $v_p$ and $v_s$ from the elastodynamic equations and say
      which modulus each measures. (§1)
- [ ] I can invert $(v_p,v_s,\rho) \to K,\mu,\nu,\phi$ without consulting the
      table. (§2.1)
- [ ] I can derive $K/\mu = (v_p/v_s)^2 - \tfrac43$ and use it as a consistency
      check. (§2.2)
- [ ] I can state the Poisson-solid values $\nu = 0.25$, $v_p/v_s = 1.732$.
      (§2.2)
- [ ] I can demonstrate the density–velocity degeneracy with three densities and
      one velocity pair. (§3.1)
- [ ] I can name three independent constraints that break the degeneracy. (§3.2)
- [ ] I can fit Birch's law, report the residuals, and explain the failure at
      the CMB. (§3.3)
- [ ] I can explain the 410 and 660 as phase changes and use the signs of their
      Clapeyron slopes. (§4.1)
- [ ] I can explain why $v_s = 0$ exactly in the outer core and describe the
      S-wave shadow. (§4.2)
- [ ] I can compute $R$ from impedance and explain the CMB anomaly. (§5)
