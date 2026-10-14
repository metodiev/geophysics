# Solutions — 01-02-04 Polynomials, Roots and Asymptotic Behaviour

> **Read this after attempting the exercises, not before.**
>
> Polynomial values, roots and iteration counts were computed with the standard
> library (`decimal` where high precision was needed). Every root reported below
> was substituted back into its polynomial.

---

## ★1 — Reading a cubic

**(a)** Degree 3, leading coefficient $1$.

**(b)** Odd degree with positive leading coefficient, so
$p \to -\infty$ as $x \to -\infty$ and $p \to +\infty$ as $x \to +\infty$.

**(c)**

| $x$ | $p(x)$ |
|---|---|
| $0$ | $-6$ |
| $1$ | $0$ |
| $2$ | $0$ |
| $3$ | $0$ |
| $4$ | $6$ |

**(d)** The roots are $1$, $2$ and $3$; indeed $p(x) = (x-1)(x-2)(x-3)$, which is
verified by expansion:
$x^{3} - 6x^{2} + 11x - 6$. Testing a point inside each interval:

| interval | test point | $p$ | sign |
|---|---|---|---|
| $x < 1$ | $0.5$ | $-1.875$ | negative |
| $1 < x < 2$ | $1.5$ | $+0.375$ | positive |
| $2 < x < 3$ | $2.5$ | $-0.375$ | negative |
| $x > 3$ | $4$ | $+6$ | positive |

So the sign alternates across each of the three **simple** roots, as it must: each
simple factor changes sign once, and the three changes compose to the pattern
$-, +, -, +$. This check is worth performing explicitly rather than asserting,
because the alternation rule *fails* at a root of even multiplicity (★3) — and the
only way to know which case you are in is to evaluate.

---

## ★2 — Horner versus expanded evaluation

**(a)** Expanded: $2(2^{4}) - 3(2^{3}) + 2 - 5 = 32 - 24 + 2 - 5 = 5$.

**(b)** Horner, with coefficients $(2, -3, 0, 1, -5)$:

| step | operation | accumulator |
|---|---|---|
| start | — | $2$ |
| 1 | $2\times2 - 3$ | $1$ |
| 2 | $1\times2 + 0$ | $2$ |
| 3 | $2\times2 + 1$ | $5$ |
| 4 | $5\times2 - 5$ | $5$ |

So $p(2) = 5$. Note the zero coefficient of $x^{2}$: Horner handles missing terms
automatically, whereas the expanded form invites the error of dropping a power.

**(c)** Expanded: two explicit powers ($2^{4}$, $2^{3}$) plus three multiplications
by the coefficients — and the powers themselves cost multiplications. Horner:
$n = 4$ multiplications and 4 additions, four operations fewer and no power
evaluation. For degree $n$, Horner is $n$ multiplications and $n$ additions
against roughly $2n$ multiplications and $n$ additions.

---

## ★3 — Factorisation and multiplicity

Expand $(x-1)^{2}(x+2)$:

$$(x^{2} - 2x + 1)(x + 2) = x^{3} + 2x^{2} - 2x^{2} - 4x + x + 2 = x^{3} - 3x + 2. ✓$$

**(a)** Roots: $x = 1$ with **multiplicity 2**, and $x = -2$ with multiplicity 1.

**(b)** At $x = 1$ the graph **touches** the axis and turns back (even
multiplicity). At $x = -2$ it **crosses** (odd multiplicity). Check: $p(0.9) =
0.729-2.7+2 = 0.029 > 0$ and $p(1.1) = 1.331-3.3+2 = 0.031 > 0$ — the function is
above the axis on both sides, confirming the touch.

**(c)** The relevant derivative is $p'(x) = 3x^{2}-3$:

$$p'(1) = 0, \qquad p'(-2) = 12 - 3 = 9.$$

Since the sensitivity of a root to a coefficient perturbation is
$|\delta r| = |\delta a_k|\,|r|^{k}/|p'(r)|$, the root at $x=1$ has an **infinite**
sensitivity (its derivative vanishes) while the root at $x=-2$ has amplification
$|\delta a_k| \times 1/9$ for the constant term. Any perturbation of the
coefficients — including the rounding error in storing them — moves the double root
by an amount that is *large compared with the perturbation*, while the simple root
moves by a small fraction of it. This is exercised numerically in ★★7 and
★★★9.

---

## ★4 — End behaviour

| polynomial | $x \to +\infty$ | $x \to -\infty$ |
|---|---|---|
| $x^{3} - 3x + 2$ | $+\infty$ | $-\infty$ |
| $x^{4} - x^{2} + 1$ | $+\infty$ | $+\infty$ |
| $-2x^{3} + x$ | $-\infty$ | $+\infty$ |
| $x^{2} + x$ | $+\infty$ | $+\infty$ |

The rule: for even degree both ends go the same way (the sign of the leading
coefficient); for odd degree they go opposite ways. The lower-order terms are
irrelevant to the limit, which is exactly why the leading term is the first thing
to write down.

---

## ★★5 — Bisection on a cubic

**(a)** $p(1) = 1 - 1 - 2 = -2 < 0$ and $p(2) = 8 - 2 - 2 = 4 > 0$, so by the
intermediate value theorem there is a root in $(1,2)$.

**(b)** After $n$ iterations the half-width is $(b-a)/2^{n+1} = 1/2^{n+1}$. Requiring
$1/2^{n+1} < 10^{-3}$ gives $n + 1 > \log_{2}1000 = 9.966$, i.e. $n \ge 9$:

| quantity | value |
|---|---|
| iterations | $9$ |
| bracket | $[1.51953125,\ 1.521484375]$ |
| midpoint | $1.5205078125$ |
| guaranteed error | $9.77\times10^{-4}$ |

**(c)** For a half-width below $10^{-6}$: $n+1 > \log_{2}10^{6} = 19.93$, so
$n = 19$ iterations give the bracket $[1.5213794708251953,\ 1.5213813781738281]$
and the midpoint $1.5213804244995117$, with a guaranteed error of
$9.5\times10^{-7}$.

**(d)** Bisection's advantage is that it **cannot fail** given a sign change: the
error bound is known in advance and is exact. Its disadvantage is speed — one bit
per iteration, so about 3.3 iterations per decimal digit, and 19 iterations here
against 4 for Newton. The practical pattern is to start with a few bisection steps
to get into the basin of attraction and then switch to Newton, which is what
production root finders do.

---

## ★★6 — Newton at a double root

**(a)** $p(x) = (x-1)^{2}(x+3)$, $p'(x) = 2(x-1)(x+3) + (x-1)^{2}$.

| $k$ | $x_k$ | $|x_k - 1|$ |
|---|---|---|
| $0$ | $2.000000000000$ | $1.000\times10^{0}$ |
| $1$ | $1.545454545455$ | $5.455\times10^{-1}$ |
| $2$ | $1.288164665523$ | $2.882\times10^{-1}$ |
| $3$ | $1.148766123765$ | $1.488\times10^{-1}$ |
| $4$ | $1.075693183702$ | $7.569\times10^{-2}$ |
| $5$ | $1.038194799135$ | $3.819\times10^{-2}$ |

**(b)** Ratios $|e_k|/|e_{k-1}|$: $0.5455$, $0.5283$, $0.5163$, $0.5086$, $0.5045$
— decreasing towards $0.5$.

**(c)** For a root of multiplicity $m$, Newton converges linearly with ratio
$(m-1)/m$; for $m = 2$ that is $1/2$, which the measurements approach. For a triple
root the limit would be $2/3$. The measured ratios are *above* $0.5$ and fall
towards it, as the asymptotic result should from a finite distance.

**(d)** The cubic $x^{3}-x-2$ has a simple root and needed 4 iterations; the double
root needs about 50 to reach the same relative error (each step halves the error,
so from $10^{-2}$ to $10^{-16}$ takes about $\log_{2}10^{14} \approx 47$ steps).
For an inversion, this is the behaviour of a misfit surface that is **flat** along
one parameter direction: the gradient gives almost no information about that
parameter, the iteration crawls along the valley floor, and the resulting model
value is poorly determined regardless of how much compute is available. The fix is
to reparametrise or regularise (so that the near-degeneracy becomes a trade-off
you state rather than a numerical accident), not to increase the iteration count.

---

## ★★7 — Sensitivity of a root to the constant term

**(a)** $p(x) = x^{3} - 3x + 2$, $p'(x) = 3x^{2}-3$, so $p'(-2) = 12 - 3 = 9$.

**(b)** For the constant term, $k = 0$ and $r^{0} = 1$:

$$\delta r = -\frac{\delta a_0\,r^{0}}{p'(r)} = -\frac{10^{-3}}{9}
= -1.1111\times10^{-4}.$$

The root moves *down*, by about one ninth of the coefficient change.

**(c)** Solving $x^{3} - 3x + (2 + 10^{-3}) = 0$ near $-2$ by Newton (or by
bisection on $[-2.5,-2]$) gives $r = -2.000111103$, i.e. a measured shift of

$$-1.11103\times10^{-4},$$

against the predicted $-1.11111\times10^{-4}$ — agreement to 0.007%, the residual
being the second-order term in the expansion.

**(d)** The amplification factor is $|r^{k}/p'(r)| = 1/9$ for the constant term,
controlled by $p'(r)$: a **small derivative at the root** means a poorly
determined root position. This is the same quantity that vanishes at a repeated
root (where the amplification becomes unbounded) and the same quantity that
appears as $1/\epsilon$ in ★★★9.

---

## ★★8 — Far-field error of the point-mass form

**(a)**

$$\frac{g(x)x^{3}}{GMh} = \frac{GMh}{(x^{2}+h^{2})^{3/2}}\cdot\frac{x^{3}}{GMh}
= x^{3}\left[x^{2}\left(1+\frac{h^{2}}{x^{2}}\right)\right]^{-3/2}
= \left(1 + \frac{h^{2}}{x^{2}}\right)^{-3/2}.$$

**(b)**

| $x/h$ | ratio | far-field error $1 - $ ratio |
|---|---|---|
| $2$ | $0.715542$ | $2.845\times10^{-1}$ |
| $5$ | $0.942866$ | $5.713\times10^{-2}$ |
| $10$ | $0.985185$ | $1.481\times10^{-2}$ |
| $20$ | $0.996262$ | $3.738\times10^{-3}$ |

**(c)** Requiring $1 - (1+h^{2}/x^{2})^{-3/2} < 10^{-3}$:

$$\left(1+\frac{h^{2}}{x^{2}}\right)^{3/2} > \frac{1}{0.999}
\;\Longrightarrow\;
1 + \frac{h^{2}}{x^{2}} > 0.999^{-2/3} = 1.0006671
\;\Longrightarrow\;
\frac{x}{h} > \sqrt{1499.3} = 38.71.$$

So $x/h \approx 38.7$, i.e. nearly **forty depths** before the far-field form is
good to 0.1%. Bracketing numerically confirms the same value (the function is
monotone, so the bracket is unambiguous).

**(d)** At $x/h = 3$ the ratio is $(1+1/9)^{-3/2} = 0.853815$, so the far-field form
$GMh/x^{3}$ **overestimates** the true $g$ by a factor $1/0.85280 = 1.1726$ — a
**17% error**, and in the direction that makes the estimated mass *too large* if
the mass is inferred from the far-field expression. Quoting a far-field mass
estimate without stating the distance-to-depth ratio is therefore not a result;
$\pm17\%$ is larger than most other errors in such an analysis.

---

## ★★★9 — Root separation controls conditioning

**(a)** $p_\epsilon'(x) = 2x - (2+\epsilon)$, so at the upper root $x = 1+\epsilon$:

$$p_\epsilon'(1+\epsilon) = 2 + 2\epsilon - 2 - \epsilon = \epsilon.$$

With $\delta c = (1+\epsilon)\rho$ (the change in the constant coefficient) and
$k=0$ (so $r^{k} = 1$):

$$\delta r \approx -\frac{\delta c}{p'(r)} = -\frac{(1+\epsilon)\rho}{\epsilon}.$$

The amplification factor is $(1+\epsilon)/\epsilon \approx 1/\epsilon$, which
**diverges** as the roots coalesce. A coefficient known to a relative accuracy
$\rho$ therefore determines the root only to about $\rho/\epsilon$ — worse than the
coefficient itself by the factor $1/\epsilon$.

**(b)** With $\rho = 10^{-10}$, computed at 60 significant digits:

| $\epsilon$ | predicted $\delta r$ | measured $\delta r$ | $\delta r/\epsilon$ |
|---|---|---|---|
| $10^{-1}$ | $-1.100000\times10^{-9}$ | $-1.100000\times10^{-9}$ | $-1.10\times10^{-8}$ |
| $10^{-2}$ | $-1.010000\times10^{-8}$ | $-1.010001\times10^{-8}$ | $-1.01\times10^{-6}$ |
| $10^{-3}$ | $-1.001000\times10^{-7}$ | $-1.001100\times10^{-7}$ | $-1.00\times10^{-4}$ |
| $10^{-4}$ | $-1.000100\times10^{-6}$ | $-1.010307\times10^{-6}$ | $-1.01\times10^{-2}$ |

The predicted and measured shifts agree to about 1% (the discrepancy grows as the
separation shrinks, as the second-order term becomes relatively larger), and
$\delta r/\epsilon$ grows by two decades for each decade of decrease in
$\epsilon$, exactly as $\rho/\epsilon^{2}$ predicts. At $\epsilon = 10^{-4}$ a
$10^{-10}$ relative error in a coefficient has become a **1% error in the root**:
eight orders of magnitude of loss, purely from conditioning.

**(c)** For $x^{2} - (2+\epsilon)x + (1+\epsilon)(1+\rho)$,

$$\Delta = (2+\epsilon)^{2} - 4(1+\epsilon)(1+\rho)
= \epsilon^{2} - 4(1+\epsilon)\rho.$$

The two roots merge into a complex pair when $\Delta < 0$, i.e. when
$\epsilon^{2} < 4(1+\epsilon)\rho$, or to leading order

$$\epsilon < 2\sqrt{\rho}.$$

For $\rho = 10^{-10}$ that threshold is $\epsilon = 2\times10^{-5}$. Verified: the
high-precision calculation returns real roots at $\epsilon = 10^{-4}$ and a
**negative discriminant** (no real roots) at $\epsilon = 10^{-5}$ and below — so a
$10^{-10}$ relative uncertainty in a single coefficient makes two roots that are
separated by $2\times10^{-5}$ *indistinguishable*: the perturbed polynomial does
not even have two real roots. This is the precise sense in which near-degenerate
parameters "cannot be resolved", and it is a statement about the data, not the
solver.

**(d)** Newton from $x_0 = 1+2\epsilon$ with the exact coefficients converges in
**5 or 6** iterations for every $\epsilon$ from $10^{-1}$ down to $10^{-8}$
(measured), i.e. the solver's speed is unaffected. The difficulty is entirely in
the conditioning: with an inexact coefficient, no algorithm can recover the root,
because the information is not in the data. This is the numerical counterpart of
the conditioning-versus-stability distinction of
[01-01-05](../../01-arithmetic/05-error-and-conditioning.md).

**(e) Report.** *Method:* high-precision (60-digit) evaluation of the perturbed
quadratic's roots via the quadratic formula, compared with the first-order
sensitivity formula; the discriminant was formed exactly enough to decide its
sign; Newton iteration counts were measured separately on the exact polynomial.
*Results:* as tabulated and stated above; the two roots become unresolvable below
$\epsilon = 2\sqrt{\rho}$. *Trend:* the root error scales as $\rho/\epsilon$, and
the resolvability threshold as $\sqrt{\rho}$. *Limits:* the numbers are for one
quadratic, one perturbed coefficient and one choice of $\rho$; the *scaling*
($1/\epsilon$ amplification, $\sqrt{\rho}$ threshold) is general to two nearby
roots of any smooth function and is the reason that "resolution" in an inverse
problem is a function of the data uncertainty. Perturbing the coefficient of $x$
instead of the constant term changes the constants but not the scaling: with
$\delta b = -(2+\epsilon)\rho$ we get
$\delta r \approx -(1+\epsilon)(2+\epsilon)\rho/\epsilon$, again $\propto \rho/
\epsilon$.

---

## ★★★10 — How far a Taylor polynomial reaches

**(a)** For $T_n(x) = \sum_{k=0}^{n}(-x)^{k}/k!$ the largest $x$ with relative
error below 1% (found by bisection on the error function):

| $n$ | largest $x$ with $<1\%$ relative error |
|---|---|
| $2$ | $0.3577$ |
| $4$ | $0.8925$ |
| $6$ | $1.4567$ |
| $8$ | $2.0266$ |

**(b)** The valid range grows with $n$, but **sub-linearly**: adding two degrees
extends the range by roughly 0.5 to 0.6 units, whereas for a series with a finite
radius of convergence that grows with the index one would see a much faster
growth. It is certainly not exponential, and it does not saturate — but the
improvement per added degree is modest.

**(c)** Successive terms of the series for $e^{-x}$ have ratio $x/k$: the $k$th
term is $x^{k}/k!$, so each new term is a factor $x/k$ smaller than the previous
one. Truncating after $n$ terms leaves a first omitted term of size
$x^{n+1}/(n+1)!$, which grows with $x$ like $x^{n}/n!$ — that is, the error at
fixed $x$ falls factorially with $n$, so to cover a *larger* $x$ one needs
$n \sim ex$ terms before the factorial overtakes the power. That is the reason the
range grows roughly linearly in $n$ for fixed accuracy, rather than jumping: the
factorial decay is fast in $n$ but the polynomial growth in $x$ has to be beaten
at each step.

**(d)** For a geophysical model linearised by truncating a series — a
small-parameter ray expansion, a linearised inverse problem, or a first-order
Born approximation — the consequence is quantitative: the approximation's
percentage error grows sharply with the size of the parameter, and the parameter
range over which the model is valid must be measured rather than assumed. A
validation test should therefore include the truncated solution *against a
nonlinear reference* (or against higher-order terms) across the full parameter
range of interest, and report the parameter value at which the truncation error
exceeds the measurement uncertainty. A single check at one parameter value,
however accurate, does not establish the range.

---

## Notes on what these solutions do not settle

- The bisection brackets and midpoints are exact results of the stated algorithm
  and tolerance; a different tolerance changes the iteration count, which is why
  the count must always be reported with the stopping rule.
- The Newton iteration counts depend on the starting point and the stopping
  criterion. The numbers quoted are for a relative-error criterion of $10^{-15}$
  and the stated starts; they are illustrative of the *scaling*, not universal.
- The statement that a double root has "infinite" sensitivity is exact for
  $\epsilon = 0$; for $\epsilon > 0$ the sensitivity is $1/\epsilon$, finite but
  unbounded as $\epsilon \to 0$, and that is the version used quantitatively in
  ★★★9.
- No real geophysical dataset is used in this set; every polynomial here is chosen
  to make a numerical point.
