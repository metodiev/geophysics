---
id: 07-05-04
title: "Mass Concentration Solutions, Leakage and Filtering"
level: research
prereqs: ["07-05-01", "07-05-03", "18-01-01"]
tags: [gravity, geodesy, satellite-gravimetry, inverse-problems, regularization]
---

# Mass Concentration Solutions, Leakage and Filtering

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a spherical-harmonic solution from a mass-concentration
   (mascon) solution, and state what each parametrisation claims about the mass
   field before any data are used.
2. **Derive** the surface-mass-to-coefficient forward model and **verify** it
   against exact mass balance for a uniform layer.
3. **Quantify** the bias introduced by truncating at degree $L$ when the region
   of interest is comparable with the resolution scale $\pi R/L$.
4. **Define** leakage operationally, **measure** it for a stated filter, and
   report it as a number rather than as a caveat.
5. **Derive** and use a Gaussian harmonic filter and **evaluate** the
   bias–leakage–noise trade for a stated science question.
6. **Show** why two adjacent sources cannot be separated without an assumption,
   and **identify** the filter width matched to the source size.
7. **Write** a defensible regional mass-change statement: measured, converted,
   chosen, inferred.

## Prerequisites

- [01 GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) —
  the coefficients, the noise, and the equivalent-water-height conversion.
- [03 Spherical Harmonic Solutions and Coefficient Interpretation](03-spherical-harmonic-solutions.md) —
  the synthesis and analysis formulas used here.
- [18-01-01 Forward and Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) —
  the vocabulary of parametrisation, rank and non-uniqueness.

> **All models and data in this module are SYNTHETIC.** The truth field, the
> observation operator, the Love-number law, the filter and the noise are all
> chosen teaching values; no measured mass change is used anywhere.

## 1. Two parametrisations, two sets of prior beliefs

A **spherical-harmonic solution** reports coefficients $\Delta C_{lm},
\Delta S_{lm}$ plus a covariance, up to some degree. Its implied statement about
the mass field is that the field *is* band-limited — no power above $L$ — and
the basis is global, smooth and fixed by Laplace's equation.

A **mascon** (mass concentration) solution reports a mass (or EWH) for each tile
of a discrete grid. Its implied statement is that the mass is piecewise constant
on tiles of a stated size, which puts all of the high-degree power *inside* each
tile and none at the tile boundaries.

Neither parametrisation is neutral: both are priors. The practical consequences:

| | spherical-harmonic | mascon tile |
|---|---|---|
| unknown count at $L = 40$ | 1677 | as many tiles as the grid has |
| resolution | $\pi R/L \approx 500\ \mathrm{km}$ | the tile size, chosen |
| natural output | global, smooth | regional, with visible tile edges |
| where the prior acts | the a priori spectrum | the piecewise-constant assumption |
| what must be reported | $L$, the error covariance | the tile size, the regularisation |

In practice the useful question is never "which is right" but "what does this
particular statement assume", and for a mascon the answer is: the tile size, the
regularisation that stabilises an underdetermined system, and the spatial
averaging kernel the regularisation implies.

## 2. The forward model, and the check that fixes its constants

The **layer formula** from [01](01-grace-gracefo.md), in the $4\pi$ normalisation
of [03](03-spherical-harmonic-solutions.md), is

$$\Delta C^{\text{layer}}_{lm} = \frac{3}{4\pi\rho_e R (2l+1)}
\iint \Delta\sigma(\theta',\phi')\,\bar P_{lm}(\cos\theta')\cos m\phi'\;
\mathrm{d}\Omega' ,$$

with $\Delta\sigma = \rho_w \times \mathrm{EWH}$ the surface density and
$\Delta C^{\text{observed}}_{lm} = (1+k_l)\Delta C^{\text{layer}}_{lm}$ for load
Love numbers $k_l$.

At $l = 0$, $\bar P_{00} = 1$ and $\iint\Delta\sigma\,\mathrm{d}\Omega =
4\pi\bar t$ where $\bar t$ is the global mean EWH, so

$$\Delta C_{00} = \frac{3\bar t\,\rho_w}{\rho_e R}.$$

**This is the check.** The demonstration integrates its synthetic truth over a
$90 \times 180$ Gauss grid and obtains $\Delta C_{00} = 1.729567\times10^{-9}$
against the closed form $3\rho_w\bar t/(\rho_e R) = 1.729567\times10^{-9}$: a
relative agreement of $1.196\times10^{-16}$, i.e. exact to round-off. Without
such a check, a missing $4\pi$ or a stray $R$ would survive every plot and
corrupt every mass budget by orders of magnitude — as indeed they did during the
writing of this demonstration, until the check was run.

*Worked example 1.* A synthetic disc of $30\ \mathrm{cm}$ EWH and radius
$300\ \mathrm{km}$ contains

$$m = \rho_w t \pi r^{2} = 1000 \times 0.30 \times \pi(3\times10^{5})^{2}
= 8.4823\times10^{13}\ \mathrm{kg}.$$

Spread over the whole Earth ($A = 4\pi R^{2} = 5.1006\times10^{14}\
\mathrm{m^{2}}$), that mass is a global mean rise of
$m/(\rho_w A) = 8.4823\times10^{13}/(1000\times5.1006\times10^{14})
= 0.1663\ \mathrm{mm}$. Two such discs give $0.3326\ \mathrm{mm}$, but the
demonstration *measures* $0.2509\ \mathrm{mm}$ — because its grid quantises the
disc area (grid spacing $\sim2^\circ$, disc radius $2.7^\circ$). **The truth is
itself a discretised assumption**, and quoting the analytic value as if it were
the truth would be a self-inflicted error.

## 3. Truncation is not noise

Band-limiting a field is a *systematic* operation: it removes signal, and the
removed signal does not average out. The demonstration's round trip — forward
model to degree 40, then exact reconstruction to the same degree, with no filter
and no noise — gives a global rms residual of only $5.1108\ \mathrm{mm}$, but the
*regional* quantities are biased:

| cap radius | truth (cm EWH) | recovered (cm EWH) | bias, as % of disc amplitude |
|---|---|---|---|
| 300 km | 32.000 | 21.734 | $-34.2\%$ |
| 600 km | 8.458 | 11.145 | $+9.0\%$ |
| 1200 km | 3.694 | 3.985 | $+1.0\%$ |
| 2000 km | 3.018 | 3.209 | $+0.6\%$ |

The pattern is the whole lesson in one table: **a cap whose radius is comparable
with the resolution scale ($\pi R/L = 500\ \mathrm{km}$ at $L = 40$) loses a third
of the signal, while a cap four times larger is accurate to about a per cent.**
The remedy is not a better inversion; it is a bigger region, or a higher $L$. Any
"basin-scale" mass change statement must therefore state the region size
*relative to the resolution*, not only in square kilometres.

*Worked example 2.* Estimate the cap-mean bias scale. The band-limited field is
the truth convolved with a kernel of width $\sim\lambda_{1/2}/2$, so a disc of
radius $a$ has its cap mean reduced by roughly the fraction of the bump that
falls outside the smoothing kernel: for $a \ll \lambda_{1/2}$ almost all of it,
for $a \gg \lambda_{1/2}$ almost none. The measured $-34\%$ at
$a/\lambda_{1/2} = 300/500 = 0.6$ and $+1\%$ at $2.4$ are consistent with that
picture and make the rule of thumb quantitative: **$a \gtrsim 2\lambda_{1/2}$
for a few-per-cent regional accuracy.**

## 4. Leakage, defined so that it can be reported

**Leakage is the spurious mass appearing in a region where the truth is
different.** It has two sources that must be distinguished:

1. **Truncation leakage** — the band limit spreads signal outward. Measured: the
   annulus $400$–$700\ \mathrm{km}$ from the disc centre holds $+2.56\ \mathrm{cm}$
   of excess EWH over the $2.00\ \mathrm{cm}$ background with no filter.
2. **Filter leakage** — the chosen averaging kernel spreads signal further, and
   also mixes neighbouring regions.

With the Gaussian kernel

$$W_{l} = \exp\left(-\frac{l(l+1)\sigma^{2}}{2R^{2}}\right),$$

*Worked example 3.* Evaluate $W_{l}$ for $\sigma = 400\ \mathrm{km}$:

$$W_{2} = \exp\left(-\frac{2\cdot3\,(4\times10^{5})^{2}}{2(6.371\times10^{6})^{2}}
\right) = 0.988,\quad
W_{10} = 0.805,\quad
W_{20} = 0.437,\quad
W_{40} = 0.0395 .$$

So a $400\ \mathrm{km}$ filter keeps degrees up to about 10 nearly intact,
halves degree 20, and suppresses degree 40 to $4\%$. That is the quantitative
meaning of "we report at $400\ \mathrm{km}$ resolution": the model space is not
truncated at a degree but *weighted*, and the weights are the resolution.

The demonstration's sweep at those kernel widths, for the $300\ \mathrm{km}$
disc:

| $\sigma$ (km) | cap mean inside (cm) | annulus 400–700 km (cm) | annulus 1000–1500 km (cm) | far-field noise rms (mm) |
|---|---|---|---|---|
| 0 | 21.734 | 4.560 | 3.555 | 294.97 |
| 100 | 20.070 | 4.816 | 3.383 | 257.56 |
| 200 | 16.160 | 5.312 | 3.036 | 177.19 |
| 400 | 8.965 | 5.501 | 2.779 | 64.35 |
| 800 | 4.474 | 4.092 | 3.059 | 16.40 |
| 1600 | 2.858 | 2.817 | 2.659 | 4.45 |

Read the columns together, not separately:

- **Bias grows monotonically** with $\sigma$: the cap mean falls from $21.7\ \mathrm{cm}$
  to $2.9\ \mathrm{cm}$ against a truth of $32.0\ \mathrm{cm}$.
- **Leakage is worst at intermediate widths**: the $400$–$700\ \mathrm{km}$
  annulus peaks at $5.50\ \mathrm{cm}$ for $\sigma = 400\ \mathrm{km}$, *worse*
  than the unfiltered case, because the filter mixes the disc into the annulus
  while the filtered field is no longer able to represent the sharp inner edge.
- **Noise collapses**: $295\ \mathrm{mm}$ to $4.5\ \mathrm{mm}$, a factor $66$.

There is no $\sigma$ that minimises all three. The choice is a *science*
decision, and the only defensible way to make it is to state which column the
question cares about.

## 5. Adjacent sources: the assumption you cannot avoid

Two identical discs $1443\ \mathrm{km}$ apart, each $300\ \mathrm{km}$ in radius,
with a $2\ \mathrm{cm}$ background. Recover disc 1 alone and read the apparent
EWH in disc 2's cap (truth there: the background):

| $\sigma$ (km) | apparent EWH in neighbour cap (cm) | excess over background |
|---|---|---|
| 0 | 2.710 | $+0.710$ |
| 100 | 2.600 | $+0.600$ |
| 200 | 2.361 | $+0.361$ |
| 400 | 2.121 | $+0.121$ |
| 800 | 2.503 | $+0.503$ |
| 1600 | 2.402 | $+0.402$ |

The contamination is positive everywhere and has a **minimum at
$\sigma \approx 400\ \mathrm{km}$**, the width matched to the source radius. Too
narrow a filter leaves truncation ringing that spreads mass outward
($+0.71\ \mathrm{cm}$); too wide a filter smooths the disc into its neighbour
($+0.40\ \mathrm{cm}$). So "matched filtering" is not a refinement but the
difference between a $0.12\ \mathrm{cm}$ and a $0.71\ \mathrm{cm}$ artefact.

The control region $60^\circ$ away recovers $1.969\ \mathrm{cm}$ and
$1.979\ \mathrm{cm}$ at $\sigma = 400$ and $1600\ \mathrm{km}$ against a truth of
$2.000\ \mathrm{cm}$: at that distance the same analysis is accurate to a few
per cent. **The distance to the nearest other mass change is therefore part of
the error budget**, and a control region is the cheapest available check.

Linear systems make one more thing visible: the demonstration verifies that the
pair's coefficients equal the sum of the single-disc coefficients to
$1.7\times10^{-9}$ (the working precision). The non-uniqueness is not in the
forward model, which is linear and exact, but entirely in the *inverse* step.

## 6. Assumptions and regime of validity

1. **Surface mass, elastic load response.** The whole conversion assumes the mass
   change is a thin layer at the surface and the Earth responds elastically with
   the assumed $k_l$. Deep mass changes (mantle, core) are misattributed to the
   surface.
2. **The truth is discretised.** Grid quantisation of the source area changed the
   global mean by $25\%$ in the demonstration; a finer grid is not automatically
   a better truth if the physics is coarser than the grid.
3. **Truncation degree is a choice.** Everything regional depends on $L$; the
   report must state it.
4. **The filter is a choice, and it is the resolution.** Reporting at
   $\sigma = 400\ \mathrm{km}$ is a claim about the smallest scale the answer can
   support.
5. **Noise is independent per coefficient.** Correlated errors (which real
   solutions have, especially at low degree) make the far-field noise larger than
   the demonstration's and the crossover a direction-dependent statement.
6. **Backgrounds are correct.** Static field, tides, atmosphere, ocean and
   solid-Earth response are removed before anything is called a mass change; an
   error in any of them appears as a trend.

## 7. Python demonstration

`code/mascons_and_leakage_demo.py` builds the whole chain and prints, with units:

1. **A synthetic truth**: a $2.0\ \mathrm{cm}$ uniform layer with two $30\
   \mathrm{cm}$, $300\ \mathrm{km}$ discs $1443\ \mathrm{km}$ apart, plus an
   empty control region.
2. **The forward model**, verified against exact mass balance to
   $1.196\times10^{-16}$, and the discretisation warning ($0.2509\ \mathrm{mm}$
   measured against $0.3326\ \mathrm{mm}$ analytic for the disc contribution).
3. **The observation operator**: truncation at $L = 40$ and independent
   coefficient noise of $1.0\times10^{-11}$.
4. **The round trip** and the region-size bias table: $-34.2\%$ at a $300\
   \mathrm{km}$ cap, $+1.0\%$ at $1200\ \mathrm{km}$.
5. **The filter sweep**: bias, leakage into two annuli, and far-field noise for
   $\sigma = 0$ to $1600\ \mathrm{km}$.
6. **Leakage between neighbours** and the linearity check, with a control
   region.
7. **The honest report**: measured, converted, chosen, inferred.

Print-only, fixed seed, no network, exits 0.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/04-mascons-and-leakage-exercises.md`](./exercises/04-mascons-and-leakage-exercises.md)
and
[`exercises/04-mascons-and-leakage-solutions.md`](./exercises/04-mascons-and-leakage-solutions.md).

- **★** Compute the mass of a $25\ \mathrm{cm}$ EWH disc of radius
  $200\ \mathrm{km}$ and its contribution to the global mean.
- **★** Evaluate the Gaussian kernel $W_{l}$ at $l = 5, 15, 30$ for
  $\sigma = 250\ \mathrm{km}$.
- **★★** Explain, with the demonstration's numbers, why a $300\ \mathrm{km}$ cap
  is biased by $-34\%$ while a $1200\ \mathrm{km}$ cap is accurate to $1\%$.
- **★★★** Design a procedure that would let you state a basin mass trend with a
  defensible error bar, given a coefficient set with covariance. Specify the
  region size criterion, the filter choice, the leakage estimate and the control
  region.

## 9. Mastery checkpoint

Do this without notes:

> A synthetic solution is complete to degree 40 with $1.0\times10^{-11}$ noise
> per coefficient. A $300\ \mathrm{km}$-radius basin loses mass at
> $30\ \mathrm{cm}$ EWH per year against a $2\ \mathrm{cm}$ background, and
> a second basin sits $1443\ \mathrm{km}$ away. **(a)** Compute the basin's
> mass change per year. **(b)** State the resolution half-wavelength and decide
> whether a $300\ \mathrm{km}$ cap can be reported. **(c)** Evaluate the
> Gaussian kernel at $l = 2, 10, 20, 40$ for $\sigma = 400\ \mathrm{km}$ and
> say what resolution that is. **(d)** Which filter width minimises the leakage
> into the neighbour, and how large is that leakage? **(e)** Write the four-part
> report (measured, converted, chosen, inferred) for this basin.

*Answers.* **(a)** $m = \rho_w t\pi r^{2}
= 1000(0.30)\pi(3\times10^{5})^{2} = 8.48\times10^{13}\
\mathrm{kg\,yr^{-1}}$, against the demonstration's measured
$8.4823\times10^{13}$. **(b)** $\pi R/40 = 500\ \mathrm{km}$, so a
$300\ \mathrm{km}$ cap is below the resolution: the demonstration measures a
$-34.2\%$ bias there ($21.73\ \mathrm{cm}$ recovered against
$32.00\ \mathrm{cm}$). Report a cap of at least $\sim2\lambda_{1/2}$, or
raise $L$. **(c)** $W_l = \exp(-l(l+1)\sigma^{2}/(2R^{2}))$ gives
$W_2 = 0.988$, $W_{10} = 0.805$, $W_{20} = 0.437$, $W_{40} = 0.0395$: a
$400\ \mathrm{km}$ filter passes degrees up to about 10 and suppresses degree
40 to $4\%$. **(d)** $\sigma \approx 400\ \mathrm{km}$, matched to the
source radius, giving $+0.121\ \mathrm{cm}$; a narrower filter
($\sigma = 0$) gives $+0.710\ \mathrm{cm}$ and a wider one
($\sigma = 1600\ \mathrm{km}$) $+0.402\ \mathrm{cm}$. **(e)**
*Measured*: coefficients for $l = 2$–$40$ with their covariance. *Converted*:
water equivalent, using the stated load Love numbers. *Chosen*: the truncation
degree, the filter width, the basin boundary and the control region. *Inferred*:
surface mass, elastic response, and correct removal of the static field, tides,
atmosphere, ocean and solid-Earth background.
## 10. Common pitfalls

1. **Reporting a regional number without the filter width.** The two are the same
   statement.
2. **Choosing the region to make the answer large.** A cap smaller than the
   resolution is guaranteed to be biased, and by a known sign.
3. **Treating leakage as a caveat instead of a number.** It can be computed, so
   it should be reported.
4. **Comparing a harmonic solution with a mascon solution without their
   kernels.** They blur differently, by construction.
5. **Assuming a control region is unnecessary.** It is the only empirical check
   of leakage available.
6. **Attributing the whole signal to the target process.** Surface mass, GIA,
   atmosphere and ocean contribute to the same coefficients.

## 11. Real-world applications

- **Groundwater and ice.** Regional trends are the headline product of
  time-variable gravity and are exactly the quantities most sensitive to leakage
  (see [05](05-grace-applications.md)).
- **Sea level.** Basin-scale ocean mass change is estimated from the same
  coefficients; the region size criterion of Section 3 applies unchanged.
- **Solid Earth.** GIA and earthquake signals are extracted from the same data
  with different assumptions about the load response.
- **Hydrological model evaluation.** Comparing a model with a filtered
  observation requires applying the same filter to the model — the "filtering
  both sides" rule, without which the comparison is meaningless.

## 12. Further reading

- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the layer formula and
  its normalisation.
- **Torge, W. & Müller, J., *Geodesy*** — regional gravity products and their
  conventions.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — filtering and
  smoothing in the harmonic domain.
- **Kaula, W. M., *Theory of Satellite Geodesy*** — degree variance and the a
  priori spectrum that acts as the regularisation.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [03 Spherical Harmonic Solutions and Coefficient Interpretation](03-spherical-harmonic-solutions.md) —
  the crossover degree beyond which regularisation, not data, writes the answer.
- [05 Applications: Groundwater Depletion, Ice Loss, Sea Level](05-grace-applications.md) —
  the trends these regional numbers become, and their error budget.
- [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../03-gravity-anomalies-and-modelling/04-inversion-gravity.md) —
  the same mathematics for ground and airborne data.
- [18-inverse-problems](../../18-inverse-problems/README.md) — resolution
  operators, regularisation and the general theory of leakage.

## 14. Related modules

- [Satellite Gravimetry](./README.md) — this module's index.
- [07-03 Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  the same inversion and non-uniqueness for ground and airborne data.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — resolution
  operators, regularisation and leakage in general.
- [26-reference-library](../../26-reference-library/README.md) — symbols, units
  and constants used without re-derivation.

## 15. Self-assessment checklist

- [ ] I can state what a mascon solution assumes that a harmonic solution does not.
- [ ] I can verify the layer formula against uniform-layer mass balance.
- [ ] I can predict the sign and rough size of a region-size bias.
- [ ] I can evaluate $W_{l}$ for a stated filter and read it as a resolution.
- [ ] I can explain why leakage peaks at an intermediate filter width.
- [ ] I can find the filter width matched to a source size.
- [ ] I can write a regional mass-change statement that labels measured, converted, chosen and inferred parts.
