# Exercises — 01-06-01 Partial Derivatives, Gradients and Directional Derivatives

Attempt these **closed-book** before opening the
[solutions](./01-partial-derivatives-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Several problems ask you to modify and run
[`../code/gradient_and_field.py`](../code/gradient_and_field.py). Do that
literally rather than reasoning about it: the point is to compare what you
predicted with what the machine returns.

---

## ★ Foundational

**★1.** Compute all first partial derivatives.

(a) $f = x^3y^2 - 4xz + 7$
(b) $f = \sin(xy) + z^2\ln x$
(c) $f = e^{-z}\cos(x+y)$
(d) $f = 1/\sqrt{x^2+y^2+z^2}$

---

**★2.** A point mass $M = 2.0\times10^{11}$ kg sits at the origin, and the
potential is $V = GM/r$ with $G = 6.674\times10^{-11}$.

(a) Express $V$ as a function of $(x,y,z)$ and compute $\partial V/\partial z$
directly.
(b) Evaluate $\nabla V$ at $(300, -400, 1000)$ m.
(c) State the magnitude of the resulting gravitational acceleration in
m/s² and in mGal.

---

**★3.** For $f(x,y) = x^2y + y^3$ at the point $(1,2)$:

(a) compute $\nabla f$;
(b) compute the directional derivative in the direction of the unit vector
$\hat{u} = (3/5,\,4/5)$;
(c) find the direction of steepest ascent and the rate of increase in that
direction;
(d) find a direction in which $f$ does not change to first order.

---

**★4.** Use the total differential to estimate the change in
$q = x^2 y^3$ when $x$ increases from 2.00 to 2.02 and $y$ decreases from 3.00 to
2.99.

(a) Compute $\delta q$ from the first-order model.
(b) Compute the exact change.
(c) State whether the linearisation over- or under-estimates the change.

---

## ★★ Applied

**★★5.** For $f(\mathbf{r}) = F(r)$ with $r = \lvert\mathbf{r}\rvert$, derive
$\partial r/\partial x$ from $r^2 = x^2+y^2+z^2$, and hence confirm
$\nabla f = F'(r)\hat{r}$.

Then apply the result to $F(r) = 1/r$ and explain in one or two sentences why
this is the identity on which the whole of gravitational potential theory rests.

---

**★★6.** A compact body of mass $M$ is buried at depth $d$ beneath the origin. On
the surface the downward gravity field is

$$g_z(x,y) = \frac{GMd}{(x^2+y^2+d^2)^{3/2}} .$$

(a) Compute $\partial g_z/\partial d$ and state its sign.
(b) Compute $\partial g_z/\partial x$ on the line $y=0$.
(c) With $M = 10^{11}$ kg and $d = 800$ m, evaluate both derivatives at
$x = 400$ m and give their units.
(d) A gravimeter resolves 0.01 mGal. Determine the smallest depth error
(resp. horizontal position error) that this resolution could detect in this
configuration. Discuss whether the linearisation is trustworthy at that size.

---

**★★7.** Using central differences, the relative error in the derivative of a
smooth function behaves like $C h^2 + \epsilon/h$ where $\epsilon$ is a
round-off scale.

(a) Explain qualitatively why one term decreases in $h$ and the other grows.
(b) If $C = 1$ and $\epsilon = 10^{-16}$, find the value of $h$ that minimises
the relative error by differentiating the expression.
(c) Compare your answer with the measured optimum in the demonstration, which is
near $h = 0.01$ m for a length scale of about $1300$ m.

---

**★★8.** A topographic surface is given by $z = g(x,y)$, and elevation is
measured with a standard uncertainty of $\sigma_z$.

(a) Write the slope magnitude as a function of the two partial derivatives.
(b) Derive the first-order uncertainty in the slope magnitude in terms of
$\sigma_{g_x}$ and $\sigma_{g_y}$, assuming they are independent and equal to
$\sigma_z/h$ where $h$ is the grid spacing.
(c) Evaluate the result for a grid spacing of 10 m and $\sigma_z = 0.5$ m on a
slope whose gradient components are both 0.1 (that is, a 10 m drop per 100 m).
Is the slope estimate useful at that resolution?

---

## ★★★ Research-oriented

**★★★9.** Write a program that measures the relative error of the
central-difference gradient of $V = GM/r$ on a sphere of radius $r_0$ as a
function of $h$, for
$h \in \{10^{-5}, 10^{-4}, \dots, 10^{2}\}$ m and $r_0 = 1300$ m.

(a) Report the observed error for each $h$ in a table.
(b) Identify the region where the error falls as $h^2$ and the value of $h$ at
which it is minimised.
(c) Repeat for the forward difference and report the slope of the log–log error
curve in the truncation-dominated region for each stencil.
(d) State the empirical relation between the best achievable relative error and
the machine epsilon, and compare with the theoretical estimate.

This is a numerical-experiment report: give the method, the results as a table,
and the limitations of your conclusion.

---

**★★★10.** The gravity gradient tensor of a point mass is the Hessian of its
potential:

$$T_{ij} = \frac{\partial^2 V}{\partial x_i \partial x_j}
= GM\left(\frac{3x_ix_j}{r^5} - \frac{\delta_{ij}}{r^3}\right).$$

(a) Verify that $T_{ij}$ is symmetric.
(b) Compute the trace $T_{xx} + T_{yy} + T_{zz}$ and interpret the result in
terms of Laplace's equation.
(c) Show that $T_{zz} = -2GM/d^3$ at the point directly above a mass at depth $d$.
(d) Compare the distance dependence of the field, $g_z \propto GM/d^2$, with that
of the tensor component, $T_{zz} \propto GM/d^3$. The amplitude of both scales
with the source mass, so the useful quantity is the ratio of the contributions
from two sources at different depths. Compute the ratio of the $g_z$
contributions and the ratio of the $T_{zz}$ contributions for one source at 200 m
and another at 400 m, and state the discriminating power gained by measuring the
tensor instead of the field.

Report measured values only if you verify them numerically; state clearly which
of your results are analytic.
