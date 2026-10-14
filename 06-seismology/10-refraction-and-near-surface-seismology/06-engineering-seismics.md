---
id: 06-10-06
title: "Engineering Seismology Applications"
level: advanced
prereqs: ["06-10-05", "06-10-02"]
tags: [seismology, near-surface, engineering, survey-design, moduli, strain]
---

# Engineering Seismology Applications

> **All models and data in this module are SYNTHETIC.** The site profile, the
> borehole geometry, the picking errors, the structural mass and stiffness, the
> design velocity and the modulus-reduction curve are chosen teaching values. No
> real site, borehole, structure or code coefficient is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Design** a refraction spread for a stated target depth from the crossover
   relation, and **compute** the deepest target a given spread can reach.
2. **Derive** the depth error of a two-layer interpretation from the
   least-squares uncertainty of the intercept, and **verify** it against a Monte
   Carlo simulation.
3. **Compute** interval shear velocities from downhole arrival times, propagate
   their errors, and **obtain** $V_{S30}$ with an uncertainty budget that
   separates velocity error from thickness error.
4. **Convert** $V_p$, $V_s$ and $\rho$ into $\mu$, $\nu$, $E$ and $M$, and
   **derive** the exact sensitivity $\partial\nu/\partial V_s$ that shows where
   Poisson's ratio is fragile.
5. **Compare** a site period with a structural period from
   $T = 2\pi\sqrt{m/k}$ and **state** the design question that comparison answers.
6. **Estimate** the shear strain from a surface velocity and **explain** why the
   small-strain velocity may not be the operative modulus, quantifying the
   consequences of applying the reduction in different places.
7. **State** which of these results are exact relations and which are
   conventions, and **identify** the two numbers in this lesson that are
   dominated by an assumption rather than by a measurement.

## Prerequisites

- [05 Site Characterisation: Vs30 and Site Response](05-seismic-hazards-site.md) —
  the $V_{S30}$ definition, the weights and the transfer function used here.
- [02 Delay-Time (Plus-Minus) Methods and Depth Estimation](02-plus-minus-method.md) —
  the depth-from-delay algebra whose error this lesson propagates into a design.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  picking and bookkeeping of the arrival times used throughout.

## 1. Intuition: what an engineering survey is actually asked

A geotechnical brief rarely says "measure the shear velocity". It says: where is
bedrock, how deep and how variable; what is the small-strain stiffness of each
unit; what is the site period; will a foundation settle; is the ground rippable;
and (for a seismic design) what is $V_{S30}$. Behind each is a seismic
measurement, and behind each measurement is a choice of method, geometry and
resolution limit.

This lesson is the assembly of the module. Every method appears, and the point of
the exercise is to see which question each one answers and where the answer is
limited by physics rather than by effort:

- **refraction** answers "where is the first fast layer, and how deep";
- **downhole/crosshole** answers "how fast is each interval, directly";
- **surface waves** (Lesson 04) answer "what is the small-strain profile, including
  slow layers that refraction cannot see";
- **the transfer function** (Lesson 05) answers "what does the column do to a wave".

Two honest difficulties recur, and this lesson quantifies both.

1. **The exact part and the empirical part are adjacent and look identical.**
   $\mu = \rho V_s^{2}$ is exact for an isotropic elastic medium; "bearing capacity
   from $V_s$" is an empirical correlation that is site specific. A velocity
   measurement constrains the small-strain modulus and nothing else directly.
2. **The uncertainty is usually dominated by geometry, not by the seismogram.**
   Section 5's budget attributes $62\%$ of the $V_{S30}$ variance to a
   $0.10\ \mathrm{m}$ survey tolerance on layer boundaries and $38\%$ to the
   velocity measurement — so buying better seismograms would not have moved the
   answer much.

## 2. Precise definitions

| Quantity | Symbol | Definition | Unit |
|---|---|---|---|
| interval velocity | $V$ | layer thickness / interval travel time | $\mathrm{m\,s^{-1}}$ |
| small-strain modulus | $\mu$ | shear modulus, $\mu = \rho V_s^{2}$ | Pa |
| Poisson's ratio | $\nu$ | $(V_p^{2}-2V_s^{2})/[2(V_p^{2}-V_s^{2})]$ | — |
| constrained modulus | $M$ | $\rho V_p^{2}$ | Pa |
| Young's modulus | $E$ | $2\mu(1+\nu)$ | Pa |
| site period | $T_0$ | $4H/V_{S,\text{avg}}$ for a uniform column on a rigid base | s |
| structural period | $T$ | $2\pi\sqrt{m/k}$ for a single-degree-of-freedom oscillator | s |
| shear strain | $\gamma$ | $\approx \mathrm{PGV}/V_s$ | — |

$\mu$, $M$, $E$ and $\nu$ as written are **exact relations for a homogeneous,
isotropic, linearly elastic medium**. They are identities, not correlations, and
misquoting them as empirical is as wrong as treating a correlation as exact.

## 3. Derivations

### 3.1 Spread design from the crossovers

Lesson 01's crossover relation,
$x_c = 2h\sqrt{(v_2+v_1)/(v_2-v_1)}$, is the design equation. Rearranged for a
spread of length $L = 3x_c$ (so that the far branch has a well-determined slope):

$$\boxed{\;h_{\max} = \frac{L}{6}\sqrt{\frac{v_2-v_1}{v_2+v_1}}.\;}$$

For the demonstration's SYNTHETIC site — $18\ \mathrm{m}$ of overburden whose
travel-time-average $\mathbf{P}$ velocity is $988.4\ \mathrm{m\,s^{-1}}$ over
bedrock at $3500\ \mathrm{m\,s^{-1}}$, a contrast of $3.541$ — the crossover is

$$x_c = 2 \times 18\sqrt{\frac{3500+988.4}{3500-988.4}} = 36 \times 1.33681
= 48.13\ \mathrm{m},$$

and the corresponding spread is $144.4\ \mathrm{m}$. Design against contrast:

| $v_2/v_1$ | $x_c$ (m) | spread $3x_c$ (m) |
|---|---|---|
| 1.2 | 119.40 | 358.20 |
| 1.5 | 80.50 | 241.50 |
| 2.0 | 62.35 | 187.06 |
| 3.541 | 48.13 | 144.38 |
| 5.0 | 44.09 | 132.27 |

**The same target at the same depth needs a spread 2.5 times longer when the
contrast is 1.2 instead of 3.5.** What makes a refraction survey expensive is a
weak contrast, not a thick layer of soil. And the reach of a fixed spread:

| spread $L$ (m) | $h_{\max}$ (m), this site |
|---|---|
| 50 | 6.23 |
| 100 | 12.47 |
| 200 | 24.93 |
| 400 | 49.87 |

Note that the effective overburden velocity here is a **travel-time average** of
three layers ($\sum h_i/V_{P,i} = 0.0182105\ \mathrm{s}$ over $18\ \mathrm{m}$),
used in a two-layer formula. That substitution is the design convenience of this
section, and Section 4 turns it into an error bar rather than hiding it.

### 3.2 Depth error from the picking error

The two-layer depth is
$h = t_i v_1 v_2/(2\sqrt{v_2^{2}-v_1^{2}})$, so with the velocities known

$$\sigma_h = \sigma_{t_i}\,\frac{v_1 v_2}{2\sqrt{v_2^{2}-v_1^{2}}}
= \sigma_{t_i} \times 515.191\ \mathrm{m\,s^{-1}}$$

for the demonstration's velocities: **one millisecond of intercept error is half a
metre of depth.** The intercept itself comes from a least-squares fit of the far
branch, $t = t_i + x/v_2$, over $N$ picks with mean offset $\bar{x}$ and spread
$S_{xx} = \sum (x-\bar{x})^{2}$:

$$\sigma_{t_i} = \sigma_t\sqrt{\frac{1}{N} + \frac{\bar{x}^{2}}{S_{xx}}},$$

which is the standard intercept uncertainty of a straight-line fit. For 40 picks
spread over $48.1$–$144.4\ \mathrm{m}$ with $\sigma_t = 1.0\ \mathrm{ms}$ this
gives $0.5571\ \mathrm{ms}$, hence

$$\sigma_h = 0.5571\times10^{-3} \times 515.191 = 0.2870\ \mathrm{m}
= 1.595\%\ \text{of}\ 18\ \mathrm{m}.$$

A 4000-realisation Monte Carlo, refitting every survey, returns
$\sigma_h = 0.2877\ \mathrm{m}$ with mean $h = 17.9968\ \mathrm{m}$: the analytic
covariance is right, so **the depth error of a design can be predicted before the
survey is shot.** Propagating the same $1\ \mathrm{ms}$ error for weaker contrasts,
with the geometry kept self-similar, gives

| $v_2/v_1$ | $x_c$ (m) | $\sigma_{t_i}$ (ms) | $\sigma_h$ (m) |
|---|---|---|---|
| 1.2 | 119.40 | 0.5571 | 0.4981 |
| 1.5 | 80.50 | 0.5571 | 0.3694 |
| 2.0 | 62.35 | 0.5571 | 0.3179 |
| 3.0 | 50.91 | 0.5571 | 0.2920 |
| 5.0 | 44.09 | 0.5571 | 0.2810 |

The intercept uncertainty is identical across rows because the self-similar
geometry scales both $\bar{x}$ and $S_{xx}$; the whole effect is the factor
$v_1v_2/(2\sqrt{v_2^{2}-v_1^{2}})$, and it inflates the depth error by a factor of
$1.8$ as the contrast falls from $5$ to $1.2$.

### 3.3 Elastic moduli — exact

For an isotropic elastic solid of density $\rho$,

$$\mu = \rho V_s^{2}, \qquad
\nu = \frac{V_p^{2}-2V_s^{2}}{2\left(V_p^{2}-V_s^{2}\right)}, \qquad
M = \rho V_p^{2}, \qquad E = 2\mu(1+\nu).$$

| layer | $V_p$ (m/s) | $V_s$ (m/s) | $\mu$ (GPa) | $\nu$ | $E$ (GPa) | $M$ (GPa) |
|---|---|---|---|---|---|---|
| 4 m fill | 400 | 150 | 0.041 | 0.418 | 0.115 | 0.288 |
| 6 m clay | 1500 | 250 | 0.119 | 0.486 | 0.353 | 4.275 |
| 8 m sand/gravel | 1900 | 450 | 0.405 | 0.470 | 1.191 | 7.220 |
| 12 m bedrock | 3500 | 1800 | 8.100 | 0.320 | 21.387 | 30.625 |

Two readings. Stiffness spans **two orders of magnitude** between the surface fill
and the bedrock, which is the physical reason a site period exists. And
Poisson's ratio is **not** monotone with stiffness: the saturated clay at
$V_p/V_s = 6$ sits at $\nu = 0.486$ (nearly incompressible in the only sense that
matters here), while the bedrock at $V_p/V_s = 1.94$ sits at $\nu = 0.320$.

Differentiating $\nu$ with respect to $V_s$ at fixed $V_p$ gives the exact result

$$\boxed{\;\frac{\partial\nu}{\partial V_s}
= -\,\frac{V_s V_p^{2}}{\left(V_p^{2}-V_s^{2}\right)^{2}}.\;}$$

For the clay, $-250 \times 2.25\times10^{6}/(2.1875\times10^{6})^{2}
= -1.176\times10^{-4}\ \mathrm{s\,m^{-1}}$, so a $5\%$ $V_s$ error
($12.5\ \mathrm{m\,s^{-1}}$) moves $\nu$ by $0.0015$; the demonstration's finite
differences give the range $0.4842$–$0.4871$. For the bedrock the same
calculation gives $-2.7\times10^{-4}\ \mathrm{s\,m^{-1}}$ and a range of
$0.2942$–$0.3432$, a span of $0.049$. **Poisson's ratio is fragile where
$V_p/V_s$ is near $\sqrt{3}$ ($\nu \approx 0.25$) and insensitive where
$\nu \to 0.5$.** A reliable $\nu$ therefore needs a reliable $V_s$, not a precise
$V_p$ — the same asymmetry Lesson 02 found for the refraction depth.

### 3.4 Period comparison

The site period of the soil column is
$T_0 = 4H/V_{S,\text{avg}}$ with $H = 18\ \mathrm{m}$ and
$V_{S,\text{avg}} = 18/\sum h_i/V_{S,i} = 263.0\ \mathrm{m\,s^{-1}}$, giving

$$T_0 = \frac{4 \times 18}{263.0} = 0.2738\ \mathrm{s}, \qquad
f_0 = 3.653\ \mathrm{Hz}.$$

A structure is represented in this comparison by its fundamental period. For a
single-degree-of-freedom oscillator of mass $m$ and stiffness $k$,

$$T = 2\pi\sqrt{\frac{m}{k}}
= 2\pi\sqrt{\frac{5.0\times10^{5}\ \mathrm{kg}}{8.0\times10^{6}\ \mathrm{N\,m^{-1}}}}
= 1.5708\ \mathrm{s},$$

so $T/T_0 = 5.737$: this structure is far from resonance with this site. The
stiffness that *would* put it on the site period is

$$k_{\text{res}} = m\left(\frac{2\pi}{T_0}\right)^{2}
= 5.0\times10^{5}\left(\frac{2\pi}{0.2738}\right)^{2}
= 2.634\times10^{8}\ \mathrm{N\,m^{-1}},$$

$32.9$ times the design value. **The engineering question is a period comparison,
and the velocity enters only through the period it implies** — which is why a
site period is more useful to a designer than a velocity profile, and why
Lesson 05's warning about $4H/V_{S30}$ matters: the rule is exact only for a
uniform column on a rigid base, and Section 4 of that lesson measured it
overestimating by $29\%$ and $35\%$ on two synthetic profiles.

### 3.5 Strain: which modulus is operative

At the top of the column a surface velocity of $\mathrm{PGV} = 0.10\
\mathrm{m\,s^{-1}}$ implies a shear strain of order

$$\gamma \approx \frac{\mathrm{PGV}}{V_s} = \frac{0.10}{150}
= 6.667\times10^{-4}.$$

Whether that is inside the linear range is a soil-property question this module
cannot answer from a velocity measurement, so apply a SYNTHETIC reduction curve and
report the sensitivity instead of asserting a threshold:

$$\frac{G}{G_{\max}} = \frac{1}{1 + \gamma/\gamma_{\text{ref}}},
\qquad \gamma_{\text{ref}} = 1.0\times10^{-3},$$

which gives $G/G_{\max} = 0.6000$. Since $V_s \propto \sqrt{G/\rho}$ for fixed
density, the top-layer velocity falls to $150\sqrt{0.6000} = 116.2\
\mathrm{m\,s^{-1}}$, a $22.5\%$ reduction. Where the reduction is applied then
decides the answer:

| case | $V_{S,\text{avg}}$ (m/s) | $T_0$ (s) | change |
|---|---|---|---|
| small strain, as measured | 263.0 | 0.2738 | — |
| reduction on every layer | 203.7 | 0.3534 | $+29.1\%$ |
| reduction on the top layer only | 236.2 | 0.3048 | $+11.3\%$ |

**The sign is certain and the size is not.** Applying the same factor everywhere
lengthens the site period by $29\%$; applying it only where the strain estimate is
large lengthens it by $11\%$. A factor of $2.6$ between two defensible
implementations, from a curve that was itself invented for this exercise. That is
the honest statement: a $V_s$ profile measures the small-strain modulus, and the
step from the small-strain modulus to the design modulus is a site-specific
modelling choice, not a measurement.

### 3.6 The uncertainty budget of Vs30

Downhole interval velocities from the demonstration's borehole (geophones at the
layer boundaries, one-way pick standard deviation $0.2\ \mathrm{ms}$):

| interval (m) | $V_s$ true (m/s) | $\Delta t$ (ms) | $V_s$ picked (m/s) | $\sigma_{V_s}$ (m/s) |
|---|---|---|---|---|
| 4 | 150 | 26.667 | 150.0 | 1.59 |
| 6 | 250 | 24.000 | 250.0 | 2.95 |
| 8 | 450 | 17.778 | 450.0 | 7.16 |
| 12 | 1800 | 6.667 | 1800.0 | 76.37 |

The relative errors rise with velocity: $1.06\%$, $1.18\%$, $1.59\%$, $4.24\%$. The
$V_{S30}$ calculation itself is $30/0.075111 = 399.41\ \mathrm{m\,s^{-1}}$ (site
class C against the standard boundaries), and its budget, from 20 000 Monte Carlo
realisations, is

| source | $\sigma_{V_{S30}}$ (m/s) | variance share |
|---|---|---|
| velocity error only | 3.020 | $38.3\%$ |
| boundary-depth error only ($\sigma = 0.10\ \mathrm{m}$) | 3.841 | $62.0\%$ |
| both | 4.880 | $100.0\%$ |

so $V_{S30} = 399.41 \pm 4.88\ \mathrm{m\,s^{-1}}$, $1.22\%$. The two single-source
variances sum to $100.3\%$ of the total, the $0.3\%$ being Monte Carlo sampling
error — i.e. the sources are independent and their variances add, as they should.
**The dominant term is a $10\ \mathrm{cm}$ survey tolerance on where the layers
are, not the seismogram.** This is the most useful number in the lesson: it says
where to spend the next unit of effort, and it is not where intuition usually
points.

## 4. Worked examples

### Example 1 — a foundation investigation, end to end

**Problem.** A site is $18\ \mathrm{m}$ of soil over bedrock. The refraction survey
gives $v_1 = 988.4\ \mathrm{m\,s^{-1}}$ (travel-time average of the overburden) and
$v_2 = 3500\ \mathrm{m\,s^{-1}}$. A design must know the bedrock depth to
$\pm 0.5\ \mathrm{m}$ with $1\ \mathrm{ms}$ picks. What spread is needed, and is the
requirement met?

**Step 1 — crossover.** $x_c = 2\times18\sqrt{4488.4/2511.6} = 48.13\ \mathrm{m}$.

**Step 2 — spread.** $L = 3x_c = 144.4\ \mathrm{m}$, say $150\ \mathrm{m}$ of
cable with $2\ \mathrm{m}$ spacing to give 75 receivers.

**Step 3 — achievable depth accuracy.** $\sigma_h = 0.2870\ \mathrm{m}$ from
Section 3.2, i.e. $\pm 1.6\%$ of the depth; with $40$ far-branch picks the Monte
Carlo confirms $0.2877\ \mathrm{m}$. **The requirement is met with room to spare.**

**Step 4 — the sensitivity to the contrast.** If the bedrock were softer and the
contrast $1.2$ instead of $3.5$, the same $1\ \mathrm{ms}$ pick would give
$\sigma_h = 0.4981\ \mathrm{m}$ and $x_c = 119.4\ \mathrm{m}$, so the spread would
have to be $358\ \mathrm{m}$ to keep the far branch inside it. Both the *cost* and
the *error* of the survey worsen together as the contrast weakens; they are not
independent penalties.

### Example 2 — from a velocity to a modulus to a period

**Problem.** Using the clay layer ($V_p = 1500$, $V_s = 250\
\mathrm{m\,s^{-1}}$, $\rho = 1900\ \mathrm{kg\,m^{-3}}$), compute $\mu$, $\nu$,
$E$ and $M$, and state what a $5\%$ $V_s$ error does to each.

**Step 1 — shear modulus.** $\mu = 1900 \times 250^{2} = 1.1875\times10^{8}\
\mathrm{Pa} = 0.119\ \mathrm{GPa}$.

**Step 2 — Poisson's ratio.**
$\nu = (2.25\times10^{6} - 1.25\times10^{5})/[2(2.25\times10^{6} -
6.25\times10^{4})] = 2.125\times10^{6}/4.375\times10^{6} = 0.4857$.

**Step 3 — the other moduli.** $E = 2\mu(1+\nu) = 2 \times 0.11875 \times
1.4857 = 0.353\ \mathrm{GPa}$ and $M = \rho V_p^{2} = 1900 \times 2.25\times10^{6}
= 4.275\ \mathrm{GPa}$.

**Step 4 — the errors.** $\mu \propto V_s^{2}$, so a $5\%$ velocity error is a
$10.25\%$ modulus error — the exponent is the amplification. $\nu$ moves by
$0.0015$ (Section 3.3), because $\nu$ is near $0.5$ and insensitive there.
$M$ does not change at all, since it contains only $V_p$. **Three quantities from
one measurement, three very different error amplifications, and the one a designer
is most likely to quote — $\nu$, through $E$ — has the smallest error here and the
largest one at a stiffer site.**

## 5. Assumptions and regime of validity

1. **$v_1$ of the overburden is a travel-time average used in a two-layer
   formula.** That is a design convenience. Its error is the dominant term in the
   depth error (Lesson 02 measures $+1.0667$ logarithmic sensitivity).
2. **Picks are independent Gaussian with a stated $\sigma$.** Real picks are
   correlated between neighbouring receivers, which makes the least-squares
   intercept uncertainty — and hence $\sigma_h$ — optimistic.
3. **Layers are homogeneous and their boundaries are horizontal.** The
   boundary-depth tolerance enters $V_{S30}$ with the largest variance share
   (Section 3.6), so a dipping or undulating contact is a first-order error, not a
   second-order one.
4. **Isotropic linear elasticity** for the moduli. Soils are neither at large
   strain; the relations of Section 3.3 are exact *within* the assumed model.
5. **The strain estimate $\gamma \approx \mathrm{PGV}/V_s$ is an order-of-magnitude
   proxy** for the wavefield-averaged strain, and the reduction curve is a
   SYNTHETIC teaching form. The *sign* of the resulting period shift is robust; the
   *size* is not (Section 3.5).
6. **A single-degree-of-freedom structure.** Real buildings have many modes and a
   period that lengthens as they damage; the comparison in Section 3.4 is a
   screening calculation, not a design.
7. **Resolution limits are respected.** A layer thinner than about a quarter of
   the dominant wavelength does not appear as a separate arrival in refraction,
   and downhole interval velocities need geophones inside the interval. The
   demonstration's $50\ \mathrm{Hz}$ P quarter-wavelengths are $2.00$,
   $7.50$, $9.50$ and $17.50\ \mathrm{m}$ for the four layers — exceeding the
   thickness of every layer except the shallowest — while the S
   quarter-wavelengths are $0.75$, $1.25$, $2.25$ and $9.00\ \mathrm{m}$, all
   shorter than the layers they belong to. **The same profile is nearly opaque to
   a P refraction survey and comfortable for an S-wave or surface-wave survey**,
   which is the quantitative reason shallow engineering work uses the latter.
8. **Velocity is not a design parameter.** Nothing here turns $V_s$ into bearing
   capacity, liquefaction resistance or settlement; those require site-specific
   correlations or in-situ tests, and the seismic survey's role is to interpolate
   between them.

## Mastery checkpoint

Use the demonstration's SYNTHETIC site: $4\ \mathrm{m}$ at $V_p = 400\
\mathrm{m\,s^{-1}}$, $V_s = 150\ \mathrm{m\,s^{-1}}$; $6\ \mathrm{m}$ at
$1500/250$; $8\ \mathrm{m}$ at $1900/450$;
$12\ \mathrm{m}$ at $3500/1800$; $\rho = 1800, 1900, 2000, 2500\
\mathrm{kg\,m^{-3}}$.

**(a)** Compute the travel-time-average $V_p$ of the $18\ \mathrm{m}$ overburden,
the crossover for bedrock at $18\ \mathrm{m}$, and the spread that places the
crossover at one third of the line.
**(b)** With $1\ \mathrm{ms}$ picks, $40$ far-branch picks and the geometry of (a),
compute $\sigma_h$ and state whether a $\pm 0.5\ \mathrm{m}$ specification is met.
**(c)** Compute $\mu$, $\nu$ and $E$ for the $8\ \mathrm{m}$ gravel layer
($\rho = 2000\ \mathrm{kg\,m^{-3}}$), and state the fractional change in $\mu$ for
a $5\%$ $V_s$ error.
**(d)** Compute the site period of the $18\ \mathrm{m}$ column, and the stiffness
that would put a $5.0\times10^{5}\ \mathrm{kg}$ oscillator on it.
**(e)** A $0.15\ \mathrm{m\,s^{-1}}$ surface velocity is expected in a design
event. Estimate the strain in the top layer, and state two reasons the measured
$V_s$ may not be the modulus that governs the response.
**(f)** List the two quantities in this lesson whose value is dominated by an
assumption rather than by a measurement, and name the assumption for each.

Worked answers are in the
[solutions](exercises/06-engineering-seismics-solutions.md).

## Common pitfalls

1. **Using the arithmetic-mean overburden velocity in the design formula.** The
   travel-time average is the one that reproduces the observed delay (Lesson 01),
   and the arithmetic mean is $14\%$ to $50\%$ higher in the demonstration's
   profiles.
2. **Ignoring the data you already have.** The reciprocal misfit and the
   near-branch picks (Lesson 02) are the free error bars of the depth and the
   overburden velocity; throwing them away leaves the design with no uncertainty
   statement at all.
3. **Quoting $\nu$ to three decimals from a $V_s$ with a $5\%$ error.** At a stiff
   site the span is $0.049$ (Section 3.3).
4. **Turning a velocity into a design parameter without a correlation.** $\mu$ is
   exact; bearing capacity is not.
5. **Comparing periods without stating which period.** A site period, a structural
   period and a predominant period from a spectrum are three different numbers, and
   the design question is which pair is being compared.
6. **Forgetting that the small-strain velocity is a ceiling.** At strong shaking the
   operative modulus is lower and the period longer; the sign is known and the size
   is not (Section 3.5).
7. **Spending the budget on better seismograms when the geometry is the error.**
   Section 3.6's budget attributes $62\%$ of the $V_{S30}$ variance to a
   $0.10\ \mathrm{m}$ boundary tolerance.

## Related modules

- [05 Site Characterisation: Vs30 and Site Response](05-seismic-hazards-site.md) —
  the transfer function and the $V_{S30}$ definition used in Sections 3.4 and 3.6.
- [01 Refraction Survey Geometry and Travel-Time Interpretation](01-refraction-basics.md) —
  the crossover relation that Section 3.1 turns into a survey design.
- [02 Delay-Time (Plus-Minus) Methods and Depth Estimation](02-plus-minus-method.md) —
  the depth and its sensitivity, propagated into a design here.
- [04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](04-masw-sasw.md) —
  the S-wave method that covers the layers refraction cannot resolve (Section 5.7).
- [11-06-01 Site Investigation: Objectives and Method Selection](../../11-exploration-geophysics/06-geotechnical-and-engineering/01-site-investigation.md) —
  how a seismic survey is chosen and combined with drilling and in-situ testing.
- [10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/01-spt-cpt-crosshole.md) —
  the in-situ tests that supply the correlations this lesson refuses to invent.

## Code and exercises

The demonstration is
[`code/engineering_seismics_demo.py`](code/engineering_seismics_demo.py):

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python engineering_seismics_demo.py
```

It prints every number quoted here — the design table, the depth-error table and
its Monte Carlo, the downhole velocities, the moduli, the period comparison, the
strain cases, the $V_{S30}$ budget and the quarter-wavelength table — with units,
and exits 0.

Exercises:
[`exercises/06-engineering-seismics-exercises.md`](exercises/06-engineering-seismics-exercises.md);
solutions:
[`exercises/06-engineering-seismics-solutions.md`](exercises/06-engineering-seismics-solutions.md).
Module overview: [`README.md`](README.md).
