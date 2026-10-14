---
id: 13-04-03
title: "Postseismic Relaxation and Viscoelastic Models"
level: research
prereqs: ["13-04-02", "02-04-07", "13-01-02"]
tags: [geodynamics, tectonophysics, postseismic, viscoelasticity, maxwell, relaxation, afterslip]
---

# Postseismic Relaxation and Viscoelastic Models

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Maxwell relaxation time $\tau = \eta/\mu$ from the
   constitutive law, and **verify** it by integrating the same law numerically.
2. **Fit** a postseismic surface-displacement transient with a single
   exponential and **report** the decay constant with its uncertainty and its
   correlations.
3. **Show** how the observation window controls whether a decay constant is
   determined, using a misfit grid on two different windows.
4. **Compare** an afterslip logarithm with a viscoelastic exponential and
   **state** what the residuals do and do not distinguish.
5. **Explain** why a layered viscosity produces a relaxation spectrum, and what a
   single fitted decay constant means in that case.
6. **State** the assumptions of a single-relaxation-time model and **identify**
   the observations that break them.

## Prerequisites

- [13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](02-fault-mechanics.md) —
  the coseismic stress change that sets the transient in motion.
- [02-04-07 Viscoelasticity](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  Maxwell, Kelvin–Voigt and the meaning of a relaxation time.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  where the viscosity comes from and how uncertain it is.

All models and data in this module are **SYNTHETIC**. The viscosities,
transient amplitudes and noise are chosen teaching values. No real earthquake,
GNSS time series or published viscosity estimate is used or quoted. The exact
constant used is the number of seconds in a year,
$1\ \mathrm{yr} = 3.1558\times10^{7}\ \mathrm{s}$.

## 1. The Maxwell time, derived

A Maxwell material in shear combines an elastic and a viscous response in
series. Its strain rate is the sum of the two contributions:

$$
\dot e = \frac{\dot\sigma}{2\mu_e} + \frac{\sigma}{2\eta},
$$

where $\mu_e$ is the shear modulus and $\eta$ the viscosity. The first term is
the elastic part (Hooke's law differentiated), the second is Newtonian viscous
flow. **Impose a constant strain** ($\dot e = 0$), as happens just after an
earthquake when the far field has not moved:

$$
\frac{\dot\sigma}{2\mu_e} = -\frac{\sigma}{2\eta}
\;\;\Longrightarrow\;\;
\dot\sigma = -\frac{\mu_e}{\eta}\,\sigma
\;\;\Longrightarrow\;\;
\sigma(t) = \sigma_0\,e^{-t/\tau},
\qquad
\boxed{\;\tau = \frac{\eta}{\mu_e}\;}
$$

The stress relaxes exponentially, with a time constant set by the ratio of
viscosity to elastic modulus and **independent of the stress magnitude**. That
independence is what makes $\tau$ a material property rather than a
configuration-dependent one, and it is why a single decay constant is so
tempting to interpret.

For $\mu_e = 30\ \mathrm{GPa}$:

| $\eta$ (Pa s) | $10^{19}$ | $10^{20}$ | $10^{21}$ |
|---|---|---|---|
| $\tau = \eta/\mu_e$ (yr) | 10.56 | 105.63 | 1056.27 |
| numerical $1/e$ time (yr) | 10.56 | 105.63 | 1056.27 |

The third column is an independent check: the demonstration integrates
$\dot\sigma = -\sigma/\tau$ with a small step and measures the time at which
$\sigma = e^{-1}$, recovering $\eta/\mu_e$ to better than $0.01\%$. That test
catches the most common error in this subject — a factor of two — because the
alternative convention $\tau = 2\eta/\mu_e$ (which arises when the elastic
compliance is written $\sigma/(2\mu_e)$ *and* the two is carried inconsistently)
would fail it immediately. **The relaxation time depends on the convention for
the elastic shear strain; state it.**

## 2. A single-relaxation-time transient

The demonstration generates a SYNTHETIC transient with exactly one decay
constant, $\tau_{\text{true}} = 10.563\ \mathrm{yr}$:

$$
D(t) = 0.25 - 0.17\,e^{-t/10.563}\ \mathrm{m},
$$

sampled at $42$ epochs between $0.02$ and $30\ \mathrm{yr}$ with
$4.0\ \mathrm{mm}$ Gaussian noise per sample — a realistic combination of
sampling density and precision for a decade of campaign GNSS. A weighted
least-squares fit gives

$$
D(t) = 0.2493 - 0.1701\,e^{-t/10.306},\qquad
\tau = 10.306 \pm 0.412\ \mathrm{yr}\;
(-2.4\%\ \text{versus truth}),
$$

with an rms residual of $4.20\ \mathrm{mm}$ against the $4.0\ \mathrm{mm}$ input
noise. The fit is good and the recovered $\tau$ is biased low by $2.4\%$, i.e.
about $0.6\sigma$ — not significant at this realisation, but a reminder that a
$\pm4\%$ error on $\eta$ is unavoidable at this noise level.

The correlations are the part that must be reported:

$$
\mathrm{corr}(\tau, \text{amplitude}) = +0.685, \qquad
\mathrm{corr}(\tau, D_\infty) = +0.892 .
$$

Both are strongly positive. Increasing $\tau$ slows the approach to the
asymptote; the fit compensates by increasing $D_\infty$ and the amplitude
together. Reporting $\tau$ without the covariance therefore hides the fact that
the "total" postseismic displacement is itself uncertain by more than the
statistical error on any single sample.

## 3. The window decides whether $\tau$ is determined

A grid search over $(\tau, \text{amplitude})$ with $\chi^{2}$ evaluated against
the same noisy data gives two very different answers depending on how much of the
transient is observed:

| window | samples | best $\tau$ (yr) | $\Delta\chi^{2}=1$ range | amplitude range (m) |
|---|---|---|---|---|
| $0.02$–$30\ \mathrm{yr}$ | 42 | 10.50 | 10.30–10.60 | 0.170–0.172 |
| $0.02$–$1.5\ \mathrm{yr}$ | 13 | 15.40 | 13.40–23.60 | 0.166–0.168 |

and the shape of the trade-off at fixed $\tau$:

| fixed $\tau$ (yr) | least-misfit amplitude, full window | $\chi^{2}$ | least-misfit amplitude, short window | $\chi^{2}$ |
|---|---|---|---|---|
| 3 | 0.212 | 4956 | 0.192 | 239 |
| 6 | 0.190 | 1054 | 0.178 | 55.0 |
| 11 | 0.168 | 56.5 | 0.170 | 22.6 |
| 22 | 0.144 | 1413 | 0.166 | 20.2 |
| 40 | 0.134 | 2418 | 0.164 | 22.3 |

**Reading the table.** Over the thirty-year window, $\tau$ is determined to a few
per cent because the data see both the curvature and the flattening: moving
$\tau$ to $3\ \mathrm{yr}$ or $40\ \mathrm{yr}$ wrecks the fit even after
re-optimising the amplitude. Over the one-and-a-half-year window, the best fit is
at $\tau = 15.4\ \mathrm{yr}$ — $46\%$ too long — and the accepted range spans
$13.4$–$23.6\ \mathrm{yr}$: **the transient is barely distinguishable from a
straight line, so the decay constant and the amplitude trade off almost
perfectly.**

The general rule, stated so it can be used before an experiment is designed:

$$
\text{$\tau$ is only determined if the observation window spans a few times }\tau .
$$

If the window is shorter, the fitted $\tau$ is a lower bound dressed as a
measurement. And because $\eta = \mu_e\tau$, the viscosity inherits the error
directly and linearly.

## 4. Afterslip versus viscoelastic relaxation

Postseismic transients are conventionally fitted by either

$$
\text{viscoelastic: } D(t) = D_\infty - A\,e^{-t/\tau}
\qquad\text{or}\qquad
\text{afterslip: } D(t) = a\,\ln\!\left(1 + t/t^{*}\right).
$$

The demonstration tests whether the data can choose, in both directions:

| data | exponential fit rms | logarithm fit rms | ratio |
|---|---|---|---|
| SYNTHETIC exponential (42 samples) | 4.20 mm | 18.98 mm | 4.52 |
| SYNTHETIC logarithmic (400 samples) | 10.56 mm | 4.01 mm | 2.63 |

Two honest conclusions:

1. **The functional forms are distinguishable when the data are good.** A factor
   of $4.5$ in rms is decisive for the exponential data, and $2.6$ for the
   logarithmic data. With this sampling density and noise level, a single
   well-sampled transient can be classified.
2. **But a factor of two to four is not an order of magnitude**, so the
   discrimination rests on details of the noise model and the sampling, and it
   improves only slowly with more data. Over a **two-decade** window each form
   absorbs the other to within a small factor; neither is ruled out by an
   order-of-magnitude misfit.

The discriminants that actually work are physical rather than statistical:

- **Depth migration.** Afterslip is confined to the coseismic rupture plane, so
  the surface pattern of displacement stays geometrically similar in time.
  Viscoelastic relaxation spreads into the deep crust, so the *shape* of the
  displacement field changes measurably with time.
- **Magnitude and location.** Relaxation can produce transients far from the
  rupture, which afterslip cannot.
- **Predicted amplitude.** The total viscoelastic contribution is bounded by the
  coseismic stress change and the rheology; a transient far larger than that
  bound is afterslip (or a data problem).

## 5. A layered viscosity has no single relaxation time

Suppose the postseismic response is the sum of two exponential modes from two
layers, with SYNTHETIC parameters

$$
\tau_1 = 10.56\ \mathrm{yr}\ (\text{weight } 0.6), \qquad
\tau_2 = 52.81\ \mathrm{yr}\ (\text{weight } 0.4),
$$

which is what a viscosity that increases by a factor of five with depth
produces. Fitting a **single** exponential to that two-mode curve gives

$$
D(t) = 0.2221 - 0.1219\,e^{-t/13.042}, \qquad \text{rms residual } 0.28\
\mathrm{mm},
$$

with $\tau_{\text{fit}} = 13.04\ \mathrm{yr}$ — **neither $10.56$ nor
$52.81\ \mathrm{yr}$** — and an rms residual of only $0.28\ \mathrm{mm}$, which
is smaller than the noise level of almost any real data set. Note also that
$D_\infty$ is recovered as $0.2221$ against a true $0.25\ \mathrm{m}$: the slow
mode is unresolved in a thirty-year window, so its contribution is absorbed into
the asymptote.

The consequences are the important part:

- **$\tau_{\text{fit}}$ is an effective value that depends on the observation
  window.** Extend the window and it grows toward the slow mode; shorten it and
  it approaches the fast one.
- **A layered Earth therefore cannot be inverted for "the viscosity".** Only the
  combination of a layer structure and a viscosity is constrained, and the two
  trade off.
- **Reporting one $\eta$ from one decay constant is only defensible when the
  layer structure is independently constrained** — by the depth extent of
  seismicity, by heat flow, or by the spatial pattern of the transient.

The same reasoning explains why quoted postseismic viscosities span orders of
magnitude across the literature while the underlying observations are broadly
similar: the models differ in how many modes they allow and over what window
they are fitted.

## 6. Assumptions and regime of validity

1. **A single Maxwell time.** The Earth has a relaxation spectrum: viscosity
   varies with depth, temperature and stress, and there is transient (primary)
   creep in olivine. Section 5 shows what a two-mode reality does to a
   one-mode interpretation.
2. **A constant imposed strain.** More generally the relaxation is driven by the
   coseismic stress change through the momentum equation, which redistributes
   stress spatially. The scalar Maxwell derivation gives the right *scale*, not
   the spatial pattern.
3. **The window must be long compared with $\tau$** for $\tau$ to be determined
   (Section 3). This is an experimental design constraint, not a modelling
   preference.
4. **Small strain, linear viscoelasticity.** Postseismic strains are tiny
   ($10^{-6}$–$10^{-5}$), so this holds; it would fail for a large
   postglacial rebound over many cycles.
5. **No poroelastic rebound.** Pore-fluid diffusion produces its own
   short-lived transient (days to months) with a diffusivity, not a viscosity, as
   the controlling parameter. Fitting it with a Maxwell time gives a wrong
   viscosity with a small residual.
6. **No afterslip included.** In reality both occur together, and a two-process
   decomposition is usually required.
7. **Elastic parameters known.** $\tau \propto 1/\mu_e$, so a $10\%$ error in
   $\mu_e$ is a $10\%$ error in $\eta$ at fixed $\tau$.

## 7. Worked example — how long a campaign does a viscosity need?

A SYNTHETIC project wants to determine the viscosity of a mid-crustal layer to
$\pm20\%$, and expects $\eta \approx 5\times10^{19}\ \mathrm{Pa\,s}$ with
$\mu_e = 30\ \mathrm{GPa}$.

1. **Relaxation time.** $\tau = 5\times10^{19}/3\times10^{10} =
   1.667\times10^{9}\ \mathrm{s} = 52.8\ \mathrm{yr}$.
2. **Window required.** The rule from Section 3 — a few times $\tau$ — says the
   transient must be observed for something like $100$–$150\ \mathrm{yr}$.
3. **What a 20-year campaign gives.** From the short-window experiment, a window
   of $0.14\tau$ yielded a $\Delta\chi^{2}=1$ range of $\tau$ from $13.4$ to
   $23.6\ \mathrm{yr}$, i.e. $+27\%/-25\%$ around a best-fit value that was
   itself $46\%$ too long. Scaling that conclusion to this case, a twenty-year
   campaign on a $52.8\ \mathrm{yr}$ relaxation gives a $\tau$ that is a lower
   bound with a factor-of-two possible range, and a viscosity error far outside
   the $\pm20\%$ target.
4. **The honest design response.** Either extend the campaign beyond a century
   (rarely possible), or add an independent constraint on the layer thickness so
   that the effective $\tau$ can be converted to a viscosity with a stated model
   ([13-03-04](../03-plate-tectonics-quantitative/04-basin-geodynamics.md) shows
   the same logic for the thermal time constant of a basin).

The point of the example is not the number but the workflow: **convert the target
precision into a required window before collecting the data**, and be prepared for
the answer to be "not feasible with these data".

## 8. Python demonstration

`code/postseismic_viscoelastic_demo.py` prints labelled results with units and
exits 0. It:

1. derives $\tau = \eta/\mu_e$ and verifies it by integrating the constitutive
   law and measuring the $1/e$ time for three viscosities;
2. fits a single exponential to a noisy SYNTHETIC transient and reports
   $\tau \pm \sigma$ with the parameter correlations;
3. maps the $(\tau,\text{amplitude})$ misfit for the full and the short window,
   showing where $\tau$ is determined and where it is not;
4. fits a logarithm and an exponential to each other's synthetic data and reports
   the rms ratios in both directions;
5. fits a single exponential to a two-mode synthetic curve, showing that the
   fitted $\tau$ equals neither mode and that the residual is smaller than
   typical noise.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC postseismic transient is fitted by
> $D(t) = 0.30 - 0.12\,e^{-t/\tau}$ with $\tau = 8.0 \pm 0.6\ \mathrm{yr}$ from
> $15$ years of data, and $\mu_e = 30\ \mathrm{GPa}$.
> **(a)** Compute the implied viscosity and its uncertainty.
> **(b)** State whether the window is long enough to determine $\tau$, and what
> the demonstration's short-window experiment implies for the sign of the bias.
> **(c)** An alternative fit uses the logarithm $D(t) = a\ln(1+t/t^{*})$. State
> two physical observations that would distinguish the two mechanisms, and
> explain why the residuals alone may not.
> **(d)** A colleague reports a second transient with $\tau = 40\ \mathrm{yr}$
> from the same data set and interprets it as a deeper, more viscous layer.
> Give one reason this interpretation might be an artefact.

## Common pitfalls

1. **Forgetting the factor-of-two convention.** $\tau = \eta/\mu_e$ versus
   $2\eta/\mu_e$ changes the viscosity by a factor of two; the demonstration's
   numerical check exists to catch exactly this.
2. **Reporting $\tau$ without its correlations.** With
   $\mathrm{corr}(\tau,D_\infty) = +0.89$ in the demonstration, $\tau$ and the
   total displacement are not independent numbers.
3. **Fitting a decay constant from a window shorter than the decay.** A
   $1.5\ \mathrm{yr}$ window on a $10.6\ \mathrm{yr}$ transient returned
   $15.4\ \mathrm{yr}$ with a $13$–$24\ \mathrm{yr}$ range.
4. **Treating "exponential beats logarithm" as a mechanism identification.**
   The rms ratio is a factor of a few, not an order of magnitude; physical
   discriminants are needed.
5. **Quoting one viscosity from one $\tau$ in a layered Earth.** The fitted value
   depends on the window and on the layer structure.
6. **Ignoring poroelastic rebound.** It produces a transient with a completely
   different controlling parameter and a small residual when misfitted.
7. **Assuming the coseismic stress change is the only driver.** Afterslip on the
   same fault is usually present and is not a viscoelastic process.

## Related modules

- [13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](02-fault-mechanics.md) —
  the stress change that drives the relaxation.
- [13-04-04 Interseismic Coupling and Megathrust Locking](04-interseismic-coupling.md) —
  the same transients that must be removed before estimating coupling.
- [13-01-02 Rheology of the Earth](../01-geodynamic-principles/02-rheology-of-earth.md) —
  where $\eta$ comes from and how wide its range is.
- [13-06-03 Glacial Isostatic Adjustment](../06-crustal-and-lithospheric-dynamics/03-glacial-isostatic-adjustment.md) —
  the same relaxation physics on a glacial timescale.
- [02-04-07 Viscoelasticity](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md).
- [18-04 Nonlinear Inversion](../../18-inverse-problems/04-nonlinear-inversion/README.md) —
  fitting exponentials and the parameter trade-offs they carry.
