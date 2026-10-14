---
id: 13-03-04
title: "Basin Formation and Subsidence Modelling"
level: doctoral
prereqs: ["13-03-02", "13-01-03", "04-03-04"]
tags: [geodynamics, tectonophysics, basins, subsidence, backstripping, flexure, compaction]
---

# Basin Formation and Subsidence Modelling

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Airy backstripping equation
   $Y = d_w + \sum_i(\rho_m-\rho_i)t_i/(\rho_m-\rho_w)$ from a mass balance, and
   **explain** what it removes from a measured stratigraphy.
2. **Quantify** how much the answer changes when the compaction model changes,
   and **state** the compaction model as part of the result.
3. **Fit** the McKenzie post-rift curve to a backstripped record, **report** the
   $( \beta, \tau )$ pair with its trade-off, and **recognise** when the fit is
   constrained by the model rather than by the data.
4. **Derive** the flexural parameter $\alpha = (4D/\Delta\rho g)^{1/4}$ and the
   line-load deflection profile of an elastic plate, and **verify** both against
   the governing differential equation and a load balance.
5. **Distinguish** an extensional from a foreland subsidence history from the
   shape in time and the migration of the depocentre, not from amplitude alone.
6. **State** the regime of validity of the linear elastic plate and the
   assumptions that break in a deep basin.

## Prerequisites

- [13-03-02 Rifting, Break-Up and Passive Margin Formation](02-rift-and-breakup.md) —
  the McKenzie model fitted here, and the isostasy it is built on.
- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the elastic plate and what $T_e$ means.
- [04-03-04 Sedimentary Basins](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/04-sedimentary-basins.md) —
  the geological classification this lesson attaches numbers to.

All models and data in this module are **SYNTHETIC**. The stratigraphy, porosity
law and loads below are chosen teaching values, and the "$80\ \mathrm{Ma}$"
break-up is a model input, not a geological date. The exact constants are
$g = 9.81\ \mathrm{m\,s^{-2}}$ and, for the elastic plate, the stated textbook
values $E = 70\ \mathrm{GPa}$ and $\nu = 0.25$.

## 1. Backstripping: what it removes and what it does not

A well records sediment thicknesses and ages. What a geodynamicist wants is the
**tectonic subsidence**: the water depth the basin would have had if the
sediment were not there. The conversion is a one-line statement of isostasy.

Consider the present-day column: water of depth $d_w$, then beds
$i = 1\dots n$ (top to bottom) of thickness $t_i$ and density $\rho_i$, then
mantle. Remove the top $k$ beds and replace them with water to a depth $Y$, and
require the mass per unit area above a fixed compensation depth to be unchanged.
The mantle's upper surface moves by $\sum_{i\le k}t_i + d_w - Y$, so

$$
\rho_w Y + \sum_{i>k}\rho_i t_i
+ \rho_m\left[\sum_{i\le k}t_i + d_w - Y\right]
= \rho_w d_w + \sum_i \rho_i t_i + \rho_m[\text{same mantle base}],
$$

which rearranges to the **backstripping equation**

$$
\boxed{\;Y = d_w + \sum_{i\le k}
\frac{\rho_m - \rho_i}{\rho_m - \rho_w}\,t_i \;}
$$

Each stripped bed contributes in proportion to its density deficit relative to
mantle, scaled by the density contrast that drives the compensation. Two
immediate checks: if $\rho_i = \rho_w$ the bed contributes exactly its own
thickness (no load), and if $\rho_i = \rho_m$ it contributes nothing (removing
dense material changes nothing).

**What it removes:** the sediment load, so that the residual subsidence can be
compared with a tectonic model. **What it does not remove:** the water load
itself, which is what makes the result a *water-loaded* subsidence, the same
quantity that the stretching models predict. It also does not remove
compaction, and that is the subject of the next section.

### 1.1 The SYNTHETIC basin

The demonstration builds a basin whose backstripped curve *is* the McKenzie
curve for $\beta = 2$, $\tau = 50.17\ \mathrm{Myr}$ with a constant fill density
of $2200\ \mathrm{kg\,m^{-3}}$. Break-up is at $80\ \mathrm{Ma}$ and the fill
records post-rift subsidence only, so the base of the fill is the break-up
unconformity. Beds are listed oldest first, with present densities computed from
the porosity law $\phi(z) = 0.55\,e^{-z/2.5\,\mathrm{km}}$ and a grain density
of $2720\ \mathrm{kg\,m^{-3}}$:

| bed | base age (Ma) | top (km) | bottom (km) | present bulk density ($\mathrm{kg\,m^{-3}}$) |
|---|---|---|---|---|
| 1 | 80 | 1.616 | 2.750 | 2328 |
| 2 | 60 | 0.854 | 1.616 | 2151 |
| 3 | 40 | 0.343 | 0.854 | 1987 |
| 4 | 20 | 0.000 | 0.343 | 1851 |

Total sediment thickness $2.750\ \mathrm{km}$. The three boundaries at $1.616$,
$0.854$ and $0.343\ \mathrm{km}$ are not invented: they follow from
$X(t) = [S(t)-S(0)](\rho_m-\rho_w)/(\rho_m-\rho_{\text{fill}})$ evaluated at
post-rift times $20, 40, 60, 80\ \mathrm{Myr}$.

## 2. The compaction model is part of the answer

Three backstrips of the *same* geometry, differing only in how each stripped bed
is represented:

- **(A)** constant density $2200\ \mathrm{kg\,m^{-3}}$, present thicknesses;
- **(B)** density from $\phi(z)$ at the present depth, present thicknesses;
- **(C)** density and thickness evaluated at the depositional depth
  (decompacted), an estimate that places each stripped bed at the paleo-surface
  and therefore ignores the partial overburden it had.

| base age (Ma) | A (km) | B (km) | C (km) | target (km) |
|---|---|---|---|---|
| 80 | 0.557 | 0.494 | 0.842 | 0.557 |
| 60 | 0.932 | 0.885 | 1.402 | 0.932 |
| 40 | 1.183 | 1.183 | 1.759 | 1.183 |
| 20 | 1.351 | 1.404 | 1.979 | 1.351 |

Curve A reproduces the target to $0.000\ \mathrm{m}$ — it was built that way, and
that is the check on the implementation. Curve B, using the
porosity-derived density, differs by up to $63\ \mathrm{m}$. Curve C differs by
up to $628\ \mathrm{m}$, **46.5% of the total subsidence**.

All three use identical data. The spread is a model choice, and it is larger than
most of the differences between competing tectonic models. Any backstripped
curve quoted without its compaction model is therefore not reproducible. A
further subtlety: decompaction is a fixed-point problem, because a bed's density
depends on its depth and its depth depends on its thickness. The demonstration
iterates 20 times per bed, which converges to better than a metre here.

## 3. Fitting the McKenzie curve: what the data actually constrain

Fit each backstrip with
$S(t) = S(\infty) - [S(\infty)-S(0)]e^{-t/\tau}$ on a
$57\times201$ grid of $(\beta,\tau)$:

| backstrip | best $\beta$ | best $\tau$ (Myr) | rms (m) | acceptable $\beta$ | acceptable $\tau$ |
|---|---|---|---|---|---|
| A | 2.000 | 50.0 | 1.9 | 2.00–2.00 | 50–50 |
| B | 2.700 | 76.0 | 3.8 | 2.65–2.80 | 74–78 |
| C | 3.350 | 46.5 | 5.9 | 3.25–3.40 | 45–47 |

The true values are $\beta = 2$, $\tau = 50.17\ \mathrm{Myr}$. Curve A recovers
them to the grid resolution *because A is the model the basin was built from*.
B and C, which differ only in the compaction model, return $\beta = 2.7$ and
$3.35$ — errors of $35\%$ and $68\%$ — and their rms residuals are $3.8$ and
$5.9\ \mathrm{m}$, i.e. the fits are **excellent**. A large error in $\beta$ is
therefore invisible in the misfit whenever the forward model and the inversion
share the same wrong assumption.

This is the working definition of a systematic error, and it is worth stating
plainly: **the residual tells you whether the model fits the data, never whether
the model is right.** The only defences are independent constraints (crustal
thickness from seismology, heat flow for $\tau$, syn-rift geometry for the
timing) and the honest reporting of the compaction model.

### 3.1 The $(\beta,\tau)$ trade-off

Within a single backstrip, $\beta$ and $\tau$ are correlated: raising $\beta$
increases the equilibrium subsidence and can be compensated by lengthening
$\tau$, which delays it. Curve C's acceptable region is
$\beta = 3.25$–$3.40$ with $\tau = 45$–$47\ \mathrm{Myr}$; the two parameters
move together. Quoting $\beta = 3.35$ without $\tau$ would overstate the
constraint, because a different $\tau$ would have given a different $\beta$ at
the same misfit.

## 4. Foreland flexure: the other basin

Not every basin is a stretched one. A thrust belt loads the lithosphere from the
side, and the deflection is the response of an elastic plate:

$$
D\frac{\mathrm d^{4}w}{\mathrm dx^{4}} + \Delta\rho\,g\,w = q(x),
\qquad
D = \frac{E\,T_e^{3}}{12(1-\nu^{2})},
\qquad
\Delta\rho = \rho_m - \rho_w .
$$

For a line load $V_0$ at $x=0$ on a semi-infinite plate, the solution that decays
away from the load is

$$
w(x) = \frac{V_0\alpha^{3}}{8D}\,e^{-x/\alpha}
\left[\cos\frac{x}{\alpha} + \sin\frac{x}{\alpha}\right],
\qquad
\boxed{\;\alpha = \left(\frac{4D}{\Delta\rho\,g}\right)^{1/4}\;}
$$

$\alpha$ is the **flexural parameter**: the distance over which the plate
responds. Two length scales follow immediately, and the demonstration measures
both:

$$
w = 0 \ \text{at}\ x = \frac{3\pi\alpha}{4}, \qquad
\text{forebulge minimum at}\ x = \pi\alpha .
$$

### 4.1 Rigidity numbers

| $T_e$ (km) | $D$ ($\mathrm{N\,m}$) | $\alpha$ (km) | forebulge at $\pi\alpha$ (km) |
|---|---|---|---|
| 5 | $7.78\times10^{20}$ | 19.3 | 60.5 |
| 10 | $6.22\times10^{21}$ | 32.4 | 101.8 |
| 20 | $4.98\times10^{22}$ | 54.5 | 171.2 |
| 40 | $3.98\times10^{23}$ | 91.7 | 288.0 |

The basin width therefore grows roughly as $T_e^{3/4}$ — a strong, measurable
dependence. For the SYNTHETIC load $V_0 = 10^{12}\ \mathrm{N\,m^{-1}}$ and
$T_e = 20\ \mathrm{km}$, $w(0) = 0.4066\ \mathrm{km}$, the profile crosses zero
at $128.4\ \mathrm{km}$ (closed form $3\pi\alpha/4 = 128.4\ \mathrm{km}$), and
the forebulge bottoms at $171.3\ \mathrm{km}$ (closed form $\pi\alpha =
171.2\ \mathrm{km}$) with an amplitude of $0.0176\ \mathrm{km}$ of uplift.

### 4.2 Two independent verifications

1. **Differential equation.** Substituting the profile into
   $D w'''' + \Delta\rho g w$ gives a maximum absolute residual of
   $333\ \mathrm{Pa}$ over the interior, against a characteristic stress scale
   $\Delta\rho g\,|w(0)| = 9.17\times10^{6}\ \mathrm{Pa}$. The relative residual
   is $3.6\times10^{-5}$, i.e. finite-difference truncation, not a modelling
   error.
2. **Load balance.** The buoyancy of the deflected region must carry the load:
   $2\int_0^\infty \Delta\rho g\,w\,\mathrm dx = V_0$. The demonstration measures
   $1.0120\times10^{12}$ against $V_0 = 1.0\times10^{12}\ \mathrm{N\,m^{-1}}$,
   i.e. $1.2\%$ high, the excess coming from the finite upper limit of the
   integral.

The second check is the physically meaningful one: it says that flexure does not
create a hole locally, it redistributes — a filled basin outboard of the load
and a forebulge beyond it. Any deflection model that fails this integral is
wrong by construction.

## 5. Telling the two basins apart

| time since start (Myr) | 0 | 10 | 25 | 50 | 80 | 120 |
|---|---|---|---|---|---|---|
| extensional $S$ (km), $\beta=2$, $\tau=50.2$ | 3.118 | 3.424 | 3.783 | 4.187 | 4.469 | 4.658 |
| rate ($\mathrm{mm\,yr^{-1}}$) | — | 30.6 | 23.9 | 16.2 | 9.4 | 4.7 |

The extensional curve is fastest at once and decays exponentially. A foreland
basin, in contrast, grows while the load advances:

| time (Myr) | loaded strip (km) | line load ($10^{12}\ \mathrm{N\,m^{-1}}$) | deflection (km) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 5 | 25 | 2.5 | 1.016 |
| 20 | 100 | 10 | 4.066 |
| 40 | 200 | 20 | 8.132 |

with a SYNTHETIC distributed load of $10^{8}\ \mathrm{Pa}$ over a strip
advancing at $5\ \mathrm{km\,Myr^{-1}}$ (so $V_0 = q\,l$).

The **shape in time** differs qualitatively: exponential decay versus growth
that tracks the load. Even more diagnostic is the **depocentre**: an extensional
basin subsides where it started, whereas a foreland basin's depocentre migrates
with the thrust front. Note that the $8.1\ \mathrm{km}$ deflection in the last
row is outside the regime of validity of the linear plate equation (Section 6,
item 4) and is shown to make the arithmetic of the load scaling explicit, not as
a prediction.

## 6. Assumptions and regime of validity

1. **Airy (local) compensation in the backstripping equation.** The derivation
   assumes the compensation depth is deep enough that each stripped bed's mass
   is fully compensated locally. For a basin narrower than the flexural
   wavelength, part of the load is carried regionally and the equation
   overestimates $Y$. A flexural backstripping scheme is then required.
2. **A stated porosity–depth law.** $\phi(z) = 0.55e^{-z/2.5\,\mathrm{km}}$ is a
   chosen law with two parameters; real lithologies differ, and the resulting
   $\beta$ error measured above is $\sim 35$–$68\%$.
3. **Lithology-independent grain density.** A sand/shale/carbonate mix has a
   range of grain densities; assuming one value biases the deeper beds most.
4. **Linear elastic plate, small deflection.** The profile assumes
   $w \ll \alpha$. Our $0.41\ \mathrm{km}$ deflection against
   $\alpha = 54.5\ \mathrm{km}$ satisfies it ($w/\alpha = 0.0075$); a
   $8.1\ \mathrm{km}$ deflection against the same $\alpha$ does not, and would
   need a finite-amplitude or non-linear treatment. Infill also changes the load
   as the basin fills, which this static solution ignores.
5. **A constant $T_e$.** $T_e$ depends on temperature and therefore on the
   basin's own thermal history; it changes as the basin subsides.
6. **No erosion, no sea-level change, no sediment supply limitation.** The
   extensional curve is water-loaded; a supply-limited basin is underfilled and
   the water depth is then an extra unknown.
7. **One stretching event.** Two-phase and depth-dependent stretching produce
   the same first-order curve with different parameters
   ([13-03-02](02-rift-and-breakup.md) §5).

## 7. Worked example — is this basin extensional or foreland?

A SYNTHETIC basin has $2.75\ \mathrm{km}$ of fill spanning $80\ \mathrm{Myr}$,
with the decompacted backstrip rising to $1.98\ \mathrm{km}$ (curve C).

1. **Extensional test.** Fitting curve C gives $\beta = 3.35$,
   $\tau = 46.5\ \mathrm{Myr}$ with a $5.9\ \mathrm{m}$ residual — an excellent
   fit. But $\tau = 46.5\ \mathrm{Myr}$ should be compared with
   $a^{2}/(\pi^{2}\kappa) = 50.17\ \mathrm{Myr}$, which it does **not** match,
   and the implied crustal thinning (35/3.35 = $10.4\ \mathrm{km}$ of crust)
   would have to be confirmed independently.
2. **Foreland test.** A $4\ \mathrm{km}$ deflection requires
   $V_0 \approx 9.8\times10^{12}\ \mathrm{N\,m^{-1}}$ at $T_e = 20\ \mathrm{km}$,
   i.e. a thrust belt loading the plate with roughly $10^{13}\
   \mathrm{N\,m^{-1}}$ — a large but not impossible load, corresponding to a
   $\sim 100\ \mathrm{km}$ wide strip of $10^{8}\ \mathrm{Pa}$.
3. **Discriminator.** The extensional model predicts a post-rift subsidence
   rate falling monotonically as $e^{-t/\tau}$, with no lateral migration; the
   foreland model predicts a depocentre that migrates in the direction of
   thrust advance and a subsidence rate that follows the load. Neither the
   total thickness nor the final depth separates them.

## 8. Python demonstration

`code/basin_geodynamics_demo.py` prints labelled results with units and exits 0.
It:

1. builds a synthetic basin from the McKenzie model with a known $\beta$ and
   $\tau$, so that the inversion has a true answer to recover;
2. backstrips the same geometry three ways — constant density, present-depth
   density, and decompacted — and measures the spread ($628\ \mathrm{m}$,
   $46.5\%$);
3. fits $(\beta,\tau)$ to each, showing that the wrong compaction model returns
   $\beta = 2.70$ and $3.35$ with residuals of a few metres;
4. computes $D$, $\alpha$ and the forebulge position for four elastic
   thicknesses, and validates the profile against the differential equation
   ($3.6\times10^{-5}$ relative residual) and against the load integral
   ($1.2\%$);
5. puts an extensional and a foreland subsidence history side by side and
   states the shape difference.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC margin has a present water depth of $0.2\ \mathrm{km}$ and three
> beds: $1.0\ \mathrm{km}$ of $2200$, $1.2\ \mathrm{km}$ of $2400$ and
> $1.5\ \mathrm{km}$ of $2550\ \mathrm{kg\,m^{-3}}$, from top to bottom.
> **(a)** Backstrip the two upper beds with
> $\rho_m = 3330$, $\rho_w = 1030\ \mathrm{kg\,m^{-3}}$ and give the tectonic
> subsidence at the top of the lowest bed. **(b)** State why the result depends
> on the compaction model and give the direction of the bias if compaction is
> ignored. **(c)** The backstripped curve is fitted by the McKenzie model and
> returns $\beta = 2.4$, $\tau = 40\ \mathrm{Myr}$. State two independent checks
> you would apply and what each would test. **(d)** The basin's width is
> $60\ \mathrm{km}$ and its asymmetry is pronounced. Which of the two basin
> types of this lesson is more likely, and what flexural parameter would you
> expect?

## Common pitfalls

1. **Quoting a backstripped curve without its compaction model.** The spread
   between defensible models is $628\ \mathrm{m}$ here — larger than most
   tectonic signals.
2. **Believing a small residual.** Curves B and C fit to $4$–$6\ \mathrm{m}$ and
   return $\beta$ in error by $35$–$68\%$.
3. **Reporting $\beta$ without $\tau$.** They trade off; the acceptable region
   is a ridge, not a point.
4. **Applying the local backstripping equation to a narrow basin.** Regional
   flexural support means part of the load is not locally compensated.
5. **Extrapolating the plate equation.** The linear solution is invalid when
   $w$ becomes comparable to $\alpha$ or to the plate thickness; the
   demonstration's $8.1\ \mathrm{km}$ row is arithmetic, not a prediction.
6. **Confusing a foreland and an extensional basin from amplitude.**
   $4$–$8\ \mathrm{km}$ is reachable both ways; the discriminator is the shape
   in time and the depocentre migration.
7. **Forgetting that the water-loaded convention presupposes a filled basin.**
   Supply-limited basins need the water depth as a free parameter.

## Related modules

- [13-03-02 Rifting, Break-Up and Passive Margin Formation](02-rift-and-breakup.md) —
  the model whose parameters are fitted here.
- [13-03-03 Orogenic Systems, Crustal Thickening and Collapse](03-orogenic-systems.md) —
  where the foreland load comes from.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md).
- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md).
- [11-03 Hydrocarbon Exploration](../../11-exploration-geophysics/03-hydrocarbon-exploration/README.md) —
  how these basins are imaged and what the images are used for.
- [18-03 Tikhonov Regularisation](../../18-inverse-problems/03-regularization/README.md) —
  the systematic treatment of the parameter trade-offs encountered here.
