# Solutions — 01-05-01 Limits, Continuity and the Idea of Approximation

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Every numerical value quoted below was computed
> rather than estimated by hand; where a value depends on a floating-point
> implementation, that is stated explicitly.

---

## ★1 — Limits

**(a)** Direct substitution gives $0/0$. Factor the numerator:

$$\lim_{x\to3}\frac{x^{2}-9}{x-3} = \lim_{x\to3}\frac{(x-3)(x+3)}{x-3}
= \lim_{x\to3}(x+3) = \boxed{6}.$$

*Technique:* algebraic cancellation of a removable discontinuity. Note that the
function is undefined at $x = 3$ and the limit nevertheless exists.

**(b)** Multiply by the conjugate, or use the identity
$1-\cos x = 2\sin^{2}(x/2)$:

$$\frac{1-\cos x}{x^{2}} = \frac{2\sin^{2}(x/2)}{x^{2}}
= \frac{1}{2}\left(\frac{\sin(x/2)}{x/2}\right)^{2}
\xrightarrow[x\to0]{}\frac{1}{2}\cdot 1^{2} = \boxed{\tfrac12}.$$

*Technique:* reduce to the fundamental limit $\sin t/t \to 1$.

**(c)** Divide numerator and denominator by $x^{3}$:

$$\frac{4x^{3}-2}{x^{3}+7} = \frac{4 - 2x^{-3}}{1 + 7x^{-3}}
\xrightarrow[x\to\infty]{}\boxed{4}.$$

*Technique:* leading-order behaviour. The result is the ratio of the leading
coefficients, and the correction is $O(x^{-3})$.

**(d)** Write $u = 5x$, so $\sin(5x)/x = 5\sin(u)/u \to 5$:

$$\boxed{5}.$$

---

## ★2 — A kink, not a jump

**(a)** Both one-sided limits equal 0:

$$\lim_{z\to33^{-}}f(z) = \lim_{z\to33^{+}}f(z) = 0 .$$

The function is *continuous* at $z = 33$.

**(b)** With $h > 0$:

$$f'_{-}(33) = \lim_{h\to0^{+}}\frac{f(33-h)-f(33)}{-h}
= \lim_{h\to0^{+}}\frac{h}{-h} = \boxed{-1},$$

$$f'_{+}(33) = \lim_{h\to0^{+}}\frac{f(33+h)-f(33)}{h} = \frac{h}{h} = \boxed{+1}.$$

**(c)** No. The one-sided derivatives exist but are unequal, so the two-sided
limit of the difference quotient does not exist and $f'(33)$ is undefined.

**(d)** A kink is a **gradient discontinuity**: the quantity is continuous and
turns a corner. In a velocity model this is a change of vertical gradient at a
lithological boundary, which bends rays but reflects nothing. A jump
*(discontinuity in value)* also produces a reflection. The two are different
physical boundaries, and a kink is easier to miss in a plot because there is no
visible gap.

---

## ★3 — Classifying discontinuities

| | Kind | Why | Geophysical instance |
|---|---|---|---|
| (a) | **removable** | $\lim_{z\to2}f = 4$ but the function is undefined at $z=2$ | a density assigned by a rule that has a hole at one depth |
| (b) | **jump** | one-sided limits differ and are finite | sediment–basement contact, Moho |
| (c) | **infinite** | $\lvert h\rvert\to\infty$ | the point-mass potential at the source |

For (a) the fix is to *define* $f(2)=4$; for (b) the discontinuity is a physical
claim about the Earth; for (c) the divergence signals that a point source is an
idealisation, and any extended body regularises it (see exercise ★★★7 of the
lesson and [01-05-06](../06-improper-integrals.md)).

---

## ★★4 — Disc potential and the point-mass limit

**(a)** Rationalise. Since
$a^{2} = \left(\sqrt{a^{2}+z^{2}}-z\right)\left(\sqrt{a^{2}+z^{2}}+z\right)$,

$$\sqrt{a^{2}+z^{2}}-z = \frac{a^{2}}{\sqrt{a^{2}+z^{2}}+z}
\;\Longrightarrow\;
\frac{2GM}{a^{2}}\left(\sqrt{a^{2}+z^{2}}-z\right) = \frac{2GM}{\sqrt{a^{2}+z^{2}}+z}. \;\checkmark$$

**(b)** With $u = a/z$:

$$V(z) = \frac{GM}{z}\cdot\frac{2}{\sqrt{1+u^{2}}+1}.$$

Expand $\sqrt{1+u^{2}} = 1 + u^{2}/2 + O(u^{4})$, so the denominator is
$2 + u^{2}/2 = 2(1+u^{2}/4)$ and

$$\frac{2}{2(1+u^{2}/4)} = 1 - \frac{u^{2}}{4} + O(u^{4})
\;\Longrightarrow\;
V(z) = \frac{GM}{z}\left(1 - \frac{a^{2}}{4z^{2}} + \cdots\right).$$

The fractional correction is $-u^{2}/4$.

**(c)** Set $u^{2}/4 = 10^{-4}$: $u^{2} = 4\times10^{-4}$, $u = 0.02$, so
$z = a/u = \boxed{50a}$.

Check against the lesson's table (computed, not hand-estimated): at $z = 10a$
($u = 0.1$) the observed fractional difference was $-2.488\times10^{-3}$, against
the prediction $-u^{2}/4 = -2.5\times10^{-3}$ — agreement to the first two digits,
with the residual explained by the next term in the expansion, which is not
negligible at $u = 0.1$. At $z = 100a$ the prediction is
$-2.5\times10^{-5}$ and the observation was $-2.500\times10^{-5}$. The expansion is
an asymptotic statement: excellent for $u \lesssim 0.1$, and unreliable once $u$ is
of order 1 (at $z = a$, $u = 1$, the prediction $-0.25$ is badly wrong against the
observed $-0.1716$).

---

## ★★5 — Smoothed jumps

**(a)** At $z = 33$ the argument of $\sigma$ is 0, so
$\sigma(0) = 1/2$ and

$$\lim_{z\to33}v_{\epsilon}(z) = 6.0 + 2.0\cdot\tfrac12 = \boxed{7.0\ \mathrm{km\,s^{-1}}}.$$

**(b)** $v_{\epsilon}(33) = 7.0$ km/s for every $\epsilon$, so
$\lim_{\epsilon\to0^{+}}v_{\epsilon}(33) = 7.0$ km/s — the **midpoint** of the jump,
whereas the jump model has no value of its own limit at all.

**(c)** The jump model is the $\epsilon\to0$ limit of the ramp everywhere *except*
at the discontinuity itself, where only one-sided limits survive. So a jump is a
property of an idealised model, not of the Earth: real media always have a
transition of some finite width. What the jump captures correctly is that the
transition is much thinner than the resolving power of the data. **The honest
statement is "the transition is unresolved", not "the transition is a jump".**

---

## ★★6 — Depth for a $10^{-3}$ mGal anomaly

Convert first: $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$, so

$$g_z = 10^{-3}\ \mathrm{mGal} = 10^{-8}\ \mathrm{m\,s^{-2}} .$$

Then

$$d^{2} = \frac{GM}{g_z} = \frac{(6.674\times10^{-11})(10^{9})}{10^{-8}}
= 6.674\times10^{6}\ \mathrm{m^{2}}
\;\Longrightarrow\;
d = \sqrt{6.674\times10^{6}} = 2583.4\ \mathrm{m}.$$

Order-of-magnitude check first: $G\sim6.7\times10^{-11}$,
$M = 10^{9}$, so $GM = 6.7\times10^{-2}$; dividing by $10^{-8}$ gives
$6.7\times10^{6}$ for $d^{2}$, hence $d\approx 2.6\times10^{3}$ m. Consistent.

**Significant figures.** $G$ is given to four figures and $M = 10^{9}$ kg as
stated, but the anomaly itself is quoted to one figure. A one-figure input does not
support a five-figure answer: quote $d \approx 2.6\times10^{3}$ m and state that the
third digit is unconstrained by the anomaly. The realistic reading is
$d \approx 2.6$ km, with the caveat that a change of a few tenths of a mGal in the
observed value moves the last digit. The point-mass approximation is a further
assumption: a body large enough to be detectable at that depth is not a point mass,
and ★4 quantifies the resulting few-percent error.

---

## ★★★7 — Where the numerical limit stops

**(a)** $\sin x = x - x^{3}/6 + \cdots$, so $\sin x - x \approx -x^{3}/6$ and the
*relative* difference from $x$ is $x^{2}/6$. The computation returns exactly 1.0
when this relative difference falls below the machine epsilon:

$$\frac{x^{2}}{6} < \varepsilon \;\Longrightarrow\;
x^{*} = \sqrt{6\varepsilon} = \sqrt{6\times2.22\times10^{-16}}
= \boxed{3.65\times10^{-8}} .$$

The lesson's table shows the computed ratio becoming exactly `1.0` at
$x = 10^{-8} < x^{*}$ and still showing a deviation of `1.665e-15` at
$x = 10^{-7}$, which is just above $x^{*}$: the prediction brackets the observed
threshold correctly.

**(b)** $\tan x = x + x^{3}/3 + \cdots$, so the relative difference is $x^{2}/3$ and
the threshold is

$$x^{*} = \sqrt{3\varepsilon} = \boxed{2.58\times10^{-8}} .$$

Observed: `1.0000000000000033` at $x = 10^{-7}$ (deviation $3.3\times10^{-15}$) and
exactly `1.0` at $x = 10^{-8}$. Again the prediction sits between the last
informative and the first uninformative probe.

**(c)** Here the mechanism is different. $e^{x} - 1$ is computed by subtracting two
numbers that both equal 1 to within $x$; the subtraction is exact, but the absolute
error of each term is $\approx\varepsilon$, so the absolute error of the difference
is $\approx\varepsilon$ and the *relative* error of
$(e^{x}-1)/x \approx x$ is

$$\text{relative error} \approx \frac{\varepsilon}{x} .$$

This is **cancellation, not truncation**: the error *grows* as $x$ shrinks. There
is no threshold below which the answer becomes exactly right; the answer
*deteriorates*. Observed on the same platform:

| $x$ | computed $(e^{x}-1)/x$ | deviation from 1 | $\varepsilon/x$ |
|---|---|---|---|
| $10^{-6}$ | `1.0000004999621837` | $+5.0\times10^{-7}$ | $2.2\times10^{-10}$ |
| $10^{-8}$ | `0.999999993922529` | $-6.1\times10^{-9}$ | $2.2\times10^{-8}$ |
| $10^{-12}$ | `1.000088900582341` | $+8.9\times10^{-5}$ | $2.2\times10^{-4}$ |
| $10^{-16}$ | `0.0` | $-1$ | $2.2\times10^{0}$ |

The observed deviations track $\varepsilon/x$ to within a small factor. At
$x = 10^{-6}$ the deviation is dominated by truncation (the true value is
$1 + x/2 = 1.0000005$, matching to seven digits), which is why that row is the most
accurate one; for $x \lesssim 10^{-8}$ cancellation takes over.

**(d)** The observed thresholds — exactly `1.0` from $10^{-8}$ for both $\sin$ and
$\tan$, and the monotone deterioration for $(e^{x}-1)/x$ — match the predictions.
The lesson to carry forward: **a limit exists for all $x>0$, but the arithmetic you
have can only confirm it above its own floor, and that floor depends on which
combination of operations your formula performs.** The stable form should be used
where one exists: $(e^{x}-1)/x$ is computed accurately by `math.expm1(x)/x`, which
avoids the cancellation entirely.

---

## ★★★8 — Why the far field forgets shape

A model answer, with the mathematics and the assumptions kept separate.

**Mathematics.**

1. Any compact body's external potential can be expanded about a distant point as
   $GM/z$ (monopole) plus terms decaying at least as fast as $(a/z)^{2}$, where $a$
   is the body's size (exercise ★★4 proves this for a disc; the general argument is
   the multipole expansion of
   [01-05-07](../07-sequences-and-series.md)).
2. The monopole term depends on $M$ alone. Shape, density distribution and depth
   enter only at higher order.
3. Therefore, for $z \gg a$ the data determine $M$ to the accuracy of the
   measurement, and the *residual* after subtracting the monopole determines the
   combination of depth and shape that produces the next term.

**Assumptions about the Earth.** That the anomaly is isolated (no interfering
sources), that the observation surface is known, that the density contrast is known
if you want to convert $M$ into a volume, and that the body is compact.

**Quantitative anchor.** With the disc result, the fractional deviation from the
point-mass value is $u^{2}/4$ with $u = a/z$. A survey whose relative accuracy is
$10^{-3}$ can therefore detect the shape only when $u^{2}/4 > 10^{-3}$, i.e.
$u > 0.063$, i.e. $z < 16a$. If the body is ten times deeper than it is wide, the
shape is undetectable at that accuracy, and *no amount of modelling* recovers it
from that data set.

**What breaks the degeneracy.** Data with a smaller $z/a$, field gradients (second
derivatives, which weight the higher multipoles), joint interpretation with
independent constraints (seismic structure, boreholes), and different physics
(magnetics, gravity gradiometry) which weight the source distribution differently.
This is the practical content of the non-uniqueness theorem for potential fields:
the ambiguity is quantitative and is defeated by better data, not by better
algorithms.
