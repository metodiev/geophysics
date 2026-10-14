---
id: 01-05-05
title: "Integration Techniques and Definite Integrals"
level: intermediate
prereqs: ["01-05-03"]
estimated_minutes: 90
tags: [calculus, integration, quadrature, accumulation]
---

# Integration Techniques and Definite Integrals

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the definite integral as a limit of Riemann sums, and state the
   fundamental theorem of calculus in both directions.
2. **Choose** between substitution, integration by parts, partial fractions and
   direct recognition, and justify the choice.
3. **Compute** physical totals — mass, moment of inertia, accumulated heat, mean
   value — by setting up the integral with its differential and its units.
4. **Apply** the trapezoidal and Simpson rules, state their error orders, and
   measure those orders numerically rather than trusting them.
5. **Verify** an integral dimensionally by checking that the integrand times the
   differential has the units of the answer.
6. **Recognise** when a signed integral cancels information, and reformulate the
   integrand instead of blaming the quadrature.

## Prerequisites

[01-05-03 Differentiation Rules and Implicit Differentiation](./03-differentiation-rules.md)
and [01-05-02 Derivatives and Rates of Change](./02-derivatives.md). Integration is
defined here as the inverse of differentiation, so fluency with derivatives is
assumed. The shell theorem quoted in Section 3.2 is proved by an integral over a
spherical shell, which is the example used in
[01-05-06](./06-improper-integrals.md).

## 1. Intuition: geophysics is measured in totals

Differentiation answers "how fast?", integration answers "how much in total?".
Almost every quantity you can name in geophysics is an integral of something else:

| Total | Integral | Differential supplies |
|---|---|---|
| Mass of a body | $\int_V \rho\,dV$ | volume element |
| Moment of inertia | $\int r^{2}\,dm$ | mass element |
| Heat flow through an area | $\int_A \mathbf{q}\cdot d\mathbf{A}$ | area element |
| Heat content of a layer | $\int_0^H c\,\rho\,T(z)\,dz$ | depth element |
| Travel time along a ray | $\int_{\text{ray}} \frac{ds}{v(s)}$ | path element |
| Gravity anomaly of a body | $\int_V \frac{G\rho\,\cos\theta}{r^{2}}\,dV$ | volume element |
| Seismic moment | $\int_A \mu\,D\,dA$ | fault-area element |
| Continuous least-squares misfit | $\int (d - F(m))^{2}\,dx$ | data-space element |

Two consequences follow immediately. First, an integral is never just a symbol:
the **differential carries the physics** ($dV$ for a volume, $dA$ for an area,
$dz$ for a depth). Second, an integral destroys information — many different
integrands produce the same total, which is the root of non-uniqueness in
inverse problems.

## 2. Precise definitions

### 2.1 Antiderivative and the indefinite integral

$F$ is an **antiderivative** of $f$ if $F' = f$. Antiderivatives are unique up to
an additive constant, which is why the indefinite integral is written

$$\int f(x)\,dx = F(x) + C .$$

### 2.2 The definite integral as a limit of Riemann sums

Partition $[a,b]$ into $n$ subintervals of width $\Delta x = (b-a)/n$ with sample
points $x_i^{*}$, and define

$$\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^{*})\,\Delta x,$$

provided the limit exists and is independent of the choices (then $f$ is
**Riemann integrable**; continuous functions are). The integral is a **signed
area**: regions below the axis count negatively.

### 2.3 The fundamental theorem of calculus

**Part 1.** If $f$ is continuous on $[a,b]$ and $F(x) = \int_a^x f(t)\,dt$, then
$F$ is differentiable and $F'(x) = f(x)$: differentiation undoes integration.

**Part 2.** If $F$ is any antiderivative of $f$ on $[a,b]$, then

$$\int_a^b f(x)\,dx = F(b) - F(a) .$$

Part 2 is the reason integrals are evaluated by finding antiderivatives rather than
by summing. It is also the reason an integral can be computed from a *rate*: if you
know the rate at which mass accumulates, the total is the difference of the
antiderivative at the endpoints.

### 2.4 Properties

$$\int_a^b (f+g) = \int_a^b f + \int_a^b g, \qquad
\int_a^b cf = c\int_a^b f, \qquad
\int_a^c f = \int_a^b f + \int_b^c f,$$
$$\int_a^b f = -\int_b^a f, \qquad
\int_a^a f = 0 .$$

### 2.5 The techniques

**Substitution.** For $x = g(u)$, $dx = g'(u)\,du$:

$$\int f(g(u))\,g'(u)\,du = \int f(x)\,dx .$$

The differential transformation is not optional bookkeeping: $dx = g'(u)\,du$ is
where the units and the Jacobian live.

**Integration by parts.** From the product rule,

$$\int u\,dv = uv - \int v\,du .$$

**Partial fractions.** A rational integrand is decomposed into terms with
elementary antiderivatives; this is the standard route for
$\int dz/(z^{2}+a^{2})$ and its relatives, which appear throughout potential-field
and diffusion problems.

**The mean value theorem for integrals.** If $f$ is continuous on $[a,b]$ there is
a point $c$ with

$$\int_a^b f = f(c)(b-a), \qquad\text{so}\qquad
\bar f = \frac{1}{b-a}\int_a^b f$$

is the **mean value** of $f$. This is what lets you replace a varying quantity by
an "effective" constant, and it is why a single borehole temperature is a poor
constraint on a curved geotherm.

### 2.6 Simple quadrature rules and their errors

For a uniform grid of $n$ panels of width $h = (b-a)/n$:

| Rule | Formula | Error |
|---|---|---|
| Midpoint | $h\sum_{i} f(x_{i+1/2})$ | $-\dfrac{(b-a)h^{2}}{24}f''(\xi)$ |
| Trapezoid | $\dfrac{h}{2}\left[f(a)+f(b)+2\sum f(x_i)\right]$ | $-\dfrac{(b-a)h^{2}}{12}f''(\xi)$ |
| Simpson | $\dfrac{h}{3}\left[f(a)+f(b)+4\!\sum_{\text{odd}}\!f+2\!\sum_{\text{even}}\!f\right]$ | $-\dfrac{(b-a)h^{4}}{180}f^{(4)}(\xi)$ |

Simpson's rule is exact for cubics, so it is *exact* for quadratic integrands —
a fact that is easy to mistake for supernaturally fast convergence, as Section 5
demonstrates.

## 3. Step-by-step derivations

### 3.1 Mass of a uniform sphere

The volume element in spherical symmetry is $dV = 4\pi r^{2}\,dr$: the volume of a
thin shell at radius $r$. Hence

$$M = \int_0^{R} \rho\,4\pi r^{2}\,dr = 4\pi\rho\,\frac{R^{3}}{3} = \frac{4}{3}\pi \rho R^{3},$$

and with $\rho = 5510\ \mathrm{kg\,m^{-3}}$, $R = 6.371\times10^{6}$ m (round
ILLUSTRATIVE values) the script obtains $M = 5.968470\times10^{24}$ kg, close to
the familiar $5.97\times10^{24}$ kg for the real, radially varying Earth.

Now the gravity *inside* a uniform sphere. By the shell theorem, a uniform
spherical shell exerts no net force on a point inside it, and acts on an external
point like a point mass at its centre. Therefore at radius $r$ only the mass inside
$r$ matters:

$$g(r) = \frac{G M(r)}{r^{2}} = \frac{G}{r^{2}}\cdot\frac{4}{3}\pi\rho r^{3}
= \frac{4}{3}\pi G \rho\, r .$$

The script evaluates this at $r = R$ and compares with $GM/R^{2}$, obtaining
`9.813727972190579` and `9.81372797219058` — the same number, as it must be, since
both expressions reduce to $GM/R^{2}$ at the surface. **Inside a uniform body,
gravity is proportional to distance from the centre**; this linearity is an
integral result, not an assumption, and it is the reason the free-air gradient and
the internal gradient have different slopes.

### 3.2 Moment of inertia, and what it tells you about the Earth

The moment of inertia about an axis through the centre is $I = \int r^{2}\,dm$ with
$dm = \rho\,4\pi r^{2}\,dr$ for the component of $r^{2}$ perpendicular to the axis
averaged over a shell, which contributes the factor $2/3$:

$$I = \frac{2}{3}\int_0^{R} r^{2}\,\rho\,4\pi r^{2}\,dr
= \frac{8\pi}{3}\rho\int_0^{R} r^{4}\,dr
= \frac{8\pi}{15}\rho R^{5}
= \frac{2}{5}MR^{2}.$$

The script confirms both the value and the factor: for the uniform model,
$I = 9.690322\times10^{37}\ \mathrm{kg\,m^{2}}$ and $I/(MR^{2}) = 0.400000$, with
the numerical quadrature agreeing with the closed form to `9.70e-12` relative.

Now replace the uniform sphere by a two-layer model: a core of radius 3480 km with
$\rho = 11000\ \mathrm{kg\,m^{-3}}$ and a mantle out to 6371 km with
$\rho = 4400\ \mathrm{kg\,m^{-3}}$ (ILLUSTRATIVE values). Summing the two shell
integrals gives $I/(MR^{2}) = 0.3449$, and the model mass
$5.9312\times10^{24}$ kg. The real Earth's value is about **0.3308**. Since
concentrating mass towards the centre lowers $I/(MR^{2})$ from the uniform value
0.4, the observed number says quantitatively that density increases with depth more
steeply than this two-step model. That single number is one of the primary
constraints on core density, and it is an *integral* constraint — it constrains a
weighted average of the density profile, not the profile itself.

### 3.3 A mean, and why it is not a profile

For a conductive layer with constant conductivity $k$ and heat flux $q$, the
geotherm is linear: $T(z) = T_0 + (q/k)z$. The mean over $0 \le z \le H$ is

$$\bar T = \frac{1}{H}\int_0^{H}\left(T_0 + \frac{q}{k}z\right)dz
= T_0 + \frac{qH}{2k} = \frac{T_0 + T(H)}{2}.$$

The script evaluates this with $q = 62.5\ \mathrm{mW\,m^{-2}}$,
$k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$, $T_0 = 10$ °C and $H = 30$ km: the
geotherm reaches 760.00 °C at 30 km and the numerical mean is `385.000000` °C,
matching $(T_0 + T(H))/2$ to all printed digits. The lesson is the *symmetry* of the
linear case: a mean can be computed from the endpoints, and consequently the
endpoints cannot distinguish a linear geotherm from any other profile with the same
mean. **An integral is a low-pass filter on a function.**

### 3.4 Accumulated heat, and the units check

Heat flow is a flux: power per unit area. Multiplying by an area gives a power, and
integrating over time gives an energy:

$$P = qA = (6.25\times10^{-2}\ \mathrm{W\,m^{-2}})(1.0\times10^{10}\ \mathrm{m^{2}})
= 6.25\times10^{8}\ \mathrm{W} = 625\ \mathrm{MW},$$

and over one year, $P \times 3.156\times10^{7}\ \mathrm{s}
= 1.9725\times10^{16}$ J $= 5.479$ TWh (dividing by $1\ \mathrm{TWh} = 3.6\times10^{15}$ J).
The dimensional check is the whole argument: $\mathrm{W\,m^{-2}\times m^{2} = W}$,
and $\mathrm{W\times s = J}$. Had the flux been quoted in mW/m² without conversion,
the power would be wrong by $10^{3}$.

### 3.5 Substitution with a physical variable: compaction

Sediment porosity often decays exponentially with depth, $\phi(z) = \phi_0 e^{-z/\lambda}$
(Athy's law). With grain density $\rho_g$ and pore-fluid density $\rho_f$,

$$\rho(z) = \rho_g - (\rho_g - \rho_f)\phi_0 e^{-z/\lambda},$$

so the mass per unit area of a column of thickness $H$ is

$$\frac{m}{A} = \int_0^{H}\rho(z)\,dz
= \rho_g H - (\rho_g - \rho_f)\phi_0\lambda\left(1 - e^{-H/\lambda}\right),$$

a closed form obtained by the substitution $u = z/\lambda$, $dz = \lambda\,du$. With
$\rho_g = 2650$, $\rho_f = 1030$, $\phi_0 = 0.5$, $\lambda = 1000$ m and
$H = 3000$ m (SYNTHETIC), the script reports an exact value of
`7180327.525378` kg/m², and the quadrature errors are:

| $n$ | trapezoid relative error | ratio | Simpson relative error | ratio |
|---|---|---|---|---|
| 8 | `1.25e-03` | — | `1.16e-05` | — |
| 16 | `3.14e-04` | 3.99 | `7.33e-07` | 15.80 |
| 32 | `7.85e-05` | 4.00 | `4.60e-08` | 15.95 |
| 64 | `1.96e-05` | 4.00 | `2.87e-09` | 15.99 |
| 128 | `4.91e-06` | 4.00 | `1.80e-10` | 16.00 |
| 256 | `1.23e-06` | 4.00 | `1.12e-11` | 16.00 |

Doubling $n$ cuts the trapezoid error by 4 and the Simpson error by 16 — the
measured signature of $O(h^{2})$ and $O(h^{4})$. The substitution that produced the
closed form is the same operation expressed analytically, and it is always worth
looking for: an exact antiderivative removes quadrature error entirely.

### 3.6 Integration by parts, and an integral you will meet again

$$\int x e^{-x}\,dx = -x e^{-x} + \int e^{-x}\,dx = -(x+1)e^{-x} + C,$$

by parts with $u = x$, $dv = e^{-x}dx$. Hence

$$\int_0^{\infty} x e^{-x}\,dx = \left[-(x+1)e^{-x}\right]_0^{\infty} = 1 .$$

This improper integral is evaluated in [01-05-06](./06-improper-integrals.md); it
appears whenever an exponential distribution is weighted by its own variable, as in
a diffusive timescale or a fission-track age. The same by-parts manipulation gives

$$\int \ln x\,dx = x\ln x - x + C,$$

by taking $u = \ln x$, $dv = dx$.

## 4. Physical interpretation

**The differential is a physical object.** Writing $\int \rho\,dr$ instead of
$\int \rho\,dV$ changes the answer from a mass-per-unit-area to a mass, and the
difference is the $4\pi r^{2}$ factor — geometry. Get in the habit of writing the
differential that carries the geometry, and check the units of the product
integrand $\times$ differential against the required answer.

**Integrals are low-pass filters.** Section 3.3 shows that a mean over an interval
retains only the average. This is why:
- the moment of inertia constrains a density *average* weighted by $r^{4}$, not a
  profile;
- the total heat flow of a region does not reveal where the heat comes from;
- gravimetric mass estimates cannot be converted into a density model without
  extra assumptions.

**Signed sums destroy information; symmetric ones double it.** The script prints
$\int_0^{\pi}\sin x\,dx = 2.000000$ and $\int_0^{2\pi}\sin x\,dx = -2.03\times10^{-16}$,
while $\int_0^{2\pi}|\sin x|\,dx = 4.000000$. If a physical total that should be
positive is coming out near zero, the integrand is wrong (or is a signed
quantity), not the quadrature. The classic instance is net mass flux: a layer can
receive and lose equal amounts, and only the absolute version answers "how much
moved".

**Order of accuracy is the cost of the computation.** Simpson's rule buys two extra
digits over the trapezoid rule for the same number of function evaluations, but it
requires the integrand to be smooth. For an integrand with a kink — a |x|
behaviour at an interface, say — Simpson's advantage degrades and you should split
the interval at the kink instead.

## 5. Python demonstration

The companion script is [`code/integration_demo.py`](./code/integration_demo.py).
It contains seven sections; each has a closed-form answer, so every quadrature
error printed is a genuine measurement.

A subtlety is worth stating before the summary table: **Simpson's rule is exact for
cubics**, so on the uniform-sphere mass integral ($4\pi\rho r^{2}$, a quadratic) it
produces the exact answer to round-off from the very first grid:

```
n             trapezoid    rel. err   ratio               Simpson    rel. err
8      6.0150987846e+24    7.81e-03     nan      5.9684701118e+24    1.80e-16
16     5.9801272800e+24    1.95e-03    4.00      5.9684701118e+24    1.80e-16
64     5.9691986848e+24    1.22e-04    4.00      5.9684701118e+24    1.80e-16
256    5.9685156476e+24    7.63e-06    4.00      5.9684701118e+24    5.40e-16
```

against the exact $M = 5.968470\times10^{24}$ kg. The trapezoid ratios are 4.00 for
every refinement, which is $O(h^{2})$; Simpson shows no convergence order at all
because there is no error left to reduce. A rule that is exact for your integrand
cannot demonstrate its order — you must test it on an integrand it cannot do
analytically, which is what Section 3.5's compaction integral does.

The remaining quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 3, moment of inertia | $I = 9.690322\times10^{37}$ kg m², $I/(MR^{2}) = 0.400000$ | closed form and quadrature agree to `9.70e-12` |
| 4, two-layer model | $I/(MR^{2}) = 0.3449$, $M = 5.9312\times10^{24}$ kg | concentrating mass raises the constraint: Earth's 0.3308 needs a steeper profile |
| 5, geotherm mean | `mean T (trapezoid) = 385.000000` = `(T0 + T(H))/2` | the mean value theorem for a linear profile |
| 6, accumulated heat | `625.00 MW`, `5.479 TWh` in one year | flux × area × time, with the units carried |
| 7, signed integral | $\int_0^{2\pi}\sin = -2.03\times10^{-16}$, $\int_0^{2\pi}\lvert\sin\rvert = 4.000000$ | cancellation is a property of the integrand |

> **Breaking exercise.** Change the compaction decay length in Section 3.5 from
> $\lambda = 1000$ m to $\lambda = 200$ m and predict, before running, whether the
> trapezoid error improves or degrades at fixed $n$, and whether the exact value
> increases or decreases. Then explain the direction of each change in terms of
> the third derivative of the integrand, which controls the truncation constant.

## 6. Exercises

Full set and worked solutions:
[`exercises/05-integration-exercises.md`](./exercises/05-integration-exercises.md)
and [`exercises/05-integration-solutions.md`](./exercises/05-integration-solutions.md).
Four to begin with:

**★1.** Evaluate: (a) $\int_0^{2}(3x^{2}-2x)\,dx$,
(b) $\int_1^{e}\frac{dx}{x}$, (c) $\int_0^{1}xe^{-x}\,dx$,
(d) $\int \frac{dz}{z^{2}+4}$.

**★2.** Check each answer in ★1 dimensionally and by differentiating.

**★★3.** A sediment column has porosity $\phi(z) = 0.55e^{-z/800}$ (SYNTHETIC),
grain density 2650 kg/m³ and fluid density 1030 kg/m³. (a) Derive the mass per unit
area to depth $H$ in closed form. (b) Evaluate it for $H = 2$ km. (c) Compute the
relative error of the trapezoid rule with $n = 10$ and compare with the $O(h^{2})$
prediction.

**★★4.** A spherical body has radius 500 m and uniform density contrast
$+250\ \mathrm{kg\,m^{-3}}$ with its surroundings. (a) Write the excess mass as an
integral and evaluate it. (b) State why the gravity anomaly of this body at 2 km
depth constrains the excess mass but not the density contrast, using the language
of Section 4.

**★★★5.** A layer has conductivity that decreases with depth,
$k(z) = k_0(1 - \beta z)$ with $z$ measured downward.
(a) Show that a *constant* upward heat flux $q$ implies a geotherm
$T(z) = T_0 - \dfrac{q}{k_0\beta}\ln(1-\beta z)$, and verify that this satisfies
$q = k(z)\,dT/dz$.
(b) Find the depth at which the temperature has risen by 100 K, first for the
variable $k(z)$ and then for a constant $k_0$ using the same $q$.
(c) Quantify the difference for $k_0 = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$\beta = 0.01\ \mathrm{km^{-1}}$, and state which assumption is doing the work.

## 7. Common mistakes

1. **Forgetting the constant of integration.** $\int f = F + C$; the constant
   matters when matching a boundary condition, and dropping it silently changes the
   physical solution.
2. **Forgetting to change the limits when substituting.** If you substitute
   $x = g(u)$ in a definite integral, the limits must become $u$-limits, or you must
   substitute back before evaluating.
3. **Omitting the differential.** $\int r^{2}\rho$ is meaningless without the
   measure; $4\pi r^{2}dr$ and $dr$ differ by the geometry of the problem.
4. **Sign errors from orientation.** $\int_a^b = -\int_b^a$. Whether depth increases
   downward or upward changes signs in heat flow and gravity gradient.
5. **Assuming symmetry that is not there.** A integrand that is odd over a symmetric
   interval integrates to zero; using that fact for an asymmetric problem produces a
   confidently wrong answer.
6. **Trusting a quadrature rule that is exact for the integrand.** See Section 5:
   Simpson on a quadratic looks perfect and teaches you nothing about Simpson.
7. **Confusing a mean with a distribution.** A total or a mean is a projection of a
   function; it does not determine the function.
8. **Ignoring the singularity at an endpoint.** Quadrature rules assume a smooth
   integrand; if the integrand blows up at an endpoint, the error converges much
   more slowly and a substitution is usually required
   ([01-05-06](./06-improper-integrals.md)).

## 8. Real-world applications

- **Heat-flow and geothermal resource assessment.** The product of a measured
  gradient and conductivity gives a flux; integrating over an area and over time
  gives extractable energy, with the arithmetic of Section 3.4.
- **Earth's moment of inertia.** The observed $I/(MR^{2}) \approx 0.3308$ is one of
  the few integral constraints available on the deep interior; it complements
  seismological travel times, which constrain velocities rather than densities. See
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md).
- **Travel-time integrals.** Travel time along a ray is $\int ds/v(s)$, and the
  linearisation of that integral about a reference model is the basis of seismic
  tomography. See [06-seismology](../../06-seismology/README.md).
- **Potential-field modelling.** The gravity or magnetic anomaly of an arbitrary
  body is a volume integral over the source; practical codes evaluate it with
  numerical quadrature over prisms or tesseroids, and their accuracy is exactly the
  quadrature question of this lesson. See
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Bouguer and terrain corrections.** Terrain corrections are numerical
  quadratures over topography; the resolution of the digital elevation model sets
  the quadrature error just as $n$ does here.
- **Continuous inverse theory.** Misfit functionals such as
  $\int (d - F(m))^{2}dx$ and their regularised variants are integrals over data and
  model spaces; discretising them is the step from continuous to discrete inverse
  theory. See [18-inverse-problems](../../18-inverse-problems/README.md).

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 13–18.
  Level: beginner upward. Riemann sums, the fundamental theorem, and the technique
  proofs.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapters 6 and 10.
  Level: beginner to intermediate. The integral as a limit of sums, done properly.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd ed.).
  Wiley.** Chapters 4 and 5. Level: beginner. Integration techniques with the
  applications attached, including moments.
- **Turcotte, D. L. & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Chapter 4. Level: intermediate. Heat-flow integrals and
  moment-of-inertia constraints.
- **Stacey, F. D. & Davis, P. M. (2008). *Physics of the Earth* (4th ed.).
  Cambridge University Press.** Chapter 1. Level: intermediate. The moment of
  inertia factor as an observational constraint.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Chapter 1. Level: advanced. Continuous inverse problems as
  integral equations.
- The SciPy documentation at <https://scipy.org> covers production quadrature
  (`scipy.integrate.quad`, adaptive and Gaussian rules). Level: intermediate. Use
  it once you understand the error behaviour of the elementary rules above.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not reproduce copyrighted text; confirm editions and
> availability through your library before citing them. Chapter references are
> indicative rather than authoritative: editions differ in numbering and content,
> so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can state both parts of the fundamental theorem of calculus and say what
      each is used for.
- [ ] I can set up a mass, moment or heat integral with the correct differential
      and verify its units.
- [ ] I can evaluate an integral by substitution and by parts, and choose the
      better technique with a reason.
- [ ] I can state the trapezoid and Simpson error orders and measure them
      numerically.
- [ ] I can derive $I = \tfrac{2}{5}MR^{2}$ for a uniform sphere and explain what
      $I/(MR^{2}) = 0.3308$ implies for the real Earth.
- [ ] I can explain why a total or a mean does not determine a distribution, with a
      geophysical instance.
- [ ] I can recognise a signed-cancellation error and reformulate the integrand.

## 11. Related lessons

- [01-05-02 Derivatives and Rates of Change](./02-derivatives.md) — the operation
  that integration inverts.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md) —
  where the quadrature error formulas come from.
- [01-05-06 Improper Integrals, Singularities and Convergence](./06-improper-integrals.md) —
  what to do when the integrand or the interval is unbounded.
- [01-06-02 Multiple Integrals and Change of Variables](../06-multivariable-calculus/02-multiple-integrals.md) —
  the several-variable version needed for volume integrals over arbitrary bodies.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../06-multivariable-calculus/03-jacobians.md) —
  why $dV = 4\pi r^{2}dr$ in spherical symmetry.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  adaptive quadrature, Gaussian rules and their practical error control.
