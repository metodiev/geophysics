---
id: 07-01-01
title: "Newtonian Gravitation, Field and Acceleration"
level: intermediate
prereqs: ["02-02-02", "02-08-01", "01-06-04"]
tags: [gravity, geodesy, newtonian-gravitation, potential-theory, field, superposition]
---

# Newtonian Gravitation, Field and Acceleration

**All models and data in this module are SYNTHETIC.** The masses, radii and
station geometries used here are chosen teaching values. Nothing in this module
is a measured gravity survey, and no station, dataset or published number is
reproduced. The only exact quantities quoted are standard constants, stated with
their units as they are used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the gravitational field $\mathbf{g}$ of a point mass from Newton's
   law of universal gravitation, and state its direction and inverse-square
   magnitude with units.
2. **Compute** the superposition of several point masses as a vector sum, and
   **explain** why a measured zero can be as informative as a measured value.
3. **Derive** the shell theorem from the symmetry of the problem, and
   **distinguish** what the theorem is exact for (a continuum shell) from what a
   finite numerical point set can show (a limit, approached as $N$ grows).
4. **Compute** the vertical attraction of a buried sphere, **measure** its
   half-width, and **state** why that half-width fixes the depth but not the
   radius.
5. **Convert** gravity values among $\mathrm{m\,s^{-2}}$, Gal, mGal and µGal, and
   **justify** the conversion factors from the exact definitions.
6. **Derive** the vertical gradient $\mathrm{d}g/\mathrm{d}r = -2g/r$ and
   **quantify** the free-air correction it predicts in $\mathrm{mGal\,m^{-1}}$.
7. **State** which parts of the observed field are the whole-Earth signal, which
   are anomalies, and why the separation is a modelling choice rather than a
   measurement.

## Prerequisites

- [02-02-02 Newton's Laws and Free-Body Analysis](../../02-physics/02-classical-mechanics/02-newtons-laws.md)
  — force, acceleration, and the vector statement of the second law that gravity
  obeys.
- [02-08-01 The Gravitational Potential](../../02-physics/08-potential-theory/01-gravitational-potential.md)
  — the scalar function whose gradient is the field, used throughout this
  module.
- [01-06-04 Divergence and Curl](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md)
  — the vector operators used to write the field compactly and to state Gauss's
  law.
- [05-01-01 Physical Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)
  — the habit of asking what contrast a measurement is really detecting.

## 1. Why gravity is the honest measurement

A seismometer hears a wave that has already travelled through the Earth; a
magnetometer measures a field that is generated in a rotating liquid core; a
gravity meter measures a number that is available anywhere, with no source
required. That apparent simplicity is exactly what makes the method instructive,
because everything interesting has to be taken out of the reading before it can
be interpreted.

At a station, the measured acceleration $\mathbf{g}$ is the vector sum of the
attraction of every element of the Earth, plus the centrifugal effect of the
Earth's rotation, plus the attraction of the Moon and the Sun (the solid Earth
tides), plus the attraction of the atmosphere and oceans, plus the instrumental
response. What a geophysicist wants is the part caused by the *local* density
distribution — a buried target, an intrusion, a cavity, a thinning crust. The
whole discipline of gravity surveying is the craft of removing the known parts
without removing the wanted part, and that craft begins with the exact field of a
known mass.

Two features of gravity shape everything that follows.

- **The field is a vector, but surveys usually measure one component.** A
  relative meter measures a *difference* in the vertical component between two
  places, so the horizontal component of an anomalous field is usually invisible.
  This is a real loss of information, not a detail: it is why gravity
  interpretation is so non-unique.
- **Gravity is additive.** There is no self-interaction and no screening, so the
  field of a body is the sum of the fields of its parts. That makes the forward
  problem easy and the inverse problem hard, which is the reverse of the usual
  situation in geophysics, and is the reason modelling in gravity is cheap and
  interpretation is not.

## 2. Definitions

### 2.1 Gravitational field and acceleration

The gravitational force on a test mass $m$ at position $\mathbf{r}$ due to a
source with mass $M$ at the origin is

$$\mathbf{F}(\mathbf{r}) = -\,G\frac{M\,m}{r^{2}}\,\hat{\mathbf{r}},
\qquad r = \left|\mathbf{r}\right|,$$

with the universal gravitational constant

$$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$$

and $\hat{\mathbf{r}}$ the unit vector from the source to the test mass. Dividing
by the test mass gives the **gravitational field**, also called the gravitational
acceleration:

$$\boxed{\;\mathbf{g}(\mathbf{r}) = -\,G\frac{M}{r^{2}}\,\hat{\mathbf{r}}.\;}$$

The field has units of acceleration, $\mathrm{m\,s^{-2}}$, and that is what a
gravimeter measures. The word "acceleration" is literal: a freely falling test
mass has no proper acceleration, so a gravimeter at rest on the ground measures
the *support* acceleration needed to hold it, which equals $-\mathbf{g}$ in
magnitude. This is worth stating precisely once, because it is a common source of
sign confusion: a gravimeter measures the upward force per unit mass required to
keep the sensor stationary, whose magnitude is $g$.

### 2.2 Gravity units

Because the interesting part of $g$ is roughly $10^{-6}$ of the total, the
centimetre–gram–second unit is used instead of the SI unit:

| Unit | Definition | In SI |
|---|---|---|
| 1 Gal | $1\ \mathrm{cm\,s^{-2}}$ | $10^{-2}\ \mathrm{m\,s^{-2}}$ (exact) |
| 1 mGal | $10^{-3}$ Gal | $10^{-5}\ \mathrm{m\,s^{-2}}$ (exact) |
| 1 µGal | $10^{-3}$ mGal | $10^{-8}\ \mathrm{m\,s^{-2}}$ (exact) |

A modern relative meter resolves a few microgal, which is $10^{-8}$ of the
Earth's field: a part in $10^{8}$. The engineering that achieves this is module
[02](../02-gravity-instruments-and-surveys/README.md); here we only need the
units. The demonstration computes the field of a spherical model Earth as
$9.820250\ \mathrm{m\,s^{-2}} = 982025.05\ \mathrm{mGal}$, so
$1\ \mathrm{mGal}$ is $1.018\times10^{-6}$ of it — about one part per billion.

### 2.3 The acceleration due to a distribution

For a continuous mass density $\rho(\mathbf{r}')$, superposition promotes the sum
to an integral:

$$\mathbf{g}(\mathbf{r}) = -G\int_{V}\rho(\mathbf{r}')
\;\frac{\mathbf{r}-\mathbf{r}'}{\left|\mathbf{r}-\mathbf{r}'\right|^{3}}\;
\mathrm{d}^{3}r'.$$

The integral is singular-looking but converges for any bounded density; the
$1/r^{2}$ decay of the integrand in three dimensions is marginal, which is why
gravity is a long-range force with no useful decay length.

## 3. Superposition and the vector nature of the field

Superposition follows immediately from the linearity of the integral: the field
of two bodies is the vector sum of their fields. The demonstration makes three
points with numbers, using two point masses $m$ at $x = \mp 2000\ \mathrm{m}$:

- With **equal** masses $m = 10^{12}\ \mathrm{kg}$, the field at the midpoint is
  exactly zero: $g_x = 0.000000\times10^{0}\ \mathrm{m\,s^{-2}}$. Each attraction
  is $G m / r^{2}$ in magnitude, but their directions are opposite. At
  $x = +1000\ \mathrm{m}$ the sum is no longer zero:
  $g_x = +5.932711\times10^{-5}\ \mathrm{m\,s^{-2}}$.
- With **unequal** masses $m_1 = 10^{12}\ \mathrm{kg}$, $m_2 = 3\times10^{12}\
  \mathrm{kg}$, the same midpoint is not a null:
  $g_x = +3.337150\times10^{-5}\ \mathrm{m\,s^{-2}}$. The cancellation was a
  property of the symmetry, not of the geometry alone.
- Off the symmetry axis, at $(0,\,1500,\,0)\ \mathrm{m}$, the field of the
  unequal pair is $\left|\mathbf{g}\right| = 3.0803\ \mathrm{mGal}$ and points at
  $-56.31^\circ$ from $+x$: it tilts towards the nearer, heavier mass.

The lesson generalises: a gravity null is a constraint, and the *direction* of
the field carries information that the magnitude alone does not. Because a
relative gravimeter measures only the vertical component, that extra information
is thrown away at the instrument, and it has to be recovered by modelling.

## 4. The shell theorem, derived and checked

**Statement.** A spherically symmetric shell of total mass $M$ and radius $R$
produces (i) exactly zero field at every interior point and (ii) outside the shell
a field identical to that of a point mass $M$ at the centre.

**Derivation (outside).** Place the field point at distance $r > R$ from the
centre and let a ring of the shell at polar angle $\theta$ subtend
$\mathrm{d}\theta$. Write the shell's surface density
$\sigma = M/(4\pi R^{2})$. The ring has area $2\pi R^{2}\sin\theta\,
\mathrm{d}\theta$ and mass $\mathrm{d}M = 2\pi R^{2}\sigma\sin\theta\,
\mathrm{d}\theta$; every element of it is at the same distance
$s = \sqrt{r^{2} + R^{2} - 2rR\cos\theta}$ from the field point, so their
transverse contributions cancel by symmetry and only the axial part survives. The
axial projection factor is $(r - R\cos\theta)/s$, giving

$$\mathrm{d}g = G\,\frac{\mathrm{d}M}{s^{2}}\cdot\frac{r - R\cos\theta}{s}.$$

Substituting $s\,\mathrm{d}s = rR\sin\theta\,\mathrm{d}\theta$ turns the integral
into an elementary one:

$$g = \frac{G M}{2 r^{2} R}\int_{r-R}^{r+R}
\left(1 + \frac{r^{2}-R^{2}}{s^{2}}\right)\mathrm{d}s
= \frac{GM}{r^{2}}.$$

**Derivation (inside).** The same integral with $r < R$ runs over
$s \in [R-r,\,R+r]$, and the two terms cancel exactly:

$$g = \frac{GM}{2r^{2}R}\Bigg[
\underbrace{\int_{R-r}^{R+r}\mathrm{d}s}_{2r}
+ \left(r^{2}-R^{2}\right)
\underbrace{\int_{R-r}^{R+r}\frac{\mathrm{d}s}{s^{2}}}_{
\frac{1}{R-r}-\frac{1}{R+r}=\frac{2r}{R^{2}-r^{2}}}
\Bigg]
= \frac{GM}{2r^{2}R}\left(2r - 2r\right) = 0 .$$

Physically: the two cones of equal solid angle from the field point intercept
mass elements whose masses are proportional to $s_1^{2}$ and $s_2^{2}$, and whose
fields fall as $s^{-2}$, so every pair cancels. That is the whole content of the
theorem, and it is why the result is independent of how mass is distributed with
radius.

**Numerical check (SYNTHETIC).** The demonstration replaces the shell by $N$
equal point masses on a Fibonacci spiral. The interior field, expressed as a
fraction of $GM/R^{2}$, is

| $N$ | interior $\left|\mathbf{g}\right| / (GM/R^{2})$ | exterior relative error |
|---|---|---|
| 500 | $6.59\times10^{-5}$ | $-7.41\times10^{-6}$ |
| 2000 | $8.47\times10^{-6}$ | $-5.79\times10^{-7}$ |
| 8000 | $8.59\times10^{-7}$ | $+2.87\times10^{-7}$ |

The interior residual is **not** round-off: it is the discretisation error of
representing a continuum shell by a finite point set, and it falls roughly as
$N^{-1}$. The theorem is a statement about the limit $N\to\infty$, and the table
shows the limit being approached. Reporting "zero" from a finite computation
without this caveat would be a numerical false claim.

**Why it matters.** The shell theorem is the reason a spherically symmetric Earth
has a field that depends only on the mass *inside* the radius of interest. It
licenses the whole hierarchy of reference models — sphere, ellipsoid, layered
sphere — which later lessons use to define what an anomaly is.

## 5. The field of a body that is not the whole Earth

An anomaly is the difference between the observed field and the field of an
assumed reference model. The simplest anomaly is a buried sphere of density
contrast $\Delta\rho$ and radius $a$, whose centre is at depth $z$ below the
station. Outside the sphere the field is that of a point mass
$M = \tfrac{4}{3}\pi a^{3}\Delta\rho$ at the centre, and the measured vertical
component at horizontal offset $x$ is

$$g_{z}(x) = G M\,\frac{z}{\left(x^{2}+z^{2}\right)^{3/2}}.$$

**Peak value.** At $x = 0$, $g_{z}(0) = GM/z^{2}$.

**Half-width.** Setting $g_z(x) = g_z(0)/2$ gives
$\left(x^{2}+z^{2}\right)^{3/2} = 2z^{3}$, hence

$$x_{1/2} = z\sqrt{2^{2/3}-1} = 0.7664\,z
\qquad\Longleftrightarrow\qquad z = 1.3048\,x_{1/2}.$$

**Non-uniqueness, stated at once.** The *shape* of the profile, through
$x_{1/2}$, fixes $z$. The *amplitude* fixes the product $a^{3}\Delta\rho$. A deep
large body and a shallow small one can have the same half-width and the same peak
amplitude, so the data determine a curve of compatible models, not a body. This
is the theme of the whole folder and it is already visible in the simplest
possible target.

**Numerical check (SYNTHETIC).** A sphere of radius $500\ \mathrm{m}$, density
$2670\ \mathrm{kg\,m^{-3}}$ and centre depth $800\ \mathrm{m}$ has mass
$1.398009\times10^{12}\ \mathrm{kg}$ and produces

| $x$ (m) | 0 | 200 | 400 | 600 | 800 | 1200 | 1600 |
|---|---|---|---|---|---|---|---|
| $g_z$ (mGal) | 14.5793 | 13.3120 | 10.4321 | 7.4646 | 5.1545 | 2.4883 | 1.3040 |

The measured half-width is $615.1\ \mathrm{m}$, giving
$z/x_{1/2} = 1.3005$ against the closed-form $1.3048$ — agreement to $0.3\%$,
the residual coming from linear interpolation of a tabulated curve. If the
density contrast were halved, the peak would halve and the half-width would not
change: shape gives depth, amplitude gives mass.

## 6. The vertical gradient, and the free-air correction

A gravimeter measures at a point on a curved, rotating, non-spherical Earth. The
first thing to remove is the effect of *where* the station sits on that
reference body. Consider only the spherically symmetric part: differentiating
$g = GM/r^{2}$ gives

$$\frac{\mathrm{d}g}{\mathrm{d}r} = -\frac{2GM}{r^{3}} = -\frac{2g}{r}.$$

**Numerical check (SYNTHETIC sphere).** With $g = 9.820250\ \mathrm{m\,s^{-2}}$
at $r = 6371\ \mathrm{km}$:

$$\frac{\mathrm{d}g}{\mathrm{d}r} = -\frac{2\left(9.820250\right)}{6.371\times10^{6}}
= -3.082797\times10^{-6}\ \mathrm{s^{-2}}
= -0.308280\ \mathrm{mGal\,m^{-1}}.$$

The **free-air correction** is the negative of this, $+0.3083\ \mathrm{mGal}$ per
metre of elevation, so a station $1000\ \mathrm{m}$ higher reads
$308.280\ \mathrm{mGal}$ lower. For $10$, $100$ and $1000\ \mathrm{m}$ the values
are $3.083$, $30.828$ and $308.280\ \mathrm{mGal}$.

The coefficient is quoted elsewhere to three decimals as $0.3086\
\mathrm{mGal\,m^{-1}}$; the difference in the third decimal is real physics, not
round-off. On the ellipsoid the gradient varies with latitude, and it also has a
contribution from the Earth's curvature and flattening. Lesson
[03](03-normal-gravity.md) derives the exact normal-gravity gradient, and lesson
[04](04-gravity-reduction.md) uses it as the free-air correction. The point of
deriving it here from $2g/r$ is that the number is not a magic constant: it is a
consequence of the inverse-square law.

## 7. Worked example — from geometry to a predicted anomaly

**Problem.** A SYNTHETIC survey crosses a spherical body of radius
$250\ \mathrm{m}$ and density contrast $+400\ \mathrm{kg\,m^{-3}}$, centre depth
$400\ \mathrm{m}$. Compute the peak anomaly in mGal and the expected half-width.
State one thing the data cannot determine.

1. Volume: $V = \tfrac{4}{3}\pi\left(250\right)^{3} = 6.54498\times10^{7}\
   \mathrm{m^{3}}$.
2. Mass: $M = \Delta\rho V = 400 \times 6.54498\times10^{7} =
   2.61799\times10^{10}\ \mathrm{kg}$.
3. Peak: $g_{z}(0) = GM/z^{2} = 6.67430\times10^{-11}\times
   2.61799\times10^{10}/(400)^{2} = 1.09208\times10^{-5}\ \mathrm{m\,s^{-2}}$.
4. In mGal: $1.09208\times10^{-5} \times 10^{5} = 1.09208\ \mathrm{mGal}$.
5. Half-width: $x_{1/2} = 0.7664 \times 400 = 306.56\ \mathrm{m}$, so the
   anomaly falls to $0.54604\ \mathrm{mGal}$ at about $307\ \mathrm{m}$ from the
   centre.
6. What is not determined: the pair $(a,\Delta\rho)$ is fixed only through
   $a^{3}\Delta\rho$. Radius $300\ \mathrm{m}$ with
   $\Delta\rho = 231.48\ \mathrm{kg\,m^{-3}}$ produces the same curve as radius
   $250\ \mathrm{m}$ with $\Delta\rho = 400\ \mathrm{kg\,m^{-3}}$, at the same
   depth. Depth is determined; size and contrast are traded.

## 8. Assumptions and regime of validity

The derivation of the field of a point mass and the shell theorem assumes:

1. **Newtonian gravity.** Post-Newtonian corrections are of order
   $GM/(rc^{2}) \approx 7\times10^{-10}$ at the Earth's surface, five orders of
   magnitude below a microgal; they are negligible for surveying and are treated
   only in relativistic geodesy.
2. **Instantaneous propagation.** Newtonian gravity has no propagation delay. The
   observational consequence — gravitational radiation — is irrelevant for
   terrestrial gravity and matters only for binary pulsar timing.
3. **The source is static.** A moving or deforming source changes the field; for
   the survey-relevant frequencies the changes are the time-variable gravity
   signal of module [05](../05-satellite-gravimetry/README.md), not a
   correction to the inverse-square law.
4. **Isolated masses and vacuum between them.** The value of $G$ in the
   laboratory is affected by surrounding mass, and the measured field at a
   station includes everything. "The field of a body" is always a modelled
   difference, never a measured quantity.
5. **Superposition is exact, but the reference model is not.** The arithmetic of
   superposition is exact; the *separation* of an anomaly from the whole-Earth
   field depends on the reference model chosen. A different reference gives a
   different anomaly from the same data.
6. **Point-mass approximation for compact bodies.** For a *uniform sphere* the
   exterior field is exactly that of a point mass at the centre, at any distance
   and for any radius, by the shell theorem applied shell by shell. The
   idealisation therefore fails only when the body is **not** spherical: for a
   flattened spheroid the leading correction is a quadrupole term of relative
   size of order $(\text{flattening})\times(a/z)^{2}$, which grows as the body is
   approached. The tabulated values in Section 5 are values of the point-mass
   model, and they are labelled as such.

## 9. Python demonstration

`code/newtonian_gravity_demo.py` computes everything above and prints labelled
results with units:

1. the field of a point mass at $r = R_{\text{mean}}$ and $2R_{\text{mean}}$, and
   the measured ratio $4.000000$;
2. superposition for equal and unequal pairs, including the exact null at the
   midpoint of an equal pair;
3. the shell theorem for $N = 500,\,2000,\,8000$ points, with the interior
   residual quoted as a fraction of $GM/R^{2}$;
4. the buried-sphere profile, peak $14.5793\ \mathrm{mGal}$, half-width
   $615.1\ \mathrm{m}$ and the measured ratio $z/x_{1/2} = 1.3005$;
5. the unit conversions, and $1\ \mathrm{mGal}$ as $1.018\times10^{-6}$ of $g$;
6. the vertical gradient $-0.308280\ \mathrm{mGal\,m^{-1}}$ and the free-air
   correction at $10$, $100$ and $1000\ \mathrm{m}$ of elevation.

The demonstration is print-only, uses a fixed seed, and needs no network.

Worked exercises with full numerical solutions are in
[`exercises/01-newtonian-gravity-exercises.md`](exercises/01-newtonian-gravity-exercises.md)
and
[`exercises/01-newtonian-gravity-solutions.md`](exercises/01-newtonian-gravity-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC relative survey measures a $12.0\ \mathrm{mGal}$ peak over a
> suspected sphere at a half-width of $500\ \mathrm{m}$. **(a)** Estimate the
> centre depth. **(b)** Given $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, estimate
> the radius. **(c)** State the one-line reason the radius is the least reliable
> of the three numbers. **(d)** A station $250\ \mathrm{m}$ above the target
> reads how much lower, from the free-air gradient alone?

A worked version of (a)–(c) is in the
[solutions](exercises/01-newtonian-gravity-solutions.md); (d) uses the
$0.3083\ \mathrm{mGal\,m^{-1}}$ measured in the demonstration.

## Common pitfalls

1. **Treating $g$ as a scalar.** It is a vector. A measured null can be a sum of
   large vectors, and the horizontal component is usually unmeasured.
2. **Reading a "zero" from a finite sum.** The interior shell field is exactly
   zero only for a continuum; the residual from $N$ points is a discretisation
   error that must be quoted.
3. **Forgetting which mass matters.** The field depends on the mass *inside* the
   radius for a spherical body, so adding mass outside changes nothing.
4. **Quoting a constant without provenance.** $0.3083\ \mathrm{mGal\,m^{-1}}$
   came from $2g/r$; if $g$ or $r$ changes, the coefficient changes.
5. **Believing the point-mass idealisation for a nearby body.** The
   approximation fails as the observation distance approaches the body's size,
   and the failure is quantitative, not stylistic.
6. **Mixing units across a paragraph.** $\mathrm{m\,s^{-2}}$, mGal and µGal are
   all in use; a factor of $10^{5}$ error usually means a conversion was skipped.

## Related modules

- [Module 01 — Gravity Fundamentals](README.md) — the module you are reading;
  the next lesson derives the potential and the geoid, and lesson 04 turns the
  gradient above into a working correction.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  Laplace's and Poisson's equations, the mathematical home of the material in
  lessons 02 and 03.
- [02-02 Classical Mechanics](../../02-physics/02-classical-mechanics/README.md) —
  forces and central-force motion.
- [05-01 What Geophysics Measures](../../05-core-geophysics/01-what-geophysics-measures/README.md) —
  property contrasts and non-uniqueness, the framing used here.
- [07-03-01 Interpreting Anomalies](../03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  where the depth rules introduced in Section 5 are developed properly.
- [Module 02 — Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the instruments that measure these numbers.
