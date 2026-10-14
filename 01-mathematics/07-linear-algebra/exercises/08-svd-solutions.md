# Solutions — 01-07-08 Singular Value Decomposition and Rank Truncation

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified. Singular vectors are defined up to sign;
> the signs quoted here follow the convention used by the companion script (first
> component positive).

---

## ★1 — A small SVD by hand

$$A = \begin{bmatrix} 3 & 0 \\ 4 & 0 \\ 0 & 1\end{bmatrix}
\quad (3\times2).$$

(a) $A^\mathsf{T}A = \begin{bmatrix} 25 & 0 \\ 0 & 1\end{bmatrix}$, so the eigenvalues are
$25$ and $1$, the singular values are $\sigma = (5, 1)$, and the eigenvectors are
$v_1 = (1,0)$, $v_2 = (0,1)$, so $V = I$.

The left singular vectors: $u_1 = Av_1/\sigma_1 = (3,4,0)^\mathsf{T}/5 = (0.6,0.8,0)$,
$u_2 = Av_2/\sigma_2 = (0,0,1)^\mathsf{T}$. Complete the basis of $\mathbb{R}^{3}$ with
$u_3 = (-0.8, 0.6, 0)^\mathsf{T}$ (orthogonal to both, unit length). Hence

$$U = \begin{bmatrix} 0.6 & 0 & -0.8 \\ 0.8 & 0 & 0.6 \\ 0 & 1 & 0\end{bmatrix},
\qquad
\Sigma = \begin{bmatrix} 5 & 0 \\ 0 & 1 \\ 0 & 0\end{bmatrix}, \qquad
V = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix}.$$

(b) $\operatorname{rank}A = 2$ (both singular values are positive), and
$\kappa_2 = 5/1 = 5$: a well-conditioned matrix.

(c) $\Sigma^{+} = \begin{bmatrix} 0.2 & 0 & 0 \\ 0 & 1 & 0\end{bmatrix}$, so

$$A^{+} = V\Sigma^{+}U^\mathsf{T} = \begin{bmatrix} 0.2 & 0 & 0 \\ 0 & 1 &
0\end{bmatrix}\begin{bmatrix} 0.6 & 0.8 & 0 \\ 0 & 0 & 1 \\ -0.8 & 0.6 &
0\end{bmatrix}
= \begin{bmatrix} 0.12 & 0.16 & 0 \\ -0.8 & 0.6 & 0\end{bmatrix}.$$

**Check:** $A^{+}A = \begin{bmatrix} 0.12 & 0.16 & 0 \\ -0.8 & 0.6 &
0\end{bmatrix}\begin{bmatrix} 3 & 0 \\ 4 & 0 \\ 0 & 1\end{bmatrix} =
\begin{bmatrix} 0.36+0.64 & 0 \\ -2.4+2.4 & 0\end{bmatrix} = I_{2}$. ✓

(d) $U\Sigma V^\mathsf{T}$: the first column of $U$ times $5$ gives $(3,4,0)$, the second
column times $1$ gives $(0,0,1)$, so the product is
$\begin{bmatrix} 3 & 0 \\ 4 & 0 \\ 0 & 1\end{bmatrix} = A$ ✓.

---

## ★2 — The four subspaces from the SVD

(a)–(b) With $r = 2$, $m = 3$, $n = 2$:

| subspace | basis | dimension |
|---|---|---|
| $\mathcal{C}(A)$ | $u_1 = (0.6,0.8,0),\ u_2 = (0,0,1)$ | $2$ |
| $\mathcal{N}(A^\mathsf{T})$ | $u_3 = (-0.8,0.6,0)$ | $1$ |
| $\mathcal{C}(A^\mathsf{T})$ | $v_1 = (1,0),\ v_2 = (0,1)$ | $2$ |
| $\mathcal{N}(A)$ | none — the null space is $\{\mathbf{0}\}$ | $0$ |

(c) Rank–nullity: columns, $r + \dim\mathcal{N}(A) = 2 + 0 = 2 = n$ ✓; rows,
$r + \dim\mathcal{N}(A^\mathsf{T}) = 2 + 1 = 3 = m$ ✓.

**Geophysical reading.** $\mathcal{C}(A)$ is the set of achievable data — in a
ray-geometry language, the data patterns any model could produce. The single left null
vector $u_3$ is the "impossible" data direction: any measured data vector with a
component along $u_3$ is unexplained by the model, and that component *is* the residual.
Because $u_2 = (0,0,1)$ is one of the basis vectors, the third datum is entirely
independent of the other two: the survey has no redundancy at all in the data space
beyond the unavoidable third component.

---

## ★★3 — Adding a duplicate ray

(a) **Prediction.** The new row is *identical* to row 1, so it spans no new direction in
the row space: the rank stays 3, $\sigma_1$ and $\sigma_2$ change only slightly (the extra
row changes the column norms and hence the row-space geometry), and $\sigma_3$ — the
direction that depends on the $2$ % path-length difference between rays 1 and 2 — is
essentially unchanged in *structure* because the new ray carries no information about the
difference. Since the new row is parallel to an existing one, it cannot resolve
$m_1 - m_2$. Expect $\sigma_3$ to change by a few per cent, and $\kappa$ similarly.

(b) **Computed:**

| kernel | $\sigma_1$ | $\sigma_2$ | $\sigma_3$ | $\kappa_2$ |
|---|---|---|---|---|
| five rays | $2.252327122$ | $1.103315518$ | $0.010835222$ | $207.870881$ |
| six rays | $2.657398328$ | $1.108373998$ | $0.011882972$ | $223.630791$ |

$\sigma_3$ rose by only $9.7$ % ($0.010835 \to 0.011883$) while $\kappa$ rose by $7.6$ %.
The prediction was correct: duplicating a ray does not improve the resolution of the weak
direction.

(c) The smallest singular value measures how strongly a *model* combination couples to
the data. The new ray's path lengths are $(1,1,0)$ — exactly proportional to ray 1 — so
the only way it could distinguish cells 1 and 2 would be through a difference in path
lengths *between its own two entries*, and there is none. The information about
$m_1 - m_2$ resides exclusively in the $2$ % contrast between rays 1 and 2, and no number
of rays parallel to either of them can add to it. Adding data strengthens whatever
directions the data already span and leaves the orthogonal directions exactly as weak as
before.

(d) **Leverage (diagonal of $N = U_rU_r^\mathsf{T}$):**

| kernel | leverages | mean $r/m$ |
|---|---|---|
| five rays | $(0.689655,\ 1.000000,\ 0.827586,\ 0.310345,\ 0.172414)$ | $0.600$ |
| six rays | $(0.408163,\ 1.000000,\ 0.816327,\ 0.265306,\ 0.102041,\ 0.408163)$ | $0.500$ |

The new datum is a duplicate of an existing one, so the total information ($r = 3$) is
spread over six data instead of five, and the *mean* leverage falls from $0.6$ to $0.5$.
Rays 1 and 6 now have identical leverage ($0.408163$), which is the arithmetic signature
of identical rows. **The new datum contributes no information about the model**; it
contributes only a repeat measurement, useful for estimating noise and nothing else.

---

## ★★4 — A three-station, two-parameter survey

$$G = \begin{bmatrix} 1 & 1 \\ 1 & 1.1 \\ 1 & 1.2\end{bmatrix}, \qquad
d = (0.03,\ 0.032,\ 0.034)^\mathsf{T}\ \text{s}.$$

(a) $G^\mathsf{T}G = \begin{bmatrix} 3 & 3.3 \\ 3.3 & 3.65\end{bmatrix}$. Singular values
$\sigma = (2.577007018,\ 0.095051730)$ and $\kappa_2 = 27.111627$. The least-squares
solution is

$$\hat m = (0.010000000,\ 0.020000000)\ \mathrm{s/km}, \qquad
G\hat m = (0.03,\ 0.032,\ 0.034)^\mathsf{T} = d \quad\text{exactly},$$

so the residual is zero: the three data lie exactly on the line traced out by the model,
because they were constructed that way.

(b) Since $G$ has full column rank and $m = 3 > n = 2$:

$$R = I_{2} \quad (\text{model fully resolved, no null space}),$$
$$N = U_2U_2^\mathsf{T} = \begin{bmatrix} 0.833333 & 0.333333 & -0.166667 \\
0.333333 & 0.333333 & 0.333333 \\ -0.166667 & 0.333333 & 0.833333\end{bmatrix},
\qquad \operatorname{tr}N = 2 .$$

The leverages are $(0.833333,\ 0.333333,\ 0.833333)$: the two outer stations carry most
of the information and the middle one is largely redundant — the same pattern as the
linear-trend fit of [01-07-07](./07-orthogonality-solutions.md), and for the same reason.

(c) $C_m = \sigma_d^{2}(G^\mathsf{T}G)^{-1}$. With $\det(G^\mathsf{T}G) = 3(3.65) -
3.3^{2} = 0.06$,

$$(G^\mathsf{T}G)^{-1} = \frac{1}{0.06}\begin{bmatrix} 3.65 & -3.3 \\ -3.3 & 3\end{bmatrix}
= \begin{bmatrix} 60.833333 & -55 \\ -55 & 50\end{bmatrix},$$

$$C_m = 10^{-6}\begin{bmatrix} 60.833333 & -55 \\ -55 & 50\end{bmatrix}, \qquad
\operatorname{diag}(C_m)^{1/2} = (7.799573\times10^{-3},\ 7.071068\times10^{-3})\
\mathrm{s/km}.$$

Along the singular directions the standard deviations are $\sigma_d/\sigma_i$:

$$i = 1: \frac{10^{-3}}{2.577007} = 3.880\times10^{-4}, \qquad
i = 2: \frac{10^{-3}}{0.095052} = 1.052\times10^{-2}\ \mathrm{s/km}.$$

(d) **Determined:** the sum-like combination $v_1$, to $3.9\times10^{-4}$ s/km — very
well. **Not determined:** the difference-like combination $v_2$, to
$1.05\times10^{-2}$ s/km, which is $21$ % of a $0.05$ s/km model. So the survey decides
the overall level of the two cells and is weak on their contrast — the same
depth–velocity-style trade-off seen from the singular-value side.

---

## ★★★5 — Bias, variance and the optimal truncation rank

(a)–(b) With $\sigma_d = 10^{-3}$ s and $m_{\text{true}} = (0.05,-0.02,0.03)$:

| $p$ | squared bias $\|(I-R_p)m\|^{2}$ | $\operatorname{tr}C_m^{(p)}$ | total | optimum |
|---|---|---|---|---|
| 1 | $3.238819\times10^{-3}$ | $1.971\times10^{-7}$ | $3.239016\times10^{-3}$ | |
| 2 | $2.455110\times10^{-3}$ | $1.0186\times10^{-6}$ | $2.456129\times10^{-3}$ | **yes** |
| 3 | $0$ | $8.518759\times10^{-3}$ | $8.518759\times10^{-3}$ | |

The optimum is $p = 2$: dropping the weak channel costs a bias of
$2.46\times10^{-3}$ (squared; the bias itself is $0.04955$ s/km) but saves a variance of
$7.5\times10^{-3}$ (squared).

(c) **Noise dependence of the optimum:**

| $\sigma_d$ (s) | $p=1$ total | $p=2$ total | $p=3$ total | optimum |
|---|---|---|---|---|
| $10^{-5}$ | $3.2388\times10^{-3}$ | $2.4551\times10^{-3}$ | $8.519\times10^{-7}$ | **3** |
| $10^{-3}$ | $3.2390\times10^{-3}$ | $2.4561\times10^{-3}$ | $8.519\times10^{-3}$ | **2** |
| $10^{-1}$ | $5.2100\times10^{-3}$ | $1.2641\times10^{-2}$ | $8.5188\times10^{1}$ | **1** |

The optimal rank moves $3 \to 2 \to 1$ as the noise increases by four orders of
magnitude in each direction.

(d) **Why.** The bias is fixed by the model content of the discarded directions and does
not depend on the data at all; the variance is proportional to $\sigma_d^{2}$. Adding one
more channel therefore costs a fixed bias $\|v_{p+1}^{\mathsf{T}}m\|^{2}$ and buys a
variance reduction $\sigma_d^{2}/\sigma_{p+1}^{2}$ along that direction. When the noise is
tiny, every channel is worth including; when it is large, only the strong channels pay
their way. **One-line criterion:** include channel $i$ if and only if its data
coefficient exceeds the noise level in that direction,

$$|u_i^\mathsf{T}d| \;>\; \tau\,\sigma_d \quad\text{for some threshold } \tau \text{ near } 1 ,$$

which is the **discrepancy principle**: stop when the remaining channels no longer
improve the fit by more than the data uncertainty allows. It is equivalent to the
trade-off computed above and is much cheaper, because it needs no model and no iteration
over $p$.

---

## ★★★6 — Low-rank compression of a two-dimensional field

**Construction used here.** Two rotated elliptical anomalies on a $12\times12$ grid —
that is the field of the companion script
([`../code/svd_resolution_demo.py`](../code/svd_resolution_demo.py)), and it is reported
here rather than a prism computation so that the numbers can be reproduced by running
it. A reader who computes the vertical gravity of two rectangular prisms numerically
will obtain a spectrum of the same shape, because the argument below depends only on
smoothness.

(a) **Spectrum** (largest six): $1.396883$, $1.223562$, $0.335839$, $0.308150$,
$0.078481$, $0.060650$, with $\|F\|_F = 1.914740$. The smallest singular value is
$1.302\times10^{-6}$, so the numerical rank is 12; the spectrum decays by two orders of
magnitude over the first ten values and then flattens at the round-off level (the field
is a finite-precision discretisation of a non-separable function).

(b) **Rank-$p$ relative Frobenius error:**

| $p$ | relative error | energy kept |
|---|---|---|
| 1 | $0.68393621$ | $0.53223126$ |
| 2 | $0.24376018$ | $0.94058098$ |
| 3 | $0.16927777$ | $0.97134503$ |
| 4 | $0.05248537$ | $0.99724529$ |
| 5 | $0.03278314$ | $0.99892527$ |
| 6 | $0.00844994$ | $0.99992860$ |
| $12$ | $0$ | $1$ |

(c) **Rank for 1 % accuracy: 6** (relative error $0.00845$), out of 12 possible — exactly
the same count as for the lesson's field, which is not a coincidence: both fields are
composed of two smooth, rotated, anisotropic features, and the spectrum of such a field is
controlled by (i) the number of features and (ii) how anisotropic they are.

(d) **Deeper and smoother means lower effective rank.** A source at depth $d$ produces a
field whose spatial spectrum is attenuated relative to a shallow source by roughly
$e^{-kd}$ at wavenumber $k$ — the upward-continuation factor. Higher wavenumbers — short
wavelengths, and therefore fine detail — are suppressed exponentially, so the field
becomes smooth and its singular-value spectrum decays faster: fewer terms are needed for a
given accuracy. The same factor is what makes deep sources poorly resolved: a fine grid
cannot distinguish models that differ only in their high-wavenumber content, because
those differences attenuate before reaching the surface. **The low effective rank of the
field and the ill-conditioning of the inversion are the same phenomenon**, viewed from
the data side and the model side respectively. That is the resolution discussion of
Section 4 of the lesson in the language of spectra.
