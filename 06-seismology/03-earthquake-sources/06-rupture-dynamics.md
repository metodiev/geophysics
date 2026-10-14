---
id: 06-03-06
title: "Rupture Dynamics, Fracture Energy and Scaling Laws"
level: doctoral
prereqs: ["06-03-04", "06-03-05"]
tags: [seismology, rupture-dynamics, fracture-energy, scaling-laws, radiation-efficiency]
---

# Rupture Dynamics, Fracture Energy and Scaling Laws

> **All models and data in this module are SYNTHETIC.** Every exponent, slip and
> energy below is produced by
> [`code/rupture_dynamics_demo.py`](code/rupture_dynamics_demo.py) from chosen
> teaching parameters ($\beta = 3500\ \mathrm{m\,s^{-1}}$,
> $\mu = 3.0\times10^{10}\ \mathrm{Pa}$, seismogenic width
> $W_{\max} = 15\ \mathrm{km}$, model constant $k = 0.37$, slip-weakening friction
> with $\tau_p = 80\ \mathrm{MPa}$, $\tau_0 = 81\ \mathrm{MPa}$,
> $D_c = 0.50\ \mathrm{m}$). No real earthquake, energy estimate or catalogue is
> quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the self-similar exponents $M_0\propto a^{3}$, $f_c\propto a^{-1}$
   and hence $M_0\propto f_c^{-3}$ from the circular-crack relations, and
   **measure** them from a synthetic population.
2. **Show** how a finite seismogenic width breaks self-similarity and
   **compute** the saturation corner frequency $f_{c,\text{sat}} = k\beta/(W_{\max}/2)$.
3. **Explain** why a stress drop inferred from a saturated event with the $-3$ law
   is an *underestimate*, and that the bias grows with moment.
4. **Derive** the quasi-dynamic slip-weakening equation
   $\dot D = (\tau_e(D)-\tau_s(D))/\eta$ with $\eta = \mu/(2\beta)$.
5. **Verify** the radiated-energy identity
   $E_R = \int(\tau_e-\tau_s)\,\mathrm{d}D = \int\eta V^{2}\,\mathrm{d}t$ against
   the independent energy ledger, and **state** what the residual measures.
6. **Compute** the fracture energy $G_c = \tfrac12(\tau_p-\tau_r)D_c$ and the
   radiation efficiency $\eta_R = E_R/(E_R+G_c)$, and **explain** the direction of
   its dependence on $D_c$.
7. **Distinguish** a physical shortfall from an artefact of a truncated
   integration window, by testing whether a discrepancy is uniform across rows.

## Prerequisites

- [06-03-04 Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) —
  rupture speed and the kinematics that this lesson replaces with dynamics.
- [06-03-05 Source Spectra, Corner Frequency and Stress Drop](05-source-spectra.md) —
  the $M_0$–$f_c$ relations whose self-similarity is tested here.
- [06-03-01 Faulting, Slip and the Elastic Rebound Cycle](01-faulting-and-slip.md) —
  the stress drop and slip definitions used throughout.

## 1. Intuition: what stops a rupture, and what it costs

A rupture is a crack that runs. Two questions decide its size and its radiation:

- **What controls its dimension?** If there were no length scale, a rupture would
  be self-similar: every size would look the same, magnified. A real fault has a
  length scale — the depth range over which rock can store elastic strain — and
  once a rupture spans that range it cannot grow deeper. Growth becomes
  one-dimensional, and the scaling changes.
- **What does breaking cost?** Creating new surface consumes energy: friction
  must be overcome and the rock must weaken. Whatever is left over after the
  fracture bill is paid is **radiated** as seismic waves. The ratio of radiated to
  available energy is the **radiation efficiency**, and it is not a constant.

The lesson derives both, then measures them. Its honest difficulty is the second
one: the efficiency depends on a friction law nobody measures directly, and the
numerical integration that produces it has a finite window that can masquerade as
physics. The demo contains exactly such an artefact, and Section 7 shows how to
recognise it from the numbers alone.

## 2. Precise definitions

| Symbol | Meaning | Unit |
|---|---|---|
| $L$, $W$ | along-strike length, down-dip width | m |
| $W_{\max}$ | seismogenic (brittle) thickness | m |
| $a$ | effective radius used for the radiation length scale | m |
| $k$ | model constant in $f_c = k\beta/a$ | — |
| $\tau_0$ | initial shear stress | Pa |
| $\tau_p$, $\tau_r$ | peak (static) and residual (dynamic) strength | Pa |
| $D$, $D_c$ | slip, slip-weakening distance | m |
| $\eta$ | radiation damping coefficient, $\mu/(2\beta)$ | $\mathrm{Pa\,s\,m^{-1}}$ |
| $G_c$ | fracture energy per unit area | $\mathrm{J\,m^{-2}}$ |
| $E_R$ | radiated energy per unit area | $\mathrm{J\,m^{-2}}$ |
| $\eta_R$ | radiation efficiency $E_R/(E_R+G_c)$ | — |
| $\tau_e(D)$ | elastic unloading stress $\tau_0 - \kappa D$ | Pa |

The **slip-weakening** friction law used here is

$$\tau_s(D) =
\begin{cases}
\tau_p - (\tau_p-\tau_r)\,D/D_c, & D < D_c,\\[2pt]
\tau_r, & D \ge D_c,
\end{cases}$$

with fracture energy (the area under the weakening curve)

$$G_c = \int_0^{D_c}\!\left(\tau_s(D)-\tau_r\right)\mathrm{d}D
= \tfrac12\left(\tau_p-\tau_r\right)D_c.$$

The elastic unloading of the surrounding rock is modelled by a linear spring,
$\tau_e(D) = \tau_0 - \kappa D$, and the fault's motion is governed by **radiation
damping**: the stress difference drives slip at a rate proportional to it,

$$\eta \dot D = \tau_e(D) - \tau_s(D), \qquad \eta = \frac{\mu}{2\beta}.$$

This is the "quasi-dynamic" approximation: inertia is represented by a damping
term rather than by a wave equation, so the model gives the energy balance and the
final slip correctly while suppressing radiated oscillations.

## 3. Derivations

### 3.1 Self-similar scaling

For a circular crack with uniform stress drop the two relations are

$$M_0 = \frac{16}{7}\,\Delta\sigma\,a^{3}, \qquad f_c = \frac{k\beta}{a}.$$

Eliminating $a$:

$$M_0 \propto a^{3}, \qquad f_c \propto a^{-1}
\;\Longrightarrow\;
\boxed{\;M_0 \propto f_c^{-3},\quad
\frac{\mathrm{d}\log_{10}M_0}{\mathrm{d}\log_{10}f_c} = -3.\;}$$

The mean slip and the aspect of the scaling follow from
$M_0 = \mu\pi a^{2}\bar D$:

$$\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}\,a
\;\Longrightarrow\; \bar D \propto a.$$

So at constant stress drop, a ten-fold larger rupture slips ten times as far and
has a hundred times the area: the moment grows as $a^{3}$ and the corner falls as
$a^{-1}$.

*Numerical check.* The demo fits a synthetic population of circular ruptures
between radii $10\ \mathrm{m}$ and $10\ \mathrm{km}$ at constant
$\Delta\sigma = 3.0\ \mathrm{MPa}$ and reports

$$\frac{\mathrm{d}\log_{10}M_0}{\mathrm{d}\log_{10}f_c} = -3.000000,\qquad
\frac{\mathrm{d}\log_{10}a}{\mathrm{d}\log_{10}f_c} = -1.000000,\qquad
\frac{\mathrm{d}\log_{10}M_0}{\mathrm{d}\log_{10}a} = 3.000000.$$

Hand check with two points, $a = 10\ \mathrm{m}$ and $a = 10^{4}\ \mathrm{m}$:
$M_0 = (16/7)\times3.0\times10^{6}\,a^{3}$ gives
$2.2857\times3.0\times10^{9} = 6.8571\times10^{9}$ and
$6.8571\times10^{18}\ \mathrm{N\,m}$ (nine decades), and
$f_c = 1295/a$ gives $129.5$ and $0.1295\ \mathrm{Hz}$ (three decades). Then
$9/(-3) = -3$ ✔.

### 3.2 What breaks it: the finite seismogenic width

Now let the rupture be a rectangle of along-strike length $L$ and down-dip width
$W = \min(L,W_{\max})$. The radiated high frequencies are controlled by the
**smallest** dimension, so the radiation length scale is

$$a = \frac{\min(L,W_{\max})}{2}, \qquad
f_c = \frac{k\beta}{a} = \frac{2k\beta}{\min(L,W_{\max})},$$

while the moment uses the actual area and the slip set by the small dimension:

$$\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}a,\qquad
M_0 = \mu\,\bar D\,\times\!\begin{cases}\pi a^{2}, & L\le W_{\max},\\ L\,W, & L>W_{\max}.\end{cases}$$

Once $L>W_{\max}$ the radius is **pinned** at $a = W_{\max}/2$, so

$$\boxed{\;f_{c,\text{sat}} = \frac{2k\beta}{W_{\max}}
= \frac{0.37\times3500}{7500} = 0.17267\ \mathrm{Hz}.\;}$$

The moment, meanwhile, keeps growing linearly with $L$. The population therefore
has **two regimes**: exponent $-3$ while the rupture is self-similar, and a
vertical (constant-$f_c$) branch once the width saturates.

*Numerical check.* The demo's population:

| $L$ (km) | $W$ (km) | $a$ (km) | $f_c$ (Hz) | $M_0$ (N m) |
|---|---|---|---|---|
| 2.0 | 2.0 | 1.00 | 1.29500 | $6.8571\times10^{15}$ |
| 11.6 | 11.6 | 5.79 | 0.22364 | $1.3313\times10^{18}$ |
| 37.3 | 15.0 | 7.50 | 0.17267 | $9.1699\times10^{18}$ |
| 53.1 | 15.0 | 7.50 | 0.17267 | $1.3029\times10^{19}$ |
| 67.1 | 15.0 | 7.50 | 0.17267 | $1.6466\times10^{19}$ |
| 388.3 | 15.0 | 7.50 | 0.17267 | $9.5348\times10^{19}$ |
| 2000.0 | 15.0 | 7.50 | 0.17267 | $4.9111\times10^{20}$ |

The corner frequency stops falling at $0.17267\ \mathrm{Hz}$, $42$ of the $60$
sources sit at that value, and the moment spans
$6.86\times10^{15}$ to $4.91\times10^{20}\ \mathrm{N\,m}$. The local slope reported
for the row near $L = 11.6\ \mathrm{km}$ is $-3.621$, not $-3$, because the
transition region is not a power law at all.

**Consequence.** Any stress drop inferred from $f_c$ using the $-3$ law is an
**underestimate** for saturated events: the measured $f_c$ is larger than the
self-similar law predicts for that $M_0$, so $\Delta\sigma\propto M_0f_c^{3}$ comes
out too small, and the bias grows without bound as $M_0$ grows.

### 3.3 The quasi-dynamic energy balance

Substituting the friction and unloading laws into radiation damping gives a
first-order equation for the slip,

$$\eta\dot D = \tau_0 - \kappa D - \tau_s(D),$$

and the radiated energy per unit area is the dissipation in the damping term:

$$E_R = \int \eta V^{2}\,\mathrm{d}t = \int \left(\tau_e(D)-\tau_s(D)\right)\mathrm{d}D.$$

The same quantity is obtained independently from the **ledger**: work done by the
elastic stress minus frictional dissipation,

$$E_R^{\text{ledger}}
= \underbrace{\int \tau_e\,\mathrm{d}D}_{\text{work}}
- \underbrace{\int \tau_s\,\mathrm{d}D}_{\text{friction}},$$

with, for the linear spring and the bilinear friction law,

$$\int \tau_e\,\mathrm{d}D = \tau_0 D - \tfrac12\kappa D^{2},$$

$$\int_0^{D_c}\!\tau_s\,\mathrm{d}D = \tau_p D - \frac{(\tau_p-\tau_r)}{2D_c}D^{2}
\quad (D\le D_c),$$

and for $D>D_c$ the weakening integral is evaluated to $D_c$ and the rest at the
constant residual stress. The two routes are **algebraically independent**, so
their agreement is a genuine check of the code.

*Numerical check.* The demo starts the fault $1\ \mathrm{MPa}$ above its peak
strength ($\tau_0 = 81\ \mathrm{MPa}$, $\tau_p = 80\ \mathrm{MPa}$) and integrates
with $\mathrm{d}t = 10^{-5}\ \mathrm{s}$, reporting for
$\tau_r = 10,\ 30,\ 50,\ 70\ \mathrm{MPa}$:

| $\tau_r$ (MPa) | $D_f$ (m) | $G_c$ ($\mathrm{J\,m^{-2}}$) | $E_R$ numeric | $E_R$ ledger | residual | $\eta_R$ |
|---|---|---|---|---|---|---|
| 10 | 111.0353 | $1.75\times10^{7}$ | $4.1674\times10^{9}$ | $4.1674\times10^{9}$ | $2.53\times10^{-9}$ | 0.9958 |
| 30 | 79.7383 | $1.25\times10^{7}$ | $2.1467\times10^{9}$ | $2.1467\times10^{9}$ | $2.38\times10^{-9}$ | 0.9942 |
| 50 | 48.4457 | $7.50\times10^{6}$ | $7.9022\times10^{8}$ | $7.9022\times10^{8}$ | $2.00\times10^{-9}$ | 0.9906 |
| 70 | 17.1664 | $2.50\times10^{6}$ | $9.7925\times10^{7}$ | $9.7925\times10^{7}$ | $3.05\times10^{-9}$ | 0.9751 |

The residual column, $\lvert E_R^{\text{numeric}}-E_R^{\text{ledger}}\rvert/E_R$,
is $2$–$3\times10^{-9}$: the error of the time integration, and the only number in
the table that is not a property of the model. The two energy routes agree, as the
energy identity requires.

### 3.4 The truncation artefact in the $D_f$ column

There is one more thing to read in that table, and the demo's own narrative gets
it wrong, so it is worth doing carefully.

The arrest condition is
$\tau_e = \tau_r$, i.e. $D_{\text{arrest}} = (\tau_0-\tau_r)/\kappa$:

$$\tau_r = 10:\ 118.33\ \mathrm{m};\quad 30:\ 85.00\ \mathrm{m};\quad
50:\ 51.67\ \mathrm{m};\quad 70:\ 18.33\ \mathrm{m}.$$

The printed $D_f$ values are $111.0353$, $79.7383$, $48.4457$, $17.1664$. Form the
ratios $D_f/D_{\text{arrest}}$:

$$0.9383,\quad 0.9381,\quad 0.9377,\quad 0.9364.$$

They are the **same** to three parts in a thousand. A source of error that is
*proportional* to the quantity, with the *same* constant across rows, is not a
physical effect — it is a fixed integration window. The demo's first energy loop
runs at most $2\times10^{6}$ steps of $\mathrm{d}t = 10^{-5}\ \mathrm{s}$, i.e.
$20\ \mathrm{s}$, and the post-weakening approach to arrest is exponential with
time constant $\eta/\kappa = 4.2857\times10^{6}/6.0\times10^{5} = 7.14\ \mathrm{s}$.
Hence the slip at the end of the window falls short of the asymptote by a factor
$\approx e^{-20/7.14} = 0.061$, i.e. $6.1\%$ — the measured $6.2$–$6.4\%$.

**So the printed $D_f$ is the slip at the end of a $20\ \mathrm{s}$ window, not
the arrest slip**, and the demo's claim that it "matches $(\tau_0-\tau_r)/\kappa$
to the same accuracy" is not what its own numbers show. The second loop in the
demo uses $4\times10^{6}$ steps ($40\ \mathrm{s}$) and therefore comes within
$0.4$–$0.9\%$ of $85.00\ \mathrm{m}$ — the same physics, a longer window.

The general rule this illustrates: **before attributing a discrepancy to physics,
test whether it is uniform across the population.** A constant fractional offset
is almost always a window, a tolerance or a unit.

### 3.5 Radiation efficiency and its dependence on $D_c$

With $E_R$ and $G_c$ both known, the **radiation efficiency** is

$$\eta_R = \frac{E_R}{E_R+G_c}.$$

Scanning the weakening distance at fixed strengths
($\tau_0 = 81\ \mathrm{MPa}$, $\tau_r = 30\ \mathrm{MPa}$, so
$D_{\text{arrest}} = 85.00\ \mathrm{m}$):

| $D_c$ (m) | $D_f$ (m) | $G_c$ ($\mathrm{J\,m^{-2}}$) | $E_R$ ($\mathrm{J\,m^{-2}}$) | $\eta_R$ |
|---|---|---|---|---|
| 0.10 | 84.6846 | $2.50\times10^{6}$ | $2.1650\times10^{9}$ | 0.9988 |
| 1.00 | 84.6742 | $2.50\times10^{7}$ | $2.1425\times10^{9}$ | 0.9885 |
| 5.00 | 84.6212 | $1.25\times10^{8}$ | $2.0425\times10^{9}$ | 0.9423 |
| 20.00 | 84.2356 | $5.00\times10^{8}$ | $1.6673\times10^{9}$ | 0.7693 |
| 60.00 | 33.5428 | $1.50\times10^{9}$ | $1.6481\times10^{8}$ | 0.0990 |

For the first four rows the same strength drop and the same stiffness give
different efficiencies: as $D_c$ grows, more work goes into the fracture term and
less is radiated. Hand check of the last two columns for $D_c = 0.10$:
$G_c = \tfrac12(80-30)\times10^{6}\times0.10 = 2.5\times10^{6}\ \mathrm{J\,m^{-2}}$
✔ and $\eta_R = 2.1650\times10^{9}/(2.1650\times10^{9}+2.5\times10^{6}) = 0.99885$
✔.

**A caveat that must be stated.** The last row is *not* a completed event. With
$D_c = 60\ \mathrm{m}$ the second loop's $40\ \mathrm{s}$ window ends while the
slip is still $33.54\ \mathrm{m}$, below $D_c$: weakening is unfinished, and the
efficiency is computed against a fracture energy the event did not fully pay. So
the row's $D_f$ and $\eta_R$ are properties of a truncated computation, and the
trend they suggest must be read off the first four rows (which come within
$0.4$–$0.9\%$ of arrest). The direction of the trend — efficiency falling with
$D_c$ — is model-independent; the absolute values are not.

**Why $\eta_R$ is near 1 for small $D_c$.** The numbers say it directly: the
final slip is $17$–$111\ \mathrm{m}$ against a weakening distance of
$0.5\ \mathrm{m}$. The fracture term is a rounding error on the work, so almost
everything is radiated. Efficiency is low when an event is *small relative to its
own weakening distance*.

## 4. Physical interpretation

**Self-similarity is not an assumption about physics; it is an assumption about
the absence of a length scale.** A population of cracks with constant stress drop
and no preferred size is self-similar by construction, and the $-3$ exponent
follows. The interesting content is therefore not the exponent but its
**breakdown**: the seismogenic width is a length scale, and the saturated branch
is where the law bends.

**Stress drop from $f_c$ is biased upward in size, downward in stress.** Because
the saturated $f_c$ is larger than the $-3$ law predicts, the standard estimator
$\Delta\sigma\propto M_0f_c^{3}$ underestimates stress drop for large events, and
by more as the event grows.

**Fracture energy is a friction property.** $G_c$ depends on how far strength
drops and over what slip distance — quantities of the friction law, not of the
elasticity. It is the least constrained part of every energy budget.

**Radiated energy is the residual, not the input.** The identity
$E_R = \int(\tau_e-\tau_s)\mathrm{d}D$ says that radiation is whatever the
fracture process leaves behind. That is why $E_R$ is hard to predict and why
efficiency varies.

**The apparent stress.** Dividing the radiated energy by the moment gives a
stress-like quantity (twice the apparent stress, $\tau_a = \mu E_R/M_0$). It is a
*measured* ratio, unlike $\Delta\sigma$, which needs a length scale and a model
constant.

## 5. Assumptions and regime of validity

1. **Quasi-dynamic radiation damping.** Inertia is modelled by $\eta V$, not by a
   wave equation. This gives the energy balance and final slip but suppresses
   oscillations, overshoot dynamics and rupture-front waves.
2. **Linear slip-weakening friction.** Real friction is rate- and
   state-dependent and heals; a constant $D_c$ and a bilinear curve are a
   parameterisation.
3. **Prescribed elastic unloading.** A linear spring, single-degree-of-freedom;
   no spatial stress heterogeneity, no barriers.
4. **Smallest dimension controls $f_c$.** A model statement, labelled as such in
   the demo.
5. **Uniform $\Delta\sigma$ and $k$.** Both are assumed constant across the size
   range; the whole saturation argument depends on the stress drop not varying
   with size.
6. **One mode of slip.** No opening, no branching, no off-fault damage.
7. **Adiabatic separation of timescales.** $D_c$ is assumed fixed during the
   event; thermal pressurisation and other weakening mechanisms are excluded.

**Consequence and non-uniqueness.** $\eta_R$, $G_c$ and $D_c$ are all inferences
from the same sampled data (seismic spectra and geodesy), and they trade off: a
larger $D_c$ can be compensated by a larger strength drop at fixed radiated
energy. Absolute energy budgets are therefore model-dependent; *ratios* within a
population are far more robust.

## 6. Units and dimensional analysis

| Quantity | Expression | Unit | Check |
|---|---|---|---|
| $\eta = \mu/(2\beta)$ | $\mathrm{Pa}/(\mathrm{m\,s^{-1}})$ | $\mathrm{Pa\,s\,m^{-1}}$ | ✔ |
| $\eta\dot D$ | $\mathrm{Pa\,s\,m^{-1}}\times\mathrm{m\,s^{-1}} = \mathrm{Pa}$ | a stress ✔ |
| $V = (\tau_e-\tau_s)/\eta$ | $\mathrm{Pa}/(\mathrm{Pa\,s\,m^{-1}}) = \mathrm{m\,s^{-1}}$ | ✔ |
| $G_c$ | $\mathrm{Pa}\times\mathrm{m} = \mathrm{J\,m^{-2}}$ | ✔ |
| $E_R = \int(\tau_e-\tau_s)\mathrm{d}D$ | $\mathrm{Pa}\times\mathrm{m} = \mathrm{J\,m^{-2}}$ | ✔ |
| $E_R = \int\eta V^{2}\mathrm{d}t$ | $\mathrm{Pa\,s\,m^{-1}}\mathrm{m^{2}s^{-2}}\mathrm{s} = \mathrm{Pa\,m}$ | $\mathrm{J\,m^{-2}}$ ✔ |
| $f_{c,\text{sat}}$ | $(2k\beta)/W_{\max}$ | $\mathrm{s^{-1}}$ | ✔ |
| $\eta_R$ | ratio of energies | — | ✔ |

The two expressions for $E_R$ having the same units is the dimensional shadow of
the identity proved in Section 3.3.

## 7. Worked examples

### Example 1 — the self-similar triple

Take $a = 10\ \mathrm{m}$, $\Delta\sigma = 3.0\ \mathrm{MPa}$,
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $k = 0.37$:

$$M_0 = \tfrac{16}{7}\Delta\sigma a^{3}
= 2.2857\times3.0\times10^{6}\times10^{3} = 6.8571\times10^{9}\ \mathrm{N\,m},$$
$$f_c = \frac{k\beta}{a} = \frac{1295}{10} = 129.5\ \mathrm{Hz},$$
$$\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}a
= 0.727575\times1.0\times10^{-4}\times10 = 7.2758\times10^{-4}\ \mathrm{m}.$$

Now take $a = 10^{4}\ \mathrm{m}$: $M_0 = 6.8571\times10^{18}\ \mathrm{N\,m}$,
$f_c = 0.1295\ \mathrm{Hz}$, $\bar D = 0.72758\ \mathrm{m}$. Moment and slip
changed by $10^{9}$ and $10^{3}$ — the exponents $3$ and $1$ in one step.

### Example 2 — the saturation corner

$$f_{c,\text{sat}} = \frac{2k\beta}{W_{\max}}
= \frac{2\times0.37\times3500}{15\,000} = \frac{2590}{15\,000}
= 0.17267\ \mathrm{Hz}.$$

For any $L>W_{\max} = 15\ \mathrm{km}$, $a = 7.5\ \mathrm{km}$ and $f_c$ stays at
this value while $M_0\propto L$. Going from the $L = 37.3\ \mathrm{km}$ row
($M_0 = 9.17\times10^{18}$) to the $L = 388.3\ \mathrm{km}$ row
($M_0 = 9.53\times10^{19}$) is a factor $10.4$ in moment at **constant** $f_c$.

### Example 3 — fracture energy and efficiency by hand

For $\tau_r = 10\ \mathrm{MPa}$, $D_c = 0.50\ \mathrm{m}$:

$$G_c = \tfrac12(80-10)\times10^{6}\times0.50 = 17.5\times10^{6}
= 1.75\times10^{7}\ \mathrm{J\,m^{-2}},$$

matching the demo. With $E_R = 4.1674\times10^{9}\ \mathrm{J\,m^{-2}}$:

$$\eta_R = \frac{4.1674\times10^{9}}{4.1674\times10^{9}+1.75\times10^{7}}
= \frac{4.1674}{4.1849} = 0.99582 \approx 0.9958,$$

matching the demo. Note how small $G_c$ is compared with $E_R$: the fracture term
is $0.42\%$ of the radiated energy.

### Example 4 — diagnosing the truncated integration

For $\tau_r = 10\ \mathrm{MPa}$ the arrest slip is
$(\tau_0-\tau_r)/\kappa = 71\times10^{6}/6.0\times10^{5} = 118.33\ \mathrm{m}$, but
the demo prints $D_f = 111.0353\ \mathrm{m}$. The shortfall is
$7.30\ \mathrm{m}$, i.e. $6.17\%$. Repeat for the other three rows:

| $\tau_r$ (MPa) | $D_{\text{arrest}}$ (m) | $D_f$ printed (m) | $D_f/D_{\text{arrest}}$ |
|---|---|---|---|
| 10 | 118.33 | 111.0353 | 0.9383 |
| 30 | 85.00 | 79.7383 | 0.9381 |
| 50 | 51.67 | 48.4457 | 0.9377 |
| 70 | 18.33 | 17.1664 | 0.9364 |

The ratio is constant to $0.2\%$. With a fixed $20\ \mathrm{s}$ window and
time constant $\eta/\kappa = 7.14\ \mathrm{s}$ the predicted shortfall is
$e^{-20/7.14} = 0.0612$, i.e. a ratio $0.9388$ — the measured $0.936$–$0.938$.
**The shortfall is the window, not the physics.**

### Example 5 — efficiency versus $D_c$ from the printed numbers

For $D_c = 5.00\ \mathrm{m}$, $G_c = 1.25\times10^{8}\ \mathrm{J\,m^{-2}}$ and
$E_R = 2.0425\times10^{9}\ \mathrm{J\,m^{-2}}$:

$$\eta_R = \frac{2.0425\times10^{9}}{2.0425\times10^{9}+1.25\times10^{8}}
= \frac{2.0425}{2.1675} = 0.9423,$$

matching the demo. Between $D_c = 0.10\ \mathrm{m}$ ($\eta_R = 0.9988$) and
$D_c = 5.00\ \mathrm{m}$ ($0.9423$) the fracture term rises from $0.1\%$ to $5.8\%$
of the total energy budget.

## 8. Python demonstration

[`code/rupture_dynamics_demo.py`](code/rupture_dynamics_demo.py):

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rupture_dynamics_demo.py
```

Four numbered parts:

1. **Self-similar scaling.** The three fitted exponents $-3.000000$,
   $-1.000000$, $3.000000$.
2. **The saturation branch.** The $L$–$W$–$a$–$f_c$–$M_0$ table, the pinned
   $f_c = 0.17267\ \mathrm{Hz}$, the count $42$ of $60$ saturated sources, and the
   moment range $6.86\times10^{15}$–$4.91\times10^{20}\ \mathrm{N\,m}$.
3. **Energy.** The slip-weakening integration, the two energy routes with
   residuals $2$–$3\times10^{-9}$, and the efficiency table. (Read the $D_f$
   column with Section 3.4 in hand: it is the slip at the end of the integration
   window.)
4. **Efficiency versus weakening distance.** The five-row $D_c$ scan, of which
   the first four arrest and the last is truncated.

The demo's closing note is worth taking literally: the exponents and the energy
residual are *measured*; the model constants ($16/7$, $k$, the friction law, the
small-dimension control of $f_c$) are *inputs*.

## 9. Exercises

- [`exercises/06-rupture-dynamics-exercises.md`](exercises/06-rupture-dynamics-exercises.md)
- [`exercises/06-rupture-dynamics-solutions.md`](exercises/06-rupture-dynamics-solutions.md)

## 10. Real-world applications

- **Radiated-energy estimates.** $E_R$ and the apparent stress are used to
  compare earthquakes, explosions and induced events on an energy footing.
- **Stress-drop systematics.** The saturation branch is why stress drops inferred
  from corner frequencies must be checked against event size.
- **Ground-motion simulation.** Rupture dynamics supplies the slip and rise-time
  distributions that scenario simulations assume.
- **Scaling-law construction.** Empirical magnitude–area–slip relations are
  regressions across the self-similar and saturated branches, and the kink is a
  physical feature.
- **Fault-zone energy budgets.** Partitioning the available energy between
  fracture, friction and radiation is the framework for comparing inferred
  parameters with laboratory friction.

## 11. Further reading

- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. The energy balance and the kinked-crack scaling.
- **Kanamori, H., & Anderson, D. L. (1975). Theoretical basis of some empirical
  relations in seismology.** *Bulletin of the Seismological Society of America*.
  Level: research. Stress drop, apparent stress and the scaling relations.
- **Scholz, C. H. (2019). *The Mechanics of Earthquakes and Faulting*.** Level:
  graduate textbook. Slip-weakening friction, fracture energy and the
  seismogenic-width saturation.
- **Eshelby, J. D. (1957). The determination of the elastic field of an
  ellipsoidal inclusion.** *Proceedings of the Royal Society A*. Level: research.
  The $16/7$ circular-crack relation used throughout.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC fault has $W_{\max} = 12\ \mathrm{km}$,
> $\Delta\sigma = 4.0\ \mathrm{MPa}$, $\mu = 3.0\times10^{10}\ \mathrm{Pa}$,
> $\beta = 3500\ \mathrm{m\,s^{-1}}$, $k = 0.37$. **(a)** Compute
> $f_{c,\text{sat}}$. **(b)** For $L = 8\ \mathrm{km}$ compute $a$, $f_c$, the
> slip and $M_0$; repeat for $L = 40\ \mathrm{km}$ and state which branch each is
> on. **(c)** State the exponent of $M_0$ versus $f_c$ in each branch. **(d)**
> Explain why a stress drop inferred from $f_c$ for the $L = 40\ \mathrm{km}$
> event with the $-3$ law would be biased, and in which direction.
> **(e)** With $\tau_p = 80\ \mathrm{MPa}$, $\tau_r = 40\ \mathrm{MPa}$ and
> $D_c = 2.0\ \mathrm{m}$, compute $G_c$. **(f)** Given $E_R = 1.5\times10^{9}\
> \mathrm{J\,m^{-2}}$, compute $\eta_R$ and state which of $G_c$ and $E_R$ is the
> more uncertain in reality, and why.

## Common pitfalls

1. **Assuming one $M_0$–$f_c$ exponent.** The population is kinked at $L = W_{\max}$.
2. **Using the $-3$ law on saturated events.** The stress drop comes out too
   small, and the bias grows with size.
3. **Reading the printed $D_f$ as the arrest slip.** It is the slip at the end of
   a finite integration window, uniformly $\approx6\%$ short.
4. **Attributing a uniform fractional offset to physics.** A constant ratio
   across a population is almost always a numerical window or a unit.
5. **Treating $G_c$ as well constrained.** It is the weakest link in the energy
   budget.
6. **Quoting $\eta_R$ from a truncated event.** If the slip has not reached
   $D_c$, the event has not paid its fracture bill.
7. **Comparing radiated energies without stating the frequency band.** Real
   $E_R$ estimates are band-limited and therefore model-corrected.

## Related modules

- [05 Source Spectra, Corner Frequency and Stress Drop](05-source-spectra.md) —
  the relations whose self-similarity is tested here.
- [04 Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) —
  the kinematic picture that dynamics explains.
- [03 Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) —
  $M_0$ as the input to the energy budget.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  how moment and energy become reported magnitudes.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  how the scaling branches shape magnitude–frequency statistics.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  time integration and the truncation errors diagnosed in Section 3.4.
