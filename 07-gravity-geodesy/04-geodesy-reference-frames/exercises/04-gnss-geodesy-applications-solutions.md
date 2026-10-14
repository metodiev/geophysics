# Solutions — 07-04-04 GNSS for Tectonics, Subsidence and Sea Level

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [04 GNSS Geodesy Applications](../04-gnss-geodesy-applications.md).

---

## ★1 — Design matrix

With $t$ in years:

$$\mathbf{A} = \begin{pmatrix}
1 & t_1 & \cos\frac{2\pi t_1}{T} & \sin\frac{2\pi t_1}{T} \\
\vdots & \vdots & \vdots & \vdots \\
1 & t_n & \cos\frac{2\pi t_n}{T} & \sin\frac{2\pi t_n}{T}
\end{pmatrix},
\qquad T = 365.25\ \mathrm{d},$$

and $\mathbf{x} = (a,\;b,\;c,\;d)^{\mathsf{T}}$. Because the regressor is $t/YR$
equivalently $t$ in years, **$b$ is in $\mathrm{m\,yr^{-1}}$ directly** — the
demonstration's own first version of this calculation divided by $365.25$ once
too often and produced a velocity $365$ times too large, which is a good reminder
to check a fitted slope against the physical scale of the data before reporting it.

---

## ★2 — Why a white-noise formal error is not an uncertainty

The least-squares covariance
$(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}s^{2}$ assumes the residuals are
independent, so that $n$ epochs provide $n$ independent samples and the error falls
as $1/\sqrt{n}$. Real position series have temporally correlated residuals
(multipath, monument motion, loading, orbit and frame errors), so the *effective*
number of independent samples is far smaller than $n$. Using the white-noise
formula therefore understates the true scatter, and the lesson measures the
inflation: a factor of $8$ for flicker noise and $15$ for random-walk-like noise at
the same rms amplitude.

---

## ★3 — Signs

$$\text{absolute sea level rate} = \text{gauge trend} - \text{land uplift rate},$$

with uplift positive upward. A subsiding coast (negative uplift) makes the gauge
read *faster* sea-level rise than the absolute rate. In the lesson's table a gauge
trend of $+3.00\ \mathrm{mm\,yr^{-1}}$ with $-1.50\ \mathrm{mm\,yr^{-1}}$ of
land motion gives $4.50\ \mathrm{mm\,yr^{-1}}$ absolute.

---

## ★4 — Realistic uncertainty for the $3$-year record

Formal: $0.03\ \mathrm{mm\,yr^{-1}}$. Inflation factors measured in the lesson:

| noise colour | empirical / formal |
|---|---|
| white | 1.0 |
| flicker (exponent 1) | $\approx8$ |
| random-walk-like (exponent 2) | $\approx15$ |

Realistic uncertainty: $0.03\times8 = \mathbf{0.24\ mm\,yr^{-1}}$ for flicker
noise, and up to $0.03\times15 = \mathbf{0.45\ mm\,yr^{-1}}$ if the series behaves
like a random walk.

**What would change the answer:** (i) the *measured* noise character — estimate it
from the residual spectrum or a spectral index fit rather than assuming; (ii) the
record length, since the inflation factor grows with the span; (iii) a monument or
multipath problem that makes the residuals worse than the model; (iv) a common-mode
error not captured by a single-station noise model, which no inflation factor can
fix and which requires network analysis.

---

## ★5 — Record length for $0.1\ \mathrm{mm\,yr^{-1}}$ under flicker noise

Two routes, and they disagree at long spans, which is itself the lesson.

**(a) Power law fitted over the short end.** The table gives
$0.714\ \mathrm{mm\,yr^{-1}}$ at $1\ \mathrm{yr}$, $0.385$ at $2$ and $0.123$ at
$5$, i.e. an exponent near $-0.4$ over the first factor of five:

$$\sigma_v(T)\approx0.714\,T^{-0.4}
\;\Longrightarrow\;
T=\left(\frac{0.714}{0.1}\right)^{1/0.4} = 7.14^{2.5} = 136\ \mathrm{yr}.$$

**(b) Direct interpolation of the measured table, which is the defensible route.**

| $T$ (yr) | empirical $\sigma_v$ (mm/yr) |
|---|---|
| 1 | 0.714 |
| 5 | 0.123 |
| 10 | 0.057 |
| 20 | 0.028 |

Log-interpolating between $5$ and $10\ \mathrm{yr}$ for
$0.1\ \mathrm{mm\,yr^{-1}}$:

$$10^{\,\log_{10}5 + \frac{\log_{10}0.123-\log_{10}0.1}
{\log_{10}0.123-\log_{10}0.057}(\log_{10}10-\log_{10}5)}
\approx \mathbf{6\ \mathrm{yr}} .$$

**Which answer to report.** The measured table implies about $6$–$7$ years; the
short-span power law over-predicts because the effective exponent changes with
span (the scatter falls by a factor $\approx2$ per doubling between $5$ and
$20\ \mathrm{yr}$, i.e. a steeper exponent than $-0.4$). The robust conclusions
are: (i) precision improves far more slowly than the $1/T$ of white noise, and
(ii) a single power law should not be extrapolated beyond the range over which it
was fitted — report the measured values and the interpolation, not the fitted
exponent.

## ★6 — Strain uncertainty from a $20\ \mathrm{km}$ baseline

Single difference over $L = 20\ \mathrm{km}$ with
$\sigma_v = 0.4\ \mathrm{mm\,yr^{-1}} = 4\times10^{-4}\ \mathrm{m\,yr^{-1}}$:

$$\sigma_e \approx \frac{\sigma_v}{L}
= \frac{4\times10^{-4}}{2.0\times10^{4}} = 2.0\times10^{-8}\ \mathrm{yr^{-1}}
= \mathbf{20\ nstrain\,yr^{-1}}.$$

Differencing two stations raises this by $\sqrt{2}$: $28\
\mathrm{nstrain\,yr^{-1}}$.

**Is a $10\ \mathrm{nstrain\,yr^{-1}}$ signal resolvable?** No — the uncertainty is
twice the signal. It becomes resolvable at roughly a $50\ \mathrm{km}$ baseline
with the same velocity error ($8\ \mathrm{nstrain\,yr^{-1}}$), or with
$0.2\ \mathrm{mm\,yr^{-1}}$ velocities on a $20\ \mathrm{km}$ baseline.

---

## ★7 — Four stations to separate strain from rotation

**Geometry condition.** The velocity gradient tensor at a point has four degrees of
freedom: three strain components (two normal plus shear) and one rotation. A
three-station array supplies exactly three independent station differences, so it
is **rank-deficient by one** and cannot separate rotation from shear — the fact
measured in the lesson ($e_{xy}$ recovered as $45$ instead of $15\
\times10^{-9}\ \mathrm{yr^{-1}}$).

**Design.** Place stations so that the **difference vectors span at least four
independent directions in the plane**: a four-station array with no three
collinear, e.g. a triangle with unequal sides plus a station inside it, or a
quadrilateral. Formally, if $\mathbf{d}_k = (dx_k, dy_k)$ are the station offsets
from the array centroid, the design matrix rows for a uniform-gradient model are
$[dx_k, dy_k, 0, -dy_k]$ and $[0, dx_k, dy_k, dx_k]$ (for the $v_x$ and $v_y$
equations, with the last column the rotation); the array must make this matrix of
full rank $4$.

**Resolution** for $0.5\ \mathrm{mm\,yr^{-1}}$ station velocities over a $50\
\mathrm{km}$ array: the strain-rate uncertainty is of order

$$\sigma_e \approx \frac{\sigma_v\,\sqrt{2}}{L}
= \frac{5\times10^{-4}\times1.41}{5.0\times10^{4}}
= 1.4\times10^{-8}\ \mathrm{yr^{-1}} = \mathbf{14\ nstrain\,yr^{-1}},$$

with the rotation determined to a comparable magnitude
($\sigma_{\omega}\approx\sigma_e$ for a symmetric array). The precision scales as
$1/L$, so a $100\ \mathrm{km}$ array gives $7\ \mathrm{nstrain\,yr^{-1}}$. **The
geometry buys the *separation*; the baseline length buys the *precision* — the two
requirements are independent** and both must be met, which is the practical reason
regional strain-rate studies use sparse but widely spread networks rather than
dense local clusters.

---

## ★8 — Absolute sea level from a five-year series

Gauge trend $+2.0\ \mathrm{mm\,yr^{-1}}$, land motion $-1.2\ \mathrm{mm\,yr^{-1}}$
(uplift positive, so the land is **subsiding**).

$$\text{absolute sea level} = \text{gauge} - \text{uplift}
= 2.0-(-1.2) = \mathbf{+3.2\ mm\,yr^{-1}}.$$

**Uncertainty.** The formal $0.08\ \mathrm{mm\,yr^{-1}}$ must be inflated for
correlated noise: from the lesson's factors a five-year record under flicker noise
gives about $0.12\ \mathrm{mm\,yr^{-1}}$ (table), and a realistic monument and
atmospheric contribution raises it to a defensible
$\sigma_{\text{VLM}} \approx 0.4\ \mathrm{mm\,yr^{-1}}$. The gauge contributes its
own correlated error of order $0.3$–$0.5\ \mathrm{mm\,yr^{-1}}$ over five years.
Combining:

$$\sigma = \sqrt{0.4^{2}+0.4^{2}} = 0.57\ \mathrm{mm\,yr^{-1}},$$

so the result is

$$\mathbf{3.2 \pm 0.6\ mm\,yr^{-1}}.$$

**Is the sign resolved?** Yes — the magnitude is $5.6$ times the uncertainty, so
the conclusion "sea level rose in absolute terms" is robust. Repeated for the
direction of the *correction*: without the land-motion term the answer would have
been $2.0\ \mathrm{mm\,yr^{-1}}$, a $38\%$ understatement — the correction matters
even when it does not change the sign.
