---
id: 13-07-02
title: "River Profiles, Steepness Indices and Uplift Inference"
level: doctoral
prereqs: ["13-07-01", "18-01-03", "13-04-01"]
tags: [geodynamics, tectonophysics, geomorphology, stream-power, chi-transform, uplift]
---

# River Profiles, Steepness Indices and Uplift Inference

> **All models and data in this module are SYNTHETIC.** The drainage network is a
> chosen area–distance relation, not a mapped river, and the erosion parameters
> are teaching values. Every number is printed by
> [`code/river_profile_tectonics_demo.py`](code/river_profile_tectonics_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the steady stream-power profile $S = k_sA^{-\theta}$ from the
   incision law $\mathrm{d}z/\mathrm{d}t = U - KA^mS^n$, and identify
   $\theta = m/n$ and $k_s = (U/K)^{1/n}$.
2. **Perform** a $\chi$ transform and show that a steady profile is a straight
   line in the $(\chi,z)$ plane with slope $-k_s/A_0^{\theta}$.
3. **Measure** the concavity and steepness index from a synthetic profile and
   **verify** them against the inputs to round-off.
4. **Demonstrate** that only the ratio $U/K$ is measurable in steady state, and
   that the degeneracy is exact rather than a data limitation.
5. **Quantify** the bias from an assumed-wrong concavity $\theta$ and an
   assumed-wrong exponent $n$.
6. **Solve** the transient stream-power equation in the $\chi$ coordinate and
   **measure** the knickpoint propagation speed $c = KA_0^m$.
7. **Report** a steepness index with the reach, the concavity and the erodibility
   assumption that make it interpretable.

## Prerequisites

- [13-07-01 Erosion, Uplift and Thermochronology](01-erosion-and-uplift.md) —
  the independent constraint on an exhumation rate.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  an independent constraint on the uplift rate.
- [18-01-03 The Null Space](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the framework for the exact degeneracy derived here.

## 1. Why a river profile is a tectonic instrument

A river incises its bed, and the faster it incises the steeper its bed becomes
until incision balances the rock uplift beneath it. In that balance the channel
slope is a function of the *ratio* of uplift to erosional efficiency, and of the
drainage area through which water is delivered. The attractively simple
consequence is that a channel's slope can be read as a proxy for uplift. The less
attractive consequence, derived in Section 4, is that the uplift rate and the
erosional efficiency are *exactly* degenerate in the steady state: no profile,
however well surveyed, can separate them. Everything in this lesson is a
consequence of that fact and of what can be done about it.

## 2. The stream-power law and its steady state

The standard incision law is

$$\frac{\partial z}{\partial t} = U - K\,A^m\left|\frac{\partial z}{\partial x}\right|^n,
\qquad S \equiv -\frac{\partial z}{\partial x},$$

with $z$ the channel elevation, $x$ the distance downstream, $A$ the upstream
drainage area, $U$ the rock-uplift rate, $K$ the erodibility and $m$, $n$ the
exponents. Setting $\partial z/\partial t = 0$:

$$S = k_s\,A^{-\theta}, \qquad \theta = \frac{m}{n}, \qquad
k_s = \left(\frac{U}{K}\right)^{1/n}.$$

$\theta$ is a **ratio of exponents** and therefore relatively well constrained by
the shape of a profile; $k_s$ is a ratio of two poorly known quantities and is
not a measurement of either. The literature convention is to report the
normalised steepness index $k_{sn} = k_s A_{\text{ref}}^{\theta}$ with a stated
reference drainage area $A_{\text{ref}}$, because $k_s$ varies with the units and
the reference choice.

Measured on a synthetic network with $A$ from $1.0\times10^{5}$ to
$1.0\times10^{6}$ m² over 100 km, $m = 0.5$, $n = 1.0$,
$U = 0.1$ mm/yr and $K = 1.0\times10^{-5}$ (in the units implied by $m$ and $n$):

| $x$ (km) | $A$ (km²) | slope (m/km) | elevation (m) |
|---|---|---|---|
| 0 | 0.100 | 31.62 | 1815.9 |
| 25 | 0.185 | 23.23 | 1117.2 |
| 50 | 0.377 | 16.29 | 631.7 |
| 75 | 0.652 | 12.39 | 277.6 |
| 100 | 1.000 | 10.00 | 0.0 |

and a least-squares fit of $\ln S$ on $\ln A$ gives

$$S = 1.000000\times10^{1}\,A^{-0.500000},$$

so the measured $\theta = 0.500000$ against an input $m/n = 0.500000$, and the
measured $k_s = 10.0$ against $(U/K)^{1/n} = 10.0$. With these exponents $k_s$ has
the units of a length; when $n \ne 1$ the erodibility carries the time dimension
instead, and comparing $k_s$ values between studies demands that the units and
$n$ be stated.

## 3. The $\chi$ transform

Define, with a reference drainage area $A_0$,

$$\chi(x) = \int^x \left(\frac{A_0}{A(x')}\right)^{\theta}\mathrm{d}x' .$$

Then $\mathrm{d}z/\mathrm{d}\chi = (\mathrm{d}z/\mathrm{d}x)(\mathrm{d}x/\mathrm{d}\chi)
= -S\,(A/A_0)^{\theta} = -k_s A_0^{-\theta}$, a constant. **A steady profile is
therefore exactly a straight line in the $(\chi,z)$ plane**, and its slope,
multiplied by $A_0^{\theta}$, is $k_s$. Measured for the profile above with
$A_0 = A_{\max}$:

| quantity | measured | input |
|---|---|---|
| span of $\chi$ | 0 to 181.59 km | — |
| fitted slope $\mathrm{d}z/\mathrm{d}\chi$ | $-1.000000\times10^{-2}$ | — |
| $k_s$ recovered as $-\text{slope}\times A_0^{\theta}$ | $1.000000\times10^{1}$ | 10.0 |
| relative difference | $1.776\times10^{-15}$ | — |
| $R^2$ of the straight-line fit | 1.0000000000 | — |
| largest residual | $1.592\times10^{-12}$ m | — |

The exactness is expected — the profile was built from the steady state it is
tested against — and that is precisely why it is a *verification* of the
implementation and not evidence about a landscape. On real data the residual
curvature is the signal: it is what a differential uplift rate along the profile,
or a change in erodibility, produces.

The $\chi$ transform is also the most sensitive place for an assumption to enter.
Using a wrong $\theta$ destroys the linearity and biases the slope:

| $\theta_{\text{try}}$ | $k_s$ recovered | $R^2$ |
|---|---|---|
| 0.25 | 0.4251 | 0.993102 |
| 0.40 | 2.8393 | 0.998892 |
| 0.50 | 10.000 | 1.000000 |
| 0.60 | 35.027 | 0.998900 |
| 0.80 | 422.81 | 0.990304 |

Two things to notice. The $R^2$ degrades *gently*: a fit quality of 0.999 does
not pin $\theta$ to better than a few hundredths, and the recovered $k_s$ changes
by a factor of 42 across the range. And the transform is therefore not a way of
*measuring* $\theta$ robustly; it is a way of *assuming* $\theta$ and testing the
consequence.

## 4. Derivation and demonstration: the exact degeneracy

In steady state the profile depends on $U$ and $K$ only through $k_s =
(U/K)^{1/n}$; hence every pair with the same ratio gives the same profile.
Measured, over four orders of magnitude in both parameters with the ratio held at
$U/K = 10$:

| $U$ (mm/yr) | $K$ | $k_s$ | max difference from the reference profile (m) |
|---|---|---|---|
| 0.001 | $1.0\times10^{-7}$ | 10.0 | $0.000\times10^{0}$ |
| 0.010 | $1.0\times10^{-6}$ | 10.0 | $0.000\times10^{0}$ |
| 0.100 | $1.0\times10^{-5}$ | 10.0 | $0.000\times10^{0}$ |
| 1.000 | $1.0\times10^{-4}$ | 10.0 | $0.000\times10^{0}$ |
| 10.000 | $1.0\times10^{-3}$ | 10.0 | $0.000\times10^{0}$ |

The profiles are identical to round-off. This is not a limitation of data
quality, of survey density or of the fitting method: the forward model has an
exact one-dimensional null space spanned by the direction that changes $U$ and
$K$ together. **A steepness index is a measurement of $U/K$. A paper that
converts one into an uplift rate has assumed a $K$**, and the assumption is not
cosmetic: a factor of ten in $K$ is a factor of ten in $U$. The demonstration
quantifies the consequence for the profile — a $k_s$ of 100 instead of 10 puts the
profile 16342.9 m higher at the divide, which is not a subtle difference, but it
is invisible without an independent constraint because the *shape* is unchanged.

The way out is not a better profile. It is an independent measurement of one of
the two: a dated terrace or a cosmogenic erosion rate (an erosion rate), a
sediment budget (a flux), a thermochronological exhumation rate
([13-07-01](01-erosion-and-uplift.md)), or a geodetic rock-uplift rate
([13-04-01](../04-tectonophysics-deformation/01-crustal-deformation-gps.md)).

## 5. Worked example: the bias from a wrong exponent

*Problem.* A profile is inverted with $\theta_{\text{try}}$ in the $\chi$
transform and $n_{\text{try}}$ in the conversion $U = Kk_s^{n}$. How large is the
error?

1. **Wrong concavity.** With the true profile and $\theta_{\text{try}}$ varying
   about the true 0.5, the reported uplift is biased by (measured):

| $\theta_{\text{try}}$ | 0.40 | 0.45 | 0.50 | 0.55 | 0.60 |
|---|---|---|---|---|---|
| bias in inferred $U$ | $-71.61\%$ | $-46.68\%$ | $0.00\%$ | $+87.28\%$ | $+250.27\%$ |

2. **Wrong slope exponent.** With $k_s$ correct and $n_{\text{try}}$ varying
   about the true 1.0 (measured):

| $n_{\text{try}}$ | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 |
|---|---|---|---|---|---|
| inferred $U$ (mm/yr) | 0.0631 | 0.0794 | 0.1000 | 0.1259 | 0.1585 |
| bias | $-36.90\%$ | $-20.57\%$ | $0.00\%$ | $+25.89\%$ | $+58.49\%$ |

*Answer.* A 0.1 error in the concavity — well inside the range that different
studies use — moves the inferred uplift by a factor of three in one direction.
The exponent error scales the answer more gently but still by tens of per cent.
Neither is detectable from the profile alone, because the profile is what the fit
was made from: the error is a *model* error, not a noise error, and no amount of
surveying removes it. This is why the honest report of a steepness index names
$\theta$, $n$, the reference area $A_0$ and the reach it was measured over.

## 6. Transients: the knickpoint and what it costs

With $n = 1$ and $m = \theta$, substituting the $\chi$ coordinate turns the
incision law into

$$\frac{\partial z}{\partial t} - c\frac{\partial z}{\partial\chi} = U,
\qquad c = K A_0^{m},$$

a linear advection with speed $c$ in the $\chi$ coordinate, with information
travelling toward decreasing $\chi$ — upstream. Doubling $U$ at $t = 0$
therefore launches a knickpoint that migrates upstream at exactly $c$. Measured
for $K = 10^{-5}$, $A_0 = 10^{6}$ m²:

$$c = K A_0^{m} = 1.0000\times10^{-2}\ \mathrm{m/yr} = 10.0\ \mathrm{mm/yr}
= 10.0\ \mathrm{km/Myr},$$

so a 181.59 km $\chi$ profile needs 18.2 Myr for the knickpoint to reach the
divide. The demonstration integrates for 9 Myr — half that time — on a
non-uniform $\chi$ grid (spacing 250.2 to 790.5 m, $\Delta t = 0.0100$ Myr, 899
steps) and then applies the steady-state inference reach by reach from the divide
to the outlet:

| reach | 1 (divide) | 2 | 3 | 4 | 5 (outlet) |
|---|---|---|---|---|---|
| apparent $U$ (mm/yr) | 0.1000 | 0.1154 | 0.2000 | 0.2000 | 0.2000 |
| % of the true 0.20 mm/yr | 50.0 | 57.7 | 100.0 | 100.0 | 100.0 |

The reaches near the outlet have adjusted to the new rate; the reaches near the
divide still carry the old one. **A steepness index measured near the divide is
the old uplift rate, and the profile contains no internal evidence that it is
stale.** The evidence is the knickpoint: its position in $\chi$ moves upstream at
$c$, its position in $\chi$ is the product of the elapsed time and the speed, and
a set of profiles at different times therefore measures $c$ — and hence $K$
itself, which is the parameter the steady state cannot give. Knickpoint
migration is thus the one place where a channel profile does escape the exact
degeneracy of Section 4.

Two implementation cautions follow from building this. The $\chi$ grid is *not
uniform in $x$* (measured spacing from 250.2 to 790.5 m here): using a single
spacing biases the discrete steady state by the ratio of the spacings, because
the steady-state elevation increment per grid cell is $U\,\Delta\chi_i/c$ and a
wrong $\Delta\chi_i$ mis-scales it. And the upwind direction matters: information travels toward smaller
$\chi$, so the difference must be taken toward larger $\chi$; the reverse choice
is unstable.

## 7. Assumptions and regime of validity

1. **The incision law is the stream-power law.** Detachment-limited bedrock
   incision, a threshold, sediment cover and hillslope processes all modify it;
   the exponents $m$, $n$ are not universal and in reality depend on the process
   mix.
2. **Steady state, or a known transient.** Section 4 applies to the steady state;
   Section 6 to a specific transient. Most landscapes are neither.
3. **Drainage area is known and steady.** $A$ is measured from a modern DEM, and
   drainage capture or divide migration changes it over the integration time.
4. **Uniform rock strength and climate along the profile.** $K$ varies with
   lithology, precipitation and sediment flux; a $k_s$ change along a profile
   can be a $K$ change rather than a $U$ change, and that is another degeneracy
   of the same kind.
5. **The $\chi$ transform uses $\theta = m/n$ as an assumption.** Section 3
   measures how much the answer moves with it.
6. **Uplift is the only rock-motion term.** The profile responds to rock uplift;
   a changing base level, a growing delta or a fault crossing each add terms that
   must be checked.

## Mastery checkpoint

Without notes:

1. Derive $S = k_sA^{-\theta}$ from the incision law and state the dimensions of
   $K$ and $k_s$ for $m = 0.5$, $n = 1$.
2. Perform a $\chi$ transform for a simple $A(x)$ of your choice, and show that a
   steady profile is a straight line in $(\chi,z)$.
3. Explain, with the demonstration's numbers, why five different $(U,K)$ pairs
   produce the same profile to round-off.
4. Estimate the bias in the inferred uplift if $\theta$ is taken as 0.55 when it
   is really 0.50.
5. Compute the knickpoint speed for $K = 5\times10^{-6}$ and $A_0 = 2\times10^{6}$ m²
   with $m = 0.5$, and the travel time along a $\chi$ profile of 250 km.
6. Design a field campaign that would break the $U$–$K$ degeneracy, and name the
   quantity it would measure.

## Common pitfalls

1. **Reporting an uplift rate from a steepness index.** A $K$ was assumed.
2. **Comparing $k_s$ values across studies.** Units, reference area and
   exponents differ.
3. **Fitting $\theta$ with the $\chi$ transform and believing the $R^2$.**
   Measured: $R^2 = 0.999$ admits $\theta$ errors that change $k_s$ by a factor
   of four.
4. **Applying a steady-state inference above a knickpoint.** The measured
   apparent rate there is the old one.
5. **Using a uniform $\chi$ spacing on a non-uniform transform.** The steady
   state comes out wrong.
6. **Forgetting that a $K$ change mimics a $U$ change.** Both are one factor in
   $U/K$.

## Related modules

- [13-07-01 Erosion, Uplift and Thermochronology](01-erosion-and-uplift.md) —
  the independent exhumation-rate measurement that breaks the degeneracy.
- [13-07-03 Tectonic-Climate Feedbacks on Geological Timescales](03-tectonics-climate-feedback.md) —
  how the erosion rate feeds back into climate.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  the geodetic uplift rate.
- [13-03-03 Orogenic Systems, Crustal Thickening and Collapse](../03-plate-tectonics-quantitative/03-orogenic-systems.md) —
  the tectonic setting of the uplift being inferred.
- [18-08-02 Synthetic Testing](../../18-inverse-problems/08-practical-inversion-workflow/02-synthetic-testing.md) —
  the workflow this lesson demonstrates.

Companion exercises:
[`exercises/02-river-profile-tectonics-exercises.md`](exercises/02-river-profile-tectonics-exercises.md)
and
[`exercises/02-river-profile-tectonics-solutions.md`](exercises/02-river-profile-tectonics-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/07-geomorphology-tectonics-climate/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python river_profile_tectonics_demo.py
```
