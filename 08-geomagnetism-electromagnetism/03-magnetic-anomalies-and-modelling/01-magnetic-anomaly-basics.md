---
id: 08-03-01
title: "Magnetic Anomaly Physics and Remanent vs Induced Magnetisation"
level: advanced
prereqs: ["08-01-07", "02-07-02"]
tags: [geomagnetism, electromagnetism, magnetic-anomalies, magnetisation, remanence, dipole]
---

# Magnetic Anomaly Physics and Remanent vs Induced Magnetisation

A magnetic survey measures one thing: the **total field**, a scalar, at each
station. What makes the measurement interesting is that a magnetised body adds a
small field to the main field of the Earth, and that addition can be turned into
a statement about rock. This lesson builds that statement from the ground up. It
derives the field of a magnetised body, shows that what the instrument records is
a **projection** of that field rather than a magnitude, and quantifies the two
magnetisations that every rock carries: an **induced** part, aligned with the
present field and proportional to susceptibility, and a **remanent** part that
the rock brought with it and that has nothing to do with today's field.

> All models and data in this module are **SYNTHETIC**. The body, its
> susceptibility, its remanence and the ambient field magnitude in this lesson
> are chosen teaching values. No survey, station or published anomaly is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between the ambient flux density $B_0$, the magnetic field
   strength $H_0$, an induced magnetisation $M$ and a magnetic moment $m$, with
   the units of each.
2. **Derive** the vector field of a point dipole from a scalar potential and
   obtain the on-axis $r^{-3}$ amplitude in the pole configuration.
3. **Derive** the total-field anomaly $\Delta T = \hat{f}\cdot\mathbf{B}_a$ and
   **state** the condition under which it may be treated as linear in the
   anomalous field.
4. **Compute** the anomaly of a uniformly magnetised body and **verify** the
   $r^{-3}$ fall-off numerically.
5. **Distinguish** induced from remanent magnetisation, **define** the
   Koenigsberger ratio $Q$, and **compute** the anomaly of a remanence-dominated
   body, including its sign.
6. **Explain** why the measured anomaly depends on the direction of the ambient
   field even when the body is unchanged, and **quantify** the
   $3\sin^2 I - 1$ factor.
7. **State** the depth–moment trade-off and **compute** the moment needed to
   reproduce a given anomaly at a given depth.

## Prerequisites

- [08-01-07 Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](../01-earth-magnetic-field/07-rock-magnetism.md) —
  what susceptibility and natural remanence mean as rock properties.
- [02-07-02 Magnetostatics](../../02-physics/07-electromagnetism/02-magnetostatics.md) —
  the magnetic dipole field, the scalar potential and the SI constitutive
  relation $\mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M})$.

## 1. Three fields, one measurement

Three quantities are easily confused and must be kept apart.

| Quantity | Symbol | Unit | What it is |
|---|---|---|---|
| Magnetic flux density | $\mathbf{B}$ | T (1 nT $=10^{-9}$ T) | What a magnetometer measures; the physical field |
| Magnetic field strength | $\mathbf{H}$ | A m$^{-1}$ | $\mathbf{H} = \mathbf{B}/\mu_0$ in vacuum |
| Magnetisation | $\mathbf{M}$ | A m$^{-1}$ | Magnetic moment per unit volume of material |

They are related in a material by

$$\mathbf{B} = \mu_0\left(\mathbf{H} + \mathbf{M}\right), \qquad \mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}.$$

For a weakly magnetic rock the induced magnetisation is proportional to the
applied field,

$$\mathbf{M}_i = \chi\,\mathbf{H}, \qquad \chi = \text{volume magnetic susceptibility (SI, dimensionless)}.$$

$\chi$ is small for almost all rocks — of order $10^{-4}$ to $10^{-1}$ — which is
why the anomalous field is a small part in $10^{4}$ or $10^{5}$ of the main
field. That is the whole difficulty of the method and the reason the instrument
must be stable to a fraction of a nanotesla.

The **magnetic moment** of a uniformly magnetised body of volume $V$ is

$$\mathbf{m} = \mathbf{M}\,V \qquad (\mathrm{A\,m^{2}}),$$

and it is the moment, not the size, that a distant magnetometer responds to.

## 2. The field of a magnetised body

### 2.1 The scalar potential route

Outside a magnetised body, currents are zero and the field may be written as the
gradient of a scalar potential,

$$\mathbf{H} = -\nabla\Psi, \qquad \Psi(\mathbf{r}) = \frac{1}{4\pi}\int \frac{\sigma_m}{|\mathbf{r}-\mathbf{r'}|}\,\mathrm{d}S',
\qquad \sigma_m = \mathbf{M}\cdot\hat{n},$$

where $\sigma_m$ is the **magnetic surface charge** on the boundary and $\hat n$
its outward normal. Every anomaly in this module is a consequence of this
relation: a contrast in magnetisation produces charges on an interface, and the
charges produce the field. The derivation is checked numerically in
[04 Forward Modelling](04-magnetic-forward-modelling.md).

### 2.2 The point dipole

For a compact body observed far away, the charges collapse into a single
expression. With $\mathbf{r}$ the vector **from the dipole to the observation
point**, $\hat r = \mathbf{r}/r$ and $r = |\mathbf{r}|$,

$$\Psi = \frac{1}{4\pi}\,\frac{\mathbf{m}\cdot\hat r}{r^{2}}.$$

Because $\nabla\left(\mathbf{m}\cdot\mathbf{r}/r^{3}\right)
= \left[\mathbf{m} - 3(\mathbf{m}\cdot\hat r)\hat r\right]/r^{3}$, the field is

$$\boxed{\;\mathbf{B}_a(\mathbf{r}) = \frac{\mu_0}{4\pi}\,
\frac{3\left(\mathbf{m}\cdot\hat r\right)\hat r - \mathbf{m}}{r^{3}}.}$$

Two consequences are used constantly:

- the field falls off as $r^{-3}$: doubling the distance to the observer divides
  the anomaly by eight;
- the field is not radial and not aligned with $\mathbf{m}$ except on the axis.

On the dipole axis ($\hat r$ parallel to $\mathbf{m}$) the bracket becomes
$2\mathbf{m}$, so

$$B_{\text{on-axis}} = \frac{\mu_0}{4\pi}\,\frac{2m}{r^{3}}.$$

### 2.3 What the instrument actually records

A magnetometer measures the **magnitude** of the total field,
$|\mathbf{B}_0 + \mathbf{B}_a|$, and reports a small difference from the main
field. Expanding,

$$\left|\mathbf{B}_0+\mathbf{B}_a\right|
= \sqrt{B_0^{2} + 2\mathbf{B}_0\!\cdot\!\mathbf{B}_a + B_a^{2}}
\approx B_0 + \hat f\cdot\mathbf{B}_a
+ \frac{B_a^{2} - \left(\hat f\cdot\mathbf{B}_a\right)^{2}}{2B_0} + \dots,
\qquad \hat f = \frac{\mathbf{B}_0}{B_0}.$$

The **total-field anomaly** is therefore

$$\Delta T = \hat f\cdot\mathbf{B}_a,$$

a *projection* of the anomalous vector on the direction of the main field.
Truncating the expansion is legitimate only while the quadratic term is
negligible. With the demonstration's numbers — $B_0 = 50.0\ \mu$T and a peak
$\Delta T = 31.08$ nT — that term is of order $(31.08\times10^{-9})^{2}/(2\times
50.0\times10^{-6}) = 9.7\times10^{-3}$ nT, which is $0.03\%$ of the anomaly. At
$\Delta T = 1000$ nT the same expression gives 10 nT, or $1\%$: strong anomalies
in strong gradients are where the linearisation starts to matter.

## 3. Worked example: the anomaly of one body

Take a **synthetic** body of volume $V = 1.00$ km$^3$ with susceptibility
$\chi = 0.050$ in an ambient field of magnitude $B_0 = 50.0\ \mu$T inclined at
$60^\circ$ to the horizontal, and observe it at the surface directly above its
centre at a depth $z = 2.0$ km.

**Step 1 — the field strength.**

$$H_0 = \frac{B_0}{\mu_0} = \frac{50.0\times10^{-6}}{1.2566\times10^{-6}}
= 39.79\ \mathrm{A\,m^{-1}}.$$

**Step 2 — induced magnetisation.**

$$M_i = \chi H_0 = 0.050 \times 39.79 = 1.989\ \mathrm{A\,m^{-1}}.$$

**Step 3 — moment.** $V = 1.00\ \mathrm{km^{3}} = 1.00\times10^{9}\ \mathrm{m^{3}}$, so

$$m = M_i V = 1.989\times10^{9}\ \mathrm{A\,m^{2}}.$$

**Step 4 — the anomaly.** With $\hat r = (0,0,-1)$ and
$\hat f = (\cos 60^\circ, 0, \sin 60^\circ) = (0.500, 0, 0.866)$,
$\mathbf{m} = m\hat f$, so

$$\Delta T = \frac{\mu_0}{4\pi}\,\frac{m}{z^{3}}
\left[3\left(\hat m\!\cdot\!\hat r\right)\left(\hat f\!\cdot\!\hat r\right)
- \hat m\!\cdot\!\hat f\right]
= 10^{-7}\times\frac{1.989\times10^{9}}{(2.0\times10^{3})^{3}}
\left[3(0.866)^{2}-1\right].$$

The bracket is $3\times0.750-1 = 1.250$, so

$$\Delta T = 1\times10^{-7}\times2.486\times10^{-1}\times1.250
= 3.108\times10^{-8}\ \mathrm{T} = 31.08\ \mathrm{nT}.$$

The demonstration prints $31.08$ nT. Note what the bracket shows: had the field
been vertical ($I = 90^\circ$), it would have been $3-1 = 2$, and the on-axis
formula $(\mu_0/4\pi)(2m/z^{3}) = 49.74$ nT would apply. Had the field been
inclined at $30^\circ$, the bracket would be $3(0.25)-1 = -0.25$ and the anomaly
would be $-6.22$ nT: the same body, a reversed anomaly.

**Step 5 — the fall-off.** Repeating step 4 at increasing depth with the same
moment gives $248.7$ nT km$^3$ at every depth (the table of the demonstration),
and a measured log–log slope of $-3.0000$. The product $\Delta T z^{3}$ is a
constant only because the *observer* moved, not the body: this is the
$r^{-3}$ law, and it is what makes depth so hard to separate from magnetisation.

## 4. Induced and remanent magnetisation

A rock carries two magnetisations.

**Induced magnetisation** is produced by the present field:
$\mathbf{M}_i = \chi\mathbf{H}$, parallel to $\mathbf{B}_0$, switched on and off
with the field.

**Remanent magnetisation** (natural remanent magnetisation, NRM) $\mathbf{M}_r$
is retained by the rock from the time it formed or was last heated. It has its
own magnitude and its own direction, acquired from an ancient field, from a
chemical process or from lightning.

The two add as vectors:

$$\mathbf{M} = \mathbf{M}_i + \mathbf{M}_r.$$

Their relative size is the **Koenigsberger ratio**

$$Q = \frac{|\mathbf{M}_r|}{|\mathbf{M}_i|} = \frac{|\mathbf{M}_r|}{\chi H_0}.$$

For the teaching values above, $M_r = 0.500\ \mathrm{A\,m^{-1}}$ gives
$Q = 0.500/1.989 = 0.251$: induced magnetisation dominates and the anomaly is
essentially the induced one. But $Q$ is a ratio to $H_0$, and $H_0$ varies by a
factor of two across the Earth, so a rock that is induced-dominated near the
pole may be remanence-dominated near the equator. Many rocks have $Q \gg 1$:
[02 Koenigsberger Ratio and Remanence Dominance](02-koenigsberger-and-remanence.md)
takes that case apart.

Two facts follow immediately from the vector sum and are worth stating before
the numbers:

- the anomaly of a body is **not** proportional to $|\mathbf{M}|$ alone; the
  direction of $\mathbf{M}$ relative to $\hat f$ enters through the same bracket
  as before;
- a body whose remanence opposes the field can produce a **negative** anomaly
  over its centre, which no induced-only interpretation can reproduce.

## 5. Why direction matters more than magnitude

Isolate the direction dependence by taking a body magnetised along $\hat f$ (the
induced case) at inclination $I$. With $\hat m = \hat f$ and
$\hat f\cdot\hat r = -I_z$ in the survey convention, the bracket is
$3\sin^{2}I - 1$ and

$$\Delta T_{\text{over the centre}} = \frac{\mu_0}{4\pi}\frac{m}{z^{3}}
\left(3\sin^{2}I - 1\right).$$

Three regimes follow:

| Inclination $I$ | $3\sin^2 I - 1$ | Anomaly over the centre |
|---|---|---|
| $90^\circ$ (pole) | $+2.00$ | strong and positive |
| $35.3^\circ$ | $0$ | zero |
| $0^\circ$ (equator) | $-1.00$ | negative, half the magnitude |

The vanishing at $35.3^\circ$ is the reason magnetic surveys at low magnetic
latitudes are hard: the anomaly over a source can be a negative lobe with
positive flanks, and it is displaced from the source. That displacement is the
subject of [03 Reduction to the Pole](03-reduction-to-pole.md).

In the demonstration, changing only the inclination of the ambient field while
holding the body fixed gives $49.74$ nT at $90^\circ$, $31.08$ nT at $60^\circ$
and $-6.22$ nT at $30^\circ$. Nothing about the body changed.

## 6. The depth–moment trade-off

Fix the target anomaly at $\Delta T = 20.0$ nT on the axis and solve for the
moment:

$$m = \frac{\Delta T\,z^{3}\,4\pi}{2\mu_0}.$$

| Depth $z$ (km) | Required $m$ (A m$^2$) | Required volume at $M_i = 1.989$ A m$^{-1}$ (km$^3$) |
|---|---|---|
| 1.0 | $1.00\times10^{8}$ | 0.050 |
| 2.0 | $8.00\times10^{8}$ | 0.402 |
| 4.0 | $6.40\times10^{9}$ | 3.217 |
| 8.0 | $5.12\times10^{10}$ | 25.736 |

Because $\Delta T \propto m/z^{3}$, depth and moment are **exactly traded** in a
dipole model: a body eight times deeper needs 512 times the moment for the same
signal. Amplitude alone can never give both. Everything in
[05 Depth Estimation](05-magnetic-depth-estimation.md) and
[06 Magnetic Inversion](06-magnetic-inversion.md) is a response to this single
degeneracy.

## 7. Assumptions and regime of validity

1. **The body is uniformly magnetised.** True for an ellipsoid in a uniform
   field, and an excellent approximation for a weakly magnetic body of any shape
   because the internal field is barely perturbed. It fails for strongly
   magnetic bodies, whose demagnetising field varies inside them; the
   demonstration of [07 Applications](07-magnetic-uses.md) quantifies the
   saturation of an induced moment for a sphere.
2. **The observation is outside the body.** Inside, $\mathbf{B}$ contains the
   $\mu_0\mathbf{M}$ term and the surface-charge formula gives $\mathbf{H}$, not
   $\mathbf{B}$.
3. **The dipole approximation applies only in the far field.** The rule of thumb
   is that it needs several body widths; the demonstration of
   [04 Forward Modelling](04-magnetic-forward-modelling.md) measures the error
   and finds $1.4\%$ at five body widths and $17\%$ at one.
4. **The anomaly is small compared with the main field**, so
   $\Delta T = \hat f\cdot\mathbf{B}_a$. Quantified in Section 2.3.
5. **No currents and no time dependence.** Induction in the ground is neglected;
   it reappears as a noise source at long periods in
   [04-06 Geomagnetic Depth Sounding](../04-electromagnetic-induction/06-geomagnetic-depth-sounding.md).
6. **The ambient field is uniform over the body.** Over a few kilometres it is,
   to better than a nanotesla; over hundreds of kilometres it is not.

## 8. Python demonstration

`code/magnetic_anomaly_basics_demo.py` performs every calculation above and
prints labelled results with units. It

1. converts $B_0\to H_0\to M_i\to m$ and prints each with its unit;
2. computes the dipole field vector and shows $\Delta T \neq |\mathbf{B}_a|$:
   the vector components are $(-12.43, 0.00, 43.07)$ nT, $|\mathbf{B}_a| =
   44.83$ nT, and $\Delta T = 31.08$ nT;
3. tabulates the $r^{-3}$ fall-off and measures its slope, $-3.0000$;
4. compares induced and remanent contributions at the same volume: a remanence
   of $0.500$ A m$^{-1}$ along the field gives $7.81$ nT and against it
   $-7.81$ nT;
5. shows the projection at three inclinations and prints the $3\sin^{2}I-1$ rule;
6. tabulates the depth–moment trade-off.

Run it with the project environment:

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_anomaly_basics_demo.py
```

It uses `np.random.default_rng(20261014)`, is print-only and exits 0.

## 9. Exercises

Full problem sets are in
[`exercises/01-magnetic-anomaly-basics-exercises.md`](./exercises/01-magnetic-anomaly-basics-exercises.md)
with worked solutions in
[`exercises/01-magnetic-anomaly-basics-solutions.md`](./exercises/01-magnetic-anomaly-basics-solutions.md).
The exercises include computing $\Delta T$ from scratch, verifying the
$r^{-3}$ law by hand, and a numerical check of the second-order term in the
total-field expansion.

## Mastery checkpoint

Without notes:

> A **synthetic** body has $V = 2.0$ km$^3$, $\chi = 0.020$, and sits $1.5$ km
> deep in an ambient field of $55\ \mu$T inclined at $70^\circ$. **(a)** Compute
> $H_0$, $M_i$ and $m$. **(b)** Compute $\Delta T$ directly above the body.
> **(c)** State what the anomaly would be if the field inclination were
> $35.3^\circ$, and why. **(d)** The same anomaly is recorded over a body at
> $6.0$ km depth: compute the moment that would be required and the
> susceptibility if the volume were unchanged. **(e)** State two things a single
> total-field profile cannot determine.

## Common pitfalls

1. **Quoting a depth without a magnetisation.** Amplitude alone is a product;
   the factors are not separable without more information.
2. **Treating $\Delta T$ as $|\mathbf{B}_a|$.** The instrument measures a
   projection, and at low inclination the difference is the whole anomaly shape.
3. **Assuming $\chi$ is the whole story.** $Q$ can exceed unity and reverse the
   anomaly; assuming induced magnetisation when $Q$ is large inflates the
   apparent susceptibility by an order of magnitude (Section 5 of the
   demonstration of [02](02-koenigsberger-and-remanence.md)).
4. **Mixing cgs units.** In the cgs literature $M$ is in emu cm$^{-3}$ and
   $4\pi$ factors appear in different places; the SI relations used here are
   $\mathbf{B}=\mu_0(\mathbf{H}+\mathbf{M})$ and $\mathbf{M}=\chi\mathbf{H}$.
5. **Forgetting that $Q$ depends on $H_0$.** The same rock has a different $Q$
   at a different latitude.
6. **Using the dipole formula too close to the body.** It is a far-field
   approximation and fails at a few body widths.

## Related modules

- [01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) —
  where $B_0$, its inclination and its secular variation come from.
- [02 Magnetic Instruments and Surveys](../02-magnetic-instruments-and-surveys/README.md) —
  how the nanotesla is actually measured and how a survey is levelled.
- [02 Koenigsberger Ratio and Remanence Dominance](02-koenigsberger-and-remanence.md) —
  the vector sum taken seriously.
- [04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) —
  the same physics for a body of finite size, verified two ways.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  susceptibility and remanence as rock properties.
