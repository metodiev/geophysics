# Exercises — 01-08-04 Systems of ODEs, Phase Portraits and Stability

Attempt these **closed-book** before opening the
[solutions](./04-systems-of-odes-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [04 Systems of ODEs](../04-systems-of-odes.md).

---

## ★ Foundational

**★1.** For each matrix compute $T$, $D$, $T^{2}-4D$, the eigenvalues, and the
name of the portrait. State whether the equilibrium is asymptotically stable,
stable, or unstable.

(a) $\begin{pmatrix}-1 & 0.5\\ 0.5 & -1\end{pmatrix}$
(b) $\begin{pmatrix}-2 & 1\\ -4 & -1\end{pmatrix}$
(c) $\begin{pmatrix}0.5 & 1\\ 1 & 0.5\end{pmatrix}$
(d) $\begin{pmatrix}0 & 4\\ -1 & 0\end{pmatrix}$
(e) $\begin{pmatrix}3 & 0\\ 0 & -2\end{pmatrix}$

---

**★2.** Reduce $x'' + 2\zeta\omega_0x' + \omega_0^{2}x = 0$ to a first-order
system and show that the eigenvalues of the system matrix are the roots of the
characteristic equation.

---

**★3.** For the Lotka–Volterra system $\dot x = ax - bxy$,
$\dot y = -cy + dxy$ with $a = 1$, $b = 0.5$, $c = 0.8$, $d = 0.4$:

(a) Find the non-trivial equilibrium and verify it by substitution.
(b) Compute the Jacobian there, its trace, determinant, and eigenvalues.
(c) State the portrait and, from the linearisation alone, whether the
equilibrium attracts.

---

## ★★ Applied

**★★4.** A two-box surface/deep-ocean energy balance model with unequal heat
capacities $C_1 = 1$, $C_2 = 2$ is

$$C_1\dot T_1 = -\lambda T_1 + \gamma(T_2-T_1), \qquad
C_2\dot T_2 = \gamma(T_1-T_2),$$

with $\lambda = 1$ and $\gamma = 0.5$.

(a) Write the matrix for the perturbation problem and compute $T$, $D$ and the
eigenvalues.
(b) Give the two relaxation timescales and identify which physical process each
corresponds to.
(c) Compute the eigenvector of the slow mode and interpret its components
physically.

---

**★★5.** For the saddle
$A = \begin{pmatrix}0.3 & 0.2\\ 0.2 & -0.1\end{pmatrix}$:

(a) Find both eigenvectors, normalised.
(b) Starting from $(0.01, 0)$ and from $(-0.01, 0)$, determine by the eigenvector
expansion where each trajectory ends up as $t\to\infty$, including the sign.
(c) State what the stable eigenvector means physically and what it is called.

---

**★★6.** Prove the Lyapunov result of the lesson for the equal-capacity
two-box model, $A = \begin{pmatrix}-(\lambda+\gamma) & \gamma\\ \gamma &
-\gamma\end{pmatrix}$ with $\lambda = 1.2$, $\gamma = 0.8$:

(a) Write $V = \tfrac12(T_1^{2}+T_2^{2})$ and compute $\dot V$ in the form
$-\mathbf{T}^{\top}Q\mathbf{T}$.
(b) Apply Sylvester's criterion and conclude.
(c) State what the result adds beyond the linear-stability conclusion from the
eigenvalues.

---

## ★★★ Research-oriented

**★★★7.** Consider the logistic-prey, mass-action predator–prey system

$$\dot x = ax\left(1-\frac{x}{K}\right) - bxy, \qquad \dot y = -cy + dxy .$$

(a) Show that at the interior equilibrium the Jacobian trace is exactly
$T = -ac/(dK)$, for all positive $a,b,c,d,K$, and deduce that no Hopf
bifurcation can occur from this equilibrium.
(b) Now replace the predation term by the saturating form $bxy/(1+hx)$ and show
that the trace becomes $T = x^{*}\left[-a/K + bhy^{*}/(1+hx^{*})^{2}\right]$.
(c) With $a = b = d = 1$, $c = 0.4$, $h = 0.5$, find the value of $K$ at which
$T = 0$ exactly, and verify that $T>0$ for $K = 5$.
(d) State in two sentences why (a) and (c) together are a warning about model
choice, not merely about algebra.

---

**★★★8.** A forcing term is added to the two-box model of ★4:
$\dot{\mathbf{T}} = A\mathbf{T} + \mathbf{F}$ with $\mathbf{F}$ constant.

(a) Find the new equilibrium $\mathbf{T}^{*}$ in terms of $A^{-1}$ and
$\mathbf{F}$, and compute it for $\mathbf{F} = (1,0)$.
(b) Show that the Jacobian of the forced problem is unchanged, so the stability
of the equilibrium is the same. State the general principle this illustrates.
(c) Integrate numerically (or reason analytically) to estimate the time at which
the surface temperature has covered 63 % of the way from its initial value to
$\mathbf{T}^{*}$, and identify which mode dominates that time.
(d) If $F_2 \neq 0$ in the second component instead, does your answer to (a)
change in sign or only in magnitude? Explain.

---

## Extension ideas

- Derive the trace–determinant classification for a $2\times2$ matrix from
  $\lambda_1+\lambda_2 = T$ and $\lambda_1\lambda_2 = D$ without quoting it.
- For the conservative Lotka–Volterra system, show by direct substitution that
  $H = dx - c\ln x + by - a\ln y$ is constant along trajectories, and identify
  where the logarithm terms come from.
- Investigate numerically what forward Euler does to the Lotka–Volterra
  invariant $H$ over 100 time units, and compare with RK4. Explain the direction
  of the drift.
