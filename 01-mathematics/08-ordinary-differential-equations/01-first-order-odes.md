---
id: 01-08-01
title: "First-Order ODEs: Separation of Variables and Integrating Factors"
level: intermediate
prereqs: ["01-02-03", "01-05-05"]
estimated_minutes: 90
tags: [ordinary-differential-equations, first-order, separation-of-variables, integrating-factor, radioactive-decay]
---

# First-Order ODEs: Separation of Variables and Integrating Factors

## Learning objectives

By the end of this lesson you will be able to:

1. **Recognise** a first-order ordinary differential equation (ODE), state its
   order and linearity, and say what a general solution and a particular
   solution each contain.
2. **Solve** separable equations by separation of variables, including the
   implicit solutions that arise when the integral cannot be inverted in closed
   form.
3. **Derive and apply** the integrating factor for the linear first-order
   equation $y' + p(x)y = q(x)$, and explain why the method is not a trick but
   a consequence of the product rule.
4. **Model** five geophysical systems with the same equation — radioactive
   decay and radiometric dating, Newton cooling of an intrusion, hydraulic-head
   relaxation, RC/RL and electromagnetic transient decay, and well drawdown —
   and compute their characteristic times.
5. **Distinguish** a relaxation time $\tau$ from a half-life, and convert
   between them, including the branching correction needed for K–Ar dating.
6. **Check** a solution by substituting it back, and **estimate** the error of a
   first-order Euler integration well enough to know when it is unacceptable.

## Prerequisites

- [01-02-03 Exponentials, Logarithms and Decay Laws in Earth Science](../02-algebra/03-exponentials-logarithms.md) —
  the exponential function, the logarithm, and the half-life idea.
- [01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md) —
  substitution and integration by parts, used for every quadrature in this
  lesson.
- [01-05-03 Differentiation Rules and Implicit Differentiation](../05-single-variable-calculus/03-differentiation-rules.md) —
  helpful for the product-rule argument in Section 3.2.

## 1. Intuition: five different systems, one equation

Geophysics is full of quantities that relax toward an equilibrium. An
intrusion cools toward the temperature of its surroundings. A pumped aquifer's
head falls toward the level set by the pumping rate. A magnetic field trapped
in a conductor decays as the induced current dissipates. A radioactive parent
decays toward its daughter. In every case the *rate* of change is set by how
far the state is from its target:

$$\frac{dy}{dt} \;\propto\; -(y - y_{\infty}).$$

Written out with a rate constant, this is

$$\frac{dy}{dt} = -a\,(y - y_\infty), \qquad a > 0,$$

whose solution is an exponential approach to $y_\infty$ with time constant
$1/a$. The same three lines of algebra describe the cooling of a 50 m sill
(a few hundred years), the drainage of a confined aquifer (about half a day),
an RC circuit (one second), and the decay of carbon-14 in a bone (a few
millennia). Only the number $a$ changes.

That is the reason this lesson is worth the effort: **the mathematics is a
single idea, and the physics is entirely in the identification of $a$.** A
geophysicist who can write down $a$ for a new problem has already solved it.

Before proceeding, fix the vocabulary:

- **Order** is the highest derivative that appears. This lesson is about order
  one, so the equation involves $y$ and $y'$ only.
- **Linear** means $y$ and $y'$ appear to the first power and are not
  multiplied together. $y' + 2y = \sin t$ is linear; $y' = -y^2$ and
  $y' = y\sin y$ are not.
- **Homogeneous** means the equation can be written with no term free of $y$.
  $y' + 2y = 0$ is homogeneous; $y' + 2y = 4t$ is not. A **forcing** or
  **source term** is the non-homogeneous part.
- A **general solution** of a first-order equation contains one arbitrary
  constant; a **particular solution** is fixed by one initial condition.

## 2. The two solvable forms, stated precisely

### 2.1 Separable equations

An equation is **separable** if it can be written

$$\frac{dy}{dx} = g(x)\,h(y).$$

Dividing by $h(y)$ and integrating gives the implicit general solution

$$\int \frac{dy}{h(y)} = \int g(x)\,dx + C.$$

The method works because both sides are integrals of a single variable. It is
valid on any interval where $h(y) \neq 0$; the points with $h(y)=0$ give
constant solutions, and they must be listed separately because the division by
$h(y)$ excluded them.

### 2.2 Linear equations and the integrating factor

The standard form of a linear first-order equation is

$$y' + p(x)\,y = q(x).$$

Multiply by the **integrating factor**

$$\mu(x) = \exp\!\left(\int p(x)\,dx\right),$$

and observe that

$$\frac{d}{dx}\bigl(\mu y\bigr) = \mu y' + \mu p y = \mu q.$$

Integrating,

$$y(x) = \frac{1}{\mu(x)}\left[\int \mu(x)\,q(x)\,dx + C\right],$$

where $C$ is fixed by the initial condition. Notice that no step required a
guess: the integrating factor is the exponential of $\int p$, and the reason it
works is the product rule.

### 2.3 When neither form applies

Two large families are not covered above and are treated later in the
curriculum:

- **Nonlinear equations of the form $y' = f(y/x)$** are made separable by the
  substitution $u = y/x$; the result is
  $\int du/(f(u)-u) = \ln|x| + C$.
- **Exact equations** $M(x,y) + N(x,y)y' = 0$ with
  $\partial M/\partial y = \partial N/\partial x$ have a potential function
  $F(x,y)$ constant along solutions. This is the same idea as the conservative
  fields of
  [01-06 Potential Fields](../06-multivariable-calculus/08-potential-theory.md),
  and the integrating factor of Section 2.2 is a special case of the general
  integrating factor that makes an equation exact.

## 3. Derivations, step by step

### 3.1 Decay: separation of variables, with the constant fixed by physics

Take $y' = -\lambda y$. Separating,

$$\int \frac{dy}{y} = -\lambda\int dt \;\Longrightarrow\; \ln|y| = -\lambda t + C.$$

Exponentiating gives $y = A e^{-\lambda t}$ with $A = y(0)$. Three
consequences deserve to be written as identities, because they are used
constantly and are frequently confused:

$$y(t) = y_0 e^{-\lambda t}, \qquad
\tau \equiv \frac{1}{\lambda}, \qquad
t_{1/2} = \frac{\ln 2}{\lambda} = \tau\ln 2 \approx 0.6931\,\tau.$$

**A relaxation time and a half-life differ by the factor $\ln 2 = 0.6931$.**
After one half-life, 50 % remains; after one time constant, $e^{-1}=36.8$ %
remains. Mixing these two up is a factor-of-1.44 error, and it appears in
published work often enough to be worth stating explicitly.

### 3.2 The integrating factor from the product rule

Consider a linear equation written in a *non*-standard form, which is how
geophysical models usually arrive. Suppose

$$h\frac{dT}{dt} = -k\,(T - T_a).$$

Rearrange to standard form:

$$\frac{dT}{dt} + \frac{k}{h}T = \frac{k}{h}T_a .$$

So $p(t) = k/h$ and $q(t) = (k/h)T_a$. The integrating factor is

$$\mu(t) = \exp\!\left(\int \frac{k}{h}\,dt\right) = e^{kt/h}.$$

Then

$$\frac{d}{dt}\left(e^{kt/h}T\right) = \frac{k}{h}T_a\,e^{kt/h}
\;\Longrightarrow\;
e^{kt/h}T = T_a e^{kt/h} + C,$$

so $T(t) = T_a + Ce^{-kt/h}$ and the initial condition $T(0)=T_0$ gives
$C = T_0 - T_a$:

$$\boxed{\;T(t) = T_a + (T_0 - T_a)\,e^{-kt/h}\;}$$

Three checks, each of which takes one line and each of which catches a
different class of error:

1. **Units.** $k/h$ must have dimensions of inverse time for the exponent to be
   dimensionless. If $k$ carries units of W K⁻¹ and $h$ of J K⁻¹, then
   $[k/h] = \mathrm{s^{-1}}$, and $1/(k/h)$ is a time. Good.
2. **Initial condition.** At $t=0$ the exponential is 1, so $T=T_0$.
3. **Long-time limit.** As $t\to\infty$, $T \to T_a$, the ambient temperature.
   A solution that does not approach the ambient temperature has the sign of $k$
   wrong.

### 3.3 Dating: solving the equation *for time*, not for concentration

For a radioactive parent $P$ decaying to a stable daughter $D$,

$$\frac{dP}{dt} = -\lambda P, \qquad
\frac{dD}{dt} = +\lambda P .$$

With $P(0)=P_0$ and $D(0)=D_0$, the accumulated radiogenic daughter is

$$D^*(t) = P_0 - P(t) = P(t)\left(e^{\lambda t} - 1\right),$$

because $P_0 = P(t)e^{\lambda t}$. Solving for the age gives the **isochron
age equation** in its simplest form,

$$\boxed{\;t = \frac{1}{\lambda}\ln\!\left(1 + \frac{D^*}{P}\right)\;}$$

**Worked example (Rb–Sr).** Take a measured ratio $^{87}\mathrm{Sr}^*/^{87}\mathrm{Rb} = 0.05$
and the commonly tabulated half-life $4.9\times10^{10}$ yr (values in the
literature differ in the last percent; the number used here is stated so that
the arithmetic can be checked independently). Then

$$\lambda = \frac{\ln 2}{4.9\times10^{10}} = 1.4146\times10^{-11}\ \mathrm{yr^{-1}},$$

and

$$t = \frac{\ln(1.05)}{1.4146\times10^{-11}}
= \frac{0.0487902}{1.4146\times10^{-11}} = 3.449\times10^{9}\ \mathrm{yr}.$$

Back-substituting the age into the age equation recovers the input ratio
exactly: $(e^{\lambda t}-1) = 0.050000$, which is what the demonstration
prints. Note that this particular ratio is far too small for a real Rb–Sr
determination — the numbers are chosen so that every step can be checked by
hand — but the algebra is the algebra that a mass spectrometer's output feeds.

**Worked example (K–Ar), with branching.** Potassium-40 decays by two routes:
electron capture to $^{40}\mathrm{Ar}$ and $\beta$ decay to $^{40}\mathrm{Ca}$.
If $\lambda_e$ is the electron-capture partial rate constant then

$$\frac{D^*}{P} = \frac{\lambda_e}{\lambda}\left(e^{\lambda t} - 1\right),
\qquad\text{so}\qquad
t = \frac{1}{\lambda}\ln\!\left(1 + \frac{\lambda}{\lambda_e}\frac{D^*}{P}\right).$$

With $\lambda = 5.5452\times10^{-10}\ \mathrm{yr^{-1}}$ (half-life
$1.25\times10^{9}$ yr) and a branching fraction of 0.1048 (a commonly tabulated
value; published branch ratios differ slightly between compilations, so state
the one you use), a measured $^{40}\mathrm{Ar}^*/^{40}\mathrm{K} = 0.01$ gives

$$t = \frac{\ln\left(1 + 0.01/0.1048\right)}{5.5452\times10^{-10}}
= \frac{0.0911254}{5.5452\times10^{-10}} = 1.643\times10^{8}\ \mathrm{yr},$$

i.e. about 164 Ma. **Notice the mistake this avoids:** ignoring the branch ratio
and computing $t = \lambda^{-1}\ln(1.01)$ would give $1.79\times10^{7}$ yr, an
error of a factor of nine.

### 3.4 The relaxation time of a geophysical system, derived rather than memorised

Each of the following is one line of dimensional analysis, and each is a
different physical mechanism.

**Radiocarbon.** $\lambda = \ln 2/5730\ \mathrm{yr} = 1.2097\times10^{-4}\ \mathrm{yr^{-1}}$.
An activity ratio $A_0/A = 1.5$ gives
$t = \lambda^{-1}\ln 1.5 = 3352$ yr. The *physical* half-life of
$^{14}\mathrm{C}$ is about 5700 yr; the conventional Libby value of 5568 yr is
retained by international convention for reporting radiocarbon dates, and the
difference between the two is part of why radiocarbon ages are reported with
a stated convention. Use the value your lab uses, and say which.

**Lumped cooling of a sill.** For an intrusion of half-thickness $L$, the
conduction-limited relaxation time scales as $\tau \sim L^2/\kappa$, because
$\kappa$ is the only combination of $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and
a length that yields a time. (The factor is $O(1)$: on this geometry the exact
first-mode time is $L^{2}/(\pi^{2}\kappa)$, as
[05 Sturm–Liouville Theory](./05-sturm-liouville.md) shows. Scaling arguments
give the exponent and the physics; the eigenfunction gives the constant.) With
$L = 50$ m, $\tau = 2500\ \mathrm{m^2}/(10^{-6}\ \mathrm{m^2\,s^{-1}})
= 2.5\times10^{9}$ s $= 79$ yr. A sill that starts at 1100 °C with a country
rock at 100 °C reaches 200 °C when $e^{-t/\tau} = 0.1$, i.e. at
$t = \tau\ln 10 = 182$ yr. **The lumped model is a statement about a
well-mixed body with no internal gradient, which a 100 m sill is not.** It
gives an order of magnitude and an upper bound on the cooling time, not a
thermal history; the honest version of this calculation is the diffusion
solution of
[01-09-02 The Diffusion/Heat Equation](../09-partial-differential-equations/02-heat-equation.md).

**Hydraulic-head relaxation in a confined aquifer.** A 1-D aquifer of length
$L$ drained at one end relaxes as $\exp(-\pi^2Tt/4SL^2)$, where $T$ is
transmissivity and $S$ storativity. Then

$$\tau = \frac{4SL^2}{\pi^2 T}.$$

With $T = 10^{-3}\ \mathrm{m^2\,s^{-1}}$, $S = 10^{-4}$ and $L = 1000$ m,
$\tau = 4.05\times10^{4}$ s $= 0.469$ d. Five metres of head falls to 0.59 m
in a day and to below a centimetre in three days. **The $L^2$ in the numerator
is not what one might guess from the cooling example**, and the reason is
physical: a longer drainage path means a *larger* storage volume to drain
through the same transmissivity, so the response is slower.

**RC and RL circuits.** For a capacitor discharging through a resistor,
$\tau = RC$; for an inductor with series resistance, $\tau = L/R$. These are
not geophysics, but they are the calibration cases: $R = 1\ \mathrm{M\Omega}$
and $C = 1\ \mu\mathrm{F}$ gives $\tau = 1$ s, and the voltage falls to 0.368 of
its initial value after that second. Because the same first-order equation
governs an inductive loop, an electromagnetic transient in the ground decays
with a time constant set by inductance over resistance, which for a fixed
receiver geometry is a function of ground conductivity. This is the elementary
observation behind time-domain electromagnetic sounding.

**Well drawdown.** Let $h$ be the drawdown at a well and let the system relax
toward a steady drawdown $h_\infty$ on a lumped time constant $\tau$. Then

$$\frac{dh}{dt} = -\frac{h}{\tau} + \frac{h_\infty}{\tau},
\qquad h(t) = h_\infty\left(1 - e^{-t/\tau}\right).$$

Ninety per cent of the steady drawdown is reached at $t = \tau\ln 10 = 2.303\tau$;
with $\tau = 2$ d that is 4.6 d. **The quantity being computed is the
*approach to steady state*, which is a different question from the Theis
drawdown itself**; the Theis solution is a diffusion problem in $r$ and $t$,
and this ODE is a lumped surrogate that needs a justification (a well-mixed
reservoir, or the slowest mode of the aquifer) before its $\tau$ can be
trusted.

## 4. Physical interpretation

Read the common structure out of Section 3. Every system there obeys

$$\frac{dy}{dt} = -\frac{y - y_\infty}{\tau}.$$

Three statements follow, and they are the reason the exponential is
everywhere in geophysics:

1. **The relaxation is faster the further from equilibrium.** The rate is
   proportional to the *distance* from equilibrium, so a large perturbation
   decays quickly at first and slowly at the end. This is why borehole
   temperatures recover visibly in the first months after drilling and then
   appear to stall.
2. **The time constant does not depend on amplitude.** A 1000 °C anomaly and a
   10 °C anomaly decay with the same $\tau$. The size of an intrusion sets how
   much heat there is; the geometry and diffusivity set how fast it leaves.
3. **The total relaxation is finite and equals $\tau$.** Because
   $\int_0^\infty e^{-t/\tau}dt = \tau$, the area under the decaying curve is
   $\tau y_0$ — a useful way to read a time constant off a plot, and the reason
   a "residence time" is an integral of a decay curve.

A caution about what the equation does **not** say. $y' = -\lambda y$ asserts
that the rate depends only on the current amount and not at all on history,
temperature, or the presence of daughter products. That is why radioactive
decay is a *clock*: the decay probability per unit time is independent of
everything the sample has experienced. It is also why thermal relaxation is
*not* a clock: $\kappa$ depends on temperature, saturation and mineralogy, all
of which change during cooling. **The same equation is a reliable clock in one
application and an unreliable one in the other, for a physical reason that
lives in the coefficient, not in the solution.**

## 5. Python demonstration

The companion script is
[`code/first_order_odes_demo.py`](./code/first_order_odes_demo.py). It runs
with the standard library only. Predict each printed number before running it,
then compare.

What it establishes, section by section, is:

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | Euler is first order, RK4 fourth order | Euler error ratio 2.03, 2.02, 2.01; RK4 ratio 17.40, 16.68, 16.34 as $h$ halves |
| 2 | The age equation inverts the decay law | age 3352 yr for $A_0/A = 1.5$; residual $0.000\times10^{0}$ |
| 3 | Branching matters for K–Ar | Rb–Sr 3.449 Ga; K–Ar 164.4 Ma; both ratios recovered exactly |
| 4 | The lumped cooling time | $\tau = 79.2$ yr; 1100 °C → 200 °C in 182.4 yr; RK4 gives 200.000 °C |
| 5 | Aquifer head relaxation | $\tau = 0.469$ d; 5 m → 0.593 m in 1 d; RK4 matches to 6 decimals |
| 6 | Approach to a forced equilibrium | drawdown tracks $h_\infty(1-e^{-t/\tau})$ to 5 decimals |
| 7 | The same ODE in circuits | $\tau = 1.000$ s (RC), 0.0500 s (RL) |
| 8 | Integrating factor on a forced problem | residual $< 7\times10^{-13}$ for $y' + 2y = 4x$ |

The convergence-order table is the one to read carefully, because it shows how
to *measure* an order rather than assert one. Halving the step halves the Euler
error (ratio 2.03) and divides the RK4 error by about 16 (ratios 17.4, 16.7,
16.3). The ratios drift toward the asymptotic values 2 and 16 as $h$ shrinks,
which is what "order" means: it is a statement about the limit, not about any
one step size.

> **Breaking exercise.** In Section 1, replace $\lambda = 1$ with
> $\lambda = 50$ and keep $h = 0.2$. Predict whether the errors will grow or
> shrink before running it, and explain your prediction in terms of $h\lambda$.

## 6. Exercises

Attempt these closed-book. The exercise set is
[`exercises/01-first-order-odes-exercises.md`](./exercises/01-first-order-odes-exercises.md)
and the fully worked solutions are
[`exercises/01-first-order-odes-solutions.md`](./exercises/01-first-order-odes-solutions.md).

## 7. Common mistakes

1. **Confusing $\tau$ with $t_{1/2}$.** They differ by $\ln 2$. State which one
   you mean every time you quote a number.
2. **Forgetting the constant of integration, or fixing it after the fact.**
   Impose $y(0)$ on the *general* solution; do not guess a form and then adjust
   it.
3. **Dividing by $h(y)$ without listing the constant solutions.** With
   $y' = y(1-y)$, the solutions $y \equiv 0$ and $y \equiv 1$ are lost by the
   separation step and must be recovered separately.
4. **Applying an exponential law where the coefficient depends on the state.**
   $y' = -\lambda y$ has an exponential solution *only* because $\lambda$ is
   constant. If $\lambda$ depends on $y$ (as in thermal relaxation with a
   temperature-dependent $\kappa$) the solution is not exponential, and quoting
   a half-life is meaningless.
5. **Using the wrong $L$.** The cooling time went as $L^2$ and the drainage
   time as $S L^2/T$. Dimensional analysis of the *coefficient* catches this;
   dimensional analysis of the *solution* does not.
6. **Ignoring branching ratios in dating.** The K–Ar example above is wrong by
   a factor of nine if the branch is ignored.
7. **Trusting first-order Euler on a long run.** Its global error is
   $O(h)$, so a decade of simulated time needs a small step, and the error
   accumulates rather than cancelling.

## 8. Real-world applications

- **Radiometric dating.** Rb–Sr, K–Ar, U–Pb and Sm–Nd geochronology are all
  the age equation of Section 3.3. The chemistry enters through the isochron
  construction, which removes the unknown initial daughter; the mathematics is
  this lesson. See
  [04-03-03 Radiometric Dating Methods](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md).
- **Radiocarbon calibration.** The physical decay law is exact; the
  *atmospheric* $^{14}\mathrm{C}$ production rate is not, which is why
  radiocarbon ages are converted to calendar ages through a calibration curve.
  The ODE is the easy part.
- **Cooling of intrusions and lava flows.** Lava-lake cooling, sill
  emplacement and hydrothermal circulation all begin from the relaxation
  timescale above. The lumped estimate is the standard first look.
- **Aquifer response and pumping tests.** The lumped $\tau$ gives the timescale
  over which a pumping test reaches steady state, and therefore whether the
  Theis solution's exponential integral has time to approach its
  large-$t$ logarithm. See
  [14-01-03 Hydraulic Head and Darcy's Law](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/03-hydraulic-head-darcy.md).
- **Electromagnetic and IP transients.** Time-domain EM systems and induced
  polarisation receivers are specified by their decay curve, and the earliest
  usable time is set by the transmitter/receiver $L/R$ and $RC$ constants.
- **Chemical weathering and residence times.** The residence time of an
  element in the ocean, of water in an aquifer, or of magma in a chamber is a
  first-order decay constant's reciprocal, and it is estimated the same way.

## 9. Further reading

- **Boyce, W. E., & DiPrima, R. C. *Elementary Differential Equations and
  Boundary Value Problems.* Wiley.** Chapters 1–3. Level: intermediate. The
  clearest treatment of separable and linear first-order equations, with
  extensive worked examples and a good discussion of when solutions exist and
  are unique.
- **Coddington, E. A., & Levinson, N. *Theory of Ordinary Differential
  Equations.* McGraw-Hill.** Chapters 1–2. Level: advanced. The existence and
  uniqueness theorem for $y' = f(x,y)$ is stated and proved here; read it once
  so that you know which equations have solutions before you try to find them.
- **Turcotte, D. L., & Schubert, G. *Geodynamics.* Cambridge University
  Press.** The thermal-problems chapter. Level: advanced. The cooling-time
  scalings used in Section 3.4, and the places where a lumped model is and is
  not admissible.
- **Carslaw, H. S., & Jaeger, J. C. *Conduction of Heat in Solids.* Oxford
  University Press.** Level: advanced. The reference for what replaces the
  lumped model once the internal gradient matters.
- **Faure, G. *Principles of Isotope Geology.* Wiley; and Dickin, A. P.
  *Radiogenic Isotope Geology.* Cambridge University Press.** Level:
  intermediate to advanced. The dating equations of Section 3.3 in their
  geological setting, including the isochron method.
- **Butcher, J. C. *Numerical Methods for Ordinary Differential Equations.*
  Wiley.** Chapters 1–3. Level: advanced. The order theory behind the
  convergence table of Section 5.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  where a second initial condition replaces the single constant of integration.
- [04 Systems of ODEs, Phase Portraits and Stability](./04-systems-of-odes.md) —
  what happens when several first-order equations are coupled.
- [07 Stiff Systems and Numerical Stability Challenges](./07-stiff-systems.md) —
  when the first-order equation has a very short $\tau$ and an explicit method
  cannot be used.
- [01-02-03 Exponentials, Logarithms and Decay Laws](../02-algebra/03-exponentials-logarithms.md) —
  the algebra of the exponential and its half-life.
- [01-09-02 The Diffusion/Heat Equation](../09-partial-differential-equations/02-heat-equation.md) —
  the honest version of the cooling calculation in Section 3.4.
- [14-01-03 Hydraulic Head and Darcy's Law](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/03-hydraulic-head-darcy.md) —
  where the aquifer time constant comes from.
- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md) —
  the physics of the decay constant used here.
- [01-11-04 The Laplace Transform and Transient Problems](../11-complex-analysis/04-laplace-transform.md) —
  a systematic way to solve forced first-order problems, including
  discontinuous sources.

## Self-assessment checklist

- [ ] I can classify a first-order ODE as separable, linear, or neither.
      (Section 2)
- [ ] I can solve a separable equation and state which constant solutions the
      method loses. (Section 2.1, Section 7.3)
- [ ] I can derive the integrating factor from the product rule rather than
      quote it, and use it on a non-standard form. (Section 3.2)
- [ ] I can convert between $\tau$ and $t_{1/2}$ in both directions without
      looking up $\ln 2$. (Section 3.1)
- [ ] I can write the age equation with and without a branching ratio, and
      compute an age from a measured ratio. (Section 3.3)
- [ ] I can state the relaxation time of a cooling body, a draining aquifer and
      an RC circuit, and say which length or volume appears and why.
      (Section 3.4)
- [ ] I can verify a claimed solution by substituting it into the ODE. (3 checks
      in Section 3.2)
- [ ] I can measure the order of a numerical method from a convergence table.
      (Section 5)
