# Solutions — 01-05-07 Sequences, Series and Convergence Tests

> **Read this after attempting the exercises, not before.** Every numerical value was
> computed. Where a verdict depends on a test that is *inconclusive*, that is stated
> rather than glossed over.

---

## ★1 — Convergence verdicts

**(a) Converges.** Limit comparison with $\sum 1/n^{2}$: since
$1/(n^{2}+1) \le 1/n^{2}$ and $\sum n^{-2}$ converges ($p = 2 > 1$), comparison
settles it.

**(b) Diverges.** The terms are $n/(n+1) \to 1 \ne 0$, so the term test gives
divergence immediately. This is the most common way a series fails.

**(c) Converges.** Ratio test:

$$\frac{a_{n+1}}{a_n} = \frac{2^{n+1}/(n+1)!}{2^{n}/n!} = \frac{2}{n+1} \to 0 < 1 .$$

**(d) Diverges.** Integral test with $f(x) = 1/(x\ln x)$, positive and decreasing for
$x \ge 2$:

$$\int_2^{\infty}\frac{dx}{x\ln x} = \left[\ln\ln x\right]_2^{\infty} = \infty .$$

Note that $1/(n\ln n)$ goes to zero *faster* than $1/n$ and still diverges. Only the
integral (or a comparison) reveals it; the term test cannot.

**(e) Converges (conditionally).** The alternating series test applies: $1/\sqrt n$ is
positive, decreasing and tends to 0. But $\sum n^{-1/2}$ diverges ($p = 1/2 < 1$), so
the convergence is **conditional** — the series cannot be rearranged freely.

---

## ★2 — Radii of convergence

**(a)** $\lvert a_{n+1}/a_n\rvert = \dfrac{n}{n+1}\to1$, so $R = 1$. Endpoints:
at $x = 1$ the series is the harmonic series → **diverges**; at $x = -1$ it is the
alternating harmonic series → **converges** (to $-\ln 2$). The two endpoints behave
differently, which is exactly why endpoints need separate treatment.

**(b)** Here $a_n = n!/n^{n}$ and

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^{n}}{n!}
= \frac{n^{n}}{(n+1)^{n}} = \frac{1}{\left(1+\frac{1}{n}\right)^{n}} \to \frac{1}{e} .$$

So $L = 1/e$ and $R = e \approx 2.71828$. At $x = \pm e$ the terms do not tend to
zero (Stirling's approximation makes $a_n e^{n} \sim \sqrt{2\pi n}$), so the series
**diverges at both endpoints**.

**(c)** $\lvert a_{n+1}/a_n\rvert = \dfrac{(n+1)^{2}/2^{n+1}}{n^{2}/2^{n}}
= \dfrac{1}{2}\left(1+\frac{1}{n}\right)^{2} \to \dfrac12$, so $R = 2$. At
$x = \pm2$ the terms are $n^{2}(\pm1)^{n}$, which do not tend to zero, so the series
**diverges at both endpoints**.

---

## ★3 — Geometric remainder

For $\lvert r\rvert<1$, $S = \dfrac{1}{1-r}$ and $R_n = \dfrac{r^{n}}{1-r}$ (truncating
after $n$ terms, i.e. keeping $k = 0,\dots,n-1$).

With $r = 0.4$ and $n = 8$:

$$R_8 = \frac{0.4^{8}}{0.6} = \frac{6.5536\times10^{-4}}{0.6} = \boxed{1.092\times10^{-3}} .$$

For $R_n < 10^{-6}$:

$$\frac{0.4^{n}}{0.6} < 10^{-6} \;\Longrightarrow\; 0.4^{n} < 6\times10^{-7}
\;\Longrightarrow\;
n > \frac{\ln(6\times10^{-7})}{\ln 0.4} = \frac{-14.326}{-0.9163} = 15.63 ,$$

so $n = \boxed{16}$ terms. The geometric remainder is the most useful error estimate in
numerical analysis precisely because it converts an accuracy request into a term count
by one logarithm.

---

## ★★4 — Iterations for a geometric rate

Solve $r^{n} = \text{tol}$ for $n = \ln(\text{tol})/\ln r$.

**(a)** $n = \dfrac{\ln 10^{-6}}{\ln 0.92} = \dfrac{-13.8155}{-0.08338} = 165.7$, so
$\boxed{166}$ iterations.

**(b)** $n = \dfrac{\ln 10^{-12}}{\ln 0.92} = \dfrac{-27.631}{-0.08338} = 331.4$, so
$\boxed{332}$ iterations. Note that doubling the number of digits doubles the work:
that is what a constant contraction factor costs.

**(c)** With $r = 0.5$: $n = 13.8155/0.69315 = 19.9 \to 20$ iterations for $10^{-6}$,
and $39.9 \to 40$ for $10^{-12}$. The ratio of work between the two rates is about
8.3 — the difference between a method you use and a method you avoid.

**(d)** A rate of $0.92$ means each iteration removes only $0.036$ of a decimal digit;
$0.5$ removes $0.301$ per iteration, an order of magnitude more. **Solver design is
about the contraction factor, not about the existence of convergence.** In a linear
iteration $\mathbf{x}_{n+1} = M\mathbf{x}_n + \mathbf{c}$ the role of $r$ is played by
the **spectral radius** $\rho(M)$ — the largest eigenvalue magnitude of the iteration
matrix — and the design of preconditioners and multigrid methods is entirely an
attempt to reduce $\rho(M)$. See
[01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../07-linear-algebra/06-eigenvalues.md).

---

## ★★5 — The alternating harmonic series

**(a)** If $a_k$ decreases to 0, the alternating series has
$\lvert R_n\rvert \le a_{n+1} = \dfrac{1}{n+1}$.

**(b)** At $n = 1000$ the partial sum is (computed)
`0.6926474305598203`, against $\ln 2 = 0.6931471805599453$: the true error is
$4.998\times10^{-4}$, and the bound is $1/1001 = 9.99\times10^{-4}$. The true error is
**0.5002 of the bound**.

**(c)** With the integral representation

$$R_n = \int_0^{1}\frac{x^{n}}{1+x}\,dx,$$

the integrand $x^{n}/(1+x)$ is concentrated near $x = 1$ for large $n$, where
$1/(1+x)\to\frac12$. Hence

$$\int_0^{1}x^{n}dx = \frac{1}{n+1} \quad\text{(the bound)} \qquad\text{but}\qquad
R_n \approx \frac12\int_0^{1}x^{n}dx = \frac{1}{2(n+1)},$$

because the weight is very nearly $\frac12$ over the region that supplies the integral.
A tighter bracket, valid for all $n$,

$$\frac{1}{2(n+1)} < \int_0^{1}\frac{x^{n}}{1+x}dx < \frac{1}{n+1},$$

follows from $\frac12 \le \frac{1}{1+x} \le 1$ on $[0,1]$.

**(d)** From the bound: $1/(n+1) < 10^{-8}$ gives $n > 10^{8} - 1$. From the sharper
estimate: $1/(2(n+1)) < 10^{-8}$ gives $n > 5\times10^{7}$. So the honest answer is
about $5\times10^{7}$ to $10^{8}$ terms — half a billion terms for eight digits, which
is the practical meaning of "converges like $1/n$".

---

## ★★★6 — The harmonic asymptotic constants

**(a)** Computed values of $d_n = H_n - \ln n - \gamma$:

| $n$ | $d_n$ | $n\,d_n$ | $n^{2}d_n$ |
|---|---|---|---|
| $10^{3}$ | `4.999167e-04` | `0.499917` | `499.917` |
| $10^{4}$ | `4.999917e-05` | `0.499992` | `4999.917` |
| $10^{5}$ | `4.999992e-06` | `0.499999` | `49999.916` |
| $10^{6}$ | `4.999992e-07` | `0.499999` | `499999.18` |

**(b)** The column $n\,d_n$ settles on **0.5**, so $C = 1/2$. The column $n^{2}d_n$
grows like $n/2$, which identifies $D$ through
$n^{2}d_n = Cn + D = n/2 + D$: at $n = 10^{3}$ this gives
$D = 499.917 - 500 = -0.083$, i.e. $D = -1/12 = -0.08333$ within the precision of the
table. So

$$H_n = \ln n + \gamma + \frac{1}{2n} - \frac{1}{12n^{2}} + O(n^{-3}),$$

confirming the standard series. Note the method: *two* columns were needed, because one
constant cannot be read off a single scaling.

**(c)** At $n = 10^{7}$ the extracted value of $d_n$ drifts: the table would give
$d_n = 4.9997\times10^{-8}$ against the asymptotic $1/(2n) = 5.000\times10^{-8}$, a
relative deviation of $5\times10^{-5}$ — far larger than the $1/(12n^{2})$ term, which
is $8\times10^{-17}$. The cause is **floating-point accumulation**: the partial sum
$H_n$ has grown to $\approx16.7$ while individual terms are $\sim10^{-7}$; the rounding
error accumulated over $10^{7}$ additions is of order $n\varepsilon\,\bar{a}
\sim 10^{7}\times2.2\times10^{-16}\times 10^{-7}$ per step, i.e. in the last few digits
of the sum, which is entirely sufficient to corrupt an estimate of a $5\times10^{-8}$
residual. The lesson: **asymptotic constants should be extracted by subtracting
analytically, or by compensated summation, never by differencing large floating-point
partial sums.** The demonstration's forward-versus-backward difference of `4.374e-14`
in Section 8 is the measurement of exactly this sensitivity.

---

## ★★★7 — Designing an iteration

**(a)** Iterating $x_{n+1}=\cos x_n$ from $x_0=0.5$ converges to
$x^{*} = 0.7390851332151607$ (the "Dottie number"), and

$$r = \lvert g'(x^{*})\rvert = \lvert\sin x^{*}\rvert = 0.6736120 .$$

For an error below $10^{-10}$:

$$n = \frac{\ln 10^{-10}}{\ln 0.6736120} = \frac{-23.026}{-0.39506} = 58.3
\;\Longrightarrow\; \boxed{59}\ \text{iterations} .$$

**(b)** For $g(x) = 1 + \sin(x)/2$: solving $x = 1+\sin(x)/2$ gives
$x^{*} = 1.4987011335178484$, and

$$r = \lvert g'(x^{*})\rvert = \frac{\lvert\cos x^{*}\rvert}{2}
= \frac{0.0720328}{2} = 0.0360164 .$$

For $10^{-10}$ this needs

$$n = \frac{-23.026}{\ln 0.0360164} = \frac{-23.026}{-3.3236} = 6.93
\;\Longrightarrow\; \boxed{7}\ \text{iterations} .$$

A 50-fold reduction in the rate buys an eightfold reduction in iterations — and the
rate was predictable from a single derivative evaluation.

**(c)** Take $g_c(x) = x + c(\cos x - x)$. It has the same fixed point (the bracket
vanishes precisely when $x = \cos x$), and

$$g_c'(x^{*}) = 1 + c(-\sin x^{*} - 1) = 1 - c(1+0.6736120) = 1 - 1.6736120\,c .$$

For $g_c'(x^{*}) = 0.1$: $c = 0.9/1.6736120 = 0.5378$. (For $-0.1$,
$c = 1.1/1.6736120 = 0.6573$; the magnitude is what matters.)

Is it worth it? Seven iterations become
$n = \ln 10^{-10}/\ln 0.1 = 10$ iterations — **worse**, because $0.1$ is a larger rate
than $0.036$. The exercise is instructive rather than useful: accelerating an
iteration requires reducing $\lvert g'\rvert$, and the cheapest way to do that is
usually not to invent a new map but to use Newton's method, which forces
$g'(x^{*}) = 0$.

**(d)** Newton's method has $g'(x^{*}) = 0$, so the linear error law
$e_{n+1}\approx g'(x^{*})e_n$ is degenerate — it predicts an error of zero. The
governing term is then the quadratic one,
$e_{n+1} \approx \frac{f''(x^{*})}{2f'(x^{*})}e_n^{2}$, and there is no fixed ratio
$r$: the *effective* ratio $e_{n+1}/e_n \approx C e_n$ shrinks as the error shrinks.
That is what "quadratic convergence" means, and why the demonstration's column of
$e_n/e_{n-1}^{2}$ is constant (`0.353522`) while the naive ratio is not.

---

## ★★★8 — The accuracy limit of an asymptotic series

**(a)** Minimise $\ln\left(k!/x^{k}\right) = \ln k! - k\ln x$ over continuous $k$. Using
$\frac{d}{dk}\ln k! \approx \ln k$ (the digamma approximation, exact to leading order),

$$\ln k - \ln x = 0 \;\Longrightarrow\; k_{\min} \approx x .$$

So the terms stop shrinking at about $k = x$, as the demonstration shows for $x = 20$
(the best observed partial sum is at $k = 8$, with the smallest *term* near $k = 20$;
the partial sums improve until the term size begins to dominate the truncation).

**(b)** At $k = x$, Stirling gives

$$\left\lvert\frac{k!}{x^{k}}\right\rvert \approx \sqrt{2\pi x}\left(\frac{x}{e}\right)^{x}\frac{1}{x^{x}}
= \sqrt{2\pi x}\,e^{-x} .$$

The expansion is $E_1(x) \sim \dfrac{e^{-x}}{x}\sum(-1)^{k}\dfrac{k!}{x^{k}}$, and its
partial sums differ from $E_1$ by roughly the first omitted term times the prefactor:
an absolute error of order $\dfrac{e^{-x}}{x}\sqrt{2\pi x}\,e^{-x}$. Relative to
$E_1 \approx e^{-x}/x$, the *relative* accuracy limit is therefore

$$\text{best relative error} \approx \sqrt{2\pi x}\,e^{-x} .$$

**(c)** At $x = 20$:

$$\sqrt{2\pi\times20}\;e^{-20} = 11.21\times2.061\times10^{-9} = 2.31\times10^{-8} .$$

The demonstration's observed best relative error is `5.004e-07` at $k = 8$. The
estimate is about 20 times too optimistic, and the reasons are identifiable: Stirling's
approximation is only asymptotically exact, the minimising $k$ is an integer near but
not equal to $x$, and the error of a truncated *alternating* asymptotic series is
bounded by the smallest term rather than equal to it. Agreement to one order of
magnitude is the correct expectation for this style of estimate, and the *scaling* —
$\sqrt{x}\,e^{-x}$, i.e. exponential in $x$ — is what matters.

**(d)** A convergent series for a function of this kind would allow arbitrarily small
relative error with enough terms, and in operations with exact arithmetic that is a
strict advantage. In floating-point arithmetic it is not: the error floor is
$\varepsilon \approx 2.2\times10^{-16}$, and the asymptotic series at $x = 20$ reaches
$5\times10^{-7}$ with nine terms — no logarithm, no recursion in a special function
library, and no loss of accuracy from cancellation of exponentially small quantities.
For $x \gtrsim 5$ the asymptotic expansion is both cheaper and more accurate in
practice than any convergent route, which is why it is the implementation of choice in
special-function libraries. The same reasoning makes multipole expansions in
potential-field theory practical.

---

## Extension notes

- **Summation order.** Forwards and backwards sums of $\sum k^{-2}$ to $n = 10^{6}$
  differ by `4.374e-14`, and both are wrong by about `1e-06` from truncation. Kahan
  compensated summation removes the $10^{-14}$ effect entirely, after which the
  difference between the two orders is at the level of a single unit in the last place —
  showing that the truncation error, not the summation, was the dominant limitation all
  along.
- **$r = 0.999$.** Here $n = \ln 10^{-6}/\ln 0.999 = 13\,815$ terms for six digits,
  against 16 terms for $r = 0.4$. The series converges, and for any practical purpose it
  does not.
- **Rearrangement.** The alternating harmonic series can be reordered to converge to
  any prescribed real number: take positives until you exceed the target, then negatives
  until you fall below it, and repeat. Each term is used exactly once, and the partial
  sums oscillate with amplitudes that do not shrink, because the total positive and
  total negative contributions are separately divergent. The practical moral: **the
  summation order of a conditionally convergent series is part of the algorithm, not an
  implementation detail**, and a compiler that reorders a floating-point reduction is
  changing your answer.
