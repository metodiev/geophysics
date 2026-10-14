---
id: 01-05-03
title: "Differentiation Rules and Implicit Differentiation"
level: beginner
prereqs: ["01-05-02"]
estimated_minutes: 90
tags: [calculus, differentiation, chain-rule, implicit-differentiation]
---

# Differentiation Rules and Implicit Differentiation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the product and quotient rules from the limit definition, rather
   than accepting them as results.
2. **Apply** the sum, product, quotient, power and chain rules to combinations of
   elementary functions without hesitation.
3. **Differentiate** a relation given implicitly, and interpret the derivative as
   the local slope of a curve defined by a constraint.
4. **Use** logarithmic differentiation on products, quotients and power laws, and
   read the result as an elasticity.
5. **Derive** the ray parameter $p = \sin\theta/v$ from the travel-time curve, and
   recognise the result as Snell's law.
6. **Choose** between a rule-based derivative and a numerical one, and say when
   each is the better instrument.

## Prerequisites

[01-05-02 Derivatives and Rates of Change](./02-derivatives.md) for the limit
definition, and the trigonometric and exponential functions from
[01-02-03 Exponentials, Logarithms and Decay Laws](../02-algebra/03-exponentials-logarithms.md)
and [01-03-02 Trigonometric Identities](../03-trigonometry/02-trig-identities.md).

## 1. Intuition: rules are compressed limits

Differentiating from first principles is honest but slow, and for a composite
function such as

$$Z(z) = \bigl(\rho_0 + \alpha z\bigr)\bigl(v_0 + \beta z\bigr)$$

the algebra of the difference quotient is unpleasant and uninformative. The
differentiation rules are the *results* of that algebra, evaluated once and
recorded. There is no new mathematics in applying them; the mathematics is in the
derivation, which is why this lesson derives the two rules that are easy to get
wrong — product and quotient — instead of merely listing them.

There is a second reason to know the rules well: they are what a computer algebra
system or an automatic-differentiation library implements. When you write a
forward model in a differentiable-programming framework, the gradient you get back
is computed by exactly these rules applied mechanically. A wrong rule in your head
becomes a wrong Jacobian in your inversion.

## 2. Precise definitions

### 2.1 The rules

Let $f$ and $g$ be differentiable, and $c$ a constant.

| Rule | Statement |
|---|---|
| Constant | $\dfrac{d}{dx}(c) = 0$ |
| Power | $\dfrac{d}{dx}x^{n} = n x^{n-1}$ (all real $n \ne 0$, $x>0$) |
| Sum | $(f \pm g)' = f' \pm g'$ |
| Product | $(fg)' = f'g + fg'$ |
| Quotient | $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^{2}}$ |
| Chain | $\dfrac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$ |
| Reciprocal | $\left(\dfrac{1}{g}\right)' = -\dfrac{g'}{g^{2}}$ |

### 2.2 Derivatives of the elementary functions

$$\frac{d}{dx}e^{x} = e^{x}, \qquad \frac{d}{dx}\ln x = \frac{1}{x}, \qquad
\frac{d}{dx}x^{n} = nx^{n-1},$$
$$\frac{d}{dx}\sin x = \cos x, \qquad \frac{d}{dx}\cos x = -\sin x, \qquad
\frac{d}{dx}\tan x = \sec^{2}x .$$

The first two are the ones that matter most in Earth science: $e^{x}$ describes
decay and diffusion kernels, and $\ln x$ converts ratios into additive
quantities — pH, magnitude scales, decibels, and the logarithmic strain used in
rock mechanics.

### 2.3 Implicit differentiation

If a curve is given by a relation $F(x,z) = 0$ rather than $z = z(x)$, then where
$F$ is differentiable and $F_z \neq 0$,

$$\frac{dz}{dx} = -\,\frac{F_x}{F_z} .$$

The formula comes from differentiating $F(x, z(x)) = 0$ with respect to $x$ by the
chain rule; the partial-derivative notation is made precise in
[01-06-01](../06-multivariable-calculus/01-partial-derivatives.md). In one-variable
language: differentiate both sides with respect to $x$, treating $z$ as an unknown
function of $x$, then solve for $dz/dx$.

### 2.4 Logarithmic differentiation

For a positive function $y(x)$, the **logarithmic derivative** is
$d(\ln y)/dx = y'/y$. It converts products to sums and powers to factors:

$$\frac{d}{dx}\ln\!\left(\frac{f g}{h}\right) = \frac{f'}{f} + \frac{g'}{g} - \frac{h'}{h},
\qquad
\frac{d}{dx}\ln\!\left(f^{\,b}\right) = b\,\frac{f'}{f} .$$

The dimensionless ratio $(dy/y)/(dx/x) = \dfrac{x\,y'}{y}$ is the **elasticity** of
$y$ with respect to $x$: the fractional change in $y$ per fractional change in
$x$. Rock physics is written in elasticities for good reason — see Section 3.6.

## 3. Step-by-step derivations

### 3.1 The product rule, from the limit definition

$$\frac{f(x+h)g(x+h) - f(x)g(x)}{h}$$
$$= \frac{f(x+h)g(x+h) - f(x+h)g(x) + f(x+h)g(x) - f(x)g(x)}{h}$$
$$= f(x+h)\frac{g(x+h)-g(x)}{h} + g(x)\frac{f(x+h)-f(x)}{h}.$$

Let $h \to 0$: $f(x+h) \to f(x)$ because differentiability implies continuity, and
the two quotients become $g'(x)$ and $f'(x)$. Hence $(fg)' = fg' + gf'$. The
trick — adding and subtracting the same quantity $f(x+h)g(x)$ — is the whole
proof; the rest is the algebra of limits from
[01-05-01](./01-limits-and-continuity.md).

### 3.2 The quotient rule, from the reciprocal rule

The reciprocal rule follows from the difference quotient

$$\frac{\frac{1}{g(x+h)} - \frac{1}{g(x)}}{h}
= \frac{g(x) - g(x+h)}{h\,g(x)g(x+h)}
\xrightarrow[h\to0]{} -\frac{g'(x)}{g(x)^{2}} .$$

Then $f/g = f\cdot(1/g)$ and the product rule gives

$$\left(\frac{f}{g}\right)' = f'\cdot\frac{1}{g} + f\cdot\left(-\frac{g'}{g^{2}}\right)
= \frac{f'g - fg'}{g^{2}},$$

which is the quotient rule. Deriving it in two lines beats memorising it, and the
derivation also shows where the asymmetry in the numerator comes from.

### 3.3 The chain rule: rates multiply

If $g$ is differentiable at $x$ and $f$ at $g(x)$, then

$$\frac{d}{dt}f(g(t)) = f'(g(t))\,g'(t) .$$

The intuition is dimensional: $f'$ is "units of $f$ per unit of $g$", $g'$ is
"units of $g$ per unit of $t$", and their product is "units of $f$ per unit of
$t$". The units must cancel in the middle or the composition is not physical.

**Geophysical instance: uplift produces a gravity change.** With
$z(t)$ the height of a station and $g(z) = GM/(R+z)^{2}$,

$$\frac{dg}{dt} = \frac{dg}{dz}\cdot\frac{dz}{dt}
= \left(-\frac{2GM}{R^{3}}\right)\dot z .$$

The script evaluates this for an uplift rate of 5 mm/yr with the free-air gradient
of lesson 01-05-02:

$$\frac{dg}{dt} = (-3.0826\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}})(5\times10^{-3}\ \mathrm{m\,yr^{-1}})
= -1.541\times10^{-8}\ \mathrm{m\,s^{-2}\,yr^{-1}} = -1.5413\ \mu\mathrm{Gal\,yr^{-1}} .$$

That number is why secular vertical motion is hard to detect gravimetrically:
several years of uplift at a plate-boundary rate are needed to reach the
repeatability of a good relative gravimeter.

### 3.4 Implicit differentiation: the slope of an elliptical interface

Suppose an interface, mapped in cross-section, satisfies

$$\frac{x^{2}}{a^{2}} + \frac{z^{2}}{b^{2}} = 1
\qquad\text{with } F_x = \frac{2x}{a^{2}}, \quad F_z = \frac{2z}{b^{2}} .$$

Then

$$\frac{dz}{dx} = -\frac{F_x}{F_z} = -\frac{b^{2}x}{a^{2}z} .$$

With $a = 2000$ m and $b = 1000$ m the script compares this analytic slope with a
central-difference slope of the same curve:

| $x$ (m) | analytic $dz/dx$ | numeric $dz/dx$ |
|---|---|---|
| 200 | `-0.0502518908` | `-0.0502518908` |
| 1000 | `-0.2886751346` | `-0.2886751346` |
| 1800 | `-1.0323708024` | `-1.0323708023` |

The agreement to ten digits is the evidence that the implicit formula is right.
Notice the physics in the last row: as the interface steepens towards its limit,
$dz/dx \to -\infty$. A vertical contact cannot be written as $z(x)$ at all — the
implicit form $F(x,z)=0$ still describes it, which is one reason implicit
multivariable formulations are preferred in gravity and magnetic modelling.

### 3.5 Logarithmic differentiation: decay laws

For $A(t) = A_0 e^{-\lambda t}$,

$$\frac{d(\ln A)}{dt} = -\lambda, \qquad\text{equivalently}\qquad
\frac{dA}{dt} = -\lambda A ,$$

so the *fractional* rate of change is constant while the absolute rate is
proportional to the current amount. The script checks this numerically at
$t = 1000$ yr for the conventional radiocarbon half-life $t_{1/2} = 5730$ yr:

$$\lambda = \frac{\ln 2}{5730} = 1.209681\times10^{-4}\ \mathrm{yr^{-1}},$$

and after ten half-lives the remaining activity is `9.765625e-04` of the initial
value, which is exactly $1/1024$. **The point of logarithmic differentiation is
that it turns a multiplicative law into an additive constant**, which is why decay
constants rather than "fractions remaining" are tabulated.

### 3.6 Power laws and elasticity

Empirical rock-physics relations between density and P-wave speed are commonly
written as power laws, $\rho = a v^{b}$ (Gardner-type relations; the exponent is
often quoted near $b \approx 0.25$, but the fitted coefficients depend on the unit
system — always read the source's units before using them). Then

$$\frac{d\rho}{dv} = a b v^{b-1}, \qquad\text{and therefore}\qquad
\frac{d\rho/\rho}{dv/v} = b .$$

The independent check in the script uses $a = 2.1$, $b = 0.25$, $v_0 = 3000$ (a
SYNTHETIC illustrative parameter set): analytic `1.2951449079e-03`, numeric
`1.2951449393e-03`. The sentence that a reader can use is the elastic one: **a 1 %
increase in $v$ implies a 0.25 % increase in $\rho$**, at every $v$. That
scale-invariance is the signature of a power law and the reason such relations
extrapolate badly — a constant elasticity is a strong assumption.

### 3.7 Differentiating the travel-time curve gives Snell's law

For one horizontal layer of thickness $h$ and speed $v$, a reflection recorded at
offset $x$ has travel time

$$t(x) = \frac{2}{v}\sqrt{h^{2} + \frac{x^{2}}{4}} = \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}},
\qquad t_0 = \frac{2h}{v}.$$

Differentiate with the chain rule ($u = t_0^{2} + x^{2}/v^{2}$):

$$\frac{dt}{dx} = \frac{1}{2\sqrt{u}}\cdot\frac{2x}{v^{2}} = \frac{x}{v^{2}t} .$$

Now read the geometry. The ray leaves the source at angle $\theta$ from the
vertical, travels a half-path $L = \sqrt{h^{2} + (x/2)^{2}} = vt/2$, and
$\sin\theta = (x/2)/L = x/(vt)$. Therefore

$$\frac{\sin\theta}{v} = \frac{x}{v^{2}t} = \frac{dt}{dx} = p .$$

The quantity $p$ is the **ray parameter**, and this identity is Snell's law. No
trigonometry was assumed: the derivative of the travel-time curve *is* the ray
parameter. The script verifies the equality column by column — for
$v = 2000$ m/s, $t_0 = 1$ s and $x = 1000$ m both columns read
`2.2360679775e-04`, agreeing to `2.7e-20`. This is the standard route from
travel-time curves to a velocity model, and it is developed further in
[01-06-01](../06-multivariable-calculus/01-partial-derivatives.md) and
[06-seismology](../../06-seismology/README.md).

## 4. Physical interpretation

**The chain rule is the mathematics of "one process driving another."** Uplift
drives a gravity change (Section 3.3); a temperature change drives a density change
through thermal expansion, which drives a gravity change; a pressure change drives
a velocity change. In each case the observable rate is a product of a sensitivity
and a forcing rate. Writing the product explicitly is how you decide whether a
measured rate is attributable to the process you have in mind.

**Implicit differentiation is what you use when your model is a constraint.**
Interface locations, isotherms, isochrones, phase boundaries and equilibria are
usually given as $F(x,z)=0$, not as functions. Their slopes follow from $F$ alone.

**Elasticities are the natural language of scaling.** Because power laws have
constant elasticity, a single number $b$ answers the question "how much does the
other quantity move?" for every value of $v$. That is convenient and dangerous: a
constant elasticity across five orders of magnitude of $v$ is a modelling claim,
not an observation.

**Rules fail where their hypotheses fail.** The chain rule needs both functions
differentiable; the quotient rule needs $g \neq 0$; implicit differentiation needs
$F_z \neq 0$. At the vertical tangent of Section 3.4,
$\partial z/\partial x$ diverges because $F_z = 0$ there. In a numerical model
this shows up as a Jacobian that becomes singular at exactly the configuration you
care about.

## 5. Python demonstration

The companion script is
[`code/differentiation_rules_demo.py`](./code/differentiation_rules_demo.py). Its
structure is deliberate: for each rule it prints the analytic derivative and a
central-difference derivative of the same function, so that a wrong rule is caught
by the arithmetic rather than by the reader's trust.

```python
def numeric_derivative(f, x, h=CENTRAL_H):
    return (f(x + h) - f(x - h)) / (2.0 * h)

impedance = lambda z: rho(z) * vel(z)
analytic = 0.10 * vel(1000.0) + rho(1000.0) * 0.5      # rho' v + rho v'
check("d(rho v)/dz", analytic, numeric_derivative(impedance, 1000.0))
```

Observed output (selected):

| Rule checked | analytic | numeric | relative difference |
|---|---|---|---|
| product, $d(\rho v)/dz$ | `1.5500000000e+03` | `1.5499999747e+03` | `1.63e-08` |
| quotient, $d(x/v)/dx$ | `4.0000000000e-04` | `3.9999999979e-04` | `5.26e-10` |
| chain, $dg/dz$ at $z=0$ | `-3.0825716631e-06` | `-3.0825716631e-06` | `6.87e-12` |
| log, $d(\ln A)/dt$ | `-1.2096809434e-04` | `-1.2096809434e-04` | `4.80e-13` |
| power law, $d(av^{b})/dv$ | `1.2951449079e-03` | `1.2951449393e-03` | `2.43e-08` |

The relative differences are at the $10^{-8}$–$10^{-13}$ level, which is the
central-difference truncation error $h^{2}/6$ for $h = 10^{-5}$ plus round-off —
exactly what [01-05-02](./02-derivatives.md) predicts. A wrong rule would give a
relative difference near $1$, so this table is a real test.

The remaining sections produce the numbers quoted in the derivation:

| Section | Observed | Interpretation |
|---|---|---|
| 3, chain rule | `dg/dt = -1.541286e-08 m s^-2 per yr` = `-1.5413 µGal/yr` | 5 mm/yr of uplift is a hard gravimetric signal |
| 4, decay law | $\lambda$ = `1.209681e-04 per year`; ten half-lives → `9.765625e-04` = $1/1024$ | logarithmic differentiation makes the rate constant |
| 6, ellipse | $dz/dx$ from `-0.0502518908` at $x=200$ m to `-1.0323708024` at $x=1800$ m | the slope diverges as the interface steepens |
| 7, travel time | `dt/dx` and `sin(theta)/v` agree to `2.7e-20` at $x=1000$ m | the derivative of the travel-time curve is the ray parameter |

> **Breaking exercise.** Section 6 uses a half-ellipse with $a = 2000$ m. Before
> running it again, predict the value of $dz/dx$ at $x = 1990$ m, then check it.
> Explain the sign of the discrepancy between the analytic and numeric columns as
> $x \to a$, in terms of the central difference straddling a vertical tangent.

## 6. Exercises

Full set and worked solutions:
[`exercises/03-differentiation-rules-exercises.md`](./exercises/03-differentiation-rules-exercises.md)
and
[`exercises/03-differentiation-rules-solutions.md`](./exercises/03-differentiation-rules-solutions.md).
Start with these four:

**★1.** Differentiate, stating the rule used at each step:
(a) $f(x) = (3x^{2}+1)(x-4)$, (b) $g(z) = \dfrac{z^{2}}{z+1}$,
(c) $h(t) = \sin(t^{2})$, (d) $q(x) = \ln(5x^{3})$.

**★2.** Verify the product rule numerically for $f(x) = x^{2}\sin x$ at
$x = 1.0$ by comparing $f'(1)$ with a central difference of step $10^{-5}$.

**★★3.** A rock-physics relation is $v = v_0 (1 + \alpha \phi)^{-1}$ with porosity
$\phi$. (a) Compute $dv/d\phi$ by the chain rule. (b) Compute the elasticity
$(dv/v)/(d\phi/\phi)$ and evaluate it at $\phi = 0.2$, $\alpha = 2.5$. (c) Is the
elasticity constant? What does that tell you about extrapolating the relation?

**★★4.** An isotherm at temperature $T_1$ is defined implicitly by
$T(x,z) = T_0 + \gamma z - A\cos(kx)e^{-kz} = T_1$. Compute $dz/dx$ on this
isotherm in terms of the given constants, and explain the meaning of the resulting
expression for large $z$.

**★★★5.** Section 3.7 derived $p = dt/dx = \sin\theta/v$ for a single layer.
Repeat the derivation for a two-layer model where the reflection comes from the
base of the second layer, this time as an implicit relation in the offset $x$, and
show that the identity still holds. State which assumption about the ray geometry
is essential. (This is the structure of a real travel-time inversion; see
[18-inverse-problems](../../18-inverse-problems/README.md).)

## 7. Common mistakes

1. **Applying the product rule to a product of three factors.** Write
   $(fgh)' = f'gh + fg'h + fgh'$ — or apply the rule twice. Forgetting the third
   term is a classic.
2. **Writing $\left(f/g\right)' = f'/g'$.** Wrong in every case except
   coincidences; the quotient rule has $f'g - fg'$ in the numerator.
3. **Ignoring the inner derivative in the chain rule.** $\frac{d}{dx}\sin(t^{2})$
   is $2t\cos(t^{2})$, not $\cos(t^{2})$.
4. **Forgetting that $x^{n}$ with non-integer $n$ needs $x>0$.** Treating
   $(-8)^{1/3}$ as a real power and differentiating it is a category error.
5. **Differentiating an implicit relation as if $z$ were a constant.** Every
   occurrence of $z$ contributes a $dz/dx$ through the chain rule.
6. **Cancelling a derivative as if it were a fraction.** The chain rule looks like
   cancellation of $dg$, but $dz/dx$ is not a quotient of two numbers; pretending
   otherwise breaks down in higher dimensions.
7. **Assuming the elasticity of an empirical relation is physical.** A fitted
   exponent $b$ is a description of the data your source had, not a law of nature.

## 8. Real-world applications

- **Travel-time inversion.** The identity $p = dt/dx$ allows a measured
  travel-time curve to be converted into a velocity–depth function through
  $dz/dp$; this is the classical Herglotz–Wiechert inversion and the conceptual
  ancestor of modern tomography.
- **Microgravity monitoring of uplift and subsidence.** The chain-rule product of
  the free-air gradient and a GNSS-derived vertical rate gives the expected
  gravity rate; disagreement is evidence of a subsurface mass change (magma, water,
  gas). See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Rock physics and seismic inversion.** Relations of the form $\rho = a v^{b}$
  and their elasticities connect seismic velocities to density, which is a
  parameter you cannot measure directly down a borehole everywhere. See
  [11-exploration-geophysics](../../11-exploration-geophysics/README.md).
- **Thermal expansion and sea level.** A temperature change drives a density
  change; the chain rule converts a temperature history into a sea-level
  contribution. See [16-atmosphere-climate](../../16-atmosphere-climate/README.md).
- **Differentiable forward models.** Modern inversion frameworks compute
  Jacobians by automatic differentiation, which is the chain rule applied
  mechanically to every operation in the code. See
  [18-inverse-problems](../../18-inverse-problems/README.md).

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 9–12.
  Level: beginner upward. Rigorous derivations of every rule in Section 2.1;
  Section 3.1 follows its presentation of the product rule.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapter 4.
  Level: beginner to intermediate. Includes the mean-value theorem needed to make
  the chain rule proof airtight.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd ed.).
  Wiley.** Chapter 4. Level: beginner. Implicit differentiation and logarithmic
  differentiation presented with physical applications.
- **Aki, K. & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Chapter 4. Level: advanced. Ray parameter, travel
  times and the geometry used in Section 3.7, developed properly.
- **Gardner, G. H. F., Gardner, L. W. & Gregory, A. R. (1974). Formation velocity
  and density — the diagnostic basics for stratigraphic traps. *Geophysics*, 39.**
  Level: intermediate. The origin of the density–velocity power law discussed in
  Section 3.6; check the volume's pagination and the unit conventions of its
  coefficients before using them.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not reproduce copyrighted text; confirm editions and
> availability through your library before citing them. Chapter references are
> indicative rather than authoritative: editions differ in numbering and content,
> so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can derive the product rule and the reciprocal rule from the limit
      definition without notes.
- [ ] I can differentiate a product of three factors and a nested chain of three
      functions correctly on the first attempt.
- [ ] I can compute $dz/dx$ for a curve given implicitly and say what $F_z = 0$
      means geometrically.
- [ ] I can compute a logarithmic derivative and interpret it as an elasticity.
- [ ] I can derive $p = \sin\theta/v = dt/dx$ for a single-layer reflection.
- [ ] I can use the chain rule to convert a forcing rate into an observable rate
      with the units carrying the check.
- [ ] I can decide when to differentiate analytically and when to use a finite
      difference, and I can justify the choice.

## 11. Related lessons

- [01-05-02 Derivatives and Rates of Change](./02-derivatives.md) — the definition
  that these rules compress, and the numerical errors that test them.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md) —
  how derivatives of all orders combine into an approximation.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  implicit differentiation in several variables, where $F_z$ is a partial
  derivative.
- [01-02-03 Exponentials, Logarithms and Decay Laws](../02-algebra/03-exponentials-logarithms.md) —
  the functions whose derivatives are simplest, and their Earth-science meanings.
- [01-03-02 Trigonometric Identities and Their Uses](../03-trigonometry/02-trig-identities.md) —
  the identities needed for the trigonometric derivatives.
- [18-inverse-problems](../../18-inverse-problems/README.md) — where derivatives
  become Jacobians and the chain rule becomes the adjoint.
