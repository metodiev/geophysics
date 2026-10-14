# Exercises — 01-05-06 Improper Integrals, Singularities and Convergence

Attempt these **closed-book** before opening the
[solutions](./06-improper-integrals-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Determine convergence or divergence, stating the test you used:

(a) $\displaystyle\int_1^{\infty}\frac{dx}{x^{3/2}}$
(b) $\displaystyle\int_1^{\infty}\frac{dx}{x+1}$
(c) $\displaystyle\int_0^{1}\frac{dx}{\sqrt x}$
(d) $\displaystyle\int_0^{1}\frac{dx}{x^{0.9}}$
(e) $\displaystyle\int_1^{\infty}\frac{e^{-x}}{x}\,dx$

---

**★2.** Evaluate exactly, or show divergence:

(a) $\displaystyle\int_1^{\infty}\frac{dx}{x^{2}}$
(b) $\displaystyle\int_0^{\infty}e^{-2x}\,dx$
(c) $\displaystyle\int_0^{1}\ln x\,dx$

---

## ★★ Applied

**★★3.** (a) Show that $\displaystyle\int_0^{\infty}\frac{dr}{(r^{2}+a^{2})^{3/2}} = \frac{1}{a^{2}}$
and name the substitution that makes it elementary.

(b) Interpret the integral as a component of the gravitational field of a
semi-infinite line mass $\lambda$ (mass per unit length) observed at perpendicular
distance $a$ from the end of the line. Write the field component in terms of $G$,
$\lambda$ and $a$.

(c) The potential of that same semi-infinite line is *not* finite. Explain the
distinction using the integrability criterion for a singularity.

---

**★★4.** A density model assigns a finite, positive density everywhere inside a body
of finite extent.

(a) State the criterion on the exponent $\alpha$ in $s^{-\alpha}$ that makes the
potential integral convergent in three dimensions, where $s$ is the distance from the
field point.
(b) Using the criterion, explain why an ordinary (bounded) density always gives a
finite potential.
(c) Explain, in one or two sentences, why a *point* mass is not representable as a
bounded density and what mathematical object would be required.
(d) State the corresponding criterion in two dimensions, and the resulting form of the
potential.

---

## ★★★ Research-oriented

**★★★5.** The Bouguer slab field was derived in the lesson as

$$g_z = \int_{-\infty}^{\infty}\frac{2G\sigma z}{x^{2}+z^{2}}\,dx = 2\pi G\sigma .$$

(a) Derive the partial integral out to $\pm L$ and show that the relative error of
the truncation is $1 - \frac{2}{\pi}\arctan(L/z)$.
(b) Show that the tail decays as $2z/(\pi L)$ and compute the half-length needed for a
relative error below $10^{-6}$ with $z = 1000$ m.
(c) Explain why the same integral with an *exponential* decay factor in the integrand
would converge far faster, and what that says about interpreting a "converged"
numerical integral in general.

---

**★★★6.** Consider $I = \displaystyle\int_1^{\infty}\frac{dx}{x^{1+\epsilon}}$ for
$0 < \epsilon \ll 1$.

(a) Evaluate the integral and show that it is finite for every $\epsilon > 0$ but that
it grows without bound as $\epsilon\to0^{+}$.
(b) Compute $I$ for $\epsilon = 0.1, 0.01, 0.001$ and state the pattern.
(c) The integral converges, yet it is not controllable: explain what "not uniformly
convergent as $\epsilon\to0$" means here, and give one physical situation in which the
same phenomenon appears (a model whose parameters can be moved so that a
"convergent" quantity becomes arbitrarily large without diverging).
(d) Truncate the integral at $L$ instead and show that the pair
$(\epsilon, L)$ is what determines the answer — the *ratio* is what matters. This is
the origin of the logarithmic dependence of two-dimensional potential problems on
the ratio of two length scales.

---

## Extension ideas

- Evaluate $\int_0^{\infty}x^{n}e^{-x}dx$ for $n = 0,1,2,3$ by parts and compare with
  $\Gamma(n+1) = n!$.
- Show that $\int_0^{\infty}\frac{dx}{1+x^{2}} = \frac{\pi}{2}$ and identify which
  potential-field geometry produces this integral.
- For a Gaussian integrand, compute the truncation length needed for a relative error
  below $10^{-6}$ and compare with the algebraic case in ★★★5(b). State the ratio of
  the two lengths, and use it to explain why the numerical treatment of power-law and
  exponential kernels is so different.
