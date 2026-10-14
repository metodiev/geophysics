# Exercises — 01-07-10 Matrix Calculus and Sensitivity Derivatives

Attempt these **closed-book**, on paper, before opening the
[solutions](./10-matrix-calculus-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Differentiate with respect to $x$ and state the dimensions of each answer:

(a) $a^\mathsf{T}x$ with $a = (2,-1,3)$;
(b) $x^\mathsf{T}Ax$ with $A = \begin{bmatrix} 1 & 2 \\ 0 & 1\end{bmatrix}$;
(c) $\|x\|^{4}$;
(d) $b^\mathsf{T}Ax$ with $b = (1,1)$ and $A$ of compatible shape.

---

**★2.** Derive $\nabla_m\tfrac12\|Gm - d\|^{2} = G^\mathsf{T}(Gm - d)$ by writing the
components out explicitly and differentiating with respect to $m_k$. Then derive the
regularised normal equations for a penalty $\alpha\|Dm\|^{2}$.

---

## ★★ Applied

**★★3.** A gravity station sits at horizontal offset $x$ from a buried sphere of radius $R$
and density contrast $\Delta\rho$ at depth $z$ to its centre. In the point-mass limit
(valid when $R \ll z$) the vertical gravity anomaly is

$$g_z = \frac{4\pi G \Delta\rho R^{3}}{3}\cdot\frac{z}{(x^{2}+z^{2})^{3/2}} .$$

(a) Compute $\partial g_z/\partial z$ and $\partial g_z/\partial R$ in closed form, and
state the units of each.
(b) Evaluate both at $x = 0$, $z = 2$ km, $R = 0.5$ km, $\Delta\rho = 500$
$\mathrm{kg\,m^{-3}}$, with $G = 6.674\times10^{-11}$ SI, and report $g_z$ in mGal.
(c) State which parameter the single measurement constrains better in absolute terms, and
by what factor.
(d) Compute the ratio $\delta z/\delta R$ of changes that leave $g_z$ unchanged, and
explain why one measurement cannot determine both parameters.
(e) Confirm that the point-mass limit is adequate for this geometry by computing the ratio
$z/R$, and state the order of the neglected term.

---

**★★4.** A one-parameter nonlinear model $F(m) = e^{m}$ is fitted to a single datum
$d = 20$.

(a) Write the residual, the misfit and the derivatives $F'(m)$, $F''(m)$.
(b) Give the exact Newton step and the Gauss–Newton step from $m_0 = 0$ in closed form.
(c) Iterate both to convergence and report the sequences.
(d) State the condition on the residual under which the Gauss–Newton step is a good
approximation, and check whether it holds at $m_0 = 0$ for this datum.

---

## ★★★ Research-oriented

**★★★5.** Implement and verify an adjoint. Take the one-dimensional steady diffusion
problem

$$A(m)u = f, \qquad A = \text{tridiagonal with layer diffusivities},$$

with objective $\phi(m) = \tfrac12\|Su - d\|^{2}$ where $S$ samples a subset of nodes.

(a) Write down the adjoint system that computes $\nabla_m\phi$.
(b) State the dot-product test that verifies an adjoint implementation, and give the exact
statement you would code.
(c) State how many linear solves the adjoint gradient needs, as a function of the number
of parameters, and compare with an explicit Jacobian.
(d) Explain why the adjoint gradient is *not* the same as "solving the forward problem
backwards" in general, and state what it is instead.
(e) State two numerical tests you would run before trusting the gradient in an inversion.

---

**★★★6.** Design a two-parameter experiment whose Jacobian is nearly singular, and quantify
the trade-off.

(a) Choose a physical parameterisation and a set of measurements such that two Jacobian
columns have a cosine above $0.999$.
(b) Report the singular values, the condition number and the angle between the columns.
(c) With a measurement uncertainty of 1 % of the datum, report the standard deviation of
each parameter and of the difference combination.
(d) State what additional measurement would eliminate the trade-off, quantify the
improvement, and state whether the improvement is worth the cost.
