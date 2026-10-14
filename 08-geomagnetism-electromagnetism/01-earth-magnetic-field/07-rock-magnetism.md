---
id: 08-01-07
title: "Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy"
level: advanced
prereqs: ["08-01-01", "02-07-07", "05-04-01"]
tags: [geomagnetism, rock-magnetism, remanence, susceptibility, hysteresis, koenigsberger-ratio, blocking]
---

# Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy

Every statement in [08-01-06](06-palaeomagnetism.md) about the ancient field is a
statement about a rock, mediated by a magnetisation that the rock acquired and
may since have altered. This lesson is about that mediation: which minerals can
carry a remanence, how the remanence is recorded and lost, and how the bulk
magnetic properties that a laboratory can measure — susceptibility, hysteresis
ratios, blocking temperatures — do and do not determine the mineralogy.

**All models and data in this module are SYNTHETIC.** The hysteresis loops,
susceptibilities, Curie temperature and blocking parameters are chosen teaching
values. The only standard constants used are
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ and
$k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$. No mineral constant, sample
or published measurement is reproduced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** saturation magnetisation, saturation remanence, coercivity and the
   coercivity of remanence from a hysteresis loop, with units.
2. **Convert** between the magnetising field in $\mathrm{A\,m^{-1}}$ and the flux
   density in nT, and between SI and cgs susceptibility statements.
3. **Compute** the induced magnetisation of a rock and its Koenigsberger ratio,
   and explain why $Q$ is not a material property.
4. **Derive** the Néel blocking condition and compute the blocking volume and
   blocking diameter of a grain at a given temperature and observation time.
5. **Distinguish** thermal, chemical, detrital and viscous remanence by their
   acquisition mechanism and their stability.
6. **Explain** how bulk magnetic parameters diagnose domain state, and state
   three ways in which that diagnosis is non-unique.
7. **State** the assumptions behind using magnetic properties as mineralogical
   proxies.

## Prerequisites

- [08-01-01 Describing the Main Field: Declination, Inclination, Intensity](01-main-field-description.md) —
  the nT and the $\mathrm{A\,m^{-1}}$ conversion.
- [02-07-07 Magnetisation, Susceptibility and Magnetic Materials](../../02-physics/07-electromagnetism/07-magnetisation-materials.md)
  — $\mathbf{M}$, $\mathbf{H}$, $\mu_0$ and the SI conventions.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md)
  — how a bulk rock property is built from mineral properties, and the same
  averaging logic.

## 1. Why a rock can remember a field

A material carries a spontaneous magnetisation if exchange coupling aligns
moments within a region. Whether that magnetisation is *stable* is a question
about energy barriers. For a uniformly magnetised single-domain grain with
uniaxial anisotropy energy density $K$ and volume $V$, the barrier between the two
easy directions is $KV$. Thermal energy can cross it, and the grain flips at the
Néel relaxation rate

$$\tau = \tau_0\exp\!\left(\frac{KV}{k_BT}\right), \qquad
\tau_0 \sim 10^{-9}\ \mathrm{s}.$$

A grain is **blocked** (carries a stable remanence) when $\tau$ exceeds the
observation time. Because the function is exponential, the transition is sharp:
the demonstration computes the blocking volume at a laboratory observation time
$\tau = 100\ \mathrm{s}$ for a synthetic material with $K = 2.0\times10^{4}\
\mathrm{J\,m^{-3}}$:

$$\ln\frac{\tau}{\tau_0} = \ln(10^{11}) = 25.3284, \qquad
V_b = \frac{k_BT\ln(\tau/\tau_0)}{K}.$$

| $T$ (K) | $V_b$ (m³) | equivalent diameter (nm) |
|---|---|---|
| 300.0 | $5.2455\times10^{-24}$ | 21.557 |
| 500.0 | $8.7424\times10^{-24}$ | 25.559 |
| 700.0 | $1.2239\times10^{-23}$ | 28.593 |
| 800.0 | $1.3988\times10^{-23}$ | 29.894 |

Check the first row by hand:

$$V_b = \frac{1.380649\times10^{-23}\times300\times25.3284}{2.0\times10^{4}}
= \frac{1.04909\times10^{-19}}{2.0\times10^{4}} = 5.2454\times10^{-24}\
\mathrm{m^{3}},$$

against the demonstration's $5.2455\times10^{-24}$ (the difference is rounding in
$\ln 10^{11}$). The diameter follows from
$V = \pi d^{3}/6$: $d = (6V/\pi)^{1/3} = 21.557\ \mathrm{nm}$.

Three consequences:

- **The blocking volume grows only linearly in $T$**, because the exponential
  argument is dominated by $\ln(\tau/\tau_0)$, which is fixed. A 2.7× change in
  temperature changes the blocking diameter by only 39%.
- **Blocking temperature is the observable.** Heating a grain until its
  relaxation time drops below the laboratory time erases its remanence; the
  temperature at which this happens identifies the carrier.
- **The grain-size window is narrow.** Grains below roughly 20 nm at room
  temperature are superparamagnetic (unblocked, no remanence); the window that
  carries a stable remanence is a *range* of sizes, not a size.

## 2. Hysteresis: reading a loop

The five numbers that describe a hysteresis loop are

| symbol | name | unit |
|---|---|---|
| $J_s$ | saturation magnetisation | $\mathrm{A\,m^{-1}}$ |
| $J_{rs}$ | saturation remanence | $\mathrm{A\,m^{-1}}$ |
| $H_c$ | coercivity | $\mathrm{A\,m^{-1}}$ (or $\mu_0H_c$ in T or nT) |
| $H_{cr}$ | coercivity of remanence | $\mathrm{A\,m^{-1}}$ |
| $J_s$, $J_{rs}$, $H_c$, $H_{cr}$ ratios | the diagnostic pairs | dimensionless |

The demonstration's SYNTHETIC material has $J_s = 4.000\times10^{5}\
\mathrm{A\,m^{-1}}$ and $H_c = 6.000\times10^{3}\ \mathrm{A\,m^{-1}}$, with a
loop whose two branches sit at $\pm0.5001\,J_s$ at $H = 0$, giving

$$J_{rs} = 2.000\times10^{5}\ \mathrm{A\,m^{-1}}, \qquad
\frac{J_{rs}}{J_s} = 0.5015 \quad (\text{model value } \tanh(1/1.82) = 0.5001),$$

and a coercivity in field units

$$\mu_0H_c = 4\pi\times10^{-7}\times6.000\times10^{3}
= 7.5398\times10^{-3}\ \mathrm{T} = 7539.8224\ \mu\mathrm{T}.$$

**The model's limitation must be stated**: in this construction the loop width
parameter fixes $J_{rs}/J_s$ through $\tanh(1/\text{width})$, so the two
quantities are not independent. A real sample's $J_{rs}/J_s$ and $H_c$ vary
independently with grain size and mineralogy, which is exactly what makes the
pair diagnostic. The demonstration is a teaching device for the *shape* of the
diagnosis, not a source of threshold values.

## 3. Susceptibility, and induced versus remanent magnetisation

In SI, a material in a field $\mathbf{H}$ acquires an induced magnetisation

$$\mathbf{M} = \kappa\mathbf{H}, \qquad \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M})
= \mu_0(1+\kappa)\mathbf{H},$$

with $\kappa$ dimensionless. The demonstration's SYNTHETIC rock has
$\kappa = 0.045$:

| ambient $B$ (nT) | $H$ (A/m) | $J_{\text{ind}} = \kappa H$ (A/m) | $\mu_0 J_{\text{ind}}$ (nT) | fraction of ambient |
|---|---|---|---|---|
| 50000 | 39.7887 | 1.790493 | 2250.000 | 4.5000% |
| 100000 | 79.5775 | 3.580986 | 4500.000 | 4.5000% |

*Hand check of the first row.*
$H = 50000\times10^{-9}/(4\pi\times10^{-7}) = 39.7887\ \mathrm{A\,m^{-1}}$;
$J = 0.045\times39.7887 = 1.79049\ \mathrm{A\,m^{-1}}$;
$\mu_0J = 1.256637\times10^{-6}\times1.79049 = 2.2500\times10^{-6}\ \mathrm{T}
= 2250.0\ \mathrm{nT}$ ✔.

The fraction is exactly $\kappa$ expressed in the same units: a susceptibility of
0.045 means the induced magnetisation field is 4.5% of the ambient field. Two
things follow:

- **Susceptibility is not a remanence.** It vanishes when the field is removed,
  and it is a *response function*, so it depends on frequency and on the
  measuring field.
- **The SI/cgs trap.** In cgs, $M = \kappa H$ with $\kappa$ differing by a factor
  $4\pi$; a body appearing to have $\kappa = 0.045$ (SI) is quoted as
  $3.58\times10^{-3}$ in the "emu/cm³ per Oe" convention. Reporting a
  susceptibility without units is reporting nothing.

## 4. The Koenigsberger ratio

Whether an anomaly (or a palaeomagnetic direction) is controlled by *induced* or
*remanent* magnetisation is decided by

$$Q = \frac{J_{r}}{|\kappa H|}.$$

With the demonstration's parameters ($\kappa = 0.045$, ambient 50000 nT, so
$\kappa H = 1.7905\ \mathrm{A\,m^{-1}}$):

| $J_r$ (A/m) | $Q$ | regime |
|---|---|---|
| 0.010 | 0.0056 | induced-dominated |
| 0.100 | 0.0559 | induced-dominated |
| 1.000 | 0.5585 | induced-dominated |
| 10.000 | 5.5851 | remanence-dominated |

The crossover $Q = 1$ sits at $J_r = 1.7905\ \mathrm{A\,m^{-1}}$. The essential
point is that $Q$ contains the **ambient field**, so it is a property of the rock
in its field, not of the rock: the same sample moved from a 50000 nT to a 30000 nT
ambient has its $Q$ changed by 67% with no change in mineralogy. Module
[08-03 Magnetic Anomalies and Modelling](../03-magnetic-anomalies-and-modelling/README.md)
turns this into the practical question of whether an anomaly map can be
interpreted with an induced-magnetisation assumption.

## 5. How remanence is acquired, and how it is lost

| mechanism | acquisition | carrier | stability |
|---|---|---|---|
| **Thermal (TRM)** | cooling through the blocking temperature in a field | fine grains, igneous rocks | high; the palaeomagnetic workhorse |
| **Chemical (CRM)** | growth of magnetic minerals through a blocking volume at fixed $T$ | authigenic grains, red beds | variable, often high |
| **Detrital (DRM)** | deposition and alignment of pre-existing grains | sediments | moderate; prone to inclination shallowing |
| **Viscous (VRM)** | slow thermal activation in the present field | the least stable fraction of any assemblage | low, but cumulative |

The blocking physics of §1 applies to all four; what differs is the *path*
through $(V, T)$ space. This is why demagnetisation works: progressively heating
the sample raises $T$ and moves the blocking volume across the grain-size
distribution, releasing the magnetisation of the grains that unblock at each
temperature, in the order of their stability.

**The time–temperature trade.** Because blocking depends on
$\ln(\tau/\tau_0)$, a modest temperature rise is equivalent to an enormous
increase in time. That is the physical basis of the **viscous remanence**
correction and of the fact that a laboratory heating experiment lasting an hour
unblocks what would take geological time in nature. A laboratory observation time
of $100\ \mathrm{s}$ versus $\tau_0 = 10^{-9}\ \mathrm{s}$ gives
$\ln(\tau/\tau_0) = 25.33$; a geological time of $10^{15}\ \mathrm{s}$ gives
55.3. The difference, a factor of 2.2 in the blocking temperature–volume
product, is the size of the extrapolation every palaeomagnetic interpretation
makes.

## 6. Mineralogy from bulk parameters, and its limits

The demonstration's three SYNTHETIC "materials", distinguished only by an input
coercivity and a loop width, reproduce the classic pattern:

| material | $H_c$ (A/m) | $H_{cr}$ (A/m) | $H_{cr}/H_c$ | $J_{rs}/J_s$ |
|---|---|---|---|---|
| fine / single-domain-like | $8.000\times10^{3}$ | $2.000\times10^{4}$ | 2.500 | 0.8997 |
| intermediate | $6.000\times10^{3}$ | $1.200\times10^{4}$ | 2.000 | 0.5001 |
| coarse / multi-domain-like | $2.000\times10^{3}$ | $2.600\times10^{3}$ | 1.300 | 0.2001 |

and, at fixed $J_s$, the loop width alone moves the pair
$(J_{rs}/J_s, H_c)$ from $(0.8997, 8.0\times10^{3})$ to
$(0.2001, 2.0\times10^{3})$.

That is the diagnostic logic: **high remanence ratio with high
$\mu_0H_{cr}$ goes with fine, stable grains; low with coarse, unstable ones.**
The limits are more important than the pattern, and there are three:

1. **Mixtures.** A bulk $J_{rs}/J_s$ is a weighted average over all carriers. A
   small fraction of a high-coercivity mineral can dominate the remanence while
   contributing almost nothing to $J_s$, so the same ratio can be produced by
   many blends.
2. **Parameter degeneracy.** $J_{rs}/J_s$, $H_c$ and $H_{cr}$ are three numbers
   derived from one loop; they cannot resolve more than three independent aspects
   of a distribution of grains.
3. **Temperature and pressure history.** Stress, oxidation and low-temperature
   transitions change the same parameters, so a bulk-parameter "mineralogy" is a
   statement about the sample's *history* as much as its composition.

The reliable statements are comparative, not absolute: within one lithology, a
systematic change in $H_{cr}/H_c$ across a section is evidence of a change in
domain state or mineralogy; a single value is a data point, not an identification.

## 7. Curie temperature

Above the Curie temperature $T_C$ the exchange coupling is overcome and the
material is paramagnetic: the remanence disappears and only an induced
magnetisation remains. The demonstration's SYNTHETIC $T_C = 900.0\ \mathrm{K}
= 626.9^{\circ}\mathrm{C}$, with a model susceptibility
$\kappa(T)\propto\sqrt{1-T/T_C}$:

| $T$ (K) | $\kappa(T)/\kappa(250\ \mathrm{K})$ |
|---|---|
| 250.0 | 0.849837 |
| 400.0 | 0.745356 |
| 550.0 | 0.623610 |
| 700.0 | 0.471405 |
| 850.0 | 0.235702 |
| 900.0 | 0.000000 |
| 950.0 | 0.000000 |

The steep, well-defined drop to zero is what makes $T_C$ a useful identifier —
**in principle**. In practice a measured $\kappa(T)$ curve is smoothed by the
grain-size distribution, by multiple carriers with different $T_C$, and by
chemical alteration during heating, so an identification from the curve alone is
a hypothesis. The operational use of $T_C$ is to *separate* a remanence from an
induced magnetisation: heat through $T_C$, cool in a known field, and see what
returns.

## 8. Assumptions and regime of validity

1. **Uniform, uniaxial, single-domain grains** for the Néel formula. Real grains
   have shape and magnetocrystalline anisotropy that is not uniaxial, and
   multi-domain grains do not obey the formula at all.
2. **A single observation time.** $\tau = 100\ \mathrm{s}$ is a laboratory choice;
   geological blocking uses a different one, and §5 quantifies the extrapolation.
3. **$\kappa$ is a scalar.** In an anisotropic rock it is a tensor; a single
   susceptibility number is an average.
4. **No chemical alteration during measurement.** Heating can create or destroy
   magnetic minerals, so the curve can reflect the experiment. This is why
   repeated heating/cooling cycles are run and compared.
5. **Synthetic parameters.** The numbers of this lesson are teaching values; the
   *relationships* are the content.

## 9. Python demonstration

`code/rock_magnetism_demo.py` prints, with units:

1. a synthetic hysteresis loop with $J_s$, $J_{rs}$, $J_{rs}/J_s$, $H_c$ and
   $\mu_0H_c$;
2. three synthetic domain-state regimes with $(H_c, H_{cr}, H_{cr}/H_c,
   J_{rs}/J_s)$;
3. susceptibility to induced magnetisation at two ambient fields, with the
   equivalent flux density;
4. the Koenigsberger ratio and its crossover remanence;
5. blocking volumes and diameters at four temperatures, with the
   $\ln(\tau/\tau_0)$ argument printed;
6. loops of three widths at fixed $J_s$, with the model's coupling between width
   and $J_{rs}/J_s$ stated explicitly;
7. $\kappa(T)/\kappa(250\ \mathrm{K})$ through the model's Curie temperature.

Exercises and solutions:
[`exercises/07-rock-magnetism-exercises.md`](./exercises/07-rock-magnetism-exercises.md),
[`exercises/07-rock-magnetism-solutions.md`](./exercises/07-rock-magnetism-solutions.md).

## Mastery checkpoint

1. Convert $H_c = 1.5\times10^{4}\ \mathrm{A\,m^{-1}}$ into $\mu$T.
2. A rock with $\kappa = 0.02$ sits in a 48000 nT field. Compute
   $J_{\text{ind}}$ and the equivalent flux density it produces.
3. Compute the Koenigsberger ratio for $J_r = 0.8\ \mathrm{A\,m^{-1}}$ in the
   rock and field of question 2.
4. Compute the blocking diameter at $T = 650\ \mathrm{K}$ for
   $K = 3.0\times10^{4}\ \mathrm{J\,m^{-3}}$, $\tau = 100\ \mathrm{s}$.
5. State three distinct ways in which a bulk hysteresis ratio fails to identify
   a magnetic mineral.
6. Explain in two sentences why heating through the Curie temperature separates
   remanent from induced magnetisation.

## Common pitfalls

1. **Quoting a susceptibility without units.** SI and cgs differ by $4\pi$.
2. **Treating $Q$ as a rock property.** It depends on the ambient field.
3. **Using a laboratory blocking temperature as a geological one.** §5 gives the
   size of the extrapolation.
4. **Reading mineralogy off one hysteresis ratio.** §6 lists three
   non-uniquenesses.
5. **Forgetting that heating alters samples.** The measurement can change what it
   measures.
6. **Confusing $J_s$ and $M_s$ notations across the literature**, and
   $H_c$-in-A/m with $\mu_0H_c$-in-$\mu$T. Both appear and both are legitimate;
   the unit must be attached.

## Related modules

- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](06-palaeomagnetism.md) —
  what a trustworthy remanence is used for.
- [08-01-01 Describing the Main Field: Declination, Inclination, Intensity](01-main-field-description.md) —
  the units and the frame.
- [08-03 Magnetic Anomalies and Modelling](../03-magnetic-anomalies-and-modelling/README.md) —
  the Koenigsberger ratio as an interpretation problem.
- [02-07-07 Magnetisation, Susceptibility and Magnetic Materials](../../02-physics/07-electromagnetism/07-magnetisation-materials.md)
  — the physics of $\mathbf{M}$ and $\kappa$.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  the same "bulk property from mineralogy" logic for conductivity.

## Self-assessment checklist

- [ ] I can read $J_s$, $J_{rs}$, $H_c$ and $H_{cr}$ from a loop and quote units.
- [ ] I can convert between nT and $\mathrm{A\,m^{-1}}$.
- [ ] I can compute induced magnetisation, its equivalent field and $Q$.
- [ ] I can derive the Néel blocking condition and evaluate it.
- [ ] I can name the four remanence mechanisms and rank their stability.
- [ ] I can state three reasons a bulk parameter does not identify a mineral.
