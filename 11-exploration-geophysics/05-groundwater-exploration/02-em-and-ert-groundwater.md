---
id: 11-05-02
title: "EM and ERT for Groundwater Mapping"
level: graduate
prereqs: ["11-05-01", "09-02-05", "09-05-01"]
tags: [exploration-geophysics, groundwater, ert, electromagnetics, resistivity, inversion, non-uniqueness]
---

# EM and ERT for Groundwater Mapping

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the geometric factor of a four-electrode array from the potential
   of a point source in a half-space, and **compute** an apparent resistivity
   from a resistance measurement.
2. **Derive** the diffusive skin depth from the induction equation and
   **compute** the depth a given frequency can reach in a given resistivity.
3. **Derive** the classical two-layer Schlumberger image solution and **verify**
   its small- and large-spacing asymptotes.
4. **Quantify** the ambiguity of a layered-earth inversion by mapping the
   admitted model set and the log-sensitivity Jacobian, and **state** how the
   acquisition controls it.
5. **Compute** the depth of investigation of a sounding from a stated
   sensitivity level, and **explain** why it is a survey property.
6. **State** why a resistivity image cannot be read directly as a salinity map.

## Prerequisites

- [11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces](../05-groundwater-exploration/01-aquifer-signatures.md)
  — what conductivity means for an aquifer, and why it is ambiguous.
- [09-02-05 ERT Tomography](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md)
  — the DC inverse problem and its regularisation.
- [09-05-01 TEM Sounding](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md)
  — time-domain sounding, the method this lesson analyses.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general
  language of non-uniqueness and resolution used here.

> All models and data in this module are **SYNTHETIC**. The resistivities,
> thicknesses and noise levels below are chosen teaching values, not measurements
> of any site.

## 1. Intuition: two ways to weigh the ground, one number to explain

Groundwater mapping with electricity uses two families of method and they answer
the same question.

- **Galvanic (DC) methods** inject current through electrodes and measure the
  resulting potential difference. ERT is the modern imaging form. Depth is
  bought with **electrode spacing**: the current spreads, and the measurement
  integrates the resistivity over an ever-larger volume.
- **Inductive (EM) methods** drive a time-varying current in a transmitter coil
  and measure the secondary field in a receiver. Depth is bought with
  **frequency** (FDEM) or with **time after switch-off** (TDEM). No electrodes
  are needed, which is why EM is the method of choice for hard ground, dry
  terrain and airborne work.

Both produce an **apparent** quantity: an apparent resistivity $\rho_a$ for DC,
an apparent conductivity $\sigma_a$ for EM. Apparent means *the resistivity of
the uniform half-space that would give this reading*. The whole interpretation
problem is that a layered or laterally varying Earth gives the same apparent
reading as many uniform half-spaces, and the inversion that recovers the
structure from a set of readings is non-unique. This lesson derives the forward
relations, then measures the non-uniqueness rather than asserting it.

## 2. Precise definitions

### 2.1 The four-electrode array and apparent resistivity

Two current electrodes A and B inject current $I$; two potential electrodes M and
N measure a voltage $\Delta V$. The measured **resistance** is
$R = \Delta V / I$, and the apparent resistivity is defined as

$$ \rho_a = K\,R = K\frac{\Delta V}{I}, $$

where $K$ is the **geometric factor** of the array (metres). For a **Wenner**
array with equal spacing $a$, $K = 2\pi a$. For a **Schlumberger** array with
current-electrode half-spacing $L = AB/2$ and potential-electrode separation
$MN$, $K = \pi(L^{2} - MN^{2}/4)/MN$, which for $MN \ll L$ reduces to
$K = \pi L^{2}/MN$.

### 2.2 Sounding, profiling and the two Dar Zarrouk parameters

A **sounding** varies the spacing (or frequency) at a fixed location to probe
depth; a **profiling** survey keeps the geometry fixed and moves to map lateral
change. A one-dimensional interpretation assumes horizontal layers. Two
combinations of a layer's resistivity and thickness control what a sounding can
see:

$$ S = \sum_i \frac{h_i}{\rho_i}\ (\text{longitudinal conductance, S}) \qquad
T = \sum_i \rho_i h_i\ (\text{transverse resistance, }\Omega\,\mathrm{m^2}). $$

$S$ dominates the response of a **thin conductive** layer; $T$ dominates that of
a **thin resistive** layer. Everything else about the layer is poorly resolved,
which is the origin of the classic **equivalence** problem.

### 2.3 Skin depth and diffusion time

In a conductor the electromagnetic field obeys a diffusion equation, not a wave
equation. Its characteristic length is the **skin depth**

$$ \delta = \sqrt{\frac{2}{\omega \mu_0 \sigma}}
= \sqrt{\frac{2\rho}{\omega\mu_0}}
= 503.29\sqrt{\frac{\rho}{f}}\ \mathrm{m}, $$

with $\rho$ in $\Omega\,\mathrm{m}$, $f$ in Hz, and
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$. In the time domain the same
physics gives a **diffusion depth**
$d(t) = \sqrt{2\rho t/\mu_0} = 1261.6\sqrt{\rho t}\ \mathrm{m}$ at time $t$ after
switch-off, which is the basis of the airborne TDEM system treated in
[11-05-04](./04-airborne-groundwater.md).

### 2.4 Apparent and true: the honest phrasing

An ERT image is a **model** whose forward response fits the data within their
error. Calling it "the resistivity of the aquifer" silently asserts that the
inversion is unique and that the physics is what the forward model says it is.
Both are assumptions. Where this lesson uses the word *image* it means the model,
with its resolution attached.

## 3. Derivations

### 3.1 The geometric factor

The potential of a point current source $I$ in a uniform half-space of
resistivity $\rho$ is

$$ V(r) = \frac{I\rho}{2\pi r}. $$

Superposing two sources, $+I$ at A and $-I$ at B, the potential difference
between M and N is

$$ \Delta V = \frac{I\rho}{2\pi}
\left(\frac{1}{AM} - \frac{1}{BM} - \frac{1}{AN} + \frac{1}{BN}\right), $$

so that $\rho_a = K\Delta V/I$ with

$$ K = 2\pi\left/\left(\frac{1}{AM} - \frac{1}{BM}
- \frac{1}{AN} + \frac{1}{BN}\right)\right. $$

For a Wenner array this collapses to the familiar $K = 2\pi a$; for a
Schlumberger array with $MN \ll L$ it collapses to $K = \pi L^{2}/MN$.

### 3.2 The classical two-layer Schlumberger solution

For a layer of resistivity $\rho_1$ and thickness $h$ over a half-space of
resistivity $\rho_2$, the surface potential is the image solution

$$ V(r) = \frac{I\rho_1}{2\pi}\left[\frac{1}{r}
+ 2\sum_{n=1}^{\infty}\frac{k^{n}}{\sqrt{r^{2} + (2nh)^{2}}}\right],
\qquad k = \frac{\rho_2-\rho_1}{\rho_2+\rho_1}. $$

In the Schlumberger limit ($MN\to 0$) the apparent resistivity involves the
potential gradient at the current-electrode distance, $\rho_a = -2\pi L^{2}
V'(L)/I$, and differentiating term by term gives the standard series

$$ \boxed{\;\rho_a(L) = \rho_1\left[1
+ 2\sum_{n=1}^{\infty}\frac{k^{n}}{\left(1 + (2nh/L)^{2}\right)^{3/2}}\right].\;} $$

The demonstration checks this against its two independent limits and against the
convergence of the sum:

| Check | Expected | Printed by the demo |
|---|---|---|
| $L \to 0$ (smallest spacing) | $\rho_a \to \rho_1 = 50\ \Omega\,\mathrm{m}$ | $50.0000$ |
| $L \to \infty$ (largest spacing) | $\rho_a \to \rho_2 = 10\ \Omega\,\mathrm{m}$ | $10.0000$ |
| series at $L = 20\ \mathrm{m}$ | stable to truncation | 6 terms $23.5991$, 400 terms $23.5771$ |

The third row shows the series is *slowly* convergent at moderate spacing: the
first six terms leave a $\approx 0.02\ \Omega\,\mathrm{m}$ ($0.1\%$) error, so a
production code sums until the increment is below tolerance or uses a digital
filter. That is a numerical fact, not a physics fact, and it is worth knowing
which is which.

### 3.3 Skin depth from the induction equation

In a uniform conductor with negligible displacement current, the electric field
satisfies

$$ \nabla^{2}\mathbf{E} = \mu_0\sigma\frac{\partial \mathbf{E}}{\partial t}. $$

Look for a plane wave $\mathbf{E} = \mathbf{E}_0 e^{i(kz-\omega t)}$. Then
$k^{2} = i\omega\mu_0\sigma$, so $k = (1+i)/\delta$ with

$$ \delta = \sqrt{\frac{2}{\omega\mu_0\sigma}} = \sqrt{\frac{2\rho}{\omega\mu_0}}. $$

The amplitude decays as $e^{-z/\delta}$, so $\delta$ is the depth over which the
field falls by $e$. Substituting $\omega = 2\pi f$ and
$\mu_0 = 4\pi\times10^{-7}$ gives the practical constant

$$ \delta = 503.29\sqrt{\rho/f}\ \mathrm{m}, $$

which the demonstration computes to five significant figures for a table of
resistivities and frequencies. Note the square root: **doubling the depth needs
four times the resistivity, or four times the period, or a hundredfold reduction
in frequency.**

### 3.4 Conductance equivalence and the sensitivity Jacobian

Consider a thin conductive layer of conductivity $\sigma$ and thickness $h$ in a
more resistive background. Current crossing it spreads laterally inside it, so
the layer acts as a **conducting sheet** whose only relevant property is its
conductance $S = \sigma h$ (equivalently $h/\rho$). Two layers with the same $S$
and the same depth produce nearly the same sounding curve, whatever their
individual $h$ and $\rho$. Where the layer is thin compared with its depth and
with the array spacing, the data determine $S$ and nothing else.

The demonstration measures this with the log-sensitivity Jacobian
$J_{ij} = \partial \ln \rho_a(L_i)/\partial \ln m_j$ for
$m = (\rho_2, h_1)$ on a full, wide spacing range:

| Quantity | Printed value |
|---|---|
| Normalised singular values | $2.707$ and $1.513$ |
| Condition number | $1.79$ |
| Least-determined direction $(d\ln\rho_2, d\ln h_1)$ | $(+0.449, -0.894)$ |

The least-determined direction is the one where the data can be matched by
raising $\rho_2$ while reducing $h_1$: the product $\rho_2 h_1$ (a transverse
resistance) is better determined than either factor. A real survey's ambiguity is
this direction, and a report that quotes $\rho_2$ and $h_1$ as independent
numbers contradicts the data it came from.

## 4. Worked examples

### Example 1 — an apparent resistivity from a resistance

A Schlumberger sounding with $L = AB/2 = 30\ \mathrm{m}$ and
$MN = 4\ \mathrm{m}$ measures $R = \Delta V/I = 0.42\ \Omega$.

$$ K = \frac{\pi(L^{2} - MN^{2}/4)}{MN}
= \frac{\pi(900 - 4)}{4} = \frac{\pi(896)}{4} = 703.7\ \mathrm{m}, $$
$$ \rho_a = K R = 703.7 \times 0.42 = 295.6\ \Omega\,\mathrm{m}. $$

The apparent resistivity is a **weighted average** of the ground sampled by that
geometry. It equals the true resistivity only if the ground is uniform.

### Example 2 — how deep does a frequency look?

At $\rho = 30\ \Omega\,\mathrm{m}$ and $f = 10\ \mathrm{Hz}$,

$$ \delta = 503.29\sqrt{30/10} = 503.29 \times 1.732 = 871.7\ \mathrm{m}. $$

At $f = 1000\ \mathrm{Hz}$ the same ground gives
$\delta = 503.29\sqrt{30/1000} = 87.2\ \mathrm{m}$ — one hundred times the
frequency buys one tenth of the depth. The demonstration's table prints
$1591.5\ \mathrm{m}$ at $1\ \mathrm{Hz}$, $503.3\ \mathrm{m}$ at $10\ \mathrm{Hz}$
and $50.3\ \mathrm{m}$ at $1000\ \mathrm{Hz}$ for $\rho = 10\
\Omega\,\mathrm{m}$, which is the same square-root law.

### Example 3 — the admitted set is a legend, not a number

A synthetic two-layer section ($\rho_1 = 50$, $\rho_2 = 10\
\Omega\,\mathrm{m}$, $h_1 = 8\ \mathrm{m}$) is sounded at 14 spacings from
$AB/2 = 2$ to $251\ \mathrm{m}$ with $3\%$ relative noise. Scanning a
$(90\times120)$-point grid and keeping every model inside the $68\%$ region
($\chi^{2}\le\chi^{2}_{\min}+2.30$ for two parameters):

| Spacing range used | Admitted models | Admitted $\rho_2$ ($\Omega$m) | Admitted $h_1$ (m) |
|---|---|---|---|
| $2$-$251\ \mathrm{m}$ (14 points) | 2 | 10.1 | 7.8-8.0 |
| $2$-$19\ \mathrm{m}$ (7 points) | 95 | 3.0-11.7 | 7.4-9.5 |

The physics is identical in both rows; only the acquisition changed. With the
long spacings that see through the first layer, the depth is $8.0\ \mathrm{m}$
to within $0.2\ \mathrm{m}$. With short spacings only, the same data admit a
depth between $7.4$ and $9.5\ \mathrm{m}$ **and** a basement resistivity from
$3$ to $12\ \Omega\,\mathrm{m}$. The report of a "value" of $8\ \mathrm{m}$ would
be a choice dressed as a measurement.

### Example 4 — depth of investigation belongs to the survey

For $AB/2$ up to $100\ \mathrm{m}$, the depth at which the sounding is *most*
sensitive to the layer boundary is $41.4\ \mathrm{m}$ for a factor-2 contrast and
$39.9\ \mathrm{m}$ for a factor-5 contrast — near $L/2$, not near $L$. The depth
at which the sensitivity has fallen to $10\%$ of its peak is
$186.6\ \mathrm{m}$ and $194.1\ \mathrm{m}$. Both are properties of the largest
spacing and of the chosen sensitivity level, and neither is a property of the
ground. **Quote the acquisition and the threshold with the number.**

## 5. Assumptions and regime of validity

1. **One-dimensional inversion** assumes layers are laterally invariant
   beneath the array. A dipping interface or a channel narrower than the array
   spread produces artefacts that a 1-D interpretation reports as layers.
2. **Isotropic resistivity.** Preferred paths (fractures, bedding) make
   resistivity directional; a 1-D isotropic inversion averages the directions in
   a way that depends on the array orientation.
3. **No induced polarisation.** With clays and sulphides the measured voltage
   has a phase lag; a DC resistivity interpretation that ignores it biases
   $\rho_a$ downward at low frequency.
4. **Geometric factor assumes a flat surface and point electrodes.** Buried or
   displaced electrodes and topography change $K$; this is a routine field error
   that mimics a resistivity change.
5. **EM low-induction-number or full-diffusion regime.** The skin-depth formula
   is a plane-wave, half-space, quasi-static approximation; near a transmitter
   the field is not a plane wave, and in the near field the depth of
   investigation is set by geometry, not by $\delta$.

## 6. Python demonstration

`code/em_and_ert_groundwater_demo.py` prints, in order:

1. the skin-depth constant and a resistivity-frequency table;
2. the two-layer Schlumberger series with its two asymptotes and its convergence;
3. the admitted model set of a noisy sounding for two spacing ranges, and the
   log-sensitivity Jacobian with its singular values and least-determined
   direction;
4. the sensitivity peak and the $10\%$ depth of investigation for
   $AB/2 \le 100\ \mathrm{m}$;
5. the salinity/porosity degeneracy of one bulk conductivity.

```bash
cd 11-exploration-geophysics/05-groundwater-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_and_ert_groundwater_demo.py
```

Companions:
[`exercises/02-em-and-ert-groundwater-exercises.md`](./exercises/02-em-and-ert-groundwater-exercises.md)
and
[`exercises/02-em-and-ert-groundwater-solutions.md`](./exercises/02-em-and-ert-groundwater-solutions.md).

## Common pitfalls

1. **Reading a 1-D inversion as a set of horizontal layers.** It is a model that
   fits a line of data; lateral change hides in it.
2. **Quoting thickness and resistivity as separate numbers.** They are
   equivalent along the least-determined direction of Section 3.4.
3. **Treating the depth of investigation as a constant.** It scales with the
   largest spacing, the latest gate, or the frequency used.
4. **Forgetting electrode geometry errors.** A wrong $MN$ changes $K$
   multiplicatively and shifts the whole curve.
5. **Assuming the conductive body is the water.** In a typical catchment the
   most conductive feature is often the clay-rich weathered zone, not the aquifer.

## Mastery checkpoint

Complete this without notes:

> A Schlumberger sounding uses $AB/2$ from $3\ \mathrm{m}$ to $150\ \mathrm{m}$
> with $MN = 2\ \mathrm{m}$, at $3\%$ noise, and the data fall from
> $180\ \Omega\,\mathrm{m}$ to $25\ \Omega\,\mathrm{m}$. **(a)** Compute the
> geometric factor at $AB/2 = 50\ \mathrm{m}$. **(b)** Sketch, in words, why the
> late (large-spacing) part of the curve fixes the deep conductor's conductance
> but not its thickness. **(c)** Compute the skin depth at $20\ \Omega\,\mathrm{m}$
> and $100\ \mathrm{Hz}$, and say whether a $150\ \mathrm{m}$-spacing sounding and
> that frequency probe comparable depths. **(d)** State the two pieces of
> information that would most reduce the ambiguity, and why.

A worked version of (a) and (c) is in the lesson-05-02
[solutions](./exercises/02-em-and-ert-groundwater-solutions.md).

## Related modules

- [11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces](./01-aquifer-signatures.md)
  — what the conductivity means.
- [11-05-03 Seismic Refraction and Surface Waves for Aquifers](./03-seismic-groundwater.md)
  — the independent porosity constraint that can break the salinity ambiguity.
- [11-05-04 Airborne EM for Regional Aquifer Mapping](./04-airborne-groundwater.md)
  — the same physics from an aircraft, with a different non-uniqueness.
- [18-03 Regularisation and Stabilisation](../../18-inverse-problems/03-regularization/01-why-regularize.md)
  — how the inversion's smoothing controls the image.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) — the second
  discipline behind regularised inversion.

## Self-assessment checklist

- [ ] I can derive $K$ for a four-electrode array from the point-source potential.
- [ ] I can compute $\rho_a$ from a measured resistance.
- [ ] I can derive $\delta = 503.29\sqrt{\rho/f}$ and use it.
- [ ] I can verify the two-layer series against both of its limits.
- [ ] I can explain what the least-determined direction of a Jacobian means.
- [ ] I can state why a depth of investigation is a survey property.
