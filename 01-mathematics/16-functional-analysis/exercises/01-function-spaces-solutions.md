# Solutions — 01-16-01 Vector Spaces of Functions, Norms and Inner Products

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output, except where a computation is explicitly
> identified as one performed for these solutions.

---

## ★1 — Norm axioms

**(N1)** $\lVert f\rVert_\infty = \sup_{x}\lvert f(x)\rvert = 0$ holds exactly
when $\lvert f(x)\rvert = 0$ for every $x$, i.e. $f$ is the zero function. For
$f \in C[0,1]$ the supremum is attained (continuous on a compact set), so
$\sup = 0$ forces $f \equiv 0$.

**(N2)** $\lVert \alpha f\rVert_\infty = \sup_x \lvert\alpha f(x)\rvert =
\lvert\alpha\rvert \sup_x\lvert f(x)\rvert = \lvert\alpha\rvert\lVert
f\rVert_\infty$, because $\lvert\alpha\rvert \ge 0$ can be pulled out of a
supremum.

**(N3)** For every $x$, $\lvert f(x) + g(x)\rvert \le \lvert f(x)\rvert +
\lvert g(x)\rvert \le \lVert f\rVert_\infty + \lVert g\rVert_\infty$. The
right-hand side is a constant upper bound, so the supremum of the left side is at
most it.

**Failure of (N1) for pointwise objects.** Define $f(0) = 1$ and $f(x) = 0$ for
$x > 0$. As a pointwise function $f \ne 0$, but $\int_0^1\lvert f\rvert\,dx = 0$.
So $\lVert f\rVert_1 = 0$ with $f \ne 0$, and (N1) fails. The repair is to
identify functions that agree almost everywhere — that is, to work with
equivalence classes — which is what $L^1$ and $L^2$ mean. This is exactly the
caveat of Section 2.1 of the lesson: a single-point change in a model is
invisible to any $L^p$-based method.

---

## ★2 — The three norms of $\sin(\pi x)$

$$\lVert f\rVert_1 = \int_0^1 \sin(\pi x)\,dx = \frac{2}{\pi} = 0.6366198$$

$$\lVert f\rVert_2^2 = \int_0^1 \sin^2(\pi x)\,dx = \frac12
\quad\Longrightarrow\quad \lVert f\rVert_2 = \frac{1}{\sqrt2} = 0.7071068$$

$$\lVert f\rVert_\infty = 1 \quad (\text{attained at } x = 1/2)$$

Ratios:

$$\frac{\lVert f\rVert_1}{\lVert f\rVert_2} = \frac{2/\pi}{1/\sqrt2}
= \frac{2\sqrt2}{\pi} = 0.9003163,\qquad
\frac{\lVert f\rVert_\infty}{\lVert f\rVert_2} = \sqrt2 = 1.4142136,\qquad
\frac{\lVert f\rVert_\infty}{\lVert f\rVert_1} = \frac{\pi}{2} = 1.5707963.$$

The last two are independent of the function, and the reason is scaling: for a
pure sinusoid $f = A\sin(\pi x)$, $A$ cancels in every ratio, and the remaining
constants are those of the sine itself. The first ratio, $0.9003163 =
2\sqrt2/\pi$, is also a pure number for this family — it is not universal, and a
different function gives a different $L^1/L^2$ ratio (compare $f = x(1-x)$, for
which the demo reports $0.912871$).

---

## ★3 — Discretising the $L^2$ norm

On a uniform grid with spacing $h$, the two forms are

$$\sum_{i=1}^{n} f_i^2 \qquad\text{and}\qquad h\sum_{i=1}^{n} f_i^2 .$$

The second is a Riemann sum for $\int f^2$; the first is that sum without the
measure. They are related by $\lVert f\rVert_{2,\text{weighted}} =
\sqrt{h}\,\lVert f\rVert_{2,\text{unweighted}}$.

With $h = 10^{-3}$, $\sqrt{h} = 0.0316228$, so an unweighted error of $10^{-4}$
corresponds to a continuum-norm error of $10^{-4}\times0.0316228 =
3.162\times10^{-5}$. **Quoting $10^{-4}$ as an $L^2$ error without the weight is
too pessimistic here by a factor of $\sqrt{h}$** — and, worse, the factor changes
with $h$, so a convergence study using unweighted norms reports a spurious extra
factor of $h^{1/2}$ in the rate. This is the single most common source of
inconsistent convergence orders in student work.

---

## ★4 — Monotonicity in $p$, and a large ratio

**Monotonicity.** Let $q < p$ and assume $\lVert f\rVert_p = 1$ (the general case
follows by scaling, since both sides are homogeneous of degree 1). Then
$\lvert f\rvert^q \le \lvert f\rvert^p$ wherever $\lvert f\rvert \le 1$, and
where $\lvert f\rvert > 1$ the measure of that set is at most $\lvert\Omega\rvert$
which is finite. More cleanly: apply Hölder to
$\lvert f\rvert^q = \lvert f\rvert^q\cdot 1$ with exponents $p/q$ and its
conjugate:

$$\int\lvert f\rvert^q \le \left(\int\lvert f\rvert^p\right)^{q/p}
\lvert\Omega\rvert^{1-q/p}
\ \Longrightarrow\
\lVert f\rVert_q \le \lVert f\rVert_p\,\lvert\Omega\rvert^{1/q - 1/p}.$$

With $\lvert\Omega\rvert = 1$ this is $\lVert f\rVert_q \le \lVert f\rVert_p$.
The finiteness of $\lvert\Omega\rvert$ is used in the second factor, which is why
the statement fails on $\mathbb{R}$.

**Example.** $f_n(x) = x^n$ on $[0,1]$:
$\lVert f_n\rVert_1 = 1/(n+1)$, $\lVert f_n\rVert_\infty = 1$, so
$\lVert f_n\rVert_\infty/\lVert f_n\rVert_1 = n+1$. For $n = 3$ this is already
$4 > 3$. The demo confirms the individual norms:

```text
         n      ||f_n||_L2    1/sqrt(2n+1)   ||f_n||_Linf    f_n(1)
         1      0.57735027      0.57735027       1.000000       1.0
         2      0.44721360      0.44721360       1.000000       1.0
         5      0.30151134      0.30151134       1.000000       1.0
        10      0.21821789      0.21821789       1.000000       1.0
```

---

## ★5 — Hölder, boundedness, and the unbounded point evaluation

**Hölder for $(1,\infty)$.** $\lvert\langle f,g\rangle\rvert \le
\lVert f\rVert_1\lVert g\rVert_\infty$, that is
$\lvert\int fg\rvert \le \int\lvert f\rvert \cdot \lVert g\rVert_\infty$.
Equality holds if and only if $\lvert g(x)\rvert = \lVert g\rVert_\infty$ almost
everywhere on the set where $f \ne 0$.

**Boundedness of point evaluation on $C[0,1]$.** With the supremum norm,
$\lvert\ell(f)\rvert = \lvert f(x_0)\rvert \le \lVert f\rVert_\infty$, so
$\lVert\ell\rVert_{C^*} \le 1$; taking $f \equiv 1$ gives equality, so
$\lVert\ell\rVert_{C^*} = 1$.

**Unboundedness of point evaluation on $L^2$.** Let

$$f_\varepsilon(x) = \begin{cases} 1/\varepsilon, & \lvert x - x_0\rvert \le
\varepsilon/2,\\ 0 & \text{otherwise.}\end{cases}$$

Then $f_\varepsilon(x_0) = 1/\varepsilon$ while

$$\lVert f_\varepsilon\rVert_2 = \left(\int \frac{1}{\varepsilon^2}\,dx\right)^{1/2}
= \left(\frac{1}{\varepsilon^2}\cdot\varepsilon\right)^{1/2}
= \frac{1}{\sqrt{\varepsilon}} .$$

The ratio is

$$\frac{\lvert f_\varepsilon(x_0)\rvert}{\lVert f_\varepsilon\rVert_2}
= \frac{1}{\varepsilon}\sqrt{\varepsilon} = \frac{1}{\sqrt{\varepsilon}}
\ \xrightarrow[\varepsilon\to0]{}\ \infty .$$

For $\varepsilon = 10^{-4}$ the ratio is $1/\sqrt{10^{-4}} = 100$: a function of
$L^2$ norm $0.01$ can have value $1$ at a point. So no finite $C$ bounds point
evaluation in $L^2$, and this is precisely the statement that
$\delta(\cdot - x_0) \notin L^2$. Equality in the bound is not available because
no $L^2$ function is a point mass; the honest setting is the dual space of a
space of continuous or $H^1$ functions, as Section 7 of the lesson says.

---

## ★6 — The norm choice, with a smaller outlier

The demo's table for the $+1.8$ s outlier:

| criterion | intercept (s) | slope (s/km) | cost | residual at $x=10$ |
|---|---|---|---|---|
| $L^2$ | $-0.1600$ | $0.5982$ | $1.4563$ | $-1.1782$ |
| $L^1$ | $0.2000$ | $0.5000$ | $1.8001$ | $-1.8000$ |
| $L^\infty$ | $-0.6477$ | $0.6840$ | $0.8080$ | $-0.8080$ |

With the outlier reduced to $+0.2$ s (computed directly for these solutions by
the same two-stage grid search):

| criterion | intercept (s) | slope (s/km) | cost |
|---|---|---|---|
| $L^2$ | $0.1618$ | $0.5109$ | — |
| $L^1$ | $0.2000$ | $0.5000$ | — |

The $L^2$ slope moves from $0.5982$ to $0.5109$, against a true $0.5000$: the
bias falls from 19.6 per cent to 2.2 per cent. $L^1$ is unchanged to four
decimals (it already fitted the ten good picks exactly, so shrinking the outlier
only reduces the residual it carries).

**Interpretation.** The norm choice matters in proportion to how much the
outlier exceeds the bulk of the residuals. With a 1.8 s error against picks that
otherwise have zero error, $L^2$ is badly biased; with a 0.2 s error the bias is
comparable to the discretisation of the grid search used to fit it. The practical
rule that follows: choose a robust norm when the expected fraction of gross
errors is non-negligible, and check the sensitivity by refitting under a second
norm — as here, the two answers agreeing is evidence, and disagreeing tells you
how much the conclusion depends on the assumption.

---

## ★7 — The finite-dimensional equivalence constant

**Upper bound.** For $x \in \mathbb{R}^n$,
$\lVert x\rVert_1 = \sum_i \lvert x_i\rvert \le \sqrt{n}\left(\sum_i
x_i^2\right)^{1/2} = \sqrt{n}\,\lVert x\rVert_2$ by Cauchy–Schwarz applied to the
vectors $(\lvert x_1\rvert,\dots,\lvert x_n\rvert)$ and $(1,\dots,1)$. Equality
requires $\lvert x_i\rvert$ to be the same for every $i$, i.e.
$x = \frac{1}{\sqrt{n}}(\pm1,\dots,\pm1)$. That vector has
$\lVert x\rVert_2 = 1$ and $\lVert x\rVert_1 = \sqrt{n}$, so the bound is attained
and the constant is exactly $\sqrt{n}$.

**Measured values.** The demonstration reports maxima over 200 Gaussian random
vectors for each $n$:

| $n$ | measured $\max\lVert x\rVert_1/\lVert x\rVert_2$ | $\sqrt{n}$ | ratio |
|---|---|---|---|
| 10 | 3.0544 | 3.1623 | 0.966 |
| 100 | 8.4326 | 10.0000 | 0.843 |
| 1000 | 25.7408 | 31.6228 | 0.814 |
| $10^4$ | 80.4228 | 100.0000 | 0.804 |

The ratios fall from 0.97 to 0.80 as $n$ grows. That is expected: the extremal
vector is a *fixed* $\pm1$ pattern, and its probability under a Gaussian
distribution of $\mathbb{R}^n$ decreases with $n$ — 200 samples cannot find it at
$n = 10^4$. The bound is attained, but not by random samples; the numbers above
are lower bounds on the true maximum, which is why they fall short by a
$n$-dependent and sampling-dependent amount. This is worth stating plainly: a
measured "worst case" over random draws is not a bound, and the lesson's use of
the values is as evidence for the growth of the constant, not as an estimate of
its value.

---

## ★8 — Weighted fit

Minimising $\chi^2 = \sum_i (r_i/\sigma_i)^2$ with $\sigma_i = 0.05 + 0.02x_i$
(the same two-stage grid search, with residuals divided by $\sigma_i$) gives

$$\text{intercept} = 0.0837\ \text{s}, \qquad \text{slope} = 0.5495\ \text{s/km},
\qquad \chi^2 = 6.3981 .$$

**(a)** The true slope is $0.5000$. The unweighted $L^2$ slope was $0.5982$; the
weighted slope is $0.5495$, so weighting halves the induced bias. The weighted
fit is still biased away from the truth, because it is still $L^2$: the outlier
is down-weighted, not removed.

**(b)** $\sigma_1 = 0.07$ and $\sigma_{10} = 0.25$, so the ratio is
$0.25/0.07 = 3.571$, or $1/\sigma^2$ ratio of $12.8$. The far-offset pick — the
outlier — has 12.8 times less influence than it would have relative to an
equal-weight fit. Early offsets gained; the last offset lost by more than a factor
of ten in squared weight.

**(c)** $\chi^2$ and the unweighted sum of squares are different numbers with
different scales; comparing them directly is meaningless. The correct comparison
is between the *weighted* residual at the weighted optimum and the *weighted*
residual at the unweighted optimum; the latter is larger by construction because
the weighted optimum minimises it. Any statement of the form "the weighted fit
has a larger $\chi^2$" is a units error.

---

## ★9 — Huber misfit

Fitted for the pick set with the $+1.8$ s outlier (values computed for these
solutions with the same grid-search solver):

| $\gamma$ | intercept (s) | slope (s/km) |
|---|---|---|
| 0.05 | 0.1847 | 0.5042 |
| 0.10 | 0.1694 | 0.5083 |
| 0.20 | 0.1389 | 0.5167 |
| 0.50 | 0.0472 | 0.5417 |
| 1.00 | $-0.1056$ | 0.5833 |
| 1.50 | $-0.1600$ | 0.5982 |
| 2.00 | $-0.1600$ | 0.5982 |

**(a)** As tabulated.

**(b)** The transition occupies roughly $\gamma \in [0.2, 1.0]$. The limits are
the $L^1$ answer, slope $0.5000$ (approached as $\gamma \to 0$: at $\gamma = 0.05$
the slope is $0.5042$), and the $L^2$ answer, slope $0.5982$, reached already at
$\gamma = 1.5$ and unchanged at $\gamma = 2.0$.

**(c)** Residuals at the optimum are essentially zero for the nine good picks and
$-1.8$ at the outlier (in the $L^2$ solution; slightly less under Huber). The
Huber cost quadratically penalises only residuals below $\gamma$ and linearly
penalises those above. For $\gamma$ above about $1.5$ the outlier's residual is
entirely in the quadratic region, so the cost reduces to $L^2$ and the answer is
identical. For $\gamma$ below about $0.2$ the outlier is entirely in the linear
region, so the cost is $L^1$ in the direction that matters and the answer tends to
the $L^1$ answer. The practical rule: set $\gamma$ to about $1$–$2$ estimated
standard deviations of the noise, measured robustly (e.g. from the median absolute
deviation), not to the size of the error you suspect. Setting $\gamma$ larger than
the gross errors makes the estimator $L^2$ and delivers no robustness at all,
which is the trap the $\gamma = 1.5$ and $2.0$ rows demonstrate.

---

## ★10 — Critical response to "misfit 0.4 per cent"

A model answer, in five parts.

**(a) Which norm?** The number 0.4 per cent is $\lVert r\rVert/\lVert d\rVert$ in
*some* norm. $L^2$ on the whole data set, $L^\infty$ on the worst datum and
$L^1$ give three different numbers for the same residuals — by up to a factor of
37 on a single function in Section 3.3 of the lesson. Ask for the norm, whether
weights were used, and whether the percentage is relative to $\lVert d\rVert$ or
to some other reference.

**(b) Small in norm, large pointwise.** The demo's $f_n(x) = x^n$ has
$\lVert f_n\rVert_2 = 1/\sqrt{2n+1}$, which is 2.2 per cent for $n = 1000$, while
$\lVert f_n\rVert_\infty = 1$ and $f_n(1) = 1$. A residual with a relative $L^2$
size of 0.4 per cent can therefore conceal a 100 per cent error at one location.
For a well-location or a hazard question, that is the entire answer.

**(c) Units and weighting.** A sum of squared residuals in mixed units is
dimensionally meaningless; if the data set mixes gravity and travel times, the
percentage is not interpretable. If the data have unequal error levels, an
unweighted percentage is dominated by whichever subset has the largest
magnitude.

**(d) Is 0.4 per cent below the noise level?** If the data carry 1 per cent noise
and the fit achieves 0.4 per cent, the fit is *better than the data*, which is
the signature of over-fitting the noise (this is measured explicitly in lesson
01-16-07, where a residual below the noise level accompanies a larger model
error). It is evidence against the model, not for it.

**(e) What would make it defensible?** The norm and the weights; the data error
level and how it was estimated; the model norm or a resolution estimate so that
the reader can see what was traded away; and a statement of the discretisation, so
that the reader can judge whether the misfit is limited by physics or by the grid.
Four numbers, none of them hard to produce, and together they turn a percentage
into evidence.
