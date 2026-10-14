# Exercises — 01-02-02 Functions, Graphs and Transformations

Attempt these **closed-book** before opening the
[solutions](./02-functions-and-graphs-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

State the domain before you evaluate anything.

---

## ★ Foundational

**★1.** Give the natural domain of each function, and one physical reason for
each restriction.

(a) $f(d) = \dfrac{GM}{d^{2}}$
(b) $f(D) = \ln\dfrac{D}{D_0}$
(c) $g = \sqrt{\dfrac{GM}{g}}$
(d) $f(x) = \dfrac{1}{1 + x^{2}}$

---

**★2.** Identify the family of each table (linear, quadratic or exponential),
write the formula, and give the rule you used.

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| A | 5 | 7 | 9 | 11 |

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| B | 3 | 6 | 12 | 24 |

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| C | 1 | 2 | 5 | 10 |

---

**★3.** Let $f(x) = \dfrac{1}{1+x^{2}}$, whose peak is at $x = 0$ with height 1.
State the position and height of the peak of:

(a) $f(x - 3)$
(b) $f(x) + 0.5$
(c) $f(2x)$
(d) $-f(x)$

Then say, for each, which survey operation it corresponds to (offset, baseline,
rescaling, polarity reversal).

---

**★4.** Classify each function as even, odd or neither:

(a) $x^{3}$  (b) $x^{2}$  (c) $x^{3} + x$  (d) $1 + x + x^{3}$  (e) $e^{x}$

Then split $f(x) = 2 + x + x^{2}$ into its even and odd parts.

---

## ★★ Applied

**★★5.** (a) Find the inverse of $t(d) = \dfrac{2d}{v}$ with $v > 0$, stating the
domain of the inverse.

(b) Find the inverse of the Newton-cooling law
$T(t) = T_\infty + (T_0 - T_\infty)e^{-t/\tau}$, i.e. solve for $t$, and state
the conditions.

(c) Evaluate (b) for $T_\infty = 10\,^\circ$C, $T_0 = 900\,^\circ$C,
$\tau = 4$ days, $T = 100\,^\circ$C.

(d) Explain why the inverse exists on $t \ge 0$ in physical terms.

---

**★★6.** Find all vertical and horizontal asymptotes.

(a) $\dfrac{3x^{2} + 2x}{x^{2} + 5}$

(b) $\dfrac{x + 1}{x^{2} - 4}$

(c) $\dfrac{z}{1 + z}$

(d) For (c), how large must $z$ be for the function to be within $10^{-4}$ of its
limit? Solve the inequality exactly rather than guessing.

---

**★★7.** For the linear geothermal profile $T(z) = 10 + 25z$ (with $z$ in km):

(a) Compute the average rate of change over $[0, 1]$, $[1, 2.5]$ and $[2.5, 5]$,
and comment.

(b) For $f(x) = x^{2}$, compute the average rate of change over $[1, 2]$,
$[1, 1.1]$ and $[1, 1.01]$.

(c) From (b), what value does the average rate of change appear to approach as
the interval shrinks, and what is that number called?

---

**★★8.** Let $f(x) = 2x$ and $g(x) = x + 1$.

(a) Compute $f(g(x))$ and $g(f(x))$ and evaluate both at $x = 3$.

(b) A velocity model is $v(z) = v_0 + kz$ and a depth–time relation is
$z(t) = z_0 + ut$. Write $v$ as a function of $t$ and say whether it is still
linear.

(c) Give a geophysical reason why the order of composition in (a) matters in a
processing chain.

---

## ★★★ Research-oriented

**★★★9.** The limit $\left(1 + 1/z\right)^{z} \to e$ is approached slowly.

(a) Compute $r(z) = e - \left(1+1/z\right)^{z}$ for
$z = 10, 10^{2}, \dots, 10^{6}$ and tabulate $r(z)$ and $z\,r(z)$.

(b) Does $z\,r(z)$ tend to a constant? If so, what is it, and what does that imply
about how $r$ depends on $z$?

(c) Relate your finding to the standard identity for the correction term of the
limit. (You may derive it from the expansion of $\ln(1 + 1/z)$, or state the
result from a reference and verify it numerically.)

(d) State the limits of your conclusion: over which range of $z$ was the fit made,
and what happens as $z$ becomes large enough that $(1+1/z)$ is no longer
distinguishable from 1 in binary64? (Find that $z$ empirically: it is of order
$1/u$.)

---

**★★★10.** The profile of a buried mass. Across a survey line, the vertical
attraction of a point mass at depth $h$ — and, by Newton's shell theorem, of a
uniform sphere whose centre is at depth $h$ — is

$$g(x) = \frac{GMh}{(x^{2} + h^{2})^{3/2}}.$$

(a) Show that $g(0) = GM/h^{2}$ and that $g(h)/g(0) = 1/(2\sqrt{2})$, quoting the
decimal value.

(b) Derive the **half-width at half maximum** $x_{1/2}$, i.e. the offset at which
$g = g(0)/2$. Show that

$$x_{1/2} = h\sqrt{2^{2/3} - 1},$$

and hence that $h = x_{1/2}/\sqrt{2^{2/3}-1} \approx 1.3048\,x_{1/2}$.

(c) Compute $g/g(0)$ at $x/h = 0,\ 0.5,\ 1,\ 2,\ 5,\ 10$ and report the values.

(d) Show that $\dfrac{g(x)\,x^{3}}{GMh} \to 1$ as $x \to \infty$, so the far-field
decay is $1/x^{3}$ rather than $1/x^{2}$. Report the value of that ratio at
$x/h = 5$ and $x/h = 10$, and say how far the far field extends before the
approximation is good to a few parts in a thousand.

(e) State what the half-width rule actually measures for a uniform sphere, and why
applying it to an anomaly produced by a very different geometry (for example an
infinite horizontal cylinder, whose anomaly varies as $1/(x^{2}+h^{2})$) gives a
biased depth. Quantify the bias for that example.

(f) Report the method, the numbers, the trend and the limits of your conclusion.

## Extension ideas

- Plot (by table, or with a plotting package) the difference between the exact
  far-field anomaly and the dipole-like next term, and find the distance at which
  the *second* correction becomes the dominant error.
- Take a real temperature log (or a synthetic one you construct) and identify the
  intervals where the profile is linear. Say what you would need to know to
  attribute the curvature to a physical cause rather than to noise.
- Construct a velocity model that is not monotonic with depth, and show that
  depth-as-a-function-of-time is then not single-valued. Explain what a processing
  code must do about it.
