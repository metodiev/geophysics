# Solutions — 01-08-01 First-Order ODEs: Separation of Variables and Integrating Factors

> **Read this after attempting the exercises, not before.** Every numerical
> value below was computed, and every solution asserted here was substituted
> back into its equation.

---

## ★1 — Classification and solution

**(a)** $y' = x^{2}y$. **Separable**, and also linear (the two dependent
variables $y$ and $y'$ appear to the first power), and homogeneous in the ODE
sense (no term free of $y$). Separating,
$\int dy/y = \int x^{2}dx$, so $\ln|y| = x^{3}/3 + C$ and

$$y = A\,e^{x^{3}/3}, \qquad A = y(0).$$

The constant solution $y \equiv 0$ is the case $A = 0$ and is recovered.

**(b)** $y' + y/x = x^{2}$. **Linear** with $p(x) = 1/x$, $q(x) = x^{2}$.
Here $\int p\,dx = \ln x$, so $\mu = x$. Then

$$\frac{d}{dx}(xy) = x\cdot x^{2} = x^{3}
\;\Longrightarrow\; xy = \frac{x^{4}}{4} + C
\;\Longrightarrow\; y = \frac{x^{3}}{4} + \frac{C}{x}.$$

*Check by substitution:* $y' = 3x^{2}/4 - C/x^{2}$, and
$y' + y/x = 3x^{2}/4 - C/x^{2} + x^{2}/4 + C/x^{2} = x^{2}$. ✓

Note the method is valid only for $x>0$ (or $x<0$); the interval must be stated,
because the solution is singular at the origin.

**(c)** $y' = y^{2} - x^{2}$. **Neither** separable (it is not $g(x)h(y)$: the
$x$ and $y$ terms are added, not multiplied) nor linear (the $y^{2}$ term).
It is a Riccati equation and is not covered by this lesson's methods; a
particular solution is needed before it can be linearised.

**(d)** $y' = (x+y)/x = 1 + y/x$. **Neither** separable nor linear, but
homogeneous of degree zero in the sense $y' = f(y/x)$. Substituting $v = y/x$
gives $y = vx$, $y' = v + xv'$, so

$$v + xv' = 1 + v \;\Longrightarrow\; xv' = 1
\;\Longrightarrow\; v = \ln|x| + C
\;\Longrightarrow\; y = x\ln|x| + Cx.$$

*Check:* $y' = \ln|x| + 1 + C$, and $(x+y)/x = 1 + \ln|x| + C$. ✓

---

## ★2 — Decay constants, times and fractions

**(a)** $y = y_0e^{-kt}$ with $k = 0.2\ \mathrm{d^{-1}}$, so

$$\tau = \frac{1}{k} = 5.000\ \mathrm{d}, \qquad
t_{1/2} = \frac{\ln 2}{k} = \frac{0.693147}{0.2} = 3.466\ \mathrm{d}.$$

The ratio $t_{1/2}/\tau = \ln 2 = 0.6931$ is the check.

**(b)** At $t = 10$ d $= 2\tau$, the remaining fraction is

$$e^{-kt} = e^{-2} = 0.135335, \qquad\text{i.e. } 13.53\ \%.$$

**(c)** $|y-y_0|/y_0 = 1-e^{-kt} = 0.01$ gives $e^{-kt} = 0.99$, so

$$t = \frac{-\ln 0.99}{0.2} = \frac{0.0100503}{0.2} = 0.0503\ \mathrm{d}
\approx 72\ \mathrm{min}.$$

---

## ★3 — Newton cooling

**(a)** Standard form: $T' + kT = kT_a$, so $\mu = e^{kt}$ and

$$\frac{d}{dt}\left(e^{kt}T\right) = kT_ae^{kt}
\;\Longrightarrow\; T = T_a + Ce^{-kt}.$$

Imposing $T(0) = T_0$ gives $C = T_0-T_a$ and

$$T(t) = T_a + (T_0-T_a)e^{-kt}.$$

**(b)** Put $u = T-T_a = (T_0-T_a)e^{-kt}$. Then $u/u_0 = e^{-kt}$, and
$u/u_0 = f$ requires

$$t = \frac{-\ln f}{k} = \tau\ln\frac{1}{f}.$$

With $f = 0.2$ and $\tau = 5$ d: $t = 5\ln 5 = 5\times1.609438
= 8.047\ \mathrm{d}$. **The amplitude $T_0-T_a$ cancels, which is why the time
to reach a given *fraction* of the excess is independent of the initial
temperature.**

---

## ★4 — Radiocarbon dating and its uncertainty

**(a)** With $\lambda = \ln 2/5730 = 1.209681\times10^{-4}\ \mathrm{yr^{-1}}$
and $A/A_0 = 0.42$,

$$t = \frac{1}{\lambda}\ln\frac{A_0}{A}
= \frac{\ln(1/0.42)}{1.209681\times10^{-4}}
= \frac{0.8675006}{1.209681\times10^{-4}} = 7171\ \mathrm{yr}.$$

Equivalently $t = (5730/\ln 2)\ln(2.380952) = 8267.0\times0.8675006$ yr, which
gives the same value — the two forms are identical.

**(b)** From $t = \lambda^{-1}\ln(A_0/A)$, differentiating with respect to $A$,

$$\frac{dt}{dA} = -\frac{1}{\lambda A}
\;\Longrightarrow\;
|\delta t| = \frac{1}{\lambda}\left|\frac{\delta A}{A}\right|
= \frac{0.01}{1.209681\times10^{-4}} = 82.7\ \mathrm{yr}.$$

**The age uncertainty is independent of the age**, depending only on the
*relative* activity uncertainty. Note that this is a first-order propagation and
that it ignores the uncertainty in $\lambda$ and in $A_0$, both of which matter
in practice.

**(c)** With the Libby half-life $T_{1/2} = 5568$ yr,
$\lambda = 0.693147/5568 = 1.244875\times10^{-4}\ \mathrm{yr^{-1}}$ and

$$t = \frac{0.8675006}{1.244875\times10^{-4}} = 6969\ \mathrm{yr}.$$

The difference is 202 yr, i.e. **2.9 %** — comparable to, though larger than, the
82.7 yr from the measurement. **This is exactly why radiocarbon ages are
reported with a stated convention and then *calibrated*; the half-life choice is
part of the reporting convention, not a physics question.**

---

## ★5 — Aquifer relaxation

**(a)** With $T = 2\times10^{-3}\ \mathrm{m^{2}\,s^{-1}}$,
$S = 5\times10^{-4}$ and $L = 2000$ m,

$$\tau = \frac{4SL^{2}}{\pi^{2}T}
= \frac{4(5\times10^{-4})(4\times10^{6})}{\pi^{2}(2\times10^{-3})}
= \frac{8000}{0.0197392} = 4.053\times10^{5}\ \mathrm{s}
= 4.690\ \mathrm{d}.$$

**(b)** The head change approaches its final value as $1-e^{-t/\tau}$, so 95 %
requires $t = \tau\ln 20 = 4.690\times2.995732 = 14.05$ d.

**(c)** For $L = 1000$ m, $\tau \propto L^{2}$ gives
$\tau = 4.690/4 = 1.173$ d. **The direction of the change is the physical
content: a shorter drainage path means less stored water to move through the
same transmissivity, so the aquifer equilibrates faster.** Note the contrast
with a cooling body, where the *numerator* carries $L^{2}$ for the same reason
(more volume, more heat) but the geometry of the flux is different.

---

## ★6 — Lumped cooling and its validity

**(a)** For a sphere of radius $r$, $A = 4\pi r^{2}$ and $V = \tfrac43\pi r^{3}$,
so the lumped rate is

$$k = \frac{hA}{\rho cV} = \frac{h\cdot4\pi r^{2}}{\rho c\cdot\frac43\pi r^{3}}
= \frac{3h}{\rho c\,r}
= \frac{3(10)}{(2700)(900)(0.5)}
= \frac{30}{1\,215\,000} = 2.4691\times10^{-5}\ \mathrm{s^{-1}},$$

$$\tau = \frac{1}{k} = 4.050\times10^{4}\ \mathrm{s} = 11.25\ \mathrm{h}.$$

**(b)** The lumped criterion is
$\mathrm{Bi} = hL_c/k_{\text{cond}} \ll 1$ with the characteristic length
$L_c = V/A = r/3$:

$$\mathrm{Bi} = \frac{10\times0.16667}{2.5} = 0.667 .$$

The usual working criterion is $\mathrm{Bi}<0.1$. Here $\mathrm{Bi} = 0.67$,
**so the lumped model is not admissible**: the internal temperature gradient is
not negligible compared with the surface-to-ambient difference.

**(c)** The true behaviour is a conduction problem with a significant internal
gradient: the surface cools quickly, the centre lags, and after a short initial
transient the cooling is described by the *first* eigenmode of the
Sturm–Liouville problem (see
[05 Sturm–Liouville Theory](../05-sturm-liouville.md)), not by a single
exponential with the lumped $k$. The lumped value of $\tau$ is a lower bound on
the true centre-cooling time because it assumes the whole body is at the surface
temperature.

---

## ★7 — Production, decay and secular equilibrium

**(a)** $\dot N + \lambda N = c$ with integrating factor $e^{\lambda t}$:

$$\frac{d}{dt}\left(e^{\lambda t}N\right) = ce^{\lambda t}
\;\Longrightarrow\; N = \frac{c}{\lambda} + A e^{-\lambda t}.$$

With $N(0) = 0$, $A = -c/\lambda$, so

$$N(t) = \frac{c}{\lambda}\left(1-e^{-\lambda t}\right),
\qquad N_\infty = \frac{c}{\lambda}.$$

*Check:* $\dot N = ce^{-\lambda t}$ and $c - \lambda N = c - c(1-e^{-\lambda t})
= ce^{-\lambda t}$. ✓

**(b)** $N/N_\infty = 1-e^{-\lambda t} = 0.9$ gives
$t = \ln 10/\lambda = 2.302585\,\tau$. In half-lives,
$t/t_{1/2} = 2.302585/\ln 2 = 3.3219$. **The production rate cancels because the
approach to equilibrium is governed by the *ratio* $N/N_\infty$, and both are
proportional to $c$.**

**(c)** With $N(0) = 3c/\lambda$, $A = N(0)-c/\lambda = 2c/\lambda$, so

$$N(t) = \frac{c}{\lambda}\left(1 + 2e^{-\lambda t}\right).$$

The initial slope is $\dot N(0) = c - \lambda(3c/\lambda) = -2c < 0$: the sample
*decays* initially because the excess over equilibrium is lost faster than the
production replenishes it. As $t\to\infty$, $N\to c/\lambda$ from above. **The
initial slope sign, not the initial value, is what distinguishes "growing
towards equilibrium" from "decaying towards it".**

---

## ★8 — Measuring the order of a method

**(a)** For $\lambda = 1$ over $[0,1]$, the exact answer is $e^{-1} =
0.36787944117$.

| $h$ | Euler error | ratio | RK4 error | ratio |
|---|---|---|---|---|
| 0.200 | $4.0199\times10^{-2}$ | — | $5.7970\times10^{-6}$ | — |
| 0.100 | $1.9201\times10^{-2}$ | 2.094 | $3.3324\times10^{-7}$ | 17.396 |
| 0.050 | $9.3935\times10^{-3}$ | 2.044 | $1.9976\times10^{-8}$ | 16.682 |
| 0.025 | $4.6470\times10^{-3}$ | 2.021 | $1.2227\times10^{-9}$ | 16.337 |

The ratios approach 2 and 16 as $h$ shrinks, as the orders predict. Taking the
last ratio: observed Euler order $\log_2 2.021 = 1.015$, observed RK4 order
$\log_2 16.337 = 4.030$. **Both are measured, neither is assumed**, and both
approach the theoretical values from the correct side (a shrinking ratio
approaching 16 from above).

**(b)** With $\lambda = 50$ the same sequence behaves completely differently.
The exact answer is $\exp(-50) = 1.9287\times10^{-22}$.

| $h$ | $h\lambda$ | Euler $y(1)$ | RK4 $y(1)$ |
|---|---|---|---|
| 0.200 | 10.0 | $-5.9049\times10^{4}$ | $2.0867\times10^{12}$ |
| 0.100 | 5.0 | $1.0486\times10^{6}$ | $2.3434\times10^{11}$ |
| 0.050 | 2.5 | $3.3253\times10^{3}$ | $1.7273\times10^{-4}$ |
| 0.025 | 1.25 | $8.2718\times10^{-25}$ | $3.2451\times10^{-21}$ |

Three separate diagnoses:

- **Euler is unstable for $h\lambda \ge 2$.** At $h\lambda = 10$ the
  amplification is $1-h\lambda = -9$, so $|y|$ grows by 9 per step and the sign
  alternates: after 5 steps $y = (-9)^{5} = -59049$.
- **RK4 is unstable too at $h\lambda = 5$ and 10.** Its stability interval on
  the negative real axis is approximately $(-2.785,\,0)$, which is *wider* than
  Euler's but still finite. At $h\lambda = 2.5$ it is stable; the error is
  $1.727\times10^{-4}$, which is twelve orders larger than the true answer.
- **At $h\lambda = 1.25$ both are stable and both are badly wrong.** Euler gives
  $(-0.25)^{40} = 8.2718\times10^{-25}$, i.e. 0.43 % of the exact value — the
  step is stable but the decay it produces is far too fast. RK4 gives
  $3.2451\times10^{-21}$, 16.8 times the exact value.

No order can be measured from this sequence, and the honest conclusion is that
**the sequence never entered the asymptotic regime $h\lambda\ll1$.** To measure
order 4 at $\lambda = 50$ the step must satisfy $h\lambda\lesssim0.4$:

| $h$ | $h\lambda$ | RK4 error | ratio |
|---|---|---|---|
| 0.008 | 0.40 | $2.897\times10^{-24}$ | — |
| 0.004 | 0.20 | $1.520\times10^{-25}$ | 19.06 |
| 0.002 | 0.10 | $8.736\times10^{-27}$ | 17.40 |
| 0.001 | 0.05 | $5.237\times10^{-28}$ | 16.68 |

giving an observed order $\log_2 16.68 = 4.06$. **The method never changed its
order; the earlier steps were simply outside the range where the order statement
applies.** This is the practical rule: a convergence study that has not reached
$h\lambda\ll1$ measures the pre-asymptotic coefficient, not the order.

**(c)** Stability for explicit Euler requires $h\lambda<2$, i.e.
$h<2/50 = 0.04$ for $\lambda = 50$. Among the tabulated steps only
$h = 0.025$ ($h\lambda = 1.25$) qualifies, and that is exactly the single row
whose Euler value is bounded. **A bounded—even small—answer is not evidence of
accuracy**: at $h\lambda = 1.25$ Euler's result is 0.43 % of the true value,
and it happens to look reassuring only because the exact answer is also tiny.
