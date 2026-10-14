# Solutions — 05-03-03 Superposition and Building Complex Models

> Numbers marked *verified* were computed.

---

## ★1

$F[\alpha\mathbf{m}_1+\beta\mathbf{m}_2] = \alpha F[\mathbf{m}_1]+\beta
F[\mathbf{m}_2]$; in matrix form
$\mathbf{G}(\mathbf{m}_1+\mathbf{m}_2) = \mathbf{G}\mathbf{m}_1+
\mathbf{G}\mathbf{m}_2$.

---

## ★2

Gravity: linear in density (exact). Magnetics: linear in magnetisation if
demagnetisation is neglected; not linear in susceptibility otherwise. DC
resistivity: linear in potential for fixed conductivity, non-linear in
conductivity. Seismic amplitude: not linear in general; only in the weak-
scattering (Born) approximation.

---

## ★3

Maxwell's equations with fixed conductivity are linear, so potentials and fields
superpose. But resistivity is the inverse of the coefficient in that equation,
so doubling the conductivity does not double the potential — the relationship
between the *measured* quantity and the *parameter of interest* is non-linear
even though the physics is linear.

---

## ★★4

Because the kernel is not constant across the body: the prism whose edge is
further from the observation contributes less, and the two prisms' anomalies
overlap with different weights. The sum is the convolution of the single-prism
response with the two-point geometry, so the combined anomaly is wider and
flatter-topped than twice a single prism, and its maximum is *less* than twice
the single-prism maximum.

---

## ★★5 *(verified)*

$\sigma_\text{residual} = \sqrt{0.2^2+0.9^2} = 0.922$ mGal, versus 0.9 mGal
from the regional alone and 0.2 mGal from the data alone. The residual is
9.0 − 8.4 = 0.6 mGal with an uncertainty of 0.92 mGal — **smaller than its own
error bar**. The subtraction was arithmetically valid but scientifically
useless: the uncertainty in the nuisance model dominates. The lesson is that
subtracting a poorly known contribution makes the residual *less* informative
than the original data.

---

## ★★6 *(verified)*

$\chi_\text{eff} = \chi/(1+\chi/3) = 0.5/1.166667 = 0.428571$. The linear
(non-demagnetised) calculation overestimates the magnetisation by
$\chi/\chi_\text{eff} = 1+\chi/3 = 1.1667$, i.e. **16.7%**.

---

## ★★★7

Expected: summation and quadrature agree to the numerical precision of the
quadrature (of order $10^{-14}$ relative for Gauss–Legendre with enough nodes);
the quadrature is the reference because it does not rely on the prism formula's
own algebra being correct — but if the quadrature also uses the prism kernel, the
test is weaker. The strongest test uses two genuinely different formulations
(e.g. prism closed form versus volume quadrature using the point-mass kernel
per sub-volume).

A 5 m displacement of one prism changes the anomaly by an amount that is one
column of $\mathbf{G}$ times the density: this is the model's sensitivity, and
comparing it with the noise level says whether that prism's position is
constrained at all.

---

## ★★★8 *(verified)*

| $\chi$ | $1+\chi/3$ (overestimate factor) |
|---|---|
| 0.2 | 1.067 |
| 0.5 | 1.167 |
| 1.0 | 1.333 |

The 10% threshold is reached at $\chi = 0.3$ for a sphere. It depends on body
shape because the demagnetising factor $N$ differs: for a sphere $N = 1/3$,
giving $\chi_\text{eff} = \chi/(1+N\chi)$; for a long cylinder perpendicular to
the field $N = 1/2$, for a thin disc in its plane $N \to 0$. Hence a thin sheet
can be treated linearly up to much higher susceptibility than a sphere.
