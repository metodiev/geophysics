---
id: 01-11-04
title: "The Laplace Transform and Transient Problems"
level: graduate
prereqs: ["01-11-03", "01-08-01"]
estimated_minutes: 90
tags: [laplace-transform, transients, bromwich-contour, diffusion, stability]
---

# The Laplace Transform and Transient Problems

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the one-sided Laplace transform, state its region of convergence,
   and explain why the one-sided version is the right tool for initial-value
   problems.
2. **Derive** the transform of the elementary functions and of a derivative from
   the integral, and explain how initial conditions enter the algebra
   automatically.
3. **Solve** a first-order and a second-order transient problem by transforming,
   solving algebraically, and inverting.
4. **Invert** by the Bromwich contour, by partial fractions and by residues, and
   explain what the closing arc contributes and why.
5. **Interpret** pole locations as decay rates and oscillation frequencies, and
   read stability off the left half plane.
6. **Recognise** a branch point and explain why a diffusive transient has no
   single decay time; invert $e^{-a\sqrt s}/s$ to the complementary error
   function and verify it against a finite-difference solution of the diffusion
   equation.
7. **Verify** a transform solution against a direct numerical integration of the
   differential equation, and state what each check rules out.

## Prerequisites

[01-11-03 Contour Integration, Residues and Real
Integrals](./03-contour-integration.md) — residues and the closing-arc argument,
which are the inversion machinery;
[01-08-01 First-Order ODEs](../08-ordinary-differential-equations/01-first-order-odes.md) —
linear initial-value problems, whose solution this lesson mechanises.

## 1. Intuition: steady state is a special case of a transient

Everything in [01-11-01](./01-complex-arithmetic.md) assumed a system that had
been running forever, driven by a sinusoid, so that the answer was a sinusoid of
the same frequency. Field data are not like that. A seismometer is switched on,
a current is stepped into a coil, a temperature is changed at the surface, an
earthquake ruptures. What is measured is a **transient**: a response that starts
at a definite time and decays, oscillates or diffuses away.

The Laplace transform is the tool built for that situation:

$$F(s) = \mathcal{L}\{f\}(s) = \int_{0}^{\infty} f(t)\,e^{-st}\,\mathrm{d}t,
\qquad \operatorname{Re}s > \sigma_{0},$$

with $s$ a complex variable. Three features do all the work:

1. **The lower limit is $0$, not $-\infty$.** Signals of interest start at a
   definite time, and the one-sided transform ignores the past. It also means the
   integral only converges for $\operatorname{Re}s$ large enough — the **region
   of convergence** — which is information, not a technicality.
2. **Differentiation becomes multiplication.** Integrating
   $\int_{0}^{\infty}f'(t)e^{-st}\mathrm{d}t$ by parts gives $sF(s)-f(0)$, so
   initial conditions enter as explicit terms. A differential equation becomes an
   algebraic equation in $s$ and **the initial conditions are carried along**
   rather than imposed afterwards.
3. **Inversion is a contour integral**, so the machinery of
   [03 Contour Integration](./03-contour-integration.md) applies: the solution is
   a sum of residues at the poles of $F(s)$, plus, when $F$ has a branch point
   rather than a pole, a genuinely different answer.

Points 2 and 3 are why the Laplace transform is not just the Fourier transform
with a complex frequency. The Fourier transform knows nothing about initial
conditions and cannot represent a growing exponential. The Laplace transform
handles both, at the price of an inversion contour that must be chosen.

## 2. Definitions and the shape of the $s$ plane

### 2.1 The pair

$$F(s) = \int_{0}^{\infty}f(t)e^{-st}\,\mathrm{d}t
\qquad\text{(forward)},$$

$$f(t) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}F(s)e^{st}\,\mathrm{d}s,
\qquad t > 0 \qquad\text{(inverse, Bromwich contour)},$$

where $c$ is any real number to the right of every singularity of $F$. The
inversion integral is a vertical line in the complex plane, and the whole
practical content of inversion is that this line may be deformed to the left
until it wraps around the singularities.

### 2.2 The Fourier transform is the boundary case

With the Fourier convention of
[01-10-02 The Fourier
Transform](../10-fourier-analysis/02-fourier-transform.md), $X(\omega) =
\int x(t)e^{-i\omega t}\mathrm{d}t$, the substitution $s = i\omega$ shows

$$X(\omega) = \mathcal{L}\{x\}(i\omega),$$

provided the region of convergence includes the imaginary axis. So the Fourier
transform is the Laplace transform on the imaginary axis, and the difference
between them is entirely about which part of the plane is available:

| question | Laplace | Fourier |
|---|---|---|
| growing or decaying exponential | pole at $s = -a$, all $a$ | only $\operatorname{Re}(i\omega) = 0$ |
| initial conditions | carried explicitly | not representable |
| stability | left half plane | not visible |
| steady-state sinusoid | pole on the imaginary axis | the whole domain |

A system is **stable** when every pole of $F(s)$ satisfies
$\operatorname{Re}s < 0$: then $f(t)\to 0$. A pole at $s = -\sigma$ contributes
$e^{-\sigma t}$, with **time constant** $1/\sigma$. A pole at
$s = -\sigma \pm i\omega_{d}$ contributes $e^{-\sigma t}\cos(\omega_{d}t + \cdot)$:
the real part is the decay, the imaginary part is the ringing. Reading a pole is
therefore reading a transient, and this is the same statement as the pole
reading in [05 The z-Transform](./05-z-transform.md), one plane over.

### 2.3 Region of convergence, with the one example that matters

For $f(t) = e^{at}$, $\mathcal{L}\{f\}(s) = 1/(s-a)$ for $\operatorname{Re}s >
a$ only. The algebraic formula $1/(s-a)$ is the same function everywhere, but it
*represents the transform of $e^{at}$* only in that half plane; in
$\operatorname{Re}s < a$ the same formula is the transform of a different
function (the anti-causal $e^{at}$ continued backwards). Two different time
functions share one algebraic expression, and the region of convergence is what
distinguishes them. This is exactly the phenomenon met in
[01-11-05](./05-z-transform.md) for the $z$-transform and in
[01-11-03](./03-contour-integration.md) Section 3.4 for Laurent series, and it is
the reason a transform is a formula *plus* a region.

## 3. The table, derived rather than quoted

Each entry is one integration. The point of deriving them is that you will need
the two properties at the bottom far more often than the functions themselves.

| $f(t)$, $t>0$ | $F(s)$ | region | how |
|---|---|---|---|
| $1$ | $1/s$ | $\operatorname{Re}s>0$ | elementary |
| $t^{n}$ | $n!/s^{n+1}$ | $\operatorname{Re}s>0$ | integrate by parts $n$ times |
| $e^{at}$ | $1/(s-a)$ | $\operatorname{Re}s>a$ | elementary |
| $t^{n}e^{at}$ | $n!/(s-a)^{n+1}$ | $\operatorname{Re}s>a$ | shift property |
| $\sin\omega t$ | $\omega/(s^{2}+\omega^{2})$ | $\operatorname{Re}s>0$ | Euler's formula or two integrations by parts |
| $\cos\omega t$ | $s/(s^{2}+\omega^{2})$ | $\operatorname{Re}s>0$ | the companion |
| $e^{at}\cos\omega t$ | $(s-a)/[(s-a)^{2}+\omega^{2}]$ | $\operatorname{Re}s>a$ | shift property |
| $f'$ | $sF(s)-f(0)$ | | integrate by parts |
| $f''$ | $s^{2}F(s)-sf(0)-f'(0)$ | | apply twice |
| $\int_{0}^{t}f$ | $F(s)/s$ | | swap the order of integration |
| $e^{at}f(t)$ | $F(s-a)$ | shifted | substitute $u = e^{-(s-a)t}$ |
| $f(t-\tau)\Theta(t-\tau)$ | $e^{-s\tau}F(s)$ | | change variable |
| $f * g$ | $F(s)G(s)$ | intersection | Fubini |

The two derivations worth writing out are the derivative and the convolution.

**Derivative:**

$$\int_{0}^{\infty}f'(t)e^{-st}\mathrm{d}t
= \Bigl[f(t)e^{-st}\Bigr]_{0}^{\infty} + s\int_{0}^{\infty}f(t)e^{-st}\mathrm{d}t
= -f(0) + sF(s),$$

with $f(t)e^{-st}\to 0$ at $t\to\infty$ inside the region of convergence. This one
line is the reason the method works: **the initial condition $f(0)$ appears as an
explicit algebraic term**, not as an integration constant to be fixed later.

**Convolution:** with $(f*g)(t) = \int_{0}^{t}f(t-\tau)g(\tau)\mathrm{d}\tau$,

$$\mathcal{L}\{f*g\}(s) = \int_{0}^{\infty}\!\!\int_{0}^{t}
f(t-\tau)g(\tau)e^{-st}\,\mathrm{d}\tau\,\mathrm{d}t
= F(s)G(s),$$

after exchanging the order of integration and substituting $u = t-\tau$. So the
Laplace transform does for causal time-domain convolutions exactly what the
Fourier transform does for the whole-line version — and this is the origin of
the statement that a linear system is characterised by its transfer function.

## 4. Solving a transient problem, end to end

### 4.1 First order, three independent routes

Take

$$\dot y + a y = 1, \qquad y(0) = 0 .$$

Transform, using $y(0)=0$:

$$sY(s) - 0 + aY(s) = \frac{1}{s}
\qquad\Longrightarrow\qquad
Y(s) = \frac{1}{s(s+a)} .$$

Then invert. Partial fractions give $Y(s) = \frac{1}{a}\left(\frac{1}{s} -
\frac{1}{s+a}\right)$, hence

$$y(t) = \frac{1-e^{-at}}{a}\quad (t>0).$$

Very little human effort has been spent, and two facts are already visible from
$Y(s)$ alone: the pole at $s=0$ gives the constant final value, and the pole at
$s=-a$ gives the transient with time constant $1/a$.

With $a = 2$ the demo checks the result three ways: the closed form, a
fourth-order Runge–Kutta integration of the differential equation, and the
Bromwich integral evaluated numerically:

| $t$ | exact | RK4 | Bromwich | $\vert$Bromwich $-$ exact$\vert$ |
|---|---|---|---|---|
| 0.10 | 0.090634623461 | 0.090634623461 | 0.090540062005 | $9.5\times10^{-5}$ |
| 0.50 | 0.316060279414 | 0.316060279414 | 0.316095145455 | $3.5\times10^{-5}$ |
| 1.00 | 0.432332358382 | 0.432332358382 | 0.432469499625 | $1.4\times10^{-4}$ |
| 3.00 | 0.498760623912 | 0.498760623912 | 0.498598717332 | $1.6\times10^{-4}$ |

The RK4 column agrees with the closed form to the digits shown — it is integrating
the same equation that the transform solved. The Bromwich column is off by
$\sim10^{-4}$, and that residual is *not* an error of the closed form: it is the
piece of the contour that the quadrature truncated, which is the subject of
Section 4.3.

### 4.2 Residues of $F(s)e^{st}$

By the residue theorem applied to the left closure of the Bromwich contour, the
solution is the sum of residues of $F(s)e^{st}$. For $Y(s)e^{st} =
e^{st}/[s(s+2)]$ the poles are at $s = 0$ and $s = -2$, and

$$\operatorname{Res}_{0} = \frac{e^{0}}{2} = \frac12, \qquad
\operatorname{Res}_{-2} = \frac{e^{-2t}}{-2} = -\frac{e^{-2t}}{2},$$

so $y(t) = \frac12(1-e^{-2t})$. The demo computes both residues from small
circular contours:

| $t$ | $\operatorname{Res}$ at $0$ | $\operatorname{Res}$ at $-2$ | sum | exact $y(t)$ |
|---|---|---|---|---|
| 0.20 | 0.500000000000 | $-0.335160023018$ | 0.164839976982 | 0.164839976982 |
| 0.50 | 0.500000000000 | $-0.183939720586$ | 0.316060279414 | 0.316060279414 |
| 1.00 | 0.500000000000 | $-0.067667641618$ | 0.432332358382 | 0.432332358382 |
| 4.00 | 0.500000000000 | $-0.000167731314$ | 0.499832268686 | 0.499832268686 |

The residue at $s=0$ is constant and equal to the final value; the residue at
$s=-2$ decays with the time constant $1/2$. **Pole position is decay rate,
residue is amplitude** — the reading of a pole that recurs throughout the
curriculum.

### 4.3 What the closing arc contributes, measured

The Bromwich contour is a vertical line; to convert it into a residue sum you
close it to the left with a large arc. If the arc's contribution vanished, the
line integral would equal the residue sum. The demo measures both terms
separately at $t=1$, with $c=3$ and the arc a semicircle of radius $R$ centred at
$c$:

| $R$ | vertical line | arc$/(2\pi i)$ | line $+$ arc | sum of residues |
|---|---|---|---|---|
| 10 | 0.484012502416 | $-0.051784660702$ | 0.432227841714 | 0.432332358382 |
| 20 | 0.416968115387 | $0.015424518795$ | 0.432392634182 | 0.432332358382 |
| 40 | 0.429805522450 | $0.002545465188$ | 0.432350987638 | 0.432332358382 |
| 80 | 0.433328672469 | $-0.001012045303$ | 0.432316627165 | 0.432332358382 |
| 160 | 0.432286753056 | $0.000046954879$ | 0.432333707935 | 0.432332358382 |

Two facts, both instructive. The vertical line alone converges only like
$1/R$ — at $R = 160$ it is still wrong in the fourth decimal — while
**line plus arc equals the residue sum to within the accuracy of the arc
quadrature at every radius**. The closure is not an approximation that
eventually becomes true; it is an identity, and only the *split* between line and
arc varies with $R$.

The reason the split varies is that on the arc, $e^{st}$ decays like
$e^{R t\cos\theta}$ for $\cos\theta < 0$, so the arc contribution is
$O(e^{-R t})$ for $t>0$ — exponentially small but with a coefficient that
oscillates. That is also why the closure works only for $t > 0$: for $t<0$ the
exponential *grows* on the left arc and the closure must be taken to the right
instead, which is exactly why $f(t) = 0$ for $t<0$.

### 4.4 Second order: the underdamped step response

Take

$$\ddot x + 2\zeta\omega_{0}\dot x + \omega_{0}^{2}x = \omega_{0}^{2},
\qquad x(0) = \dot x(0) = 0 .$$

Transforming with both initial conditions equal to zero:

$$Y(s) = \frac{\omega_{0}^{2}}{s\bigl(s^{2}+2\zeta\omega_{0}s+\omega_{0}^{2}\bigr)},$$

whose non-zero poles are $s = -\zeta\omega_{0} \pm i\omega_{d}$ with
$\omega_{d} = \omega_{0}\sqrt{1-\zeta^{2}}$. The inverse is

$$x(t) = 1 - e^{-\zeta\omega_{0}t}\left(\cos\omega_{d}t +
\frac{\zeta\omega_{0}}{\omega_{d}}\sin\omega_{d}t\right).$$

With $\omega_{0} = 5$ and $\zeta = 0.25$ the poles are at
$-1.250000 \pm 4.841229i$, and

| $t$ | exact | RK4 | Bromwich | difference |
|---|---|---|---|---|
| 0.20 | 0.392945150833 | 0.392945150833 | 0.392943046173 | $2.1\times10^{-6}$ |
| 0.60 | 1.430559837736 | 1.430559837736 | 1.430558876976 | $9.6\times10^{-7}$ |
| 1.20 | 0.827722592984 | 0.827722592984 | 0.827721773027 | $8.2\times10^{-7}$ |
| 2.50 | 0.965764586911 | 0.965764586911 | 0.965752601312 | $1.2\times10^{-5}$ |

The overshoot past the final value of $1$ is visible in the table
($1.4306$ at $t = 0.6$), and it comes from the complex poles: a decaying
exponential times a cosine cannot approach $1$ monotonically. The real part
$-1.25$ is the decay constant, so the envelope time constant is $0.8$ s and after
about four of those the ringing has gone.

### 4.5 Two limits you can read off without inverting

Two theorems are worth having because they turn a transform into a check.

**Initial value.** If $f$ has no impulse at $t=0$,
$f(0^{+}) = \lim_{s\to\infty}sF(s)$, provided the limit exists. For
$Y(s) = 1/[s(s+2)]$ this gives $sY = 1/(s+2) \to 0$ as $s\to\infty$, agreeing
with the table of Section 4.1 where $y(0) = 0$.

**Final value.** If every pole of $sF(s)$ lies in $\operatorname{Re}s < 0$ except
possibly a simple pole at $s = 0$, then
$f(\infty) = \lim_{s\to0}sF(s)$. For the same $Y$, $sY\to1/2$ as $s\to0$, which is
the constant residue $0.500000000000$ printed in Section 4.2. For the
second-order step response of Section 4.4, $sY\to1$: the final value is $1$, as
the table's approach from $0.9658$ at $t = 2.5$ shows. For the diffusive
$F(s) = e^{-a\sqrt s}/s$ the final value theorem gives $sF\to1$, so $f(\infty) = 1$,
consistent with $\operatorname{erfc}(0) = 1$.

The final value theorem is the one that catches errors. It fails exactly when the
hypothesis fails: with a pole on the imaginary axis the limit does not exist (an
undamped oscillation), and with a pole in the right half plane the limit is
infinite (an unstable system). Applying it to a system with a pole at
$s = +1$ returns a finite number that means nothing.

## 5. When there is no pole: diffusion and the branch point

### 5.1 The transient that has no time constant

Consider

$$F(s) = \frac{e^{-a\sqrt s}}{s} .$$

There is no pole anywhere except at $s = 0$, and $s = 0$ is a **branch point**
of $\sqrt s$, not a pole: $\sqrt s$ is not single-valued in any punctured disc
about the origin. The inversion therefore cannot be a residue sum, and the
answer is not a sum of exponentials. It is

$$f(t) = \operatorname{erfc}\!\left(\frac{a}{2\sqrt t}\right),$$

the complementary error function — a function with no characteristic time at all,
which is precisely why diffusion looks the way it does.

The demo computes the Bromwich integral numerically (with $c=1$ and a
truncated range $|\omega| \le 800$) and compares with `math.erfc`:

| $t$ | Bromwich | $\operatorname{erfc}(a/(2\sqrt t))$ | difference |
|---|---|---|---|
| 0.20 | 0.017706065807 | 0.017706065807 | $3.7\times10^{-16}$ |
| 0.50 | 0.133614402538 | 0.133614402538 | $1.9\times10^{-15}$ |
| 1.00 | 0.288844366346 | 0.288844366346 | $1.4\times10^{-15}$ |
| 2.00 | 0.453254704754 | 0.453254704754 | $2.6\times10^{-15}$ |
| 5.00 | 0.635256295997 | 0.635256295997 | $8.9\times10^{-16}$ |

The agreement to machine precision is not luck: on the Bromwich line,
$\sqrt s$ with the principal branch has positive real part, so
$|e^{-a\sqrt s}| = e^{-a\sqrt{|\omega|/2}}$ decays *exponentially in
$\sqrt\omega$*, faster than any power, and the truncated integral converges
rapidly. Compare the $1/\omega$ decay of $1/(1+i\omega)$ in the previous lesson,
which needed a tail correction to reach $10^{-10}$.

### 5.2 The same problem as a partial differential equation

The transform pair above is the solution of the 1-D diffusion equation

$$\frac{\partial T}{\partial t} = \kappa\frac{\partial^{2}T}{\partial x^{2}},
\qquad T(0,t) = 1, \qquad T(x,0) = 0, \qquad x>0,$$

whose solution is $T(x,t) = \operatorname{erfc}\bigl(x/(2\sqrt{\kappa t})\bigr)$.
The demo solves that equation by an explicit finite difference on a grid with
$\Delta x = 0.05$ and $\Delta t = 10^{-3}$ (3999 steps to $t = 3.999$) and
compares:

| $x$ | FD solution | $\operatorname{erfc}(x/(2\sqrt t))$ | difference |
|---|---|---|---|
| 1.00 | 0.72366127 | 0.72364048 | $2.1\times10^{-5}$ |
| 2.00 | 0.47947666 | 0.47944519 | $3.2\times10^{-5}$ |
| 4.00 | 0.15726569 | 0.15724732 | $1.8\times10^{-5}$ |
| 6.00 | 0.03387232 | 0.03387256 | $2.4\times10^{-7}$ |
| 8.00 | 0.00466988 | 0.00467257 | $2.7\times10^{-6}$ |

The worst difference is $3.2\times10^{-5}$, four orders of magnitude larger than
the Bromwich residual of Section 5.1 — and it is the truncation error of the
finite-difference scheme, not an error in the transform pair. The pairing of the
two checks is what makes the result credible: the transform pair is confirmed by
a contour integral, and the physical problem is confirmed by solving it
independently.

## Assumptions and regime of validity

| assumption | statement | where it fails or must be checked |
|---|---|---|
| **One-sided transform** | $f(t) = 0$ for $t<0$; the lower limit is $0$ | signals defined for all time; use the two-sided transform |
| **Existence of the integral** | convergence for $\operatorname{Re}s>\sigma_{0}$ | functions growing faster than any exponential have no transform in this sense |
| **Region of convergence is part of the answer** | the formula alone does not determine the function | quoting $1/(s-a)$ without its region |
| **Initial conditions carried explicitly** | $\mathcal{L}\{f'\} = sF(s)-f(0)$ | dropping the $f(0)$ term, the commonest error |
| **Closure of the Bromwich contour to the left** | valid for $t>0$, with decay of $F$ on the arc | a growing $F$ at infinity; $t<0$ |
| **Isolated singularities for residue inversion** | poles give exponentials | branch points give error functions, Fresnel integrals, Bessel functions, or worse |
| **Hypotheses of the limit theorems** | final value needs $sF$ poles in $\operatorname{Re}s<0$ (plus at most a simple pole at $0$); initial value needs $sF\to$ finite as $s\to\infty$ | an undamped oscillator or a pole on the imaginary axis: the final value does not exist |

**Regime of validity.** The transform solution is exact for the linear,
time-invariant, constant-coefficient problem it was set up for, and it is *only*
as good as the model. Two limitations recur in geophysics:

- **The physical model, not the method, limits the answer.** A transform pair
  describes a particular constitutive law; if the medium is nonlinear or the
  parameters depend on state, the linear transform solution is a first
  approximation whose error is not visible in the algebra.
- **The inversion must be justified, not assumed.** Writing down a residue sum
  for a function with a branch point is not a small error: the answer is
  qualitatively different (an error function instead of an exponential), and the
  numerical inversion will show a kink rather than a smooth curve.

**Idealised inputs.** The step and the impulse are mathematical limits: a real
step has a finite rise time and a real impulse a finite width. Using them is
legitimate whenever the rise time is short compared with every time constant in
the problem, and it is illegitimate when it is not — a step switched in over
$0.1$ s tells you nothing about the millisecond transient of the same system.
The transform makes this visible: the spectrum of a finite-rise-time step rolls
off above $1/\tau_{\text{rise}}$, so any feature of $F(s)$ above that frequency
is an artefact of the idealisation rather than a prediction.

## 6. Python demonstration

[`code/laplace_transient_demo.py`](./code/laplace_transient_demo.py) prints all
the tables above in about four seconds:

```text
python3 code/laplace_transient_demo.py
```

It uses only `cmath` and `math`. Four notes on method:

**The forward transform is checked with an exact tail.** For $f = 1$ the integral
from $T$ to $\infty$ is $e^{-sT}/s$, known exactly, so the quadrature error is
isolated from the truncation error. Measured, for $s = 0.7+1.1i$:

| $T$ | error in $\mathcal{L}\{1\}$ |
|---|---|
| 1.0 | $3.81\times10^{-1}$ |
| 2.0 | $1.89\times10^{-1}$ |
| 5.0 | $2.32\times10^{-2}$ |
| 20.0 | $6.38\times10^{-7}$ |
| 60.0 | $1.58\times10^{-13}$ |

At $T = 60$ the truncation error is $e^{-0.7\times60} = 5.8\times10^{-19}$, so the
measured $1.6\times10^{-13}$ is the quadrature error alone. Without that
separation, a quadrature error would be mistaken for a property of the transform.

**The Bromwich integral is evaluated as written.** With $s = c+i\omega$ the
inversion becomes $(1/2\pi)\int Y(c+i\omega)e^{(c+i\omega)t}\mathrm{d}\omega$
over the real $\omega$ axis, and the demo Simpson-integrates it. The residual is
then explained rather than assumed, by measuring the arc separately
(Section 4.3).

**Amplitude measurements use projection, not peak-picking.** The RK4 columns come
from a least-squares fit of $a\cos\omega t + b\sin\omega t$ over many cycles, not
from `max(abs(x))`; the sampling-phase bias of peak-picking would otherwise
contaminate the comparison.

**Every inverse pair is checked against something that does not use the
transform.** The first-order and second-order solutions are checked against
Runge–Kutta; the diffusive solution is checked against `math.erfc` and against a
finite-difference solution of the PDE. A transform routine that is only checked
against itself is a transform routine that has never been tested.

## 7. Common mistakes

1. **Forgetting the initial condition.** $\mathcal{L}\{f'\} = sF(s)-f(0)$; drop
   the $-f(0)$ and the answer is wrong by a decaying transient. This is the
   single most common error with the method.
2. **Quoting $F(s)$ without its region of convergence.** $1/(s-a)$ represents
   two different time functions depending on the region.
3. **Assuming every inverse is a sum of exponentials.** A branch point gives
   $\operatorname{erfc}$, a Fresnel integral, or a Bessel function. Diffusion,
   viscoelastic creep and electromagnetic diffusion in a conducting half-space
   are all of this kind.
4. **Closing the contour on the wrong side.** The Bromwich closure works for
   $t>0$ only; the closure for $t<0$ is what proves $f(t)=0$ there.
5. **Treating a pole on the imaginary axis as a decay.** A pole at
   $s = \pm i\omega$ is an undamped oscillation, and a pole at $s=0$ is a
   permanent offset. Both are marginal, not stable.
6. **Losing the $1/s$ from integration.** An indefinite integral in the time
   domain is a division by $s$; the step response of a system is its impulse
   response integrated, so $Y_{\text{step}} = Y_{\text{impulse}}/s$.
7. **Believing a numerical inverse without checking the contour.** A numerical
   Bromwich integral with a badly chosen $c$, or a truncated range, can look
   plausible and be wrong in the third digit. Converge it in $c$ and in the
   range before quoting it.

## 8. Real-world applications

- **Viscoelastic relaxation.** The creep and relaxation functions of a
  Maxwell, Kelvin–Voigt or standard linear solid are Laplace transforms of
  elementary functions; a step load produces the transient that the pole
  positions describe
  ([02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)).
- **Heat flow in the subsurface.** The response of a layered ground to a
  surface temperature step is a diffusion transient; borehole temperature
  inversions, permafrost modelling and thermal conductivity probes all use it
  ([12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)).
- **Electromagnetic diffusion.** The transient electromagnetic method's step-off
  response is the Laplace-domain solution of a diffusive Maxwell system inverted
  to the time domain, with the same $\sqrt s$ structure
  ([10-gpr-near-surface](../../10-gpr-near-surface/README.md),
  [09-electrical-em-methods](../../09-electrical-em-methods/README.md)).
- **Instrument step response.** The step or impulse response of a seismometer,
  geophone or tiltmeter is quoted as a transfer function with poles and zeros;
  the Laplace transform is the natural language
  ([23-field-methods-instruments](../../23-field-methods-instruments/README.md)).
- **Circuit and filter transients.** Switching a network on produces a transient
  whose decay rates are the pole positions — the discrete counterpart is
  [05 The z-Transform](./05-z-transform.md).
- **Seismic source time functions.** A moment-release history is a transient
  whose transform multiplies the medium's response, so the recorded spectrum is
  the product of source, path and instrument transfer functions
  ([06-seismology](../../06-seismology/README.md)).

## 9. Further reading

- **Doetsch, G. (1974). *Introduction to the Theory and Application of the
  Laplace Transformation* (3rd ed.). Springer.** Level: graduate. Region of
  convergence, inversion theorems and asymptotic behaviour, done properly.
- **Abramowitz, M. & Stegun, I. A. (1964). *Handbook of Mathematical
  Functions*. NBS Applied Mathematics Series 55.** Chapter 29. Level:
  reference. The standard table of transform pairs, including the ones with
  branch points.
- **Carslaw, H. S. & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** §§2, 12. Level: graduate. The textbook
  of diffusion transients; every result is derived by the Laplace transform.
- **Churchill, R. V. (1972). *Operational Mathematics* (3rd ed.).
  McGraw-Hill.** Level: intermediate. The contour-integral route to inversion,
  with many worked examples.
- **Crank, J. (1975). *The Mathematics of Diffusion* (2nd ed.). Oxford
  University Press.** Chapter 2. Level: intermediate. The complementary error
  function solution and its finite-difference verification, done at length.
- **Nabighian, M. N. & Macnae, J. C. (1991). Time-domain electromagnetic
  prospecting. In *Electromagnetic Methods in Applied Geophysics*, Vol. 2, ed.
  M. N. Nabighian, SEG.** Level: advanced. The diffusive transient of a
  conducting half-space, and its measurement.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library before citing them.

## 10. Related lessons

- [03 Contour Integration, Residues and Real
  Integrals](./03-contour-integration.md) — the inversion machinery, including
  the arc argument that Section 4.3 measures.
- [06 Dispersion Relations and Causality in Wave
  Physics](./06-dispersion-relations.md) — where analyticity in the two half
  planes becomes a physical constraint rather than a computational convenience.
- [05 The z-Transform and Discrete Linear
  Systems](./05-z-transform.md) — the same pole reading, per sample instead of
  per second.
- [01-08-01 First-Order
  ODEs](../08-ordinary-differential-equations/01-first-order-odes.md) and
  [01-08-02 Second-Order Linear
  ODEs](../08-ordinary-differential-equations/02-second-order-linear.md) — the
  equations transformed here.
- [01-09-02 The Heat
  Equation](../09-partial-differential-equations/02-heat-equation.md) — the
  physical problem of Section 5.2, solved there by separation of variables.
- [20 Signal Processing](../../20-signal-processing/README.md) — where impulse
  and step responses are used to characterise field instruments.

## 11. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/04-laplace-transform-exercises.md`](./exercises/04-laplace-transform-exercises.md).
Solutions:
[`exercises/04-laplace-transform-solutions.md`](./exercises/04-laplace-transform-solutions.md).

## Self-assessment checklist

- [ ] I can define the one-sided Laplace transform and state its region of
      convergence for an exponential.
- [ ] I can derive the transform of a derivative and say where the initial
      condition enters.
- [ ] I can solve a first-order and a second-order transient problem by
      transforming, solving algebraically, and inverting by partial fractions.
- [ ] I can explain the Bromwich contour, invert by residues, and say what the
      closing arc contributes.
- [ ] I can read decay rate and oscillation frequency off the poles, and state
      the stability criterion.
- [ ] I can recognise a branch point and explain why a diffusive transient has
      no single time constant.
- [ ] I can invert $e^{-a\sqrt s}/s$ to a complementary error function and verify
      it against a finite-difference solution of the diffusion equation.
- [ ] I can check a transform solution against a direct numerical integration of
      the differential equation.
