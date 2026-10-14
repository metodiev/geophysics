# Exercises — 01-07-05 Determinants, Inverses and Matrix Conditioning

Attempt these **closed-book**, on paper, before opening the
[solutions](./05-determinants-inverses-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** For $A = \begin{bmatrix} 3 & 1 \\ 2 & 4\end{bmatrix}$ compute the determinant,
the adjugate (the transposed matrix of cofactors), and the inverse; verify
$AA^{-1} = I$ by hand.

---

**★2.** For $B = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 2 & 1 & 1\end{bmatrix}$
compute $\det B$ by (a) cofactor expansion along the first row and (b) elimination with
pivots. Confirm that the two agree, and state the number of row swaps and the sign.

---

## ★★ Applied

**★★3.** A two-station, two-layer experiment gives
$G = \begin{bmatrix} 1 & 1 \\ 1 & 1.05\end{bmatrix}$ km with a travel-time uncertainty
of $0.5$ ms.

(a) Compute $\kappa_2(G)$ and $\det G$.
(b) Give the worst-case relative model error for a relative data error of $10^{-3}$.
(c) Express the same physical experiment with distances in metres, so
$G' = \begin{bmatrix} 1000 & 1000 \\ 1000 & 1050\end{bmatrix}$. Compute $\kappa_2(G')$
and $\det G'$ and state which changed and by how much.
(d) If the second station could be moved so that the path lengths become $(1, 1.5)$,
compute the new $\kappa_2$ and the reduction factor.

---

**★★4.** Explain, with explicit numbers, why $\kappa_2(G^\mathsf{T}G) =
\kappa_2(G)^{2}$ makes the normal equations unusable once
$\kappa_2(G) > 6.7\times10^{7}$.

(a) State the general argument in three lines.
(b) For the two-ray geometry $G = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta\end{bmatrix}$,
give the value of $\delta$ at which $\kappa_2(G^\mathsf{T}G)$ first exceeds
$1/\epsilon_{\text{mach}}$ in double precision.
(c) Verify your answer numerically by computing $\kappa_2(G)$ and $\kappa_2(G^\mathsf{T}G)$
at $\delta = 10^{-7}$ and $\delta = 10^{-8}$.
(d) State what happens numerically, rather than merely quantitatively, when the
threshold is crossed.

---

## ★★★ Research-oriented

**★★★5.** Equilibration. Let
$A = \begin{bmatrix} 10^{3} & 1 \\ 1 & 1.001\times10^{-3}\end{bmatrix}$.

(a) Compute $\kappa_2(A)$ and $\det A$.
(b) Scale each row by the reciprocal of its largest absolute entry, then each column by
the reciprocal of its largest absolute entry. Give the resulting matrix and its
$\kappa_2$.
(c) State the reduction factor in $\kappa_2$.
(d) Does equilibration change the solution of a consistent system $Ax = b$? Prove your
answer.
(e) State what equilibration does change, and why that matters for a parameterised
inverse problem.

---

**★★★6.** Design and run a numerical experiment measuring the relative error of the
solution of $G(\delta)m = d$ as a function of $\delta$, for
$G(\delta) = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta\end{bmatrix}$ and
$m_{\text{true}} = (0.05,-0.02)$ $\mathrm{s/km}$.

(a) Define your perturbation protocol precisely (what you perturb, by how much, and
why that value).
(b) Tabulate the relative model error against $\delta$, $\kappa_2(G)$ and
$\kappa_2(G)\epsilon_{\text{mach}}$.
(c) Report the $\delta$ at which all digits are lost, and compare with the prediction.
(d) State the $\delta$ at which the experiment fails in a different way — the matrix
becoming exactly singular in floating point — and explain the mechanism.
(e) State the limits of your conclusion: does it depend on which datum you perturbed,
and on the value of $m_{\text{true}}$?

