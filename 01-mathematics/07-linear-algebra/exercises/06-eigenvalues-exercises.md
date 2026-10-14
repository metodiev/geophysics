# Exercises — 01-07-06 Eigenvalues, Eigenvectors and Diagonalisation

Attempt these **closed-book**, on paper, before opening the
[solutions](./06-eigenvalues-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** For $A = \begin{bmatrix} 3 & 1 \\ 1 & 3\end{bmatrix}$:

(a) Write the characteristic polynomial and solve it.
(b) Find both eigenvectors and verify that they are orthogonal.
(c) Confirm that the trace and determinant equal the sum and product of the eigenvalues.
(d) Verify $A = Q\Lambda Q^\mathsf{T}$ with an orthogonal $Q$.

---

**★2.** A two-dimensional strain tensor measured at a station is
$\epsilon = \begin{bmatrix} 2 & -1 \\ -1 & 1\end{bmatrix}\times10^{-4}$.

(a) Compute the principal strains, with units.
(b) Compute the principal directions and their bearings (clockwise from north).
(c) Compute the maximum shear strain.
(d) State whether the strain is isotropic, and justify from the eigenvalues.

---

## ★★ Applied

**★★3.** The stress tensor of the lesson is
$\sigma = \begin{bmatrix} 60 & -25 \\ -25 & 20\end{bmatrix}$ MPa with principal stresses
$\sigma_1 = 72.015621$ MPa and $\sigma_2 = 7.984379$ MPa.

(a) Compute the normal and shear traction on a plane whose normal is at $45^{\circ}$ to
the major principal axis.
(b) Verify by transforming the tensor into the frame of that plane:
$\sigma' = Q^\mathsf{T}\sigma Q$ with $Q$ the rotation by $45^{\circ}$ from the principal
frame, and read off $\sigma'_{11}$ and $\sigma'_{12}$.
(c) State the maximum value of the shear traction over all plane orientations, and at
what angle it occurs.
(d) Express both results as fractions of $(\sigma_1 - \sigma_2)$ and comment.

---

**★★4.** The Jacobi iteration matrix for a $2\times2$ system is
$B = -\begin{bmatrix} 0 & a \\ b & 0\end{bmatrix}$ with $a = 0.4$, $b = 0.9$.

(a) Compute the eigenvalues of $B$ and $\rho(B)$. Does Jacobi converge?
(b) Predict the number of iterations to reduce the error by $10^{-6}$ using the exact
formula $k = \ln(\text{tolerance})/\ln\rho$ and using the small-$\rho$-gap approximation
$k \approx p\ln 10/(1-\rho)$. Compare.
(c) Verify by iterating a $2\times2$ system of your choice with this iteration matrix.
(d) Repeat for $ab = 1.01$ and explain the outcome.

---

## ★★★ Research-oriented

**★★★5.** Consider the bilinear form $q(x) = x^\mathsf{T}Ax$ with
$A = \begin{bmatrix} 1 & c \\ c & 1\end{bmatrix}$.

(a) Compute the eigenvalues as functions of $c$ and sketch the two branches.
(b) For which $c$ is $A$ positive definite, positive semidefinite, indefinite?
(c) At the transition values of $c$, describe the set of minimisers of $q$ and connect
this with [01-07-04](../04-rank-and-nullspace.md).
(d) $A$ is the curvature matrix of a least-squares problem in two parameters. Translate
the transition into a statement about the experiment that produced the data.

---

**★★★6.** Verify the claim $\rho_{\text{GS}} = \rho_J^{2}$ for consistently ordered
matrices on two examples:

(i) the five-point Laplacian on a $4\times4$ interior grid;
(ii) a symmetric tridiagonal matrix with diagonal entries larger than the sum of the
off-diagonals, e.g. diagonal $4 + u_i$ with $u_i$ pseudo-random in $[0,1)$ and unit
off-diagonals.

(a) Report $\rho_J$ (exact, from the eigenvalues of the Jacobi matrix) and
$\rho_{\text{GS}}$ (measured from a converged iteration).
(b) Compare $\rho_{\text{GS}}$ with $\rho_J^{2}$ in each case and state the agreement.
(c) State which of the two examples is consistently ordered, and whether the relation
held in the other.
(d) State the limits of your empirical claim: what would you need to check to turn it
into a theorem, and what class of matrix would you expect to violate it?
