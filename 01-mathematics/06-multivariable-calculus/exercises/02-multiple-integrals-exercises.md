# Exercises — 01-06-02 Multiple Integrals and Change of Variables

Attempt these **closed-book** before opening the
[solutions](./02-multiple-integrals-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Unless a problem says otherwise, use $G = 6.674\times10^{-11}$ and report
defensible significant figures.

---

## ★ Foundational

**★1.** Evaluate $\displaystyle\iint_R (x + 2y)\,dA$ over the rectangle
$R = [0,3]\times[0,2]$, in both orders of integration, and confirm that the
answers agree.

---

**★2.** Evaluate the integral of $f(x,y) = xy$ over the triangle with vertices
$(0,0)$, $(1,0)$ and $(1,1)$.

(a) Set it up with $x$ on the outside.
(b) Set it up with $y$ on the outside.
(c) Evaluate one of the two and confirm you get the same value as the other by
inspection of the limits.

---

**★3.** Find the area of the region bounded above by $y = \sqrt{x}$ and below by
$y = x^2$ for $0 \le x \le 1$.

---

**★4.** Using the spherical volume element, evaluate
$\displaystyle\iiint x^2\, dV$ over the unit ball, and then use the symmetry of
the integrand in the three coordinates to state the value of
$\displaystyle\iiint (x^2+y^2+z^2)\,dV$ over the same ball.

---

## ★★ Applied

**★★5.** A body has radius $R$ and density profile
$\rho(r) = \rho_0\left(1 - r^2/R^2\right)$.

(a) Set up and evaluate $M = 4\pi\int_0^R \rho(r) r^2\, dr$ in closed form.
(b) Evaluate the mean density $\bar{\rho} = M/V$ and compare it with $\rho_0$.
(c) Evaluate $M$ numerically for $\rho_0 = 3000\ \mathrm{kg\,m^{-3}}$ and
$R = 6.0\times10^5$ m.
(d) Explain in one sentence why the mean is a smaller fraction of $\rho_0$ here
than for the linear profile $\rho = \rho_0(1-r/R)$.

---

**★★6.** Show, by explicit integration, that the moment of inertia of a uniform
solid sphere of mass $M$ and radius $R$ about an axis through its centre is
$I = \tfrac{2}{5}MR^2$.

(a) Write $I_z = \iiint\rho (x^2+y^2)\,dV$ and evaluate it directly.
(b) Confirm your result by substituting $M = \tfrac{4}{3}\pi\rho R^3$ into it.
(c) State the radius of gyration.

---

**★★7.** A map sheet covers the square $[-10,10]\times[-10,10]$ km. A quantity
$f(x,y)$ is measured on a grid with spacing 1 km, and a student computes the
average of the grid values, reporting it as "the mean over the area".

(a) Write the correct integral expression for the mean.
(b) Assuming $f$ is smooth, estimate the quadrature error of the midpoint rule
with a 1 km grid in terms of the second derivatives of $f$.
(c) Give a concrete $f$ for which the grid average differs substantially from the
area mean, and evaluate both analytically.
(d) State the general condition under which the arithmetic mean of gridded values
*is* the area mean.

---

**★★8.** Consider $\displaystyle\int_{-1}^{1}\sqrt{1-x^2}\,dx$ and
$\displaystyle\int_{-1}^{1}(1-x^2)^{1/4}\,dx$.

(a) Determine the exact value of the first integral.
(b) Show that the integrands have infinite derivatives at the endpoints in both
cases, and describe how the asymptotic error of the midpoint rule differs between
them.
(c) Verify your prediction numerically with the midpoint rule at
$n = 100, 400, 1600$ and report the observed error ratios.

---

## ★★★ Research-oriented

**★★★9.** Compare quadrature and Monte Carlo in $d = 1, 2, 3, 4$ dimensions for
the volume of the $d$-dimensional unit ball, using the same total number of
integrand evaluations $N$ in each case.

(a) State the exact $d$-ball volume for each $d$ (the general formula uses the
gamma function).
(b) Implement both methods, and for $N = 10^4, 10^5, 10^6$ report the relative
error of each.
(c) Plot or tabulate relative error against $N$ and estimate the empirical
exponent for each method in each dimension.
(d) State the dimension at which Monte Carlo becomes competitive in your
measurements, and compare with the theoretical crossover implied by
$N^{-2/d}$ against $N^{-1/2}$.

This is a numerical-experiment report; include a table and state the limits of
your conclusion.

---

**★★★10.** A gravity survey over an ore body produces a total excess mass
estimate from the integral of the anomaly over the survey area. Suppose the
anomaly field is known only inside the survey polygon, and the region outside is
unknown.

(a) Write the estimate as a double integral over the polygon.
(b) If the anomaly is approximated as zero outside the polygon, express the
resulting error as an integral over the complement, and show it depends on the
behaviour of the anomaly at the boundary.
(c) For a point-mass anomaly $g_z = GMd/(\rho^2+d^2)^{3/2}$ truncated at radius
$R$, compute the fraction of the true "excess mass" integral captured as a
function of $R/d$: evaluate it at $R/d = 1, 3, 10$ and state how much of the
total is lost.
(d) Discuss what this implies for mass-balance estimates from limited surveys.

For (c) you may use the result
$\int_0^R \dfrac{2\pi\rho\, d\rho}{(\rho^2+d^2)^{3/2}} =
\dfrac{2\pi}{d}\left(1 - \dfrac{d}{\sqrt{R^2+d^2}}\right)$
and the fact that the total over $0 < \rho < \infty$ equals $2\pi/d$.
