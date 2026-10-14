# Exercises — 01-16-03 Linear Operators, Adjoints and Compactness

Attempt these **closed-book** before opening the
[solutions](./03-operators-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $V$ and $W$ are Hilbert spaces with inner products
$\langle\cdot,\cdot\rangle$; $L^*$ is the adjoint with respect to those inner
products; $\lVert L\rVert = \sup_{\lVert f\rVert\le1}\lVert Lf\rVert$; the
discretised forward operator is $F$ and the misfit is $J(m) = \lVert Fm -
d\rVert^2$. State the inner product whenever an adjoint is computed.

---

## ★ Foundational

**★1.** Show that $\lVert L\rVert = \sup_{\lVert f\rVert\le1}\lVert Lf\rVert$
defines a norm on the space of bounded linear operators $V \to W$, and give the
identity that relates $\lVert L\rVert$ to $\lVert L^*\rVert$.

---

**★2.** For $(Kf)(x) = \int_0^1 k(x,y)f(y)\,dy$ on $L^2(0,1)$, compute the adjoint
kernel. State the condition on $k$ for $K$ to be self-adjoint, and give one
geophysical kernel that satisfies it and one that does not.

---

**★3.** Define compactness for a linear operator and state its equivalence with
the decay of the singular values. Explain why the identity operator on an
infinite-dimensional Hilbert space is not compact.

---

## ★★ Applied

**★★4.** Derive the adjoint of $L = -d^2/dx^2$ on $(0,1)$ under the Robin
condition $u'(0) = hu(0)$ and $u(1) = 0$, including the boundary terms. Is $L$
self-adjoint? What changes if the boundary condition is replaced by
$u(0) = 0$, $u'(1) = g$?

---

**★★5.** Show that the orthogonal projection onto a closed subspace is bounded
with norm 1. Show that a projection onto a finite-dimensional subspace is compact
and that the identity on an infinite-dimensional Hilbert space is not. Reconcile
this with the demonstration's table, in which the $n \times n$ identity has
$n$ singular values equal to 1 at every $n$.

---

**★★6.** Using the demonstration's table of contraction factors, verify that mode
$k$ contracts by $1 - \lambda_k/L$ per steepest-descent step and compute the
number of steps to reduce it by $10^{-3}$ for $k = 8$ and $k = 16$. Compare with
the reported values.

---

**★★7.** Write the dot-product test $\langle Ax,y\rangle -
\langle x,A^{\mathsf T}y\rangle$ for a general matrix and prove that the
discrepancy equals $\langle\delta A\,x,y\rangle$ when $A$ is perturbed to
$A + \delta A$. Hence predict how the test's failure grows with the size of a
single perturbed entry, and state why the test is a *necessary* but not a
*sufficient* check.

---

## ★★★ Research-oriented

**★★★8.** Repeat the rank-3 separable-kernel experiment of the demonstration with
amplitudes $a = (1, 0.9, 0.8)$ instead of $(1, 0.5, 0.2)$.

(a) State the eigenvalues of $K^{\mathsf T}K$ and the contraction factor of the
slowest retained mode.
(b) Predict the number of steepest-descent steps needed for that mode to reach
$10^{-3}$, then run it and report the iteration at which the model error reaches
the null-space norm.
(c) Explain why the data misfit reaches $10^{-29}$ while the model error does not
change from the null-space norm.

---

**★★★9.** Take the Gaussian kernel $K(x,y) = e^{-(x-y)^2/(2\sigma^2)}$ with
$\sigma = 0.1$ on 64 nodes, a two-Gaussian true model, and a fixed starting model.
Set $\tau = \alpha/L$ with $L = \lVert K^{\mathsf T}K\rVert$ and run 500
steepest-descent steps for $\alpha = 0.1, 0.25, 0.5, 0.75, 0.9, 1.0, 1.2$.

(a) Derive the stability limit for $\alpha$ from the iteration
$m_{j+1} = m_j - \tau\,\nabla J$.
(b) Report the model error and the misfit after 500 steps for each $\alpha$.
(c) Explain why the error keeps improving as $\alpha \to 1$ while the first mode
converged after one step, and why it then diverges.

---

**★★★10.** Write a short section for an inversion code's documentation that
specifies, for a weighted misfit $J = \lVert W^{1/2}(Fm - d)\rVert^2$:
(a) the gradient formula and why $F^{\mathsf T}$ alone is wrong; (b) the boundary
conditions of the adjoint and how they are inherited; (c) the dot-product test as
an automated check with a stated acceptance threshold; (d) the reason the
gradient is not the inverse and what must be added before a model is reported.
