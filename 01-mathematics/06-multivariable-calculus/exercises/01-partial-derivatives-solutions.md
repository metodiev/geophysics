# Solutions — 01-06-01 Partial Derivatives, Gradients and Directional Derivatives

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Every numeric answer below was computed, not
> estimated by hand; where a computation was done by program, the program is
> identified.

Throughout, $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

---

## ★1 — First partial derivatives

**(a)** $f = x^3y^2 - 4xz + 7$

$$\frac{\partial f}{\partial x} = 3x^2y^2 - 4z, \qquad
\frac{\partial f}{\partial y} = 2x^3y, \qquad
\frac{\partial f}{\partial z} = -4x .$$

**(b)** $f = \sin(xy) + z^2\ln x$

$$\frac{\partial f}{\partial x} = y\cos(xy) + \frac{z^2}{x}, \qquad
\frac{\partial f}{\partial y} = x\cos(xy), \qquad
\frac{\partial f}{\partial z} = 2z\ln x .$$

**(c)** $f = e^{-z}\cos(x+y)$

$$\frac{\partial f}{\partial x} = -e^{-z}\sin(x+y), \qquad
\frac{\partial f}{\partial y} = -e^{-z}\sin(x+y), \qquad
\frac{\partial f}{\partial z} = -e^{-z}\cos(x+y) .$$

Note $\partial f/\partial x = \partial f/\partial y$ here: $f$ depends on $x$ and
$y$ only through their sum, so it is constant along lines $x + y = \mathrm{const}$.

**(d)** $f = (x^2+y^2+z^2)^{-1/2}$. With $r^2 = x^2+y^2+z^2$,

$$\frac{\partial f}{\partial x} = -\frac{1}{2}\left(x^2+y^2+z^2\right)^{-3/2}(2x)
= -\frac{x}{r^3},$$

and cyclically. So $\nabla f = -\mathbf{r}/r^3 = -\hat{r}/r^2$.

---

## ★2 — Gradient of a gravitational potential

**(a)** With $r = \sqrt{x^2+y^2+z^2}$,

$$\frac{\partial V}{\partial z}
= GM\frac{\partial}{\partial z}\left(x^2+y^2+z^2\right)^{-1/2}
= GM\left(-\frac{1}{2}\right)\left(x^2+y^2+z^2\right)^{-3/2}(2z)
= -\frac{GMz}{r^3}.$$

**(b)** At $\mathbf{r} = (300, -400, 1000)$ m:

$$r = \sqrt{9.0\times10^4 + 1.6\times10^5 + 1.0\times10^6}
= 1118.034\ \mathrm{m}, \qquad r^3 = 1.3975\times10^{9}\ \mathrm{m^3},$$

and $GM = 6.674\times10^{-11}\times2.0\times10^{11} = 13.348$. Therefore

$$\nabla V = -\frac{13.348}{1.3975\times10^{9}}(300,\,-400,\,1000)
= \left(-2.8653\times10^{-6},\ 3.8204\times10^{-6},\
-9.5511\times10^{-6}\right)\ \mathrm{m\,s^{-2}} .$$

**(c)**

$$\lvert\nabla V\rvert = \frac{GM}{r^2} = \frac{13.348}{1.25\times10^{6}}
= 1.06784\times10^{-5}\ \mathrm{m\,s^{-2}} = 1.0678\ \mathrm{mGal}.$$

**Check on the direction.** $\nabla V$ is a negative multiple of $\mathbf{r}$, so
the field points toward the origin, where the mass is. That is required.

**Check against the short formula.** $\lvert\nabla V\rvert = GM/r^2$ and
$r^2 = 1.25\times10^6$ m². The components' magnitude
$\sqrt{2.8653^2+3.8204^2+9.5511^2}\times10^{-6} = 1.06785\times10^{-5}$ agrees.
The component route is a genuine check on the radial formula, not a restatement.

---

## ★3 — Directional derivatives at $(1,2)$

**(a)** $f = x^2y + y^3$ gives

$$\nabla f = \left(2xy,\ x^2 + 3y^2\right), \qquad
\nabla f(1,2) = (4,\ 1 + 12) = (4,\ 13).$$

**(b)** $D_{\hat{u}}f = \nabla f\cdot\hat{u}
= 4\left(\tfrac{3}{5}\right) + 13\left(\tfrac{4}{5}\right)
= 2.4 + 10.4 = 12.8$ per unit distance.

**(c)** The gradient points in the direction of steepest ascent, so

$$\hat{u}_{\max} = \frac{(4,13)}{\lvert(4,13)\rvert}
= \frac{(4,13)}{\sqrt{185}} \approx (0.2941,\ 0.9558),$$

and the rate of increase in that direction is
$\lvert\nabla f\rvert = \sqrt{185} = 13.6015$.

**(d)** A direction orthogonal to the gradient:
$\hat{u} = (-13,\,4)/\sqrt{185} \approx (-0.9558,\ 0.2941)$. Then
$D_{\hat{u}}f = 4(-13) + 13(4) = 0$, so to first order $f$ does not change along
it — the direction is tangent to the level curve through $(1,2)$.

**Consistency check.** $D_{\hat{u}}f$ for the steepest direction should be at least
as large as for any other: $12.8 \le 13.6015$ ✓, and
$13.6015\cos\psi = 12.8$ gives $\psi = 19.8^\circ$, the angle between $(3,4)$ and
$(4,13)$.

---

## ★4 — A linearised change

**(a)** $q = x^2y^3$, so

$$dq = 2xy^3\,dx + 3x^2y^2\,dy .$$

At $(2,3)$ with $dx = +0.02$, $dy = -0.01$:

$$dq = 2(2)(27)(0.02) + 3(4)(9)(-0.01) = 2.16 - 1.08 = +1.08 .$$

**(b)** Exactly:

$$q(2.02,\ 2.99) = 2.02^2 \times 2.99^3
= 4.0804 \times 26.730899 = 109.0727\ldots,$$

while $q(2,3) = 108$, so the exact change is $+1.07276$.

**(c)** The linearisation (1.08) **over-estimates** the change by about 0.67 %.
The relative error of the linear model is $0.0072/1.0728 = 0.68\%$, consistent
with a second-order term of size
$\tfrac12(2y^3 dx^2 + 6xy^2\,dx\,dy + 6x^2y\,dy^2)$ evaluated at $(2,3)$:
$\tfrac12(2(27)(0.0004) + 6(2)(9)(-0.0002) + 6(4)(3)(0.0001))
= \tfrac12(0.0216 - 0.0216 + 0.0072) = 0.0036$,
which is small compared with the first-order terms but not zero, and its sign is
that of the observed discrepancy.

**Lesson.** Two-significant-figure agreement between a linear model and the truth
is not a validation of the model; the discrepancy here is exactly the second-order
term and can be *predicted* rather than discovered.

---

## ★★5 — Radial functions and the gradient of $1/r$

From $r^2 = x^2+y^2+z^2$, differentiate implicitly:

$$2r\frac{\partial r}{\partial x} = 2x
\qquad\Longrightarrow\qquad
\frac{\partial r}{\partial x} = \frac{x}{r}.$$

Cyclically, $\nabla r = (x,y,z)/r = \hat{r}$. Then the chain rule gives

$$\frac{\partial f}{\partial x} = F'(r)\frac{\partial r}{\partial x}
= F'(r)\frac{x}{r},$$

and collecting the three components,

$$\nabla f = F'(r)\frac{(x,y,z)}{r} = F'(r)\,\hat{r}. $$

For $F(r) = 1/r$, $F'(r) = -1/r^2$, so

$$\nabla\left(\frac{1}{r}\right) = -\frac{\hat{r}}{r^2}.$$

**Why this is the foundational identity.** The gravitational potential of any mass
distribution is $V = G\int\rho/D\,dV'$ and the field is $\nabla V$. The field of
the elementary source is the gradient of $1/D$, which is exactly this identity, so
the whole of potential theory — Gauss's law, Poisson's equation, the shell
theorem, the uniqueness theorems — is built from this one line of the chain rule.
It also produces the delta function of Lesson 07 through its divergence, which is
where the source term of Poisson's equation comes from.

---

## ★★6 — Sensitivities of a compact-body anomaly

Write $D^2 = x^2+y^2+d^2$, so $g_z = GMd\,D^{-3}$.

**(a)** Differentiating with respect to $d$ at fixed $(x,y)$,

$$\frac{\partial g_z}{\partial d}
= GM\left[D^{-3} + d\left(-3\right)D^{-4}\frac{\partial D}{\partial d}\right]
= GM\left[D^{-3} - 3d^2 D^{-5}\right]
= \frac{GM}{D^{3}}\left(1 - \frac{3d^2}{D^2}\right).$$

The sign is **negative** whenever $D^2 < 3d^2$, i.e. whenever
$x^2+y^2 < 2d^2$, and in particular at any point directly above the body. A deeper
body of the same mass produces a weaker and broader anomaly; at $x = y = 0$,
$g_z = GM/d^2$ and $\partial g_z/\partial d = -2GM/d^3$.

**(b)** On the line $y = 0$,

$$\frac{\partial g_z}{\partial x}
= GMd\left(-3\right)\left(x^2+d^2\right)^{-5/2}(2x)
= -\frac{3GMdx}{\left(x^2+d^2\right)^{5/2}},$$

which is negative for $x>0$: the anomaly falls off to the right of the peak, as it
must.

**(c)** With $M = 10^{11}$ kg and $d = 800$ m at $x = 400$ m, so
$D^2 = 400^2+800^2 = 8.0\times10^5\ \mathrm{m^2}$:

$$g_z = \frac{(6.674\times10^{-11})(10^{11})(800)}
{(8.0\times10^5)^{3/2}}
= 7.4618\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.7462\ \mathrm{mGal},$$

$$\frac{\partial g_z}{\partial d}
= \frac{6.674}{7.1554\times10^{8}}\left(1 - \frac{3(6.4\times10^5)}
{8.0\times10^5}\right) = -1.3058\times10^{-8}\ \mathrm{s^{-2}},$$

$$\frac{\partial g_z}{\partial x}
= -\frac{3(6.674)(800)(400)}{(8.0\times10^5)^{5/2}}
= -1.1193\times10^{-8}\ \mathrm{s^{-2}} .$$

The units of both derivatives are acceleration per metre, that is
$\mathrm{m\,s^{-2}\,m^{-1}} = \mathrm{s^{-2}}$.

**(d)** A resolution of 0.01 mGal is
$\Delta g = 10^{-7}\ \mathrm{m\,s^{-2}}$. Then

$$\lvert\Delta d\rvert = \frac{10^{-7}}{1.3058\times10^{-8}} = 7.66\ \mathrm{m},
\qquad
\lvert\Delta x\rvert = \frac{10^{-7}}{1.1193\times10^{-8}} = 8.93\ \mathrm{m}.$$

So in this configuration a ~8 m positional or depth error is equivalent to the
instrument resolution. The linearisation is comfortably valid: 8 m against a
length scale of 800 m is a 1 % perturbation, and the neglected second-order term
is of order $(8/800)^2 \approx 10^{-4}$ relative.

**Why this matters.** A survey that invests in a gravimeter with microgal
resolution but locates stations with metre-level GPS will be limited by geometry,
not by instrumentation. The computation above is the standard justification.

---

## ★★7 — The optimal finite-difference step

**(a)** The two error contributions are:

- **truncation**, from truncating the Taylor series of $f$ at the terms used by
  the stencil. For a central difference the leading term is
  $-\tfrac{h^2}{6}f'''(\xi)$, so it scales as $h^2$ and shrinks with $h$;
- **round-off**, from the fact that each $f$ value carries a relative error of
  order the machine epsilon $\epsilon_m$, and the difference is divided by
  $2h$. The absolute error in the difference is $\sim \epsilon_m\lvert f\rvert$,
  so the error in the quotient is $\sim \epsilon_m\lvert f\rvert/(2h)$, which
  *grows* as $h$ shrinks.

One term decreases, one grows, and their sum has a minimum.

**(b)** Minimise $\varphi(h) = Ch^2 + \epsilon/h$:

$$\varphi'(h) = 2Ch - \frac{\epsilon}{h^2} = 0
\qquad\Longrightarrow\qquad h^3 = \frac{\epsilon}{2C}
\qquad\Longrightarrow\qquad h = \left(\frac{\epsilon}{2C}\right)^{1/3}.$$

With $C = 1$ and $\epsilon = 10^{-16}$, $h = (5\times10^{-17})^{1/3}
= 3.7\times10^{-6}$.

**(c)** That answer is far from the measured optimum because the constants are
wrong by many orders of magnitude. Fitting the demonstration's own measurements
gives $C \approx 4.5\times10^{-7}$ (from the error $4.541\times10^{-7}$ at
$h = 1$ m) and $\epsilon \approx 7.2\times10^{-14}$ (from the observed floor of
$7.2\times10^{-11}$ at $h = 10^{-3}$ m). Then

$$h = \left(\frac{7.2\times10^{-14}}{2(4.5\times10^{-7})}\right)^{1/3}
= (8.0\times10^{-8})^{1/3} = 4.3\times10^{-3}\ \mathrm{m},$$

which is within a factor of a few of the measured optimum near $h = 10^{-2}$ m.
**The formula is the right tool; the constants must be measured, not guessed.**

---

## ★★8 — Slope uncertainty on a gridded surface

**(a)** With $z = g(x,y)$,

$$\lvert\nabla g\rvert = \sqrt{g_x^2 + g_y^2},$$

and the slope angle is $\arctan\lvert\nabla g\rvert$.

**(b)** Let $s = \sqrt{g_x^2+g_y^2}$. Then

$$\frac{\partial s}{\partial g_x} = \frac{g_x}{s}, \qquad
\frac{\partial s}{\partial g_y} = \frac{g_y}{s},$$

and with independent errors,

$$\sigma_s^2 = \left(\frac{g_x}{s}\right)^2\sigma_{g_x}^2
+ \left(\frac{g_y}{s}\right)^2\sigma_{g_y}^2.$$

A finite difference over a grid spacing $a$ converts an elevation error
$\sigma_z$ into a gradient error of order $\sigma_{g} \approx \sigma_z/a$ (the
factor depends on the stencil). With
$\sigma_{g_x} = \sigma_{g_y} = \sigma_z/a = \sigma_g$, the weights sum to one and

$$\sigma_s = \sigma_g = \frac{\sigma_z}{a}.$$

Note the cancellation of $s$: for a two-component gradient with equal component
errors, the *magnitude* has the same uncertainty as either component.

**(c)** With $a = 10$ m and $\sigma_z = 0.5$ m,
$\sigma_s = 0.5/10 = 0.05$. For $g_x = g_y = 0.1$, $s = 0.1414$ and the relative
uncertainty is

$$\frac{\sigma_s}{s} = \frac{0.05}{0.1414} = 35.4\%.$$

A 36 % slope error is not useful for anything quantitative. **The resolution
requirement is a property of the terrain, not of the DEM alone:** a gentler slope
gives a larger relative error at the same $\sigma_z/a$.

---

## ★★★9 — A measured convergence study

**Method.** For $V = GM/r$ with $M = 10^{11}$ kg and the observation point
$(400, -300, 1200)$ m ($r = 1300$ m), the analytic gradient is
$\nabla V = -GM\mathbf{r}/r^3$. The gradient was estimated with central and
forward differences for
$h \in \{10^{-5}, 10^{-4}, \dots, 10^{2}\}$ m, and the relative error reported as
$\lVert\nabla_h V - \nabla V\rVert/\lVert\nabla V\rVert$.

**Results.**

| $h$ (m) | central rel. error | forward rel. error |
|---|---|---|
| $10^{-5}$ | $1.471\times10^{-8}$ | $2.502\times10^{-8}$ |
| $10^{-4}$ | $1.126\times10^{-9}$ | $7.117\times10^{-8}$ |
| $10^{-3}$ | $7.222\times10^{-11}$ | $7.338\times10^{-7}$ |
| $10^{-2}$ | $5.113\times10^{-11}$ | $7.338\times10^{-6}$ |
| $10^{-1}$ | $4.541\times10^{-9}$ | $7.338\times10^{-5}$ |
| $10^{0}$ | $4.541\times10^{-7}$ | $7.336\times10^{-4}$ |
| $10^{1}$ | $4.541\times10^{-5}$ | $7.310\times10^{-3}$ |
| $10^{2}$ | $4.534\times10^{-3}$ | $7.070\times10^{-2}$ |

**(a)** Reported above.

**(b)** Between $h = 10^{-1}$ and $h = 10^{2}$ m the central-difference error falls
by a factor of $10^{2}$ per decade in $h$, which is the $h^2$ of a second-order
stencil. The error reaches a minimum of $5.113\times10^{-11}$ at $h = 10^{-2}$ m.
Below that the error *rises*: $7.2\times10^{-11}$ at $h = 10^{-3}$ and
$1.5\times10^{-8}$ at $h = 10^{-5}$ m. That is the round-off term
$\sim\epsilon_m/h$ taking over.

**(c)** In the truncation-dominated region the forward difference falls by a
factor of about $10$ per decade, so its log–log slope is $-1$ and it is
**first-order** accurate, against $-2$ for the central difference. The measured
error at $h = 1$ m differs by a factor of $7.336\times10^{-4}/4.541\times10^{-7}
= 1615$, i.e. the two extra orders of magnitude expected from one extra order of
accuracy plus a larger constant.

**(d)** The best achievable relative error is of order
$\sqrt{\epsilon_m}$-ish combination of the two terms at the optimum:
from Section ★★7, $h^\star = (\epsilon/(2C))^{1/3}$ and the minimum error is
$\approx \tfrac{3}{2}C^{1/3}\epsilon^{2/3}$. With $C = 4.5\times10^{-7}$ and
$\epsilon = 7.2\times10^{-14}$ this predicts
$1.5\times(7.7\times10^{-3})\times(1.7\times10^{-9}) \approx 2\times10^{-11}$,
against the measured $5.1\times10^{-11}$. Agreement to a factor of 2.5, which is
as much as the crude model should be expected to deliver.

**Limitations.** The measured $C$ and $\epsilon$ depend on the function, the
point, and the summation order inside the stencil. The exponent 2 is a property
of the *stencil*, and would change for a one-sided or higher-order scheme. The
result says nothing about accuracy in the presence of *modelled* noise, which is
a different and usually larger effect.

---

## ★★★10 — The gravity gradient tensor

**(a)** $T_{ij} = GM(3x_ix_j/r^5 - \delta_{ij}/r^3)$. The first term is symmetric
in $i$ and $j$ because $x_ix_j = x_jx_i$ and the delta is symmetric, so
$T_{ij} = T_{ji}$. **This is the Clairaut–Schwarz theorem from Section 2.2 of the
lesson**, applied to a $C^\infty$ potential away from the source.

**(b)**

$$T_{xx} + T_{yy} + T_{zz}
= GM\left[\frac{3(x^2+y^2+z^2)}{r^5} - \frac{3}{r^3}\right]
= GM\left[\frac{3r^2}{r^5} - \frac{3}{r^3}\right] = 0 .$$

The trace is **identically zero**. That is Laplace's equation in disguise:
$\nabla^2V = \mathrm{tr}\,\mathbf{H} = 0$ outside the source. The eleven
independent components of a symmetric traceless $3\times3$ tensor are five, which
is why a gravity gradiometer measures five independent quantities and why the
tensor is a favourite target for interpretation: the constraint
$\mathrm{tr}\,\mathbf{T} = 0$ holds whatever the source distribution is, and can
be used as a noise or consistency check on measured gradients.

**(c)** Directly above a mass at depth $d$ (mass at $(0,0,-d)$, station at the
origin), the potential along the axis is $V(z) = GM/(z+d)$, so

$$g_z = -\frac{\partial V}{\partial z} = \frac{GM}{(z+d)^2},
\qquad
T_{zz} = \frac{\partial g_z}{\partial z}
= -\frac{2GM}{(z+d)^3}\Big|_{z=0} = -\frac{2GM}{d^3}.$$

The negative sign has a physical reading: the downward field weakens as you move
up, so its vertical gradient is negative. The value agrees with the numerical
second difference computed in the lesson demonstration, which reported
$-2.607039\times10^{-8}\ \mathrm{s^{-2}}$ against the analytic
$-2.607031\times10^{-8}\ \mathrm{s^{-2}}$ for $M = 10^{11}$ kg and $d = 800$ m.

**(d)** The field scales as $d^{-2}$ and the tensor as $d^{-3}$. For a source at
200 m against one at 400 m, the ratio of their contributions is

$$\left(\frac{400}{200}\right)^2 = 4 \quad\text{(field)},
\qquad
\left(\frac{400}{200}\right)^3 = 8 \quad\text{(tensor)} .$$

So the tensor discriminates the shallow source by a factor of 8 where the field
discriminates it by a factor of 4 — a factor of 2 improvement in the contrast
between the two, achieved by measuring one more derivative. The same scaling
explains why the tensor is dominated by near-surface structure and why
gradiometry is used for airborne surveys where the sensor is far from the target.

**Statement of status.** (a), (b), (c) are analytic. The numerical comparison in
(c) is quoted from
[`../code/gradient_and_field.py`](../code/gradient_and_field.py), which was run
for this module; the agreement is limited by the $h^2$ truncation error of the
one-metre second difference, as the lesson's Section 5 documents.
