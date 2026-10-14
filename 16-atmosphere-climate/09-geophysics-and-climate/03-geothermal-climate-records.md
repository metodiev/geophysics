---
id: 16-09-03
title: "Borehole Temperature Records of Past Climate"
level: doctoral
prereqs: ["02-05-04", "18-01-01", "16-09-02"]
tags: [atmosphere, climate, borehole, palaeoclimate, heat-conduction, inverse-problem, geothermal]
---

# Borehole Temperature Records of Past Climate

> **All models and data in this module are SYNTHETIC.** The thermal properties,
> the surface history, the profile noise and the depth range in
> `code/geothermal_climate_records_demo.py` are chosen teaching values. No real
> borehole, site, measurement or published reconstruction is used, and no
> published temperature change or inversion result is quoted.

A borehole is a thermometer that has been buried in a slow, forgiving filter. The
ground diffuses surface temperature downward, so a measurement of temperature
against depth is a record of the surface history — but passed through a
**low-pass filter** whose cut-off moves with depth and whose inverse is **ill
posed**. That combination makes borehole climatology a compact case study of the
whole curriculum's central difficulty: the forward physics is exact and
elementary, and the inverse problem is under-determined, so the deliverable is an
admitted set of histories rather than a curve.

This lesson derives the forward Green's function (an erfc), quantifies the filter
(e-folding depth against period), and then treats the inversion honestly. The
demonstration shows an unregularised least-squares reconstruction returning bin
values up to $31.8\ \mathrm{K}$ from a true history whose largest value is
$2.75\ \mathrm{K}$ — a correct fit to the data and a meaningless answer — and then
shows truncated-SVD regularisation recovering the history with a
$0.399\ \mathrm{K}$ rms bin error at an optimum truncation $k=3$. The
non-uniqueness is not a caveat appended at the end; it is a measured number
($6.0\ \mathrm{K}$ of amplification along the weakest retained direction, and a
machine-precision null direction on a finer grid).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Green's function for the heat equation with a surface step, and
   explain its $\mathrm{erfc}$ form.
2. **Compute** the penetration depth of a surface oscillation as a function of its
   period, and **state** which timescales a borehole profile can and cannot
   resolve.
3. **Build** the forward matrix for a piecewise-constant surface history and
   **compute** the synthetic profile it predicts.
4. **Demonstrate** that unregularised inversion of a noisy profile is unstable, and
   **explain** the instability in terms of the singular values.
5. **Regularise** by truncated SVD, **measure** the misfit/resolution trade-off,
   and **choose** a truncation against a stated noise level.
6. **Quantify** the non-uniqueness: the amplification of noise along the weakest
   retained direction and the existence of a null direction.
7. **State** the assumptions that separate a reconstructed ground-surface
   temperature from an air-temperature history.

## Prerequisites

- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the diffusion equation and its Green's functions.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) —
  ill-posedness, resolution and regularisation as general concepts.
- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  the surface process whose thermal signature the borehole records.

## 1. The forward problem

Heat conduction in the ground with no advection satisfies

$$\frac{\partial T}{\partial t} = \kappa\,\frac{\partial^{2} T}{\partial z^{2}},
\qquad z \ge 0,$$

with thermal diffusivity $\kappa = k/(\rho c)$. For a surface temperature that
steps by $\Delta T$ at time $t_0$ before the present and stays there, the
perturbation at depth $z$ today is

$$\boxed{\;\Delta T(z) = \Delta T\,\operatorname{erfc}\!\left(\frac{z}{2\sqrt{\kappa t_0}}\right).}$$

The demonstration uses $\kappa = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ (a
chosen rock value) and prints the response of a unit step:

| $z$ (m) | at 10 yr | at 100 yr | at 1000 yr |
|---|---|---|---|
| 10 | 0.6906 | 0.8998 | 0.9682 |
| 50 | 0.0466 | 0.5291 | 0.8422 |
| 100 | 0.0001 | 0.2081 | 0.6906 |
| 200 | 0.0000 | 0.0118 | 0.4260 |
| 300 | 0.0000 | 0.0002 | 0.2324 |

The structure of the table *is* the method. A ten-year-old change is invisible
below about $100\ \mathrm{m}$; a thousand-year-old change reaches the bottom of
the profile. Depth therefore maps to time, and the mapping is nonlinear — which is
why the time resolution of a borehole reconstruction degrades into the past.

## 2. Diffusion as a low-pass filter, quantified

For a surface oscillation of period $P$, the amplitude at depth $z$ decays as
$e^{-z/d}$ with the **e-folding depth**

$$d = \sqrt{\frac{\kappa P}{\pi}}.$$

With the demonstration's $\kappa$:

| period | $d$ (m) |
|---|---|
| 1 yr | 3.17 |
| 10 yr | 10.02 |
| 100 yr | 31.69 |
| 1000 yr | 100.23 |

Two consequences. The annual cycle is extinguished within a few metres, so a
borehole profile **cannot** record individual years or even individual decades;
and the century scale reaches tens of metres, so a profile a few hundred metres
deep can carry it. A borehole is thus a *century-scale* instrument, and the
filtering is not a defect — it is the reason the record is stable enough to be
useful.

## 3. A synthetic history and its profile

The demonstration defines a synthetic surface history over the last
$300\ \mathrm{yr}$ in six $50$-year bins, with a linear cooling into the past,

$$T_s(\text{age}) = -0.010\ \mathrm{K\,yr^{-1}} \times \text{age}
\quad\Longrightarrow\quad
\{-0.25, -0.75, -1.25, -1.75, -2.25, -2.75\}\ \mathrm{K}.$$

For a piecewise-constant history the forward operator is the difference of two
step responses per bin, so the predicted perturbation is a matrix product
$\mathbf{d} = \mathbf{G}\mathbf{h}$ with

$$G_{ji} = \operatorname{erfc}\!\left(\frac{z_j}{2\sqrt{\kappa t_{i}}}\right)
- \operatorname{erfc}\!\left(\frac{z_j}{2\sqrt{\kappa t_{i+1}}}\right),$$

where bin $i$ covers ages $[t_{i+1}, t_i]$. The demonstration measures at $30$
depths from $20$ to $310\ \mathrm{m}$ with a profile noise of
$0.02\ \mathrm{K}$, after removing a geothermal gradient of
$0.025\ \mathrm{K\,m^{-1}}$. That gradient contributes
$0.025 \times 310 = 7.75\ \mathrm{K}$ at the deepest point, against a total
perturbation of $0.60\ \mathrm{K}$: **the signal of interest is $8\%$ of the
background being removed**, so the gradient estimate is itself a source of error,
usually derived from the deepest part of the same profile.

## 4. Why unregularised inversion explodes

Solving $\mathbf{G}\mathbf{h} = \mathbf{d}$ by ordinary least squares on the noisy
profile gives bin values

$$\{-0.2,\ -0.2,\ -9.9,\ +25.2,\ -31.8,\ +7.7\}\ \mathrm{K}$$

against a truth whose largest magnitude is $2.75\ \mathrm{K}$. **The fit is
excellent and the answer is meaningless.** The reason is visible in the singular
values of the design matrix,

$$\sigma = (1.266,\ 0.493,\ 0.143,\ 0.028,\ 0.003,\ 0.000),$$

a condition number of $7.2\times10^{3}$. The solution component along a singular
direction is a data projection divided by $\sigma$; the last direction amplifies
the $0.02\ \mathrm{K}$ noise by $1/0.0033 \approx 300$ and the smallest by more.
Ill-posedness is not an abstraction — it is a division by a small number, and it
looks exactly like this.

## 5. Regularisation: the measured misfit/resolution trade-off

Truncating the SVD to $k$ components (retaining only the algebraically largest
singular values) regularises the problem. The demonstration measures both the
misfit and the error of the recovered history over the $k$ values:

| $k$ | rms misfit (K) | rms bin error (K) |
|---|---|---|
| 1 | 0.2881 | 1.653 |
| 2 | 0.0635 | 1.045 |
| 3 | **0.0238** | **0.399** |
| 4 | 0.0195 | 0.708 |
| 5 | 0.0191 | 2.845 |
| 6 | 0.0190 | 17.230 |

The optimal truncation is $k = 3$: its misfit ($0.0238\ \mathrm{K}$) has already
reached the noise level ($0.02\ \mathrm{K}$), and its bin error is the smallest of
any row. Beyond $k = 3$ the misfit improves by less than $0.005\ \mathrm{K}$ while
the bin error grows by more than an order of magnitude. **The resolution is
limited by the noise, not by the number of parameters**, and the truncation is a
choice that must be reported alongside the reconstruction.

The second table makes the same point about the time grid. Refining the history
into more bins does not create information: with $6$, $9$, $12$ and $18$ bins the
number of components above a singular-value threshold of $0.01$ is $4$, $4$, $5$,
$5$, and the bin error at a fixed truncation of $k=3$ *rises* with the number of
bins ($0.399, 0.569, 0.680, 0.820\ \mathrm{K}$) because the same information is
being spread over more unknowns. **A borehole profile has a finite information
content; the grid should be chosen to match it, not to look impressive.**

## 6. Non-uniqueness, measured two ways

**Practical.** The weakest direction retained at $k = 5$ has
$\sigma = 0.0033$, so a profile error of $0.02\ \mathrm{K}$ is amplified to about
$6.0\ \mathrm{K}$ along it. That direction, over the six bins, is proportional to
$\{+0.00, -0.17, +0.88, -1.00, -0.49, +0.84\}$ — an oscillating pattern of
surface temperature that changes the predicted profile by only
$0.0010\ \mathrm{K\,rms}$. This is why the $k = 5$ row of the table has
kelvin-scale errors: the extra component is measuring noise along a nearly
invisible direction.

**Exact.** On a finer $12$-bin grid the smallest singular value is
$8.9\times10^{-12}$: a genuine null direction. A $1\ \mathrm{K}$ change along it
alters the predicted profile by $2.6\times10^{-12}\ \mathrm{K\,rms}$, which no
measurement can detect. The pattern is again oscillatory, concentrated at the
older bins. **A null direction means the data cannot distinguish two histories at
all** along that direction, so an unqualified single-curve reconstruction is a
statement the data do not support; the honest product is a family of histories
consistent with the profile at the stated noise.

## 7. Assumptions and regime of validity

1. **Pure conduction.** Groundwater advection, latent heat from freezing and
   thawing, and convective exchange all move heat by other means and invalidate
   the diffusion Green's function.
2. **Constant, known diffusivity.** $\kappa$ varies with lithology, porosity,
   saturation and temperature; an error in $\kappa$ rescales the depth-to-time
   mapping directly.
3. **A horizontally uniform surface forcing.** Topography, vegetation, snow and
   land-use change produce lateral gradients and a site-specific offset between
   ground-surface and air temperature.
4. **A correct geothermal gradient removal.** The gradient dominates the signal,
   so its error propagates straight into the reconstruction.
5. **A one-dimensional half-space.** Layered conductivity and finite layer
   thickness require a layered forward model.
6. **A truncation chosen and reported.** The result is conditional on $k$; the
   misfit/resolution trade-off above makes that explicit.
7. **The estimate is of ground-surface temperature**, which equals air temperature
   only under assumptions about snow cover, vegetation and soil properties — the
   step that converts a borehole profile into a palaeoclimate record.

## 8. Python demonstration

[`code/geothermal_climate_records_demo.py`](code/geothermal_climate_records_demo.py)
builds the forward model and runs the inversions, printing labelled results in K
and metres. It:

1. computes the step-response $\mathrm{erfc}$ signature at depth;
2. tabulates e-folding depth against period;
3. builds a synthetic surface history and the noisy profile it predicts;
4. demonstrates the explosion of unregularised inversion and reports the
   condition number;
5. regularises by truncated SVD and measures the misfit/resolution trade-off and
   the effect of refining the time grid;
6. measures the practical amplification and the exact null direction;
7. states what is and is not determined.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's synthetic history is a linear cooling of
> $-0.010\ \mathrm{K\,yr^{-1}}$ over $300\ \mathrm{yr}$ in six $50$-year bins,
> sampled at $30$ depths with a profile noise of $0.02\ \mathrm{K}$ and
> $\kappa = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$.
>
> **(a)** Derive $\Delta T(z) = \Delta T\,\operatorname{erfc}(z/2\sqrt{\kappa t})$
> from the diffusion equation, stating the boundary conditions.
> **(b)** Compute the e-folding depth for a 100-year oscillation and state which
> timescales a $300\ \mathrm{m}$ profile can resolve.
> **(c)** The unregularised inversion returns a bin value of $+25.2\
> \mathrm{K}$ against a truth of $-1.75\ \mathrm{K}$. Explain why the fit is
> nevertheless good.
> **(d)** From the singular values
> $(1.266, 0.493, 0.143, 0.028, 0.003, 0.000)$, estimate the noise amplification
> for the fourth and fifth components and explain the optimum at $k = 3$.
> **(e)** Why does refining the history from $6$ to $18$ bins *increase* the
> recovered bin error at fixed $k$?
> **(f)** State the two assumptions that most strongly limit the conversion of a
> reconstructed ground-surface temperature into an air-temperature history.

## Common pitfalls

1. **Believing a low misfit means a good answer.** The unregularised fit was
   excellent and the answer was $31.8\ \mathrm{K}$ wrong per bin.
2. **Adding time bins to increase resolution.** The information content saturates
   at $4$–$5$ components.
3. **Reporting a single reconstructed curve.** Null directions make families of
   histories equally consistent.
4. **Forgetting that the gradient dominates.** $7.75\ \mathrm{K}$ of background
   against $0.60\ \mathrm{K}$ of signal.
5. **Treating ground-surface temperature as air temperature.** Snow, vegetation
   and soil properties intervene.
6. **Assuming conduction only.** Advection and latent heat are common in practice.
7. **Quoting a resolution without quoting the noise level that sets it.**

## Related modules

- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  the surface and mass changes whose thermal signature this records.
- [16-06-01 Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes](../06-palaeoclimate/01-paleoclimate-proxies.md) —
  the other proxies, with the same inversion logic.
- [12-03 Geotherms and Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md) —
  the geothermal gradient that must be removed here.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  the measurement practice for downhole temperature.
- [18-01 Inverse Problem Foundations](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  the general theory of the ill-posedness measured here.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  a different statistical tool applied to a different tail problem.

## Self-assessment checklist

- [ ] I can derive the erfc Green's function for a surface step.
- [ ] I can compute an e-folding depth and state the resolvable timescales.
- [ ] I can build the forward matrix for a piecewise-constant history.
- [ ] I can explain an unstable inversion from its singular values.
- [ ] I can choose a truncation against a stated noise level.
- [ ] I can quantify a null direction and state its consequence for reporting.
