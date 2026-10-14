---
id: 12-02-02
title: "High-Pressure Experiments and Diamond Anvil Cells"
level: research
prereqs: ["12-01-01", "12-02-01", "02-05-07", "02-04-03"]
tags: [global-geophysics, earth-interior, high-pressure, diamond-anvil-cell, equation-of-state, equation-of-state-fitting]
---

# High-Pressure Experiments and Diamond Anvil Cells

> **All models and data in this module are SYNTHETIC.** Loads, culet sizes,
> calibration constants, volumes and elastic parameters used here are chosen
> teaching values. No laboratory measurement, sample, calibration or published
> equation of state is reproduced. In particular the pressure scale in the
> demonstration is a **synthetic linear scale** with a chosen sensitivity; it is not
> the ruby scale, and no published calibration number is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the idealised pressure of a diamond anvil cell from load and culet
   area, and **state** the three reasons the real limit is lower.
2. **Convert** a pressure-scale reading into a pressure and **propagate** the scale's
   resolution into a *relative* pressure uncertainty that depends on the pressure.
3. **Write** the third-order Birch–Murnaghan equation of state in two algebraically
   equivalent forms, and **validate** one against the other.
4. **Fit** $V_0$, $K_0$ and $K_0'$ to synthetic $P$–$V$ data, **report** their
   uncertainties, and **interpret** the $K_0$–$K_0'$ correlation of −0.93.
5. **Quantify** the systematic bias produced by truncating the pressure range, and
   explain why a quoted $K_0$ without a range is meaningless.
6. **Compute** the thermal pressure of a heated sample and explain why it must be
   removed before an isothermal EOS is fitted.
7. **Distinguish** the quantities a cell experiment measures from those its analysis
   assumes.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  the pressures and depths the experiments aim to reproduce.
- [12-02-01 Mantle Composition and Peridotite Models](01-mantle-composition.md) —
  what the measured moduli are used for.
- [02-05-07 Phase Equilibria](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  the thermodynamic framework an EOS lives in.
- [02-04-03 Constitutive Laws and Generalised Hooke's Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md) —
  where $K$ comes from mechanically.

## 1. Making the pressure

A diamond anvil cell forces two brilliant-cut diamonds together, trapping a sample
of a few tens of micrometres between their flat tips (the **culets**), held in place
by a metal gasket. The idealised pressure is the load divided by the culet area:

$$P = \frac{F}{A}, \qquad A = \pi\left(\frac{d_c}{2}\right)^{2}.$$

At a load of 500 N:

| culet $d_c$ (µm) | area (m²) | $P$ (GPa) |
|---|---|---|
| 1000 | $7.854\times10^{-7}$ | 0.6 |
| 500 | $1.963\times10^{-7}$ | 2.5 |
| 300 | $7.069\times10^{-8}$ | 7.1 |
| 200 | $3.142\times10^{-8}$ | 15.9 |
| 100 | $7.854\times10^{-9}$ | 63.7 |
| 50 | $1.963\times10^{-9}$ | 254.6 |

The estimate says a load a strong person can apply with a lever will exceed 200 GPa.
The real limit is lower, for three reasons that are all about *geometry*, not force:

1. **The pressure is not uniform.** It concentrates near the culet edges and the
   sample sees a gradient of tens of per cent across a few tens of micrometres. A
   quoted sample pressure is an average over a gradient, and the gradient is the
   largest single uncertainty in the experiment.
2. **The diamond yields.** The ceiling is set by the anvil's stress state and
   geometry (the bevel angles, the culet size) rather than by the load.
3. **The gasket deforms.** The loaded area is not the culet area; the gasket flows
   and the effective contact area changes with pressure.

A useful mental model: the cell converts a force into a *gradient* of pressure, and
the experiment's job is to know the gradient well enough to say what the sample
actually experienced.

## 2. Measuring the pressure

The pressure is not measured directly. It is inferred from a **calibrated
secondary scale** — a material whose spectrum or lattice parameter changes with
pressure in a known way, placed next to the sample. The demonstration uses a
SYNTHETIC linear scale:

$$P = \frac{1}{s}\left(\frac{\Delta\lambda}{\lambda_0}\right), \qquad
s = 5.26\times10^{-4}\ \mathrm{GPa^{-1}}, \quad \lambda_0 = 694.0\ \mathrm{nm},$$

a deliberately simple form that behaves like a fluorescence-line shift scale
without reproducing any published calibration. With a wavelength resolution of
$\Delta\lambda_\text{res} = 0.05\ \mathrm{nm}$, the pressure resolution is

$$\Delta P = \frac{1}{s}\frac{\Delta\lambda_\text{res}}{\lambda_0}
= \frac{1}{5.26\times10^{-4}}\cdot\frac{0.05}{694.0}
= \frac{1}{5.26\times10^{-4}}\times 7.205\times10^{-5}
= 0.1370\ \mathrm{GPa},$$

**independent of the pressure** — which is the whole story:

| $P$ (GPa) | relative pressure error (%) |
|---|---|
| 1 | 13.70 |
| 5 | 2.74 |
| 20 | 0.68 |
| 100 | 0.14 |
| 200 | 0.07 |

The scale is precise in *absolute* terms and coarse at *low* pressure. Two
consequences:

- Experiments at low pressure have large *relative* pressure uncertainties, so the
  low-pressure part of a data set carries much less information about $K_0$ than its
  point count suggests — which is exactly the mechanism behind the truncation bias of
  Section 4.
- The dominant systematic error is not the resolution but the **calibration slope**
  $s$ itself, which is traceable to primary standards through a chain of
  experiments. In this demonstration $s$ is a *chosen* number, which is the honest
  way to present a scale you are not reproducing.

## 3. The equation of state

### 3.1 Birch–Murnaghan in two forms

Compress a solid and its volume decreases; the relation $P(V)$ is the **equation of
state**. The third-order Birch–Murnaghan (BM3) EOS is the standard form in mineral
physics, obtained by expanding the elastic energy in the **Eulerian strain**

$$f = \frac{1}{2}\left[\left(\frac{V_0}{V}\right)^{2/3} - 1\right]$$

and differentiating with respect to volume. One way of writing the result is

$$P = 3K_0 f\left(1+2f\right)^{5/2}
\left[1 + \frac{3}{2}\left(K_0'-4\right)f\right],$$

and another is the algebraically equivalent

$$P = \frac{3}{2}K_0\left[x^{7/2} - x^{5/2}\right]
\left[1 + \frac{3}{4}\left(K_0'-4\right)\left(x-1\right)\right],
\qquad x = \left(\frac{V_0}{V}\right)^{2/3}.$$

with $K_0$ the zero-pressure bulk modulus and
$K_0' = \left(\mathrm{d}K/\mathrm{d}P\right)_{P=0}$ its pressure derivative. The
demonstration integrates both over volumes from $V/V_0 = 0.5$ to 1 (pressures to
467 GPa) and finds a maximum difference of $1.7\times10^{-13}$ GPa. **Checking that
two algebraic forms of the model agree is the cheapest possible validation**, and it
isolates any later fitting problem to the fit rather than the formula.

### 3.2 Fitting, and the correlation that matters

The demonstration generates synthetic $P$–$V$ data on the BM3 model with
$V_0 = 40.00\ \mathrm{\AA^3}$, $K_0 = 160.0$ GPa, $K_0' = 4.10$, adds independent
Gaussian noise (0.2 % in volume, 0.5 % in pressure) at 30 pressures to 120 GPa, and
fits the three parameters by weighted least squares:

| parameter | true | fitted | 1σ | error (%) |
|---|---|---|---|---|
| $V_0$ ($\mathrm{\AA^3}$) | 40.000 | 39.991 | 0.032 | 0.022 |
| $K_0$ (GPa) | 160.000 | 159.963 | 2.642 | 0.023 |
| $K_0'$ | 4.100 | 4.111 | 0.092 | 0.260 |

with a **correlation coefficient between $K_0$ and $K_0'$ of −0.9334**.

The correlation is the result to understand. A correlation near −1 means the data
determine a *combination* of the two parameters, not each separately: increasing
$K_0$ and decreasing $K_0'$ together leaves the fit essentially unchanged. The
formal 1σ values above are therefore *conditional on the other parameter being
known*; the honest error on $K_0$ alone is larger, and is obtained by projecting the
covariance ellipse — or by reporting the pair with their correlation, as here.

The formal uncertainties also ignore the systematic error of the pressure scale.
Since a 0.5 % pressure error at 100 GPa is 0.5 GPa, comparable to the whole
$K_0$ uncertainty, the *systematic* term usually dominates in real experiments. **A
reported $K_0$ with no experimental systematic attached is a lower bound on the
true uncertainty.**

## 4. Truncating the pressure range

Now the experiment's most common self-inflicted problem. Refit the same data using
only points below a maximum pressure, with $V_0$ fixed (the usual practice when
$V_0$ is measured separately):

| $P_\text{max}$ (GPa) | points | $K_0$ (GPa) | 1σ | $K_0'$ | 1σ |
|---|---|---|---|---|---|
| 20 | 5 | 170.23 | 13.69 | 2.21 | 2.061 |
| 30 | 8 | 157.38 | 7.84 | 4.58 | 0.956 |
| 40 | 10 | 158.52 | 5.44 | 4.41 | 0.545 |
| 60 | 15 | 162.57 | 3.73 | 3.89 | 0.252 |
| 90 | 22 | 160.98 | 2.37 | 4.01 | 0.125 |
| 120 | 30 | 159.42 | 1.73 | 4.12 | 0.077 |

(true: $K_0 = 160.0$ GPa, $K_0' = 4.10$.)

Read three things:

1. **The bias at low pressure is large and structured.** Restricting to $P < 20$ GPa
   gives $K_0' = 2.21$ — half the true value — and $K_0 = 170$ GPa, 6 % high. The
   fit cannot separate compression from curvature when the compression is small, so
   $K_0$ absorbs what $K_0'$ should carry.
2. **The uncertainties grow by an order of magnitude** (13.7 GPa against 1.7 GPa for
   $K_0$) *even though the misfit stays small*. A good fit is not evidence of good
   parameters.
3. **The bias is not random.** Every truncated fit is wrong in a correlated way, so
   averaging more low-pressure experiments does not remove it. This is the same
   lesson as the systematic-velocity bias in
   [12-01-02](../01-seismic-structure-of-the-earth/02-crustal-structure.md), in a
   different laboratory.

**The reporting rule that follows:** a $K_0$ must be quoted with the pressure range
used, the fitted $K_0'$, and the EOS form. Without them it describes one experiment,
not one mineral.

## 5. Thermal pressure

For a heated sample, the measured $P$–$V$ relation is not isothermal. To first order
the pressure at volume $V$ and temperature $T$ separates into a static part and a
thermal part:

$$P(V,T) = P_\text{static}(V) + P_\text{th}(T),
\qquad P_\text{th} \approx \alpha K_T\,\Delta T,$$

where $\alpha$ is the thermal expansion and $K_T$ the isothermal bulk modulus. With
the demonstration's chosen values $\alpha = 3.0\times10^{-5}\ \mathrm{K^{-1}}$ and
$K_T = 130$ GPa:

| $\Delta T$ (K) | $P_\text{th}$ (GPa) | equivalent compression (km of mantle) |
|---|---|---|
| 500 | 1.95 | 59.1 |
| 1000 | 3.90 | 118.2 |
| 1500 | 5.85 | 177.3 |
| 2000 | 7.80 | 236.4 |

Heating a sample by 1500 K adds **5.85 GPa** of internal pressure — equivalent to
burying the sample nearly 180 km deeper in the mantle. An analysis that compares a
hot volume with a cold EOS without removing $P_\text{th}$ will systematically
underestimate the bulk modulus, because some of the observed compression is thermal.

The equivalent thermodynamic statement is the Grüneisen parameter,
$\gamma = \alpha K_T V/C_V$, which converts thermal energy into pressure. The
practical point stands: **a laser-heated experiment trades a pressure uncertainty for
a temperature uncertainty**, and the temperature (often known to only 10 % at
2000 K) is usually the larger of the two.

## 6. What is measured and what is assumed

| quantity | status |
|---|---|
| unit-cell volume $V$ | **measured** (diffraction), typically 0.1–0.3 % |
| pressure $P$ | **inferred** through a calibration |
| temperature $T$ | **measured**, 10 % at 2000 K in laser-heated experiments |
| $V_0$, $K_0$, $K_0'$ | **fitted** parameters of an assumed EOS form |
| thermal pressure | **modelled** ($\alpha$, $K_T$ and their temperature dependence) |
| sample composition | **assumed**; not measured in situ |
| absence of phase change, reaction, deviatoric stress | **assumed** |

Two consequences worth stating plainly:

- **The EOS form is a choice.** Fitting a different functional form to the same data
  would give different $K_0$ and $K_0'$ with a similar misfit. The fit tests the
  parameters *within* the model, not the model.
- **A deviatoric stress bias is invisible in the fit.** Non-hydrostatic conditions
  shift diffraction lines in ways that can be absorbed by $K_0$ and $K_0'$, which is
  why annealing and pressure-medium choices are part of the method, not
  housekeeping.

## 7. Assumptions and regime of validity

1. **Hydrostatic (or at least known) stress.** The single largest systematic in most
   cell experiments.
2. **A calibrated pressure scale**, with the calibration's own uncertainty attached.
   A scale calibrated against another scale inherits both.
3. **No sample–medium reaction** and no phase change over the measured range. If a
   phase change occurs, the fitted "EOS" is a fit to two different materials.
4. **The sample's composition is known** — for solid solutions, the composition
   determined before loading may not be the composition at the sampled spot.
5. **Isothermal conditions**, or a thermal-pressure correction with known $\alpha$ and
   $K_T$; both are themselves $P$–$T$ dependent, so the correction is iterative.
6. **The third-order truncation of the strain expansion.** For very large
   compressions ($V/V_0 \lesssim 0.5$) the truncation error grows; higher-order
   forms exist and give different $K_0$.
7. **Covariance reported.** Parameters quoted without their correlation overstate
   what the data determine (Section 3.2).

## 8. Worked examples

### Example 1 — the culet needed for a target pressure

To reach 100 GPa at a load of 400 N, the required area is

$$A = \frac{F}{P} = \frac{400}{100\times10^{9}} = 4.0\times10^{-9}\ \mathrm{m^{2}},$$

so the culet diameter is

$$d_c = 2\sqrt{\frac{A}{\pi}} = 2\sqrt{\frac{4.0\times10^{-9}}{3.1416}}
= 2 \times 3.568\times10^{-5}\ \mathrm{m} = 71.4\ \mu\mathrm{m}.$$

Cross-check against the demonstration's table: 500 N on a 100 µm culet gives
63.7 GPa, and 400 N on the same culet gives
$400/(\pi\,(50\times10^{-6})^{2}) = 50.9$ GPa. Since $P \propto d_c^{-2}$, halving
the area doubles the pressure, and 71.4 µm is exactly the culet that turns 400 N into
100 GPa — the arithmetic is consistent. Whether the *diamond* survives is a
different question, which is why culet size is always quoted alongside the pressure
in real work.

### Example 2 — how much does the volume noise matter?

Differentiate the definition of the bulk modulus, $K_0 = -V\,\mathrm{d}P/\mathrm{d}V$
at zero pressure. In the demonstration's synthetic data set the compression at
120 GPa is $\Delta V/V_0 = 1 - 0.6989 = 0.3011$ (computed from the model), so a
relative volume error $\epsilon_V$ propagates roughly as

$$\frac{\delta K_0}{K_0} \sim \epsilon_V\,
\frac{P_\text{max}}{K_0\,\left(\Delta V/V_0\right)}
= 0.002 \times \frac{120}{160 \times 0.3011} = 0.002 \times 2.49
= 0.50\ \%,$$

i.e. $\delta K_0 \approx 0.8$ GPa. The demonstration's formal 1σ is **2.64 GPa**,
three times larger, because the pressure noise also contributes the $K_0$–$K_0'$
trade-off lets the two parameters absorb each other. **The order of magnitude is set
by (volume precision) × (pressure range)/(compression range): buying a better $K_0$
means either better diffraction or a wider pressure range, and never more points in
the same range.**

### Example 3 — removing the thermal pressure

An experiment reports a volume $V$ at 30 GPa and 1800 K. With
$\alpha = 3.0\times10^{-5}\ \mathrm{K^{-1}}$ and $K_T = 130$ GPa, the thermal
pressure is

$$P_\text{th} = 3.0\times10^{-5} \times 130\times10^{9} \times (1800-300)
= 5.85\ \mathrm{GPa},$$

so the *static* pressure to use in the isothermal EOS is $30 - 5.85 = 24.15$ GPa —
a 20 % correction. If instead the analyst neglects it, the point is plotted 5.85 GPa
too far right, which biases the fitted $K_T$ downward. And note the double
dependency: $\alpha$ and $K_T$ are themselves functions of pressure and temperature,
so the correction must be iterated with the EOS being fitted. **The correction is not
a fixed offset; it is part of the model.**

## 9. Python demonstration

`code/high_pressure_experiments_demo.py` validates the two forms of BM3 against each
other, computes the load–culet–pressure table, propagates a synthetic pressure
scale's resolution into relative errors, generates and fits synthetic $P$–$V$ data
with reported uncertainties and correlation, runs the truncated-range experiment,
computes the thermal pressure, and tabulates what is measured against what is
modelled. It prints labelled results with units and runs in about 0.3 s:

```bash
cd 12-global-geophysics-interior/02-composition-and-mineral-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python high_pressure_experiments_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-high-pressure-experiments-exercises.md`](exercises/02-high-pressure-experiments-exercises.md)
and
[`exercises/02-high-pressure-experiments-solutions.md`](exercises/02-high-pressure-experiments-solutions.md).

- **★** Compute a culet size and a pressure-scale resolution.
- **★★** Compute $K_0$ and $K_0'$ uncertainties from a covariance matrix and interpret
  the correlation.
- **★★** Compute a thermal-pressure correction and its effect on a data point.
- **★★★** Design an experiment that determines $K_0'$ independently of $K_0$, with a
  predicted uncertainty.

## Mastery checkpoint

Without notes:

> A cell experiment reports $V_0 = 40.12\ \mathrm{\AA^3}$,
> $K_0 = 152 \pm 3$ GPa, $K_0' = 4.30 \pm 0.10$ with
> $\mathrm{corr}(K_0,K_0') = -0.94$, over the range 0–40 GPa, at
> $T = 300$ K, using a scale whose calibration is quoted as ±1 %.
> **(a)** Compute the systematic pressure error at 40 GPa.
> **(b)** State whether the $K_0$ uncertainty of ±3 GPa is dominated by the formal or
> the systematic term.
> **(c)** Predict what would happen to the fitted $K_0$ and $K_0'$ if the same sample
> were measured to 120 GPa, and why.
> **(d)** Name the two quantities in the reported list that are fitted model
> parameters rather than measurements.

A worked version appears in the lesson-02
[solutions](exercises/02-high-pressure-experiments-solutions.md).

## Common pitfalls

1. **Believing $P = F/A$.** It is the idealisation; the sample sees a gradient.
2. **Quoting a pressure without the scale's calibration uncertainty.** The resolution
   is not the accuracy.
3. **Fitting $K_0$ without reporting $K_0'$ and the pressure range.** Section 4: the
   same data give 170 or 159 GPa depending on the range.
4. **Treating a good fit as validation.** A truncated-range fit has a small misfit and
   badly biased parameters.
5. **Forgetting the thermal pressure.** A 1500 K heating is 5.85 GPa, which is 20 % of
   a 30 GPa experiment.
6. **Reporting parameters without their correlation.** $K_0$ and $K_0'$ are
   anticorrelated at −0.93; quoting both with independent error bars misrepresents the
   constraint.
7. **Assuming hydrostatic conditions.** Deviatoric stress biases $K_0$ in a way the
   fit cannot detect.

## Related modules

- [01 Mantle Composition and Peridotite Models](01-mantle-composition.md) — where the
  measured moduli are used.
- [03 Ab Initio Mineral Physics and Elastic Constants](03-ab-initio-mineral-physics.md) —
  the same elastic constants computed rather than measured, and the same validation
  discipline.
- [04 Core Composition, Light Elements and the Geodynamo](04-core-composition.md) —
  an argument that leans directly on high-pressure densities.
- [12-01-05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](../01-seismic-structure-of-the-earth/05-core-mantle-boundary.md) —
  the Clapeyron slope that only experiments and computations can supply.
- [02-05-07 Phase Equilibria](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  the thermodynamics behind the Clapeyron slope.

## Self-assessment checklist

- [ ] I can compute an idealised cell pressure and state why it is an overestimate.
- [ ] I can convert a scale reading to a pressure and give the relative error.
- [ ] I can write BM3 in two forms and check them against each other.
- [ ] I can fit $V_0$, $K_0$, $K_0'$ and interpret the correlation.
- [ ] I can predict and explain the truncation bias.
- [ ] I can compute and apply a thermal-pressure correction.
- [ ] I can list what a cell experiment measures and what its analysis assumes.
