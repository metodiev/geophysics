# Exercises — 01-07-02 Matrices, Matrix Multiplication and Linear Maps

Attempt these **closed-book**, on paper, before opening the
[solutions](./02-matrices-and-operations-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** With $A = \begin{bmatrix} 2 & 1 \\ 0 & 3\end{bmatrix}$ and
$B = \begin{bmatrix} 1 & -1 \\ 4 & 2\end{bmatrix}$, compute $AB$ and $BA$ and confirm
that they differ. Then give a $2\times2$ example, other than a scalar multiple of the
identity, for which $AB = BA$.

---

**★2.** A two-layer refraction experiment gives, in seconds,

$$t_1 = 0.4\,s_1 + 0.6\,s_2, \qquad t_2 = 0.5\,s_1 + 0.5\,s_2,$$

with $s_i$ in $\mathrm{s/km}$.

(a) Write the system as $d = Gm$ and state the units of every entry of $G$.
(b) Which ray has more influence on the second layer, and by how much?
(c) Compute $\det G$ and say what it means geometrically.
(d) What model perturbation produces no change in either travel time? Verify by
matrix–vector multiplication.

---

**★3.** Build the $5\times5$ central-difference matrix $D$ on a uniform grid with
spacing $h$ on the interval $[0,4h]$, using one-sided differences in the first and
last rows.

(a) Write $D$ out with the factors of $1/h$ made explicit.
(b) Verify that $D\mathbf{1} = \mathbf{0}$.
(c) Compute $\operatorname{rank}D$ and give a basis of its null space.
(d) Compute $D(0,1,2,3,4)^\mathsf{T}$ and $D(5,6,7,8,9)^\mathsf{T}$ and explain why
the answers are identical, without appealing to the null-space calculation.
(e) A GPS network measures a strain rate from velocity gradients. State, in one
sentence, what the null space of $D$ means for that measurement.

---

## ★★ Applied

**★★4.** Let $R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta &
\cos\theta\end{bmatrix}$.

(a) Show that $R(\theta)R(\phi) = R(\theta+\phi)$ by direct multiplication.
(b) Show that $R(\theta)^{-1} = R(-\theta) = R(\theta)^\mathsf{T}$.
(c) Compute $\det R(\theta)$ and explain why orthogonality forces that value.
(d) Give $\|R(\theta)x\|$ for arbitrary $x$ and explain in one sentence what physical
property of a rotation this expresses.

---

**★★5.** For a horizontal reflector at depth $h$ with constant velocity $v$ above it,
the two-way travel time at source–receiver offset $x$ is
$T(x) = \sqrt{x^{2}+4h^{2}}/v$. Take $(h, v) = (1.2\ \mathrm{km},\ 3.7\
\mathrm{km/s})$ and offsets $x = 0, 1, 2, 3, 4, 5$ km.

(a) Write the $6\times2$ Jacobian $J$, with the units of each column.
(b) Verify that $J\ \delta$ reproduces the true change in travel time to second order
in $\delta$ for $\delta = (0.01\ \mathrm{km},\ 0.01\ \mathrm{km/s})$: compute the
linear prediction and the exact change.
(c) Compute $J^\mathsf{T}J$, its determinant, and $\kappa_2(J)$.
(d) State whether these six offsets determine $h$ and $v$ separately, and support the
answer with a number.

---

**★★6.** The $5\times5$ smoothing matrix of the lesson is
$C$ with rows $(0.25, 0.5, 0.25)$ shifted along the diagonal.

(a) Verify that $\|C\|_\infty = 1$ and hence $\|C\|_2 \le 1$, and state which rows
achieve the bound.
(b) Compute $\det C$ exactly and explain why it is small but nonzero.
(c) Compute the eigenvalues of $C$ and identify the largest. Give the largest
eigenvalue in closed form if you can.
(d) Apply $C$ a hundred times to the trace $(1, 2, 4, 3, 1.5)$ and report the result.
(e) Explain the connection between the repeated smoothing of (d) and the null space
of the derivative operator of ★3.

---

## ★★★ Research-oriented

**★★★7.** A processing chain consists of a rotation into an anisotropic frame
$R(\theta)$, a directional gain $S = \operatorname{diag}(1, 2)$, and a subsequent
rotation back $R(-\theta)$.

(a) Write the composite matrix $M = R(-\theta)SR(\theta)$ and compute it for
$\theta = 30^{\circ}$.
(b) Verify that $M$ is symmetric and that its eigenvalues are $1$ and $2$, with
eigenvectors along the rotated axes. Explain why reducing the composition to two
numbers (the eigenvalues) loses no information here.
(c) Show that the trace and determinant of $M$ are independent of $\theta$, and
verify numerically at $\theta = 0^{\circ}$ and $30^{\circ}$.
(d) Now replace $S$ by a general non-symmetric matrix and state, with a numerical
counterexample, whether $M$ is still symmetric.

---

**★★★8.** A data kernel for a reflection survey is built as a $2\times2$ matrix whose
rows are two rays with path lengths $(1,1)$ and $(1, 1+\delta)$ km, and a model
parameterisation is changed by scaling the first model parameter by $10^{3}$ (for
instance, measuring it in metres instead of kilometres).

(a) Write the transformed kernel.
(b) Show by explicit computation that the two kernels represent the same physical
experiment.
(c) Compute $\det$ of both kernels for $\delta = 0.01$, and state the ratio.
(d) Compute $\kappa_2$ of both and state the ratio.
(e) Explain which of the two changed, why the other did not, and which of the two is
the honest measure of the difficulty of the experiment.

