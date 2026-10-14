# Solutions — 01-07-04 Rank, Null Space and Solvability

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified. Where a decomposition has an arbitrary
> sign (eigenvectors, null vectors), the sign chosen here is a convention.

---

## ★1 — Rank, null space and consistency

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1\end{bmatrix}.$$

(a) Row 2 $= 2\times$row 1, so eliminate it and reduce:

$$\begin{bmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & 0 & 0\end{bmatrix}
\;\longrightarrow\;
\text{RREF} = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 0\end{bmatrix}.$$

Pivot columns 1 and 2, so $\operatorname{rank}A = 2$; the free column is 3. Setting
$x_3 = 1$ gives $x_1 = 1$, $x_2 = -2$:

$$\mathcal{N}(A) = \operatorname{span}\{(1,-2,1)^\mathsf{T}\}, \qquad
A(1,-2,1)^\mathsf{T} = (1-4+3,\ 2-8+6,\ 1-2+1)^\mathsf{T} = \mathbf{0}. ✓$$

(b) Solve $A^\mathsf{T}\lambda = 0$:

$$\lambda_1 + 2\lambda_2 + \lambda_3 = 0, \quad 2\lambda_1 + 4\lambda_2 + \lambda_3 = 0,
\quad 3\lambda_1 + 6\lambda_2 + \lambda_3 = 0 .$$

Subtracting consecutive equations gives $\lambda_1 + 2\lambda_2 = 0$ twice, so
$\lambda_1 = -2\lambda_2$ and then $\lambda_3 = 0$:

$$\mathcal{N}(A^\mathsf{T}) = \operatorname{span}\{(-2,1,0)^\mathsf{T}\}.$$

The consistency condition is $\lambda^\mathsf{T}d = 0$, i.e. $-2d_1 + d_2 = 0$, or
**$d_2 = 2d_1$**.

(c) $d = (1,2,1)$: $d_2 = 2 = 2d_1$ ✓ **consistent** — uniqueness fails
(null space of dimension 1), existence holds. $d = (1,0,0)$: $0 \neq 2$ ✗
**inconsistent** — both failures, since the null space is the same regardless of $d$.

(d) Rank–nullity: model space, $r + \dim\mathcal{N}(A) = 2 + 1 = 3 = n$ ✓. Data space,
$r + \dim\mathcal{N}(A^\mathsf{T}) = 2 + 1 = 3 = m$ ✓.

---

## ★2 — The redundant-ray kernel

$$G = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1\end{bmatrix}, \qquad
\text{row}_3 = \text{row}_1 + \text{row}_2 .$$

(a) The left null space is $\operatorname{span}\{(1,1,-1)^\mathsf{T}\}$, so the
consistency condition is $d_1 + d_2 - d_3 = 0$, i.e. $d_3 = d_1 + d_2$.

- $d = (2,-1,1)$: $d_3 = 1$ and $d_1 + d_2 = 1$ ✓ **consistent**.
- $d = (2,-1,2)$: $d_3 = 2$ but $d_1 + d_2 = 1$ ✗ **inconsistent**.

(b) Attempting to solve the consistent case: $\operatorname{rank}([G \mid d]) = 2 =
\operatorname{rank}(G)$, and elimination leaves a consistent triangular system.
For the inconsistent case, eliminating the third row with row 3 − row 1 − row 2 gives
the equation $0 = 2 - 2 - (-1) = 1$, i.e. $0 = 1$: the classic inconsistent signature.

(c) Two distinct models fitting $d = (2,-1,1)$: the equations are
$m_1 + m_2 = 2$, $m_2 + m_3 = -1$ and $m_1 + 2m_2 + m_3 = 1$, the last being the sum of
the first two and therefore automatic. Choose $m_2 = 0$; then $m_1 = 2$ and $m_3 = -1$,
and

$$G(2,0,-1)^\mathsf{T} = (2,\ -1,\ 2 - 1)^\mathsf{T} = (2,-1,1)^\mathsf{T}. ✓$$

The general solution is $m = (2,0,-1) + \alpha(1,-1,1)$; taking $\alpha = 0.5$ gives
$m = (2.5,-0.5,-0.5)$, and

$$G(2.5,-0.5,-0.5)^\mathsf{T} = (2.5-0.5,\ -0.5-0.5,\ 2.5-1-0.5)^\mathsf{T}
= (2,\ -1,\ 1)^\mathsf{T}. ✓$$

Two members of the family, both exact, differing by $0.5$ $\mathrm{s/km}$ per cell.

**Practical note.** The safest way to produce a particular solution is to set the free
variables to zero and solve for the pivots from the reduced row echelon form, then
verify by multiplication. Deriving one from a single row and hoping is how sign errors
enter a worked solution.

---

## ★★3 — A four-ray, three-cell survey

$$G = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 1\end{bmatrix}.$$

(a) The first three rows are the identity, so $\operatorname{rank}G = 3$ and
$\mathcal{N}(G) = \{\mathbf{0}\}$: every model direction is seen. The third column is
also independent, so the rank cannot be less than 3.

(b) $\mathcal{N}(G^\mathsf{T})$: solve $G^\mathsf{T}\lambda = 0$, i.e.
$\lambda_1 + \lambda_4 = 0$, $\lambda_2 + \lambda_4 = 0$, $\lambda_3 + \lambda_4 = 0$:

$$\mathcal{N}(G^\mathsf{T}) = \operatorname{span}\{(-1,-1,-1,1)^\mathsf{T}\},$$

so the consistency condition is $-d_1 - d_2 - d_3 + d_4 = 0$, i.e.
**$d_4 = d_1 + d_2 + d_3$**.

(c) Singular values:

| kernel | singular values | $\kappa_2$ |
|---|---|---|
| three rays ($G = I$) | $(1, 1, 1)$ | $1.000000$ |
| four rays | $(2, 1, 1)$ | $2.000000$ |

The fourth ray **buys** a consistency check on the other three (a redundant datum whose
residual measures noise) and does **not** improve the conditioning of the model
parameters at all: the three parameters were already perfectly resolved by the identity
rows. In fact $\kappa_2$ *rose* from $1$ to $2$, because the added row is large relative
to the others. Replicating an existing measurement adds information about the noise, not
about the model — the central practical distinction of survey design.

(d) $d = (0.01, 0.02, 0.03, 0.06)$ satisfies $0.06 = 0.01+0.02+0.03$ ✓, so it is
consistent. With full column rank the solution is **unique**, and the first three rows
give it directly:

$$m = (0.01,\ 0.02,\ 0.03)\ \mathrm{s/km}, \qquad
Gm = (0.01,\ 0.02,\ 0.03,\ 0.06). ✓$$

"Minimum norm" is vacuous here because the solution set is a single point: minimising a
norm over a one-element set returns that element, and the constraint adds nothing. A
constraint matters only when there is a family to choose from, i.e. only when
$\mathcal{N}(G) \neq \{\mathbf{0}\}$.

---

## ★★4 — The resolution matrix, by hand

Row space of $G = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1\end{bmatrix}$:
spanned by $r_1 = (1,1,0)$ and $r_2 = (0,1,1)$. Orthonormalise:

$$e_1 = \frac{1}{\sqrt2}(1,1,0), \qquad
w_2 = r_2 - \langle r_2, e_1\rangle e_1 = (0,1,1) - \frac{1}{\sqrt2}\frac{1}{\sqrt2}
(1,1,0) = \left(-\tfrac12, \tfrac12, 1\right),$$
$$\|w_2\| = \sqrt{\tfrac14 + \tfrac14 + 1} = \sqrt{\tfrac32}, \qquad
e_2 = \sqrt{\tfrac23}\left(-\tfrac12, \tfrac12, 1\right)
= \left(-\tfrac{1}{\sqrt6}, \tfrac{1}{\sqrt6}, \sqrt{\tfrac23}\right).$$

Then $R = e_1e_1^\mathsf{T} + e_2e_2^\mathsf{T}$:

$$R = \frac{1}{3}\begin{bmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2\end{bmatrix}.$$

(a) $R^{2}$: since $R = E E^\mathsf{T}$ with $E$ orthonormal columns,
$R^{2} = E E^\mathsf{T}EE^\mathsf{T} = EE^\mathsf{T} = R$ ✓, and
$R^\mathsf{T} = (EE^\mathsf{T})^\mathsf{T} = EE^\mathsf{T} = R$ ✓. Numerically
$\max|R^{2} - R| = 2.22\times10^{-16}$ and $\max|R^\mathsf{T} - R| = 0$.

(b) $\operatorname{tr}R = \frac13(2+2+2) = 2 = \operatorname{rank}G$ ✓.

(c) $\hat n = (1,-1,1)/\sqrt3$ and
$\langle m, \hat n\rangle = (1-2+3)/\sqrt3 = 2/\sqrt3 = 1.154701$. Then
$m - Rm = (2/\sqrt3)\hat n = (2/3)(1,-1,1) = (0.666667,\ -0.666667,\ 0.666667)$,
with norm $2/\sqrt3 = 1.154701$. Verified directly: $Rm = (0.333333,\ 2.666667,\
2.333333)$ and $m - Rm = (0.666667,\ -0.666667,\ 0.666667)$ ✓. The proportionality
constant is $\langle m, \hat n\rangle = 1.154701$.

(d) $\operatorname{diag}R = (2/3, 2/3, 2/3)$: **no cell is resolved on its own.** Each
recovered cell is a weighted average of the true values — for cell 1,
$(2m_1 + m_2 - m_3)/3$ — so an anomaly appearing in one cell will leak into its
neighbours with weights $1/3$ and $-1/3$. Publishing this matrix alongside the model is
the standard way to avoid over-interpreting the image.

---

## ★★★5 — A survey with a two-dimensional null space

(a) Four cells, four rays, with each ray sampling a pair:

$$G = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1
& 1\end{bmatrix}.$$

Physical reading: rays 1 and 2 both traverse cells 1 and 2 with unit path lengths (a
duplicated ray, or a reciprocal pair); rays 3 and 4 both traverse cells 3 and 4. The two
groups are geometrically separated — the survey never crosses between the left pair and
the right pair.

(b) The rows span only two independent directions, so $\operatorname{rank}G = 2$ and

$$\mathcal{N}(G) = \operatorname{span}\{(1,-1,0,0)^\mathsf{T},\ (0,0,1,-1)^\mathsf{T}\},$$

verified: $G(1,-1,0,0)^\mathsf{T} = \mathbf{0}$ and
$G(0,0,1,-1)^\mathsf{T} = \mathbf{0}$. Rank–nullity: $2 + 2 = 4 = n$ ✓. The left null
space is the same two directions in data space,
$\operatorname{span}\{(1,-1,0,0)^\mathsf{T}, (0,0,1,-1)^\mathsf{T}\}$, since the rows
are duplicated within each group.

(c) **Consistency conditions:** $\lambda^\mathsf{T}d$ must vanish for both left null
vectors, giving

$$d_1 - d_2 = 0, \qquad d_3 - d_4 = 0 .$$

Interpretation: each duplicated pair must agree exactly. In a noise-free survey they do;
with real data the discrepancies *are* the noise, because the two rays of a pair are
genuinely the same measurement of the same combination of cells.

(d) **Noise checks.** Compute $\varepsilon_1 = d_1 - d_2$ and
$\varepsilon_3 = d_3 - d_4$. Under the assumption that the two members of a pair are
identical measurements, each is an independent realisation of the noise on one
combination of two data, so

$$\hat\sigma = \sqrt{\frac{\varepsilon_1^{2} + \varepsilon_3^{2}}{2}}$$

estimates the noise standard deviation from the data alone, with no repeat survey. With
more redundant rays the estimate improves, and the *pattern* of the discrepancies (are
they correlated with azimuth? with amplitude?) diagnoses systematic errors rather than
random noise — a mis-tie check in the language of reflection seismology.

(e) **One additional ray through cells 2 and 3**, say $(0,1,1,0)$, reduces the null
space to the single direction $(1,-1,1,-1)$ — the alternating pattern, which combines
movements that keep the total of each pair fixed. The kernel becomes

$$G' = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1
& 1 \\ 0 & 1 & 1 & 0\end{bmatrix}, \qquad
\mathcal{N}(G') = \operatorname{span}\{(1,-1,1,-1)^\mathsf{T}\}.$$

A further ray through cells 1 and 4 would remove even that direction. Note that the
duplicated rays contribute nothing to this: only genuinely new cell combinations shrink
the null space.

---

## ★★★6 — Resolution is not determinacy

(a) $R = V_rV_r^\mathsf{T}$ is built from the *singular vectors* and not from the
singular *values*. With full column rank there is no null space, so $R = I$ exactly. The
error in the presence of noise depends on $1/\sigma_i$, which $R$ does not see. $R$
answers "is the model direction representable?"; the covariance answers "is it
determined?".

(b) $\det(G^\mathsf{T}G) = 2(2.0201) - 2.01^{2} = 0.0001$, so

$$C_m = \sigma_d^{2}(G^\mathsf{T}G)^{-1} = 10^{-6}
\begin{bmatrix} 20201 & -20100 \\ -20100 & 20000\end{bmatrix},$$

and $R = I$ because $G$ has two independent columns.

(c) Standard deviations:

| quantity | variance | standard deviation (s/km) |
|---|---|---|
| $m_1$ | $2.0201\times10^{-2}$ | $0.142130$ |
| $m_2$ | $2.0000\times10^{-2}$ | $0.141421$ |
| $m_1 - m_2$ | $8.0401\times10^{-2}$ | $0.283551$ |
| $m_1 + m_2$ | $1.0000\times10^{-6}$ | $0.001000$ |

(For the sum: $\operatorname{Var} = C_{11} + C_{22} + 2C_{12} = 10^{-6}(20201 + 20000 -
40200) = 10^{-6}$. For the difference:
$10^{-6}(20201+20000+40200) = 8.0401\times10^{-2}$.)

(d) **Only the sum is resolved**, and the word is justified quantitatively: its standard
deviation is $0.001$ s/km, which equals the assumed data uncertainty $\sigma_d$ exactly —
the best any single measurement can do. The difference has a standard deviation
$284$ times larger, and the individual parameters are mixtures. With a model of size
around $0.01$–$0.05$ s/km, a parameter uncertainty of $0.14$ s/km means the individual
parameters are **not determined at all**, despite $R = I$.

(e) The first row of $G$ is $(1,1)$, so the sum $m_1 + m_2$ is exactly $d_1$: a single
measurement determines it, with the measurement's own uncertainty $\sigma_d$ — hence
$0.001$ s/km. The difference is determined only by the $1$ % difference between the two
rows, and it is amplified by $1/0.01 = 100$; hence the factor of $284$ (the exact
amplification is $1/(\sigma_{\min}) = 1/0.005$ for the operator norm, and the standard
deviation of the difference is
$\sqrt{2}\,\sigma_d/\sigma_{\min} = 1.414\times10^{-3}/0.0049875 = 0.2836$ s/km).
