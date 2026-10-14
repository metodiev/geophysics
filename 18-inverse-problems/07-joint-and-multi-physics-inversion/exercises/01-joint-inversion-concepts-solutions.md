# Solutions — 18-07-01 Why Joint Inversion: Complementary Sensitivities

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [01 Why Joint Inversion](../01-joint-inversion-concepts.md).

---

## ★1 — Reading a resolution diagonal

$\operatorname{diag}R = (0.95, 0.62, 0.31, 0.08)$: cell 1 is essentially
recovered ($0.95$), cell 2 is mostly recovered ($0.62$), cell 3 is largely an
average of its neighbours ($0.31$), cell 4 is unresolved ($0.08$).

$$\operatorname{tr}R = 0.95+0.62+0.31+0.08 = 1.96 .$$

$\operatorname{tr}R$ is the **effective number of parameters**: four cells are
carrying the information of about two independent numbers.

---

## ★2 — Rank of a joint operator

For a stacked operator $G = [G_1; G_2]$ the rank satisfies

$$\max(r_1,r_2) \le \operatorname{rank}G \le \min(n,\; r_1+r_2)
= \min(40, 16) = 16 .$$

So any rank from 10 to 16 is possible. The demonstration measured **14**. The
sum 16 is not attained because the two operators share low-order directions
(both are smooth), so their row spaces overlap rather than being independent.

---

## ★3 — Equivalence curve

$d = H\Delta\rho = 1.2000$:

| $(\Delta\rho, H)$ | $(0.60, 2.0)$ | $(0.30, 4.0)$ | $(0.20, 6.0)$ |
|---|---|---|---|
| $H\Delta\rho$ | 1.20000 | 1.20000 | 1.20000 |

For $H = 4.5$ km: $\Delta\rho = 1.2000/4.5 = 0.2667\ \mathrm{g\,cm^{-3}}$.

---

## ★4 — Joint posterior for the two-parameter problem

With $G = \left(\begin{smallmatrix}\Delta\rho & H\\ 1 & 0\end{smallmatrix}\right)
= \left(\begin{smallmatrix}0.30 & 4.00\\ 1 & 0\end{smallmatrix}\right)$ and
$C_d = \operatorname{diag}(0.020^2, 0.10^2) = \operatorname{diag}(4\times10^{-4}, 10^{-2})$,

$$G^{T}C_d^{-1}G =
\begin{pmatrix}
\dfrac{0.30^2}{4\times10^{-4}} + \dfrac{1}{10^{-2}} & \dfrac{0.30\cdot4}{4\times10^{-4}}\\[2mm]
\dfrac{0.30\cdot4}{4\times10^{-4}} & \dfrac{4^2}{4\times10^{-4}}
\end{pmatrix}
=
\begin{pmatrix}
225 + 100 & 3000\\ 3000 & 40000
\end{pmatrix}.$$

Determinant: $325\times40000 - 3000^2 = 1.3\times10^{7} - 9.0\times10^{6}
= 4.0\times10^{6}$. Hence

$$C_{\text{post}} = \frac{1}{4.0\times10^{6}}
\begin{pmatrix} 40000 & -3000\\ -3000 & 325\end{pmatrix}
= \begin{pmatrix} 1.000\times10^{-2} & -7.5\times10^{-4}\\
-7.5\times10^{-4} & 8.125\times10^{-5}\end{pmatrix},$$

$$\sigma_H = \sqrt{10^{-2}} = 0.1000\ \mathrm{km},\qquad
\sigma_{\Delta\rho} = \sqrt{8.125\times10^{-5}} = 0.0090\ \mathrm{g\,cm^{-3}},$$

$$\rho_{H\Delta\rho} = \frac{-7.5\times10^{-4}}{0.1000\times0.0090} = -0.833 .$$

✔ matches the demonstration's $-0.832$ (round-off in the interpolation of the
printed digits).

For $\rho = 0.9$, $C_d = \left(\begin{smallmatrix}4\times10^{-4} & 1.8\times10^{-3}\\
1.8\times10^{-3} & 10^{-2}\end{smallmatrix}\right)$,
$\det C_d = 4\times10^{-6} - 3.24\times10^{-6} = 7.6\times10^{-7}$, and
$C_d^{-1} = \frac{1}{7.6\times10^{-7}}\left(\begin{smallmatrix}10^{-2} & -1.8\times10^{-3}\\
-1.8\times10^{-3} & 4\times10^{-4}\end{smallmatrix}\right)$; the demo reports
$\sigma_{\Delta\rho} = 0.0037$ and $\sigma_H = 0.1000$ — **the depth uncertainty
is unchanged**, only the parameter that the null direction concerned improves.

---

## ★5 — Gain and limitation

*Gain.* "Combining the two operators raised the mean model resolution from 0.15
and 0.25 to 0.35 and the rank at a $10^{-3}$ cut from 6 and 10 to 14, so the
joint model is better resolved everywhere than either single-method model."

*Limitation.* "Thirty-five of forty cells still have
$\operatorname{diag}R < 0.5$, so the joint result remains an average over
several cells and must be reported with its resolution width rather than as a
layer-by-layer structure."

---

## ★6 — Second-order residual of the tangent step

Truth $(4.00, 0.30)$, $n = (H,-\Delta\rho)/\|(H,-\Delta\rho)\|$,
$\|(4,-0.3)\| = 4.0112$, so $n = (0.99721,-0.07479)$. With step 0.50:

$$H = 4.00 + 0.50(0.99721) = 4.4986,\qquad
\Delta\rho = 0.30 + 0.50(-0.07479) = 0.26260,$$

$$H\Delta\rho = 4.4986\times0.26260 = 1.18135 .$$

The first-order prediction is $1.20000$ (change 0). The actual change is
$-0.01865$, which is second order: the leading term is
$t^2 n_H n_{\Delta\rho} = 0.25\,(0.99721)(-0.07479) = -0.01865$ ✔ exactly.

---

## ★7 — Removing the ambiguity without measuring $H$

A workable design: keep the gravity-like datum $d_1 = H\Delta\rho$ and add a
second measurement with a *known, differently shaped* kernel that also depends on
$H$ and $\Delta\rho$, for example a reading at a different offset whose kernel
$K_2(H)$ multiplies the same mass anomaly:

$$d_2 = \Delta\rho\,K_2(H).$$

Then the joint gradient matrix is
$\left(\begin{smallmatrix}\Delta\rho & H\\ K_2 & \Delta\rho K_2'(H)\end{smallmatrix}\right)$,
which is full rank wherever $K_2$ actually varies with depth (i.e. $K_2'(H)\ne0$
and the two rows are not proportional). The joint rank is 2, versus 1 for either
datum alone. The quantity that decides success is the smallest singular value of
the scaled, noise-normalised Jacobian: if it is below the noise level, the
ambiguity survives. A kernel that is flat in $H$ (for example an infinitely wide
sheet) adds no rank at all.

---

## ★8 — Correlated errors and a reporting rule

An example producing $\rho<0$: the two data sets are processed with the same
elevation datum that is *mis-set by a constant offset*, one survey measuring a
quantity that increases with that offset and the other a quantity that decreases
with it. The shared processing error then enters the two residuals with opposite
sign, giving negative correlation.

Practical rule: when $\rho$ is unknown, report the uncertainty band spanned by
$\rho \in \{-1,0,+1\}$ (or by the defensible range) alongside the $\rho=0$
figure, and state explicitly that the narrowest value is conditional on an
assumption the data do not test. In the demonstration that band is
$0.0037$–$0.0122\ \mathrm{g\,cm^{-3}}$, a factor of 3.3.
