---
id: 01-02-02
title: "Functions, Graphs and Transformations"
level: beginner
prereqs: ["01-02-01"]
estimated_minutes: 75
tags: [functions, graphs, transformations, inverse-functions]
---

# Functions, Graphs and Transformations

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the definition of a function including its domain, and explain why
   changing the domain changes the function.
2. **Sketch** and read the graphs of the four families that dominate geophysics:
   linear, polynomial, exponential and rational.
3. **Predict** how a graph changes under shifts, scalings and reflections, and
   connect each transformation to a survey operation (offset, gain, polarity).
4. **Identify** symmetry, monotonicity and asymptotes from the formula alone.
5. **Decide** whether an inverse function exists on a stated domain, and
   construct it when it does.

## Prerequisites

[01-02-01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
for rearranging and solving. This lesson also uses the graphical vocabulary of
arithmetic lessons
[01-01-01](../01-arithmetic/01-number-systems-and-precision.md) and
[01-01-02](../01-arithmetic/02-orders-of-magnitude.md) for scale.

## 1. Intuition: a physical law is a function with a domain

When we write that the two-way travel time to a reflector at depth $d$ in a
medium of speed $v$ is

$$t(d) = \frac{2d}{v},$$

we are stating a *function*: a rule that takes a depth and returns a time. But we
are also stating its domain, usually without saying so:

$$d \ge 0, \qquad v > 0.$$

Negative depths and zero velocities are outside the domain. Every physical
formula carries such restrictions, and a formula divorced from its domain can
produce nonsense: $t(-100)$ is a perfectly good number and a meaningless arrival
time.

This lesson is about reading functions as pictures (graphs) and as rules
(transformations, inverses). The habits are the ones that let you look at a
record section, an anomaly profile, or a temperature log and say what the shape
implies about the process.

## 2. Definitions

### 2.1 Function, domain, range

A **function** $f$ is a rule that assigns to each element $x$ of a set $D$, its
**domain**, exactly one element $f(x)$ of a set. The **range** is the set of
values actually taken:

$$\text{range} = \{\,f(x) : x \in D\,\}.$$

Three consequences that beginners skip and practitioners cannot:

- The **domain is part of the function**. $f(x) = 1/(1+x^{2})$ on
  $x \in \mathbb{R}$ and the same formula restricted to $x \ge 0$ are different
  functions.
- Every $x$ in $D$ must give exactly one $f(x)$. A "function" that returns two
  values for one input (a travel time with two arrivals, say) must be separated
  into branches or replaced by a relation.
- The **range** is often what the physics constrains. A Newton-cooling law
  $T(t) = T_\infty + (T_0 - T_\infty)e^{-t/\tau}$ has range
  $(T_\infty, T_0]$ for $t \ge 0$ — the body can never be cooler than its
  surroundings.

**Graph.** The graph is the set of points $(x, f(x))$ in the plane. The
**vertical line test** is the graphical version of "exactly one output": if any
vertical line meets the graph more than once, it is not a graph of a function.

### 2.2 Domains that physics imposes

| function | natural domain | geophysical restriction |
|---|---|---|
| $\dfrac{2d}{v}$ | $v \ne 0$ | $v > 0$, $d \ge 0$ |
| $\dfrac{GM}{d^{2}}$ | $d \ne 0$ | $d > 0$ (depth or distance) |
| $\ln x$ | $x > 0$ | $x > 0$ (a ratio of activities, an amplitude) |
| $\sqrt{x}$ | $x \ge 0$ | $x \ge 0$ (a squared quantity) |
| $\arcsin x$ | $-1 \le x \le 1$ | $|\sin\theta| \le 1$, i.e. $v_1 \le v_2$ |
| $\tan x$ | $x \ne \pi/2 + k\pi$ | horizontal distance $> 0$ for a dip calculation |

Listing the domain is not pedantry: the last row is exactly why a vertical
incidence computation returns nonsense.

## 3. Four families that run geophysics

### 3.1 Linear: $f(x) = f_0 + mx$

Constant rate of change, straight graph, slope $m$ everywhere. A geothermal
profile $T(z) = T_0 + \gamma z$; depth from a constant velocity; a calibration
line between count rate and concentration.

**Signature:** equal steps in $x$ produce equal steps in $f$. If your data
double the input and not much else changes, it is not linear.

### 3.2 Polynomial: $f(x) = a_nx^{n} + \dots + a_1x + a_0$

The local shape is set by the roots; the global shape by the leading term. Full
treatment is in [01-02-04](./04-polynomials-roots.md); here it is enough to know
that a quadratic bends once, a cubic bends twice, and the number of turning
points is at most one less than the degree.

### 3.3 Exponential: $f(x) = A e^{kx}$

Constant **relative** rate of change. Doubling time (for $k>0$) or half-life
(for $k<0$) is fixed. Radioactive decay, seismic attenuation, Newton cooling,
and the temperature dependence of any Arrhenius process. Developed in
[01-02-03](./03-exponentials-logarithms.md).

**Signature:** equal steps in $x$ multiply $f$ by a constant factor. The
demonstration's table makes this visible: at $x=1,2,\dots,10$ the values
$2^{x}$ are $2, 4, 8, \dots, 1024$, doubling every step, while $2x$ grows by 2
and $x^{2}$ by increasing amounts.

### 3.4 Rational: ratio of polynomials, e.g. $f(x) = \dfrac{1}{1+x^{2}}$

Smooth, bounded, and with asymptotes where the denominator vanishes or as
$|x| \to \infty$. Many *sensitivity* and *kernel* functions have this shape: the
response of an instrument to a source at distance, a filter's amplitude response,
and the shape of a potential-field anomaly over a compact body.

## 4. Symmetry, monotonicity and asymptotes

- **Even**: $f(-x) = f(x)$; the graph is symmetric about the $x = 0$ axis.
  Example: $f(x) = 1/(1+x^{2})$.
- **Odd**: $f(-x) = -f(x)$; the graph has rotational symmetry about the origin.
  Example: $f(x) = x^{3}$.
- **Neither** is the common case, but every function on a symmetric domain splits
  uniquely into an even and an odd part:

$$f_{\text{even}}(x) = \frac{f(x) + f(-x)}{2}, \qquad
f_{\text{odd}}(x) = \frac{f(x) - f(-x)}{2}.$$

For $f(x) = 1 + x + x^{3}$ the split is even part $1$, odd part $x + x^{3}$;
the demonstration confirms it numerically at $x = \pm1, \pm2$.

- **Monotonic increasing** on an interval: $x_1 < x_2 \Rightarrow f(x_1) <
  f(x_2)$. Monotonicity is what makes an inverse function possible.
- **Asymptote.** A line the graph approaches. Horizontal asymptotes come from the
  behaviour as $x \to \pm\infty$ (take the leading terms); vertical asymptotes
  from where the denominator vanishes with a nonzero numerator.

**Reading asymptotics from the formula.** For large $z$, $z/(1+z) = 1/(1 + 1/z)
\to 1$; the demonstration gives $0.999990$ at $z = 10^{5}$, confirming the
approach and showing how slowly it happens. The same table shows
$\left(1 + 1/z\right)^{z} \to e = 2.718281828\ldots$ from below: at $z = 10^{5}$
it is $2.718268$, still four parts in $10^{6}$ short. **Asymptotic behaviour is
often slow**, and "the limit is 1" is not the same statement as "at the depths you
care about, it is 1".

## 5. Transformations, and what they mean in a survey

| transformation | effect on graph | survey language |
|---|---|---|
| $f(x) + c$ | shift up by $c$ | adding a datum baseline / regional field |
| $f(x - c)$ | shift **right** by $c$ | a delayed arrival, an offset source |
| $a f(x)$, $a > 0$ | vertical stretch by $a$ | gain, scaling of amplitudes |
| $f(ax)$ | horizontal compression by $1/a$ | time-axis scaling on a display |
| $-f(x)$ | reflection in the $x$-axis | polarity reversal |
| $f(-x)$ | reflection in the $y$-axis | reversing the direction of a profile |

Two rules worth memorising because they are the ones people get backwards:

1. Inside the bracket acts **oppositely**: $f(x-2)$ moves the graph *right*, not
   left.
2. Inside the bracket acts on the **input**, so a horizontal compression by 2
   happens before any shift you write outside.

The demonstration confirms the algebra numerically for the bump
$f(x) = 1/(1+x^{2})$: the peak at $x=0$ with height $1$ becomes a peak at
$x = +1.00$ with height $1.0000$ under $f(x-1)$, height $1.5000$ under
$f(x)+0.5$, height $2.0000$ under $2f(x)$, and $-1.0000$ at $x=0$ under $-f(x)$.

## 6. Inverses: when you can go back

A function $f$ on a domain $D$ has an **inverse** $f^{-1}$ if and only if it is
one-to-one on $D$: distinct inputs give distinct outputs. A sufficient condition
(and in practice the one you use) is **strict monotonicity**.

The graph of $f^{-1}$ is the graph of $f$ reflected in the line $y = x$; the
algebra is "solve $y = f(x)$ for $x$".

**Geophysical example.** With $t(d) = 2d/v$ on $d \ge 0$, the function is
strictly increasing, so it is invertible:

$$d(t) = \frac{vt}{2}, \qquad t \ge 0.$$

The demonstration checks the round trip at three depths ($1000$, $5000$ and
$30000$ m with $v = 6000$ m/s). The printed recovered depths are
`1000.000000`, `5000.000000` and `30000.000000` m — exact to the displayed
precision — which is what a successful inverse looks like.

**Where inverses fail.** $f(x) = x^{2}$ on all of $\mathbb{R}$ is not
one-to-one, so it has no inverse; restricted to $x \ge 0$ it has one, $f^{-1}(y) =
\sqrt{y}$. This is not a technicality — it is exactly the reason that solving
$d = \sqrt{GM/g}$ returns only the positive root in
[01-02-01](./01-algebraic-manipulation.md), Section 5.2. **Choosing the domain
is choosing the inverse.**

## 7. Worked derivations

### 7.1 Composition, and why order matters

Given a temperature profile in depth and a depth as a function of time (for a
slowly subsiding basin, say), the temperature as a function of time is the
**composition**

$$T(t) = T_{\text{profile}}\big(z(t)\big).$$

Composition is not commutative in general. With $f(x) = 2x$ and $g(x) = x + 1$:
$f(g(x)) = 2x + 2$ but $g(f(x)) = 2x + 1$. Numerically at $x = 3$: 8 versus 7.
Whenever you chain models — a rock-physics law feeding a velocity model feeding a
travel time — the order of application is part of the model, not an
implementation detail.

### 7.2 Splitting a function into even and odd parts

Claim: every function on a symmetric domain can be written uniquely as
$f = f_e + f_o$ with $f_e$ even and $f_o$ odd.

*Proof of the formula.* Suppose such a decomposition exists. Then

$$f(x) = f_e(x) + f_o(x), \qquad f(-x) = f_e(x) - f_o(x).$$

Adding gives $f_e(x) = \tfrac{1}{2}[f(x) + f(-x)]$ and subtracting gives
$f_o(x) = \tfrac{1}{2}[f(x) - f(-x)]$, which proves both existence and uniqueness.

*Check with a real function.* For $f(x) = 1 + x + x^{3}$: $f(2) = 11$,
$f(-2) = -9$, so $f_e(2) = (11 - 9)/2 = 1$ and $f_o(2) = (11 + 9)/2 = 10$,
and indeed the even part is the constant $1$ and the odd part is $x + x^{3}$
evaluated at 2, i.e. $10$. The demonstration prints exactly these values.

*Why it matters.* Decomposing a signal or a field into symmetric and
antisymmetric parts is a standard diagnostic: a symmetric anomaly suggests a
centred body, while an antisymmetric one suggests a gradient, a contact or a
dyke.

### 7.3 Average rate of change, and the road to the derivative

The **average rate of change** of $f$ over $[a, b]$ is

$$\frac{f(b) - f(a)}{b - a}.$$

For the linear geothermal profile $T(z) = 10 + 25z$ this is $25\,^\circ$C/km over
*every* interval, which is the distinguishing property of a linear function. For
any other function the average rate depends on the interval: it is the slope of
the **secant** line. Taking the limit as the interval shrinks gives the derivative,
which is the subject of
[01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md).

### 7.4 Horizontal asymptotes from leading terms

For a ratio of polynomials, divide numerator and denominator by the highest power
of $x$ and take the limit. For example

$$\frac{3x^{2} + 2x}{x^{2} + 5} = \frac{3 + 2/x}{1 + 5/x^{2}}
\;\xrightarrow[x\to\infty]{}\; 3.$$

The rule of thumb is: compare degrees — equal degrees give the ratio of leading
coefficients (a horizontal asymptote), numerator degree larger gives growth like a
power (no horizontal asymptote), denominator degree larger gives $0$. Because
this is a statement about limits, it must be read as "at the scales where the
leading terms dominate", exactly as in [01-01-02](../01-arithmetic/02-orders-of-magnitude.md).

### 7.5 The slow approach to $e$

The limit

$$\lim_{z\to\infty}\left(1 + \frac{1}{z}\right)^{z} = e$$

is the definition of the base of the natural logarithm, and it appears whenever
compounding happens continuously. The demonstration's table shows the approach
from below: $2.000000$ at $z=1$, $2.593742$ at $z=10$, $2.704814$ at $z=100$,
$2.716924$ at $z=1000$ and $2.718268$ at $z=10^{5}$, against
$e = 2.718281828$. At $z = 10^{5}$ the residual is $1.4\times10^{-5}$: the limit
is approached, slowly, from below.

## 8. Python demonstration

```bash
python3 code/functions_demo.py
```

`code/functions_demo.py` uses only the standard library — including a small
ASCII plotter, so that shape can be *seen* without a plotting package. It covers:
a function and its inverse checked by composition; the transformation table of
Section 5; the linear/quadratic/exponential comparison; average rates of change;
even–odd splitting; an asymptotic table; and a damped-oscillation plot.

Observed output worth dwelling on:

```text
    x         2x       x**2         2**x
    5         10         25           32
   10         20        100         1024
```

```text
  z (km)      z/(1+z)     1 - 1/(1+z**2)     (1+1/z)**z
       1     0.500000        0.500000000       2.000000
   100000     0.999990        1.000000000       2.718268
```

| Observation | Consequence in geophysics |
|---|---|
| the exponential overtakes both others | growth and decay laws must be written exponentially, not polynomially |
| the linear function has one slope everywhere | a curved temperature log means the profile is not purely conductive |
| $z/(1+z)$ needs $z \sim 10^{5}$ to reach 1 in the fifth digit | "asymptotically flat" is a statement about a scale |
| the round trip $f \circ f^{-1}$ returns the input | invertibility is a checkable property, not an assumption |
| $\left(1+1/z\right)^{z}$ approaches $e$ from below | limits are approached, not attained; report the residual |

## 9. Exercises

Ten graded exercises with worked solutions are in
[`exercises/02-functions-and-graphs-exercises.md`](./exercises/02-functions-and-graphs-exercises.md)
and
[`exercises/02-functions-and-graphs-solutions.md`](./exercises/02-functions-and-graphs-solutions.md).

**★1.** State the natural domain of each:
(a) $\dfrac{GM}{d^{2}}$, (b) $\ln(D/D_0)$, (c) $\sqrt{GM/g}$.

**★★2.** $f(x) = 1/(1+x^{2})$ has its peak at $x = 0$. Where is the peak of
$g(x) = f(x-3)$, and what is its height? Where is the peak of
$h(x) = f(2x) + 1$?

**★★★3.** Design and run an experiment that measures how far the finite-$z$
values of $(1+1/z)^{z}$ are from $e$ as a function of $z$, fit the leading
correction, and state the limits of your fit.

## 10. Common mistakes

1. **Ignoring the domain.** A formula without its domain is not a function, and
   negative depths and zero denominators are physical, not hypothetical.
2. **Shifting the wrong way.** $f(x - 2)$ moves the graph right; the minus sign
   acts backwards because it acts on the input.
3. **Assuming every function has an inverse.** $x^{2}$ does not, until you restrict
   the domain; monotonicity is the check.
4. **Treating a log-linear plot as proof of an exponential.** A power law is also
   straight on log–log axes; fit the residual before naming the mechanism.
5. **Reading asymptotes as achieved values.** $z/(1+z)$ differs from 1 in the fifth
   digit only at $z \approx 10^{5}$.
6. **Forgetting that composition order matters.** $f(g(x)) \ne g(f(x))$ in
   general, and the physical model usually dictates the order.

## 11. Real-world applications

- **Potential-field profiles.** The shape $1/(1+x^{2})$-like kernel is what makes
  an anomaly width a depth indicator; transforming the profile (upward
  continuation, filtering) is a transformation in the sense of Section 5.
- **Temperature logs.** A linear segment indicates conductive gradient; a curved
  segment indicates advection, a transient, or a change in conductivity, and the
  sign of the curvature is diagnostic.
- **Time–depth conversion.** Inverting a monotonic velocity–depth function is how
  a time section becomes a depth section; non-monotonic velocity requires care
  precisely because the inverse does not exist.
- **Instrument response.** Gain and phase responses are functions whose
  asymptotes and pass-band shape determine what the instrument can measure.
- **Decay and dating.** The one-to-one property of the exponential map on
  $[0,\infty)$ is what makes an age uniquely recoverable from an activity ratio.

## 12. Further reading

- **Stewart, J. *Calculus: Early Transcendentals* (current edition).** Chapter 1
  (functions, transformations, inverse functions) and Section 2.1 (average rate of
  change). Level: beginner. The clearest treatment of the material in Sections
  2–7 here.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd
  ed.). Wiley.** Chapters 1–3. Level: beginner to intermediate. Physics-flavoured
  examples, including graphing and inverse relations.
- **Bronshtein, I. N., Semendyayev, K. A., Musiol, G., & Mühlig, H. *Handbook of
  Mathematics* (current edition). Springer.** Level: reference. For a compact
  summary of elementary function properties and identities.
- **Kreyszig, E. *Advanced Engineering Mathematics* (current edition).** Chapters
  1–2. Level: intermediate. Useful for the engineering-style treatment of
  graphs, series and transforms.

> Note on citations: bibliographic details are given so you can locate the works;
> textbook printings vary and page numbers are deliberately omitted where they
> differ between editions. This repository does not reproduce copyrighted text.

## 13. Related lessons

- [01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
  — the algebra used to find inverses and asymptotes.
- [03 Exponentials, Logarithms and Decay Laws](./03-exponentials-logarithms.md)
  — Section 3.3 in depth.
- [04 Polynomials, Roots and Asymptotic Behaviour](./04-polynomials-roots.md)
  — Section 3.2 in depth.
- [01-03 Trigonometry](../03-trigonometry/README.md) — periodic functions, the
  family this lesson deliberately left out.
- [01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  the derivative, which is the limit of the average rate of change of Section 7.3.

## Self-assessment checklist

- [ ] I can state the domain of a physical formula and say which values are
      excluded and why.
- [ ] I can sketch the four function families from memory and label the features
      that identify them.
- [ ] I can predict the effect of a shift, a scaling and a reflection.
- [ ] I can decide whether an inverse exists on a stated domain.
- [ ] I can estimate a horizontal asymptote from leading terms.
- [ ] I can split a function into even and odd parts.
