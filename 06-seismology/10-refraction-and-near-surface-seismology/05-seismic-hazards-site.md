---
id: 06-10-05
title: "Site Characterisation: Vs30 and Site Response"
level: advanced
prereqs: ["06-10-04", "06-01-03"]
tags: [seismology, near-surface, vs30, site-response, amplification, site-class]
---

# Site Characterisation: Vs30 and Site Response

> **All models and data in this module are SYNTHETIC.** The two soil profiles, the
> densities, the damping, the design velocity and the perturbation size are chosen
> teaching values. No measured $V_{S30}$, no site classification of a real
> location and no published amplification factor is used. The site-class
> boundaries quoted in Section 2 are standard regulatory constants, stated
> explicitly as constants and applied here only as arithmetic.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** $V_{S30}$ exactly as a travel-time average and **derive** the
   arithmetic–harmonic inequality that bounds it.
2. **Derive** the exact sensitivity
   $\partial\ln V_{S30}/\partial\ln V_{S,i} = w_i$, where $w_i$ is the fraction of
   the vertical travel time spent in layer $i$, and **show** that the weights sum
   to one.
3. **Derive** the 1-D SH transfer function of a layered column from the wave
   equation, the free-surface condition and continuity, and **verify** the
   transfer-matrix implementation against the closed form for one layer.
4. **Explain** why the lossless resonance of a single layer equals the impedance
   ratio, and **measure** how damping reduces it.
5. **Demonstrate** that two profiles with identical $V_{S30}$ and identical site
   class can have different fundamental periods and different peak amplifications,
   and **quantify** the difference.
6. **Quantify** the uncertainty of $V_{S30}$ for a stated layer-velocity error, and
   **explain** why it is smaller than that error.
7. **State** the conditions under which a site class is a sufficient input to a
   design calculation, and the conditions under which it is not.

## Prerequisites

- [04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](04-masw-sasw.md) — where a
  $V_S$ profile comes from, and how wide its acceptable set is.
- [06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity](../01-elastic-wave-propagation/03-surface-waves.md) —
  why a long wavelength samples deep, which is the whole content of $V_{S30}$.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  the processing machinery behind any measured profile.

## 1. Intuition: one number for a design, and what it cannot carry

Most seismic design codes ask the engineer for **one** number describing the ground
beneath a site: the average shear-wave velocity in the uppermost $30\ \mathrm{m}$,
written $V_{S30}$. That single number selects a site class, and the site class
scales a whole design spectrum. The choice is not arbitrary. Soft ground amplifies
long-period shaking and $V_{S30}$ is a cheap, repeatable proxy for "how soft is the
top $30\ \mathrm{m}$", obtainable from a surface-wave survey, a downhole
measurement, or even a correlation with penetration tests.

The difficulty is that $V_{S30}$ is a *single scalar summary of a function* — the
velocity profile $V_S(z)$ — and summaries lose information. Two sites can share a
$V_{S30}$ exactly and still resonate at different frequencies with different peak
amplifications, because what the ground does to a wave depends on the *arrangement*
of the velocities and on the impedance contrasts between layers, not only on their
travel-time average.

This lesson does three things in order. It defines $V_{S30}$ and derives exactly
what it weights. It derives the 1-D SH transfer function that says what a layered
column does to a wave. Then it puts two profiles with identical $V_{S30}$ through
both, and measures the difference — which is the honest difficulty, stated as a
number rather than a caveat.

## 2. Precise definitions

### 2.1 Vs30

For a profile of $N$ layers of thickness $h_i$ and shear velocity $V_{S,i}$ whose
thicknesses sum to $30\ \mathrm{m}$,

$$\boxed{\;V_{S30} = \frac{30\ \mathrm{m}}
{\displaystyle\sum_{i=1}^{N} \frac{h_i}{V_{S,i}}}\;}$$

with units $\mathrm{m\,s^{-1}}$. The numerator is a distance and the denominator is
a time, so $V_{S30}$ is the velocity of the *uniform* column that a vertically
travelling wave would cross in the same time. It is the **thickness-weighted
harmonic mean** of the layer velocities; the thickness-weighted *arithmetic* mean
is a different and larger number (Section 3.1).

### 2.2 Site class

The widely used NEHRP/IBC style classification assigns a class from $V_{S30}$
against the standard boundaries

| class | $V_{S30}$ range ($\mathrm{m\,s^{-1}}$) |
|---|---|
| A | $> 1500$ |
| B | $760$–$1500$ |
| C | $360$–$760$ |
| D | $180$–$360$ |
| E | $< 180$ |

These boundaries are **conventions with legal force, not physical thresholds**:
there is no discontinuity in ground behaviour at $360\ \mathrm{m\,s^{-1}}$, and the
class is a label for a range of a proxy parameter. The demonstration's profiles,
with $V_{S30} = 200.00\ \mathrm{m\,s^{-1}}$, both fall in class D.

### 2.3 Site period, impedance and damping

| Quantity | Symbol | Definition |
|---|---|---|
| site period | $T_0$ | period of the fundamental resonance of the column |
| impedance | $Z$ | $\rho V_S$, with $\rho$ the density ($\mathrm{kg\,m^{-2}\,s^{-1}}$) |
| impedance ratio | — | $Z_{\text{half-space}}/Z_{\text{layer}}$, dimensionless |
| quality factor | $Q$ | $1/Q$ is the fraction of energy lost per radian |

The **site period** is the quantity a structure can be unlucky enough to match; the
**impedance ratio** sets how strongly the column can respond; and the **damping**
sets how much of that response is realised. All three are lost when a profile is
reduced to $V_{S30}$.

## 3. Derivations

### 3.1 Why a travel-time average, and what it weights

$V_{S30}$ is not a choice among averages: a vertical travel time through a column
is additive, $\Delta t = \sum_i h_i/V_{S,i}$, and the only velocity that produces
that time in a uniform column is $30/\Delta t$. Hence the definition in Section
2.1.

Take a fractional change $\delta V_{S,i}$ in one layer. Then
$\Delta t \to \Delta t + \delta(h_i/V_{S,i})$, and

$$\frac{\partial \ln V_{S30}}{\partial \ln V_{S,i}}
= \frac{h_i/V_{S,i}}{\Delta t} \equiv w_i,$$

**the fraction of the vertical travel time spent in layer $i$.** Three properties
follow, and they are the whole reason to prefer this definition to the arithmetic
mean:

- $0 < w_i < 1$ and $\sum_i w_i = 1$, so the weights are a partition;
- a thin slow layer can dominate, because $w_i \propto h_i/V_{S,i}$;
- the weighting is by time, not by thickness, which is the physically relevant
  weighting for a wave crossing the column.

The demonstration measures both sides of this identity. For its profile A
($6\ \mathrm{m}$ at $120$, $9\ \mathrm{m}$ at $180$, $15\ \mathrm{m}$ at
$300\ \mathrm{m\,s^{-1}}$) each layer takes exactly one third of the travel time
($0.05\ \mathrm{s}$ of $0.150000\ \mathrm{s}$), so the exact weights are
$0.3333$ each; a central finite difference of $\pm1\%$ on each layer's velocity
returns $0.3345$. For profile B ($10\ \mathrm{m}$ at $100$ over $20\ \mathrm{m}$ at
$400\ \mathrm{m\,s^{-1}}$) the exact weights are $0.6667$ and $0.3333$, measured as
$0.6712$ and $0.3345$, and the two measured weights sum to $1.0000$ as they must.
The small excess over the exact value at $\pm1\%$ is the curvature the second-order
term of the finite difference leaves behind.

**The arithmetic mean is not a harmless alternative.** For profile A it is
$228.00\ \mathrm{m\,s^{-1}}$, $14.0\%$ above $V_{S30}$; for profile B it is
$300.00\ \mathrm{m\,s^{-1}}$, $50.0\%$ above. The arithmetic–harmonic inequality
guarantees $V_{S30} \le$ arithmetic mean, with equality only for a uniform column,
and the gap grows with the velocity spread. Using the arithmetic mean would shift
profile B by half a class width.

### 3.2 The 1-D SH transfer function of a layered column

Take vertically propagating SH waves, $z$ measured down from the free surface, and
time dependence $e^{-i\omega t}$. In each layer the displacement is a superposition
of up- and down-going waves, $u = A e^{ikz} + B e^{-ikz}$ with $k = \omega/v^{*}$,
and the shear stress is $\tau = \mu^{*}\, \mathrm{d}u/\mathrm{d}z$ with
$\mu^{*} = \rho (v^{*})^{2}$. Propagating the state $(u, \tau)$ across a layer of
thickness $h$ gives

$$\begin{pmatrix} u \\ \tau \end{pmatrix}_{\!h}
= \mathbf{M}\,\begin{pmatrix} u \\ \tau \end{pmatrix}_{\!0}, \qquad
\mathbf{M} = \begin{pmatrix} \cos(kh) & \dfrac{\sin(kh)}{\mu^{*}k} \\[2mm]
-\mu^{*}k\,\sin(kh) & \cos(kh) \end{pmatrix},$$

with $\det \mathbf{M} = 1$. Multiplying the layer matrices from the top down gives
$\mathbf{M}_{\text{tot}}$, and the two boundary conditions are the free surface
($\tau = 0$) and the half-space field (an incident plus a reflected wave, with the
incident amplitude defining the reference "bedrock outcrop" motion). Eliminating
the free constants gives the **transfer function**

$$\boxed{\;T(\omega) = \frac{u_{\text{surface}}}{u_{\text{outcrop}}}
= \frac{1}{M^{\text{tot}}_{11}
- \dfrac{M^{\text{tot}}_{21}}{i\,Z_{\text{hs}}\,\omega}}.\;}$$

For a **single elastic layer** on a half-space this collapses to the familiar form

$$|T(f)| = \left|\frac{1}{\cos(2\pi f H/v_{s1})
+ i\,(Z_1/Z_2)\sin(2\pi f H/v_{s1})}\right|,$$

whose properties are worth reading off directly:

- $f \to 0$: $|T| \to 1$ — long-period motion is not amplified;
- $\cos(2\pi f H/v_{s1}) = 0$, i.e. $f_n = (2n+1)v_{s1}/(4H)$: the response equals
  the **impedance ratio** $Z_2/Z_1$, and the fundamental is
  $f_0 = v_{s1}/(4H)$, i.e. $T_0 = 4H/v_{s1}$;
- $\sin(2\pi f H/v_{s1}) = 0$: $|T| = 1$ — the anti-resonances.

The demonstration verifies its own transfer-matrix implementation against this
closed form: for $30\ \mathrm{m}$ of $200\ \mathrm{m\,s^{-1}}$ at
$1900\ \mathrm{kg\,m^{-3}}$ over $900\ \mathrm{m\,s^{-1}}$ at
$2200\ \mathrm{kg\,m^{-3}}$, the impedance ratio is $5.2105$ and the maximum
difference between the two computations over $5990$ frequencies is
$2.975\times10^{-14}$. For the damped case
($Q = 20$ on a rigid base, where the closed form is $1/|\cos(kh)|$ with the same
complex $k$), the peaks agree as $25.4630$ against $25.4630$ with a maximum
absolute deviation of $1.297\times10^{-10}$ — larger in absolute terms only because
a resonance amplifies every rounding difference. And the two common first-order
constant-$Q$ conventions differ by $0.01\%$ in the peak, which is the level at
which any constant-$Q$ statement is defined.

### 3.3 Damping, and the height of the peak

Without damping a single elastic layer's resonance equals the impedance ratio
exactly, which the demonstration measures at four contrasts:

| $V_{S,\text{half-space}}$ (m/s) | $Z_{\text{hs}}/Z_{\text{soil}}$ | peak $|T|$ (measured) |
|---|---|---|
| 400 | 2.3158 | 2.3158 |
| 600 | 3.4737 | 3.4737 |
| 900 | 5.2105 | 5.2105 |
| 1800 | 10.4211 | 10.4211 |

The measured peak equals the impedance ratio to five significant figures, which is
the derivation of Section 3.2 made visible. Add damping and the peak falls and
moves:

| $Q$ | fundamental $|T|$ | $f_0$ (Hz) |
|---|---|---|---|
| $\infty$ | 5.8759 | 2.1600 |
| 1000 | 5.8523 | 2.1600 |
| 100 | 5.6484 | 2.1580 |
| 50 | 5.4376 | 2.1560 |
| 20 | 4.8886 | 2.1500 |
| 10 | 4.1804 | 2.1420 |
| 5 | 3.2312 | 2.1240 |

For the layered column A, $Q = 20$ realises $83\%$ of the lossless peak. **A site
amplification quoted without its damping is at best two-thirds of a model**: the
impedance contrast sets the ceiling and $Q$ decides how much of it is reached.

### 3.4 "The" amplification factor needs its band

Averaging the same two sites' responses over different bands:

| band (Hz) | mean $|T|$, profile A | mean $|T|$, profile B |
|---|---|---|---|
| 0.05–1 | 1.1166 | 1.1094 |
| 0.1–10 | 2.3297 | 2.3559 |
| 0.5–2 | 2.0224 | 1.9926 |
| 0.5–10 | 2.3844 | 2.4118 |
| 2–10 | 2.4522 | 2.4904 |

The same site has factors from $1.11$ to $2.45$ depending only on the band. That is
not a contradiction: a band average answers "how much does this site amplify this
range of periods", and a peak answers "what does it do at resonance". Both are
useful, neither is "the" factor, and a quoted factor without its band is not a
result.

## 4. Two profiles, one $V_{S30}$ — the honest difficulty

Take

| | profile A | profile B |
|---|---|---|
| layer 1 | $6\ \mathrm{m}$ at $120\ \mathrm{m\,s^{-1}}$ | $10\ \mathrm{m}$ at $100\ \mathrm{m\,s^{-1}}$ |
| layer 2 | $9\ \mathrm{m}$ at $180\ \mathrm{m\,s^{-1}}$ | $20\ \mathrm{m}$ at $400\ \mathrm{m\,s^{-1}}$ |
| layer 3 | $15\ \mathrm{m}$ at $300\ \mathrm{m\,s^{-1}}$ | — |
| travel time to 30 m | $0.150000\ \mathrm{s}$ | $0.150000\ \mathrm{s}$ |
| $V_{S30}$ | $200.00\ \mathrm{m\,s^{-1}}$ | $200.00\ \mathrm{m\,s^{-1}}$ |
| site class | D | D |

The travel-time construction of profile B makes the equality exact: with
$\sum h_i/V_{S,i} = 0.1 + 0.05 = 0.15\ \mathrm{s}$, both columns give
$30/0.15 = 200.00\ \mathrm{m\,s^{-1}}$, and the demonstration prints a difference of
$0.00\times10^{0}\ \mathrm{m\,s^{-1}}$.

A is a normally consolidated column that stiffens gradually; B is a soft layer
sitting directly on much stiffer material — a very different site, with the same
class. Over a half-space of $900\ \mathrm{m\,s^{-1}}$ and
$2200\ \mathrm{kg\,m^{-3}}$, with $Q = 20$ in the soil and $Q = 100$ in the
half-space:

| quantity | profile A | profile B |
|---|---|---|
| fundamental resonance $f_0$ | $2.1500\ \mathrm{Hz}$ | $2.2520\ \mathrm{Hz}$ |
| fundamental period $T_0 = 1/f_0$ | $0.4651\ \mathrm{s}$ | $0.4440\ \mathrm{s}$ |
| $|T|$ at the fundamental | $4.8886$ | $6.9782$ |
| uniform-column rule $4H/V_{S30}$ | $0.6000\ \mathrm{s}$ | $0.6000\ \mathrm{s}$ |
| rule / measured period | $1.290$ | $1.351$ |

Four measured statements:

1. **The peak amplification differs by a factor of $1.427$** between sites that a
   code cannot distinguish.
2. **The periods differ by $4.5\%$**, small but real, and in opposite directions
   from any simple argument about layer thickness.
3. **The uniform-column rule $T_0 = 4H/V_{S30}$ overestimates the period by
   $29\%$ and $35\%$** (it is exact only for a uniform column on a rigid base),
   which is the same lesson as the time-weighted sensitivity: $V_{S30}$ is a
   *travel-time* average, and resonance is not a travel-time property.
4. **The band means are nearly identical** ($2.3297$ against $2.3559$, a $1.1\%$
   difference) while the peaks differ by $43\%$. A band average is the one summary
   in which these two sites *do* look alike, which is why the difference they hide
   matters for a structure whose period is near $0.45\ \mathrm{s}$.

The conclusion is not that $V_{S30}$ is useless. It is a reproducible, cheap,
first-order descriptor, and across many sites it correlates with response. The
conclusion is that **a site class is a population statement, and the response of
the individual site in front of you is a function, not a class** — and that a
structure whose period is close to the site period needs the function.

## 5. Worked examples

### Example 1 — $V_{S30}$, its uncertainty, and its weights

**Problem.** Profile A, with each layer's $V_S$ uncertain by $10\%$ (independent).
Compute $V_{S30}$, its standard deviation, and the share of the variance from each
layer.

**Step 1 — the value.** $\Delta t = 6/120 + 9/180 + 15/300
= 0.05 + 0.05 + 0.05 = 0.150000\ \mathrm{s}$, so
$V_{S30} = 30/0.150000 = 200.00\ \mathrm{m\,s^{-1}}$.

**Step 2 — the weights.** $w_i = 0.3333$ for each layer, from Section 3.1.

**Step 3 — the analytic spread.** With independent errors and all
$\sigma_{V,i}/V_{S,i} = 0.10$,

$$\frac{\sigma_{V_{S30}}}{V_{S30}}
= \sqrt{\sum_i \left(w_i \frac{\sigma_{V,i}}{V_{S,i}}\right)^{2}}
= 0.10\sqrt{3 \times 0.3333^{2}} = 0.10 \times 0.5774 = 0.0577,$$

i.e. $\sigma_{V_{S30}} = 11.55\ \mathrm{m\,s^{-1}}$. The demonstration prints
$11.547\ \mathrm{m\,s^{-1}}$ ($5.77\%$). **A $10\%$ velocity error produces a
$5.8\%$ error in $V_{S30}$**: the quadrature of the weights averages independent
errors down, exactly as a sum of independent random terms does.

**Step 4 — the check.** A 20 000-realisation Monte Carlo gives
$\sigma = 11.704\ \mathrm{m\,s^{-1}}$ ($5.85\%$) with mean
$198.62\ \mathrm{m\,s^{-1}}$ and a 5th–95th percentile range of $179.2$ to
$217.8\ \mathrm{m\,s^{-1}}$. The mean sits $1.4\ \mathrm{m\,s^{-1}}$ *below* the
profile value because $V_{S30}$ is a convex function of the velocities (Jensen's
inequality): the estimator is biased low by an amount second order in the
uncertainty, and the Monte Carlo reproduces it. The $1.4\%$ difference between the
analytic and simulated standard deviations is the same nonlinearity.

### Example 2 — the transfer function by hand for one layer

**Problem.** Compute $|T|$ at $f = 5\ \mathrm{Hz}$ for $30\ \mathrm{m}$ of
$200\ \mathrm{m\,s^{-1}}$ ($\rho = 1900$) over a half-space of
$900\ \mathrm{m\,s^{-1}}$ ($\rho = 2200$).

**Step 1 — the impedance ratio.** $Z_1 = 1900 \times 200 = 3.80\times10^{5}$ and
$Z_2 = 2200 \times 900 = 1.98\times10^{6}$, so $Z_1/Z_2 = 0.19192$.

**Step 2 — the phase.** $2\pi f H/v_{s1} = 2\pi \times 5 \times 30/200 = 4.7124\
\mathrm{rad}$, so $\cos = 0.0000$ and $\sin = -1.0000$.

**Step 3 — the amplitude.**
$|T| = 1/|0.0000 + i(0.19192)(-1.0000)| = 1/0.19192 = 5.2105$, the impedance
ratio, as the resonance condition demands. The demonstration's table reports
exactly $5.2105$ at $5\ \mathrm{Hz}$.

**Step 4 — the interpretation.** At its resonance a lossless layer is a perfect
resonator, which is unphysical; the finite answer in any real calculation comes
from damping (Section 3.3) or from a finite impedance ratio. The peak frequency
here is $f_0 = v_{s1}/(4H) = 200/120 = 1.6667\ \mathrm{Hz}$, and the
higher resonances are the odd multiples one would expect — the $5\ \mathrm{Hz}$
value is the third.

## 6. Assumptions and regime of validity

1. **One-dimensional, horizontally layered, vertically propagating SH.** Basin
   geometry, surface waves and 2-D focusing are omitted, and the largest
   amplifications observed in nature come from exactly those omissions. A
   1-D column is the floor of the problem, not the ceiling.
2. **Linear viscoelastic response with constant $Q$.** Real damping is
   frequency-dependent and strain-dependent; the constant-$Q$ substitution is a
   first-order approximation, and the two common conventions differ by $0.01\%$ in
   the peak (Section 3.2), which is the size of the statement.
3. **Small strain.** $V_S$ from a MASW or downhole survey is the small-strain
   velocity. At strong shaking the operative modulus is smaller (Lesson 06
   measures the direction and size of that effect).
4. **A density assumption.** $V_{S30}$ contains no density, but the impedance
   ratio does; a density guessed to $10\%$ moves the peak by roughly $10\%$.
5. **The half-space is the reference condition.** The transfer function is defined
   against the half-space *outcrop*; applying it to a hazard curve computed for a
   different reference condition double-counts or omits the correction.
6. **$V_{S30}$ is treated as an input, not a measurement.** Every $V_{S30}$ carries
   the profile uncertainty of Example 1 plus the inversion's acceptable set
   (Lesson 04), and the class boundary arithmetic hides both: a site with
   $V_{S30} = 365 \pm 20\ \mathrm{m\,s^{-1}}$ sits on the C/D boundary and can be
   reported in either class by an entirely honest study.
7. **The profile is laterally homogeneous over the array footprint.** The deepest
   part of a 30 m column measured by surface waves is smeared over tens of metres
   laterally, so $V_{S30}$ describes an average site, not a borehole.

## Mastery checkpoint

Use the demonstration's two profiles and its $900\ \mathrm{m\,s^{-1}}$,
$2200\ \mathrm{kg\,m^{-3}}$ half-space with $Q = 20$ in the soil.

**(a)** For a third profile, $5\ \mathrm{m}$ at $150\ \mathrm{m\,s^{-1}}$,
$10\ \mathrm{m}$ at $250\ \mathrm{m\,s^{-1}}$ and $15\ \mathrm{m}$ at
$500\ \mathrm{m\,s^{-1}}$, compute $\Delta t$, $V_{S30}$, the class, the exact
weights $w_i$, and the arithmetic mean for comparison.
**(b)** Compute $4H/V_{S30}$ for that profile and state what the rule assumes and
why it is only an estimate.
**(c)** Its top layer is stiffened by $20\%$. Compute the change in $V_{S30}$ from
the weight $w_1$ alone, and say which statement about the site changed more: the
class or the response.
**(d)** Estimate the variance share attributable to $w_1$ if every layer velocity
has the same $10\%$ uncertainty, and state when the top layer dominates.
**(e)** Explain in two sentences why two profiles with equal $V_{S30}$ can differ by
$43\%$ in peak amplification, using the words *impedance contrast* and *arrangement*.
**(f)** A colleague reports $V_{S30} = 370 \pm 25\ \mathrm{m\,s^{-1}}$ and labels
the site class C. State the honest alternative and why it is not a mistake.

Worked answers are in the
[solutions](exercises/05-seismic-hazards-site-solutions.md).

## Common pitfalls

1. **Averaging velocities arithmetically.** For profile B the arithmetic mean is
   $50\%$ above $V_{S30}$; the travel-time average is the only one a travel time
   supports.
2. **Treating the class boundary as physics.** $360\ \mathrm{m\,s^{-1}}$ is a
   convention; a site measured at $365 \pm 20$ spans two classes.
3. **Quoting an amplification with no band, no damping and no statement of the
   frequency of interest.** Section 3.4's factors run from $1.11$ to $2.45$ for one
   site.
4. **Assuming equal $V_{S30}$ means equal response.** Section 4 measures a $1.427$
   ratio in the peak.
5. **Using $T_0 = 4H/V_{S30}$ as the site period.** It overestimates by $29\%$ and
   $35\%$ on the two demonstration profiles; it is exact only for a uniform column
   on a rigid base.
6. **Forgetting that the deepest part of the profile is the least constrained.**
   Depth-of-investigation limits (Lesson 04) mean the bottom of the 30 m column is
   usually the weakest link, and it may carry a large weight.
7. **Transferring a small-strain $V_{S30}$ to a strong-motion design without a
   strain statement.** The direction is predictable (softer, longer period); the
   size is site-specific (Lesson 06).

## Related modules

- [04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](04-masw-sasw.md) — where
  the profile comes from, and how wide its acceptable set is.
- [06 Engineering Seismology Applications](06-engineering-seismics.md) — downhole
  and refraction measurements of the same profile, and the section that puts the
  two methods side by side.
- [06-11-06 Hazard Maps, Site Amplification and Design Codes](../11-earthquake-statistics-and-hazard/06-hazard-mapping.md) —
  what is done with the site factor: the hazard curve, the design spectrum, the
  nonlinearity and the map.
- [06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity](../01-elastic-wave-propagation/03-surface-waves.md) —
  why depth sensitivity scales with wavelength, which is what makes $V_{S30}$ a
  30 m average and not a deeper one.
- [10-04-02 Shear-Wave Velocity Modelling and Site Classification](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/02-shear-wave-velocity-modelling.md) —
  the geotechnical workflow that consumes this number.

## Code and exercises

The demonstration is
[`code/seismic_hazards_site_demo.py`](code/seismic_hazards_site_demo.py):

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_hazards_site_demo.py
```

It prints every number quoted here — $V_{S30}$ for both profiles, the weights,
the transfer-matrix verification, the contrast and damping tables, the band
averages and the Monte Carlo — with units, and exits 0.

Exercises:
[`exercises/05-seismic-hazards-site-exercises.md`](exercises/05-seismic-hazards-site-exercises.md);
solutions:
[`exercises/05-seismic-hazards-site-solutions.md`](exercises/05-seismic-hazards-site-solutions.md).
Module overview: [`README.md`](README.md).
