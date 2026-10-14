# Exercises — 01-11-03 Contour Integration, Residues and Real Integrals

Attempt these **closed-book**, then open the
[solutions](./03-contour-integration-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

For every real integral you evaluate by residues, state: the contour, the poles
inside it, and the argument that the arc contributes nothing.

---

## ★ Foundational

**★1.** Evaluate $\displaystyle\int_{-\infty}^{\infty}
\frac{\mathrm{d}x}{x^{2}+2x+10}$ by residues. Complete the square first.

---

**★2.** Evaluate $\displaystyle\int_{-\infty}^{\infty}
\frac{\mathrm{d}x}{(x^{2}+1)(x^{2}+4)}$ in two ways: by partial fractions in the
real domain, and by residues. Confirm that the two agree.

---

**★3.** Compute the residue at each stated pole.

(a) $\dfrac{e^{z}}{z^{2}+1}$ at $z = i$
(b) $\dfrac{z^{2}}{(z-1)^{3}}$ at $z = 1$
(c) $\dfrac{1}{z\sin z}$ at $z = 0$
(d) $\dfrac{\cos z}{z^{4}}$ at $z = 0$

---

**★4.** Evaluate $\displaystyle\oint_{|z| = 3}\frac{e^{z}}{z-2}\,\mathrm{d}z$
and $\displaystyle\oint_{|z-2| = 1}\frac{\cos z}{z^{2}+1}\,\mathrm{d}z$.

---

## ★★ Applied

**★★5.** Evaluate $\displaystyle\int_{0}^{\infty}
\frac{\mathrm{d}x}{x^{4}+1}$ by residues, and say why the answer is half the
whole-line integral rather than something more complicated.

---

**★★6.** Evaluate $\displaystyle\int_{-\infty}^{\infty}
\frac{\cos 2x}{x^{2}+1}\,\mathrm{d}x$ by residues, stating which half plane you
close in and why.

---

**★★7.** The **indentation lemma** for a simple pole on the contour: let $f$ have
a simple pole at $x_{0}$ on the real axis with residue $r$, and let $\gamma$ be a
small semicircle of radius $\epsilon$ centred at $x_{0}$.

(a) Show that $\int_{\gamma}f\,\mathrm{d}z \to \pm i\pi r$ as
$\epsilon\to0$, and identify which sign belongs to a semicircle in the upper half
plane traversed from left to right.
(b) Use the result to evaluate
$\mathrm{P.V.}\int_{-\infty}^{\infty}\dfrac{e^{ix}}{x-a}\,\mathrm{d}x$ for
$a$ real.
(c) Explain why the same integral without the $e^{ix}$ is divergent rather than
a principal value, and what the indentation lemma would return if applied to it
anyway.

---

**★★8.** Sum the series
$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{2}+1}$ by residues, using the known
identity $\sum_{n=-\infty}^{\infty}1/(n^{2}+a^{2}) = (\pi/a)\coth(\pi a)$, and
verify the result against a partial sum with its tail correction.

---

## ★★★ Research-oriented

**★★★9.** The Debye response $H(\omega) = 1/(1+i\omega\tau)$ has
$\operatorname{Im}H(\omega) = -\omega\tau/(1+\omega^{2}\tau^{2})$.

(a) Evaluate $\mathrm{P.V.}\int_{0}^{\infty}
\omega'\operatorname{Im}H(\omega')/(\omega'^{2}-\omega^{2})\,\mathrm{d}\omega'$
in closed form by partial fractions, and hence recover $\operatorname{Re}H$ from
the Kramers-Kronig relation of
[lesson 06](../06-dispersion-relations.md) Section 3.1.
(b) State which part of the partial-fraction expansion vanishes because the
principal value is taken, and why the remaining integral is elementary.
(c) Give the value of $\operatorname{Re}H$ at $\omega\tau = 1$ from your formula
and compare with the exact $1/2$. Explain what this check does and does not
establish.

---

**★★★10.** Invert $Y(s) = \dfrac{s+3}{(s+1)(s+2)}$ by residues of $Y(s)e^{st}$.

(a) Find the partial-fraction expansion and the pole positions.
(b) Write $y(t)$ explicitly.
(c) Check the result with the initial- and final-value theorems.
(d) A numerical Bromwich integral with $c = 0$ (rather than $c > 0$) is run
instead. Explain what goes wrong and what the numerical answer would look like.

---

## Self-assessment before the solutions

- [ ] I stated the degree condition for the arc in every rational integral.
- [ ] I chose the closing half plane from the sign of $\omega$ in ★★6, and said so.
- [ ] I got the direction of the indentation right in ★★7(a) by drawing it.
- [ ] I identified which term the principal value kills in ★★★9(a).
