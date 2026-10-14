---
id: 01-07-08
title: "Singular Value Decomposition and Rank Truncation"
level: graduate
prereqs: ["01-07-06", "01-07-07"]
estimated_minutes: 90
tags: [linear-algebra, svd, resolution, regularisation, inverse-theory]
---

# Singular Value Decomposition and Rank Truncation

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the singular value decomposition $A = U\Sigma V^\mathsf{T}$ for any
   matrix, and derive it from the symmetric eigenproblem of $A^\mathsf{T}A$.
2. **Read off** all four fundamental subspaces from $U$ and $V$, and decide
   existence and uniqueness from the singular values alone.
3. **Interpret** each singular triple $(\sigma_i, u_i, v_i)$ as a statement about
   the experiment: which data pattern is produced by which model pattern, and how
   strongly.
4. **Build** the resolution matrix $R = V_rV_r^\mathsf{T}$ and the data resolution
   matrix $N = U_rU_r^\mathsf{T}$, and explain why $R = I$ and "well determined"
   are different claims.
5. **Compute** the model covariance from the singular values and a data uncertainty,
   and identify the model combination that the survey cannot determine.
6. **Apply** the Picard condition to decide where to truncate, and **quantify** the
   bias–variance trade-off that truncation implements.
7. **Justify** a truncated-SVD (TSVD) solution numerically against the exact-data
   solution, and state what is sacrificed.
8. **Use** the Eckart–Young theorem to justify low-rank approximation, and apply it
   to a two-dimensional field.

## Prerequisites

[01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) for
the symmetric spectral theorem, [01-07-07 Orthogonality, Projections and Least
Squares](./07-orthogonality.md) for the projection geometry, and
[01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md)
for the condition number built from singular values.

## 1. Intuition: the answer to "which data constrain which parameters"

A data kernel $G$ maps a model to data. The SVD produces two *orthonormal bases* —
one for the model space, one for the data space — in which the map is diagonal:

$$G = U\Sigma V^\mathsf{T} = \sum_{i=1}^{r} \sigma_i\, u_i v_i^\mathsf{T},$$

with $\sigma_1 \ge \sigma_2 \ge \cdots > 0$, the columns $v_i$ an orthonormal basis
of the model space, and the columns $u_i$ an orthonormal basis of the data space.

Read the sum as a set of *channels*. Channel $i$ takes the model coefficient
$v_i^\mathsf{T}m$, multiplies it by $\sigma_i$, and emits the data pattern
$u_i$. So:

- a **large** $\sigma_i$ means "this model pattern produces a strong, clean data
  pattern, and if I see that data pattern I know that model pattern";
- a **small** $\sigma_i$ means "this model pattern produces a weak data pattern, and
  a small amount of noise in that data direction will be amplified into a large
  model error when I invert".

That is the whole content of resolution, information content and regularisation, and
it is why the SVD is the single most useful piece of linear algebra in geophysics.
The lesson's running example is a five-ray kernel with singular values

$$\sigma = (2.2523271221,\ 1.1033155184,\ 0.0108352219), \qquad
\kappa_2 = \frac{\sigma_1}{\sigma_3} = 207.8709 ,$$

and its smallest singular vector, computed below, is
$(0.709992, -0.704209, -0.001157)$: the difference $m_1 - m_2$. The survey cannot
separate cell 1 from cell 2, and the SVD says so as a number rather than as an
opinion.

## 2. Precise definitions

### 2.1 The decomposition

**Theorem (existence).** Every real $m \times n$ matrix $A$ has a factorisation
$A = U\Sigma V^\mathsf{T}$ with $U$ an $m \times m$ orthogonal matrix, $V$ an
$n \times n$ orthogonal matrix, and $\Sigma$ an $m \times n$ matrix that is zero
except for its leading diagonal, whose entries $\sigma_1 \ge \cdots \ge \sigma_{\min(m,n)}
\ge 0$ are the **singular values**.

The **thin** (economy) form keeps only the first $r = \operatorname{rank}A$ columns
of $U$ and $V$, and the corresponding $\sigma$: $A = U_r\Sigma_r V_r^\mathsf{T}$.
Dimensions: $U_r$ is $m \times r$, $\Sigma_r$ is $r \times r$, $V_r$ is
$n \times r$.

### 2.2 Construction, and the relation to the eigenproblem

$A^\mathsf{T}A$ is symmetric positive semidefinite, so by
[01-07-06](./06-eigenvalues.md) Section 2.2 it has real nonnegative eigenvalues and
an orthonormal eigenbasis. Write $A^\mathsf{T}Av_i = \lambda_i v_i$ with
$\lambda_1 \ge \cdots \ge \lambda_n \ge 0$ and set $\sigma_i = \sqrt{\lambda_i}$.
Then

$$v_i^\mathsf{T}A^\mathsf{T}Av_i = \|Av_i\|^{2} = \sigma_i^{2}
\;\Longrightarrow\; u_i = \frac{Av_i}{\sigma_i} \quad (\sigma_i > 0),$$

and a short calculation confirms $\langle u_i, u_j\rangle = \delta_{ij}$ for
$\sigma_i, \sigma_j > 0$. For $\sigma_i = 0$ the corresponding $v_i$ spans the null
space and $u_i$ is not determined by $A$; any orthonormal completion will do, and it
spans the left null space. That is precisely how the demonstration's code builds the
decomposition, and Section 3.3 explains why this route is a *construction* and not
the algorithm a production library uses.

### 2.3 The four fundamental subspaces, from the SVD

| Subspace | Basis | Dimension |
|---|---|---|
| Column space $\mathcal{C}(A)$ | $u_1, \dots, u_r$ | $r$ |
| Left null space $\mathcal{N}(A^\mathsf{T})$ | $u_{r+1}, \dots, u_m$ | $m - r$ |
| Row space $\mathcal{C}(A^\mathsf{T})$ | $v_1, \dots, v_r$ | $r$ |
| Null space $\mathcal{N}(A)$ | $v_{r+1}, \dots, v_n$ | $n - r$ |

Everything that [01-07-04](./04-rank-and-nullspace.md) established by row
reduction appears here with *orthonormal, physically ordered* bases. Rank deficiency
is $\sigma_r > 0$ and $\sigma_{r+1} = 0$; near-deficiency is $\sigma_r/\sigma_1 =
\epsilon_{\text{mach}}$; and the distinction between them is a number rather than a
judgement.

### 2.4 The pseudoinverse

The **Moore–Penrose pseudoinverse** of $A = U\Sigma V^\mathsf{T}$ is

$$A^{+} = V\Sigma^{+}U^\mathsf{T} = \sum_{i:\, \sigma_i > 0}
\frac{v_i u_i^\mathsf{T}}{\sigma_i} ,$$

where $\Sigma^{+}$ replaces each positive $\sigma_i$ by $1/\sigma_i$ and transposes
the shape. Its properties: $AA^{+}$ is the orthogonal projector onto
$\mathcal{C}(A)$ and $A^{+}A$ the orthogonal projector onto $\mathcal{C}(A^\mathsf{T})$;
$A^{+}d$ is the **minimum-norm least-squares solution** of $Am = d$ for every $d$;
and $A^{+} = A^{-1}$ when $A$ is square and nonsingular. It therefore solves
existence (by projecting) and uniqueness (by choosing the smallest-norm member) in one
object. Writing the solution out,

$$m^{*} = A^{+}d = \sum_{i:\, \sigma_i > 0} \frac{u_i^\mathsf{T}d}{\sigma_i}\, v_i ,$$

exposes the difficulty immediately: each term divides by $\sigma_i$, so a component
of the data along $u_i$ is amplified by $1/\sigma_i$ in the model. The whole art of
regularisation is deciding which terms to keep.

### 2.5 Resolution and covariance

Let $R = V_rV_r^\mathsf{T}$ (the resolution matrix) and
$N = U_rU_r^\mathsf{T}$ (the data resolution matrix). Both are orthogonal
projectors: symmetric and idempotent, with $\operatorname{tr}R = \operatorname{tr}N = r$.
Since $A^{+}A = R$,

$$\hat m = A^{+}d = A^{+}(Gm + \delta d) = Rm + A^{+}\delta d ,$$

so the error splits into a **bias** term (the null-space part of the true model,
which no inversion can recover) and a **noise** term (the amplified data error). If
the data covariance is $C_d = \sigma_d^{2}I$, the model covariance is

$$C_m = \sigma_d^{2}\,V_r\Sigma_r^{-2}V_r^\mathsf{T}
= \sigma_d^{2}\sum_{i \le r} \frac{v_i v_i^\mathsf{T}}{\sigma_i^{2}} ,$$

whose diagonal entries are the variances of individual model parameters and whose
eigenvalues along $v_i$ are $\sigma_d^{2}/\sigma_i^{2}$. The **standard deviation
along the worst-determined direction** is therefore $\sigma_d/\sigma_{\min}$.

If the inversion is *truncated* at rank $p < r$, then $R = V_pV_p^\mathsf{T} \neq I$
and the discarded directions are not recovered at all: resolution is traded for
variance. This is the bias–variance trade-off, and Section 3.6 quantifies it for the
running example.

### 2.6 The Picard condition

For exact data generated by a model, $u_i^\mathsf{T}d = \sigma_i(v_i^\mathsf{T}m)$,
so the **coefficients** $u_i^\mathsf{T}d$ decay at least as fast as the singular
values, and the ratios $u_i^\mathsf{T}d/\sigma_i$ remain of the size of the model. For
noisy data, once $\sigma_i$ falls below the noise level the coefficients
$u_i^\mathsf{T}d$ stop decaying — they are noise — and the ratios grow without bound.
The **Picard condition** is the requirement
$|u_i^\mathsf{T}d| \to 0$ faster than $\sigma_i$; when it fails, the sum
$\sum (u_i^\mathsf{T}d/\sigma_i)v_i$ is dominated by noise and must be truncated.

### 2.7 Rank truncation and Eckart–Young

The **TSVD** (truncated singular value decomposition) solution keeps the first $p$
terms. The justification is the **Eckart–Young theorem**: for every $p$,

$$\min_{\operatorname{rank}B \le p}\|A - B\|_2 = \sigma_{p+1}, \qquad
\min_{\operatorname{rank}B \le p}\|A - B\|_F =
\sqrt{\sum_{i > p}\sigma_i^{2}} ,$$

and the minimiser in both cases is $A_p = \sum_{i \le p}\sigma_iu_iv_i^\mathsf{T}$.
Truncation is therefore *optimal* in both norms, not merely convenient — which is why
it is the reference method against which other regularisations are judged.

## 3. Step-by-step derivations

### 3.1 The running example, and what its singular vectors mean

Three cells in a strip; five rays with path lengths, in km,

$$A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 1.02 & 0 \\ 0 & 0 & 1 \\
0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0 \end{bmatrix}.$$

Rays 1, 4 and 5 all traverse cells 1 and 2 with equal path lengths, so all three
measure the *sum* $m_1 + m_2$. Only the 2 % difference between rays 1 and 2 carries
information about the *difference*. Ray 3 samples cell 3 alone.

Computed quantities:

$$\sigma = (2.2523271221,\ 1.1033155184,\ 0.0108352219), \qquad
\kappa_2 = 207.8709,$$

| $i$ | $\sigma_i$ | $v_i$ (cells 1, 2, 3) | $u_i$ (rays 1…5) |
|---|---|---|---|
| 1 | 2.252327 | $(0.701293,\ 0.706900,\ 0.092087)$ | $(0.62522,\ 0.63149,\ 0.04089,\ 0.33305,\ 0.31261)$ |
| 2 | 1.103316 | $(0.064031,\ 0.066192,\ -0.995750)$ | $(0.11803,\ 0.11923,\ -0.90251,\ -0.39224,\ 0.05901)$ |
| 3 | 0.010835 | $(0.709992,\ -0.704209,\ -0.001157)$ | $(0.53369,\ -0.76616,\ -0.10675,\ 0.21347,\ 0.26685)$ |

Reading the table:

- $v_1 \approx (1,1,0)/\sqrt2$: the **sum** of cells 1 and 2. Well determined
  ($\sigma_1 = 2.25$).
- $v_2 \approx (0,0,1)$: cell 3 on its own. Well determined ($\sigma_2 = 1.10$).
- $v_3 \approx (1,-1,0)/\sqrt2$: the **difference** of cells 1 and 2. Nearly
  invisible ($\sigma_3 = 0.0108$), because the only data that distinguish the two
  cells are the 2 % path-length contrast between rays 1 and 2.
- $u_3 = (0.534, -0.766, -0.107, 0.213, 0.267)$: the *data pattern* that the
  difference produces. Rays 1 and 2 enter with opposite signs, as they must.

The orthonormality and reconstruction checks: $\max|A - U\Sigma V^\mathsf{T}| =
1.110\times10^{-15}$, $\max|V^\mathsf{T}V - I| = 6.661\times10^{-16}$, and
$\max|U^\mathsf{T}U - I| = 7.150\times10^{-13}$ — the last being the largest because
the construction routes through $A^\mathsf{T}A$ and so squares the conditioning
(Section 3.3). The Frobenius identity closes exactly:
$\|A\|_F^{2} = 6.290400 = \sum\sigma_i^{2}$, with the three shares of the total
$0.806463$, $0.193518$ and $0.000019$.

### 3.2 Which channel carries the information

With the true model $m = (0.05, -0.02, 0.03)$ $\mathrm{s/km}$, the exact data are
$d = (0.03,\ 0.0296,\ 0.03,\ 0.03,\ 0.015)$ s. The data coefficients and the model
coefficients are related exactly by $u_i^\mathsf{T}d = \sigma_i v_i^\mathsf{T}m$:

| $i$ | $|u_i^\mathsf{T}d|$ (s) | $u_i^\mathsf{T}d/\sigma_i$ (s/km) | $v_i^\mathsf{T}m$ (s/km) |
|---|---|---|---|
| 1 | $5.335597\times10^{-2}$ | $0.02368926$ | $0.02368926$ |
| 2 | $3.088709\times10^{-2}$ | $0.02799480$ | $-0.02799480$ |
| 3 | $5.368752\times10^{-4}$ | $0.04954907$ | $0.04954907$ |

The ratio column *is* the model coefficient, to the last printed digit. Now add 1 ms
of picking noise and recompute the third entry:

$$u_3^\mathsf{T}d/\sigma_3: \quad 0.04954907 \longrightarrow 0.01175899 .$$

The coefficient moved by $0.038$, of the same order as its exact value $0.0495$: the
model information in that channel has been replaced by noise. The Picard condition
has failed in channel 3 and nowhere else, which is exactly the diagnosis needed to
decide where to truncate.

### 3.3 Never form $A^\mathsf{T}A$: a numerical aside

The identity $\sigma_i^{2} = \lambda_i(A^\mathsf{T}A)$ is mathematically correct and
numerically dangerous. $\kappa_2(A^\mathsf{T}A) = \kappa_2(A)^{2}$, so forming
$A^\mathsf{T}A$ in double precision destroys any singular value below
$\sigma_1\sqrt{\epsilon_{\text{mach}}} = \sigma_1 \times 1.5\times10^{-8}$.
[01-07-05](./05-determinants-inverses.md) Section 3.3 demonstrates it concretely: for
the two-ray geometry with $\delta = 10^{-8}$, the $A^\mathsf{T}A$ route reports
$\sigma_{\min} = 0$ where the exact value is $5\times10^{-9}$.

Production SVD algorithms (Golub–Kahan bidiagonalisation, then a QR iteration on the
bidiagonal form) never form $A^\mathsf{T}A$; they reduce $A$ itself by orthogonal
transformations to bidiagonal form and iterate there, at a cost of about
$4mn^{2} - \frac{4}{3}n^{3}$ operations with backward-stable error bounds. The
demonstration's construction through $A^\mathsf{T}A$ is used because it is short
enough to read, and its results are quoted with that caveat: the
$7.150\times10^{-13}$ orthogonality defect above, and the four-digit accuracy of the
smallest singular value in the 12×12 compression example of Section 5.

### 3.4 Resolution

For the *full* rank-three inversion, $V$ is $3\times3$ orthogonal, so

$$R = VV^\mathsf{T} = I \quad\text{exactly},\qquad
\max|R - I| = 6.661\times10^{-16} .$$

Every model direction is formally resolved, no null space exists, and yet the
standard deviations of the model parameters are

$$\operatorname{diag}(C_m)^{1/2} = (0.06552704,\ 0.06499337,\ 0.00090972)\ \mathrm{s/km}$$

against a model whose largest component is $0.05$ $\mathrm{s/km}$. The parameters are
*formally* determined and *practically* worthless. The standard deviation along the
worst direction is

$$\frac{\sigma_d}{\sigma_3} = \frac{10^{-3}}{0.0108352219} = 0.09229\ \mathrm{s/km} ,$$

nearly twice the size of the model itself.

That is the distinction the lesson insists on: **$R$ answers "is there a null
space?"; $C_m$ answers "how well is it determined?".** They are different questions
with different answers, and a paper that reports only $R = I$ has answered the less
interesting one.

Now truncate. With $p = 2$ (drop the worst channel):

| rank $p$ | $\operatorname{diag}R$ | $\operatorname{tr}R$ | resolution error $\|m - Rm\|$ (s/km) | parameter std (s/km) |
|---|---|---|---|---|
| 1 | $(0.491812,\ 0.499708,\ 0.008480)$ | 1.000000 | $0.05691062$ | $(0.00031136,\ 0.00031385,\ 0.00004089)$ |
| 2 | $(0.495912,\ 0.504090,\ 0.999999)$ | 2.000000 | $0.04954907$ | $(0.00031673,\ 0.00031954,\ 0.00090343)$ |
| 3 | $(1,\ 1,\ 1)$ | 3.000000 | $0.00000000$ | $(0.06552704,\ 0.06499337,\ 0.00090972)$ |

The diagonal of $R$ is the classic "resolution" diagnostic of the tomographic
literature, and it now behaves as expected: at $p = 2$ cells 1 and 2 are resolved at
about $0.5$ each — the survey cannot separate them, so the inversion reports their
average — while cell 3 is resolved at $0.999999$. The bias introduced by truncation
is $\|m - Rm\| = 0.0495$ $\mathrm{s/km}$, which is precisely $\|v_3^\mathsf{T}m\|$,
the discarded channel's model content. And the variance falls by a factor of about
208 in cells 1 and 2 ($0.0655 \to 0.000317$), which is $(\sigma_3/\sigma_2)^{2}$ up
to the mixing of directions.

### 3.5 Truncated inversion beats exact inversion on noisy data

Now invert with three different ranks and four noise levels. The model error is
$\|\hat m - m_{\text{true}}\|$ and the misfit is $\|A\hat m - d_{\text{noisy}}\|$,
both in the natural units:

| noise (s) | rank | model error (s/km) | data misfit (s) |
|---|---|---|---|
| 0 | 3 | $0.0000000000$ | $1.7\times10^{-15}$ |
| 0 | 2 | $0.0500425596$ | $3.317\times10^{-2}$ |
| 0 | 1 | $0.0588972769$ | $4.772\times10^{-2}$ |
| $10^{-4}$ | 3 | $0.0061323289$ | $1.211\times10^{-4}$ |
| $10^{-4}$ | 2 | $0.0500427515$ | $4.858\times10^{-4}$ |
| $10^{-4}$ | 1 | $0.0569106405$ | $3.075\times10^{-2}$ |
| $10^{-3}$ | 3 | $0.0613232891$ | $1.211\times10^{-3}$ |
| $10^{-3}$ | 2 | $0.0495679118$ | $1.217\times10^{-3}$ |
| $10^{-3}$ | 1 | $0.0569124891$ | $2.949\times10^{-2}$ |
| $10^{-2}$ | 3 | $0.6132328909$ | $1.211\times10^{-2}$ |
| $10^{-2}$ | 2 | $0.0513991988$ | $1.356\times10^{-2}$ |
| $10^{-2}$ | 1 | $0.0570970444$ | $2.151\times10^{-2}$ |

Three conclusions, in order of importance.

1. **With exact data, rank 3 is perfect** and truncation only introduces bias. There
   is nothing wrong with the exact inverse when the data are exact.
2. **At 1 ms noise, rank 3 has become worse than rank 2**: $0.0613$ against
   $0.0496$ $\mathrm{s/km}$. The model error of the full-rank solution grows linearly
   with the noise amplitude ($0.0061$ at $0.1$ ms, $0.0613$ at $1$ ms, $0.6132$ at
   $10$ ms), because it is $\approx$ noise/$\sigma_3$; the rank-2 error is essentially
   independent of the noise.
3. **The truncated solution always fits the data worse** and estimates the model
   better. At $10$ ms noise, rank 2 fits with misfit $0.01356$ against rank 3's
   $0.01211$ — a 12 % worse fit — while being **twelve times more accurate**. Any
   inversion selected by data fit alone would choose the wrong answer.

This is the single most important practical fact in the module: **the best data fit
is not the best model**, and the singular values tell you where to stop. Choosing
where is the substance of [18-inverse-problems](../../18-inverse-problems/README.md);
the SVD supplies the information on which the choice is based.

### 3.6 Where the truncation error comes from, exactly

Write the truncated estimate with $p = 2$ and $R = V_2V_2^\mathsf{T}$:

$$\hat m = Rm_{\text{true}} + V_2\Sigma_2^{-1}U_2^\mathsf{T}\delta d .$$

The first term is the bias and the second is the noise. For this example the bias has
norm $\|(I - R)m\| = \|v_3\,v_3^\mathsf{T}m\| = 0.04954907$ $\mathrm{s/km}$ and the
noise term has standard deviation $\sqrt{\sigma_d^{2}\sum_{i\le2}\|v_i\|^{2}/\sigma_i^{2}}$
along its own directions — of order $\sigma_d/\sigma_2 = 9.06\times10^{-4}$
$\mathrm{s/km}$. Adding an estimated bias of $0.0495$ to an estimated standard
deviation of $0.0009$ gives $0.0504$, against the observed rank-2 error at
$10^{-3}$ s noise of $0.04957$: the decomposition is quantitatively right, which is
the check that the machinery is not decoration. The full-rank alternative has bias
zero and standard deviation $0.0923$ $\mathrm{s/km}$, which is why it loses at
1 ms noise.

The optimal truncation rank minimises the sum of squared bias and variance, and it
depends on the noise level. It moves from 3 at zero noise to 2 at 1 ms, in exact
agreement with the table.

### 3.7 Data resolution, and which datum is earning its place

$N = U_rU_r^\mathsf{T}$ is a rank-3 projector in $\mathbb{R}^{5}$:

$$N = \begin{bmatrix} 0.68966 & 0.00000 & -0.13793 & 0.27586 & 0.34483 \\
0.00000 & 1.00000 & 0.00000 & 0.00000 & 0.00000 \\
-0.13793 & 0.00000 & 0.82759 & 0.34483 & -0.06897 \\
0.27586 & 0.00000 & 0.34483 & 0.31034 & 0.13793 \\
0.34483 & 0.00000 & -0.06897 & 0.13793 & 0.17241 \end{bmatrix},$$

with $\operatorname{tr}N = 3$, $\|N - I\|_\infty = 0.827586$, and leverages

$$(0.689655,\ 1.000000,\ 0.827586,\ 0.310345,\ 0.172414), \qquad
\text{mean} = 3/5 = 0.6 .$$

Ray 2 has leverage exactly 1: the model

$$m = (-50.0,\ 50.0,\ 0.0)\ \mathrm{s/km}$$

reproduces ray 2's datum alone, with $\|m\|/\|d\| = 70.7107$, and
$Am = (0,\ 1,\ 0,\ 0,\ 0)$ verified exactly. So high leverage does **not** mean a
well-determined parameter: it means the datum lies in the range of the operator. Ray
2's datum is reproducible only by a model fifty times its own size, which is the same
near-degeneracy that produced $\sigma_3 = 0.0108$, seen from the data side. Rays 4
and 5, at leverage $0.310$ and $0.172$, largely repeat what rays 1, 4 and 5 jointly
measure and contribute little new information — a statement about survey economics
that follows from the design matrix alone.

### 3.8 Rank deficiency, exactly

For the kernel of [01-07-04](./04-rank-and-nullspace.md),

$$G = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{bmatrix},$$

the computed singular values are $(3.0,\ 1.0,\ 0.0)$ exactly, and

$$v_3 = (0.57735027,\ -0.57735027,\ 0.57735027), \qquad
Gv_3 = (0,\ 0,\ 0),$$
$$u_3 = (0.57735027,\ 0.57735027,\ -0.57735027), \qquad
G^\mathsf{T}u_3 = (0,\ 0,\ 0).$$

The right null vector is the non-uniqueness; the left null vector is the redundant
data combination $d_1 + d_2 - d_3 = 0$. With $r = 2$,
$\operatorname{diag}R = (2/3, 2/3, 2/3)$ and $Rv_3 = 0$: the projection removes the
null direction from every model. The SVD reports exact rank deficiency as a zero
singular value, and near-deficiency as a small one. Both are visible on one axis, which
is why the singular-value spectrum is the standard first figure of any inversion
paper.

## 4. Physical interpretation

**A singular triple is a measurement you can actually make.** $\sigma_i$ is the gain
of channel $i$, $v_i$ is the model pattern it measures, and $u_i$ is the data pattern
it produces. The set of channels with large $\sigma_i$ is the *information content*
of the survey, and it is finite: the model space may have $10^{6}$ dimensions, but the
row space of $G$ has $r$ dimensions, and $r$ is what the survey determines. Everything
orthogonal to that is prior assumption.

**Resolution is a blurring operator, and it is data-dependent.** $Rm$ is a weighted
average of true model values, with weights given by the rows of $R$. The blurring
pattern is a property of the ray geometry, so two surveys over the same target
produce different images of the same Earth, and the difference is resolution rather
than geology. Publishing a resolution matrix alongside a tomographic image is the
standard defence.

**Data resolution says which measurements matter.** A datum with leverage near zero
is nearly a linear combination of the others: it adds no new information and its noise
is averaged in. A datum with leverage 1 is reproducible by some model, which may be
an enormous model. Neither statement is about the *value* of the datum, and both are
computable before the survey is shot.

**The bias–variance trade-off is a physical choice, not a numerical one.** Truncating
at $p = 2$ asserts that the model contains no component of $v_3$ — that the cells 1
and 2 are perturbed together. That is a geological statement. Choosing a truncation
rank is choosing an assumption about the Earth, and the SVD makes the choice explicit
and its consequences computable.

**Low-rank structure is a property of smooth fields.** Section 5 shows a 12×12
gravitational-anomaly-like field reproduced to within 5 % with four rank-one terms and
1 % with six, out of twelve possible. Sensitivity kernels, data covariance matrices
and resolution operators are all smooth in this sense, which is what makes
low-rank approximation the standard compression tool of large inversions. See
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

## 5. Python demonstration

The companion script is
[`code/svd_resolution_demo.py`](./code/svd_resolution_demo.py), with eight sections:
the ray geometry and its singular triples, the decomposition as a sum of rank-one
maps, the coefficient and Picard analysis, resolution and covariance against
truncation rank, truncated inversion against exact inversion on noisy data, data
resolution and leverage, exact rank deficiency, and low-rank compression of a
two-dimensional field.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, spectrum | $\sigma = (2.2523271,\ 1.1033155,\ 0.0108352)$, $\kappa_2 = 207.8709$ | one badly determined direction, from geometry alone |
| 1, weak mode | $v_3 = (0.709992,\ -0.704209,\ -0.001157)$ | the cell-1-minus-cell-2 difference |
| 2, reconstruction | $\max\|A - U\Sigma V^\mathsf{T}\| = 1.11\times10^{-15}$; $\|A\|_F^{2} = 6.290400 = \sum\sigma_i^{2}$ | the decomposition is exact, and its energy is graded $0.806$, $0.194$, $0.000019$ |
| 3, Picard | ratio column equals $v_i^\mathsf{T}m$ exactly; third coefficient moves $0.0495 \to 0.0118$ with 1 ms noise | the noise has replaced the model information in the weak channel |
| 4, resolution | $R = I$ at $p = 3$ with parameter std $(0.0655,\ 0.0650,\ 0.00091)$; at $p=2$ cells 1–2 resolve at $0.496$ | resolved and determined are different questions |
| 4, worst direction | $\sigma_d/\sigma_3 = 0.09229$ s/km against a model of size $0.05$ s/km | the weak direction is not recoverable at any useful accuracy |
| 5, truncation | 1 ms noise: rank 3 error $0.0613$, rank 2 error $0.0496$; 10 ms: $0.6132$ vs $0.0514$ | truncated inversion is more accurate, and always fits worse |
| 6, leverage | $(0.689655,\ 1.000000,\ 0.827586,\ 0.310345,\ 0.172414)$, mean $0.6$ | ray 2's datum needs a model of size $70\times$ the datum |
| 7, exact null space | $\sigma_3 = 0$; $v_3 = (0.57735, -0.57735, 0.57735)$; $Gv_3 = 0$ | the null space as a zero singular value |
| 8, compression | relative error $0.684$, $0.244$, $0.169$, $0.0525$, $0.0328$, $0.00845$ for ranks 1–6 of 12 | smoothness gives low effective rank |

> **Breaking exercise.** In Section 5 of the script, replace the deterministic
> noise vector with the *exact* direction $u_3$ scaled by $10^{-3}$ s. Predict,
> before running: (a) which rank minimises the model error, (b) the exact model error
> at rank 3, and (c) whether rank 2 can beat it. Then check. This is the cleanest
> possible experiment on the bias–variance trade-off, because the noise is confined
> to a single singular direction and the arithmetic can be done on paper.

## 6. Exercises

Full set and worked solutions:
[`exercises/08-svd-exercises.md`](./exercises/08-svd-exercises.md)
and
[`exercises/08-svd-solutions.md`](./exercises/08-svd-solutions.md).
Four to start with:

**★1.** Compute the SVD by hand for
$A = \begin{bmatrix} 3 & 0 \\ 4 & 0 \\ 0 & 1\end{bmatrix}$. Report $U$, $\Sigma$,
$V$, the rank, the condition number, and the pseudoinverse.

**★2.** For the matrix of ★1, compute $\mathcal{C}(A)$, $\mathcal{N}(A)$,
$\mathcal{C}(A^\mathsf{T})$ and $\mathcal{N}(A^\mathsf{T})$ from the SVD, and check
the rank–nullity theorem in both spaces.

**★★3.** For the five-ray kernel of Section 3.1, an additional ray is added with
path lengths $(1,\ 1,\ 0)$ — a third ray measuring only the sum of cells 1 and 2.
(a) Predict the effect on the three singular values before computing. (b) Compute
them. (c) Explain the change in $\sigma_3$ and interpret it as a statement about the
survey. (d) Does the new datum raise or lower the mean leverage?

**★★4.** A survey has $G = \begin{bmatrix} 1 & 1 \\ 1 & 1.1 \\ 1 & 1.2
\end{bmatrix}$ km with $d = (0.03,\ 0.032,\ 0.034)^\mathsf{T}$ s.
(a) Compute the SVD and the least-squares solution. (b) Compute $R$ and $N$.
(c) With $\sigma_d = 10^{-3}$ s, compute the model covariance and the standard
deviation along each singular direction. (d) State, in one sentence each, which model
combination this survey determines and which it does not.

**★★★5.** Bias–variance. For the kernel of Section 3.1 with $\sigma_d = 10^{-3}$ s
and true model $m = (0.05, -0.02, 0.03)$ $\mathrm{s/km}$: (a) compute the squared bias
$\|(I - R_p)m\|^{2}$ and the trace of the covariance for $p = 1, 2, 3$. (b) Report
the total expected squared error $\|(I - R_p)m\|^{2} + \operatorname{tr}C_m^{(p)}$
for each $p$ and state the optimum. (c) Repeat for $\sigma_d = 10^{-1}$ s and for
$\sigma_d = 10^{-5}$ s, and report how the optimal $p$ moves. (d) Explain the
dependence of the optimal rank on the noise level in one paragraph.

**★★★6.** Reproduce the low-rank compression of Section 8 of the demonstration with
your own field: a synthetic gravity anomaly produced by two rectangular prisms of
different size, depth and orientation. (a) Report the singular value spectrum.
(b) Report the relative Frobenius error for ranks 1 to 10. (c) State the rank needed
for 1 % accuracy and compare with the rank needed for the field of Section 5.
(d) Explain why a deeper, smoother source has a lower effective rank than a shallow,
compact one, and connect this with the resolution discussion of Section 4.

## 7. Common mistakes

1. **Reporting $R = I$ as evidence of a good inversion.** $R$ is about the null
   space; with full column rank it is always $I$, however bad the covariance is.
2. **Choosing a truncation rank from the singular values alone.** The decision needs
   the data coefficients as well — that is the Picard condition.
3. **Believing that a better fit means a better model.** Section 3.5's rank-3
   solution fits better and is twelve times less accurate at $10$ ms noise.
4. **Forming $A^\mathsf{T}A$ to get singular values.** It halves the number of usable
   digits and destroys the smallest ones outright (Section 3.3).
5. **Interpreting a small singular value as a null space.** They are different
   objects: one is a limit, the other is exact, and only the second gives exact
   non-uniqueness.
6. **Forgetting that $u_i$ and $v_i$ are defined up to sign.** A reported singular
   vector's sign is a convention; magnitudes and relative signs within a vector are
   not.
7. **Truncating without stating the assumed model content of the discarded
   directions.** Truncation asserts that the model has no component along $v_{p+1}$,
   which is a physical claim.
8. **Comparing singular-value spectra of matrices with different physical units.**
   $\sigma_i$ has the units of (data)/(model), so a spectrum is only comparable
   across parameterisations of the same physics.
9. **Assuming the SVD is expensive.** For $m \times n$ with $m \ge n$ it costs about
   $4mn^{2} - \tfrac43n^{3}$; for a $10^{4} \times 10^{2}$ kernel it is trivial, and
   for larger problems randomised and Lanczos variants apply.
10. **Using an SVD of a poorly scaled matrix and blaming the algorithm.** Centre and
    scale first ([01-07-07](./07-orthogonality.md) Section 3.4).

## 8. Real-world applications

- **Tomographic inversion with resolution analysis.** The resolution matrix, the
  data kernel and the model covariance are all SVD constructions, and reporting them
  is standard practice in body-wave, surface-wave and full-waveform tomography. See
  [06-seismology](../../06-seismology/README.md) and
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md).
- **Truncated SVD and Tikhonov regularisation.** TSVD is the reference regularisation
  and the benchmark for damped least squares, since both are filters on the singular
  spectrum. See [18-inverse-problems](../../18-inverse-problems/README.md).
- **Principal component analysis and empirical orthogonal functions.** The SVD of a
  centred data matrix *is* PCA; EOF analysis of climate or ocean fields is the same
  decomposition applied to a space–time matrix. See
  [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) and
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md).
- **Low-rank compression of operators.** Sensitivity kernels, Green's function
  libraries and covariance matrices are stored and applied in low-rank form, which is
  what makes large stochastic inversions affordable.
  See [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).
- **Noise estimation from the data themselves.** The left null space of a redundant
  survey gives data combinations that must vanish, and their residual magnitude is a
  noise estimate with no repeat measurements required.
- **Moment-tensor and focal-mechanism decomposition.** The SVD of a moment tensor
  separates it into isotropic, double-couple and compensated-linear-vector-dipole
  parts, which is standard in source-mechanism reporting. See
  [06-seismology](../../06-seismology/README.md).
- **Geodetic strain and velocity field analysis.** The SVD of a set of GPS station
  velocities separates a common-mode translation from internal deformation, and the
  spectrum shows how many modes the network resolves.
- **Image and potential-field data compression.** Gridded magnetic and gravity fields
  are frequently stored as a small number of singular triplets rather than as grids.

## 9. Further reading

- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** Chapter 2 for the decomposition and its properties, Chapter 5
  for the algorithms and their costs, including why $A^\mathsf{T}A$ is avoided.
  Level: advanced.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 4–5
  (the four subspaces), 11 (least squares), 15 (conditioning) and 31 (low-rank
  approximation). The clearest short account available. Level: intermediate to
  advanced.
- **Hansen, P. C. *Rank-Deficient and Discrete Ill-Posed Problems: Numerical Aspects
  of Linear Inversion.* SIAM.** The definitive treatment of TSVD, the Picard
  condition, and the bias–variance formulation used in Section 3.6. Level: advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** Singular-value decomposition and generalised inversion in the notation of
  geophysics, with resolution and covariance matrices. Level: intermediate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and Inverse
  Problems.* Academic Press.** The same material with worked tomographic examples and
  a full chapter on TSVD and Tikhonov methods. Level: intermediate to advanced.
- **Lawson, C. L., & Hanson, R. J. *Solving Least Squares Problems.* SIAM.** The
  classical algorithmic reference, including rank determination from the singular
  spectrum. Level: advanced.
- **Eckart, C., & Young, G. (1936). "The approximation of one matrix by another of
  lower rank." *Psychometrika* 1, 211–218.** The original theorem behind rank
  truncation. Level: research, but short and readable.
- **Jackson, D. D. (1972). "Interpretation of inaccurate, insufficient and
  inconsistent data." *Geophysical Journal of the Royal Astronomical Society* 29,
  65–74.** The paper that introduced resolution and information matrices to
  geophysics, and still the clearest statement of the ideas in Section 4.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can state the SVD for a rectangular matrix and construct it from the
      eigenproblem of $A^\mathsf{T}A$ for a small example.
- [ ] I can read all four fundamental subspaces off $U$, $\Sigma$ and $V$, with their
      dimensions.
- [ ] I can write the pseudoinverse and show that it gives the minimum-norm
      least-squares solution.
- [ ] I can interpret a singular triple as a physical channel with a gain.
- [ ] I can compute $R$ and $N$ for a small problem and interpret their diagonals.
- [ ] I can compute a model covariance from $\sigma_d$ and the singular spectrum, and
      name the worst-determined direction.
- [ ] I can apply the Picard condition to a coefficient table and decide where to
      truncate.
- [ ] I can quantify the bias and the variance for each truncation rank and explain
      why the optimal rank depends on the noise level.
- [ ] I can state the Eckart–Young theorem and use it to justify a low-rank
      approximation.
- [ ] I can explain why singular values should not be computed through
      $A^\mathsf{T}A$.

## 11. Related lessons

- [01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) — the
  un-ordered version of the same subspace picture.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  where the condition number $\sigma_{\max}/\sigma_{\min}$ comes from.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) — the
  symmetric eigenproblem this decomposition is built on.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  the projection geometry the pseudoinverse implements.
- [01-07-09 Sparse Matrices and Structured Systems](./09-sparse-matrices.md) — what to
  do when the matrix is far too large for a dense SVD.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) —
  differentiating through an SVD, which requires care precisely where the singular
  values are close.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  the singular-value expansion in infinite dimensions, where the spectrum becomes a
  continuous function and ill-posedness is a decay rate.
- [18-inverse-problems](../../18-inverse-problems/README.md) — where these tools are
  used to construct practical inversions.
