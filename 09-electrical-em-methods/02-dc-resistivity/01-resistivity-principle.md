---
id: 09-02-01
title: "Resistivity Principle and the Four-Electrode Arrangement"
level: intermediate
prereqs: ["09-01-01", "02-07-01", "05-02-01"]
tags: [electrical-methods, four-electrode, geometric-factor, contact-resistance, reciprocity]
---

# Resistivity Principle and the Four-Electrode Arrangement

The resistivity measurement is an act of geometry as much as of physics. Two
electrodes push current into the ground and two others measure the resulting
voltage difference; the ratio, multiplied by a purely geometric factor, is
called an *apparent* resistivity. This lesson derives the geometric factor from
the half-space potential, shows why two electrodes cannot do the job, and
measures how much an electrode positioning error costs.

**All models and data in this module are SYNTHETIC.** The half-space
resistivity, the injected current, the contact resistances and the noise are
chosen teaching values; no real survey, instrument or data set is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the potential of a point current source on a conducting half-space
   and verify that the field carries the injected current.
2. **Derive** the general four-electrode geometric factor
   $k = 2\pi/\left[r_{AM}^{-1} - r_{AN}^{-1} - r_{BM}^{-1} + r_{BN}^{-1}\right]^{-1}$
   and **compute** it for a Wenner layout.
3. **Compute** an apparent resistivity from a measured voltage and current, and
   state its units.
4. **Quantify** the error made by a two-electrode measurement in the presence of
   contact resistance, and **explain** how four electrodes remove it.
5. **Estimate** the accuracy cost of an electrode mislocation and identify which
   electrode dominates.
6. **Explain** reciprocity and verify it numerically.
7. **State** the assumptions under which apparent resistivity is a meaningful
   quantity.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  $\rho$, $\sigma$, $V = \rho I/(2\pi r)$ and contact resistance.
- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../../02-physics/07-electromagnetism/01-electrostatics.md) —
  superposition of potentials.
- [05-02-01 Scalar and Vector Fields; Potentials and Gradients](../../05-core-geophysics/02-geophysical-fields-and-observables/01-scalar-vs-vector-fields.md) —
  potentials and fields in geophysics.

## 1. The two-source potential

Superposition gives the potential of a current *pair*. With $+I$ injected at
$A$ and $-I$ extracted at $B$, both on the surface of a uniform half-space,

$$V(P) = \frac{\rho I}{2\pi}\left(\frac{1}{r_{AP}} -
\frac{1}{r_{BP}}\right).$$

*Numerical check (SYNTHETIC).* With $\rho = 100\ \Omega\,\mathrm{m}$,
$I = 0.10\ \mathrm{A}$, `code/resistivity_principle_demo.py` prints the
single-source potential $V(r) = \rho I/(2\pi r)$: 3.18310 V at 0.5 m, 1.59155 V
at 1 m, 0.79577 V at 2 m, 0.31831 V at 5 m, 0.15915 V at 10 m, 0.07958 V at
20 m and 0.03183 V at 50 m, with the dimensionless check
$V\,2\pi r/(\rho I) = 1.000000$ in every row. The demo also integrates the
current density over a hemisphere by Gauss–Legendre quadrature and prints
$\int_0^{\pi/2}\sin\theta\,\mathrm{d}\theta = 1.000000000000$, hence a carried
current of exactly $0.100000000000\ \mathrm{A}$ — the injected value.

## 2. The four-electrode geometric factor

Measure the potential difference between two more electrodes $M$ and $N$:

$$\Delta V = V(M) - V(N) = \frac{\rho I}{2\pi}\left(\frac{1}{r_{AM}} -
\frac{1}{r_{AN}} - \frac{1}{r_{BM}} + \frac{1}{r_{BN}}\right).$$

Define the **geometric factor** $k$ by $\rho_a = k\,\Delta V/I$. Then

$$\boxed{\;k = \frac{2\pi}{\dfrac{1}{r_{AM}} - \dfrac{1}{r_{AN}} -
\dfrac{1}{r_{BM}} + \dfrac{1}{r_{BN}}}\;}\qquad (\mathrm{m}),$$

and for a uniform half-space $\rho_a = \rho$ **for every geometry**: the
apparent resistivity is built so that the answer is exact when the ground is
uniform.

*Numerical check (SYNTHETIC).* The demo evaluates the general expression and
compares it with the closed forms:

| array | electrodes (m) | $k$ from the general formula | closed form | ratio |
|---|---|---|---|---|
| Wenner, $a = 5$ m | $-7.5,\ 7.5,\ -2.5,\ 2.5$ | 31.415927 | $2\pi a = 31.415927$ | 1.000000 |
| Schlumberger, $L = 100$, $l = 10$ m | $-50,\ 50,\ -5,\ 5$ | 777.544182 | $\pi(L^2-l^2)/(4l)$ | 1.000000 |
| dipole-dipole, $n = 3$, $a = 5$ m | $0,\ 5,\ 20,\ 25$ | $-942.477796$ | $-\pi n(n+1)(n+2)a$ | 1.000000 |
| pole-pole, $a = 5$ m | $0,\ \infty,\ 5,\ -\infty$ | 31.415927 | $2\pi a$ | 1.000000 |

The demo reports the *difference* between the two routes as
$0.000\times10^{0}\ \mathrm{m}$ for Wenner and the same for the others: the
named arrays are conventions built on one formula, not different physics. The
sign of $k$ is a convention about which potential electrode is called positive;
measurements use $|k|$.

## 3. Worked example: an apparent resistivity from a reading

A SYNTHETIC Wenner array with $a = 5\ \mathrm{m}$ carries $I = 0.10\ \mathrm{A}$
over a $100\ \Omega\,\mathrm{m}$ half-space. Then

$$\Delta V = \frac{\rho I}{2\pi}\left(\frac{1}{a} - \frac{1}{2a} -
\frac{1}{2a} + \frac{1}{a}\right) = \frac{\rho I}{2\pi a}
= \frac{100\times0.10}{31.415927} = 0.318310\ \mathrm{V},$$

and

$$\rho_a = \frac{k\,\Delta V}{I} = \frac{31.415927\times0.318310}{0.10}
= 100.000000\ \Omega\,\mathrm{m},$$

an error of $0.000\times10^{0}$ against the model. The demo then adds noise:
with 1% voltage noise it recovers $99.529\ \Omega\,\mathrm{m}$ ($-0.47\%$) and
with 5% noise $102.309\ \Omega\,\mathrm{m}$ ($+2.31\%$) — noise propagates
one-for-one into $\rho_a$, so a 2% resistivity target means a 2% voltage target.

**Reciprocity.** Exchanging the current pair and the potential pair leaves the
measurement unchanged: the demo recomputes the array with $A \leftrightarrow M$,
$B \leftrightarrow N$ and prints the ratio of the two voltages as
$1.000000000000$ and the same $100.000000\ \Omega\,\mathrm{m}$. Reciprocity is a
property of the conductivity operator; a forward model that does not reproduce it
is broken, and it is the cheapest check available (see
[09-02-06](06-resistivity-forward-modelling.md) for the same check over a layered
earth).

## 4. Why four electrodes

A two-electrode measurement measures the ground *and* the contacts. With
hemispherical electrodes of radius $a = 0.05\ \mathrm{m}$ on a
$100\ \Omega\,\mathrm{m}$ half-space the geometric resistance is

$$R_\text{geo} = \frac{\rho}{2\pi}\left(\frac{1}{a_1}+\frac{1}{a_2}\right)
= 636.620\ \Omega,$$

and with a SYNTHETIC contact resistance of $500\ \Omega$ per electrode the
reading is $1636.620\ \Omega$ — an apparent resistivity of $257.1\ \Omega\,
\mathrm{m}$ instead of $100.0\ \Omega\,\mathrm{m}$, a factor $2.57$. Section 4
of [09-01-01](../01-electrical-properties-of-earth/01-resistivity-conductivity.md)
showed that making the electrode *larger* makes this worse, because $R_\text{geo}$
falls while $R_c$ does not.

The four-electrode arrangement does not measure a better contact; it moves the
contact into a circuit that carries almost no current. If the voltmeter has input
impedance $Z_\text{in}$, the current in the potential circuit is
$i = \Delta V/Z_\text{in}$ and the extra voltage across the contacts is
$2R_c i$, a fractional error $2R_c/Z_\text{in}$:

| $Z_\text{in}$ ($\Omega$) | $10^{6}$ | $10^{7}$ | $10^{9}$ |
|---|---|---|---|
| error in $\Delta V$ | 0.10000% | 0.01000% | 0.00010% |

**The contact resistance has not been measured away; it has been engineered out
of the measurement path.** That is the whole idea, and it is why the
four-electrode arrangement is universal.

## 5. Geometric error: what a misplaced electrode costs

Over a uniform half-space, a misplaced electrode costs *nothing*: the demo moves
the inner electrode $M$ by 1 cm and, computing $k$ from the actual positions,
recovers $100.000000\ \Omega\,\mathrm{m}$ again. The same 1 cm error with the
*recorded* (nominal) geometry gives $99.750349\ \Omega\,\mathrm{m}$, $-0.2497\%$.
So the error appears only as a mismatch between the geometry used in the
arithmetic and the geometry in the ground.

Over a real (layered) earth the effect is larger and depends on which electrode
moves. For a SYNTHETIC two-layer model ($\rho_1 = 100\ \Omega\,\mathrm{m}$,
$h_1 = 5\ \mathrm{m}$, $\rho_2 = 10\ \Omega\,\mathrm{m}$):

| array | $\rho_a$ (nominal) | move C1/A | move C2/B | move P1/M | move P2/N |
|---|---|---|---|---|---|
| Wenner $a = 5$ m | 86.6952 | +0.1723% | $-0.1715\%$ | $-0.2589\%$ | +0.2597% |
| dipole-dipole $n = 3$, $a = 5$ m | 66.3608 | $-0.1264\%$ | +0.3104% | $-0.3097\%$ | +0.1262% |

(The sign follows the sign of the perturbation of the geometric factor.) The
**closest pair dominates**: the inner Wenner electrode and the adjacent
dipole-dipole electrodes cost about 0.26–0.31% per centimetre, roughly twice the
far pair. Decimetre positioning over a real three-dimensional ground is what
limits accuracy in practice, not the voltmeter.

## 6. Regime of validity

1. **Uniform, isotropic half-space** for the closed forms. Over a layered or
   laterally varying earth $\rho_a$ is a weighted average, not a property of any
   layer. *That* is the subject of
   [09-02-03](03-apparent-resistivity.md).
2. **Point electrodes.** Finite electrode size changes the effective spacing
   near the electrode; Section 4 of
   [09-01-01](../01-electrical-properties-of-earth/01-resistivity-conductivity.md)
   quantifies the resistance, not the geometry.
3. **Flat surface, no topography.** A slope moves electrodes vertically and
   changes $k$ by more than the numbers in Section 5 in steep terrain.
4. **Quasi-static fields.** Valid below the charge-relaxation frequency of
   [09-01-05](../01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)
   (about $10^{8}\ \mathrm{Hz}$ here): always satisfied in practice.
5. **Ohmic, linear ground.** No induced polarisation in the frequency band used;
   if there is, $\Delta V$ depends on time and the reading depends on when it is
   taken.

## 7. Mastery checkpoint

1. Derive $k$ for the Wenner array from the general formula and check it against
   $2\pi a$.
2. A dipole-dipole array with $a = 10$ m, $n = 2$ reads $\Delta V = 4.0\
   \mathrm{mV}$ at $I = 0.5\ \mathrm{A}$. Compute $k$, $\rho_a$ and the units of
   each factor.
3. A Wenner array with $a = 20\ \mathrm{m}$ has $k = 125.66\ \mathrm{m}$.
   What does a 1 cm error in the spacing cost in $\rho_a$ over a uniform
   half-space? Over a two-layer model?
4. Show that reciprocity holds for the four-electrode formula by writing
   $\Delta V$ with the labels exchanged.

## 8. Common pitfalls

1. **Forgetting the geometric factor.** A voltage in volts is not a resistivity.
2. **Assuming a large electrode solves contact resistance.** It makes the
   relative error worse.
3. **Recording nominal positions.** The arithmetic uses recorded positions;
   centimetre errors are invisible until the survey is interpreted.
4. **Reading $\rho_a$ as a layer resistivity.** Over a layered earth it never is.
5. **Mixing units of $k$ and spacings.** $k$ is in metres and scales linearly
   with the array size.

## 9. Related modules

- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md) —
  what each arrangement buys.
- [09-02-03 Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md) —
  what $\rho_a$ means over a real earth.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md).
- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md).
- [05-05 Survey Design and Data Acquisition Principles](../../05-core-geophysics/05-survey-design-and-acquisition/README.md).

## 10. Demonstration and exercises

- [`code/resistivity_principle_demo.py`](code/resistivity_principle_demo.py)
  prints the point-source table, the current-conservation quadrature, the
  geometric factors against their closed forms, the noise propagation, the
  contact-resistance comparison and the mislocation experiment.
- [Exercises](exercises/01-resistivity-principle-exercises.md) and
  [worked solutions](exercises/01-resistivity-principle-solutions.md).
