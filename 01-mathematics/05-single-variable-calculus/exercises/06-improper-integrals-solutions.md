# Solutions — 01-05-06 Improper Integrals, Singularities and Convergence

> **Read this after attempting the exercises, not before.** Numerical values were
> computed; the convergence statements are derived.

---

## ★1 — Convergence verdicts

**(a) Converges.** $p = 3/2 > 1$, so the $p$-test applies:

$$\int_1^{\infty}x^{-3/2}dx = \left[-2x^{-1/2}\right]_1^{\infty} = 2 .$$

**(b) Diverges.** For $x \ge 1$, $\dfrac{1}{x+1} \ge \dfrac{1}{2x}$, and
$\int_1^{\infty}dx/(2x)$ diverges logarithmically. By the comparison test the
integral diverges like $\ln L$.

**(c) Converges.** $p = 1/2 < 1$ at the zero end:

$$\int_0^{1}x^{-1/2}dx = \left[2\sqrt x\right]_0^{1} = 2 .$$

**(d) Converges.** $p = 0.9 < 1$:

$$\int_0^{1}x^{-0.9}dx = \left[\frac{x^{0.1}}{0.1}\right]_0^{1} = 10 .$$

Note how *close* to divergence this is: $p = 0.9$ gives 10, and $p = 0.99$ gives 100.
The boundary case $p = 1$ diverges logarithmically, and the numbers just below it are
large but finite.

**(e) Converges.** $e^{-x}/x \le e^{-x}$ for $x \ge 1$, and
$\int_1^{\infty}e^{-x}dx = e^{-1}$ converges. The integral converges absolutely, and
comparison with $e^{-x}$ is the right comparison because the exponential dominates
the $1/x$ for large $x$.

---

## ★2 — Exact values

**(a)** $\displaystyle\int_1^{\infty}\frac{dx}{x^{2}}
= \left[-\frac{1}{x}\right]_1^{\infty} = 0 + 1 = \boxed{1}$.

**(b)** $\displaystyle\int_0^{\infty}e^{-2x}dx
= \left[-\frac{e^{-2x}}{2}\right]_0^{\infty} = \boxed{\tfrac12}$.

**(c)** By parts with $u = \ln x$, $dv = dx$:

$$\int\ln x\,dx = x\ln x - x,$$

so

$$\int_0^{1}\ln x\,dx = \left[x\ln x - x\right]_0^{1} = (0-1) - \lim_{x\to0^{+}}(x\ln x - x).$$

The limit is $0$, since $x\ln x\to0$ (l'Hôpital applied to $\ln x/(1/x)$). Hence

$$\int_0^{1}\ln x\,dx = \boxed{-1} .$$

The singularity is integrable, and the value is finite and negative — the integrand
is negative throughout.

---

## ★★3 — A field integral and its potential counterpart

**(a)** Substitute $r = a\tan\theta$, so $dr = a\sec^{2}\theta\,d\theta$ and
$(r^{2}+a^{2})^{3/2} = (a^{2}\sec^{2}\theta)^{3/2} = a^{3}\sec^{3}\theta$. Then

$$\frac{dr}{(r^{2}+a^{2})^{3/2}}
= \frac{a\sec^{2}\theta}{a^{3}\sec^{3}\theta}d\theta
= \frac{\cos\theta}{a^{2}}d\theta,$$

and the limits $r: 0\to\infty$ become $\theta: 0\to\pi/2$:

$$\int_0^{\infty}\frac{dr}{(r^{2}+a^{2})^{3/2}}
= \frac{1}{a^{2}}\left[\sin\theta\right]_0^{\pi/2} = \boxed{\frac{1}{a^{2}}} .$$

**(b)** A line element of mass $\lambda\,dx$ at along-line coordinate $x$ produces a
field of magnitude $G\lambda\,dx/s^{2}$ with $s = \sqrt{a^{2}+x^{2}}$, directed along
the line from the element to the observation point. Its perpendicular component is

$$dg_{\perp} = \frac{G\lambda\,dx}{s^{2}}\cdot\frac{a}{s}
= G\lambda a\,\frac{dx}{(a^{2}+x^{2})^{3/2}} .$$

Integrating over a semi-infinite line, $x: 0\to\infty$:

$$g_{\perp} = G\lambda a\int_0^{\infty}\frac{dx}{(a^{2}+x^{2})^{3/2}}
= G\lambda a\cdot\frac{1}{a^{2}} = \boxed{\frac{G\lambda}{a}} .$$

By the same integral with a factor $x$ instead of $a$, the component *parallel* to
the line is $\displaystyle G\lambda\int_0^{\infty}\frac{x\,dx}{(a^{2}+x^{2})^{3/2}}
= \frac{G\lambda}{a}$ as well. So the field of a semi-infinite line has two equal
components, hence magnitude $\sqrt2\,G\lambda/a$ directed at 45° to the line. Each
component is exactly half the corresponding component of the field of an *infinite*
line (whose perpendicular component is $2G\lambda/a$), which is what the symmetry of
the missing half demands.

**(c)** The **field** integral converges because its integrand decays as $x^{-2}$: the
geometrical factor $a/s$ supplies an extra power of $x$ relative to the naive
$1/x^{2}$ form. The **potential**, by contrast, involves $\int\ln s\,dx$ in two
dimensions, which grows without bound.

In terms of the integrability criterion: near the observation point the field
integrand behaves like $s^{-2}$ and the two-dimensional measure element contributes
$s^{1}$, giving $s^{-1}$, which is integrable in two dimensions ($\alpha < 2$). The
potential integrand behaves like $s^{-1}$ and the measure contributes $s^{1}$, giving
a finite local contribution — but the *far-field* contribution is what diverges,
because $\int^{L}dx/s$ for large $x$ behaves like $\ln L$. **A singularity and a
distant tail are different failure modes, and it is worth knowing which one you are
looking at.**

---

## ★★4 — When a density can represent a source

**(a)** A singularity $s^{-\alpha}$ is integrable in three dimensions if
$\alpha < 3$, because the volume element contributes $s^{2}$ and $s^{2-\alpha}$ is
integrable at $0$ exactly when $\alpha < 3$.

**(b)** An ordinary (bounded, measurable) density gives a bounded integrand near the
field point, so $\alpha = 0$ and the local integral converges trivially. The
far-field behaviour also converges because the body is of finite extent and the
integrand decays like $s^{-1}$ while the measure grows like $s^{2}$ — the mass
integral itself, $\int\rho\,dV$, is finite, which is what makes the potential finite.

**(c)** A point mass has all its mass at one point, so it cannot be described by a
bounded density: the required "density" would have to be a **Dirac delta
distribution**, $\rho = M\delta(\mathbf{x}-\mathbf{x}_0)$, an object defined by its
action under integration rather than by a value at each point. This is precisely why
the point-mass potential $-GM/r$ is singular at the source while every extended body's
potential is not.

**(d)** In two dimensions the measure contributes $s^{1}$, so the criterion is
$\alpha < 2$; and the far-field behaviour changes qualitatively. A two-dimensional
"point" source (a line in 3-D) has a potential proportional to $\ln r$, not $1/r$, and
therefore needs a reference length — the logarithmic divergence of Section 3.8 of the
lesson.

---

## ★★★5 — Truncating the Bouguer integral

**(a)** With the substitution $x = z\tan\phi$,

$$\int_{-L}^{L}\frac{2G\sigma z}{x^{2}+z^{2}}dx
= 2G\sigma z\cdot\frac{1}{z}\left[\arctan\frac{x}{z}\right]_{-L}^{L}
= 4G\sigma\arctan\frac{L}{z} .$$

The exact value is $2\pi G\sigma$, so the fractional shortfall is

$$\frac{2\pi G\sigma - 4G\sigma\arctan(L/z)}{2\pi G\sigma}
= 1 - \frac{2}{\pi}\arctan\frac{L}{z} . \;\checkmark$$

**(b)** For $L \gg z$, use
$\arctan y = \dfrac{\pi}{2} - \dfrac{1}{y} + O(y^{-3})$:

$$1 - \frac{2}{\pi}\left(\frac{\pi}{2} - \frac{z}{L}\right)
= \frac{2z}{\pi L} + O\!\left(\frac{z^{3}}{L^{3}}\right) .$$

Setting $2z/(\pi L) = 10^{-6}$ with $z = 1000$ m:

$$L = \frac{2\times1000}{\pi\times10^{-6}} = 6.37\times10^{8}\ \mathrm{m},$$

i.e. 637 000 km — more than 1.5 times the Earth–Moon distance, for a slab whose
influence you might naively have thought was local. The lesson's script shows the
same slow convergence directly: relative errors of `-6.345e-02` at $L = 10^{4}$ m,
`-6.366e-03` at $10^{5}$ m and `-6.366e-04` at $10^{6}$ m — one digit per decade of
$L$.

**(c)** With an exponential factor, say $\int_{-\infty}^{\infty}e^{-|x|/b}\cos(\omega x)dx$,
the integrand decays exponentially and the tail beyond $L$ is bounded by a constant
times $e^{-L/b}$: reaching $10^{-6}$ needs $L \approx 14b$, not $3\times10^{5}z$.
Algebraic decay costs a factor of $10^{4}$–$10^{5}$ in the truncation length compared
with exponential decay.

The general lesson: **when a numerical integral is reported as "converged", the
question to ask is whether the tail is exponential or algebraic.** If it is algebraic,
doubling the domain buys one more digit of accuracy, and the reported convergence may
simply reflect a grid that was fine enough to *look* flat. This is the numerical
version of the point made in Section 3.8 of the lesson about logarithmic divergence:
power-law behaviour is where numerical intuition fails.

---

## ★★★6 — A convergent integral that is not controllable

**(a)**

$$I(\epsilon) = \int_1^{\infty}x^{-1-\epsilon}dx
= \left[\frac{x^{-\epsilon}}{-\epsilon}\right]_1^{\infty}
= \frac{1}{\epsilon} .$$

This is finite for every $\epsilon > 0$, but $I \to \infty$ as $\epsilon\to0^{+}$.

**(b)**

| $\epsilon$ | $I = 1/\epsilon$ |
|---|---|
| 0.1 | 10 |
| 0.01 | 100 |
| 0.001 | 1000 |

The pattern is exactly $1/\epsilon$: each factor of ten in $\epsilon$ multiplies the
integral by ten. The value is not merely unbounded as $\epsilon\to0$, it is
unbounded *predictably*, and there is no threshold below which the integral becomes
"large but safe".

**(c)** "Not uniformly convergent as $\epsilon\to0$" means that the convergence is
not controlled by a single bound that holds for all sufficiently small $\epsilon$: for
any target $M$ there is an $\epsilon$ small enough that $I(\epsilon) > M$. The integral
converges for each $\epsilon$ and the family does not converge.

A physical instance: the resistance of a layered medium, or the potential of a
two-dimensional body, where a parameter can be tuned so that a quantity that is
formally finite becomes arbitrarily large. In potential-field work the arrangement is
standard — an almost-perfectly balanced positive and negative source pair produces a
"finite" field whose magnitude depends on the imbalance, and small changes in the
imbalance make the field arbitrarily large. **Finite is not the same as bounded
across parameter values.**

**(d)** Truncate at $L$:

$$\int_1^{L}x^{-1-\epsilon}dx = \frac{1 - L^{-\epsilon}}{\epsilon}
= \frac{1}{\epsilon}\left(1 - e^{-\epsilon\ln L}\right).$$

For $\epsilon\ln L \ll 1$ this is $\approx \ln L$; for $\epsilon\ln L \gg 1$ it is
$\approx 1/\epsilon$. So the value depends on $\epsilon$ and $L$ only through the
combination $\epsilon\ln L$: **the *ratio* $L^{1}$ to $L^{\epsilon}$ is what matters**,
and only a logarithmic function of the two scales appears.

This is precisely the origin of the logarithmic dependence of two-dimensional
potential problems on the ratio of two length scales — the appearance of
$\ln(r/r_0)$ in the line-mass potential, and of $\ln(H/a)$ or $\ln(R/r)$ in problems
with two separated scales. The logarithm is not an inelegant detail; it is the
signature of a marginal convergence, and it always means that the answer depends on
the logarithm of a ratio you must state explicitly.

---

## Extension notes

- **Gamma integrals.** $\int_0^{\infty}x^{n}e^{-x}dx = n!$ by repeated integration by
  parts; the values are $1, 1, 2, 6$ for $n = 0,1,2,3$. The $n = 1$ case is the
  integral used in the lesson's Section 3.6.
- **A classic improper integral.** $\int_0^{\infty}\frac{dx}{1+x^{2}} = \frac{\pi}{2}$.
  The same integrand appears in the field of an infinite slab (Section 3.3 of the
  lesson) and in the arctan solution of the Laplace equation in a half-space, which is
  why the arctangent is so common in potential-field formulas.
- **Gaussian versus algebraic.** For $\int_L^{\infty}e^{-x^{2}}dx$ the tail bound
  $e^{-L^{2}}/(2L)$ reaches $10^{-6}$ at $L \approx 3.5$; for
  $\int_L^{\infty}x^{-2}dx = 1/L$ the same accuracy needs $L = 10^{6}$. The ratio is
  more than five orders of magnitude, and it is the single most important practical
  fact about numerical integration in geophysics.
