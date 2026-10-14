---
id: 01-05-07
title: "Sequences, Series and Convergence Tests"
level: intermediate
prereqs: ["01-05-01", "01-05-04"]
estimated_minutes: 90
tags: [calculus, series, convergence, iterative-solvers]
---

# Sequences, Series and Convergence Tests

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a sequence from a series, and state what convergence means for
   each.
2. **Apply** the divergence, comparison, ratio, root, integral and alternating
   series tests, and say which test is decisive and which is inconclusive.
3. **Derive** the geometric series remainder and use it to bound any series that
   can be compared with a geometric one.
4. **Prove** that the harmonic series diverges, and explain why a divergent series
   can look convergent numerically for a very long time.
5. **Bound** the error of a truncated alternating series, and explain why the
   simple bound is tight to a factor of two.
6. **Relate** convergence to iterative solvers: fixed-point iteration converges
   linearly with rate $|g'(x^{*})|$, Newton's method quadratically.
7. **Explain** what an asymptotic (divergent but useful) series is, and how it is
   truncated.

## Prerequisites

[01-05-01 Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md)
for limits, and [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md)
for power series. This lesson supplies the convergence theory that lesson 01-05-04
used and deferred.

## 1. Intuition: convergence is the professional question

Two of the questions asked most often in computational geophysics are series
questions:

- **Will this iteration converge?** Fixed-point solvers, Gauss–Newton inversions,
  relaxation methods for potential fields, conjugate-gradient solvers and
  Markov-chain samplers are all sequences, and their usefulness is decided by
  whether the sequence has a limit and how fast it approaches it.
- **How many terms do I need?** Every expansion in a semi-infinite parameter —
  multipoles, moveout in offset, perturbation in a small parameter — is a series
  whose truncation error you have to bound.

The distinction that matters throughout is between *convergence* and *rate of
convergence*. A method that converges as $1/n$ needs ten times the work for one
more digit; a method that converges geometrically needs a fixed amount of work per
digit; a method that converges quadratically (Newton) doubles the number of correct
digits per iteration. All three converge, and only one of them is usable.

## 2. Precise definitions

### 2.1 Sequences

A **sequence** $(a_n)$ is an ordered list of numbers. It **converges** to $L$ if
for every $\varepsilon > 0$ there is an $N$ with $|a_n - L| < \varepsilon$ for all
$n > N$ — the same $\varepsilon$–$N$ structure as the limit of a function.

Useful theorems: a bounded monotone sequence converges; a sequence squeezed between
two sequences with the same limit converges to that limit; if $a_n \to L$ then every
subsequence does.

### 2.2 Series and partial sums

A **series** is a formal sum $\sum_{k=1}^{\infty}a_k$, and it is *defined* by its
sequence of **partial sums** $S_n = \sum_{k=1}^{n}a_k$. The series converges iff
$(S_n)$ converges; its value is $\lim S_n$. The **remainder** is
$R_n = \sum_{k=n+1}^{\infty}a_k = S - S_n$.

A necessary condition: if $\sum a_k$ converges then $a_k \to 0$. The converse is
false — the harmonic series is the standard counter-example — so the **term test**
can only ever prove divergence.

### 2.3 Absolute and conditional convergence

$\sum a_k$ converges **absolutely** if $\sum |a_k|$ converges. Absolute convergence
implies convergence and is preserved under rearrangement of terms. A series that
converges but not absolutely is **conditionally convergent**, and its sum depends on
the order of summation (Riemann's rearrangement theorem). Every numerical
implementation sums in *some* order, so conditional convergence is a practical
warning, not a technicality.

### 2.4 The tests

| Test | Statement | Use |
|---|---|---|
| Term | $a_k \not\to 0 \Rightarrow$ diverges | quick divergence only |
| Geometric | $\sum r^{k}$ converges iff $\lvert r \rvert < 1$ | the reference series |
| $p$-series | $\sum k^{-p}$ converges iff $p > 1$ | comparison standard |
| Comparison | $0 \le a_k \le b_k$, $\sum b_k$ converges $\Rightarrow \sum a_k$ converges | bounding |
| Ratio | $L = \lim \lvert a_{k+1}/a_k\rvert$; converges if $L<1$, diverges if $L>1$ | factorials, exponentials |
| Root | $L = \lim \lvert a_k\rvert^{1/k}$; same verdicts | $k$-th powers |
| Integral | $f$ positive decreasing: $\sum f(k)$ and $\int_1^{\infty}f$ converge or diverge together | $p$-series, logarithms |
| Alternating | $a_k$ decreasing, $a_k \to 0$: $\sum(-1)^{k+1}a_k$ converges | sign-changing series |

The ratio and root tests are **inconclusive when $L = 1$**, and that is not a rare
edge case: it happens for every $p$-series, which is why the integral test exists.

### 2.5 Power series and radius of convergence

A **power series** $\sum a_k(x-c)^{k}$ converges on an interval $(c-R, c+R)$ with
$R = 1/\limsup|a_k|^{1/k}$, the **radius of convergence**, and may or may not
converge at the endpoints. Inside the radius, convergence is absolute; outside, the
series diverges; at the endpoints, anything can happen and each case needs its own
argument. The ratio test applied to the coefficients computes $R$ in practice.

### 2.6 Asymptotic series

A series can be useful without converging. We write $f(x) \sim \sum_{k\ge0}a_k x^{-k}$
as $x \to \infty$ if, for each fixed $N$, the difference between $f$ and the $N$-term
partial sum is $O(x^{-N-1})$. Such a series frequently diverges for every $x$, and is
still the right tool: truncate it at the smallest term and the error is of the order
of that term. This is the structure of every multipole expansion.

## 3. Step-by-step derivations

### 3.1 The geometric series, with its remainder

$$S_n = \sum_{k=0}^{n-1}r^{k} = \frac{1-r^{n}}{1-r} \quad (r \ne 1),
\qquad\text{so}\qquad
S = \frac{1}{1-r}\ \text{ for } |r|<1,\qquad R_n = \frac{r^{n}}{1-r}.$$

The remainder formula is the most useful inequality in numerical analysis: **any
series you can bound by a geometric series has a computable error budget.** The
script sums $r = 0.8$ explicitly:

| terms $n$ | partial sum | error | previous error / this error |
|---|---|---|---|
| 1 | `1.00000000000000000` | `4.000e+00` | — |
| 10 | `4.46312908800000052` | `5.369e-01` | `3.0518` |
| 20 | `4.94235392476965885` | `5.765e-02` | `9.3132` |
| 50 | `4.99992863761536555` | `7.136e-05` | `807.7936` |
| 100 | `4.99999999898148317` | `1.019e-09` | `70064.9420` |

Each of these ratios is $(1/r)^{\text{steps added}}$: from $n=20$ to $n=50$,
$1.25^{30} = 808$; from 50 to 100, $1.25^{50} = 70065$. The error itself falls by
exactly the factor $r = 0.8$ per term, which is what "converges geometrically" means.

### 3.2 The harmonic series diverges — slowly

**Grouping argument.** Combine terms in blocks of lengths $1, 2, 4, 8, \dots$:

$$1 + \frac12 + \left(\frac13+\frac14\right) + \left(\frac15+\cdots+\frac18\right)+\cdots$$

The block from index $2^{k}+1$ to $2^{k+1}$ contains $2^{k}$ terms, each at least
$1/2^{k+1}$, so every block from the second onwards sums to at least $\tfrac12$.
After $k$ complete blocks the partial sum therefore exceeds $1 + k/2$, which is
unbounded, so $H_n \to \infty$.

**Asymptotics.** More precisely, $H_n = \ln n + \gamma + \frac{1}{2n} - \cdots$ with
$\gamma = 0.5772156649\ldots$ the Euler–Mascheroni constant. The script's table:

| $n$ | $H_n$ | $\ln n + \gamma$ | difference |
|---|---|---|---|
| $10^{4}$ | `9.7876060360` | `9.7875560369` | `5.0e-05` |
| $10^{6}$ | `14.3927267229` | `14.3927262229` | `5.0e-07` |
| $10^{7}$ | `16.6953113659` | `16.6953113159` | `5.0e-08` |

At $n = 10^{7}$ the observed difference is $5.004\times10^{-8}$ against
$1/(2n) = 5.0\times10^{-8}$: the first correction term is measured, not quoted.
Note what the table also says — after ten million terms the sum has reached only
16.7. **A divergent series can be numerically indistinguishable from a slowly
convergent one**, which is exactly why an iterative solver's stopping criterion must
be based on the observed rate of change, not on the assumption that "small change
means converged".

### 3.3 The integral test, and the $p$-series

Let $f$ be positive and decreasing on $[1,\infty)$ with $a_k = f(k)$. Comparing
areas with rectangles gives

$$\int_1^{n+1}f(x)\,dx \;\le\; \sum_{k=1}^{n}f(k) \;\le\; f(1) + \int_1^{n}f(x)\,dx,$$

so the series and the integral converge or diverge together. With
$f(x) = x^{-p}$ this gives the $p$-series criterion $\sum k^{-p}$ converges iff
$p > 1$, matching the improper-integral test of
[01-05-06](./06-improper-integrals.md) — the discrete and continuous statements are
the same statement.

The same comparison gives the size of the truncation error for $p = 2$: the tail is
$\sum_{k>n}k^{-2} \approx 1/n$. The script's partial sums confirm it —

| $n$ | partial sum | $\pi^{2}/6$ | gap |
|---|---|---|---|
| 100 | `1.634983900185` | `1.644934066848` | `9.95e-03` |
| $10^{4}$ | `1.644834071848` | `1.644934066848` | `1.00e-04` |
| $10^{6}$ | `1.644933066849` | `1.644934066848` | `1.00e-06` |

exactly one part in $n$, so reaching eight digits would need $n = 10^{8}$ terms.
Knowing the tail size in advance is what lets you budget a computation rather than
hoping.

### 3.4 The ratio test, decisive and inconclusive

For $\sum 10^{n}/n!$ the ratio is $10/(n+1) \to 0$, so the series converges — in
fact to $e^{10}$. The script's ratios are

$$5.000000,\ 1.666667,\ 0.909091,\ 0.476190,\ 0.196078,\ 0.099010$$

at $n = 1, 5, 10, 20, 50, 100$, falling towards zero. The terms themselves fall from
`1.000000e+01` at $n=1$ to `1.071510e-58` at $n=100$, and the largest term is near
$n \approx 9$, where the ratio $10/(n+1)$ passes through 1. Two practical points
follow: the series converges for every fixed $x$ by the ratio test, and summing
largest-term-first is the wrong order for accuracy.

For any $p$-series, by contrast, the ratio is

$$\frac{n^{-p}}{(n+1)^{-p}} = \left(\frac{n+1}{n}\right)^{p} \to 1,$$

so the ratio test tells you nothing: at $n = 10^{4}$ it is already `1.00020001`.
**An inconclusive test is a signal to change tool, not evidence of divergence.**

### 3.5 An alternating series remainder, computed exactly

For $\sum_{k\ge1}(-1)^{k+1}/k = \ln 2$, sum the geometric identity
$\sum_{k=1}^{n}(-x)^{k-1} = \frac{1-(-x)^{n}}{1+x}$ over $[0,1]$:

$$S_n = \int_0^{1}\frac{1-(-x)^{n}}{1+x}\,dx
\quad\Longrightarrow\quad
R_n = \ln 2 - S_n = \int_0^{1}\frac{(-x)^{n}}{1+x}\,dx .$$

Since $1/(1+x)$ is decreasing from 1 to $\tfrac12$ on $[0,1]$,

$$\frac{1}{2(n+1)} = \frac12\int_0^{1}x^{n}dx < \int_0^{1}\frac{x^{n}}{1+x}\,dx
< \int_0^{1}x^{n}dx = \frac{1}{n+1} .$$

So the error is bracketed between half and all of the first omitted term, and it
approaches the lower end for large $n$. The script's column of
$\lvert\text{error}\rvert / (1/(n+1))$ reads `0.5226`, `0.5025`, `0.5002`, `0.5000`,
`0.5000` for $n = 10, 10^{2}, 10^{3}, 10^{4}, 10^{6}$ — the bound is exactly tight
to a factor of two, and now you know why. **The alternating series bound is safe but
pessimistic by a factor of 2 for the alternating harmonic series; the integral
representation tells you which side you are on.**

### 3.6 Sequences that are solvers: fixed-point iteration

To solve $x = g(x)$, iterate $x_{n+1} = g(x_n)$. If $g$ is continuously
differentiable on an interval containing the root $x^{*}$ and $|g'(x^{*})| < 1$,
then for $x_0$ close enough the iteration converges, and

$$x_{n+1} - x^{*} = g(x_n) - g(x^{*}) \approx g'(x^{*})(x_n - x^{*}),$$

so **the error is multiplied by $|g'(x^{*})|$ at every step**. The script solves
$x = \cos x$ from $x_0 = 0.5$; the ratio of successive errors settles on `0.6758`,
`0.6737`, `0.6736` at $n = 10, 20, 40$, matching $|g'(x^{*})| = \sin(0.739085) = 0.673612$
to five figures.

Two practical consequences follow directly from the error law rather than from
experience:

- To reduce the error by $10^{-6}$ you need $n \ge 6 / (-\log_{10}|g'|)$ iterations.
  For $|g'| = 0.6736$ that is about 35 iterations. You can predict this before you
  start.
- If $|g'(x^{*})|$ is close to 1, the method "converges" in theory and is useless in
  practice. This is exactly the situation for slow, nearly-divergent series: the
  mathematics is fine, the rate is not.

### 3.7 Newton's method: quadratic convergence

Newton's method for $f(x) = 0$ is $x_{n+1} = x_n - f(x_n)/f'(x_n)$, which is
fixed-point iteration with $g(x) = x - f/f'$; at the root $g'(x^{*}) = 0$, so the
linear term vanishes and the error obeys

$$e_{n+1} \approx \frac{f''(x^{*})}{2f'(x^{*})}\,e_n^{2} .$$

For $\sqrt 2$ via $x_{n+1} = \tfrac12(x_n + 2/x_n)$ from $x_0 = 1$, the script
records

| $n$ | $x_n$ | error | error / previous error$^{2}$ |
|---|---|---|---|
| 0 | `1.00000000000000000` | `4.142e-01` | — |
| 1 | `1.50000000000000000` | `8.579e-02` | `0.500000` |
| 2 | `1.41666666666666652` | `2.453e-03` | `0.333333` |
| 3 | `1.41421568627450966` | `2.124e-06` | `0.352941` |
| 4 | `1.41421356237468987` | `1.595e-12` | `0.353522` |

The final column settles on $0.353553 = 1/(2\sqrt2)$, which is the constant
$f''/(2f')$ evaluated for $f = x^{2}-2$: the error law is measured, not asserted.
The price is visible too: Newton needs $f'$, and it fails when $f' = 0$ or the
initial guess is outside the basin of attraction. (The row after $n = 4$ breaks the
pattern only because the error has hit the floating-point floor.)

### 3.8 Convergence in floating point, and which question dominates

The script sums $\sum k^{-2}$ to $n = 10^{6}$ forwards and backwards:

| order | value |
|---|---|
| forwards | `1.64493306684877` |
| backwards | `1.6449330668487263` |
| difference | `4.374e-14` |
| true limit $\pi^{2}/6$ | `1.6449340668482264` |
| truncation tail $\approx 1/n$ | `1.000e-06` |

The two orders differ by three parts in $10^{14}$ **and both are wrong by about
$10^{-6}$**. The lesson is the ordering of priorities: bound the mathematical tail
first, then worry about the arithmetic. Summing small terms first is good practice;
it does not substitute for knowing how large the tail is.

### 3.9 Divergent but useful: an asymptotic series

The exponential integral $E_1(x) = \int_x^{\infty}e^{-t}t^{-1}dt$ has the asymptotic
expansion

$$E_1(x) \sim \frac{e^{-x}}{x}\sum_{k\ge0}(-1)^{k}\frac{k!}{x^{k}},$$

which diverges for every $x$ because $k!/x^{k}$ eventually grows without bound. The
script compares partial sums with a quadrature evaluation at $x = 20$:

| terms $k$ | partial sum | relative error |
|---|---|---|
| 0 | `1.030576811219e-10` | `4.781e-02` |
| 4 | `9.835825086277e-11` | `3.048e-05` |
| 8 | `9.835530212487e-11` | `5.004e-07` |

against the quadrature value `9.835525290647515e-11`. The terms decrease while
$k < x$ and increase once $k > x$, so the best available accuracy is of the order of
the smallest term, here about $10^{-6}$ relative. **This is the standard pattern for
multipole expansions in potential-field theory:** they are asymptotic, not
convergent, and they are used by truncating at the smallest term. Expecting a
multipole series to converge is a category error; expecting it to be accurate at the
right truncation is correct.

## 4. Physical interpretation

**Convergence rate is a physical as well as a numerical statement.** Seismic
ray perturbation series, Born scattering series and reflectivity multiple series all
have physical convergence conditions — small velocity contrast, weak scattering,
large impedance contrast — that are exactly the conditions for the corresponding
series to converge. When the series fails, the physics is genuinely different (strong
scattering, wide-angle reflections), not merely harder to compute.

**Conditional convergence is rare in physics and common in signal processing.**
Physical series usually converge absolutely, because their terms are positive
quanta (masses, energies). Fourier-type series can converge conditionally, and their
sums depend on ordering; discretising them requires care.

**Geometric bounds are the currency of numerical error control.** A geometric
remainder, $R_n \le Cr^{n}$, means a fixed amount of work per digit. Anything else
means the cost grows: logarithmically for the alternating harmonic case, and
unboundedly for the harmonic case.

**Divergent asymptotics are not a failure.** Many of the most useful formulas in
geophysics are truncated asymptotic expansions: the multipole expansion of a
potential field, moveout expansions in offset, corrections in the WKB
approximation. Their accuracy is limited by the smallest term, not by the limit of
the series, and the smallest term usually sets the achievable accuracy of the
method.

**Iterative solvers inherit all of this.** A Gauss–Newton inversion is a sequence
whose convergence rate depends on the linearity of the problem; a relaxation solver
for Laplace's equation converges geometrically with a rate that depends on the
grid's aspect ratio; a conjugate-gradient solver's error bound involves
$\sqrt{\kappa}$ where $\kappa$ is the condition number. All are statements about
series and rates.

## 5. Python demonstration

The companion script is
[`code/series_convergence_demo.py`](./code/series_convergence_demo.py), with nine
sections: geometric series, harmonic series, $p$-series, the ratio test, alternating
series, fixed-point iteration, Newton's method, floating-point summation order, and
the asymptotic $E_1$.

The section that best repays study is the fixed-point iteration, because the
observed convergence rate is *predicted* by the derivative of the map:

```python
x, root = 0.5, 0.7390851332151607
for n in range(1, 41):
    x = math.cos(x)
    error = abs(x - root)
    ratio = error / previous if previous else float("nan")
```

Observed:

```
   n                   x_n       |error|   err_n / err_(n-1)
   1    0.8775825618903728     1.385e-01                 nan
   5    0.7681958312820161     2.911e-02              0.6570
  10    0.7350063090148431     4.079e-03              0.6758
  20    0.7390067797808130     7.835e-05              0.6737
  40    0.7390851042254710     2.899e-08              0.6736
  |g'(root)| = |sin(root)| = 0.673612
```

The error ratio converges to the derivative of the map at the fixed point. That is
the whole theory of fixed-point iteration, in one column of output.

The remaining quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 2, harmonic | $H_{10^{7}} = 16.6953113659$ vs $\ln n + \gamma = 16.6953113159$ | difference $5.0\times10^{-8} = 1/(2n)$: the next asymptotic term |
| 3, $p$-series | $p=2$ at $n=10^{6}$ gives `1.644933066849` against $\pi^{2}/6$ = `1.644934066848` | tail $\approx 1/n$, measured |
| 4, ratio test | ratios `5.000000`, `0.909091`, `0.196078`, `0.099010` for $10^{n}/n!$ | decisive; `1.00020001` for any $p$-series: inconclusive |
| 5, alternating | error / bound = `0.5000` over four decades of $n$ | the exact bracket of Section 3.5 |
| 7, Newton | error / previous error² → `0.353522` | $1/(2\sqrt2)$: quadratic convergence |
| 8, summation order | forward `1.64493306684877`, backward `1.6449330668487263` | differ by `4.374e-14`; both truncated by `1e-06` |
| 9, asymptotic $E_1$ | best relative error `5.004e-07` at $k=8$ | divergent series, optimally truncated |

> **Breaking exercise.** Section 6 solves $x = \cos x$. Replace the map with
> $x_{n+1} = 1 + \sin(x_n)/2$ (a different equation with a different fixed point)
> and predict the convergence rate from $|g'(x^{*})|$ before running it. Then predict
> the number of iterations needed for a $10^{-10}$ tolerance using
> $n \approx \log(\text{tolerance})/\log|g'|$.

## 6. Exercises

Full set and worked solutions:
[`exercises/07-sequences-and-series-exercises.md`](./exercises/07-sequences-and-series-exercises.md)
and
[`exercises/07-sequences-and-series-solutions.md`](./exercises/07-sequences-and-series-solutions.md).
Four to start with:

**★1.** State whether each converges, and name the test you used:
(a) $\sum \frac{1}{n^{2}+1}$, (b) $\sum \frac{n}{n+1}$,
(c) $\sum \frac{2^{n}}{n!}$, (d) $\sum \frac{1}{n\ln n}$ (for $n \ge 2$),
(e) $\sum (-1)^{n}\frac{1}{\sqrt n}$.

**★2.** Find the radius of convergence: (a) $\sum \frac{x^{n}}{n}$,
(b) $\sum \frac{n!}{n^{n}}x^{n}$, (c) $\sum \frac{n^{2}}{2^{n}}x^{n}$.
State what happens at the endpoints where you can decide it.

**★★3.** A solver's error decays geometrically with ratio $0.92$ per iteration.
(a) How many iterations are needed to reduce the error by $10^{-6}$? (b) How many
for $10^{-12}$? (c) Compare with a ratio of $0.5$, and state the practical
consequence for solver design.

**★★4.** Prove that $\sum k^{-p}$ converges for $p = 1.001$ using the integral
test, and estimate the number of terms needed for the partial sum to come within
1 % of the limit. Explain why this series converges in theory and is useless in
practice.

**★★★5.** Verify the error term $1/(2n)$ in the harmonic asymptotic by computing
$H_n - \ln n - \gamma$ for $n = 10^{3}, 10^{4}, 10^{5}, 10^{6}$ and fitting
$C/n + D/n^{2}$. Report the fitted constants, and state the limits of your
conclusion (in particular, how the floating-point summation order affects the
result).

## 7. Common mistakes

1. **Concluding convergence from $a_n \to 0$.** The harmonic series disproves it.
   The term test proves only divergence.
2. **Using the ratio test on a $p$-series.** The limit is 1, which is inconclusive;
   the integral or comparison test decides it.
3. **Judging convergence from the first few terms.** $H_{10^{7}} \approx 16.7$ and
   rising; the first ten terms look perfectly convergent.
4. **Rearranging a conditionally convergent series.** Riemann's theorem says the sum
   changes. Numerical summation order is a rearrangement.
5. **Forgetting the endpoint at the radius of convergence.** Convergence *at* the
   radius requires a separate argument ($\sum x^{n}/n$ converges at $x = -1$ and
   diverges at $x = 1$).
6. **Expecting a divergent series to be worthless.** Section 3.9's asymptotic
   expansion gives five correct digits where the diverging series is truncated
   correctly.
7. **Assuming small change means converged.** With a ratio of 0.999, a small change
   per step still leaves a large error for many steps; the ratio, not the step size,
   is the diagnostic.
8. **Confusing the truncation error with the round-off error.** Section 3.8 shows a
   case where round-off is twelve orders of magnitude smaller than truncation. Both
   exist; the larger one governs.

## 8. Real-world applications

- **Iterative inversion.** Gauss–Newton and its relatives converge quadratically
  near a well-behaved solution and linearly (or not at all) otherwise; the
  diagnostics are the same error ratios computed here. See
  [18-inverse-problems](../../18-inverse-problems/README.md).
- **Relaxation and multigrid solvers.** Convergence rates for iterative PDE solvers
  are spectral radii of iteration matrices, and the design of multigrid is
  explicitly a convergence-rate argument. See
  [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).
- **Moveout and travel-time expansions.** The parabolic NMO equation of
  [01-05-04](./04-taylor-series.md) is the first term of a series in offset; whether
  the series converges or is merely asymptotic determines whether higher-order
  terms help.
- **Multiple reflections.** The reflectivity series for a layered medium is a
  geometric series in the reflection coefficients; its convergence (multiplied by
  internal attenuation) determines whether the "multiples are small" assumption
  holds. See [06-seismology](../../06-seismology/README.md).
- **Multipole and moment expansions.** Gravity and magnetic field expansions are
  asymptotic in $a/z$; the achievable accuracy is set by the smallest term, exactly
  as in Section 3.9. See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Markov-chain Monte Carlo.** Convergence diagnostics for MCMC samplers are
  tests on sequences and are only as trustworthy as the mixing rate they assume.
  See [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 22–24.
  Level: beginner upward. Sequences, series and the standard convergence tests,
  proved carefully.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapters 10–11.
  Level: beginner to intermediate. Power series, radius of convergence, and the
  integral test.
- **Courant, R. & John, F. *Introduction to Calculus and Analysis, Vol. I*.
  Springer.** Level: intermediate. A classical treatment with an emphasis on
  asymptotic behaviour rather than on tests for their own sake.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapters 1–4. Level: advanced undergraduate upward. Summation
  order, compensated summation and the convergence-rate analysis of iterative
  methods.
- **Menke, W. (2012). *Geophysical Data Analysis: Discrete Inverse Theory*
  (3rd ed.). Academic Press.** Chapter 3. Level: intermediate. Iterative solvers in
  geophysics, with the convergence criteria in the notation of this lesson.
- **Trefethen, L. N. & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.** Lectures
  38–40. Level: advanced. Convergence of iterative methods, and why the distinction
  between convergence and rate of convergence is decisive.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not reproduce copyrighted text; confirm editions and
> availability through your library before citing them. Chapter, lecture and
> section references are indicative rather than authoritative: editions differ in
> numbering and content, so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can distinguish a sequence from a series and state both convergence
      criteria.
- [ ] I can choose an appropriate convergence test and, crucially, recognise when a
      test is inconclusive.
- [ ] I can derive the geometric-series remainder and use it to bound another
      series.
- [ ] I can prove the harmonic series diverges and quote the measured size of its
      next asymptotic correction.
- [ ] I can bound and explain the error of a truncated alternating series.
- [ ] I can predict the convergence rate of a fixed-point iteration from
      $|g'(x^{*})|$ and the number of iterations a tolerance requires.
- [ ] I can explain the difference between a convergent series and an asymptotic
      one, and how each is truncated.

## 11. Related lessons

- [01-05-01 Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md) —
  the definition of a limit that everything here builds on.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md) —
  the power series whose convergence this lesson makes rigorous.
- [01-05-06 Improper Integrals, Singularities and Convergence](./06-improper-integrals.md) —
  the continuous counterpart of the integral test.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  root finding, iteration and error control in practice.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md) —
  the spectral radius that governs the convergence rate of linear iterations.
- [18-inverse-problems](../../18-inverse-problems/README.md) — where solver
  convergence and rate decide whether an inversion is usable.
