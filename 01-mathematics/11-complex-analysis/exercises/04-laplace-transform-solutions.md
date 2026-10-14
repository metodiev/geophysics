# Solutions — 01-11-04 The Laplace Transform and Transient Problems

> **Read this after attempting the exercises, not before.**
>
> Numerical values quoted as "measured" come from the companion script in
> [`../code/`](../code/laplace_transient_demo.py).

---

## ★1 — Transforms from the definition

**(a)** $\mathcal{L}\{t^{2}\} = \int_{0}^{\infty}t^{2}e^{-st}\mathrm{d}t$.
Integrating by parts twice, or using
$\int_{0}^{\infty}t^{n}e^{-st}\mathrm{d}t = n!/s^{n+1}$ for
$\operatorname{Re}s>0$:

$$F(s) = \frac{2}{s^{3}}, \qquad \operatorname{Re}s > 0 .$$

**(b)** Use the shift property $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$ with
$f = \cos 2t$, $F = s/(s^{2}+4)$, $a = -3$:

$$\mathcal{L}\{e^{-3t}\cos 2t\} = \frac{s+3}{(s+3)^{2}+4}
= \frac{s+3}{s^{2}+6s+13}, \qquad \operatorname{Re}s > -3 .$$

The region shifts with the exponent: the integrand contains
$e^{-(s+3)t}$.

**(c)** $\mathcal{L}\{u(t-2)\} = \int_{2}^{\infty}e^{-st}\mathrm{d}t =
e^{-2s}/s$ for $\operatorname{Re}s>0$ — the delay property applied to the unit
step $u(t)$, with $\mathcal{L}\{u\} = 1/s$. Note the exponent carries the delay
and the region is unchanged (a delay does not affect convergence).

---

## ★2 — First-order with a forcing term

Transform, using $\mathcal{L}\{\dot y\} = sY - y(0)$:

$$(s+3)Y - 2 = \frac{1}{s+1}
\qquad\Longrightarrow\qquad
Y = \frac{2}{s+3} + \frac{1}{(s+1)(s+3)} .$$

Partial fractions:
$\frac{1}{(s+1)(s+3)} = \frac{1}{2}\left(\frac{1}{s+1}-\frac{1}{s+3}\right)$, so

$$Y = \frac{1/2}{s+1} + \left(2 - \frac{1}{2}\right)\frac{1}{s+3}
= \frac{1/2}{s+1} + \frac{3/2}{s+3},$$

$$y(t) = \frac12 e^{-t} + \frac32 e^{-3t} .$$

**Checks.** $y(0) = 1/2+3/2 = 2$ ✓.
$\dot y = -\frac12e^{-t} - \frac92e^{-3t}$, so
$\dot y + 3y = -\frac12e^{-t}-\frac92e^{-3t}+\frac32e^{-t}+\frac92e^{-3t}
= e^{-t}$ ✓. As $t\to\infty$, $y\to0$: both poles are in the left half plane, and
the forcing $e^{-t}$ itself decays.

**Reading the poles.** Had the forcing been a constant instead, there would have
been a pole at $s=0$ and the response would have settled to a constant. The
position of the poles of $Y$ — not of the input — determines the behaviour.

---

## ★3 — Free oscillation

Transform: $(s^{2}+4)Y = s\cdot1 + 0$, so

$$Y = \frac{s}{s^{2}+4}, \qquad y(t) = \cos 2t .$$

The **second** initial condition matters: with $\dot y(0) = v_{0}$ instead of
zero, $Y = (s+v_{0})/(s^{2}+4)$ and

$$y(t) = \cos 2t + \frac{v_{0}}{2}\sin 2t,$$

so the amplitude becomes $\sqrt{1 + v_{0}^{2}/4}$ and the phase changes. The
first initial condition, $y(0)$, also matters, of course, but it entered as the
$s\,y(0)$ term and here produced the cosine; it is the *velocity* that generates
the sine. The general rule: $\mathcal{L}\{\ddot y\}$ carries both $y(0)$ and
$\dot y(0)$ explicitly, so both enter the algebra and neither has to be fitted
afterwards.

---

## ★4 — Initial and final value theorems

$$F(s) = \frac{3s+5}{s(s^{2}+4s+5)} .$$

**Initial value.** $sF(s) = (3s+5)/(s^{2}+4s+5) \to 3$ as $s\to\infty$, so
$f(0^{+}) = 3$. Hypothesis: $F(s)\to0$ as $s\to\infty$ with the polynomial parts
having the right degrees — satisfied here.

**Final value.** $sF(s)$ has poles at the roots of $s^{2}+4s+5$, namely
$s = -2\pm i$, both with $\operatorname{Re}s = -2 < 0$, and no pole at $s=0$
(the factor $s$ cancelled). The hypothesis holds, so

$$f(\infty) = \lim_{s\to0}sF(s) = \frac{5}{5} = 1 .$$

**What the numbers mean.** The transient starts at $3$ (a discontinuous rise,
since the numerator and denominator have equal degree so $F$ does not vanish at
infinity — there is an impulse at $t=0$) and decays to $1$ with time constant
$1/2$ and oscillation frequency $1$ rad s⁻¹, from the poles at $-2\pm i$.

**One caution.** If the denominator had contained a factor $s$ that did not
cancel, $sF$ would have had a simple pole at the origin and the final value would
be a non-zero constant from the *pole at zero* rather than from a decaying
transient; if a pole had lain in the right half plane the limit would be infinite
and the theorem's answer would be meaningless. Always check the pole positions
before quoting $f(\infty)$.

---

## ★★5 — A second-order step response

**(a)** With zero initial conditions,
$Y(s^{2}+3s+2) = 1/s$, so

$$Y = \frac{1}{s(s+1)(s+2)}
= \frac{1/2}{s} - \frac{1}{s+1} + \frac{1/2}{s+2},$$

the coefficients from the usual cover-up rule:
$A = 1/[(1)(2)] = 1/2$, $B = 1/[(-1)(1)] = -1$,
$C = 1/[(-2)(-1)] = 1/2$.

**(b)** Residues of $Y(s)e^{st}$:

| pole | residue |
|---|---|
| $s=0$ | $e^{0}/[(1)(2)] = 1/2$ |
| $s=-1$ | $e^{-t}/[(-1)(1)] = -e^{-t}$ |
| $s=-2$ | $e^{-2t}/[(-2)(-1)] = \frac12 e^{-2t}$ |

so

$$y(t) = \frac12 - e^{-t} + \frac12 e^{-2t} .$$

**(c)** Final value $\frac12$, supplied by the pole at $s=0$ — it is the residue
there, i.e. the coefficient of the constant term. The slowest time constant is
$1$ s, from the pole at $s=-1$; the pole at $s=-2$ contributes a transient that
decays twice as fast and is invisible after a few seconds. Checks:
$y(0) = 0.5-1+0.5 = 0$ ✓, and $\dot y = e^{-t}-e^{-2t}\ge0$ for $t\ge0$, so the
response is monotone — as it must be for an overdamped system ($\zeta>1$ here,
since $3^{2} > 4\cdot2$).

---

## ★★6 — A seismometer step response

**(a)** $X(s) = \dfrac{\omega_{0}^{2}}{s(s^{2}+2\zeta\omega_{0}s+\omega_{0}^{2})}$.
With $\omega_{0} = 20$, $\zeta = 0.5$: $2\zeta\omega_{0} = 20$,
$\omega_{0}^{2} = 400$, so the quadratic is $s^{2}+20s+400$ with roots

$$s = -10 \pm \sqrt{100-400} = -10 \pm 17.320508i .$$

**(b)** For $\zeta<1$ the inverse is

$$x(t) = 1 - e^{-\zeta\omega_{0}t}\left(\cos\omega_{d}t +
\frac{\zeta\omega_{0}}{\omega_{d}}\sin\omega_{d}t\right),
\qquad \omega_{d} = \omega_{0}\sqrt{1-\zeta^{2}} = 17.320508 .$$

The response rises to $1$ while ringing at $17.32$ rad s⁻¹
($2.76$ Hz), with an envelope decaying as $e^{-10t}$. It overshoots — a decaying
cosine cannot approach a constant monotonically — and the first peak occurs near
$t = \pi/\omega_{d} = 0.181$ s.

**(c)** The envelope decays with time constant $1/(\zeta\omega_{0}) = 1/10 = 0.1$
s. Setting the envelope equal to $0.1$:
$e^{-10t} = 0.1$ gives $t = \ln 10/10 = 0.230$ s. Numerically solving the exact
expression gives $t_{90} = 0.1063$ s — **much earlier**. The envelope estimate is
an over-estimate for a simple reason: the ringing term is a cosine, and $90\%$ of
the final value is first reached while the cosine is *positive and large*, long
before the envelope has decayed to $10\%$. Envelope arguments give the order of
magnitude and the late-time behaviour; they are not a substitute for evaluating
the transient when a crossing time is wanted.

---

## ★★7 — Inverting $(s+5)/(s^{2}+4s+13)$

Complete the square: $s^{2}+4s+13 = (s+2)^{2}+9$. Then

$$F(s) = \frac{(s+2)+3}{(s+2)^{2}+9}
= \frac{s+2}{(s+2)^{2}+3^{2}} + \frac{3}{(s+2)^{2}+3^{2}},$$

so, using $\mathcal{L}\{e^{-2t}\cos 3t\}$ and $\mathcal{L}\{e^{-2t}\sin 3t\}$,

$$f(t) = e^{-2t}\left(\cos 3t + \sin 3t\right) .$$

**At $t=0$:** $f(0) = 1$, and the initial-value theorem gives
$\lim_{s\to\infty}sF(s) = 1$ ✓ (degrees equal, so the limit is the ratio of
leading coefficients).
**As $t\to\infty$:** both poles are at $-2\pm3i$ with $\operatorname{Re}<0$, so
$f\to0$, and $\lim_{s\to0}sF(s) = 0$ ✓.
**Intermediate check:** $f(0.5) = e^{-1}(\cos 1.5 + \sin 1.5) = 0.392981$ to
seven figures, computed earlier and reproducible by the same formula.

---

## ★★8 — The diffusive response

**(a)** $F(s) = e^{-a\sqrt s}/s$ has a **branch point** at $s = 0$: $\sqrt s$ is
not single-valued in any punctured disc about the origin, so there is no Laurent
series with a finite negative part and no isolated singularity. The function is
analytic on the cut plane $\mathbb{C}\setminus(-\infty,0]$, and $\sqrt s$ is
continuous on the closed right half plane with the principal branch.

**(b)** The residue theorem applies to isolated singularities; a branch point is
not one. Any contour encircling the origin must either cross the cut or be
deformed into a "keyhole" whose contributions along the two sides of the cut do
not cancel — and those contributions *are* part of the answer. Inverting the
transform therefore requires the keyhole contour, and the resulting integral is
not a sum of residues.

**(c)** The classical result is

$$f(t) = \operatorname{erfc}\!\left(\frac{a}{2\sqrt t}\right) .$$

Limits: as $t\to0^{+}$, $a/(2\sqrt t)\to\infty$ and
$\operatorname{erfc}\to0$ — the effect has not had time to arrive. As
$t\to\infty$, the argument tends to $0$ and
$\operatorname{erfc}\to1$ — the full step. Both limits are the ones the physical
problem is supposed to have, and they are what makes this pair worth remembering.
The demo's numerical Bromwich integral reproduces the values to machine precision
($3.7\times10^{-16}$ at $t=0.2$, $8.9\times10^{-16}$ at $t=5$), because
$|e^{-a\sqrt s}| = e^{-a\sqrt{|\omega|/2}}$ decays exponentially in $\sqrt\omega$
along the Bromwich line.

**(d)** The "kink" is the signature of integrating the wrong branch. On a contour
that crosses the cut, $e^{-a\sqrt s}$ jumps by
$e^{-a\sqrt{s}} \to e^{+a\sqrt{s}}$ (the sign of the square root flips), so the
integrand is discontinuous and the numerical result inherits a visible break at
the crossing. The cure is to deform the contour around the cut (keyhole) and to
enforce a consistent branch, or to work on the cut plane and note explicitly which
side of the branch cut the contour lies on. **A branch of a square root and the
contour it is evaluated on must be chosen together**; choosing them independently
is the source of most errors with fractional powers.

---

## ★★★9 — Numerical Bromwich inversion, and the arc

**(a)** $Y(s) = 1/[s(s+2)]$, so $Y(s)e^{st}$ has poles at $s = 0$ and $s = -2$.
The Bromwich line must lie to the right of all of them: $c > 0$. The demo uses
$c = 3$.

**(b)** On the vertical line $s = c+i\omega$ the integrand decays like
$1/|\omega|^{2}$ multiplied by $e^{i\omega t}$, and truncating at $|\omega| =
\Omega$ leaves an oscillatory remainder of order $1/\Omega$;
the exact integral of $1/\omega^{2}$-type tails is not zero, so the truncation
error appears at first order. The residue sum, by contrast, is an identity at
*every* $\Omega$: the difference between the line integral and the residue sum is
exactly the arc contribution, and the two errors cancel.

**(c)** The values $1.6\times10^{-4}$ ($\Omega = 200$, $t=1$) and
$1.4\times10^{-4}$ ($t=3$) are consistent with $1/\Omega$ convergence:
$1/(2\pi\cdot200) \approx 8\times10^{-4}$, and the oscillatory coefficient is of
order one, so $10^{-4}$ is the expected size. The next check is to **double
$\Omega$** and see the residual halve; a residual that does not fall with $\Omega$
points to the quadrature (too few nodes per oscillation) rather than to
truncation. The demo performs exactly this: at $R = 10, 20, 40, 80, 160$ the line
integral moves from $0.4840$ to $0.4323$ while the arc contribution, added to the
line, reproduces the residue sum $0.432332358382$ at every radius to
$\sim10^{-6}$.

**(d)** Two checks that do not use the transform:

1. **Direct numerical integration of the differential equation.** For
   $Y = 1/[s(s+2)]$ the ODE is $\dot y + 2y = 1$, $y(0)=0$, and Runge–Kutta
   reproduces $y(1) = 0.432332358382$ to the digits shown.
2. **The two limits, computed independently.** The final value $1/2$ can be read
   off from the steady state of the ODE (or from an experiment), and the initial
   slope from the initial condition; both bound the transient without any
   transform.

A third, if the signal is measurable: conservation or energy accounting, which the
transform solution must satisfy and which an erroneous inversion typically
violates.

---

## ★★★10 — A surface temperature step

**(a)** With $\theta = T - T_{0}$:

$$\frac{\partial\theta}{\partial t} =
\kappa\frac{\partial^{2}\theta}{\partial x^{2}},
\qquad \theta(0,t) = \Delta T = T_{1}-T_{0}, \qquad \theta(x,0) = 0,
\qquad \theta\to0 \text{ as } x\to\infty .$$

Transforming in time (initial condition zero, so no extra term):

$$\kappa\frac{\partial^{2}\hat\theta}{\partial x^{2}} = s\,\hat\theta
\qquad\Longrightarrow\qquad
\hat\theta(x,s) = \frac{\Delta T}{s}e^{-x\sqrt{s/\kappa}},$$

the decaying exponential being the only bounded solution.

**(b)** With $a = x/\sqrt\kappa$ and using the pair of ★★8,

$$\theta(x,t) = \Delta T\operatorname{erfc}
\left(\frac{x}{2\sqrt{\kappa t}}\right),
\qquad\text{so}\qquad
T(x,t) = T_{0} + (T_{1}-T_{0})\operatorname{erfc}
\left(\frac{x}{2\sqrt{\kappa t}}\right) .$$

**(c)** Half the surface step means $\operatorname{erfc}(z) = 1/2$, whose
solution is $z = 0.4769362762$. Then

$$x = 2z\sqrt{\kappa t} = 2(0.4769362762)\sqrt{10^{-6}\times2\,592\,000}
= 0.9538725524\times1.6099689438 = 1.535705\ \mathrm{m} .$$

So at 30 days, the temperature swing at about $1.54$ m is half the surface swing.
Two orders of magnitude of depth separation in a month is the everyday reason
shallow boreholes are used for climate work.

**(d)** The probe adds a first-order lag: its transfer function is
$1/(1+\tau_{p}s)$. The combined response is the product,

$$H_{\text{tot}}(s) = \frac{1}{1+\tau_{p}s}\cdot
\frac{e^{-x\sqrt{s/\kappa}}}{s},$$

in the sense that the *measured* deviation is
$\Delta T\cdot\mathcal{L}^{-1}[e^{-x\sqrt{s/\kappa}}/(s(1+\tau_{p}s))]$. The
product structure is the statement that two cascaded linear systems convolve their
impulse responses, which is the convolution property of Section 3 of the lesson.
The surface step is not instantaneous as seen by the probe because the probe's own
time constant ($\tau_{p} = 1$ h) is finite: for times much shorter than 1 h the
probe reports a smoothed version of the step, and for $t\gg\tau_{p}$ it tracks
it. Whether the lag matters is decided by comparing $\tau_{p}$ with the time
resolution you claim, not by comparing it with the depth scale.

**(e)** From $x = 2z\sqrt{\kappa t}$ at fixed $z$ (the half-amplitude condition),
$t \propto x^{2}$. At twice the depth the half-amplitude time is therefore
**four times** later: if the first probe reaches half-amplitude at $t_{1}$, the
second reaches it at $4t_{1}$, a lag of $3t_{1}$ — for $t_{1} = 30$ days, a lag
of 90 days.

The scaling law is the **square-root-of-time law of diffusion**,
$x\propto\sqrt{\kappa t}$, and the specific consequence used here is
$t\propto x^{2}$. It is the reason a temperature record from 1 m and one from 2 m
are related by a factor of four in time, and the reason a thermal-diffusivity
estimate from two depths requires an accurate amplitude *and* phase pair — a
single amplitude ratio alone cannot separate $\kappa$ from the surface history.

---

## Self-assessment: have you actually learned this?

You can, without notes:

- write $\mathcal{L}\{f'\}$ and $\mathcal{L}\{f''\}$ with their initial-condition
  terms and explain why they appear;
- transform, solve algebraically and invert a first- and a second-order
  initial-value problem;
- read the final value and the slowest time constant off the poles;
- state the hypothesis of the final-value theorem and a case where it fails;
- identify a branch point and say why the inverse is not a residue sum;
- explain why the truncated Bromwich integral converges slowly while the residue
  sum does not, and how to measure the difference.
