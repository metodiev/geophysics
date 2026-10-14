---
id: 01-05-02
title: "Derivatives and Rates of Change"
level: beginner
prereqs: ["01-05-01"]
estimated_minutes: 90
tags: [calculus, derivatives, rates-of-change, finite-differences]
---

# Derivatives and Rates of Change

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the derivative as the limit of a difference quotient, and compute
   derivatives from first principles for simple functions.
2. **Interpret** a derivative physically and state its units, for a velocity
   gradient, a geothermal gradient, a strain rate and a gravity gradient.
3. **Estimate** a derivative numerically with a forward and a central difference
   and state the truncation error of each.
4. **Explain** why numerical differentiation amplifies noise, and choose an
   interval from the data's precision rather than from convenience.
5. **Interpret** a second derivative as a curvature scale, and show that the
   curvature scale of the Earth's gravity field is thousands of kilometres.
6. **Recognise** a point where a derivative fails to exist, and say what the
   failure means in a geological model.

## Prerequisites

[01-05-01 Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md).
The derivative *is* a limit, and every subtlety about limits — one-sided limits,
discontinuities, precision floors — reappears here.

## 1. Intuition: gradients are the language of Earth processes

Almost every quantity in geophysics is a gradient of something:

| Quantity | Definition | Typical sense |
|---|---|---|
| Velocity gradient $dv/dz$ | change of seismic speed with depth | turns rays, controls refraction |
| Geothermal gradient $dT/dz$ | temperature increase with depth | multiplied by conductivity gives heat flux |
| Strain rate $\dot\varepsilon = dv/dx$ | velocity change across a zone | how fast rock deforms |
| Gravity gradient $dg/dz$ | change of gravity with height | the free-air correction |
| Thermal gradient in the atmosphere | $-dT/dz$ | lapse rate; determines stability |

Each of these is the same mathematical object. Learning the derivative once and
then attaching four or five physical meanings to it is far more efficient than
learning four or five formulas.

The derivative also answers the question that a table of numbers cannot: **how
fast is it changing, and therefore what happens next?** A velocity model tells you
where a ray has been; the velocity gradient tells you where it goes.

## 2. Precise definitions

### 2.1 The derivative

For a function $f$ defined near $x$,

$$f'(x) = \frac{df}{dx} = \lim_{h\to0}\frac{f(x+h) - f(x)}{h},$$

provided the limit exists. If it does, $f$ is **differentiable at** $x$;
differentiability implies continuity, but not the converse.

The quotient before the limit is the **difference quotient**, and it has a
geometric meaning: the slope of the secant line through $(x, f(x))$ and
$(x+h, f(x+h))$. The derivative is the slope of the tangent, i.e. the limit of
the secants.

### 2.2 One-sided derivatives and non-differentiability

$$f'_-(x) = \lim_{h\to0^{-}}\frac{f(x+h)-f(x)}{h}, \qquad
f'_+(x) = \lim_{h\to0^{+}}\frac{f(x+h)-f(x)}{h}.$$

$f'(x)$ exists if and only if both one-sided derivatives exist and are equal.
Three standard failures: a **kink** (one-sided derivatives exist but differ), a
**jump** (the difference quotient diverges), and an **infinite slope** (the
quotient diverges even though $f$ is continuous).

### 2.3 Notation and higher derivatives

$f'$, $df/dx$, $\dot f$ (time derivatives in physics) all mean the same thing.
Higher derivatives are written $f''$, $f'''$, or $d^{2}f/dx^{2}$. The
**units** of $df/dx$ are the units of $f$ divided by the units of $x$: a
velocity gradient is $\mathrm{s^{-1}}$, a geothermal gradient is
$\mathrm{K\,m^{-1}}$, a strain rate is $\mathrm{s^{-1}}$.

### 2.4 The derivative as a local linear model

Near $x_0$,

$$f(x_0 + h) \approx f(x_0) + f'(x_0)\,h .$$

This is the approximation that makes the derivative useful rather than merely
elegant: it says that over a small enough interval, every differentiable function
is a straight line, and the derivative is the slope of that line. The error of the
approximation is the subject of [01-05-04](./04-taylor-series.md).

## 3. Step-by-step derivations

### 3.1 From first principles: $d(x^{2})/dx = 2x$ and $d(1/x)/dx = -1/x^{2}$

$$\frac{(x+h)^{2}-x^{2}}{h} = \frac{2xh + h^{2}}{h} = 2x + h \xrightarrow[h\to0]{} 2x .$$

$$\frac{\dfrac{1}{x+h}-\dfrac{1}{x}}{h}
= \frac{x - (x+h)}{h\,x(x+h)} = \frac{-1}{x(x+h)}
\xrightarrow[h\to0]{} -\frac{1}{x^{2}} .$$

In both cases the algebra removes the $h$ from the denominator — that is what
"cancelling the $0/0$" means in practice, and it is why the limit of a difference
quotient is *not* evaluated by substituting $h = 0$.

### 3.2 The free-air gradient: differentiating the gravity field

Let $z$ be height above the surface and treat the Earth as a point mass for this
purpose. Then

$$g(z) = \frac{GM}{(R+z)^{2}} .$$

Use the chain rule with $u = R+z$:

$$\frac{dg}{dz} = -\,\frac{2GM}{(R+z)^{3}} ,
\qquad\text{so at } z = 0:\quad g'(0) = -\frac{2GM}{R^{3}} = -\frac{2g(0)}{R} .$$

With $G = 6.674\times10^{-11}$, $M = 5.972\times10^{24}$ kg and
$R = 6.371\times10^{6}$ m (round ILLUSTRATIVE values), the script evaluates

$$g(0) = 9.819532 \ \mathrm{m\,s^{-2}}, \qquad
g'(0) = -3.0825716631\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}} = -0.308257\ \mathrm{mGal\,m^{-1}} .$$

The standard quoted free-air gradient is about $0.3086\ \mathrm{mGal\,m^{-1}}$.
The difference in the third decimal is not arithmetic error: the quoted value comes
from the normal-gravity formula of the reference ellipsoid, which includes
centrifugal effects and ellipticity, while the expression above is a spherical
model. **Use $0.3086\ \mathrm{mGal\,m^{-1}}$ for routine work and a gravity
formula when you need more**, and note that the true gradient varies with latitude
because $R$ and the centrifugal term do.

### 3.3 Forward and central differences, and their errors

Taylor's theorem (proved in [01-05-04](./04-taylor-series.md)) gives

$$f(x+h) = f(x) + h f'(x) + \frac{h^{2}}{2}f''(\xi),$$

so the **forward difference** satisfies

$$\frac{f(x+h)-f(x)}{h} = f'(x) + \underbrace{\frac{h}{2}f''(\xi)}_{\text{truncation}} .$$

Expanding to one more term on each side and subtracting,

$$f(x+h) - f(x-h) = 2h f'(x) + \frac{h^{3}}{3}f'''(\xi),$$

so the **central difference** satisfies

$$\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \underbrace{\frac{h^{2}}{6}f'''(\xi)}_{\text{truncation}} .$$

The orders matter: halving $h$ buys one decimal digit with the forward formula and
two with the central formula. The script confirms both:

| $h$ (m) | forward error | central error | $h$ (m) | forward | central |
|---|---|---|---|---|---|
| $10^{3}$ | $7.26\times10^{-10}$ | $1.52\times10^{-13}$ | $10^{1}$ | $7.26\times10^{-12}$ | $2.12\times10^{-17}$ |
| $10^{2}$ | $7.26\times10^{-11}$ | $1.52\times10^{-15}$ | $10^{0}$ | $7.27\times10^{-13}$ | $2.88\times10^{-16}$ |

The forward errors fall by 10 per decade of $h$ and the central errors by 100,
exactly as the analysis predicts. At $h = 1$ m and below, round-off takes over
and the improvement stops — differentiation has a **precision floor** as well as a
truncation error.

### 3.4 Differentiation amplifies noise

A real velocity profile is a *measured* profile. Write it as
$v_{\text{obs}}(z) = v(z) + \eta(z)$ with noise of standard deviation $\sigma$.
The central difference of the noise is

$$\frac{\eta(z+h)-\eta(z-h)}{2h}, \qquad
\text{standard deviation} \approx \frac{\sigma}{\sqrt{2}\,h} .$$

Truncation error falls with $h$; noise error rises as $1/h$. The optimum is a
compromise, and it is *not* small. The script measures the mean absolute error of
$dv/dz$ for a true gradient of $0.5\ \mathrm{s^{-1}}$ with $\sigma = 10$ m/s:

| $h$ (m) | mean absolute error | $h$ (m) | mean absolute error |
|---|---|---|---|
| 1000 | 0.0053 | 50 | 0.1075 |
| 200 | 0.0252 | 20 | 0.2593 |
| | | 5 | 1.0291 |

Halving $h$ doubles the error, as the $\sigma/(\sqrt2 h)$ law says. At
$h = 5$ m the estimate of a $0.5\ \mathrm{s^{-1}}$ gradient is wrong by
$1.03\ \mathrm{s^{-1}}$ — twice the true value. **A finer grid does not improve a
derivative of noisy data; a coarser one does, up to the point where truncation
takes over.**

### 3.5 Second derivatives set length scales

Differentiate again:

$$g''(z) = \frac{6GM}{(R+z)^{4}} = \frac{6g(z)}{(R+z)^{2}} .$$

The ratio $g/g''$ has units of length squared, so it defines a scale:

$$\sqrt{\frac{g}{g''}} = \sqrt{\frac{R^{2}}{6}} = \frac{R}{\sqrt6} = 2.600950\times10^{6}\ \mathrm{m},$$

confirmed by the script to seven significant figures. The second derivative of the
gravity field is not a small-scale quantity; it varies appreciably only over
thousands of kilometres. This is the origin of the length scale in the free-air
gradient, and the reason a gravity survey's "regional" field is a long-wavelength
object.

### 3.6 Two more geophysical rates

**Geothermal gradient to heat flux.** Fourier's law in one dimension is
$q = -k\,dT/dz$. With $z$ increasing downward and $dT/dz = 25\ \mathrm{K\,km^{-1}}
= 2.5\times10^{-2}\ \mathrm{K\,m^{-1}}$ (ILLUSTRATIVE), the script gives

$$k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}} \Rightarrow q = 6.25\times10^{-2}\ \mathrm{W\,m^{-2}} = 62.5\ \mathrm{mW\,m^{-2}},$$

and $75.0\ \mathrm{mW\,m^{-2}}$ for $k = 3.0$. For scale, Earth's global mean
surface heat flux is usually quoted near $90\ \mathrm{mW\,m^{-2}}$, with continental
shield values well below and young ocean floor well above; treat 62.5 as a worked
number for a specified gradient and conductivity, not as a measurement.

**Strain rate.** Relative motion of 50 mm/yr across a 100 km wide shear zone gives

$$\dot\varepsilon = \frac{v}{W} = \frac{0.050\ \mathrm{m\,yr^{-1}}}{1.0\times10^{5}\ \mathrm{m}}
= 5.0\times10^{-7}\ \mathrm{yr^{-1}} = 1.584\times10^{-14}\ \mathrm{s^{-1}} .$$

The reciprocal is the time to accumulate unit strain: $2.0\times10^{6}$ yr, or
2 Myr. Strain rate is a derivative with respect to time, and its unit
($\mathrm{s^{-1}}$) is the same as a frequency's. That coincidence is harmless but
confusing; keep the physics in view.

### 3.7 A derivative that fails to exist

Take a velocity model that is continuous but whose gradient jumps at the Moho:

$$v(z) = 6.0 + 0.05\max(0,\ z - 33)\ \ \mathrm{km\,s^{-1}} .$$

Then $v'_-(33) = 0$ and $v'_+(33) = 0.05\ \mathrm{s^{-1}}$, and the script shows the
one-sided quotients are `0.000000` and `0.050000` for every $h$ tested. The
derivative does not exist at the Moho. Physically this is a *gradient change*, not
a velocity jump: rays pass through without reflection but the geometry changes
abruptly. Such a model is a mathematical claim about the Earth, and it should be
justified by data resolution, not assumed.

## 4. Physical interpretation

**The derivative is a local statement.** $f'(x_0)$ says nothing about $f$ far from
$x_0$. A velocity gradient measured in a borehole constrains the velocity gradient
*at that borehole*, and extending it to a whole basin is an extrapolation, not a
derivative.

**Signs and conventions cost more than calculus.** Whether $dT/dz$ is positive
depends on whether $z$ points up or down; whether the free-air correction is added
or subtracted depends on whether you are reducing to the datum or from it. Two
competent geophysicists disagreeing about a sign usually disagree about a
convention, not about mathematics. State the convention, then do the calculus.

**A kink in a model is a claim about a boundary.** Since rays turn where the
velocity gradient is non-zero, a gradient discontinuity (a kink) is as much a
boundary as a velocity discontinuity (a jump): both mark a change in medium. The
difference is that a kink does not generate a reflection.

**Smoothness is an assumption you have to buy.** Every finite-difference solver,
every Taylor expansion and every ray tracer assumes a certain number of continuous
derivatives. When a model violates that assumption, the discretisation is wrong
near the violation — and the error is *localised*, which usually makes it easy to
find but easy to miss if your diagnostic is an average over the whole model.

## 5. Python demonstration

The companion script is [`code/derivatives_demo.py`](./code/derivatives_demo.py).
It computes each derivative twice — analytically from the rules and numerically by
a finite difference — so that the difference between the columns is the lesson.

The core experiment is the gravity gradient:

```python
def g_of_z(z):                      # point mass at the Earth's centre
    return G * M_EARTH / (R_EARTH + z) ** 2

analytic = -2.0 * G * M_EARTH / R_EARTH ** 3
for h in (1.0e3, 1.0e2, 1.0e1, 1.0, 1.0e-1):
    fwd = (g_of_z(h) - g_of_z(0.0)) / h
    ctr = (g_of_z(h) - g_of_z(-h)) / (2.0 * h)
```

Observed output:

| $h$ (m) | forward | central | forward error | central error |
|---|---|---|---|---|
| `1e+03` | `-3.081846048600e-06` | `-3.082571814993e-06` | `7.26e-10` | `1.52e-13` |
| `1e+02` | `-3.082499087981e-06` | `-3.082571664619e-06` | `7.26e-11` | `1.52e-15` |
| `1e+01` | `-3.082564405332e-06` | `-3.082571663082e-06` | `7.26e-12` | `2.12e-17` |

with the analytic value `-3.0825716631e-06` and the identity
`-2*g(0)/R = -3.0825716631e-06` printed alongside it.

Other observed outputs, with their interpretation:

| Section | Observed | Interpretation |
|---|---|---|
| 1, linear $v(z)$ | forward and central both exactly `0.500000000000000` for $h\ge1$ m | a linear function is differentiated exactly; the floor `1.26e-08` at $h=10^{-5}$ m is round-off |
| 3, curvature | `sqrt(g/g'') = 2.600950e+06` m, `R/sqrt(6) = 2.600950e+06` m | the second derivative defines a scale of thousands of km |
| 4, heat flux | `62.50 mW/m^2` ($k=2.5$), `75.00 mW/m^2` ($k=3.0$) | Fourier's law applied to a stated gradient |
| 5, strain rate | `5.000e-07 per year`, `1.584e-14 per second`, `2.000 Myr` to unit strain | derivatives with respect to time have units of inverse time |
| 6, kink at the Moho | left `0.000000`, right `0.050000` for every $h$ | the derivative genuinely does not exist there |
| 7, noisy data | error falls from `1.0291` at $h=5$ m to `0.0053` at $h=1000$ m | differentiation amplifies noise as $1/h$ |

> **Breaking exercise.** Section 4 uses $k = 2.5$ and $k = 3.0$. Identify which is
> more plausible for a dry crystalline rock and which for a saturated porous rock,
> and state the physical mechanism (conduction through grains versus convection of
> pore water). Then explain why a heat-flux estimate requires that you state *which*
> you assumed.

## 6. Exercises

Full set and worked solutions:
[`exercises/02-derivatives-exercises.md`](./exercises/02-derivatives-exercises.md)
and [`exercises/02-derivatives-solutions.md`](./exercises/02-derivatives-solutions.md).
Four to attempt first:

**★1.** Differentiate from first principles: (a) $f(x) = 3x^{2} - 5x$,
(b) $f(x) = 1/(x+2)$, (c) $f(t) = \sqrt{t}$.

**★2.** State the units of each derivative, and check with dimensional analysis:
(a) $dv/dz$ for $v$ in km/s and $z$ in km; (b) $dT/dz$ for $T$ in K and $z$ in km;
(c) $dg/dz$ for $g$ in m/s² and $z$ in m.

**★★3.** A velocity model is $v(z) = 1500 + 0.5z$ m/s for $z$ in metres.
(a) Compute $dv/dz$. (b) Estimate $dv/dz$ at $z = 3000$ m by a central difference
with $h = 100$ m and with $h = 1$ m, and compare with (a). (c) Explain why the
answer for $h = 10^{-5}$ m is *worse* than for $h = 100$ m.

**★★4.** A borehole records temperatures 22.0 °C at 0 m and 91.0 °C at 2000 m.
(a) Compute the geothermal gradient in K/km. (b) Estimate the heat flux for
$k = 2.4\ \mathrm{W\,m^{-1}\,K^{-1}}$. (c) State two physical reasons the
gradient measured over 0–2000 m may differ from the true steady-state gradient.

**★★★5.** Repeat the noise experiment of Section 3.4 for a *second* derivative,
using $\sigma = 10$ m/s and $h = 500, 100, 20$ m. The noise in a second difference
scales as $\sigma/h^{2}$. Measure the exponent from your results and compare with
the prediction. This is a numerical-experiment report: state the method, the
result, and the limits of your conclusion.

## 7. Common mistakes

1. **Reporting a finite difference as if it were the derivative.** It has a
   truncation error that depends on $h$, and a round-off error that grows as $h$
   shrinks. Always state which interval you used.
2. **Choosing $h$ as small as possible.** For a function evaluated in floating
   point, or for data with noise, that is the worst choice available.
3. **Forgetting the units of the derivative.** Dividing km/s by km gives
   $\mathrm{s^{-1}}$, which is neither a velocity nor a frequency.
4. **Assuming differentiability.** Real Earth models contain jumps and kinks.
   Differentiating across one is meaningless; differentiate up to it instead.
5. **Confusing the derivative with a difference quotient in sign conventions.**
   $g'(0) = -2g/R$ is negative because gravity decreases upward. If your sign is
   positive, you have oriented $z$ downward.
6. **Extrapolating a borehole gradient into a basin.** A derivative is a local
   measurement; using it as a regional constant is a model assumption.
7. **Ignoring that a measured rate has an uncertainty.** The value
   $1.584\times10^{-14}\,\mathrm{s^{-1}}$ is arithmetic from 50 mm/yr and 100 km;
   the strain rate is uncertain to whatever those inputs are uncertain by.

## 8. Real-world applications

- **Microgravity monitoring.** Repeated surveys detect the height change of a
  gravimeter station through the free-air gradient; a 1 cm elevation error is
  about 3 µGal, which is close to the repeatability of modern instruments.
  Uplift of 5 mm/yr produces a gravity rate near $-1.5\ \mu\mathrm{Gal\,yr^{-1}}$
  (computed in the script), so secular motion is detectable only over years.
- **Geothermics.** The product of a measured gradient and a measured conductivity
  is a heat flux; both measurements are noisy, which is why heat-flow values are
  quoted with uncertainties of tens of percent.
- **Tomography and ray tracing.** Velocity gradients determine ray curvature. A
  linear gradient produces a circular arc; a constant gradient produces the
  straight rays of a homogeneous medium.
- **GNSS and strain.** Strain rates from continuous GNSS time series are
  derivatives of noisy displacement series, and the same $1/h$-versus-truncation
  trade-off governs how long a time window you should difference over. See
  [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).
- **Numerical modelling.** Every finite-difference operator is a truncated Taylor
  series, so its accuracy order follows from the expansion in Section 3.3. See
  [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 9–11.
  Level: beginner upward. The careful treatment of differentiability and the
  distinction between derivative and difference quotient.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapters 4–5.
  Level: beginner to intermediate. Includes the mean-value theorem in the form used
  in Section 3.3.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapter 1. Level: advanced undergraduate upward. The error
  analysis behind the optimal-step trade-off in Section 3.4.
- **Turcotte, D. L. & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Chapters 4 and 6. Level: intermediate. Geothermal gradients
  and heat flow as worked applications of the derivative.
- **Stein, S. & Wysession, M. (2003). *An Introduction to Seismology, Earthquakes,
  and Earth Structure*. Blackwell.** Chapters 2–3. Level: beginner to
  intermediate. Velocity gradients and their effect on ray paths.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not reproduce copyrighted text; confirm editions and
> availability through your library before citing them. Chapter references are
> indicative rather than authoritative: editions differ in numbering and content,
> so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can compute a derivative from the limit definition without looking up a
      rule, and I can say why cancelling the $h$ is not dividing by zero.
- [ ] I can state the units of any derivative I write and check them
      dimensionally.
- [ ] I can write down the forward and central difference formulas together with
      their truncation error orders.
- [ ] I can explain why differentiating noisy data requires a *large* step, and
      estimate that step from the noise level.
- [ ] I can derive the free-air gradient $-2g/R$ and turn it into
      mGal/m.
- [ ] I can explain what it means for a derivative not to exist at a boundary, and
      give a geological example.
- [ ] I can compute a strain rate and a geothermal gradient and interpret both.

## 11. Related lessons

- [01-05-01 Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md) —
  the limit that defines the derivative, and the discontinuities that remove it.
- [01-05-03 Differentiation Rules and Implicit Differentiation](./03-differentiation-rules.md) —
  the rules that replace first-principles calculations in practice.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md) —
  the theory behind the truncation errors quoted in Section 3.3.
- [01-05-05 Integration Techniques and Definite Integrals](./05-integration.md) —
  the inverse operation: from a gradient back to a total.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  where the derivative goes when the field depends on three coordinates.
- [01-04 Floating-Point Representation](../01-arithmetic/04-floating-point.md) —
  catastrophic cancellation, the mechanism behind the precision floor.
