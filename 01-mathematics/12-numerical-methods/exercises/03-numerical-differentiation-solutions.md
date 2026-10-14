# Solutions — 01-12-03 Numerical Differentiation and Finite-Difference Stencils

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed rather than estimated. Where a result is quoted from the
> module's demonstration, the script and its output are named so you can reproduce
> it.

---

## ★1 — Forward and backward truncation terms

Expanding about $x_i$,

$$f_{i+1} = f_i + h f_i' + \frac{h^2}{2}f_i'' + \frac{h^3}{6}f_i''' + O(h^4),$$

so

$$D^+f_i = \frac{f_{i+1}-f_i}{h} = f_i' + \frac{h}{2}f_i'' + \frac{h^2}{6}f_i'''
+ O(h^3).$$

Similarly $f_{i-1} = f_i - hf_i' + \frac{h^2}{2}f_i'' - \frac{h^3}{6}f_i''' + O(h^4)$
gives

$$D^-f_i = f_i' - \frac{h}{2}f_i'' + \frac{h^2}{6}f_i''' + O(h^3).$$

The leading terms are $+\frac h2 f''$ and $-\frac h2 f''$: **opposite signs, equal
magnitude**. This is not a curiosity. Writing $h/2$ for $|h|$, it shows the
forward difference *over*-estimates a convex function's slope and the backward
difference under-estimates it by the same amount — which is exactly what
$\arctan$-type slope estimates do on a convex topography. Their average is the
centred difference, whose $O(h)$ term cancels:

$$\frac{D^+ + D^-}{2} = D^0 = f_i' + \frac{h^2}{6}f_i''' + O(h^3).$$

The sign structure also explains why the two one-sided errors are correlated and
why averaging two independent one-sided estimates is *not* equivalent to using
them separately.

---

## ★2 — Exactness of the centred second difference on cubics

$$D^0_2 f_i = \frac{f_{i+1}-2f_i+f_{i-1}}{h^2}.$$

Adding the two expansions above,

$$f_{i+1}+f_{i-1} = 2f_i + h^2f_i'' + \frac{h^4}{12}f_i'''' + O(h^6),$$

so

$$D^0_2 f_i = f_i'' + \frac{h^2}{12}f_i'''' + O(h^4) .$$

For a cubic, $f''''=0$, so the stencil is exact; for a quartic the error is
$\frac{h^2}{12}\cdot24 = 2h^2$, which is why the demonstration's monomial table
shows the second difference exact for $p\le3$ and failing at $p=4$. The leading
error term is $\frac{h^2}{12}f''''$.

**Consistency check with the lesson's error-model table.** The generic optimal
step for a stencil with leading truncation order $q$ is $h^\*\propto u^{1/(q+1)}$,
so for the second difference ($q=2$) it is $u^{1/3}$, the same as for the centred
first difference.

---

## ★3 — Optimal steps and the two exponents

**Forward difference.** With $E(h) = \frac{|f''|}{2}h + \frac{u|f|}{h}$,

$$\frac{dE}{dh} = \frac{|f''|}{2} - \frac{u|f|}{h^2} = 0
\ \Longrightarrow\ h^\* = \sqrt{\frac{2u|f|}{|f''|}}
= \sqrt{\frac{2(2.2\times10^{-16})(1)}{2}} = \boxed{1.483\times10^{-8}}.$$

The minimum error is

$$E(h^\*) = \frac{2}{2}(1.483\times10^{-8}) +
\frac{2.2\times10^{-16}}{1.483\times10^{-8}} = 2.97\times10^{-8},$$

i.e. about **7 correct digits** in the derivative.

**Centred difference.** With $E(h) = \frac{|f'''|}{6}h^2 + \frac{u|f|}{h}$,

$$\frac{dE}{dh} = \frac{|f'''|}{3}h - \frac{u|f|}{h^2} = 0
\ \Longrightarrow\
h^\* = \left(\frac{3u|f|}{|f'''|}\right)^{1/3}
= \left(\frac{3(2.2\times10^{-16})}{6}\right)^{1/3}
= \boxed{4.791\times10^{-6}}.$$

The minimum error is

$$E(h^\*) = 1.0\,(4.791\times10^{-6})^2 +
\frac{2.2\times10^{-16}}{4.791\times10^{-6}} = 6.89\times10^{-11},$$

about **10 correct digits**.

**Reading the result.** The centred stencil tolerates a step 323 times larger and
delivers 430 times smaller error at the optimum. Both facts follow from the
single difference between the two error models: the exponent of $h$ in the
truncation term. This is why "use the smallest step you can" is wrong advice, and
why the two exponents $u^{1/2}$ and $u^{1/3}$ must not be interchanged.

---

## ★4 — Sampling, noise and the usable spacing

The two error sources that grow as $h$ shrinks are round-off
$\approx u\lvert f\rvert/h$ and noise $\approx\sigma/(h\sqrt2)$. For a gravity
reading, $f$ is of order $10^{4}$ mGal (the absolute field) but the *anomaly*
being differentiated is of order 1 mGal, so the relevant $\lvert f\rvert$ is the
anomaly magnitude, and the noise term dominates by a factor
$\sigma/(u\lvert f\rvert) = 0.01/(2.2\times10^{-16}\times1) \approx 4.5\times10^{13}$.

Setting the noise term against the truncation term
$\frac{\lvert f'''\rvert}{6}h^2$:

$$\frac{\sigma}{h\sqrt2} = \frac{\lvert f'''\rvert}{6}h^2
\ \Longrightarrow\
h^\* = \left(\frac{6\sigma}{\sqrt2\,\lvert f'''\rvert}\right)^{1/3}.$$

For a compact body the third derivative of the gradient is set by the depth $z_0$
and the anomaly amplitude approximately as $\lvert f'''\rvert\sim A/z_0^4$ with $A$
in mGal per metre. For $A \approx 5$ mGal and $z_0 = 500$ m this is
$\lvert f'''\rvert \approx 8\times10^{-11}$ mGal/m³, giving

$$h^\* \approx \left(\frac{6(0.01)}{1.414(8\times10^{-11})}\right)^{1/3}
= 8.1\times10^{7}\ \text{... m}^3 \Rightarrow h^\*\approx 4.3\times10^{2}\ \text{m}.$$

So the optimum is of order **a few hundred metres**, not the 20 m sampling
interval: below about 400 m the estimate gets *worse*, and the error source is the
reading noise, not the arithmetic. The module's demonstration measures this
directly with a synthetic body: with $\sigma = 0.01$ mGal the RMS error of the
centred difference is minimised near $h = 25$–$50$ m at a level matching
$\sigma/(h\sqrt2)$, and the same experiment with $\sigma$ reduced by a factor of
ten moves the minimum to smaller $h$ and reduces the error proportionally.

**Which source sets the spacing: the data.** Round-off at $u=2.2\times10^{-16}$ is
thirteen orders of magnitude smaller than a 0.01 mGal reading error, so no choice
of precision helps; only smoothing, averaging or model fitting does.

---

## ★★5 — The five-point centred stencil

**Moment conditions.** For a symmetric stencil with weights $w_{\pm1},w_{\pm2}$
at offsets $\pm h, \pm2h$,

$$\sum_j w_j = 0 \ (\text{degree } 0), \qquad
\sum_j w_j x_j = 1 \ (\text{first moment}), \qquad
\sum_j w_j x_j^p = 0 \ \text{for } p = 2,3,4 .$$

By antisymmetry $w_{-k} = -w_k$, so the even conditions are automatic and the
odd ones give

$$2h w_1 + 4h w_2 = 1, \qquad 2h^3w_1 + 16h^3w_2 = 0
\ \Longrightarrow\ w_1 = \frac{2}{3h},\ w_2 = -\frac{1}{12h}.$$

Hence

$$f_i' \approx \frac{-f_{i+2} + 8f_{i+1} - 8f_{i-1} + f_{i-2}}{12h}
+ O(h^4),$$

with leading error term $-\frac{h^4}{30}f^{(5)}(\xi)$.

**Verification on $\sin x$ at $x=1$** (exact derivative $\cos 1 =
0.540302305868$):

| $h$ | measured error | ratio |
|---|---|---|
| 0.2 | $2.868\times10^{-5}$ | – |
| 0.1 | $1.799\times10^{-6}$ | 15.9 |
| 0.05 | $1.125\times10^{-7}$ | 16.0 |
| 0.025 | $7.035\times10^{-9}$ | 16.0 |

The ratio 16 per halving of $h$ is order 4, as predicted. Note the cost: five
evaluations instead of two for a gain of two orders of magnitude per step, which
is worth it only when the function is cheap or when the grid is fixed.

---

## ★★6 — A one-sided third-order stencil

Seek
$f'_0 \approx \frac{1}{h}(a_0f_0+a_1f_1+a_2f_2+a_3f_3)$ exact for polynomials of
degree $\le3$, with $x_k = kh$. Substituting $f = x^p$ for $p=0,1,2,3$ and
dividing by $h$:

$$\text{degree }0:\ \sum_k a_k = 0, \qquad
\text{degree }1:\ \sum_k k\,a_k = 1,$$

$$\text{degree }2:\ \sum_k k^2a_k = 0 \quad\Longleftrightarrow\quad
a_1+4a_2+9a_3 = 0,$$

$$\text{degree }3:\ \sum_k k^3a_k = 0 \quad\Longleftrightarrow\quad
a_1+8a_2+27a_3 = 0 .$$

Subtracting the last two gives $4a_2+18a_3=0$, so $a_2 = -\tfrac92a_3$, and then
$a_1 = -4a_2-9a_3 = 9a_3$. The degree-1 equation then fixes the scale:
$a_1+2a_2+3a_3 = 9a_3-9a_3+3a_3 = 3a_3 = 1$, so $a_3 = \tfrac13$, and

$$a_0 = -\tfrac{11}{6},\qquad a_1 = 3,\qquad a_2 = -\tfrac32,\qquad
a_3 = \tfrac13 .$$

Hence

$$f'_0 \approx \frac{-11f_0 + 18f_1 - 9f_2 + 2f_3}{6h}
+ \frac{h^3}{4}f^{(4)}(\xi) .$$

Four weights, four conditions: the system is square and nonsingular, and the
degree-4 moment is what does *not* vanish — which is precisely why the stencil is
order 3 and not 4. (A general $m$-point stencil for a first derivative can be made
exact to degree $m-1$; one more condition would require a fifth point.)

**Why the boundary matters.** This stencil has the same order as the five-point
interior stencil of ★5, so a grid with this boundary treatment keeps its global
order. Replacing it by the two-point one-sided stencil
$-3f_0+4f_1-f_2$ (order 2) would silently reduce the whole solution to second
order — the same mechanism that made the natural cubic spline second-order in
[01-12-02](../02-interpolation.md): the boundary treatment, not the interior
stencil, sets the global order.

## ★★7 — Repeated Richardson extrapolation

**One application.** $D^+(h) = f' + c_1h + c_2h^2 + O(h^3)$. Then

$$2D^+(h/2) - D^+(h) = 2\left(f' + \frac{c_1h}{2} + \frac{c_2h^2}{4} + \cdots\right)
- \left(f' + c_1h + c_2h^2 + \cdots\right)
= f' - \frac{c_2}{2}h^2 + O(h^3),$$

so the combination is order 2 for any smooth $f$ — the $c_1h$ terms cancel
identically. **Measured** on $\sin x$ at $x=1$:

| $h$ | $D^+$ error | Richardson error | ratio |
|---|---|---|---|
| 0.1 | $4.294\times10^{-2}$ | $4.236\times10^{-4}$ | – |
| 0.05 | $2.126\times10^{-2}$ | $1.093\times10^{-4}$ | 3.88 |
| 0.025 | $1.057\times10^{-2}$ | $2.773\times10^{-5}$ | 3.94 |
| 0.0125 | $5.273\times10^{-3}$ | $6.984\times10^{-6}$ | 3.97 |

Ratios approaching 4 per halving confirm order 2.

**Second application.** The same idea applied to the $h^2$ term (combining the
order-2 result at $h$ and $h/2$ with weights $4$ and $-1$, divided by 3) cancels
$c_2h^2$ and leaves order 3. **The first argument does not transfer to $D^0$** for
a specific and instructive reason: $D^0$'s error series contains only *even*
powers, $f' + b_1h^2 + b_2h^4+\cdots$, because the stencil is symmetric. Applying
the forward-difference weights $2$ and $-1$ to $D^0$ would leave a residual
$b_1h^2(2/4-1) = -b_1h^2/2 \ne 0$: it *changes* the constant without removing the
term. The correct weights for an even-power series are $4$ and $-1$ over $3$,
which removes $h^2$ and gives order 4 directly, skipping the order-3 stage
entirely. **General rule:** the extrapolation weights depend on which powers are
present in the error series, which depends on the symmetry of the stencil.

---

## ★★8 — GNSS strain-rate noise

**Single day.** The strain rate is $\dot\epsilon = \Delta\dot d/L$ with
$\Delta d$ the change in baseline. The difference of two independent positions each
with standard deviation $\sigma = 1.5$ mm has standard deviation
$\sqrt2\,\sigma = 2.12\times10^{-3}$ m, so the daily strain-rate noise is

$$\sigma_{\dot\epsilon} = \frac{\sqrt2\,\sigma}{L\,\Delta t}
= \frac{2.12\times10^{-3}}{1.2\times10^{4}\times8.64\times10^{4}}
= 2.05\times10^{-12}\ \mathrm{s^{-1}} .$$

Converting, $1\ \mu\epsilon = 10^{-6}$ and one year is $3.156\times10^{7}$ s:

$$\sigma_{\dot\epsilon} = 2.05\times10^{-12}\times3.156\times10^{7}
= \boxed{64.6\ \mu\epsilon\ \mathrm{yr^{-1}}}.$$

**One year of daily data.** If the daily errors are independent, the mean of 365
daily estimates has noise reduced by $\sqrt{365} = 19.1$:

$$\sigma_{\dot\epsilon}^{(1\,\text{yr})} = \frac{64.6}{19.1}
= \boxed{3.4\ \mu\epsilon\ \mathrm{yr^{-1}}}.$$

**Assumptions and conclusion.** The assumption is that daily position errors are
independent — if they are correlated (a common-mode orbit or reference-frame
error), the $\sqrt N$ reduction does not happen and the noise floor is set by the
correlated component, which is why daily solutions are routinely differenced
between nearby stations. Even granting independence, a $3.4\ \mu\epsilon$ yr$^{-1}$
floor is above typical interseismic rates ($0.01$–$0.1\ \mu\epsilon$ yr$^{-1}$ in
many settings), so this baseline is unusable for a one-year rate; the remedies are
a longer baseline (a factor of 10 in $L$ buys a factor of 10), a longer time
series, or a network solution that constrains the common mode. **The measurement
that matters is the noise floor, not the baseline length.**

---

## ★★★9 — Distinguishing round-off from data noise

**Design.** Use the same function and grid, and vary one thing at a time.

1. *Round-off hypothesis.* The error is $\sim u\lvert f\rvert/h$ with
  $u = 2.2\times10^{-16}$. Diagnostic: simulate reduced precision by rounding every
  function value to a multiple of a prescribed $u$, as the module's
  `numerical_differentiation.py` does. The error at small $h$ then scales
  *linearly* in $u$ and is deterministic for a given function and grid. Prediction:
  the optimal step scales as $u^{1/3}$ for a centred stencil, and a fitted
  log–log slope of $\log h^\*$ against $\log u$ is $+1/3$.
2. *Noise hypothesis.* The error is $\sim\sigma/(h\sqrt2)$, i.e. linear in $\sigma$,
  and it is *not* deterministic: it changes with the realisation. Diagnostic:
  repeat with many noise realisations and average the squared error. Prediction:
  the RMS error is proportional to $\sigma$ and independent of $u$.

**Result of the experiment** (the module's demonstration, run as described):

- Round-off: fitted log–log slopes $+0.4775$ (forward stencil) and $+0.3329$
  (centred stencil) against the theoretical $+0.5$ and $+1/3$. At $u =
  1.0\times10^{-12}$ the optimal step is $3.7\times10^{-7}$ m for the centred
  stencil; at $u = 1.0\times10^{-10}$ it is $4.2\times10^{-4}$ m.
- Noise: with $\sigma = 0.01$ mGal on a synthetic gravity profile, the RMS error
  over 40 realisations at $h = 5$ m is $1.150\times10^{-3}$ mGal/m against a
  predicted $\sigma/(h\sqrt2) = 1.414\times10^{-3}$; at $h = 100$ m it is
  $1.310\times10^{-3}$ against a prediction of $7.07\times10^{-5}$, where
  truncation ($2.5\times10^{-4}$) has taken over. The minimum sits near
  $h = 25$–$50$ m.

**Conclusion.** The two are distinguishable by (i) the *scaling with precision* —
round-off responds, noise does not — and (ii) *reproducibility* — round-off is
deterministic, noise is not. A single error-versus-$h$ curve cannot tell them
apart, which is why the design above varies two different variables rather than
one.

---

## ★★★10 — Is a finer grid an improvement?

**The arithmetic.** The two error contributions for a centred stencil on a
250 m grid with $\sigma = 0.02$ mGal are

$$E_{\text{noise}} \approx \frac{\sigma}{h\sqrt2}
= \frac{0.02}{250\sqrt2} = 5.7\times10^{-5}\ \text{mGal/m},$$

$$E_{\text{trunc}} \approx \frac{\lvert f'''\rvert}{6}h^2 .$$

For a body at depth $z_0$ with a gradient anomaly of amplitude $A$ mGal/m, the
third derivative of the *anomaly* is of order $A/z_0^2$ per metre:
$\lvert f'''\rvert \sim A/z_0^{3}$ with $A$ in mGal/m and $z_0$ in metres. Taking
$A = 0.05$ mGal/m and $z_0 = 1000$ m, $\lvert f'''\rvert \sim 5\times10^{-11}$
mGal/m³, so at $h=250$ m the truncation error is $5\times10^{-7}$ mGal/m — **two
orders of magnitude smaller than the noise term**. The map is therefore
noise-limited, not resolution-limited.

**Answer.** A finer grid would make the gradient map *worse*, not better: halving
the grid spacing doubles the noise term ($5.7\times10^{-5}\to1.14\times10^{-4}$
mGal/m) while the truncation term falls by a factor of four from a level that was
already negligible. Beyond a certain density, additional stations add noise
amplification and no information. The correct improvements are to reduce $\sigma$
(longer occupations, repeat measurements, better levelling and drift control) or
to *smooth* the profile before differentiating — which is a deliberate trade of
resolution for noise suppression and is the standard practice in gradiometry.

**The measurement to request.** The single most useful additional quantity is
**a repeat observation of a subset of stations**, giving an empirical estimate of
$\sigma$ rather than the instrument's nominal repeatability. The *effective* noise
of a field profile includes terrain, drift, elevation and positioning errors — the
demonstration's noise experiment shows that the achievable derivative accuracy
scales as $\sigma/h$, so an error of a factor of two in $\sigma$ is an error of a
factor of two in the recommended grid spacing. Repeatability quoted on a test
range is rarely the field value, and the whole recommendation is sensitive to it.

If a repeat is impossible, the second-best request is the *acquisition grid and
line spacing*: if the 250 m grid is interpolated from a coarser acquisition, the
real noise is the interpolation error of
[01-12-02](../02-interpolation.md), which no differentiation scheme can undo.
