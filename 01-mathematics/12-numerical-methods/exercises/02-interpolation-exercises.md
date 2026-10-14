# Exercises — 01-12-02 Interpolation, Splines and Approximation Theory

Attempt these **closed-book** before opening the
[solutions](./02-interpolation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $p_n$ denotes the degree-$\le n$ interpolating polynomial through
$n+1$ nodes; $\omega(x)=\prod_j(x-x_j)$; a cubic spline has moments
$M_i=s''(x_i)$; "natural" means $M_0=M_n=0$ and "clamped" means the end slopes are
prescribed. State any convention you add.

---

## ★ Foundational

**★1.** Write the Lagrange cardinal polynomials for the nodes $0, 1, 3$ and
evaluate the interpolant at $x=2$ for the values $y=(1,2,0)$.

---

**★2.** Construct the divided-difference table for the same data and evaluate the
Newton form at $x=2$. Confirm that the two forms agree.

---

**★3.** Show that $\max_{[-1,1]}\lvert\omega(x)\rvert$ for three equispaced nodes
at $x=-1,0,1$ is $2/(3\sqrt3)$, and use it to bound the interpolation error of
$f(x)=\mathrm e^x$ on $[-1,1]$.

---

**★4.** A well log has values 0.19, 0.21, 0.22 at depths 1000, 1001, 1002 m.
Estimate the value at 1001.4 m by linear interpolation, and state the size of the
curvature error if the second derivative is $2\times10^{-4}\ \mathrm{m^{-1}}$.

---

## ★★ Applied

**★★5.** Derive the tridiagonal moment system of the spline from the $C^1$
continuity condition, showing each step. State why the system is uniquely
solvable.

---

**★★6.** For the natural cubic spline on nodes $0,1,2,3$ with $y=(0,1,1,0)$,
solve for the moments and evaluate the spline at $x=1.5$. State $s''$ at the ends
and comment on whether the natural condition is appropriate here.

---

**★★7.** Using the error formula, explain why the Runge function's equispaced
interpolation error grows roughly by a constant factor per added node, and
estimate that factor from the measured table in the lesson. State the two
competing factors in the error formula and which one wins.

---

**★★8.** A gravity profile is sampled at $x = 0,100,\dots,1000$ m and a value is
wanted at $x=1500$ m. Write a short paragraph stating what you would do and why
the sentence "I will use a cubic spline" is not an answer.

---

## ★★★ Research-oriented

**★★★9.** Construct a data set of 20 equispaced samples of $f(x)=1/(1+25x^2)$
with 1% relative Gaussian noise and compare the max interpolation error on
$[-1,1]$ obtained by (a) the interpolating polynomial, (b) a natural cubic spline,
and (c) a degree-6 least-squares fit. Report the measured errors for the noisy and
the noise-free data, and explain why the ranking is what it is.

---

**★★★10.** A published map of a gravity field is described as "interpolated with
a bicubic spline from a 5 km grid". Write a critique: what can legitimately be
inferred from the map at 1 km scale, what cannot, and what diagnostic would reveal
whether overshoot has produced spurious anomalies?
