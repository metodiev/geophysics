---
id: 18-02-03
title: "The Generalised (Moore-Penrose) Inverse"
level: graduate
prereqs: ["18-02-01", "18-02-02", "01-07-08"]
tags: [inverse-problems, moore-penrose, pseudo-inverse, rank-deficient, mixed-determined]
---

# The Generalised (Moore-Penrose) Inverse

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the Moore–Penrose inverse $G^{+}$ by its four algebraic conditions
   and **verify** them numerically.
2. **Construct** $G^{+}$ from the singular value decomposition and **explain** why
   the construction makes it unique.
3. **Recognise** a mixed-determined problem where neither the overdetermined nor
   the underdetermined formula applies, and **solve** it with $G^{+}$.
4. **Write** the complete solution set
   $\mathbf{m} = G^{+}\mathbf{d} + (I-G^{+}G)\mathbf{z}$ and **explain** each term.
5. **Prove** that $G^{+}\mathbf{d}$ is simultaneously the minimum-norm and the
   least-squares solution.
6. **Demonstrate** that $G^{+}$ is discontinuous where the rank changes, and
   **state** the tolerance consequence for software.

## Prerequisites

- [18-02-01 Overdetermined Problems and Least Squares](01-overdetermined.md) —
  the least-squares problem solved by $G^{+}$.
- [18-02-02 Underdetermined Problems and Minimum-Norm Solutions](02-underdetermined.md) —
  the minimum-norm problem solved by $G^{+}$.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the factorisation on which everything here is built.

## 1. One operator for all three regimes

Real problems are rarely purely over- or underdetermined. The data may constrain
some combinations of parameters well and others not at all, so $G$ is 8×6 with
rank 4 — more data than parameters *and* more parameters than independent
directions. The object that solves all three regimes at once is the
**Moore–Penrose inverse**, the unique matrix $G^{+}$ satisfying

$$\text{(1)}\ G G^{+} G = G, \qquad
\text{(2)}\ G^{+} G G^{+} = G^{+}, \qquad
\text{(3)}\ (GG^{+})^{\!\top} = GG^{+}, \qquad
\text{(4)}\ (G^{+}G)^{\!\top} = G^{+}G .$$

Conditions (3) and (4) say that $GG^{+}$ and $G^{+}G$ are **orthogonal** projectors,
hence symmetric; conditions (1) and (2) say that $G^{+}$ behaves as an inverse on
the parts of the spaces where $G$ is invertible and does nothing elsewhere.

All models and data in this module are **SYNTHETIC**.

## 2. The problem the demonstration uses

The operator is constructed as $G = AB$ with

$$A = \begin{pmatrix}1&0&2&0\\0&1&0&1\\1&1&1&0\\0&0&1&2\\
2&0&0&1\\0&2&1&0\\1&0&1&1\\0&1&2&1\end{pmatrix},\qquad
B = \begin{pmatrix}1&0&1&0&2&0\\0&1&0&1&0&2\\0&0&1&1&0&0\\1&0&0&0&1&1\end{pmatrix},$$

so $G$ is $8\times6$ and $\operatorname{rank}(G)\le4$ by construction — and equals
$4$ here. The measured spectrum is

$$\sigma = (11.28828,\ 6.155607,\ 3.114394,\ 0.9918831,\
2.997650\times10^{-16},\ 1.438992\times10^{-16}),$$

$$\sigma/\sigma_1 = (1,\ 0.5453,\ 0.2759,\ 0.08787,\
2.656\times10^{-17},\ 1.275\times10^{-17}),$$

so

$$\dim\operatorname{range}(G) = 4,\qquad
\dim\mathcal{N}(G) = 6-4 = 2,\qquad
\dim\operatorname{range}(G)^{\perp} = 8-4 = 4 .$$

Constructing $G=AB$ deliberately is not a trick: it is the honest way to build a
test problem with a known rank, and any real operator with rank deficiency looks
like this after its own SVD.

## 3. Construction and verification

The SVD $G=U\Sigma V^{\!\top}$ gives

$$G^{+} = \sum_{i:\sigma_i>0}\frac{\mathbf{v}_i\mathbf{u}_i^{\!\top}}{\sigma_i}
= V_r\,\Sigma_r^{-1}U_r^{\!\top},$$

where $r$ is the numerical rank at a declared tolerance. All four conditions hold
in the demonstration at machine precision:

| condition | measured $\max\lvert\cdot\rvert$ |
|---|---|
| $GG^{+}G - G$ | $1.776\times10^{-15}$ |
| $G^{+}GG^{+} - G^{+}$ | $2.220\times10^{-16}$ |
| $(GG^{+})^{\!\top} - GG^{+}$ | $6.384\times10^{-16}$ |
| $(G^{+}G)^{\!\top} - G^{+}G$ | $5.551\times10^{-16}$ |

Uniqueness is a consequence of the four conditions: if $X$ and $Y$ both satisfy
them, then $X = XGX = XGYGX = \dots = Y$, a two-line exercise worth doing once
(see the companion). The construction agrees with independent routes:

$$\lVert\operatorname{pinv}(G) - G^{+}\rVert_{\max} = 5.551\times10^{-17},$$

$$\lVert(G^{\!\top}G)^{+}G^{\!\top} - G^{+}\rVert_{\max} = 1.277\times10^{-15},
\qquad
\lVert G^{\!\top}(GG^{\!\top})^{+} - G^{+}\rVert_{\max} = 1.082\times10^{-15}.$$

So the two classical formulas are *correct* when written with pseudo-inverses —
and *unavailable* when written with inverses. That distinction matters more than it
looks, and the demonstration makes it concrete:

- `np.linalg.solve(G.T@G, G.T@d)` **does not raise an exception**: it returns
  numbers, with $\kappa(G^{\!\top}G) = 3.357\times10^{17}$, and those numbers are
  wrong by $1.902$ in absolute terms against $G^{+}\mathbf{d}$;
- `np.linalg.inv(G @ G.T)` raises `LinAlgError`, because $GG^{\!\top}$ is exactly
  singular.

The first case is the dangerous one. A silent wrong answer at
$\kappa=10^{17}$ looks like a result.

## 4. The complete solution set

For any data vector and any $\mathbf{z}$,

$$\mathbf{m} = G^{+}\mathbf{d} + (I-G^{+}G)\mathbf{z}$$

satisfies $G\mathbf{m} = G G^{+}\mathbf{d} = P_{\text{range}}\mathbf{d}$, which is
the projection of $\mathbf{d}$ onto $\operatorname{range}(G)$: the best
least-squares fit available. Measured with $\mathbf{d} = G(1,2,3,4,5,6)^{\!\top}$
and $G^{+}\mathbf{d} = \hat{\mathbf{m}}$:

$$\lVert\hat{\mathbf{m}}\rVert = 9.402127,\qquad
\lVert G\hat{\mathbf{m}}-\mathbf{d}\rVert = 2.275\times10^{-14},$$

| $\lVert\mathbf{z}\rVert$ | $\lVert\mathbf{m}\rVert$ | $\lVert G\mathbf{m}-\mathbf{d}\rVert$ | $\lVert\mathbf{m}-\hat{\mathbf{m}}\rVert$ |
|---|---|---|---|
| 0.0 | 9.4021 | $2.28\times10^{-14}$ | 0.0000 |
| 0.5 | 9.4120 | $2.51\times10^{-14}$ | 0.4316 |
| 2.0 | 9.4415 | $2.38\times10^{-14}$ | 0.8619 |

Every $\mathbf{z}$ gives the same fit and a larger norm. Checking 500 random
candidates, the largest norm found is $9.406785$ against
$\lVert G^{+}\mathbf{d}\rVert = 9.402127$: **$G^{+}\mathbf{d}$ is the
minimum-norm least-squares solution.** Two optimisations, one formula:

$$\left\{\begin{aligned}
&\text{minimise } \lVert\mathbf{r}\rVert^{2} &&\Longrightarrow\quad
G^{\!\top}G\mathbf{m} = G^{\!\top}\mathbf{d},\\
&\text{then minimise } \lVert\mathbf{m}\rVert^{2} \text{ among the minimisers}
&&\Longrightarrow\quad \mathbf{m} = G^{+}\mathbf{d}.
\end{aligned}\right.$$

## 5. Continuity: the price of rank deficiency

The four conditions determine $G^{+}$ uniquely as an algebraic object, but they do
**not** make it continuous in $G$. The demonstration perturbs every entry of $G$ by
a relative amount $\delta$ and records the worst relative change in $G^{+}$:

| $\delta$ | $\max \lVert\Delta G^{+}\rVert/\lVert G^{+}\rVert$ (rank-deficient $G$) |
|---|---|
| $10^{-2}$ | 730.0 |
| $10^{-3}$ | 14334.9 |
| $10^{-4}$ | 43071.9 |

Compare a full-rank, well-conditioned $3\times2$ operator at $\delta = 10^{-3}$:
the worst relative change is $0.003$ — a factor $5\times10^{6}$ smaller.

The mechanism is elementary: a perturbation promotes a formerly empty direction
from $\sigma = 0$ to $\sigma\sim\delta\lVert G\rVert$, and its inverse
$1/\sigma\sim1/\delta$ is unbounded as $\delta\to0$. Consequences to internalise:

- any rank decision must be made at a **declared tolerance**, and the tolerance
  must be reported with the result
  ([18-01-02 §6](../01-inverse-problem-foundations/02-hadamard-well-posedness.md));
- $G^{+}$ is a *model*, not a physical quantity: two implementations that cut at
  slightly different tolerances will legitimately disagree;
- a regularised inverse is the practical replacement, because it is continuous by
  construction ([18-03-02](../03-regularization/02-tikhonov.md)).

## 6. Fully worked example: the damping trap

Suppose the true model is all ones and you "fix" the singularity of
$G^{\!\top}G$ by adding a small damping $\alpha^{2}I$:

$$\tilde{\mathbf{m}} = (G^{\!\top}G+\alpha^{2}I)^{-1}G^{\!\top}G\,\mathbf{1},
\qquad \alpha = 10^{-6}.$$

The demonstration computes

$$\tilde{\mathbf{m}} = (0.6,\ 0.6,\ 1.0,\ 1.0,\ 1.2,\ 1.2),$$

which is *exactly* $G^{+}G\mathbf{1}$ as well — because $\alpha^{2} = 10^{-12}$ is
twelve orders below the smallest retained eigenvalue $\sigma_4^{2} = 0.9838$
and therefore invisible. The maximum entry-wise difference is
$1.866\times10^{-7}$.

The arithmetic of that number: with $G^{\!\top}G$ having eigenvalues
$\{\sigma_i^{2}\} = \{127.4,\ 37.9,\ 9.70,\ 0.984\}$ and two exact zeros, the
damped solution contracts the $i$-th direction by
$\sigma_i^{2}/(\sigma_i^{2}+\alpha^{2})$, and the two zero eigenvalues are
replaced by $0/\alpha^{2} = 0$ contributions scaled by $\alpha^{2}$ — so
$\tilde{\mathbf{m}}$ is $\hat{\mathbf{m}}$ up to the first-order corrections
$\alpha^{2}/\sigma_i^{2} = 10^{-12}/\sigma_i^{2} \le 10^{-12}$. The printed
$1.9\times10^{-7}$ is the *solver's* roundoff, not the damping's effect: an
augmented 10×10 system with $\alpha^{2}$ entries has condition number
$\sigma_{\max}^{2}/\alpha^{2} = 127.4/10^{-12} = 1.27\times10^{14}$, so it loses nearly all
precision even though the answer happens to be right.

Two practical rules follow:

1. **when $\alpha^{2}$ is far below the smallest retained eigenvalue, damping does
   nothing except slow the solver down and cost digits** — so damping must be
   chosen relative to the spectrum ([18-03-03](../03-regularization/03-parameter-choice.md));
2. **never use a damped normal-equation solve as a substitute for a truncated
   SVD.** The SVD tells you which directions you discarded; the damped solve
   silently mixes them in.

## 7. Assumptions and regime of validity

- **A declared numerical rank.** All statements about $\mathcal{N}(G)$ and
  $\operatorname{range}(G)$ are relative to a tolerance.
- **Exact arithmetic for the identities.** The four conditions hold to
  $\varepsilon\kappa(G)$ in practice, so a problem with
  $\kappa\sim10^{10}$ will show the identities violated at $10^{-6}$; that is
  roundoff, not a defective implementation.
- **$G^{+}\mathbf{d}$ as the answer** presumes you accept minimum norm as your
  selection rule ([18-02-02 §5](02-underdetermined.md)).
- **Known $G$.** Model error enters as a systematic, not as noise, and $G^{+}$
  propagates it without any warning.
- **Linear problem.** The generalised inverse is a one-shot linear operator; a
  nonlinear problem needs iteration around a linearisation
  ([18-04-01](../04-nonlinear-inversion/01-local-linearization.md)).

## 8. Running the demonstration

The demonstration for this lesson is [`code/generalized_inverse_demo.py`](code/generalized_inverse_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generalized_inverse_demo.py
```

It prints the spectrum, the four condition residuals, the three constructions, the
complete solution set, the minimality test and the continuity table. Runtime is
under a second. Companion problems are in
[`exercises/03-generalized-inverse-exercises.md`](exercises/03-generalized-inverse-exercises.md).

## Mastery checkpoint

Without notes:

> An operator $G$ is $8\times6$ with rank $4$. **(a)** State the dimensions of
> $G^{+}$, $\operatorname{range}(G^{+})$, $\mathcal{N}(G)$ and the projector
> $I-G^{+}G$. **(b)** Write the general solution of $G\mathbf{m}=\mathbf{d}$ and
> say which member $G^{+}\mathbf{d}$ is. **(c)** Which of the following are
> well posed for this $G$: $(G^{\!\top}G)^{-1}G^{\!\top}\mathbf{d}$,
> $G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d}$, $(G^{\!\top}G)^{+}G^{\!\top}\mathbf{d}$?
> **(d)** Explain in two sentences why $G^{+}$ changes discontinuously when an
> entry of $G$ changes, and what you must therefore report.

Worked solutions are in
[`exercises/03-generalized-inverse-solutions.md`](exercises/03-generalized-inverse-solutions.md).

## Common pitfalls

1. **Calling `inv(G.T@G)` and getting numbers.** Rank-deficient matrices often do
   not raise; they return garbage.
2. **Marking a matrix "full rank" from its dimensions.** Rank is numerical.
3. **Believing $G^{+}$ is continuous.** It is unique, not stable.
4. **Using damping as a rank truncation.** Different objects with different biases.
5. **Reporting $G^{+}\mathbf{d}$ without the rule.** Say "minimum-norm
   least-squares solution at tolerance $10^{-10}$".
6. **Forgetting the orthogonal complements.** Four dimensions of this data space
   can never be fitted.

## Related modules

- [18-02-04 SVD Analysis: Model Resolution and Data Importance](04-svd-analysis-inverse.md) —
  what the retained singular directions mean physically.
- [18-02-05 Resolution and Information Matrices in Interpretation](05-resolution-matrices.md) —
  $G^{+}G$ and $GG^{+}$ read as resolution.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the continuous replacement for the truncated inverse.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the underlying factorisation.
- [01-16-03 Linear Operators, Adjoints and Compactness](../../01-mathematics/16-functional-analysis/03-operators.md) —
  the continuum analogue of $G^{+}$.
