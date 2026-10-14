---
id: 06-03-01
title: "Faulting, Slip and the Elastic Rebound Cycle"
level: advanced
prereqs: ["06-01-02", "06-02-02"]
tags: [seismology, faulting, elastic-rebound, stress-drop, seismic-moment]
---

# Faulting, Slip and the Elastic Rebound Cycle

> **All models and data in this module are SYNTHETIC.** Every fault, slip rate,
> stress drop and moment below is a chosen teaching value, printed by
> [`code/faulting_and_slip_demo.py`](code/faulting_and_slip_demo.py). No real
> earthquake, catalogue, borehole or measured constant is quoted anywhere.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the tectonic loading rate $\dot\tau = \mu V / W$ from the strain
   rate a plate boundary imposes on a finite brittle layer.
2. **Compute** the mean recurrence interval $T = \Delta\tau\,W/(\mu V)$ and
   **state** every assumption that makes it a *mean* rather than a clock.
3. **Show** algebraically that the coseismic slip $D = \Delta\tau\,W/\mu$ and
   the slip deficit $VT$ are the same quantity, and explain why that identity is
   what fixes $T$.
4. **Compute** the seismic moment $M_0 = \mu A D$ and the moment rate of a
   fault, and **explain** why the long-term moment rate depends on area and
   plate rate but not on how the slip is parcelled into events.
5. **Quantify** the stress drop as a fraction of the ambient stress, and
   **state** why an approximately constant stress drop is an empirical
   regularity rather than a law.
6. **Apply** the Coulomb failure function $CFF = \tau - \mu_s(\sigma_n - p)$ to
   compute how much pore-pressure change is needed to bring a fault to failure.
7. **Identify** which of the model's inputs are measured, nominal or chosen, and
   **report** the resulting uncertainty in $T$ and $M_0$.

## Prerequisites

- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  the elastic moduli and the shear modulus $\mu$ used throughout.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  how the waves from a source reach a station, the subject of the rest of the
  module.
- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  module-level background on elasticity and stress.

## 1. Intuition: a fault is a shear crack loaded by a slow wall

Two blocks of rock move past each other at a few centimetres per year. The rock
between them is not sliding smoothly; it sticks. Because the far sides keep
moving, elastic strain accumulates in the rock near the fault, and with it a
shear stress that grows without bound — until the rock breaks. The break is an
earthquake. After the break, the stress near the fault is lower, the blocks have
moved past each other by some centimetres or metres, and the cycle begins again.

This is **Reid's elastic rebound** picture, and it is the organising idea for the
whole module. Three consequences follow immediately and are worth stating now
because every later lesson uses them:

- An earthquake is the **release** of stored elastic strain, not a sudden push.
  Between events the fault is *deficient* in slip relative to the far field.
- The observable size of the event is the product of three quantities: how
  stiff the rock is, how large the patch that broke is, and how far it slipped.
  That product is the **seismic moment** $M_0$.
- Because the loading is slow and the release is fast, we can almost always
  separate the problem into a **quasi-static loading problem** and a **dynamic
  rupture problem**. This lesson does the first; [06](06-rupture-dynamics.md)
  does the second.

The point of the quantitative model below is not that it predicts a particular
earthquake. It is that it shows, with arithmetic, *which* physical inputs control
*which* observables — and how strongly a mistake in each input propagates.

## 2. Precise definitions

| Symbol | Name | Definition | Unit |
|---|---|---|---|
| $V$ | relative plate rate | long-term slip rate of the two walls past each other | $\mathrm{m\,a^{-1}}$ |
| $W$ | brittle (seismogenic) width | the depth range that deforms by stick-slip rather than creeping | km |
| $\mu$ | shear modulus | elastic constant of the surrounding rock | Pa |
| $\Delta\tau$ | static stress drop | average shear stress released by one event | Pa |
| $A$ | rupture area | the fault patch that slipped | $\mathrm{m^2}$ |
| $D$ | mean coseismic slip | average slip over $A$ | m |
| $M_0$ | seismic moment | $M_0 = \mu A D$ | $\mathrm{N\,m}$ |
| $T$ | recurrence interval | time between two successive events on the same patch | a |
| $\sigma_n$ | effective normal stress | $\sigma_n - p$, the normal stress minus pore pressure | Pa |
| $\mu_s$ | static friction coefficient | dimensionless ratio of shear to effective normal strength | — |

Two remarks on the table. First, $W$ is a *model boundary*: rock below the
brittle layer creeps at a comparable rate, so it does not accumulate the same
elastic strain. Choosing $W$ is choosing where stick-slip stops. Second,
$\Delta\tau$ is an average over the ruptured patch; real faults are not uniformly
loaded, so $\Delta\tau$ is a spatial average and carries the uncertainty of that
averaging.

The demo uses one SYNTHETIC scenario repeatedly, so the page and the code can be
read side by side:

| Input | Value | Label in the demo | Status |
|---|---|---|---|
| $\mu$ | $3.000\times10^{10}\ \mathrm{Pa}$ | `MU` | NOMINAL (crustal rock) |
| $V$ | $35.0\ \mathrm{mm\,a^{-1}} = 3.500\times10^{-2}\ \mathrm{m\,a^{-1}}$ | `V_PLATE` | NOMINAL |
| $W$ | $12.0\ \mathrm{km}$ | `W_BRITTLE` | NOMINAL |
| $A$ | $40\ \mathrm{km}\times12\ \mathrm{km} = 4.800\times10^{8}\ \mathrm{m^2}$ | `A_FAULT` | SYNTHETIC |
| $\Delta\tau$ | $3.0\ \mathrm{MPa}$ | `DTAU` | SYNTHETIC |
| $\mu_s$ | $0.60$ | part 5 | SYNTHETIC, laboratory range |

## 3. Derivations

### 3.1 The loading rate $\dot\tau = \mu V / W$

Let the two far-field walls move past each other at rate $V$. The intervening
brittle layer of width $W$ must absorb the entire relative motion across that
width, so the average engineering shear strain rate in the layer is

$$\dot\gamma = \frac{V}{W} \qquad (\mathrm{s^{-1}}),$$

because a relative velocity divided by a length is a strain per unit time. For a
linear elastic material the shear stress is $\tau = \mu\gamma$ with $\mu$ the
shear modulus, so

$$\boxed{\;\dot\tau = \mu\,\dot\gamma = \frac{\mu V}{W}.\;}$$

*Numerical check (SYNTHETIC).* With $\mu = 3.000\times10^{10}\ \mathrm{Pa}$,
$V = 3.500\times10^{-2}\ \mathrm{m\,a^{-1}}$ and $W = 1.2\times10^{4}\ \mathrm{m}$:

$$\dot\tau = \frac{3.000\times10^{10} \times 3.500\times10^{-2}}{1.2\times10^{4}}
= 8.7500\times10^{4}\ \mathrm{Pa\,a^{-1}}
= 2.7727\times10^{-3}\ \mathrm{Pa\,s^{-1}}.$$

The demo prints exactly these two values. The second follows from the first by
dividing by $1$ year $= 3.15576\times10^{7}\ \mathrm{s}$:

$$\frac{8.7500\times10^{4}}{3.15576\times10^{7}} = 2.7727\times10^{-3}.$$

Note the size of the daily creep: a few **kilopascals per year**, against a
strength of order $10^{8}\ \mathrm{Pa}$. That six-order-of-magnitude gap is the
whole reason earthquakes look like sudden events on a human timescale: the clock
runs slowly and the release is instantaneous.

### 3.2 The recurrence interval

If each event drops the average stress by $\Delta\tau$ and the stress reloads at
the constant rate $\dot\tau$, the mean interval is

$$\boxed{\;T = \frac{\Delta\tau}{\dot\tau}
= \frac{\Delta\tau\,W}{\mu V}.\;}$$

With the scenario above, $T = 3.0\times10^{6} / 8.7500\times10^{4} = 34.29\
\mathrm{a}$.

The demo does not assume this; it *integrates* it. It steps the stress forward
with $\mathrm{d}t = 0.01\,T = 3.429\times10^{-1}\ \mathrm{a}$, drops the stress
by $\Delta\tau$ whenever it reaches $\Delta\tau$, and records the event times:
$34.29$, $68.57$ and $102.86\ \mathrm{a}$. The measured mean interval is
$34.29\ \mathrm{a}$ and the relative difference from the closed form is
$2.69\times10^{-15}$ — machine precision. **In this idealised model the cycle is
exactly periodic.** Nothing in the physics of a real fault guarantees that, and
Section 5 says why.

### 3.3 Slip deficit and the identity that fixes $T$

Between events the walls have moved $VT$ past each other while the fault itself
has moved nothing, so the fault carries a **slip deficit**

$$D_{\text{deficit}} = V T.$$

At the event, the same slip is recovered: a stress drop $\Delta\tau$ acting
across an elastic layer of width $W$ corresponds to a slip

$$D = \frac{\Delta\tau\,W}{\mu}.$$

For the scenario both come out at $D = 1.200\ \mathrm{m}$. This is not a
coincidence and not a second independent fact — substitute $T$ from Section 3.2:

$$V T = V\cdot\frac{\Delta\tau\,W}{\mu V} = \frac{\Delta\tau\,W}{\mu} = D.$$

The equality is exact by construction, which is why the demo reports a relative
difference of $1.85\times10^{-16}$ (floating-point round-off only). The physical
reading is: **the slip deficit accumulated by loading and the slip released by
the stress drop are two ways of writing the same displacement**, and setting
them equal is what *defines* $T$ once $\Delta\tau$, $W$, $\mu$ and $V$ are
chosen. Change any one of the four and the interval changes.

### 3.4 Seismic moment and moment rate

The seismic moment is defined as

$$\boxed{\;M_0 = \mu A D = 1.7280\times10^{19}\ \mathrm{N\,m}.\;}$$

Substituting $D = \Delta\tau W/\mu$ gives the equally useful form
$M_0 = A\,\Delta\tau\,W$, which shows that the moment is *stress drop times
volume*: the energy-like product of the released stress and the deforming
volume. The demo computes $3.000\times10^{10}\times4.800\times10^{8}\times
1.200 = 1.7280\times10^{19}\ \mathrm{N\,m}$.

Now the **moment rate**, the quantity that matters for long-term hazard and for
comparing a fault's seismicity with its tectonics. There are two ways to write
it, and they must agree:

$$\dot M_0\big|_{\text{fault}} = \mu A V = 5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}},
\qquad
\dot M_0\big|_{\text{events}} = \frac{M_0}{T}.$$

The demo evaluates both and finds $5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}}$
and $5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}}$, relative difference
$1.27\times10^{-16}$. Again this is algebra: $M_0/T = \mu A D/(\Delta\tau W/(\mu V))
= \mu A V$. The physical content is the point of Section 4.

### 3.5 Coulomb failure and pore pressure

Whether a fault slips is decided, at the simplest level, by the **Coulomb failure
function**

$$\boxed{\;CFF = \tau - \mu_s\left(\sigma_n - p\right) = \tau - \mu_s\,\sigma_n^{\text{eff}},\;}$$

where $\sigma_n$ is the total normal stress, $p$ the pore-fluid pressure and
$\sigma_n^{\text{eff}}$ the effective normal stress. Failure is favoured when
$CFF$ increases towards zero from below. Differentiating with respect to pore
pressure at fixed $\tau$ and $\sigma_n$:

$$\frac{\partial\,CFF}{\partial p} = +\mu_s.$$

A pore-pressure *increase* therefore always pushes the fault towards failure, and
the leverage is $\mu_s$. With the SYNTHETIC $\mu_s = 0.60$ the demo tabulates:

| $\Delta p$ (MPa) | $\Delta CFF$ (MPa) | $\Delta CFF / \Delta\tau$ ($\Delta\tau = 1\ \mathrm{MPa}$) |
|---|---|---|
| 0.00 | 0.000 | 0.000 |
| 0.50 | 0.300 | 0.300 |
| 1.00 | 0.600 | 0.600 |
| 2.00 | 1.200 | 1.200 |
| 5.00 | 3.000 | 3.000 |

A $1\ \mathrm{MPa}$ pore-pressure rise is worth $0.60\ \mathrm{MPa}$ of added
shear stress. Read in reverse it is a *trigger* calculation: to undo a stress drop
of $3.0\ \mathrm{MPa}$ the fault needs a pore-pressure rise of
$3.0/0.60 = 5.00\ \mathrm{MPa}$, which is the last line of the demo's table.

## 4. Physical interpretation

**The moment rate is a tectonic property; the moment is not.** Section 3.4
showed $\dot M_0 = \mu A V$: only the area of the fault, the stiffness of the
rock and the plate rate enter. How the moment is delivered — one $M_0 = 1.7\times
10^{19}\ \mathrm{N\,m}$ event every $34\ \mathrm{a}$, or a thousand small events —
does not change the long-term moment rate. This single observation is the bridge
to
[06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md):
the moment rate is what a catalogue must average out to, and the *distribution* of
events around that average is a separate question.

**Stress drops are a small fraction of the ambient stress.** At $10\ \mathrm{km}$
depth the lithostatic vertical stress is $\sigma_v = \rho g z = 2700\times
9.80665\times10^{4} = 264.8\ \mathrm{MPa}$ (with $\rho = 2700\ \mathrm{kg\,m^{-3}}$
NOMINAL). The SYNTHETIC stress drop is $3.0\ \mathrm{MPa}$, so

$$\frac{\Delta\tau}{\sigma_v} = \frac{3.0}{264.8} = 0.0113,$$

of order $10^{-2}$. This is why the same fault can host a long sequence of
similar-sized events: if $\Delta\tau$ is roughly the same every time, then
$D = \Delta\tau W/\mu$ is roughly the same every time, and the only free variable
left in $M_0 = \mu A D$ is the **area** $A$. That is the geometric statement
behind self-similarity, which
[06 Rupture Dynamics, Fracture Energy and Scaling Laws](06-rupture-dynamics.md)
quantifies.

**What is empirical here.** The demonstration *assumes* a constant $\Delta\tau$
and finds a periodic cycle. The claim that real earthquakes have an
approximately constant stress drop is an **empirical regularity inferred from
spectra** (developed in [05 Source Spectra](05-source-spectra.md)), not a law
derived from elasticity. It is also only approximate: individual events range over
roughly an order of magnitude in $\Delta\tau$, and the assumption fails most
visibly for the largest and smallest events.

## 5. Assumptions and regime of validity

The block-slider model is exactly as good as this list, and no better.

1. **One fault, one patch.** $A$ is fixed and every event ruptures all of it. A
   real fault has a distribution of patch sizes and partial ruptures; the
   recurrence interval is then a statistical statement, not a clock.
2. **Uniform loading and/or uniform stress drop.** $\Delta\tau$ is a spatial
   average. Real faults have stress concentrations at their edges and barriers
   that survive several cycles.
3. **Constant $\mu$ and $W$.** Both vary with depth, temperature and lithology.
   $W$ in particular is defined by the brittle–ductile transition, which moves
   with strain rate.
4. **No aseismic slip.** Creep, afterslip and slow slip remove part of the
   accumulated moment without a normal earthquake, so $\dot M_0|_{\text{events}}$
   measured from a catalogue is a *lower bound* on $\mu A V$.
5. **Quasi-static separation.** Loading is slow compared with the event, so the
   two problems decouple. This fails for slow earthquakes and for rupture
   propagation itself, which is dynamic.
6. **Pure shear loading on a pre-existing plane.** No out-of-plane stress
   rotation, no fault growth, no interaction with neighbouring faults.
7. **Constant friction coefficient.** $\mu_s$ in reality depends on slip,
   slip rate and history; rate-and-state friction replaces the constant used in
   Section 3.5.
8. **The stress drop is released entirely seismically.** In the energy ledger of
   [06](06-rupture-dynamics.md) only part of it becomes radiated energy.

**Consequence.** The model predicts a *mean* interval given a *median* stress
drop, and nothing more. Quotes such as "this fault ruptures every 34 years"
should be read as "under these SYNTHETIC, uniform assumptions the mean is
34 years", with the sensitivity computed next.

## 6. Units and dimensional analysis

| Quantity | Expression | Units | Check |
|---|---|---|---|
| strain rate | $V/W$ | $\mathrm{m\,s^{-1}}/\mathrm{m} = \mathrm{s^{-1}}$ | a velocity over a length is a rate ✔ |
| loading rate | $\mu V/W$ | $\mathrm{Pa}\times\mathrm{s^{-1}} = \mathrm{Pa\,s^{-1}}$ | ✔ |
| interval | $\Delta\tau/\dot\tau$ | $\mathrm{Pa}/(\mathrm{Pa\,s^{-1}}) = \mathrm{s}$ | ✔ |
| slip | $\Delta\tau W/\mu$ | $\mathrm{Pa}\cdot\mathrm{m}/\mathrm{Pa} = \mathrm{m}$ | ✔ |
| moment | $\mu A D$ | $\mathrm{Pa}\cdot\mathrm{m^2}\cdot\mathrm{m} = \mathrm{N\,m}$ | since $\mathrm{Pa} = \mathrm{N\,m^{-2}}$ ✔ |
| moment rate | $\mu A V$ | $\mathrm{N\,m}\cdot\mathrm{s^{-1}}$ | ✔ |

One trap: the interval is often wanted in years while $V$ is given in
$\mathrm{mm\,a^{-1}}$. Mixing $\mathrm{mm\,a^{-1}}$ with metres in $W$ introduces a
factor $10^{3}$; the demo keeps everything in metres and years and prints the
$\mathrm{Pa\,s^{-1}}$ rate as a second line so the conversion is visible.

## 7. Worked examples

### Example 1 — doubling the stress drop

Take the demo scenario but let the fault release $\Delta\tau = 6.0\ \mathrm{MPa}$
(twice the printed value) with everything else unchanged.

1. The loading rate is unchanged: $\dot\tau = 8.7500\times10^{4}\ \mathrm{Pa\,a^{-1}}$.
2. The interval doubles: $T = 6.0\times10^{6}/8.7500\times10^{4} = 68.57\ \mathrm{a}$.
3. The slip doubles: $D = \Delta\tau W/\mu = 6.0\times10^{6}\times1.2\times10^{4}
   /3.0\times10^{10} = 2.400\ \mathrm{m}$, and indeed $VT = 3.5\times10^{-2}
   \times68.571 = 2.400\ \mathrm{m}$.
4. The moment doubles: $M_0 = 3.0\times10^{10}\times4.8\times10^{8}\times2.400
   = 3.456\times10^{19}\ \mathrm{N\,m}$.
5. The **moment rate is unchanged**: $\mu A V = 5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}}$,
   and $M_0/T = 3.456\times10^{19}/68.571 = 5.0400\times10^{17}$ ✔.

**Lesson.** A factor-2 change in stress drop moves the interval and the event
size by a factor 2 and leaves the long-term moment rate alone. Stress drop is the
most poorly constrained of the four inputs and the one that most strongly biases
*individual-event* statements.

### Example 2 — how much pore pressure to trigger?

The fault has just failed and released $3.0\ \mathrm{MPa}$; the loading rate is
$8.7500\times10^{4}\ \mathrm{Pa\,a^{-1}}$. A nearby operation raises the pore
pressure by $1.0\ \mathrm{MPa}$.

1. Coulomb leverage: $\Delta CFF = \mu_s\Delta p = 0.60\times1.0 = 0.60\ \mathrm{MPa}$.
2. Time that the same stress would have taken to rebuild:
   $0.60\times10^{6}/8.7500\times10^{4} = 6.857\ \mathrm{a}$.
3. So a $1\ \mathrm{MPa}$ pressure rise is worth about $6.9$ years of tectonic
   loading — the quantitative version of the statement that human operations can
   advance the clock.

The mechanism, its limits and its non-uniqueness are developed in
[06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/01-induced-seismicity-causes.md).

### Example 3 — the stress ratio at two depths

With $\rho = 2700\ \mathrm{kg\,m^{-3}}$ and $g = 9.80665\ \mathrm{m\,s^{-2}}$,
the lithostatic stress at depth $z$ is $\rho g z$.

- At $z = 10\ \mathrm{km}$: $\sigma_v = 2700\times9.80665\times10^{4}
  = 2.648\times10^{8}\ \mathrm{Pa} = 264.8\ \mathrm{MPa}$, ratio $0.0113$.
- At $z = 5\ \mathrm{km}$: $\sigma_v = 1.324\times10^{8}\ \mathrm{Pa}
  = 132.4\ \mathrm{MPa}$, ratio $3.0/132.4 = 0.0227$.

The ratio grows towards the surface because $\sigma_v$ grows with depth while
$\Delta\tau$ in this model does not. Both values are of order $10^{-2}$; that
order, not the exact number, is what the "small stress drop" statement means.

## 8. Python demonstration

[`code/faulting_and_slip_demo.py`](code/faulting_and_slip_demo.py) computes all
of the above and prints labelled results with units:

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python faulting_and_slip_demo.py
```

It has five numbered parts:

1. **Stress accumulation and the recurrence interval.** It integrates the
   loading numerically over 300 steps of $\mathrm{d}t = 3.429\times10^{-1}\
   \mathrm{a}$, records event times $34.29$, $68.57$, $102.86\ \mathrm{a}$, and
   compares the mean interval with $\Delta\tau/\dot\tau$: relative difference
   $2.69\times10^{-15}$.
2. **Slip deficit and coseismic slip.** $VT = 1.200\ \mathrm{m}$ against
   $\Delta\tau W/\mu = 1.200\ \mathrm{m}$, relative difference $1.85\times10^{-16}$.
3. **Seismic moment and moment rate.** $M_0 = 1.7280\times10^{19}\ \mathrm{N\,m}$;
   moment rate $5.0400\times10^{17}\ \mathrm{N\,m\,a^{-1}}$ from both routes,
   relative difference $1.27\times10^{-16}$.
4. **Stress drop against ambient stress.** $\sigma_v = 264.8\ \mathrm{MPa}$ and
   $\Delta\tau/\sigma_v = 0.0113$.
5. **Coulomb failure under a pore-pressure change.** The five-row table of
   Section 3.5 and the $5.00\ \mathrm{MPa}$ trigger pressure.

**What the checks mean.** The three printed residuals compare a *closed form*
against an *independent computation* (a time integration, or a second algebraic
route). Values near $10^{-15}$ say the arithmetic agrees, not that the physics is
right — the physics is carried entirely by the labelled inputs.

## 9. Exercises

Full problem sets with worked solutions:

- [`exercises/01-faulting-and-slip-exercises.md`](exercises/01-faulting-and-slip-exercises.md)
- [`exercises/01-faulting-and-slip-solutions.md`](exercises/01-faulting-and-slip-solutions.md)

They span three tiers (foundational, applied, research-oriented) and use the
synthetic values of the demo throughout.

## 10. Real-world applications

- **Fault slip-rate budgets.** Comparisons of geodetic strain rates with
  catalogue moment release use exactly $\mu A V$ against $M_0/T$, and the
  shortfall is interpreted as aseismic slip or missing small events.
- **Recurrence-interval estimates.** Paleoseismic trenching measures $D$ and $T$
  at a point; the model converts them to $M_0$ and hence to a hazard input.
- **Induced seismicity.** Reservoir impoundment, fluid injection and extraction
  change $p$; the Coulomb term in Section 3.5 is the first-order criterion for
  whether a fault is brought closer to failure.
- **Coulomb stress transfer.** The same $CFF$ is used with an elastic
  dislocation model to test whether one event is promoted or delayed by a
  neighbouring one.
- **Aseismic and slow slip.** Where the model fails, the failure is informative:
  the moment budget reveals slip that does not radiate earthquakes.

## 11. Further reading

- **Reid, H. F. (1910). The mechanism of the earthquake.** In *The California
  Earthquake of April 18, 1906*, Carnegie Institution of Washington, vol. 2.
  Level: research/historical. The origin of elastic rebound; read for the
  argument, not the numbers.
- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. The standard source for the moment tensor, the Coulomb
  framework and the notation used throughout this module.
- **Kanamori, H., & Anderson, D. L. (1975). Theoretical basis of some empirical
  relations in seismology.** *Bulletin of the Seismological Society of America*.
  Level: research. The scaling relations that connect $M_0$, area and stress
  drop.
- **Scholz, C. H. (2019). *The Mechanics of Earthquakes and Faulting*.** Level:
  graduate textbook. Friction, the seismic cycle and fault-zone structure,
  including the places where the block-slider model fails.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC strike-slip fault has $\mu = 3.0\times10^{10}\ \mathrm{Pa}$,
> $W = 12.0\ \mathrm{km}$, $V = 20.0\ \mathrm{mm\,a^{-1}}$ and a mean stress drop
> of $2.0\ \mathrm{MPa}$. **(a)** Compute the loading rate in
> $\mathrm{Pa\,a^{-1}}$. **(b)** Compute the mean recurrence interval. **(c)**
> Compute the coseismic slip two ways and check that they agree. **(d)** Compute
> $M_0$ for a $30\ \mathrm{km}\times12\ \mathrm{km}$ rupture and the fault's
> moment rate. **(e)** State in one sentence why (b) is a mean and not a
> prediction, naming two of the assumptions in Section 5 that fail in reality.
> **(f)** A $2\ \mathrm{MPa}$ pore-pressure rise is proposed; compute the
> equivalent advance of the seismic cycle in years using $\mu_s = 0.60$, and
> state the one assumption this uses.

## Common pitfalls

1. **Treating the recurrence interval as a clock.** In this model it is exactly
   periodic; in reality quasi-periodic at best and often clustered.
2. **Quoting $M_0$ without saying which $\Delta\tau$, $A$ and $D$ produced it.**
   $M_0$ is a product of three quantities, two of which are model choices.
3. **Confusing the moment rate with the moment.** $\mu A V$ is independent of how
   the slip is parcelled into events; $M_0$ is not.
4. **Forgetting that stress drop is an average.** $\Delta\tau$ hides the spatial
   variation that controls where rupture starts and stops.
5. **Mixing units in the recurrence calculation.** $\mathrm{mm\,a^{-1}}$ with
   km introduces a factor $10^{3}$; convert once, and state the year length used
   ($3.15576\times10^{7}\ \mathrm{s}$).
6. **Reading $CFF$ as an absolute statement.** It is a *change* criterion; a
   positive $\Delta CFF$ means "closer to failure", not "will break".

## Related modules

- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  what is actually measured from a seismogram, and how $M_0$ becomes a magnitude.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  why the radiated energy seen at a distance is a filtered version of the source.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  how the moment rate of this lesson becomes a probability.
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/01-induced-seismicity-causes.md) —
  pore pressure and the Coulomb criterion in practice.
- [04-structural-geology/04 Structural Geology](../../04-earth-science-geology/04-structural-geology/README.md) —
  fault geometry and kinematics as mapped in the field.
- [02 Double-Couple](02-double-couple.md) — next lesson: what the radiated
  wavefield of a slipping fault looks like.
