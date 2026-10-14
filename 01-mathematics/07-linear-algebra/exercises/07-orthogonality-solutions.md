# Solutions — 01-07-07 Orthogonality, Projections and Least Squares

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified. All arithmetic here is small enough to
> check by hand.

---

## ★1 — A least-squares line

Points $(0,1), (1,2), (2,2), (3,4)$; model $y = a + bx$.

(a)

$$G = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3\end{bmatrix}, \qquad
G^\mathsf{T}G = \begin{bmatrix} 4 & 6 \\ 6 & 14\end{bmatrix}, \qquad
G^\mathsf{T}d = \begin{bmatrix} 9 \\ 18\end{bmatrix},$$

using $\sum 1 = 4$, $\sum x = 6$, $\sum x^{2} = 14$, $\sum y = 9$,
$\sum xy = 0 + 2 + 4 + 12 = 18$. Then

$$a = \frac{14(9) - 6(18)}{4(14) - 36} = \frac{126 - 108}{20} = 0.9, \qquad
b = \frac{4(18) - 6(9)}{20} = \frac{18}{20} = 0.9 .$$

So the fitted line is $y = 0.9 + 0.9x$.

(b) Residuals $r_i = y_i - (0.9 + 0.9x_i)$:

$$r = (0.1,\ 0.2,\ -0.7,\ 0.4), \qquad \|r\| = 0.8366600265 .$$

(c) $G^\mathsf{T}r$:

$$\begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3\end{bmatrix}
\begin{bmatrix} 0.1 \\ 0.2 \\ -0.7 \\ 0.4\end{bmatrix}
= \begin{bmatrix} 0.1 + 0.2 - 0.7 + 0.4 \\ 0 + 0.2 - 1.4 + 1.2\end{bmatrix}
= \begin{bmatrix} 0 \\ 0\end{bmatrix}. ✓$$

In words: **the residuals contain no mean offset and no linear trend in $x$.** Those are
exactly the two things the model can represent, so orthogonality to the column space
means the fit has extracted everything of that kind from the data. A plot of residuals
against $x$ showing a trend is a proof that the fit is not least squares (or that the
model is wrong).

(d) The residuals sum to $0.1+0.2-0.7+0.4 = 0$ ✓, which is the first component of
$G^\mathsf{T}r = 0$: orthogonality to the constant column forces the mean to vanish.

---

## ★2 — The gradient from components

$$\phi(m) = \tfrac12\sum_{i}\left(\sum_j G_{ij}m_j - d_i\right)^{2}.$$

Differentiate with respect to one component $m_k$. The chain rule gives

$$\frac{\partial\phi}{\partial m_k}
= \sum_i \left(\sum_j G_{ij}m_j - d_i\right)\frac{\partial}{\partial m_k}
\left(\sum_j G_{ij}m_j\right)
= \sum_i G_{ik}\left(\sum_j G_{ij}m_j - d_i\right) .$$

Now assemble: the last expression is the $k$-th component of
$G^\mathsf{T}(Gm - d)$, since
$\left(G^\mathsf{T}(Gm-d)\right)_k = \sum_i (G^\mathsf{T})_{ki}(Gm-d)_i
= \sum_i G_{ik}(Gm-d)_i$. Hence

$$\nabla_m\phi = G^\mathsf{T}(Gm - d). ✓$$

**The two-index structure is the whole content:** $G_{ij}$ appears once as $G_{ij}$ (in
the bracket) and once as $G_{ik}$ (multiplying), which is why the answer is
$G^\mathsf{T}$ times a residual and not $G$ times anything. Setting the gradient to zero
gives $G^\mathsf{T}Gm = G^\mathsf{T}d$.

**Regularised variant.** For
$\phi_\alpha(m) = \tfrac12\|Gm-d\|^{2} + \tfrac{\alpha}{2}\|Dm\|^{2}$ the second term has
gradient $\alpha D^\mathsf{T}Dm$, so stationarity gives

$$(G^\mathsf{T}G + \alpha D^\mathsf{T}D)m = G^\mathsf{T}d ,$$

the Tikhonov normal equations — derived rather than remembered.

---

## ★★3 — The projection matrix and leverages

(a) $\det(G^\mathsf{T}G) = 56 - 36 = 20$, so

$$(G^\mathsf{T}G)^{-1} = \frac{1}{20}\begin{bmatrix} 14 & -6 \\ -6 & 4\end{bmatrix}
= \begin{bmatrix} 0.7 & -0.3 \\ -0.3 & 0.2\end{bmatrix},$$

$$P = G(G^\mathsf{T}G)^{-1}G^\mathsf{T} =
\begin{bmatrix}
0.7 & 0.4 & 0.1 & -0.2 \\
0.4 & 0.3 & 0.2 & 0.1 \\
0.1 & 0.2 & 0.3 & 0.4 \\
-0.2 & 0.1 & 0.4 & 0.7
\end{bmatrix}.$$

(b) Leverages are the diagonal: $h = (0.7,\ 0.3,\ 0.3,\ 0.7)$ and
$\sum h_i = 2.000000$ ✓ — equal to the number of parameters, as always.

(c) $P$ is symmetric by inspection (it is $G$ times a symmetric matrix times
$G^\mathsf{T}$), and $P^{2} = P$ holds to $\max|P^{2} - P| = 3.33\times10^{-16}$ ✓. It is
a projection, not a rescaling.

(d) The largest leverage, $h = 0.7$, is at $x = 0$ and $x = 3$ — the two *endpoint*
stations. In a straight-line fit the endpoints determine the slope, so a blunder at
either end has the largest effect on the fitted trend, and a blunder in the middle is
partly absorbed by the intercept.

(e) The change in the fitted parameters from a perturbation $\delta d$ is
$(G^\mathsf{T}G)^{-1}G^\mathsf{T}\delta d$, whose slope row is
$(-0.3,\ -0.1,\ 0.1,\ 0.3)$ against the four stations. So:

| blunder | change in slope |
|---|---|
| $+1.0$ at $x = 0$ (leverage $0.7$) | $-0.300$ |
| $+1.0$ at $x = 3$ (leverage $0.7$) | $+0.300$ |
| $+1.0$ at $x = 1$ (leverage $0.3$) | $-0.100$ |

A blunder at an endpoint moves the slope three times as much as the same blunder at
$x = 1$. Note also the signs: an error at $x = 3$ tilts the line up, an error at $x = 0$
tilts it down. **Practical consequence:** in a trend-removal step, a bad datum at the
edge of the profile is the most damaging single error you can make, and it is worth
checking the edge stations first.

---

## ★★4 — QR, and why it is used

(a) For the first column $g_1$ of $G$, form $x = g_1$ and
$\alpha = -\operatorname{sign}(x_1)\|x\|$. Set

$$v = x - \alpha e_1, \qquad H = I - \frac{2vv^\mathsf{T}}{v^\mathsf{T}v}.$$

$H$ is symmetric and orthogonal ($H^{2} = I$), and $Hx = \alpha e_1$: the choice of
sign for $\alpha$ (opposite to $x_1$) ensures that $x - \alpha e_1$ does not suffer
cancellation, so $\|v\|$ is as large as it can be and the transformation is accurate.
Applying $H$ to $G$ and to the right-hand side removes the first column below the
diagonal; repeating on the successive subcolumns produces $R$ upper triangular and
accumulates $Q$.

(b) **$\kappa_2(R) = \kappa_2(G)$.** $G = QR$ with $Q$ orthogonal, so the singular values
of $G$ and of $R$ are identical ($R = Q^\mathsf{T}G$, and orthogonal multiplication on
the left preserves singular values). Hence $\sigma_{\max}/\sigma_{\min}$ is the same for
the triangular factor as for the original matrix. In contrast,
$\kappa_2(G^\mathsf{T}G) = \kappa_2(G)^{2}$.

(c) "Losing eight of sixteen digits" means $\kappa \ge 10^{8}$ for the matrix actually
solved. For the normal equations that matrix is $G^\mathsf{T}G$, so the condition is

$$\kappa_2(G)^{2} \ge 10^{8} \;\Longrightarrow\; \kappa_2(G) \ge 10^{4} .$$

(d) At $\kappa_2(G) = 10^{4}$ the QR route retains about $16 - 4 = 12$ digits. The
normal-equation route retains about $16 - 8 = 8$: a loss of four orders of magnitude in
accuracy for the same mathematical problem, produced entirely by the squaring.

---

## ★★★5 — Weighted least squares

(a) For independent measurements the covariance is
$C_d = \operatorname{diag}(0.1^{2},\ 1.0^{2}) = \operatorname{diag}(0.01,\ 1)$, so the
weights are $w = C_d^{-1} = (100,\ 1)$.

(b) With $G = (1,1)^\mathsf{T}$ (a single parameter, the mean),

$$\hat m_W = \frac{\sum w_i d_i}{\sum w_i} = \frac{100(10.0) + 1(11.0)}{101}
= \frac{1011}{101} = 10.00990099 ,$$

and the unweighted mean is $(10.0+11.0)/2 = 10.5$.

(c) **Variances.** The weighted estimator is unbiased with

$$\operatorname{Var}(\hat m_W) = \frac{1}{\sum w_i} = \frac{1}{101}
= 9.900990\times10^{-3} .$$

The unweighted estimator $\hat m_U = (d_1 + d_2)/2$ has

$$\operatorname{Var}(\hat m_U) = \tfrac14\left(\sigma_1^{2} + \sigma_2^{2}\right)
= \tfrac14(0.01 + 1.0) = 0.2525 .$$

(d) Standard deviations: $\hat m_W$ gives $0.0995045$, $\hat m_U$ gives $0.502494$. The
efficiency ratio (variance ratio) is $0.2525/0.009901 = 25.5$: the unweighted estimator
is $5.05$ times worse in standard deviation, and it "wastes" all but $1/25.5$ of the
information in the better measurement.

(e) The unweighted answer is not merely inefficient but **wrong as an answer to the
stated question**: it implicitly asserts $C_d \propto I$, i.e. that the two
measurements have equal uncertainty, which contradicts the reported uncertainties. If
you believe $\pm0.1$, you must weight; if you do not, the quoted uncertainties are
false. There is no third option in which both statements are true.

**Sanity check.** The weighted mean $10.0099$ lies much closer to the precise datum
$10.0$ than to the imprecise $11.0$ — correct, since $100:1$ weights say the first
measurement is a hundred times more informative. Had one measurement been reported to
two decimal places and the other to one, the same conclusion would apply on
significant-figure grounds alone.

---

## ★★★6 — Orthogonal polynomials and basis conditioning

Data: $z = 0, 200, \ldots, 1400$ m, $g = 25.0 - 0.3086z + \epsilon$ mGal with the
lesson's deterministic perturbations.

(i) **Conditioning.** Using $\kappa_2(G) = \sqrt{\kappa_2(G^\mathsf{T}G)}$ from the
eigenvalues of $G^\mathsf{T}G$:

| basis | $\kappa_2(G)$ | $\kappa_2(G^\mathsf{T}G)$ |
|---|---|---|
| centred and scaled, $s = (z-700)/1400$ | $4.075\times10^{1}$ | $1.660\times10^{3}$ |
| raw monomial, $z$ in metres | $3.252\times10^{9}$ | $1.057\times10^{19}$ |

The raw basis has a *condition number larger than $1/\epsilon_{\text{mach}}$ for
$G^\mathsf{T}G$*: the normal equations are numerically singular there, while $G$ itself
remains usable ($3.3\times10^{9}$ leaves about six digits).

(ii) **Fitted values** at the eight stations (mGal), from the centred basis:

$$(25.032727,\ -36.712186,\ -98.444394,\ -160.167835,\ -221.886450,\
-283.604177,\ -345.324957,\ -407.052727),$$

and the raw basis gives the same values to the printed digits.

(iii) **Maximum difference between the two sets of fitted values:**
$9.27\times10^{-13}$ mGal — i.e. agreement to twelve digits, against a fit residual of
order $0.12$ mGal.

(iv) **Parameters are not comparable directly**, because the bases differ. Converted to
common units (coefficients of $1, z, z^{2}, z^{3}$ in metres) the centred fit gives
$(25.032727,\ -0.3087629,\ 2.081\times10^{-7},\ -8.2\times10^{-11})$, essentially the
same numbers as the raw fit. Their *accuracies* are not the same, however: against an
exact rational reference solution, the raw-basis parameter vector from the normal
equations has a maximum relative error of $1.15\times10^{-10}$ — about ten digits lost —
against $2.16\times10^{-12}$ for QR on the same matrix, and both of the centred-basis
routes are at about $2.7\times10^{-12}$.

**Why the fitted values agree while the parameters do not.** The fitted values are
$G\hat m = P d$, a projection of the data onto the column space — an operation that is
stable because it never divides by a small singular value. The parameters are
$\hat m = G^{+}d = \sum_i (u_i^\mathsf{T}d/\sigma_i)v_i$, a sum in which the weak
directions are divided by small $\sigma_i$. A change of basis $G \to GP$ leaves the
column space — and therefore every fitted value — unchanged, while moving the
parameters by $P^{-1}$; and the condition number of $G$ changes with $P$. So:

- **Trust fitted values and predictions.** They are properties of the data and the model
  space, not of the parameterisation.
- **Never trust individual parameters without reporting the basis and its condition
  number.** A coefficient of $z^{3}$ in metres is not a physical quantity that can be
  quoted to nine digits; it is a bookkeeping device whose uncertainty is enormous.
- **The practical remedy** is to centre and scale the basis (making it
  near-orthogonal) *and* to solve with QR or an SVD rather than the normal equations.
  Both are free, and either alone is insufficient: QR alone leaves six digits in the raw
  basis, and centring alone still squares an unnecessarily large condition number.
