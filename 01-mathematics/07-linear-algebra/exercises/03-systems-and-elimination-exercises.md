# Exercises — 01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation

Attempt these **closed-book**, on paper, before opening the
[solutions](./03-systems-and-elimination-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Solve by Gaussian elimination with partial pivoting, showing the augmented
matrix at each step:

$$2x + y = 5, \qquad x + 3y = 10 .$$

Report the multipliers, the pivots and $\det A$. State the row picture and the column
picture of the same system.

---

**★2.** The lesson's tomography system is $Gm = d$ with

$$G = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2\end{bmatrix}
\ \text{km}, \qquad d = \begin{bmatrix} 0.080 \\ 0.110 \\ 0.180\end{bmatrix}
\ \text{s}.$$

(a) Delete the third ray and solve the resulting $2\times2$ system for the first two
cells.
(b) Compare with the true model $(0.05, -0.02, 0.10)$ $\mathrm{s/km}$ and state, in one
sentence, what the third ray contributed.
(c) Now delete the third *cell* as well (solve for cell 1 only from ray 1) and comment
on whether that system is even determined.

---

## ★★ Applied

**★★3.** Factorise
$A = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 3 & 1 & 1\end{bmatrix}$ as $PA = LU$
with partial pivoting.

(a) Report $P$, $L$ and $U$, with the multipliers visible in $L$.
(b) Verify $PA = LU$ numerically and report $\max|PA - LU|$.
(c) Report the pivots and hence $\det A$, including the sign.
(d) State which entries of $L$ would have been larger than one without pivoting, and
why that matters.

---

**★★4.** Let $A = \begin{bmatrix} \epsilon & 1 \\ 1 & 1\end{bmatrix}$ with
$\epsilon = 10^{-8}$ and $b = (1, 2)^\mathsf{T}$.

(a) Solve exactly by hand, keeping the terms in $\epsilon$.
(b) Solve by unpivoted elimination in double precision. Report the multiplier and the
relative error of each component.
(c) Redo with partial pivoting. Report the multiplier and the relative error.
(d) Explain the difference in terms of the multiplier magnitude and the growth factor.

---

**★★5.** A survey accumulates data in three batches, each giving a $1000\times1000$
system with the *same* kernel $G$ and different right-hand sides.

(a) Count the multiply-adds for three separate eliminations, using
$n^{3}/3 + n^{2}/2$ per elimination.
(b) Count the multiply-adds for one $LU$ factorisation plus three pairs of triangular
solves, using $n^{2}$ per pair of solves.
(c) Report the ratio and the saving factor.
(d) Repeat at $n = 10$, $100$, $10^{4}$ and state the limiting saving as
$n \to \infty$, with a one-sentence explanation of why it is not larger.

---

## ★★★ Research-oriented

**★★★6.** Construct a $3\times3$ system whose unpivoted elimination succeeds in exact
arithmetic but loses at least six digits in double precision, while partial pivoting
retains essentially all digits.

(a) Give the matrix and the right-hand side, and the exact solution.
(b) Report the multipliers in each case.
(c) Report the relative error of each component of the solution for each route.
(d) Explain, in terms of the growth factor, how the example achieves the effect, and
state the condition on the matrix that makes it work.
(e) State whether partial pivoting *guarantees* small error for every matrix, and
support your answer with the name of a counterexample family.

---

**★★★7.** Residual versus error, measured. For
$G = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta\end{bmatrix}$ with
$m_{\text{true}} = (0.05, -0.02)$ $\mathrm{s/km}$, perturb the second datum by a
relative $10^{-3}$.

(a) For $\delta = 10^{-2}, 10^{-3}, 10^{-4}$ compute the exact solution, the model
error, and the residual $\|G\hat m - d\|$.
(b) Report the table and confirm that the residual is at round-off level in every row.
(c) Compute $\kappa_2(G)$ for each $\delta$ and state how the model error tracks it.
(d) Explain in one paragraph why a small residual cannot detect this failure, and what
diagnostic would.
(e) State which of $(G, d)$ contains the information needed for the diagnosis.
