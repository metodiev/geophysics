# Exercises — 01-07-01 Vectors, Vector Spaces and Basis

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-vectors-and-spaces-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** For $a = (2,-1,2)$ and $b = (1,3,-2)$ compute $\|a\|$, $\|b\|$,
$\langle a,b\rangle$, the angle between them, $\|a+b\|$ and $\|a-b\|$. Verify the
Cauchy–Schwarz inequality and the parallelogram identity
$\|a+b\|^{2} + \|a-b\|^{2} = 2\|a\|^{2} + 2\|b\|^{2}$.

---

**★2.** Which of these sets are vector spaces over $\mathbb{R}$? Justify each in one
line.

(a) $\{(x,y,z) : x + 2y - z = 0\}$
(b) $\{(x,y,z) : x + 2y - z = 1\}$
(c) the $2\times2$ real matrices of zero trace
(d) the invertible $2\times2$ real matrices
(e) the velocity profiles $v(z) = a + bz$ on $[0,1]$

---

**★3.** Two candidate directions at a station are $v_1 = (1,0,0)$ and
$v_2 = (1,1,0)$ in (N, E, Z). (a) Compute the angle between them. (b) Normalise both
and verify the normalised pair has unit length. (c) Are they independent? Give the
reason in one sentence.

---

## ★★ Applied

**★★4.** A three-component recording gives $\mathbf{u} = (1.2, 0.9, -1.4)$ in
(N, E, Z), in counts.

(a) Compute $\|\mathbf{u}\|$, the incidence angle from the vertical, and the back
azimuth (clockwise from north).
(b) The horizontal components are rotated by $40^{\circ}$ clockwise; give the new
triple and verify the horizontal magnitude is unchanged.
(c) State which of the quantities in (a) are invariant under that rotation and which
are not, and why.
(d) How many independent physical quantities does this one sample contain?

---

**★★5.** Orthonormalise $v_1 = (1,1,1)$, $v_2 = (1,-1,0)$, $v_3 = (0,1,-1)$ by
Gram–Schmidt.

(a) Report the residual norm $\|w_j\|$ at each of the three steps.
(b) Verify orthonormality by computing all six inner products.
(c) Compute the coordinates of $c = (1,2,3)$ in the new basis and reconstruct it.
(d) What does the smallest residual norm tell you about the conditioning of the set?
(e) Comment on the fact that $\langle v_1, v_2\rangle = 0$ and
$\langle v_1, v_3 \rangle = 0$ but $\langle v_2, v_3 \rangle = -1$.

---

**★★6.** A ray-path kernel has rows $r_1 = (1,1,0)$, $r_2 = (1,1,0.001)$ and
$r_3 = (0,0,1)$ (path lengths in km).

(a) Are the three rows independent? Justify.
(b) For which $\delta$ in $r_2 = (1,1,\delta)$ do the rows become dependent?
(c) Using the angle between $r_1$ and $r_2$ as a diagnostic, compute it for
$\delta = 0.001$ and for $\delta = 0$. Explain why the diagnostic is
ill-conditioned near $\delta = 0$ and propose a stable alternative.
(d) Interpret the result as a statement about a three-ray, three-cell survey.

---

## ★★★ Research-oriented

**★★★7.** Three parameterisations of the same 2-D model space share a set of basis
vectors:

$$A = \{(1,0),\ (0,1)\}, \qquad B = \{(1,0.5),\ (0,1)\}, \qquad
C = \{(1,1)/\sqrt2,\ (1,-1)/\sqrt2\}.$$

The model is $m = (0.05,-0.02)$ $\mathrm{s/km}$.

(a) Give the coordinates of $m$ in all three bases and verify the reconstruction in
each.
(b) Compute $\|m\|$ once, and the Euclidean norm of the coordinate triple in each
basis. Which agree with $\|m\|$ and which do not, and what distinguishes them?
(c) A regularisation term penalises $\|c\|^{2}$ where $c$ are the coordinates in the
basis used. Compute the penalty for the same model in each basis, report all three
values, and explain why they differ.
(d) Show that $\|c\| = \|m\|$ holds for all $m$ if and only if the change-of-basis
matrix is orthogonal.
(e) Rank the three bases for a prior belief that "the two cells are probably perturbed
in opposition", and justify your ranking in two sentences each.

---

**★★★8.** Reproduce the rank-versus-$\delta$ experiment of the lesson: take
$v = (1,1,0)$ and $w = (1, 1+\delta, 0)$ and decide numerical independence from the
residual norm after projecting $w$ off $v$.

(a) Show analytically that the perpendicular component has norm $\delta/\sqrt2$.
(b) For tolerances $10^{-8}$, $10^{-12}$ and $10^{-15}$, report the value of $\delta$
at which the numerical rank changes, and compare with the prediction $\delta =
\sqrt2\,\text{tol}$.
(c) The angle between $v$ and $w$ has exact value $\arcsin(\delta/\sqrt2)$ for small
$\delta$. Compute it for $\delta = 10^{-9}$ in degrees, and compare with the value
$\arccos(\langle v,w\rangle/\|v\|\|w\|)$ computed in floating point. Report both and
explain the discrepancy.
(d) Rewrite the angle computation in a numerically stable way and show that the
discrepancy disappears.
(e) State the practical rule you would put in a code-review comment about rank
decisions.

