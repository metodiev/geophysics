---
id: 05-09-01
title: "Measuring Terrestrial Heat Flow"
level: graduate
prereqs: ["02-05-04", "05-08-02", "05-09-02"]
tags: [heat-flow, geotherm, borehole-temperature, equilibration, paleoclimate, sign-convention]
---

# Measuring Terrestrial Heat Flow

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the sign convention and the direction of the vertical coordinate
   unambiguously, and derive $q = k\,\mathrm{d}T/\mathrm{d}z$ from Fourier's law
   with depth positive downward.
2. **Solve** steady conduction with a conductivity contrast and demonstrate that the
   **flux is continuous while the gradient is not**, and use that as the primary
   check on a heat-flow calculation.
3. **Compute** the decay of a borehole drilling disturbance with a line-source
   relaxation model, and quantify the bias it produces in the heat flow at a stated
   elapsed time.
4. **Explain** why a bottom-hole temperature is not an equilibrium temperature, and
   how a Horner-type extrapolation is used.
5. **Solve** the ground-surface-temperature inverse problem and demonstrate its
   genuine non-uniqueness: two different histories give the same present-day
   profile within a stated noise.
6. **Report** a heat flow as a value with an uncertainty, the conductivity
   orientation, and the equilibration state of the hole.

## Prerequisites

- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the governing equation and the diffusion timescales used throughout.
- [05-08-02 Natural Gamma and Spectral Gamma Logging](../08-geophysical-logging/02-gamma-logging.md)
  — the radiogenic heat production that enters a geotherm.
- [05-09-02 Thermal Conductivity Measurement and Corrections](./02-thermal-conductivity.md)
  — the $k$ in $q = k\,\mathrm{d}T/\mathrm{d}z$.

## 1. Intuition: one equation, one product, and two places to go wrong

Terrestrial heat flow is measured as a **product**:

$$q = k\,\frac{\mathrm{d}T}{\mathrm{d}z}, \tag{1}$$

the thermal conductivity times the vertical temperature gradient. Everything hard
about the subject follows from that product: both factors are measured separately,
both have uncertainties, and the multiplication is where the errors combine.

Two conventions cause most of the confusion in the literature, and both must be
fixed before any number is written down:

1. **The direction of $z$.** If $z$ is depth, positive downward, and temperature
   increases downward, then $\mathrm{d}T/\mathrm{d}z > 0$. Fourier's law says heat
   flows *down* the gradient, i.e. upward. The **reported heat flow is the upward
   magnitude**, so it is positive: $q = +k\,\mathrm{d}T/\mathrm{d}z$ with $z$
   downward. Write the convention in every report. If you instead take $z$ positive
   upward, the gradient is negative and the same physical flux is
   $q = -k\,\mathrm{d}T/\mathrm{d}z$. Getting this wrong flips a sign and,
   occasionally, a tectonic argument.
2. **Which conductivity.** A rock with layering has two effective conductivities
   differing by up to the contrast in the layers
   ([05-09-02 §3](./02-thermal-conductivity.md)). The one that belongs in
   equation (1) is the one for **vertical** flow.

Then there is the measurement problem that is unique to heat flow: **the borehole
disturbs exactly the quantity being measured.** Drilling fluid resets the
temperature over the whole hole, and the formation takes days to months to relax.
A temperature log is therefore always a *perturbed* profile, and the perturbation
decays slowly, which is why heat flow is often measured in holes drilled for other
purposes and re-logged years later.

## 2. Precise definitions

### 2.1 Heat flow

$$q = k\frac{\mathrm{d}T}{\mathrm{d}z} \quad [\mathrm{W\,m^{-2}}],
\qquad 1\ \mathrm{mW\,m^{-2}} = 10^{-3}\ \mathrm{W\,m^{-2}}. \tag{2}$$

Global averages are quoted in mW m⁻²; the *Heat Flow Unit* (HFU) of 41.84 mW m⁻²
is historical and best avoided.

### 2.2 Equilibrium temperature and BHT

- **Equilibrium temperature** $T_{\text{eq}}(z)$: the formation temperature in the
  absence of any drilling disturbance.
- **Bottom-hole temperature (BHT)**: the temperature recorded during or shortly
  after drilling. It is always **lower** than equilibrium at depth in a
  conventionally cooled hole, and the difference is the **BHT correction**.

### 2.3 Horner-type extrapolation

If the temperature at a fixed depth is logged at several elapsed times $t$ after
circulation stops, then plotting $T$ against
$\ln[(t+\Delta t)/\Delta t]$ (with $\Delta t$ the circulation time) gives an
approximately straight line whose intercept is the equilibrium temperature. The
linearity is empirical rather than exact, which is why the *correction* carries an
uncertainty of its own.

### 2.4 Geotherm and the radiogenic partition

A **geotherm** is $T(z)$. For steady conduction with a uniform heat production $A$
(W m⁻³) in a layer of thickness $h$ over a mantle heat flow $q_m$,

$$k\frac{\mathrm{d}^2T}{\mathrm{d}z^2} + A = 0
\;\Longrightarrow\;
T(z) = T_0 + \frac{q_0 z}{k} - \frac{Az^2}{2k},
\qquad q_m = q_0 - Ah. \tag{3}$$

The **radiogenic share** of the surface heat flow is $Ah/q_0$.

## 3. Derivations

### 3.1 Flux continuity across a conductivity contrast

In steady state with no sources, $\mathrm{d}q/\mathrm{d}z = 0$, so $q$ is the same
at every depth. Across a boundary between layers of conductivity $k_1$ and $k_2$,

$$k_1\left(\frac{\mathrm{d}T}{\mathrm{d}z}\right)_1
= k_2\left(\frac{\mathrm{d}T}{\mathrm{d}z}\right)_2 . \tag{4}$$

The demonstration solves a two-layer model with $k = 1.5$ W m⁻¹ K⁻¹ from 0 to
500 m and $k = 3.0$ W m⁻¹ K⁻¹ from 500 to 2000 m, with $q = 60$ mW m⁻² and a
surface temperature of 10 °C. Measured:

| Depth (m) | $k$ (W m⁻¹ K⁻¹) | $\mathrm{d}T/\mathrm{d}z$ (K km⁻¹) | $q$ (mW m⁻²) | $T$ (°C) |
|---|---|---|---|---|
| 1 | 1.50 | 40.00 | 60.0 | 10.0 |
| 499 | 1.50 | 40.00 | 60.0 | 30.0 |
| 501 | 3.00 | 20.00 | 60.0 | 30.0 |
| 1999 | 3.00 | 20.00 | 60.0 | 60.0 |

**The gradient halves across the contrast; the flux does not change at all.** A
heat-flow profile that shows $q$ jumping at a lithological boundary is wrong, and
the error is always a mis-assigned conductivity — usually a core measured parallel
to the bedding but used in a vertical calculation.

### 3.2 The drilling disturbance, quantified

Model the drilling disturbance as a line source released at $t = 0$: the
temperature perturbation at radius $r$ and time $t$ is

$$\Delta T(r,t) = \frac{Q}{4\pi k t}
\exp\!\left(-\frac{r^2}{4\kappa t}\right), \tag{5}$$

so the fraction of the initial perturbation remaining at the wall is

$$F(t) = \frac{t_{\text{ref}}}{t}
\exp\!\left[-\frac{r_w^2}{4\kappa t}
+ \frac{r_w^2}{4\kappa t_{\text{ref}}}\right]. \tag{6}$$

The demonstration takes $r_w = 0.10$ m, $\kappa = 10^{-6}$ m² s⁻¹, and an initial
perturbation that increases linearly with depth by 20 K over 2 km — the simplest
non-uniform disturbance, and the shape that produces a *gradient* bias. With a
conductivity of 2.5 W m⁻¹ K⁻¹ and $q_0 = 60$ mW m⁻²:

| Elapsed (h) | $F(t)$ | Gradient bias (K km⁻¹) | Heat-flow bias |
|---|---|---|---|
| 1 | 1.0000 | 10.000 | 41.67 % |
| 4 | 0.4209 | 4.209 | 17.54 % |
| 12 | 0.1575 | 1.575 | 6.56 % |
| 24 | 0.0811 | 0.811 | 3.38 % |
| 120 | 0.0166 | 0.166 | 0.69 % |
| 720 | 0.0028 | 0.028 | 0.12 % |
| 2160 | 0.0009 | 0.009 | 0.04 % |

Three conclusions:

1. **A log run within a day of circulation stopping carries a heat-flow bias of a
   few per cent to tens of per cent**, and the sign is that the measured gradient is
   *low* relative to the equilibrium gradient for this perturbation shape (the mud
   is cooler at depth), so the heat flow is *under*estimated.
2. **Equilibration takes days to months**, not hours. The 0.7 per cent level needs
   about five days; 0.1 per cent needs a month.
3. **The disturbance primarily biases the absolute temperature, not the gradient.**
   That is why a *gradient*-based heat-flow estimate survives a partially
   equilibrated hole reasonably well, while an absolute-temperature-based estimate
   (or a conductivity that depends on temperature) does not. Both statements are
   true and they are frequently confused.

### 3.3 The ground-surface-temperature inverse problem and its non-uniqueness

A surface temperature history $T(0,t)$ propagates into the subsurface by diffusion.
For a step change $\Delta T$ at time $t$ before present, the perturbation at depth
$z$ is

$$\Delta T(z) = \Delta T\left[1 - \mathrm{erf}\!\left(\frac{z}{2\sqrt{\kappa t}}
\right)\right]. \tag{7}$$

The demonstration propagates two genuinely different histories:

- **A:** a 1.0 K step increase 200 yr before present;
- **B:** a smooth 1.6 K rise spread linearly over 600 yr.

Measured present-day anomalies:

| Depth (m) | A (K) | B (K) | difference (K) |
|---|---|---|---|
| 50 | 0.6563 | 1.0424 | $-0.3861$ |
| 100 | 0.3734 | 0.6535 | $-0.2800$ |
| 200 | 0.0751 | 0.2267 | $-0.1516$ |
| 300 | 0.0076 | 0.0657 | $-0.0581$ |
| 500 | 0.0000 | 0.0030 | $-0.0030$ |
| 800 | 0.0000 | 0.0000 | $-0.0000$ |

**Below about 300 m the two histories are indistinguishable**, and any measurement
noise above a few hundredths of a kelvin makes them indistinguishable everywhere.
This is not a limitation of the analysis; it is the physics of diffusion, which
attenuates short timescales as $\exp(-z\sqrt{\omega/2\kappa})$ and therefore
destroys high-frequency information about the past.

The correct output of a GST study is therefore **a family of histories consistent
with the profile and its noise**, plus the statement of which features are resolved
(a step of a stated size at a stated age, or a trend over a stated interval) and
which are not. A single reconstructed curve without its family overstates the
measurement. This is the inverse-problem discipline of
[18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md)
applied to a borehole.

## 4. Worked examples

### 4.1 A heat flow with its uncertainty

**Problem.** A 1500 m hole gives a linear gradient of $27.5 \pm 0.8$ K km⁻¹
between 400 and 1400 m, and core conductivity (vertical) of
$2.60 \pm 0.15$ W m⁻¹ K⁻¹.

$$q = k\frac{\mathrm{d}T}{\mathrm{d}z} = 2.60 \times 27.5\ \mathrm{mW\,m^{-2}}
= 71.5\ \mathrm{mW\,m^{-2}}.$$

Relative uncertainty:
$\sqrt{(0.15/2.60)^2 + (0.8/27.5)^2} = \sqrt{0.00333 + 0.00085} = 0.0647$, so

$$q = 71.5 \pm 4.6\ \mathrm{mW\,m^{-2}} .$$

The conductivity dominates (80 per cent of the variance), which is the usual case
and the reason core conductivity gets more attention than temperature precision.

### 4.2 Reading the equilibration state from the log

A temperature log that is **convex** at the top of the logged interval and becomes
linear below it is the signature of a disturbance that has not fully decayed: the
lower part is equilibrated, the upper part is not. The correct procedure is to fit
the gradient in the *linear, deep* portion, state the interval, and check the
result against a repeat log months later. A single log with no repeat is an
unverifiable measurement, and the honest report says so.

### 4.3 From heat flow to a geotherm

With a surface temperature of 10 °C, $q_0 = 65$ mW m⁻², $k = 2.5$ W m⁻¹ K⁻¹ and a
radiogenic layer of $h = 20$ km with $A = 0.8$ µW m⁻³:

$$q_m = 65 - (0.8\times10^{-6})(20\,000)\times10^{3} = 65 - 16
= 49\ \mathrm{mW\,m^{-2}},$$

a radiogenic share of 25 per cent, and temperatures at 20, 50 and 100 km of
$466$, $1054$ and $2034$ °C (measured in the demonstration's table). All three
decrease as $A$ rises, and the 100 km temperature is the most sensitive — which is
why the lithospheric thickness inferred from a geotherm is the most
model-dependent number in the chain.

## 5. Assumptions

1. **Pure conduction in the logged interval.** Advection by groundwater moves the
   profile by tens of per cent and produces *curvature*, which is the diagnostic
   ([14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)).
2. **Steady state** over the interval's diffusion time. A recent surface change
   invalidates the top few hundred metres; a recent tectonic event invalidates more.
3. **A single, vertical, correctly oriented conductivity** per interval, with the
   anisotropy accounted for.
4. **Equilibrium temperature** in the fit interval, or a stated correction.
5. **No significant topographic or palaeoclimate correction unaccounted for.**
6. **The thermal conductivity's temperature dependence is negligible over the
   interval**, or is accounted for — which fails in deep, hot holes and is exactly
   what makes the absolute temperature harder than the gradient.

## 6. Units and dimensional analysis

- $q$: W m⁻²; usually mW m⁻². 1 HFU $= 41.84$ mW m⁻² (historical).
- $k$: W m⁻¹ K⁻¹; the older cal cm⁻¹ s⁻¹ °C⁻¹ equals 418.4 W m⁻¹ K⁻¹ — a factor of
  418 between unit systems, and a real source of published inconsistency.
- $\mathrm{d}T/\mathrm{d}z$: K km⁻¹ in the field; convert to K m⁻¹ before
  multiplying. **The single commonest numerical error is multiplying W m⁻¹ K⁻¹ by
  K km⁻¹ and reporting the answer in mW m⁻²** — that is dimensionally consistent
  *only* if the K km⁻¹ is converted, so check the arithmetic with a known example.
- $\kappa$: m² s⁻¹, from $k/(\rho c_p)$. A rock at $\kappa = 10^{-6}$ m² s⁻¹ has a
  diffusion length $\sqrt{\kappa t}$ of 5.6 m in a year and 178 m in a millennium.
- $\Delta T$ in the erfc argument $z/(2\sqrt{\kappa t})$: dimensionless ✓; a $\kappa$
  in cm² s⁻¹ gives a wrong answer by a factor of 10 in length.

## 7. Python demonstration

`code/heatflow_demo.py` computes the flux-continuity check, the disturbance decay
and the GST comparison.

```python
frac = (t_ref / t) * np.exp(-R_W ** 2 / (4 * KAPPA * t)
                            + R_W ** 2 / (4 * KAPPA * t_ref))
bias_grad = dT0 * frac / (L * 1e-3)          # K/km
```

Measured output, abridged:

```
depth (m)   k (W/m/K)   dT/dz (K/km)   q (mW/m^2)   T (degC)
      499        1.50          40.00         60.0       30.00
      501        3.00          20.00         60.0       30.00

elapsed (h)   residual fraction   gradient bias (K/km)   heat-flow bias (%)
          1              1.0000                 10.000             41.67
         24              0.0811                  0.811              3.38
        120              0.0166                  0.166              0.69
       2160              0.0009                  0.009              0.04

depth (m)   history A (K)   history B (K)   difference (K)
       50           0.6563            1.0424          -0.3861
      200           0.0751            0.2267          -0.1516
      500           0.0000            0.0030          -0.0030
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| The gradient halves across the contrast, $q$ does not change | Flux continuity is the first check on any heat-flow profile |
| Bias 41.67 % at 1 h, 3.38 % at 24 h, 0.04 % at 90 days | Equilibration is a days-to-months problem, not an hours one |
| The disturbance biases the gradient much less than the temperature | Gradient-based flow survives an imperfectly equilibrated hole |
| Two GST histories differ by 0.06 K at 300 m and 0.003 K at 500 m | The history is not recoverable below a few hundred metres |
| Noise above a few hundredths of a kelvin removes all discrimination | The output must be a family of histories, not a curve |

> **Breaking exercise.** Change the reference time $t_{\text{ref}}$ from 1 h to 24 h
> and re-run. Predict which rows of the disturbance table change and why; then
> explain what $t_{\text{ref}}$ physically represents and what happens to the model
> when it is large.

## 8. Exercises

[`exercises/01-heat-flow-measurement-exercises.md`](./exercises/01-heat-flow-measurement-exercises.md)
and
[`exercises/01-heat-flow-measurement-solutions.md`](./exercises/01-heat-flow-measurement-solutions.md).

### ★ Foundational

**★1.** State the sign convention used in this lesson and write $q$ for both
choices of the direction of $z$.

**★2.** A gradient of 22 K km⁻¹ and a conductivity of 2.8 W m⁻¹ K⁻¹: compute the
heat flow in mW m⁻².

**★3.** Distinguish an equilibrium temperature from a BHT, and state the sign of the
difference at depth in a conventionally cooled hole.

### ★★ Applied

**★★4.** Run `code/heatflow_demo.py` and report the disturbance table with
$t_{\text{ref}} = 6$ h. State the elapsed time at which the bias falls below 1 per
cent.

**★★5.** A two-layer model has $k_1 = 2.0$ W m⁻¹ K⁻¹ over 0–800 m and
$k_2 = 4.0$ W m⁻¹ K⁻¹ over 800–2000 m, with a surface temperature of 12 °C and a
flux of 70 mW m⁻². Compute the gradient in each layer and the temperature at 800 and
2000 m.

**★★6.** For $\kappa = 1.2\times10^{-6}$ m² s⁻¹, compute the depth at which a step
surface change has decayed to 10 per cent of its amplitude after 100 yr, 1 ka and
10 ka.

### ★★★ Research-oriented

**★★★7.** Invert the demonstration's erfc forward model for a GST history using a
stated parameterisation (say five step changes), synthetic data with 0.02 K noise,
and a Monte Carlo or a linearised inversion. Report the posterior family of
histories and state which time intervals are resolved and which are not.

**★★★8.** A hole shows systematic curvature below 600 m. Using a stated one-
dimensional advection–conduction model with a groundwater flux, show that the
curvature can be explained by a vertical Darcy velocity, estimate the velocity
required, and state the ambiguity between the velocity and a conductivity that
varies with depth.

## 9. Common mistakes

1. **Getting the sign convention wrong**, or not stating it.
2. **Multiplying W m⁻¹ K⁻¹ by K km⁻¹** without converting, and reporting mW m⁻².
3. **Using a conductivity measured parallel to the bedding** in a vertical
   calculation.
4. **Ignoring the drilling disturbance** and reporting a gradient measured hours
   after circulation stopped.
5. **Reading a BHT as a formation temperature.**
6. **Reporting a single GST history** rather than the family consistent with the
   data and its noise.
7. **Fitting a gradient through a curved profile** and hiding the curvature, which
   is the signature of advection or of a surface change.

## 10. Real-world applications

- **Global heat-flow maps.** The primary constraint on the Earth's energy budget and
  on the thermal state of the lithosphere
  ([12-03-02 Global Heat Flow and Its Distribution](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md)).
- **Basin and petroleum thermal history.** Heat flow sets maturity, so an error of
  10 per cent in $q$ moves a maturity estimate
  ([04-06-03 Geothermal Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Geothermal resource assessment.** Heat flow is one of the two inputs to ther
  heat-in-place estimate.
- **Palaeoclimate.** Borehole temperature profiles are one of the few continental
  palaeoclimate proxies, with the non-uniqueness of §3.3 as its honest limit.
- **Permafrost and climate monitoring.** Repeat temperature logs measure the
  propagation of surface warming, which is the same physics in reverse.

## 11. Further reading

- **Carslaw, H. S. & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** Chapters 10 and 13. Level: advanced. The
  line-source and cylinder solutions of §3.2 and the diffusion of surface
  temperature histories.
- **Beardsmore, G. R. & Cull, J. P. (2001). *Crustal Heat Flow: A Guide to
  Measurement and Modelling*. Cambridge University Press.** Level: advanced. The
  standard practical reference: gradients, conductivity, corrections and their
  uncertainties.
- **Jaupart, C. & Mareschal, J.-C. (2011). *Heat Generation and Transport in the
  Earth*. Cambridge University Press.** Level: advanced. The modern treatment of
  the geotherm, the radiogenic partition and crustal heat budgets.
- **Pollack, H. N. & Huang, S. (2000). Climate reconstruction from subsurface
  temperatures. *Annual Review of Earth and Planetary Sciences*, 28, 339–365.**
  Level: advanced. The GST inverse problem, including its non-uniqueness.
- **Bullard, E. C. (1947). The time necessary for a bore hole to attain
  temperature equilibrium. *Monthly Notices of the Royal Astronomical Society*,
  5, 127–130.** Level: advanced. The original analysis of the disturbance of §3.2.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-09-02 Thermal Conductivity Measurement and Corrections](./02-thermal-conductivity.md)
  — the other factor in the product, and its anisotropy.
- [05-09-03 Geothermal Exploration Geophysics](./03-geothermal-exploration.md)
  — where heat flow becomes a resource estimate.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the physics and the diffusion timescales in full.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md)
  — the global geotherm and the heat budget.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](../08-geophysical-logging/07-log-interpretation.md)
  — the uncertainty-reporting discipline applied to a temperature profile.

## Self-assessment checklist

- [ ] I can state the sign convention for both choices of $z$ and derive $q = k\,\mathrm{d}T/\mathrm{d}z$. (§1, §2.1)
- [ ] I can check a heat-flow profile for flux continuity across a conductivity contrast. (§3.1)
- [ ] I can compute the disturbance decay and the heat-flow bias it causes. (§3.2)
- [ ] I can explain why a BHT is not an equilibrium temperature and how Horner extrapolation helps. (§2.2–2.3)
- [ ] I can demonstrate the non-uniqueness of a GST reconstruction. (§3.3)
- [ ] I can estimate a heat flow with an uncertainty budget. (§4.1)
- [ ] I can compute a geotherm with a radiogenic source and the mantle heat flow. (§2.4, §4.3)
- [ ] I can run the demonstration and explain every printed number. (§7)
