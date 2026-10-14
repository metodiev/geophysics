# Solutions — 18-06-04 Surrogate Models and Polynomial Chaos for UQ

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [04 Surrogate Models and Polynomial Chaos for UQ](../04-surrogate-uq.md).

---

## ★1 — Orthonormality

Legendre polynomials satisfy $\int_{-1}^{1}P_m P_n\,\mathrm{d}\xi =
\frac{2}{2n+1}\delta_{mn}$. With the measure $\mathrm{d}\xi/2$,

$$
\int_{-1}^{1}\psi_m\psi_n\,\frac{\mathrm{d}\xi}{2}
= \sqrt{2m+1}\sqrt{2n+1}\,\frac{1}{2}\int_{-1}^{1}P_mP_n\,\mathrm{d}\xi
= \frac{2n+1}{2}\cdot\frac{2}{2n+1}\,\delta_{mn} = \delta_{mn}.
$$

The measure $\mathrm{d}\xi/2$ with $\xi = 2x-1$ is exactly the uniform distribution
on $[0,1]$, i.e. $x\sim\mathcal{U}[0,1]$. Had the input been Gaussian, the
corresponding orthonormal family would be Hermite polynomials with the Gaussian
weight.

---

## ★2 — The coefficient of $\psi_2(\xi_1)$

With $\xi_1 = 2x_1-1$, we have $x_1-0.5 = \xi_1/2$, so

$$
10(x_1-0.5)^2 = 10\cdot\frac{\xi_1^{2}}{4} = 2.5\,\xi_1^{2},
\qquad
\xi_1^{2} = \frac{2P_2(\xi_1) + P_0(\xi_1)}{3},
$$

using $P_0 = 1$ and $P_2 = (3\xi^2-1)/2$. Hence

$$
2.5\,\xi_1^{2} = \frac{5}{3}P_2(\xi_1) + \frac{5}{6}P_0(\xi_1),
\qquad
\psi_2 = \sqrt5\,P_2,
$$

$$
c_{(2,0,0)} = \frac{5/3}{\sqrt5} = \frac{\sqrt5}{3} = 0.745356,
\qquad
c_{(2,0,0)}^{2} = \frac{5}{9} = 0.5555556 = V_1 .
$$

---

## ★3 — Why degree 1 reports $x_1$ as inert

The quadratic term has zero mean *after* centring: the projection of
$10(x_1-0.5)^2$ onto the constant and linear basis functions is
$\mathbb{E}[10(x_1-0.5)^2] = 10/12 = 0.8333$ on $\psi_0$ and nothing on $\psi_1$.
A degree-1 expansion therefore represents the mean contribution and nothing else,
and the variance attributed to $x_1$ is $7.5\times10^{-8}$ — numerical zero. The
model's variance in $x_1$ lives entirely in the degree-2 coefficient, which the
truncation has discarded.

---

## ★★4 — Variance from the coefficients

The three nontrivial coefficients are

$$
c_{(2,0,0)} = \frac{\sqrt5}{3}, \qquad
x_2 = \frac{\xi_2+1}{2}\ \Rightarrow\ c_{(0,1,0)} = \frac{1/2}{\sqrt3} = 0.288675,
$$

$$
0.5\,x_3 = \frac{0.5}{2}(\xi_3+1)\ \Rightarrow\
c_{(0,0,1)} = \frac{0.25}{\sqrt3} = 0.144338 .
$$

Their squares are $5/9 = 0.555556$, $1/12 = 0.083333$ and $0.25/12 = 0.020833$,
which sum to $0.659722$ — the exact variance printed in the demonstration. There
are no interaction coefficients because the model is additive, so the sum of squares
is complete.

---

## ★★5 — The underdetermined fit

At $20$ training points with $35$ basis functions the least-squares problem is
underdetermined: infinitely many coefficient vectors reproduce the training data
exactly, and the pseudo-inverse returns one of them, which extrapolates badly. The
held-out RMSE of $1.03$ is of the order of the function's own standard deviation
($\sqrt{0.659722} = 0.812$), i.e. the surrogate has no predictive skill.

**Diagnostic.** Compute the numerical rank or the condition number of the design
matrix before fitting (the demonstration prints $11.15$ at $N = 20$ against $1.15$ at
$N = 1000$), and always validate on held-out points drawn from the same measure. A
training-set error would be zero for the $N=20$ fit and would have disguised the
failure completely.

---

## ★★6 — Cost accounting

**(a)** For a Gaussian-like output, $\operatorname{Var}(\hat V)/V^{2} \approx 2/N$, so
a $1\%$ relative standard error needs

$$
\frac{2}{N} = (0.01)^{2} \ \Rightarrow\ N = \frac{2}{10^{-4}} = 20\,000 .
$$

**(b)** For $0.1\%$: $N = 2/(10^{-3})^{2} = 2\times10^{6}$.

**(c)** The saving of $20\,000/1024 = 19.5$ (and $1953$ in case (b)) is real only if
the surrogate's own error is small compared with the target accuracy, if the model is
smooth enough for the expansion to converge at the chosen degree, and if the query
points lie inside the range the training design covered. Otherwise the comparison is
between a precise answer to the wrong question and a noisy answer to the right one.

---

## ★★7 — A gap larger than the reference's error

**Can be concluded:** the surrogate's variance is biased low by $0.000261$, which is
$2.7$ times the Monte Carlo standard error of the reference, so the bias is real and
not a sampling artefact. The residual is truncation error of the expansion.

**Cannot be concluded:** that the reference is the truth. The reference itself carries
$0.000097$ of standard error, and a still higher-degree expansion would be needed to
show whether the remaining gap closes onto the reference or onto a slightly different
value.

**Reporting.** Quote the surrogate variance with the interval produced by its own
validation error, e.g. $0.096586 \pm 0.0003$ where the $\pm$ is the truncation
estimate obtained by comparing degrees 5 and 6, and state the reference with its own
standard error. Presenting $0.096586$ as the answer would attribute the surrogate's
error to the physics.

---

## ★★8 — Surrogate workflow for 20 parameters

- **Family:** for independent uniform inputs, Legendre; if the inputs are lognormal
  or Gaussian, Hermite in the transformed variable. State the transform and check
  that the transformed variables are the ones sampled.
- **Truncation:** total degree $p$ with a hyperbolic-cross rule $|\alpha|_q \le p$ to
  keep the basis polynomial rather than combinatorial; report the number of retained
  terms and the criterion used to discard the rest.
- **Training design:** a Sobol' sequence of at least twice the number of retained
  coefficients, plus a doubling check that the coefficients are stable.
- **Validation:** at least $200$ held-out points from the same measure; report RMSE
  and the maximum error relative to the output standard deviation; run a
  degree-$p$ against degree-$(p+1)$ comparison for the quantities actually reported.
- **Error propagation:** compute the UQ quantities at degrees $p$ and $p+1$; take the
  difference as the surrogate error and add it, in quadrature with the Monte Carlo
  error of the surrogate ensemble, to the reported interval. State both terms
  separately so a reader can see which dominates.
