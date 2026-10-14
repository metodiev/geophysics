---
id: 12-03-03
title: "Thermal Evolution of the Earth and Secular Cooling"
level: research
prereqs: ["12-03-01", "12-03-02", "02-06-06"]
tags: [global-geophysics, earth-interior, thermal-evolution, secular-cooling, urey-ratio, mantle-convection]
---

# Thermal Evolution of the Earth and Secular Cooling

**All models and data in this module are SYNTHETIC.** The rheology, the radiogenic
inventory, the heat loss and the core flux used below are adopted inputs of a
teaching model. They are representative rather than measured, no geological
province is implied, and every number in this lesson is printed by
[`code/thermal_evolution_demo.py`](./code/thermal_evolution_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** the one-box mantle energy balance and **identify** the three
   independent inputs it needs: production, core flux and transport efficiency.
2. **Calibrate** a convection parameterisation to a present-day flux and
   **explain** why that calibration removes a degree of freedom rather than
   adding one.
3. **Demonstrate** that a temperature-dependent viscosity buffers the mantle
   thermal state, and **quantify** how insensitive the present is to the initial
   condition.
4. **Compute** the Urey ratio and the secular cooling rate, and **distinguish**
   the quasi-static rate from the instantaneous budget rate.
5. **Measure** how the cooling rate depends on the assumed rheological
   sensitivity, and **report** the resulting range as an admitted uncertainty
   rather than as a number.
6. **Compare** the dynamic model's cooling rate with an independent
   whole-Earth inventory budget and **state** exactly what the agreement does and
   does not prove.
7. **Specify** the observation that would break the degeneracy between the
   model's parameters.

## Prerequisites

- [01 Radiogenic Heat Production and Mantle Geotherms](01-radiogenic-heat.md) —
  the inventory whose decay drives the whole evolution.
- [02 Heat Flow and Its Distribution](02-heat-flow-global.md) — the present-day
  heat loss that the model must reproduce.
- [02-06-06 Mantle Convection and Rayleigh-Benard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md) —
  the Rayleigh number and the Nusselt-number scaling used here as a
  parameterisation.

## 1. The problem

The Earth loses more heat at its surface than it produces radioactively. From
[02](02-heat-flow-global.md) the loss is about
$73.5\ \mathrm{mW\,m^{-2}}$ averaged over the whole surface, while the adopted
crustal and mantle production plus the core flux come to
$19.3 + 34.7 + 10.0 = 64.0\ \mathrm{mW\,m^{-2}}$. The difference,
$9.5\ \mathrm{mW\,m^{-2}}$, must come from **cooling**.

Two questions follow, and they are different questions.

1. **How fast is the Earth cooling now?** This is a present-day budget question.
   It needs the inventory and the heat loss, and it does not need a convection
   model.
2. **How did it get here?** This is an evolution question. It needs a transport
   law, an initial condition and $4.5\ \mathrm{Gyr}$ of integration, and its
   answer is a *history*, not a number.

This lesson keeps the two apart, because conflating them is the commonest error in
the subject. A cooling rate obtained by dividing a heat-flow deficit by a heat
capacity is a budget result. A cooling rate obtained by integrating a
parameterised convection model is a model result. They can be compared, and the
comparison is informative — but it is a consistency check between two models,
not a measurement of the Earth.

## 2. Precise definitions

### 2.1 The one-box balance

Treat the mantle as a single well-mixed box of potential temperature $T$, with
heat capacity per unit area $\rho c_p d$. Its energy balance is

$$\rho c_p d \frac{\mathrm{d}T}{\mathrm{d}t}
= H(t) + q_{\text{cmb}} - q_{\text{surf}}(T),$$

where $H(t) = A(t)\,d$ is the radiogenic flux per unit area,
$q_{\text{cmb}}$ is the flux supplied by the core, and $q_{\text{surf}}$ is the
mantle-derived surface flux. The **Urey ratio** is the ratio of production to
loss,

$$Ur = \frac{H}{q_{\text{surf}}},$$

and $Ur = 1$ means the mantle is in energetic equilibrium with no cooling at all.

### 2.2 The transport law

Parameterise convection exactly as in
[01](01-radiogenic-heat.md) §3.5, but let the viscosity depend on temperature:

$$\eta(T) = \eta_{\text{ref}}\exp\!\left[\frac{E_a}{R}\left(\frac1T -
\frac1{T_{\text{ref}}}\right)\right],\qquad
Ra = \frac{\rho\alpha g (T - T_s) d^3}{\kappa\,\eta(T)},\qquad
Nu = \left(\frac{Ra}{Ra_c}\right)^{\beta},$$

$$q_{\text{surf}}(T) = \frac{k\,(T-T_s)}{d}\,Nu .$$

Three parameters control everything: the reference viscosity $\eta_{\text{ref}}$,
the activation energy $E_a$ (the *strength* of the feedback) and the exponent
$\beta$. The adopted values are $\eta_{\text{ref}} = 1.499\times10^{21}\ \mathrm{Pa\,s}$,
$E_a = 300\ \mathrm{kJ\,mol^{-1}}$, $\beta = 1/3$, $Ra_c = 1100$.

### 2.3 Two cooling rates

- The **instantaneous budget rate**,
  $\left.\mathrm{d}T/\mathrm{d}t\right|_{\text{bud}} = (H + q_{\text{cmb}} - q_{\text{surf}})/(\rho c_p d)$:
  what the box does this instant, with its transport unchanged.
- The **quasi-static rate**,
  $\left.\mathrm{d}T/\mathrm{d}t\right|_{\text{qs}} = -\lambda H / (\mathrm{d}q/\mathrm{d}T)$
  with $\lambda = \ln 2/T_{1/2}$: what the box does once the transport has
  adjusted, i.e. after the fast transient has decayed.

They differ by exactly the amount by which the box is out of equilibrium, and
reporting only one of them is a common way to hide the distinction.

## 3. Derivations and results

### 3.1 Calibration fixes the viscosity

The reference viscosity is chosen so that the parameterisation reproduces an
adopted present-day mantle-derived flux of $55.0\ \mathrm{mW\,m^{-2}}$ at
$T = 1600\ \mathrm{K}$. Solving
$q_{\text{surf}}(1600\ \mathrm{K}) = 55.0\ \mathrm{mW\,m^{-2}}$ gives

$$\eta_{\text{ref}} = 1.499\times10^{21}\ \mathrm{Pa\,s},\qquad
Ra = 2.08\times10^{7},\qquad Nu = 26.6 .$$

This is an important methodological point rather than an arithmetic one. The
calibration **removes** a free parameter: after it, the model has no freedom left
to change the present-day flux, and any disagreement between the model and the
data must appear as a disagreement in something else (the temperature, the Urey
ratio or the cooling rate). A model that is calibrated to every observable has
nothing left to predict.

### 3.2 The buffering

The flux sensitivity defines a thermal response time,

$$\tau = \frac{\rho c_p d}{\mathrm{d}q/\mathrm{d}T} .$$

At the adopted state, $\mathrm{d}q/\mathrm{d}T = 0.3137\ \mathrm{mW\,m^{-2}\,K^{-1}}$,
so a 10 K error in temperature is a 5.7% flux error, and

$$\tau = 1.20\times10^{3}\ \mathrm{Myr} = 1.20\ \mathrm{Gyr}.$$

Compare this with the conduction time $d^2/\kappa = 2.65\times10^{5}\ \mathrm{Myr}$
— a factor of 220 longer. The viscosity feedback shortens the thermal response of
the mantle by two orders of magnitude, and this is why the mantle's temperature
is *buffered*: it adjusts to changes in production and transport on about a
billion years, not on the conduction timescale of the box.

Whether the present state remembers the initial condition is then simply a
comparison of $\tau$ with the age. Since $\tau/\text{age} \approx 0.27$, the
memory is partial, and the demonstration measures it:

| $T(0)$ (K) | $T(1\ \mathrm{Gyr})$ | $T(2\ \mathrm{Gyr})$ | $T(3\ \mathrm{Gyr})$ | $T(4.5\ \mathrm{Gyr})$ | $q(4.5\ \mathrm{Gyr})$ (mW m⁻²) |
|---|---|---|---|---|---|
| 1300 | 1470.6 | 1559.6 | 1588.2 | 1581.7 | 49.5 |
| 1600 | 1641.2 | 1638.5 | 1622.0 | 1591.6 | 52.4 |
| 2200 | 1754.5 | 1674.3 | 1635.1 | 1595.2 | 53.5 |

A **900 K** spread in the initial condition leaves a **13.4 K (0.85%)** spread
at 4.5 Gyr. The present state is *stiffly*, not absolutely, independent of the
past — and that residual sensitivity is the reason a thermal history is never
unique. The two extreme trajectories are not equally good descriptions of the
Earth even though they end in nearly the same place: they differ in what they
imply about early-Earth volcanism, and only a constraint on the *history* can
separate them.

### 3.3 Present-day diagnostics and the two rates

Integrating the hottest trajectory and reading the present-day values:

$$T = 1595.2\ \mathrm{K},\qquad q_{\text{surf}} = 53.5\ \mathrm{mW\,m^{-2}},
\qquad Ur = \frac{34.7}{53.5} = 0.648,$$

$$\left.\frac{\mathrm{d}T}{\mathrm{d}t}\right|_{\text{bud}}
= -23.32\ \mathrm{K\,Gyr^{-1}} = -23.3\ \mathrm{mK\,Ma^{-1}},$$

$$\left.\frac{\mathrm{d}T}{\mathrm{d}t}\right|_{\text{qs}}
= -19.59\ \mathrm{K\,Gyr^{-1}} .$$

The two differ by **19%**, and the sign of the difference is informative: the
box is still catching up with a moving equilibrium, because the model was started
hotter than the equilibrium at 4.5 Gyr
($T_{\text{eq}} = 1564.4\ \mathrm{K}$ for today's production). The default
"secular cooling" number one reads in a textbook is the quasi-static one; the
default number a numerical model prints is the budget one. They are not the same
number, and the difference is the model's disequilibrium, not noise.

Note also what the Urey ratio does *not* determine. At fixed $Ur = 0.648$, the
cooling rate can be anything from $-15$ to $-109\ \mathrm{K\,Gyr^{-1}}$ depending
on the assumed $E_a$ (§3.4). **The Urey ratio is not a cooling rate.**

### 3.4 The rheology sets the admitted cooling range

Sweeping the activation energy, with everything else fixed and the sensitivity
evaluated at the model's present temperature:

| $E_a$ (kJ mol⁻¹) | $\mathrm{d}q/\mathrm{d}T$ (mW m⁻² K⁻¹) | $\tau$ (Myr) | $\mathrm{d}T/\mathrm{d}t$ (K Gyr⁻¹) |
|---|---|---|---|
| 0 | 0.05520 | 6847 | −108.92 |
| 100 | 0.14036 | 2692 | −42.83 |
| 200 | 0.22425 | 1685 | −26.81 |
| 300 | 0.30685 | 1232 | −19.59 |
| 400 | 0.38821 | 973 | −15.49 |

A factor of seven in the admitted cooling rate, with the present-day state held
identical. The physical content of the table is a single sentence: a mantle whose
transport efficiency depends strongly on temperature responds to a heat-flow
deficit by a small temperature change, so the deficit persists and the cooling is
slow; a mantle with a sluggish feedback must cool much further before it can shed
the same excess. **The parameter that controls the thermal history is the
sensitivity of transport to temperature, and it is the least well known input in
the model.**

### 3.5 The independent inventory budget

Now do the calculation *without* a convection model. Adopt a mean surface loss of
$73.5\ \mathrm{mW\,m^{-2}}$, of which $19.3$ is crustal radiogenic, $10.0$ comes
from the core and $34.7$ is mantle radiogenic. Then

$$\text{production} - \text{loss} = 64.0 - 73.5 = -9.5\ \mathrm{mW\,m^{-2}},$$

which over an area of $5.6\times10^{14}\ \mathrm{m^2}$ is

$$-9.5\times10^{-3}\times5.6\times10^{14} = -5.3\ \mathrm{TW}.$$

With the mantle's heat capacity $\rho c_p d A = 6.678\times10^{27}\ \mathrm{J\,K^{-1}}$,

$$\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{-5.3\times10^{12}}{6.678\times10^{27}}
\times 3.1557\times10^{16} = -25.2\ \mathrm{K\,Gyr^{-1}}.$$

**The inventory budget and the dynamic model agree to 7.9%** — $25.2$ against
$23.3\ \mathrm{K\,Gyr^{-1}}$ — despite sharing almost none of their machinery.
One is a parameterised convection simulation; the other is `production minus
loss`, divided by a heat capacity.

The agreement is a check, and it is worth being precise about what it checks.
It tests the **internal consistency** of the adopted inputs: production, heat
loss, core flux and heat capacity. It does **not** measure the cooling rate. If
the adopted mantle production were half as large, the inventory rate would rise to
about $-97\ \mathrm{K\,Gyr^{-1}}$, and the dynamic model — whose present state is
calibrated to the same flux — would still report $-23\ \mathrm{K\,Gyr^{-1}}$.
Agreement between two boxes that share their inputs is not independent
confirmation of the Earth.

## 4. Assumptions and regime of validity

1. **One box.** The mantle is treated as a single temperature with no lateral or
   radial structure. Real mantle convection has plate-scale boundary layers,
   slabs and plumes; a box model averages all of them into one number and cannot
   represent, for example, the temperature of a subducting slab.
2. **The $Nu(Ra)$ law is a parameterisation.** It is calibrated on isoviscous
   convection and applied to a rheology that varies by orders of magnitude. In
   [01](01-radiogenic-heat.md) §3.5 the same law needed a viscosity six times the
   adopted one to reproduce a plausible flux — the discrepancy is inherited here.
3. **The present-day flux is an adopted target.** The calibration makes the
   model reproduce it by construction, so the present-day flux is not a test.
4. **The half-life is a single effective value.** Four parents with different
   half-lives are collapsed into one $4.0\ \mathrm{Gyr}$; the early Earth's
   production is therefore underestimated, which matters for $t < 1\ \mathrm{Gyr}$.
5. **The core flux is constant.** In reality it grows as the inner core freezes
   and the core cools; a constant $q_{\text{cmb}}$ over 4.5 Gyr is a strong
   simplification with a direct effect on the partition in §3.5.
6. **Radiogenic production is uniformly distributed in the box.** Crustal
   enrichment, which [01](01-radiogenic-heat.md) §3.2 showed to be a factor of
   several hundred, is treated as a separate surface term rather than as a
   stratified distribution.
7. **No phase-change or latent-heat terms.** Melting, solidification and the
   latent heat of the transition zone are omitted.

## 5. Worked example: what the 7.9% agreement is worth

Take the agreement in §3.5 at face value and ask what change in an input would
destroy it.

1. **Halve the adopted crustal production**, from 19.3 to
   $9.65\ \mathrm{mW\,m^{-2}}$. The inventory residual becomes
   $73.5 - 9.65 - 10.0 - 34.7 = 19.15\ \mathrm{mW\,m^{-2}}$, and the rate
   becomes $-25.2\times(19.15/9.5) = -50.8\ \mathrm{K\,Gyr^{-1}}$. The agreement
   is gone.
2. **Halve the core flux**, from 10.0 to $5.0\ \mathrm{mW\,m^{-2}}$. The residual
   becomes $14.5\ \mathrm{mW\,m^{-2}}$ and the rate
   $-38.5\ \mathrm{K\,Gyr^{-1}}$. Also gone.
3. **What this means.** The agreement constrains the *sum* of the inputs, not
   each of them. A larger crustal inventory and a smaller core flux can restore
   the same total, so the consistency check cannot separate the two contributions
   — and separating them is precisely what a thermal-evolution model is asked to
   do. That is the honest limitation of the budget route.

## 6. The degeneracy, stated as a falsification problem

The model has three knobs ($\eta_{\text{ref}}$, $E_a$, $\beta$), one calibration
(the present-day flux) and one output that is claimed to be interesting (the
cooling history). What would break the degeneracy?

- **A constraint on the past, not the present.** A record of Archean or
  Proterozoic thermal state — metamorphic P–T paths, komatiite eruption
  temperatures, or a dated lithosphere thickness — constrains $T(t)$ at a
  specific time and therefore constrains $\mathrm{d}q/\mathrm{d}T$, which is what
  §3.4 shows to be the controlling parameter.
- **An independent measurement of $\eta(T)$.** Laboratory creep laws give $E_a$
  for the relevant minerals; the model's $E_a$ is an assumption that a
  mineral-physics measurement can replace, breaking one leg of the degeneracy.
- **A core-evolution constraint.** The palaeomagnetic record (see
  [04 Geomagnetic Field and Core Dynamics](../04-geomagnetism-and-core/README.md))
  constrains when the geodynamo existed and therefore how much heat the core must
  have been supplying at various times, which is exactly the $q_{\text{cmb}}(t)$
  that §4 item 5 assumed constant.

None of the three is available in the adopted synthetic model, so within this
lesson the cooling history remains under-determined. Stating that explicitly —
rather than choosing the parameter set that gives a preferred answer — is the
point of the exercise.

## 7. Verification in the demonstration

Four independent checks are printed.

1. **Two integrators.** `RK45` and `LSODA` agree on the final temperature to
   $5.2\times10^{-5}\ \mathrm{K}$ from the same initial condition, with 164 and
   157 right-hand-side evaluations respectively.
2. **The equilibrium condition.** Substituting $T_{\text{eq}} = 1564.4\
   \mathrm{K}$ back into the balance leaves a residual of
   $6.25\times10^{-5}\ \mathrm{pW\,m^{-2}}$, i.e. the root-find converged.
3. **The quasi-static rate against the numerical rate.** The analytic
   $-\lambda H/(\mathrm{d}q/\mathrm{d}T) = -19.59\ \mathrm{K\,Gyr^{-1}}$ against
   the integrated $-23.32\ \mathrm{K\,Gyr^{-1}}$, differing by 19%. The residual
   is the disequilibrium identified in §3.3, and its size sets how far the box is
   from its own equilibrium.
4. **The lag prediction.** $-24.7\ \mathrm{K\,Gyr^{-1}}$ from the linearised lag
   formula against $-23.3$ from the integration, i.e. the linearisation is good
   to about 6%.

## 8. Python demonstration

[`code/thermal_evolution_demo.py`](./code/thermal_evolution_demo.py) prints, in
seven labelled sections: the model and its calibration; the flux sensitivity,
equilibrium temperature and response time; the three-trajectory table and the
initial-condition spread; the present-day Urey ratio and both cooling rates; the
activation-energy sweep; the whole-Earth inventory budget with its comparison;
and the four verification checks. It exits 0 in well under a second.

```bash
cd 12-global-geophysics-interior/03-geotherms-and-heat-budget/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_evolution_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-thermal-evolution-exercises.md`](./exercises/03-thermal-evolution-exercises.md)
and
[`exercises/03-thermal-evolution-solutions.md`](./exercises/03-thermal-evolution-solutions.md).

- **★** Write the one-box balance, identify each term's units, and compute the
  Urey ratio for $H = 30$, $q_{\text{cmb}} = 8$ and
  $q_{\text{surf}} = 50\ \mathrm{mW\,m^{-2}}$.
- **★★** Derive $\mathrm{d}T/\mathrm{d}t|_{\text{qs}} = -\lambda H/(\mathrm{d}q/\mathrm{d}T)$
  from the balance by requiring the box to stay on the equilibrium curve, and
  evaluate it for the adopted $H$, $\lambda$ and $\mathrm{d}q/\mathrm{d}T$.
- **★★** Show that changing the half-life from 4.0 to 5.0 Gyr changes the
  quasi-static rate by the same factor, and explain why the Urey ratio does not
  change at all.
- **★★★** Propose a synthetic observable that would distinguish $E_a = 200$ from
  $E_a = 400\ \mathrm{kJ\,mol^{-1}}$, and specify the data you would need and the
  precision required.

## 10. Mastery checkpoint

Without notes:

> A one-box mantle has $\rho c_p d = 1.19\times10^{13}\ \mathrm{J\,m^{-2}\,K^{-1}}$,
> a time-dependent production $H(t)$ with a $6.0\ \mathrm{Gyr}$ half-life equal
> to $40\ \mathrm{mW\,m^{-2}}$ today, a constant core flux of
> $8\ \mathrm{mW\,m^{-2}}$ and a transport law with
> $\mathrm{d}q/\mathrm{d}T = 0.25\ \mathrm{mW\,m^{-2}\,K^{-1}}$ and
> $q_{\text{surf}} = 56\ \mathrm{mW\,m^{-2}}$ today. **(a)** Compute the Urey
> ratio. **(b)** Compute the instantaneous budget cooling rate. **(c)** Compute
> the quasi-static rate and explain the difference. **(d)** Decide whether the
> box is above or below its equilibrium and justify it with one number.
> **(e)** State one observation that would let you measure rather than assume
> $\mathrm{d}q/\mathrm{d}T$.

## 11. Common pitfalls

1. **Reporting one cooling rate as "the" rate.** The budget rate and the
   quasi-static rate differ by 19% here, and the difference is physics.
2. **Treating the Urey ratio as a cooling rate.** At fixed $Ur = 0.648$ the
   admitted rate spans $-15$ to $-109\ \mathrm{K\,Gyr^{-1}}$.
3. **Calibrating to the present and calling it a test.** Calibration removes the
   degree of freedom that would have made the present day a prediction.
4. **Assuming the initial condition is irrelevant.** A 900 K spread in $T(0)$
   leaves a 13 K spread today: small, but not zero, and it is the only handle on
   the early Earth.
5. **Reading an agreement between two shared-input budgets as independent
   confirmation.** The inventory route and the dynamic route share the adopted
   production and loss.
6. **Working in mixed units.** The heat capacity per unit area is
   $10^{13}\ \mathrm{J\,m^{-2}\,K^{-1}}$, not $10^{10}$; a factor-of-1000 slip
   here turns a plausible cooling rate into a nonsense one.

## 12. Related modules

- [01 Radiogenic Heat Production and Mantle Geotherms](01-radiogenic-heat.md) —
  the inventory this model decays.
- [02 Heat Flow and Its Distribution](02-heat-flow-global.md) — the loss this
  model must match.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  where the core composition, its radiogenic content and its heat capacity come
  from.
- [04 Geomagnetic Field and Core Dynamics](../04-geomagnetism-and-core/README.md) —
  the palaeomagnetic record that constrains the core's heat output over time.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the convection equations that the $Nu(Ra)$ law abbreviates.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — stiff
  ODE integration and the solvers used in the demonstration.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of under-determined parameter combinations such as
  $(\eta_{\text{ref}}, E_a, \beta)$.
