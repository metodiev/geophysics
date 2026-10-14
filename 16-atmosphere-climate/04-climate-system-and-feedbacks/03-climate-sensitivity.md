---
id: 16-04-03
title: "Climate Sensitivity: Definitions and Estimation"
level: research
prereqs: ["16-04-02", "16-04-01", "18-02"]
tags: [atmosphere, climate, climate-sensitivity, feedbacks, gregory-regression, ocean-heat-uptake]
---

# Climate Sensitivity: Definitions and Estimation

"Climate sensitivity" is not one number. It is a family of numbers, each defined
by a forcing pathway and a time horizon, and the differences between them are
larger than most of the uncertainties people argue about. The two that matter
most are:

- **Equilibrium climate sensitivity (ECS)**: the surface warming after the
  system has fully equilibrated to a doubled-CO₂ forcing. The demonstration's
  synthetic two-layer model gives **1.0571 K** for its chosen parameters.
- **Transient climate response (TCR)**: the warming at the moment the forcing
  reaches the doubled value, on a prescribed pathway. For a 1% yr⁻¹ CO₂
  increase, the same model gives **0.8688 K**, i.e. 82% of ECS — and with a
  stronger ocean coupling the ratio falls to 71%.

Both are model outputs, and estimating them from data is a separate exercise
with its own pitfalls. The **Gregory regression** — regressing the net
top-of-atmosphere flux on the temperature change — is the standard method, and
this lesson shows what it does and does not recover. In a model where the
feedback parameter drifts with temperature, the regression fits the data with
$R^2 > 0.999$ at every window length and yet returns answers spanning 10%,
because the fitted slope is an average of the feedback parameter over the
temperatures the window happened to sample. A high $R^2$ is evidence that a
straight line fits the data you chose; it is not evidence of an unbiased slope.

All models and data in this module are **SYNTHETIC**. Every capacity, feedback
parameter, drift slope, forcing and assumed range below is a **chosen teaching
value** printed by [`code/climate_sensitivity_demo.py`](code/climate_sensitivity_demo.py).
None is quoted from any assessment, and nothing here is an estimate of the real
Earth's sensitivity.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** ECS and TCR precisely, and **state** the two things that must be
   specified before either is a number.
2. **Compute** both from a two-layer model, and **relate** them through the
   ocean heat uptake efficiency $\kappa$ with the approximation
   $\text{TCR}\approx F_{2\times}/(|\lambda|+\kappa)$.
3. **Perform** a Gregory regression, **state** what it recovers exactly and what
   it recovers only approximately, and **quantify** the dependence of the
   result on the regression window when the feedback drifts.
4. **Explain** why $R^2$ near unity does not validate a sensitivity estimate.
5. **Propagate** an assumed feedback range to a distribution of ECS, and
   **report** it with its median, spread and skew rather than as a single value.
6. **Compare** several estimators of the same quantity, and **state** why their
   differences are not noise.
7. **Compute** how TCR changes with the ocean coupling at fixed ECS, and
   **explain** why TCR is the more constrained quantity.

## Prerequisites

- [16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](../04-climate-system-and-feedbacks/02-climate-feedbacks.md) —
  where $\lambda$ comes from and why it is state-dependent.
- [16-04-01 Components of the Climate System and Their Timescales](../04-climate-system-and-feedbacks/01-climate-system-components.md) —
  the two-layer ocean model used throughout.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  linear regression as an inverse problem, including the distinction between a
  good fit and an unbiased parameter.

## 1. Definitions

| Quantity | Definition | Depends on |
|---|---|---|
| $\lambda$ | $\partial N/\partial T$, total | the climate state |
| $\kappa$ | Ocean heat uptake efficiency, $N/\Delta T$ during a transient | the ocean, the pathway, the time |
| ECS | $\Delta T$ when $N = 0$ for $F = F_{2\times}$ | $\lambda$ at the equilibrium state |
| TCR | $\Delta T$ when $F(t)$ first reaches $F_{2\times}$ on a prescribed pathway | $\lambda$, $\kappa$, and the pathway |
| $F_{2\times}$ | Forcing from doubled CO₂ | the forcing agent and the radiative transfer |

The forcing $F_{2\times}$ is chosen here as $3.7\ \mathrm{W\,m^{-2}}$, and the
pathway for TCR is a 1% yr⁻¹ CO₂ increase, which reaches doubling after
$\ln 2/\ln 1.01 = 69.7$ yr. **Changing either changes the answer**, so "TCR"
without its pathway is incomplete in the same way that "distance" without a
route is.

## 2. Two numbers from one model

The two-layer model of [16-04-01](01-climate-system-components.md) §5 with
$C_m = 2.04\times10^8$, $C_d = 1.37\times10^{10}$ J m⁻² K⁻¹,
$\gamma = 0.7$ W m⁻² K⁻¹ and $|\lambda| = 3.5$ W m⁻² K⁻¹ gives

$$\text{ECS} = \frac{F_{2\times}}{|\lambda|} = \frac{3.7}{3.5}
= 1.0571\ \mathrm{K},$$

and, integrating the same model with $F(t) = F_{2\times}(\ln
1.01/\ln2)t$,

$$\text{TCR} = 0.8688\ \mathrm{K},\qquad
\frac{\text{TCR}}{\text{ECS}} = 0.822,\qquad
\kappa \equiv \frac{N}{\Delta T} = 0.759\ \mathrm{W\,m^{-2}K^{-1}}.$$

The approximation

$$\text{TCR} \approx \frac{F_{2\times}}{|\lambda| + \kappa}$$

returns 0.8688 K — the same number, exactly, because this model is linear: the
relation $N = F - |\lambda|\Delta T$ holds at every instant, so $\kappa$ is
determined by the trajectory rather than estimated from it. The approximation is
*exact here and approximate in reality*; its usefulness is that it shows TCR to
be a competition between the feedback ($|\lambda|$) and the ocean ($\kappa$).

## 3. The Gregory regression, and its window

The method: apply a step forcing $F_{2\times}$, record $N(t)$ and
$\Delta T(t)$, and regress $N$ on $\Delta T$. The intercept estimates
$F_{2\times}$ and the slope estimates $\lambda$ (here, $-|\lambda|$), so
$\text{ECS} \approx F_{2\times}/|\text{slope}|$.

In a model with a *constant* $\lambda$ the regression is exact at any window.
Real systems are not so kind. Let the feedback strengthen with warming,
$|\lambda(T)| = 3.50 + 1.00\,T$ W m⁻² K⁻¹, so that the model's own equilibrium
is 0.8505 K — the linear estimate $F_{2\times}/3.5 = 1.0571$ K is **24% above**
it. Regressing over increasing windows:

| window (yr) | slope (W m⁻² K⁻¹) | intercept | $R^2$ | $\lvert\lambda\rvert$ at end | ECS from slope |
|---|---|---|---|---|---|
| 20 | 4.4749 | 3.8755 | 0.99836 | 4.250 | 0.8268 |
| 50 | 4.4891 | 3.8810 | 0.99841 | 4.255 | 0.8242 |
| 100 | 4.4996 | 3.8859 | 0.99837 | 4.261 | 0.8223 |
| 200 | 4.5236 | 3.9002 | 0.99809 | 4.273 | 0.8179 |
| 500 | 4.6477 | 3.9877 | 0.99666 | 4.300 | 0.7961 |
| 1000 | 4.8351 | 4.1285 | 0.99641 | 4.326 | 0.7652 |
| 2000 | 4.9737 | 4.2357 | 0.99752 | 4.345 | 0.7439 |

Three readings, in order of importance:

1. **The window matters.** The ECS implied by the same model and the same
   experiment ranges from 0.8268 K (20 yr) to 0.7439 K (2000 yr) — a spread of
   10.0% — and it moves *systematically* with length rather than scattering.
2. **$R^2$ does not detect it.** Every row has $R^2>0.996$. The fit is excellent
   because $N$ really is almost linear in $\Delta T$ over each window; the
   *slope* is nonetheless biased, because it is an average of $|\lambda|$ over
   the temperatures that window sampled, weighted by the shape of the
   trajectory, while ECS is governed by $|\lambda|$ at the equilibrium
   temperature.
3. **The intercept is not pristine either.** It runs from 3.876 to 4.236 against
   a true forcing of 3.7, a 14% overestimate at the longest window, and again
   purely from the curvature.

The lesson's quantitative content is therefore not "the regression gives ECS" but
"the regression gives a *state-weighted average* of the feedback parameter, and
that average is only the equilibrium one if the feedback does not drift".

## 4. One number or a distribution?

Assume the total feedback is uniform on $[-3.0, -1.5]$ W m⁻² K⁻¹ — a **chosen**
range — and compute $\text{ECS} = -F_{2\times}/\lambda$:

| percentile | ECS (K) |
|---|---|
| 1 | 1.240 |
| 5 | 1.265 |
| 25 | 1.410 |
| 50 | 1.645 |
| 75 | 1.976 |
| 95 | 2.350 |
| 99 | 2.442 |

with mean 1.711 K, median 1.645 K, sd 0.346 K and skewness 0.483. Three
consequences:

- **The distribution is skewed**, because ECS is the reciprocal of a quantity
  whose range approaches zero from below. The mean exceeds the median, and the
  upper tail is long: the 99th percentile is 1.5× the median.
- **A single number must be labelled.** "1.7 K" is the mean; "1.65 K" is the
  median; "1.3–2.4 K" is the 5–95% range. All three are correct summaries of the
  same model output, and they answer different questions.
- **The range is an assumption.** It came from the assumed uniform
  distribution of $\lambda$, nothing else. A different functional form with the
  same endpoints gives a different median.

## 5. Five estimators side by side

| estimator | value (K) | implied $\lvert\lambda\rvert$ | error vs truth |
|---|---|---|---|
| true equilibrium of the model | 0.8505 | 4.350 | — |
| ECS, Gregory 50 yr | 0.8242 | 4.4891 | $-3.1\%$ |
| ECS, Gregory 150 yr | 0.8203 | 4.5104 | $-3.5\%$ |
| ECS, Gregory 500 yr | 0.7961 | 4.6477 | $-6.4\%$ |
| TCR, from the 1% yr⁻¹ ramp | 0.3894 | — | — |

The ECS estimates differ from each other by up to 3.5% and from the model's own
equilibrium by up to 6.4%, and the TCR is a different quantity altogether —
**46% of ECS** for this pathway. The honest statement of a sensitivity estimate
therefore has four parts: the quantity (ECS or TCR), the estimator (regression,
fit to observations, palaeoclimate constraint), the window or pathway, and the
model or data set. Anything less is a number in search of a definition.

## 6. Why TCR is the friendlier target

Fix ECS by fixing $|\lambda| = 3.5$ W m⁻² K⁻¹ and vary only the ocean coupling:

| $\gamma$ (W m⁻² K⁻¹) | TCR (K) | TCR/ECS | $\kappa$ at doubling (W m⁻² K⁻¹) |
|---|---|---|---|
| 0.3 | 0.9515 | 0.900 | 0.389 |
| 0.5 | 0.9076 | 0.859 | 0.577 |
| 0.7 | 0.8688 | 0.822 | 0.759 |
| 1.0 | 0.8182 | 0.774 | 1.022 |
| 1.5 | 0.7497 | 0.709 | 1.435 |

ECS is *identical* in every row, and TCR spans a factor of 1.27 (from 0.9515 to
0.7497). The transient response is governed by how fast the ocean buries heat,
which is a property of decades; the equilibrium response is governed by a
feedback parameter evaluated in a state that has never been observed. That
asymmetry is the reason transient quantities are generally better constrained
than equilibrium ones, and it is also why an estimate of TCR is not an estimate
of ECS.

## 7. Assumptions and regime of validity

1. **Linearity of the feedback.** Sections 2 and 6 use a constant $\lambda$.
   Section 3 deliberately breaks this and shows the consequence: a 24% error in
   ECS if the drift is ignored, and a 10% window dependence in the regression.
2. **A single global temperature.** No pattern effect: the spatial structure of
   the warming is assumed irrelevant, which is exactly what real Gregory
   regressions worry about.
3. **A two-box ocean.** $\kappa$ is a trajectory property of this model, not an
   observable.
4. **Prescribed forcing pathway.** TCR depends on the 1% yr⁻¹ choice. A faster
   ramp gives a smaller TCR; a slower one approaches ECS.
5. **A chosen $F_{2\times}$.** 3.7 W m⁻² is used throughout; a different value
   scales every $\Delta T$ linearly.
6. **No aerosol, no carbon cycle, no ice sheet** is coupled; each would change
   the effective $\lambda$ or add a slow reservoir.
7. **Assumed ranges everywhere in Section 4.** The distribution is a direct
   consequence of that assumption and nothing else.

## 8. Worked examples

### Example 1 — ECS, TCR and $\kappa$

$$\text{ECS} = \frac{3.7}{3.5} = 1.0571\ \mathrm{K},\qquad
\kappa = \frac{N}{\Delta T}\bigg|_\text{doubling}
= \frac{3.7 - 3.5\times0.8688}{0.8688} = 0.759\ \mathrm{W\,m^{-2}K^{-1}},$$

$$\frac{F_{2\times}}{|\lambda|+\kappa} = \frac{3.7}{3.5 + 0.759}
= 0.8688\ \mathrm{K} = \text{TCR}.$$

The agreement is exact because the model is linear; in a model with a drifting
feedback it would not be.

### Example 2 — the window bias

With the drift, the slope from the 2000-year window is 4.9737 W m⁻² K⁻¹ against
an equilibrium value of 4.350 W m⁻² K⁻¹: a 14% bias that propagates to a 13%
error in ECS (0.7439 against 0.8505). The bias is not an error in arithmetic —
the regression is correct; the *estimand* is not ECS.

### Example 3 — a percentile to a range

From the assumed uniform $\lambda\in[-3.0,-1.5]$ W m⁻² K⁻¹, the 5–95% range of
ECS is $1.265$–$2.350$ K, i.e. a factor of 1.86. Note that the range is *not*
symmetric about the median: $1.645 - 1.265 = 0.380$ below and $2.350 - 1.645 =
0.705$ above. Reporting "ECS = 1.6 ± 0.4 K" would misrepresent both the skew and
the upper tail.

## 9. Python demonstration

[`code/climate_sensitivity_demo.py`](code/climate_sensitivity_demo.py) prints
every number above: ECS and TCR with the $\kappa$ approximation; the Gregory
regression over seven windows with $R^2$ and the implied ECS; the ECS
distribution from an assumed feedback range; the five-estimator comparison; and
the TCR-versus-$\gamma$ survey. It integrates the two-layer model with a
fourth-order Runge–Kutta step in seconds and reports time in years. It needs no
network, runs in about three seconds, and exits 0.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/03-climate-sensitivity-exercises.md`](exercises/03-climate-sensitivity-exercises.md)
and
[`exercises/03-climate-sensitivity-solutions.md`](exercises/03-climate-sensitivity-solutions.md).

- **★** Compute ECS and TCR for $|\lambda| = 4.0$ W m⁻² K⁻¹ with
  $F_{2\times} = 3.7$, and the ratio.
- **★** Compute the doubling time for a 0.5% yr⁻¹ CO₂ increase and state whether
  the TCR on that pathway would be larger or smaller than on the 1% yr⁻¹ path.
- **★★** From the approximation $\text{TCR} = F_{2\times}/(|\lambda|+\kappa)$,
  compute TCR for $|\lambda| = 3.5$ and $\kappa \in \{0.4, 0.8, 1.4\}$, and state
  the limiting value as $\kappa\to0$.
- **★★** Using the assumed uniform $\lambda\in[-3.5,-2.0]$, compute the median
  ECS, the 5–95% range and the ratio of the range's upper half-width to its
  lower half-width, and comment on the skew.
- **★★★** A study reports ECS from a Gregory regression over 150 years with
  $R^2 = 0.998$. Construct the argument that this does not establish the value,
  using the lesson's table as evidence, and state the additional diagnostic you
  would request.

## 11. Common mistakes

1. **Quoting ECS without the feedback set and the model.** ECS is a model
   output, not a measurement.
2. **Treating TCR as a second estimate of ECS.** They differ by construction and
   are governed by different parameters.
3. **Reporting a mean of a skewed distribution.** Section 4's mean and median
   differ, and so do any two quantiles.
4. **Using $R^2$ as a validation of a slope.** Section 3's table is the
   counterexample.
5. **Forgetting the pathway in TCR.** The 1% yr⁻¹ convention is a definition,
   not a law.
6. **Assuming the intercept of a Gregory regression is the forcing.** It is a
   regression intercept, biased by the same curvature as the slope.
7. **Extrapolating a transient response to equilibrium by a fixed ratio.** The
   ratio is a property of the pathway and of the ocean.

## Mastery checkpoint

Complete this without notes.

> A two-layer model with $C_m = 2.0\times10^8$, $C_d = 1.4\times10^{10}$
> J m⁻² K⁻¹, $\gamma = 0.9$ W m⁻² K⁻¹ has $|\lambda| = 3.0\
> \mathrm{W\,m^{-2}K^{-1}}$ and is forced by $F_{2\times} = 3.7\
> \mathrm{W\,m^{-2}}$.
> **(a)** Compute ECS.
> **(b)** State the sign of the change in TCR if $\gamma$ is halved, and compute
> the two TCRs from the approximation with
> $\kappa = \gamma/0.75$ (a chosen closure).
> **(c)** A Gregory regression on this model returns a slope of
> $-3.4\ \mathrm{W\,m^{-2}K^{-1}}$. Compute the implied ECS and state the
> implied drift direction of the feedback.
> **(d)** State two reasons a real regression of the same kind would be less
> trustworthy than this synthetic one.
> **(e)** State the four things a sensitivity estimate must specify to be
> meaningful.

A worked version of (a)–(c) appears in the lesson-03
[solutions](exercises/03-climate-sensitivity-solutions.md).

## Common pitfalls

- **Confusing $\kappa$ with a physical constant.** It is $N/\Delta T$ during a
  particular transient, not a property of seawater.
- **Assuming the feedback parameter is state-independent** when the whole point
  of the exercise is often to detect that it is not.
- **Treating the forcing $F_{2\times}$ as known to three figures.** It enters
  every product linearly.
- **Reading a distribution's mean as its "expected" outcome** when the
  distribution is skewed and the quantity is a ratio.
- **Ignoring the ocean when comparing sensitivity estimates from different
  periods.** Two decades with different $\kappa$ give different TCRs even with
  identical feedbacks.

## Related modules

- [01 Components of the Climate System and Their Timescales](01-climate-system-components.md) —
  the model used here.
- [02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](02-climate-feedbacks.md) —
  where $\lambda$ comes from.
- [04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](04-natural-variability.md) —
  the variability that contaminates any regression on a short record.
- [05 The Carbon Cycle: Reservoirs, Fluxes and Perturbations](05-carbon-cycle.md) —
  the other half of a scenario calculation.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) —
  how ECS and TCR are actually computed in models, and with what spread.
- [16-06 Palaeoclimate](../06-palaeoclimate/README.md) —
  the empirical constraints from climates far from the present.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  regression, bias and the difference between a fit and an estimate.
