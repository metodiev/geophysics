---
id: 11-02-03
title: "Gravity for Chromite, Massive Sulphide and Iron Ore"
level: graduate
prereqs: ["07-03-01", "07-03-02", "11-02-01"]
tags: [exploration-geophysics, mineral-exploration, gravity, bouguer, depth-estimation, excess-mass]
---

# Gravity for Chromite, Massive Sulphide and Iron Ore

Gravity is the exploration method with the fewest interpretation ambiguities, and
the cleanest reason: unlike magnetics, it has no direction problem, and unlike EM,
it has no conductivity–depth coupling. What it has instead is a **shape problem**.
The anomaly of a body depends on its aspect ratio through the power of $z$ in the
denominator — $1/z^{2}$ for a sphere, $1/z$ for a long cylinder — and the depth
inferred from a profile is only as good as the shape assumed. This lesson derives
both formulas, shows that the cylinder's depth rule is *exact* while the sphere's
must be calibrated, quantifies the bias from using the wrong one, computes the
free-air and Bouguer corrections from standard constants, demonstrates that the
residual anomaly is a *choice* rather than a measurement, and derives the
excess-mass invariant that recovers the body's mass without knowing its shape.

**All models and data in this module are SYNTHETIC.** Density contrasts,
geometries, station spacing, noise, regional functions and reduction density are
chosen teaching values, not measurements or properties of any real deposit.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the anomaly of a buried sphere and of an infinite horizontal
   cylinder from the potential, and **explain** why the powers of $z$ differ.
2. **Compute** the anomaly amplitudes of chromite, massive sulphide and iron-ore
   contrasts in a common geometry, and **state** which input dominates the
   uncertainty in a massive sulphide target model.
3. **Derive** the exact depth rule of the cylinder ($x_{1/2}=z$) and the
   calibrated rule of the sphere ($x_{1/2} = z\sqrt{2^{2/3}-1}$), and **quantify**
   the depth bias from using the wrong shape.
4. **Compute** the free-air gradient $2g/a$ and the Bouguer slab effect
   $2\pi G\rho t$, and **explain** why a levelling tolerance translates into a
   height-accuracy requirement.
5. **Measure** how the order of a fitted regional changes the residual amplitude
   and the inferred depth, and **state** what must accompany a quoted depth.
6. **Derive** the excess-mass integral $\lambda = (1/2\pi G)\int \Delta g\,
   \mathrm{d}x$ for a 2-D body, **verify** it numerically, and **explain** why the
   equivalent statement for a 3-D body requires a map rather than a profile.
7. **State** the assumptions under which a gravity depth is meaningful.

## Prerequisites

- [07-03-01 Anomaly Interpretation](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md)
  — free-air, Bouguer and the anomaly concepts used here.
- [07-03-02 Simple-Body Formulas](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md)
  — the sphere, cylinder and slab formulas, derived.
- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where density contrasts sit in the deposit-class table.

## 1. Two shapes, two powers of $z$

### 1.1 The buried sphere: $1/z^{2}$

Outside a spherically symmetric body the potential is that of a point mass,
$V = GM/r$, so directly above the centre at depth $z$

$$\Delta g_{\text{sphere}} = \frac{GM}{z^{2}}
= \frac{4}{3}\pi G\,\Delta\rho\,\frac{R^{3}}{z^{2}} .$$

### 1.2 The infinite horizontal cylinder: $1/z$

Integrate the point-mass attraction along an infinite line of mass per unit length
$\lambda = \pi R^{2}\Delta\rho$. For a line element at horizontal distance $u$ from
the observation point, the vertical contribution falls as
$(z^{2}+u^{2})^{-3/2}$, and

$$\Delta g_{\text{cyl}}(x) = G\lambda z\int_{-\infty}^{\infty}
\frac{\mathrm{d}u}{\left[(x-u)^{2}+z^{2}\right]^{3/2}}
= \frac{2G\lambda z}{x^{2}+z^{2}},
\qquad\text{so}\qquad
\Delta g_{\text{cyl}}(0) = \frac{2G\lambda}{z} .$$

The integral evaluates to $2/z^{2}$, which is where the single power of $z$
comes from: **the third dimension is not there to dilute the field.** The
demonstration checks this by superposing point masses along a finite line: at
$L = 2\ \mathrm{km}$ the summed attraction is $98.1\%$ of the 2-D formula, at
$L = 20\ \mathrm{km}$ it is $99.98\%$, and at $L = 100\ \mathrm{km}$ it agrees to
four decimals. The 2-D formula is the long-line limit, and the ratio is the
measure of how "2-D" a finite body is.

### 1.3 Why the difference matters, measured

| $z$ (m) | sphere (mGal) | cylinder (mGal) | ratio |
|---|---|---|---|
| 100 | 1.6774 | 2.5162 | 1.50 |
| 200 | 0.4194 | 1.2581 | 3.00 |
| 400 | 0.1048 | 0.6290 | 6.00 |
| 800 | 0.0262 | 0.3145 | 12.00 |

with $\Delta\rho = 600\ \mathrm{kg\,m^{-3}}$ and $R = 100\ \mathrm{m}$. Solving
for the depth at which a cylinder produces the *same* amplitude as a sphere at a
given depth:

| sphere at (m) | equivalent cylinder depth (m) | factor |
|---|---|---|
| 100 | 150.0 | 1.50 |
| 200 | 600.0 | 3.00 |
| 400 | 2400.0 | 6.00 |

The factor grows without bound. There is no "twice as deep" rule of thumb, and any
such rule also depends on the noise threshold. **Deciding which formula applies is
a statement about the body's aspect ratio, not about the method**, and it is
usually the largest single modelling uncertainty in a gravity interpretation.

## 2. Anomaly amplitudes for three deposit classes

| deposit class | $\Delta\rho$ (kg m⁻³) | sphere, $\Delta g$ (mGal) | cylinder, $\Delta g$ (mGal) |
|---|---|---|---|
| chromite | 800 | 0.559 | 1.677 |
| massive sulphide | 600 | 0.419 | 1.258 |
| iron ore (hematite-rich) | 900 | 0.629 | 1.887 |

at $R = 100\ \mathrm{m}$, $z = 200\ \mathrm{m}$. Two comments:

- The **chromite and iron-ore contrasts are large and robust**, because they are
  carried by oxide minerals whose densities are fixed by mineralogy
  ($\sim4.5$–$5.2\ \mathrm{g\,cm^{-3}}$ for chromite, $\sim5.2$ for hematite)
  against a silicate host.
- The **massive sulphide contrast is the least certain**, because it depends on
  the proportion of sulphide to gangue, on the sulphide assemblage, and on the
  porosity. Its *range* is the dominant uncertainty in the target model, and it is
  the reason a gravity anomaly over a sulphide body is rarely quoted with a
  better than $\pm30\%$ density contrast.

## 3. Depth from shape: one exact rule, one calibrated rule

### 3.1 The cylinder rule is exact

From §1.2,

$$\frac{\Delta g_{\text{cyl}}(x)}{\Delta g_{\text{cyl}}(0)}
= \frac{z^{2}}{x^{2}+z^{2}} = \frac12
\;\Longrightarrow\; x_{1/2} = z .$$

**The half-width at half-maximum equals the depth exactly**, with no calibration
constant and no assumption beyond the 2-D geometry. The demonstration measures
$200.000\ \mathrm{m}$ for a true depth of $200\ \mathrm{m}$, a ratio of exactly
$1.000000$.

### 3.2 The sphere rule needs a constant

From §1.1 the profile is
$\Delta g(x) = \tfrac{4}{3}\pi G\Delta\rho R^{3} z (x^{2}+z^{2})^{-3/2}$, so

$$\frac{z}{(x^{2}+z^{2})^{3/2}} = \frac{1}{2z^{2}}
\;\Longrightarrow\; x^{2}+z^{2} = 2^{2/3}z^{2}
\;\Longrightarrow\;
x_{1/2} = z\sqrt{2^{2/3}-1} = 0.766421\,z .$$

The demonstration reproduces $0.766421$ both by measurement and from the closed
form. A rule of this kind is only as good as the shape assumed, and the shape is
what a single profile constrains least.

### 3.3 The bias from the wrong shape, measured

Applying the **sphere** rule to a **cylinder** anomaly at $200\ \mathrm{m}$:

$$z_{\text{apparent}} = \frac{x_{1/2}}{0.766421} = \frac{200.0}{0.766421}
= 261.0\ \mathrm{m} \quad (+61.0\ \mathrm{m},\ +30.5\%).$$

A $30\%$ depth error from a modelling choice, with perfect data and no noise. This
is the honest content of the shape problem: it is systematic, it does not shrink
with better instruments, and it is only resolved by a second measurement — a
profile in a different direction, a map, or an independent constraint on the
strike length.

## 4. Free-air and Bouguer: standard constants, computed

### 4.1 The free-air correction

Normal gravity falls with height at the rate $\mathrm{d}g/\mathrm{d}h = -2g/a$
(differentiating $GM/r^{2}$ and using $g = GM/a^{2}$). With the standard constants
$g = 9.80665\ \mathrm{m\,s^{-2}}$ and $a = 6.371\times10^{6}\ \mathrm{m}$,

$$\frac{2g}{a} = \frac{2(9.80665)}{6.371\times10^{6}}
= 3.078528\times10^{-6}\ \mathrm{s^{-2}} = 0.3079\ \mathrm{mGal\,m^{-1}} .$$

The conventional value quoted for the reference ellipsoid is
$0.3086\ \mathrm{mGal\,m^{-1}}$; the difference is the latitude dependence of the
normal vertical gradient, and the demonstration prints its computed value so the
reader can see which convention is in use.

### 4.2 The Bouguer slab

An infinite flat sheet of surface density $\sigma$ produces the vertical attraction
$2\pi G\sigma$, **independent of the observer's height** — a result worth deriving,
because it is the reason a slab correction exists at all. For a sheet of thickness
$t$ and density $\rho$, $\sigma = \rho t$, so

$$\boxed{\;\Delta g_{\text{slab}} = 2\pi G\rho t\;}$$

and the correction is linear in thickness with coefficient $2\pi G\rho$:

| $\rho$ (kg m⁻³) | slab coefficient (mGal m⁻¹) | effect of 100 m of relief (mGal) |
|---|---|---|
| 2200 | 0.0923 | 9.23 |
| 2670 | 0.1120 | 11.20 |
| 3000 | 0.1258 | 12.58 |

For $100\ \mathrm{m}$ of relief at $\rho = 2670\ \mathrm{kg\,m^{-3}}$ the free-air
term is $+30.79\ \mathrm{mGal}$, the slab term is $-11.20\ \mathrm{mGal}$, and the
net is $+19.59\ \mathrm{mGal}$. **A $100\ \mathrm{m}$ terrain step leaves a
$20\ \mathrm{mGal}$ residual, fifty times the amplitude of the target in §2.**
Levelling to $0.02\ \mathrm{mGal}$ therefore requires station heights accurate to
about $1\ \mathrm{mm}$ in the free-air term alone, or — in practice — a terrain
correction and a consistent reduction density, which is why gravity surveys live or
die on their reducers.

## 5. The residual is a choice, not a measurement

A gravity map is the sum of the target anomaly and everything else. Something must
be subtracted, and that something is a fitted model. Using a SYNTHETIC cylinder
anomaly ($R = 120\ \mathrm{m}$, $z = 250\ \mathrm{m}$,
$\Delta\rho = 600\ \mathrm{kg\,m^{-3}}$) plus a linear regional and $0.02\ \mathrm{mGal}$
noise:

| regional order | residual peak (mGal) | half-width (m) | implied depth (m) |
|---|---|---|---|
| 0 (constant) | 17.8320 | undefined | undefined |
| 1 (linear) | 1.3315 | 199.7 | 199.7 |
| 2 (quadratic) | 1.1792 | 191.5 | 191.5 |
| 3 (cubic) | 1.1792 | 191.5 | 191.5 |

The residual amplitude moves by $13\%$ and the implied depth by $8\ \mathrm{m}$
between two defensible choices, and with a constant regional **no depth can be
extracted at all** because the residual has no closed maximum (the linear regional
survives the subtraction and dominates the profile).

Two rules follow, and they are reporting rules rather than physics:

1. **A quoted depth must be accompanied by the regional model** that produced the
   residual, in the same way a reserve must be accompanied by its price deck.
2. **Choose the regional from independent information** — a wider survey, a
   regional gravity model, or the requirement that the residual be zero outside
   the anomalous area — and not from the polynomial order that gives the
   prettiest anomaly.

## 6. The excess-mass invariant

### 6.1 Derivation for a 2-D body

Take Gauss's theorem for the gravitational field,
$\oint \mathbf{g}\cdot\mathrm{d}\mathbf{A} = -4\pi G M_{\text{enc}}$, and apply it
to the half-space above the ground with the observation plane as the capping
surface. For a 2-D body the flux through the plane per unit strike length gives

$$\int_{-\infty}^{\infty}\Delta g(x)\,\mathrm{d}x = 2\pi G\lambda
\;\Longrightarrow\;
\boxed{\;\lambda = \frac{1}{2\pi G}\int_{-\infty}^{\infty}\Delta g(x)\,
\mathrm{d}x\;}$$

where $\lambda$ is the **mass per unit length**. Nothing in this expression
contains the shape or the depth: it recovers the excess mass directly from the
profile, provided the anomaly is isolated and the regional is correctly removed.

*Numerical check.* The SYNTHETIC cylinder has
$\lambda = \pi R^{2}\Delta\rho = \pi(120)^{2}(600) = 2.714336\times10^{7}\
\mathrm{kg\,m^{-1}}$. The demonstration integrates the profile over growing
windows:

| window (km) | $\int \Delta g\,\mathrm{d}x$ (mGal m) | recovered $\lambda$ (kg m⁻¹) | ratio to true |
|---|---|---|---|
| ±0.5 | 802.28 | 1.9131×10⁷ | 0.7048 |
| ±1.0 | 960.75 | 2.2910×10⁷ | 0.8440 |
| ±2.0 | 1048.17 | 2.4995×10⁷ | 0.9208 |
| ±4.0 | 1093.05 | 2.6065×10⁷ | 0.9603 |

The recovered mass converges slowly because the $1/z$ tail decays slowly: a
window of only $5$ times the depth recovers $70\%$ of the mass. **The invariant is
exact but the integral is not convergeable in practice at the precision one would
like** — and the missing $4\%$ at $\pm4\ \mathrm{km}$ is measured, not assumed.

The efficiency of a truncated window follows in closed form from the same integral:

$$\frac{\lambda_{\text{rec}}}{\lambda}
= \frac{1}{2\pi G\lambda}\int_{-X}^{X}\frac{2G\lambda z}{x^{2}+z^{2}}
\,\mathrm{d}x = \frac{2}{\pi}\arctan\!\left(\frac{X}{z}\right).$$

The demonstration's measurements confirm it: $X/z = 4$ gives
$(2/\pi)\arctan 4 = 0.84404$ against a measured $0.8440$; $X/z = 8$ gives
$0.92083$ against $0.9208$; $X/z = 16$ gives $0.96026$ against $0.9603$. **So the
correction is not a fudge factor but a formula**, and it can be inverted to choose
the window: recovering $95\%$ of the mass requires
$X/z = \tan(0.95\pi/2) = 12.7$.

### 6.2 Why a profile is not enough for a 3-D body

For a 3-D body the same argument requires an integral over the *plane*:

$$\iint_{\text{plane}}\Delta g\,\mathrm{d}A = 2\pi G M .$$

A single profile does not provide it. Integrating the sphere's profile instead
gives

$$\int_{-\infty}^{\infty}\Delta g_{\text{sphere}}(x)\,\mathrm{d}x
= \frac{4}{3}\pi G\Delta\rho R^{3}\!\cdot\! z\!\cdot\! \frac{2}{z^{2}}
= \frac{2GM}{z},$$

so a profile returns $M/z$, not $M$: **the old mass–depth trade-off**. The
demonstration verifies both: the numerical sphere integral converges to
$231.44\ \mathrm{mGal\,m}$ against the analytic $2GM/z = 231.89\
\mathrm{mGal\,m}$ (ratio $0.9981$ at $\pm4\ \mathrm{km}$), while the 2-D cylinder
integral gives a true mass.

This is the fundamental difference from
[11-02-02 Magnetics](02-magnetics-for-minerals.md): gravity's shape-free
information exists for 2-D bodies from a profile and for 3-D bodies only from a
map. **The third dimension has to be measured, not estimated.**

## 7. Worked example — a chromite target

A SYNTHETIC chromite body is modelled as a horizontal cylinder of strike length
$L = 3\ \mathrm{km}$, radius $R = 90\ \mathrm{m}$, axis at $z = 180\ \mathrm{m}$,
with $\Delta\rho = 800\ \mathrm{kg\,m^{-3}}$ in a host of
$2670\ \mathrm{kg\,m^{-3}}$.

1. **Excess mass per unit length:**
   $\lambda = \pi(90)^{2}(800) = 2.036\times10^{7}\ \mathrm{kg\,m^{-1}}$.
2. **Peak anomaly (2-D formula):**
   $\Delta g(0) = 2G\lambda/z = 2(6.6743\times10^{-11})(2.036\times10^{7})/180
   = 1.510\times10^{-5}\ \mathrm{m\,s^{-2}} = 1.510\ \mathrm{mGal}$.
3. **Finite strike length.** With $L/z = 3000/180 = 16.7$, the finite-line
   correction from §1.2 lies between the demonstration's values at $L/z = 10$
   ($2.2\%$ low) and $L/z = 25$ ($0.3\%$ low), so the 2-D formula understates the
   anomaly by roughly $1\%$ — about $0.015\ \mathrm{mGal}$ at this amplitude.
4. **Depth from the half-width.** The measured $x_{1/2} = 179\ \mathrm{m}$ gives
   $z = 179\ \mathrm{m}$ directly (the rule is exact), a $0.6\%$ error entirely
   attributable to picking the half-maximum on a sampled profile.
5. **Depth from the excess mass instead.** $\lambda$ is recovered from a
   $\pm1\ \mathrm{km}$ window with the $84.4\%$ efficiency measured in §6.1, i.e.
   $\lambda_{\text{rec}} = 0.844\lambda$, so the mass estimate must be divided by
   the window's efficiency or a wider window used. Reporting the raw integral as
   the mass would understate it by $16\%$.
6. **The honest statement.** "A body whose excess mass per unit length is between
   $1.7\times10^{7}$ and $2.4\times10^{7}\ \mathrm{kg\,m^{-1}}$ (the range spans
   the window-efficiency correction), with its axis $179\pm5\ \mathrm{m}$ below
   the datum, **if** the density contrast is $800\ \mathrm{kg\,m^{-3}}$ and
   **if** the body is effectively 2-D over the profile." Both conditions are
   assumptions about the rock and the shape, not statements the profile can check:
   a sphere with radius $R = \sqrt{\lambda/(\pi\Delta\rho)}$ would fit the same
   amplitude at a different depth, and one profile cannot separate the two.

## 8. Assumptions and regime of validity

1. **Known density contrast.** The depth from the half-width is independent of
   $\Delta\rho$ for the cylinder (the rule is exact), but the *mass* and any
   radius derived from it are directly proportional to it.
2. **Two-dimensional geometry.** The cylinder formula requires a strike length
   much greater than the depth; §1.2 gives the demonstration's measure of the
   error when it is not.
3. **Uniform density.** A weathered or altered carapace, or a density contrast
   that varies with depth, changes both the shape and the amplitude.
4. **A correct regional.** §5 quantifies the consequence of getting it wrong; it
   is the largest error source in the lesson and the least discussed.
5. **An isolated anomaly.** The half-width rule and the excess-mass integral both
   assume no overlapping bodies. Two close bodies produce a merged profile whose
   half-width implies an over-deep single body.
6. **Accurate heights and a consistent reduction density.** §4: $100\ \mathrm{m}$
   of relief is $20\ \mathrm{mGal}$ net, so a target of $0.5\ \mathrm{mGal}$
   demands sub-decimetre height control or a full terrain correction.
7. **Terrain (topographic) correction omitted here.** Real surveys need it, and
   its magnitude scales with the roughness of the ground, not with the size of the
   body.
8. **No isostatic or deep-crustal contribution inside the residual.** Long
   wavelengths must be removed by a regional with a physical basis, not by a
   polynomial.
9. **All numbers SYNTHETIC**, and the equivalence of "excess mass" to ore
   tonnage is a *modelling* claim: a gravity anomaly gives mass contrast, never
   grade.

## 9. Units and dimensional checks

| Quantity | Unit | Check |
|---|---|---|
| $\Delta\rho$ | kg m⁻³ |  |
| $\lambda = \pi R^{2}\Delta\rho$ | kg m⁻¹ | m² × kg m⁻³ ✔ |
| $2G\lambda/z$ | m s⁻² | m³ kg⁻¹ s⁻² × kg m⁻¹ / m ✔ |
| $\int\Delta g\,\mathrm{d}x$ | m² s⁻² (report mGal m) | m s⁻² × m ✔ |
| $\lambda$ from the integral | kg m⁻¹ | $\mathrm{m^{2}s^{-2}}/(\mathrm{m^{3}kg^{-1}s^{-2}}) = \mathrm{kg\,m^{-1}}$ ✔ |
| slab coefficient $2\pi G\rho$ | s⁻² | m³ kg⁻¹ s⁻² × kg m⁻³ ✔; × m gives m s⁻² ✔ |
| free-air $2g/a$ | s⁻² | m s⁻² / m ✔ |

Two checks catch most errors. First, the **slab coefficient must be positive and
about $0.1\ \mathrm{mGal\,m^{-1}}$** at crustal densities: an answer ten times
larger usually means $\rho$ was used in g cm⁻³ instead of kg m⁻³. Second, the
**free-air gradient must be about $0.31\ \mathrm{mGal\,m^{-1}}$**: an error of
$\pi$ or of $2$ there is the commonest arithmetic slip in reduction work.

## 10. Exercises

Full sets with worked solutions:
[`exercises/03-gravity-for-minerals-exercises.md`](exercises/03-gravity-for-minerals-exercises.md)
and
[`exercises/03-gravity-for-minerals-solutions.md`](exercises/03-gravity-for-minerals-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC body is modelled as an infinite horizontal cylinder of radius
> $110\ \mathrm{m}$ with its axis at $240\ \mathrm{m}$, in a host of
> $2700\ \mathrm{kg\,m^{-3}}$, with a density contrast of $700\
> \mathrm{kg\,m^{-3}}$. **(a)** Compute the excess mass per unit length and the
> peak anomaly. **(b)** Compute the expected half-width at half-maximum and state
> what the rule gives if the body were actually a sphere. **(c)** Compute the
> free-air and Bouguer corrections for $150\ \mathrm{m}$ of relief at the host
> density, and the net. **(d)** Compute the mass per unit length you would recover
> from a profile integrated over $\pm1.5\ \mathrm{km}$, using the window
> efficiency measured in the lesson. **(e)** State which two assumptions your
> answer depends on most.

A worked version is in the
[solutions](exercises/03-gravity-for-minerals-solutions.md).

## Common pitfalls

1. **Applying a sphere rule to a 2-D anomaly.** A measured $+30.5\%$ depth bias in
   this lesson's model, with perfect data.
2. **Reporting a depth without the regional model.** The residual is defined by
   subtraction from a fitted model.
3. **Integrating the anomaly over a small window and calling it the mass.** A
   $1/z$ tail keeps $30\%$ of the mass outside $\pm0.5\ \mathrm{km}$ at
   $z = 0.2\ \mathrm{km}$.
4. **Using $\rho$ in g cm⁻³.** The slab coefficient is then $1000\times$ wrong.
5. **Quoting a radius from a profile.** Radius and strike length trade off; only a
   map breaks it.
6. **Ignoring terrain.** $100\ \mathrm{m}$ of relief is a $20\ \mathrm{mGal}$
   effect against a $0.5\ \mathrm{mGal}$ target.
7. **Treating an excess mass as ore tonnage.** It is a *mass contrast*, and it is
   proportional to the assumed $\Delta\rho$.

## Related modules

- [11-02-02 Magnetics for IOCG, Porphyry and Magmatic Sulphides](02-magnetics-for-minerals.md)
  — the same shape-versus-amplitude logic, with a direction problem added.
- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where density sits in the signature vector.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](07-multi-method-targeting.md)
  — combining gravity with magnetics to separate dense-magnetic from dense-only.
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md)
  — the general treatment, including inversion and derivative filters.
