# Solutions — 01-05-03 Differentiation Rules and Implicit Differentiation

> **Read this after attempting the exercises, not before.** Every numerical value
> below was computed, and the derivations are complete rather than sketched.

---

## ★1 — Rules

**(a)** Product rule with $f = 3x^{2}+1$, $g = x-4$:

$$f' = 6x(x-4) + (3x^{2}+1)(1) = 6x^{2}-24x+3x^{2}+1 = \boxed{9x^{2}-24x+1}.$$

Check at $x=1$: $9-24+1 = -14$.

**(b)** Quotient rule:

$$g'(z) = \frac{(2z)(z+1) - z^{2}(1)}{(z+1)^{2}} = \boxed{\frac{z^{2}+2z}{(z+1)^{2}}}.$$

**(c)** Chain rule with inner function $u = t^{2}$:

$$h'(t) = \cos(t^{2})\cdot 2t = \boxed{2t\cos(t^{2})}.$$

**(d)** First simplify: $\ln(5x^{3}) = \ln 5 + 3\ln x$, so

$$q'(x) = \boxed{\frac{3}{x}} .$$

The alternative route — $q' = \dfrac{15x^{2}}{5x^{3}} = \dfrac{3}{x}$ — gives the
same result. Simplifying first is almost always cheaper, and it is a good check.

---

## ★2 — Verifying the product rule numerically

Analytically,

$$f'(x) = 2x\sin x + x^{2}\cos x
\;\Longrightarrow\;
f'(1) = 2\sin 1 + \cos 1 = 2.2232442754839328 .$$

Numerically, with $h = 10^{-5}$,

$$\frac{f(1+h)-f(1-h)}{2h} = 2.223244275445513 .$$

Relative difference:

$$\frac{\lvert 2.2232442754839328 - 2.223244275445513\rvert}{2.2232442754839328}
= 1.7\times10^{-11} .$$

Is that consistent? The central-difference truncation error is
$\frac{h^{2}}{6}f'''(\xi) = \frac{10^{-10}}{6}f'''(\xi)$. With
$f''' = -6\sin x - 6x\cos x + x^{2}\sin x$ at $x\approx1$, $\lvert f'''\rvert \approx 7.5$,
the predicted absolute error is about $1.3\times10^{-10}$, i.e. a relative error
$\approx 5.7\times10^{-11}$. The observed $1.7\times10^{-11}$ is the same order.
Round-off in the two function values ($\sim10^{-16}$ each, divided by $2h=2\times10^{-5}$)
contributes $\sim10^{-11}$ as well, at the same scale. **The agreement is therefore
consistent with theory, and the exercise also shows that at $h = 10^{-5}$ you cannot
separate truncation from round-off** — a smaller $h$ would increase the round-off
contribution faster than it reduces the truncation.

---

## ★★3 — A porosity–velocity relation

**(a)** Write $v = v_0(1+\alpha\phi)^{-1}$ and use the chain rule with
$u = 1+\alpha\phi$:

$$\frac{dv}{d\phi} = -v_0(1+\alpha\phi)^{-2}\cdot\alpha
= \boxed{-\frac{\alpha v_0}{(1+\alpha\phi)^{2}}} .$$

**(b)** The elasticity is

$$\frac{dv/v}{d\phi/\phi} = \frac{\phi}{v}\frac{dv}{d\phi}
= \phi\,(1+\alpha\phi)\cdot\left(-\frac{\alpha}{(1+\alpha\phi)^{2}}\right)
= \boxed{-\frac{\alpha\phi}{1+\alpha\phi}} .$$

At $\phi = 0.2$, $\alpha = 2.5$: $-\dfrac{0.5}{1.5} = \boxed{-0.3333}$. A 1 %
increase in porosity lowers the velocity by 0.33 %.

**(c)** No. The elasticity ranges from 0 at $\phi = 0$ to $-1$ as
$\phi \to \infty$ (it is bounded below by $-1$). At $\phi = 0.5$ it is
$-1.25/2.25 = -0.556$, nearly double the value at $\phi = 0.2$. So **the response
strengthens with porosity, and extrapolating a single measured elasticity from
$\phi = 0.2$ to $\phi = 0.5$ understates the velocity change by a factor of about
1.7.** This is the practical failure mode of a power-law mindset: a power law would
have a constant elasticity, and this relation does not.

**(d)** $v$ is finite for every finite $\phi \ge 0$ because the denominator never
vanishes for positive $\alpha$; for large $\phi$ it decays like
$v \sim v_0/(\alpha\phi)$. It is **not** a power law: $v_0(1+\alpha\phi)^{-1}$ cannot
be written as $a\phi^{b}$ for constants $a$ and $b$, because its log–log slope varies
with $\phi$.

Contrast this with the lesson's Section 3.6, where $\rho = av^{b}$ has the *constant*
elasticity $b$. The distinction is practical, not pedantic: a power law fitted over
one porosity range predicts the same fractional response at every porosity, whereas
this relation predicts a response that grows in magnitude from 0 at $\phi = 0$ to
almost $-1$ at large $\phi$. Deciding which functional form your measurements
support is a modelling decision, and the elasticity is the diagnostic that exposes
the difference.

---

## ★★4 — Implicit differentiation of an isotherm

**(a)** Define $F(x,z) = T_0 + \gamma z - A\cos(kx)e^{-kz} - T_1$. Then

$$F_x = A k\sin(kx)\,e^{-kz}, \qquad
F_z = \gamma + A k\cos(kx)\,e^{-kz},$$

and therefore

$$\frac{dz}{dx} = -\frac{F_x}{F_z}
= \boxed{-\frac{A k\sin(kx)\,e^{-kz}}{\gamma + A k\cos(kx)\,e^{-kz}}}.$$

Note that solving for $z(x)$ in closed form is impossible: the isotherm mixes $z$
linearly inside an exponential.

**(b)** As $z\to\infty$, $e^{-kz}\to0$, so $\dfrac{dz}{dx}\to0$: the isotherm becomes
horizontal. Physically, the surface temperature perturbation is damped out with
depth on a scale $1/k$ (the same $e^{-kz}$ decay that appears in every
half-space solution), so far below the topography the isotherm is flat and the
lateral temperature gradient vanishes.

**(c)** The formula fails when $F_z = 0$:

$$\gamma + Ak\cos(kx)e^{-kz} = 0
\;\Longrightarrow\;
e^{-kz} = -\frac{\gamma}{Ak\cos(kx)},$$

which requires the right-hand side to be positive and at most 1. When that happens,
the isotherm has a vertical tangent at a single depth: the isotherm *overturns*, and
the temperature at that point is not a single-valued function of $x$ near it. In
terms of the lesson's warning, $F_z = 0$ is the signal that the implicit formula has
stopped describing a curve that can be parametrised by $x$.

---

## ★★★5 — Snell's law from the two-layer travel-time curve

**(a)** Write the travel time as the sum of two straight segments, each traversed
twice (down and up):

$$t = \frac{2h_1}{v_1\cos\theta_1} + \frac{2h_2}{v_2\cos\theta_2},$$

with the geometry constraint

$$x = 2h_1\tan\theta_1 + 2h_2\tan\theta_2 .$$

**(b)** The ray actually observed is the one for which the travel time is stationary
subject to the fixed geometry — Fermat's principle. Impose the constraint with a
Lagrange multiplier $\lambda$ and require stationarity in $\theta_1$ and $\theta_2$
at fixed source–receiver offset:

$$\frac{\partial}{\partial\theta_i}\Bigl[t - \lambda\bigl(x(\theta_1,\theta_2) - x_{\text{target}}\bigr)\Bigr] = 0 .$$

For $i = 1$, with $t$ and $x$ as in (a):

$$\frac{2h_1\sin\theta_1}{v_1\cos^{2}\theta_1} = \lambda\,\frac{2h_1}{\cos^{2}\theta_1}
\;\Longrightarrow\;
\frac{\sin\theta_1}{v_1} = \lambda,$$

and identically $\sin\theta_2/v_2 = \lambda$. The multiplier is therefore the same
for both layers.

**(c)** Hence

$$\boxed{\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2} = p}$$

with $p = \lambda$ constant along the ray: **this is Snell's law, derived rather than
assumed.** Finally, the envelope theorem for a constrained stationary value states
that $dt/dx = \lambda$ — the rate at which the optimal travel time grows as the
offset is increased is precisely the multiplier — so

$$\boxed{p = \frac{dt}{dx}} .$$

That is the identity used throughout the lesson: the slope of the travel-time curve
is the ray parameter, and it is the same number in every layer.

**(d)** The essential assumption is that each layer is **homogeneous**, so that the
ray is a straight line within it and the angles are constant along each segment.
If the velocity varies continuously with depth, $v = v(z)$, there is no single
$\theta$; instead the ray curves and $p = \sin\theta(z)/v(z)$ is constant *along the
ray* while both $\theta$ and $v$ change. The differential statement replaces the
algebraic one, and the travel time becomes an integral rather than a sum. This is
the starting point of ray theory in
[06-seismology](../../../06-seismology/README.md), and it is why the ray parameter —
not the angle — is the natural variable for inversion.
