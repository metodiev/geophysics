# Exercises — 01-14-04 Linear and Nonlinear Least Squares

Attempt these **closed-book** before opening the
[solutions](./04-least-squares-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $\phi(m) = \tfrac12\|Gm - d\|^{2}$ for a linear forward operator $G$;
$\kappa = \sigma_{\max}(G)/\sigma_{\min}(G)$; $\hat\sigma^{2} =
\|r\|^{2}/(n-p)$; $u = 2.2\times10^{-16}$. Where a problem asks for a numerical
result, state the method used and the accuracy claimed.

Problems referring to
[`../code/least_squares_demo.py`](../code/least_squares_demo.py) require you to
run it and report its actual output.

---

## ★ Foundational

**★1.** Derive the normal equations for $\phi(m) = \tfrac12\|Gm - d\|^{2}$.

(a) Expand $\phi$ and compute $\nabla\phi$ using
$\nabla_m\,\tfrac12m^{\mathsf T}Am = \tfrac12(A+A^{\mathsf T})m$.
(b) Set the gradient to zero and obtain $G^{\mathsf T}Gm = G^{\mathsf T}d$.
(c) Show $G^{\mathsf T}r = 0$ at the solution and explain the geometric statement
this makes about $r$ and the column space of $G$.
(d) State what happens to the solution if $G$ has a nontrivial null space.

---

**★2.** Show that $\kappa_2(G^{\mathsf T}G) = \kappa_2(G)^{2}$.

(a) Use the SVD $G = U\Sigma V^{\mathsf T}$ to compute $G^{\mathsf T}G$.
(b) Hence state the identity and explain why it is an identity and not a bound.
(c) Compute the value of $\kappa_2(G)$ above which $\kappa^{2}$ exceeds
$1/u$, and state what that means for a binary64 solve.
(d) State the *second* consequence of the squaring, concerning the model
covariance, and write the covariance matrix in terms of the SVD.

---

**★3.** For the model $f(x) = a\,\mathrm{e}^{-x/h}$ with two parameters:

(a) Write down the Jacobian $J$ at a general $x_i$.
(b) Write one Gauss–Newton step explicitly.
(c) Show that when every datum has $x_i \gg h$ the two columns of $J$ become
nearly parallel, and identify the parameter combination that remains determined.
(d) Compute $\kappa_2(J)$ for the designs $x = (0,1,2,3,4,5)$,
$x = (5,10,15,20,25,30)$ and $x = (50,60,\dots,100)$, with $a = 1$, $h = 1$, and
state the practical consequence of each number.

---

**★4.** Data with uncertainties $\sigma = (0.1, 0.1, 1.0, 1.0)$ are fitted by
$y = a + bx$ at $x = 0,1,2,3$ with $y = (1.0, 2.0, 2.2, 3.4)$.

(a) Compute the ordinary least-squares estimate and $\hat\sigma^{2}$.
(b) Compute the weighted estimate with weights $w_i = 1/\sigma_i^{2}$, and the
weighted $\hat\sigma^{2}$.
(c) Compute the standard errors of $a$ and $b$ in both cases.
(d) State which quantities the weights legitimately change and which they must
leave alone.

---

## ★★ Applied

**★★5.** The model $y = A\mathrm{e}^{-\lambda x}$ is fitted to exact data
generated from $A = 2$, $\lambda = 0.5$ at $x = 0,1,\dots,5$, starting from
$(A,\lambda) = (1,1)$.

(a) Write $J$ and the Gauss–Newton step.
(b) Carry out the iteration and report the parameters and $\|r\|$ after each of
the first four steps.
(c) Report the residual norm at the start, the largest residual norm encountered,
and the step at which the iteration reaches $\|r\| < 10^{-10}$.
(d) Explain why the first step *increases* the residual, and state what a
trust-region or damping modification would do about it.

---

**★★6.** Show that Gauss–Newton is exact for a linear model.

(a) For $F(m) = Gm$, write $r_k = Gm_k - d$ and $J_k = G$.
(b) Show that the Gauss–Newton step gives $m_1 = (G^{\mathsf T}G)^{-1}G^{\mathsf T}d$
regardless of $m_0$.
(c) Relate this to Newton's method on a quadratic and to the curvature model
$J^{\mathsf T}J$.
(d) State the two reasons the same argument does *not* transfer to a nonlinear
model with large residuals, naming the missing Hessian term.

---

**★★7.** For the scalar problem $\min_m\,\phi(m) = (m^{2} - 2)^{2}$:

(a) Write the residual $r(m)$, the Jacobian $J(m)$, and the Gauss–Newton step.
(b) Show the Gauss–Newton iteration is $m_{k+1} = (m_k^{2} + 2)/(2m_k)$ — Newton's
method for $m^{2} = 2$ — and hence that convergence is quadratic.
(c) Write the Levenberg–Marquardt step with $D = I$ and damping $\lambda$.
(d) Iterate from $m_0 = 1$ with $\lambda = 0, 1, 10, 100$ for exactly ten steps and
report the error each time. State what a fixed $\lambda$ does to the fixed point
and what it does to the *path*.

---

**★★8.** Leverage in a straight-line fit.

Data at $x = 0,1,2,3,4$ with the last datum a blunder, $y = (1,2,2,4,9)$; the
"clean" data replace $9$ by $4.6$.

(a) Compute the leverages $h_i = 1/n + (x_i - \bar x)^{2}/S_{xx}$, verify
$\sum_ih_i = p$, and comment on which samples control the fit.
(b) Compute the ordinary least-squares line for both datasets.
(c) Show that the shift in the slope is $\Delta b = e(x_j - \bar x)/S_{xx}$ with
$e$ the blunder at sample $j$, and evaluate it; do the same for the intercept and
for the fitted value at the outlier.
(d) Explain why a single high-leverage outlier moves the slope by more than the
outlier's own size — in this dataset, a factor of about five.

---

## ★★★ Research-oriented

**★★★9.** Two nearly parallel rays are least-squares fitted with
$G = \begin{pmatrix}1&1\\1&1+\delta\end{pmatrix}$ and exact data generated from
$m = (0.05,-0.02)$, for $\delta = 10^{-2}, 10^{-4}, 10^{-6}, 10^{-8}$.

(a) Implement the normal-equation route and a Householder QR route in the same
programming language, and compute an exact rational reference solution from the
same floating-point inputs.
(b) Tabulate $\kappa_2(G)$, the float determinant of $G^{\mathsf T}G$, the
relative error of each float route, and the ratio between them, for the four
values of $\delta$.
(c) Report the $\delta$ at which the normal-equation route fails outright, and
state what the QR route achieves there.
(d) Explain why an extended-precision computation of $\kappa$ is required for the
$10^{-8}$ case, and what "measuring $\kappa$ badly" means.

---

**★★★10.** A colleague solves a 40-station gravity profile for 200 coefficients by
forming $G^{\mathsf T}G$ and reports a *residual* of $10^{-11}$ mGal together with
a model that oscillates with a wavelength of two stations.

(a) Explain the oscillation from the resolution matrix and the conditioning
argument, without asserting a number you have not computed.
(b) Explain why the small residual is not evidence of a good model, and state the
identity that relates the model error to the residual.
(c) State the two changes you would make, in order, and what each does to the
resolution and to the variance of the estimate.
(d) State one quantity you would report alongside the model so that a reader can
judge the oscillation, and say how it is computed from the same matrices.
