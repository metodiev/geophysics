# Exercises — 05-03-04 Numerical Forward Modelling and Discretisation

Difficulty: ★ · ★★ · ★★★. Use the project virtual environment for the
computational parts.

---

## ★ Foundational

**★1.** Name the three error sources in a numerical forward model and state how
each responds to grid refinement.

**★2.** State the truncation error of the 5-point Laplacian and its order.

**★3.** Given errors $E_1 = 5.14\times10^{-4}$ at $h_1 = 0.025$ and
$E_2 = 1.29\times10^{-4}$ at $h_2 = 0.0125$, compute the convergence order.

---

## ★★ Applied

**★★4.** Write down the manufactured solution $u = \sin\pi x\sin\pi y$ and
derive the source term $b = -\nabla^2u$.

**★★5.** For the explicit diffusion scheme, state the stability condition and
compute the maximum time step for $D = 7.9577\times10^{5}$ m²/s and
$dz = 251.6$ m.

**★★6.** A refinement study shows relative errors $1.2\times10^{-2}$,
$1.5\times10^{-4}$, $3.6\times10^{-8}$, $8.5\times10^{-15}$,
$4.0\times10^{-15}$ at $n = 4, 8, 16, 32, 64$. Identify the convergence regime
and the round-off floor, and state the largest useful $n$.

---

## ★★★ Research-oriented

**★★★7.** Implement a Poisson solver with the 5-point stencil for the
manufactured solution on the unit square, measure the order over four grids, and
report the fitted slope with a stated tolerance. Then change one coefficient in
the stencil by 1% and report the new measured order. Explain why the order
collapses, and why that makes the order test a sensitive bug detector.

**★★★8.** Error budget. For a gravity forward model of a prism, construct a
table separating modelling error (point-mass approximation versus the exact prism
formula), discretisation error (quadrature node count) and round-off, at three
depths. Report which term dominates at each depth and state the practical
tolerance you would adopt for each regime. Justify each number.
