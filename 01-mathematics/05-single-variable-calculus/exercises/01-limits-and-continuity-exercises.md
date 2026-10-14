# Exercises — 01-05-01 Limits, Continuity and the Idea of Approximation

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-limits-and-continuity-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Evaluate, showing each step and naming the technique:

(a) $\displaystyle\lim_{x\to3}\frac{x^{2}-9}{x-3}$

(b) $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^{2}}$

(c) $\displaystyle\lim_{x\to\infty}\frac{4x^{3}-2}{x^{3}+7}$

(d) $\displaystyle\lim_{x\to0}\frac{\sin(5x)}{x}$

---

**★2.** For $f(z) = \lvert z - 33 \rvert$ (with $z$ in km):

(a) Compute $\lim_{z\to33^{-}}f(z)$ and $\lim_{z\to33^{+}}f(z)$.
(b) Compute $f'_{-}(33)$ and $f'_{+}(33)$ from the definition.
(c) Does $f'(33)$ exist? Justify your answer.
(d) Which geological feature does a kink of this kind represent, and how does it
differ from a jump?

---

**★3.** Classify each discontinuity as removable, jump or infinite, and give a
geophysical example of each:

(a) $f(z) = \dfrac{z^{2}-4}{z-2}$ at $z = 2$.
(b) $g(z) = \rho_1$ for $z < 2$ km and $\rho_2$ for $z > 2$ km at $z = 2$ km.
(c) $h(r) = -GM/r$ at $r = 0$.

---

## ★★ Applied

**★★4.** A thin uniform disc of mass $M$ and radius $a$ has, on its axis,

$$V(z) = \frac{2GM}{\sqrt{a^{2}+z^{2}}+z}.$$

(a) Show that this is the limit of the standard form
$\frac{2GM}{a^{2}}\left(\sqrt{a^{2}+z^{2}}-z\right)$.
(b) Expand in $u = a/z$ to first order and obtain the fractional correction to the
point-mass potential $GM/z$.
(c) How far away, in units of $a$, must an observation be for the point-mass
approximation to be accurate to 1 part in $10^{4}$? Work from the expansion, then
check the prediction against the table in the lesson.

---

**★★5.** A velocity model is defined by

$$v(z) = \begin{cases} 6.0\ \mathrm{km\,s^{-1}} & z < 33\ \mathrm{km}\\
8.0\ \mathrm{km\,s^{-1}} & z > 33\ \mathrm{km}\end{cases}$$

and a smoothed version is $v_{\epsilon}(z) = 6.0 + 2.0\,\sigma\!\left(\dfrac{z-33}{\epsilon}\right)$
with $\sigma(t) = 1/(1+e^{-t})$.

(a) Compute $\lim_{z\to33}v_{\epsilon}(z)$ for $\epsilon = 0.1$ km.
(b) Compute $\lim_{\epsilon\to0^{+}}v_{\epsilon}(33)$ and compare with the jump
model.
(c) In one or two sentences, state what the limit $\epsilon\to0$ says about
whether a jump discontinuity is a property of the Earth or of the model.

---

**★★6.** A body of mass $10^{9}$ kg is buried at depth $d$. Using
$g_z = GM/d^{2}$ with $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
find the depth at which the anomaly is $10^{-3}$ mGal, and express your answer to
the number of significant figures the inputs justify.

---

## ★★★ Research-oriented

**★★★7.** The demonstration probes $\sin(x)/x$ numerically and reports that the
computed ratio becomes exactly `1.0` at $x = 10^{-8}$.

(a) Derive the threshold $x^{*} = \sqrt{6\varepsilon}$ from the floating-point
model, with $\varepsilon \approx 2.22\times10^{-16}$, and evaluate it.
(b) Predict the corresponding threshold for $\tan(x)/x$, given
$\tan x = x + x^{3}/3 + \cdots$.
(c) Predict the behaviour of $(e^{x}-1)/x$ for small $x$, given that $e^{x}-1$ is
computed by subtraction. State whether its floor is governed by a *truncation*
threshold (as for $\sin$) or by *cancellation*, and give the scaling of the error
in $x$.
(d) Run all three predictions and report the observed thresholds. Where your
prediction and the observation disagree, explain why.

---

**★★★8.** The far-field limit of any compact body is that of a point mass. Write a
short report (one page) answering: *why does this make the depth and the shape of a
gravity anomaly inseparable in the far field, and what data would break the
degeneracy?* Use the $u^{2}/4$ correction of ★4 as your quantitative anchor, and
state clearly which parts of your argument are mathematics and which are
assumptions about the Earth.

---

## Extension ideas

- Rewrite the disc-potential expression as a function that takes $M$, $a$, $z$ and
  returns the *fractional* error of the point-mass approximation, then verify that
  your function reproduces the lesson's table at $z = 10^{3}, 10^{4}, 10^{5},
  10^{6}, 10^{7}$ m for $a = 1000$ m.
- Repeat ★1(d) with $\tan(5x)/x$ and $\log(1+5x)/x$, and state a general rule for
  $\lim_{x\to0}f(ax)/x$ when $f(0) = 0$ and $f'(0) = 1$.
- Estimate the minimum $n$ for which $(1+1/n)^{n}$ agrees with $e$ to six decimal
  places using the asymptotic error $1/(2n)$, then test the prediction with the
  demonstration.
