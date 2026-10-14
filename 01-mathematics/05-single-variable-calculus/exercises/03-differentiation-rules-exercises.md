# Exercises — 01-05-03 Differentiation Rules and Implicit Differentiation

Attempt these **closed-book** before opening the
[solutions](./03-differentiation-rules-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Differentiate, naming the rule used at each step:

(a) $f(x) = (3x^{2}+1)(x-4)$
(b) $g(z) = \dfrac{z^{2}}{z+1}$
(c) $h(t) = \sin(t^{2})$
(d) $q(x) = \ln(5x^{3})$

---

**★2.** Verify the product rule for $f(x) = x^{2}\sin x$ at $x = 1$ by comparing
the analytic derivative with a central difference of step $h = 10^{-5}$. State the
relative difference you obtain and say whether it is consistent with the truncation
error of the central difference.

---

## ★★ Applied

**★★3.** A rock-physics relation for a porous rock is

$$v(\phi) = \frac{v_0}{1 + \alpha\phi},$$

with porosity $\phi$, matrix velocity $v_0$ and a positive coefficient $\alpha$.

(a) Compute $dv/d\phi$ by the chain rule.
(b) Compute the elasticity $\dfrac{dv/v}{d\phi/\phi}$ and evaluate it for
$\phi = 0.2$, $\alpha = 2.5$.
(c) Is the elasticity constant? Explain what your answer implies about
extrapolating the relation to $\phi = 0.5$.
(d) Show that $v$ remains finite at every $\phi \ge 0$ but that $v(\phi)$ is *not* a
power law. Why does this matter for the argument in the lesson's Section 3.6?

---

**★★4.** A temperature field near a periodic topography is modelled as

$$T(x,z) = T_0 + \gamma z - A\cos(kx)\,e^{-kz}.$$

The isotherm $T = T_1$ is defined implicitly.

(a) Calculate $dz/dx$ on that isotherm without solving for $z$.
(b) Evaluate the limit of $dz/dx$ as $z\to\infty$ and interpret it physically.
(c) State the point at which $dz/dx$ fails to exist in terms of the constants, and
explain what it means.

---

## ★★★ Research-oriented

**★★★5.** The lesson derived the ray parameter identity $p = dt/dx = \sin\theta/v$
for a single layer. Extend it to two layers, with the reflection coming from the
base of the second layer.

Let $h_1, v_1$ be the thickness and speed of the first layer and $h_2, v_2$ of the
second, and let $x$ be the total source–receiver offset.

(a) Write the total travel time $t(x)$ as the sum of the two straight-segment times,
with the ray angles $\theta_1$ and $\theta_2$ as intermediate variables.
(b) Differentiate $t$ with respect to $x$, treating $\theta_1$ and $\theta_2$ as
functions of $x$, and eliminate the derivatives using the geometry
$x = 2h_1\tan\theta_1 + 2h_2\tan\theta_2$.
(c) Show that $dt/dx = \sin\theta_1/v_1 = \sin\theta_2/v_2$, i.e. that $p$ is
constant along the ray. This is Snell's law, obtained by differentiation rather than
assumed.
(d) State the essential assumption about the velocity structure that makes the
straight-segment geometry valid, and what changes if the velocity varies
continuously with depth.

---

## Extension ideas

- Use logarithmic differentiation to differentiate $y = z^{z}$ and
  $y = \dfrac{(z+1)^{3}}{\sqrt{z^{2}+1}}$.
- Differentiate $V(z) = GM/(R+z)^{2}$ twice by the product/chain rules and confirm
  the second derivative $6GM/(R+z)^{4}$ quoted in the previous lesson.
- Show that the implicit formula $dz/dx = -F_x/F_z$ applied to $F = x^{2}+z^{2}-r^{2}$
  reproduces the slope of a circle, and explain why the formula fails at the
  leftmost and rightmost points of the circle.
