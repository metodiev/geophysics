# Exercises — 01-05-07 Sequences, Series and Convergence Tests

Attempt these **closed-book** before opening the
[solutions](./07-sequences-and-series-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** State whether each series converges or diverges, and name the test you used:

(a) $\displaystyle\sum_{n\ge1}\frac{1}{n^{2}+1}$
(b) $\displaystyle\sum_{n\ge1}\frac{n}{n+1}$
(c) $\displaystyle\sum_{n\ge1}\frac{2^{n}}{n!}$
(d) $\displaystyle\sum_{n\ge2}\frac{1}{n\ln n}$
(e) $\displaystyle\sum_{n\ge1}(-1)^{n}\frac{1}{\sqrt n}$

---

**★2.** Find the radius of convergence, and decide convergence at each endpoint where
you can:

(a) $\displaystyle\sum_{n\ge1}\frac{x^{n}}{n}$
(b) $\displaystyle\sum_{n\ge1}\frac{n!}{n^{n}}x^{n}$
(c) $\displaystyle\sum_{n\ge1}\frac{n^{2}}{2^{n}}x^{n}$

---

**★3.** State the geometric-series remainder formula and use it to bound the error of
truncating $\sum(0.4)^{k}$ after 8 terms. Then find the smallest number of terms
guaranteeing an error below $10^{-6}$.

---

## ★★ Applied

**★★4.** A solver's error decays geometrically with ratio $r = 0.92$ per iteration.

(a) How many iterations are needed to reduce the error by $10^{-6}$? Derive from
$r^{n} = 10^{-6}$ rather than by trial.
(b) How many for $10^{-12}$?
(c) Compare with $r = 0.5$ for the same two tolerances.
(d) State the practical consequence for solver design in one sentence, and explain
what quantity in a linear-algebra setting plays the role of $r$
(see [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../07-linear-algebra/06-eigenvalues.md)).

---

**★★5.** The alternating series $\sum_{k\ge1}(-1)^{k+1}/k$ converges to $\ln 2$.

(a) State the alternating-series error bound after $n$ terms.
(b) Compute the partial sum for $n = 1000$ and compare the true error with the bound.
(c) Using the integral representation of the remainder,
$R_n = \int_0^{1}\frac{x^{n}}{1+x}dx$, explain why the true error is close to *half*
the bound.
(d) How many terms would you need for an error below $10^{-8}$? State the answer both
from the bound and from the sharper estimate.

---

## ★★★ Research-oriented

**★★★6.** The harmonic numbers satisfy
$H_n = \ln n + \gamma + \frac{C}{n} + \frac{D}{n^{2}} + O(n^{-3})$.

(a) Compute $H_n - \ln n - \gamma$ for $n = 10^{3}, 10^{4}, 10^{5}, 10^{6}$ and tabulate
$n(H_n - \ln n - \gamma)$ and $n^{2}(H_n - \ln n - \gamma)$.
(b) From the two columns, estimate $C$ and $D$. Compare with the known series
$H_n \sim \ln n + \gamma + \frac{1}{2n} - \frac{1}{12n^{2}} + \frac{1}{120n^{4}} - \cdots$
and state your agreement.
(c) The demonstration reports that at $n = 10^{7}$ the extracted value drifts. Explain
why, and state what that implies about using floating-point partial sums to estimate
asymptotic constants.

---

**★★★7.** The convergence rate of a fixed-point iteration $x_{n+1} = g(x_n)$ is
$r = \lvert g'(x^{*})\rvert$ at the fixed point.

(a) For $x = \cos x$, verify that $x^{*} \approx 0.739085$ and $r \approx 0.6736$,
and compute the number of iterations needed for an error below $10^{-10}$ from
$x_0 = 0.5$.
(b) For $x = 1 + \sin(x)/2$, find $x^{*}$, compute $r$, and repeat the estimate.
(c) Design a map $g$ with $\lvert g'(x^{*})\rvert = 0.1$ solving the same equation
$x = \cos x$ — for instance $g(x) = x + c(\cos x - x)$ — find the value of $c$ that
gives that rate, and state whether the extra derivative evaluations are worth it.
(d) Explain, in terms of the error law, why Newton's method has no fixed rate $r$ at
all.

---

**★★★8.** The asymptotic series $E_1(x) \sim \frac{e^{-x}}{x}\sum_{k\ge0}(-1)^{k}k!/x^{k}$
diverges for every $x$.

(a) Find the term index $k$ at which $\lvert k!/x^{k}\rvert$ is smallest, as a
function of $x$, by minimising $\ln(k!/x^{k})$ over $k$ treated as continuous.
(b) Use Stirling's approximation $k! \approx \sqrt{2\pi k}\,(k/e)^{k}$ to show that
the smallest term is of order $\sqrt{2\pi x}\,e^{-x}$ in the sum
$\sum(-1)^{k}k!/x^{k}$, and hence that the best achievable *relative* accuracy of the
truncated expansion is of order $\sqrt{2\pi x}\,e^{-x}$.
(c) Evaluate your estimate for $x = 20$ and compare with the demonstration's observed
best relative error of `5.004e-07` at $k = 8$. State whether the agreement is
satisfactory and what accounts for any residual factor.
(d) State, in two sentences, how this accuracy limit compares with a *convergent*
series for the same function, and why the asymptotic series is nevertheless the
practical tool.

---

## Extension ideas

- Write a program that sums $\sum k^{-2}$ forwards and backwards for $n = 10^{6}$ and
  reports both results and the difference. Then repeat with Kahan compensated
  summation and state what the compensated result tells you about which order was
  closer to the truth.
- For the geometric series with $r = 0.999$, compute the number of terms needed for
  six-digit accuracy and explain, in one sentence, why the series is useless for that
  purpose in practice even though it converges.
- Show that a conditionally convergent series can be rearranged to converge to any
  prescribed value, and state the implication for a numerical summation whose order is
  determined by a compiler rather than by the author.
