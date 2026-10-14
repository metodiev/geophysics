# Exercises — 01-12-06 Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive

Attempt these **closed-book** before opening the
[solutions](./06-ode-solvers-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the model problem is $y' = \lambda y$ with
$\mathrm{Re}\,\lambda < 0$, $z = h\lambda$, and the **stability function** $R(z)$
is defined by $y_{n+1} = R(z)y_n$. The explicit stability interval on the
negative real axis is written $[z_{\min},0]$. Report every order as a measured
ratio, not as a claim.

Problems referring to [`../code/ode_solvers.py`](../code/ode_solvers.py) require
you to run it and report its actual output.

---

## ★ Foundational

**★1.** Take $y' = -3y$, $y(0) = 2$.

(a) Write the exact solution and evaluate it at $t = 0.1$.
(b) Take one forward Euler step with $h = 0.1$ and compute the exact error.
(c) Compute the local truncation error $\tfrac{h^2}{2}y''(0)$ and compare its
magnitude with the error of (b), stating why the two are not equal.
(d) Integrate to $t = 1$ with $n = 10, 20, 40$ Euler steps and measure the order
from the error sequence.
(e) State the amplification factor $|1 + z|$ at $h = 0.1$ and confirm the
iteration is stable.

---

**★2.** Compute the stability function of Heun's method.

(a) Apply one Heun step to $y' = \lambda y$ and show that
$R(z) = 1 + z + z^{2}/2$.
(b) Evaluate $R$ at $z = -2.5$, $-2.2$, $-2.0$, $-1.9$ and $0$.
(c) Hence state the stability interval and compare it with forward Euler's.
(d) State in one sentence why a second-order method has the same real-axis
stability limit as the first-order method it improves on.

---

**★3.** For backward Euler $R(z) = 1/(1-z)$ and for the trapezoidal rule
$R(z) = (1 + z/2)/(1 - z/2)$:

(a) Evaluate both at $z = -10$, $-100$, $-1000$ and $-10^{6}$.
(b) Show algebraically that $|R(z)| \le 1$ for every $\mathrm{Re}\,z \le 0$ for
both methods.
(c) Hence state which of the two is L-stable, with the limiting value as
$z \to -\infty$ as the evidence.

---

**★4.** A stiff problem has $\lambda = 50\ \mathrm{s^{-1}}$ and is integrated over
$t \in [0, 1]$ with forward Euler.

(a) State the stability limit on $h$ and the corresponding minimum number of
steps.
(b) At $n = 25$ steps, compute the first two iterates from $y(0) = 1$ and the
error of the first one.
(c) Compute $n = 20, 22, 25, 26$ and report the maximum error on $[0,1]$ for each,
together with the per-step multiplier $|1 - \lambda h|$.
(d) Explain, from the multiplier, why the $n = 25$ run is bounded but useless.

---

## ★★ Applied

**★★5.** Derive the amplification factor of the implicit trapezoidal rule.

(a) Write the one-step update for $y' = \lambda y$ and solve it for
$y_{n+1}/y_n$.
(b) Show $|R(z)|\le 1$ on the closed left half-plane and give $\lim_{z\to-\infty} R(z)$.
(c) Tabulate $R(z)$ at $z = -0.5, -2, -10$ on the negative real axis.
(d) Explain the ringing of §3.3 at $h = 0.5$ in terms of (b) and (c), using the
lesson's measured errors $7.253\times10^{-1}$ (trapezoidal) against
$4.863\times10^{-3}$ (backward Euler).

---

**★★6.** The two-step Adams–Bashforth method is
$y_{n+1} = y_n + \tfrac{h}{2}\left(3f_n - f_{n-1}\right)$.

(a) Show it is order 2 by substituting the exact solution and expanding.
(b) Form the characteristic polynomial for $y' = \lambda y$ and identify the two
roots: the principal (physical) one and the spurious (computational) one.
(c) Evaluate both root moduli at $z = -0.5$, $-0.9$, $-1.0$, $-1.1$ and hence
locate the stability interval.
(d) Compare the interval with Heun's $[-2, 0]$ and state the practical
consequence for a stiff problem.

---

**★★7.** A code integrates a problem whose Jacobian has an eigenvalue
$\lambda = -2\times10^{4}\ \mathrm{s^{-1}}$ using classical RK4 with
$h = 10^{-3}$ s.

(a) Compute $z = h\lambda$ and $R(z) = 1 + z + z^{2}/2 + z^{3}/6 + z^{4}/24$ at
that $z$.
(b) State whether the run is stable and by what factor round-off grows per step.
(c) Compute the RK4 real-axis stability limit (the $z$ at which $|R(z)| = 1$) and
the largest stable $h$.
(d) Explain why the answer to (b) cannot be inferred from the local truncation
error, and give the growth expected over 1000 steps.

---

**★★8.** Reproduce the adaptive failure of §3.5 conceptually.

(a) State exactly what the step-doubling estimator measures and what error model
it assumes.
(b) Explain why the estimator underestimates the error when $\lambda h$ is of
order 1, naming the two competing error terms.
(c) The measured error fell as $\mathrm{tol}^{0.49}$, $0.52$ on the stiff
problem. State what exponent the estimator's model predicts and what the measured
exponent therefore implies about which term dominates.
(d) State the remedy and the reason a smaller safety factor is not one, using the
lesson's uniform-RK4 step counts ($128$ steps for $10^{-6}$).

---

## ★★★ Research-oriented

**★★★9.** A semi-implicit scheme for the damped oscillator
$m\ddot x + c\dot x + kx = 0$ is implicit in the damping and explicit in the
restoring force:

$$v_{n+1} = \frac{v_n - h\omega_0^{2}x_n}{1 + 2\zeta\omega_0h}, \qquad
x_{n+1} = x_n + h\,v_{n+1}, \qquad \omega_0^{2} = k/m,\quad
2\zeta\omega_0 = c/m .$$

(a) Write the $2\times2$ update matrix and show its determinant is
$(1 + \omega_0^{2}h^{2})/(1 + 2\zeta\omega_0h)$.
(b) Show that when the eigenvalues are complex the stability condition is
$\det \le 1$, and hence derive the exact stability limit
$h \le 2\zeta/\omega_0$.
(c) Evaluate that limit for $m = 1$ kg, $c = 0.4$ N s m$^{-1}$, $k = 25$ N m$^{-1}$
and compare it with the limit $2/\omega_0$ of the fully explicit scheme.
(d) Integrate to $t = 2$ s at $n = 50, 100, \ldots, 800$ with $x(0) = 1$,
$v(0) = 0$ and measure the order from the error sequence.
(e) State the trade-off: what did the implicitness buy, and what did it cost?

---

**★★★10.** A geothermal forward model is reported to run with explicit Euler at a
step of one year, on a system whose fastest relaxation time is one month.

(a) Compute $\lambda$, the stability limit $h_{\max} = 2/\lambda$ in months, and
the dimensionless product $\lambda h$ for the reported step.
(b) Predict the growth factor per step and the growth after 5, 20 and 100 steps.
(c) State the observed behaviour a diagnostic plot would show, and say why a
steady-state-looking answer at early times is not evidence of stability.
(d) Solve the relaxation $T' = -k(T - T_s)$ with $k = 1/(30\ \text{days})$,
$T(0) = 12$ °C, $T_s = 8$ °C at the reported step both explicitly and with
backward Euler for 100 years, and compare with the analytic answer.
(e) State the two remedies in order of preference with their costs.
