# Solutions — 10-05-01 EM Induction (EMI) and Conductivity Meters

> **Read after attempting the exercises.** All numbers were computed, not
> estimated by hand. The layer weights are those printed by
> `code/em_induction_demo.py` for $a = 0.25\ \mathrm{m}$: at
> $s = 1.00\ \mathrm{m}$ they are $W(0\text{–}0.5) = 0.3501$,
> $W(0.5\text{–}1.5) = 0.4306$, $W(1.5\text{–}12) = 0.2194$, and at
> $s = 2.50\ \mathrm{m}$ they are $0.0845$ and $0.4811$ for the intervals
> $0$–$0.50$ and $0$–$1.50\ \mathrm{m}$.

Lesson: [01 EM Induction](../01-electromagnetic-induction-nearsurface.md).

---

## ★1 — Skin depth and induction number

$$\omega = 2\pi(9.8\times10^{3}) = 6.1575\times10^{4}\ \mathrm{rad\,s^{-1}},$$
$$\omega\mu_0\sigma = 6.1575\times10^{4}\times1.2566\times10^{-6}\times0.050
= 3.8689\times10^{-3}\ \mathrm{m^{-2}},$$
$$\delta = \sqrt{\frac{2}{3.8689\times10^{-3}}} = \sqrt{516.94}
= 22.74\ \mathrm{m},$$
$$B(1.00) = \frac{1.00}{22.74} = 0.044, \qquad
B(2.50) = \frac{2.50}{22.74} = 0.110 .$$

Both are much smaller than unity, so the linear interpretation is defensible at
either spacing. $B$ scales linearly with $s$, so doubling the spacing doubles the
induction number and doubles the size of the neglected terms.

---

## ★2 — Dimensional analysis

$\omega$ is $\mathrm{s^{-1}}$. With $\mathrm{1\ H = 1\ kg\,m^{2}\,s^{-2}\,A^{-2}}$,
$\mu_0$ is $\mathrm{kg\,m\,s^{-2}\,A^{-2}}$, and $\sigma$ in
$\mathrm{S\,m^{-1}}$ is $\mathrm{A^{2}\,s^{3}\,kg^{-1}\,m^{-3}}$ (since
$\mathrm{1\ S = 1\ A^{2}\,s^{3}\,kg^{-1}\,m^{-2}}$). Then

$$\omega\mu_0\sigma = \mathrm{s^{-1}\cdot kg\,m\,s^{-2}\,A^{-2}\cdot
A^{2}s^{3}\,kg^{-1}\,m^{-3}} = \mathrm{m^{-2}},$$

so $2/(\omega\mu_0\sigma)$ is $\mathrm{m^{2}}$ and its square root is a length in
metres. ✔

---

## ★3 — Apparent conductivity of a three-layer soil

$$\sigma_a = 80(0.3501) + 30(0.4306) + 10(0.2194)\ \mathrm{mS\,m^{-1}}$$
$$= 28.01 + 12.92 + 2.19 = 43.12\ \mathrm{mS\,m^{-1}}.$$

The **top interval contributes most** ($28.01$ of $43.12\ \mathrm{mS\,m^{-1}}$),
even though its weight is smaller than the middle interval's, because its
conductivity contrast is larger. Weight and contrast are different things: the
middle layer has the largest weight ($0.4306$) but only
$30\ \mathrm{mS\,m^{-1}}$. A reading is a contrast-weighted average.

---

## ★★4 — Two models, one reading

With $\sigma_{\text{hs}} = 20.0$ and $\sigma_a = 55.0\ \mathrm{mS\,m^{-1}}$, the
contrast rule $\sigma_a = \sigma_{\text{hs}} + (\sigma_1-\sigma_{\text{hs}})W_1$
gives $\sigma_1 - \sigma_{\text{hs}} = 35.0/W_1$.

**(a)** $W_1 = 0.3501$: $\sigma_1 = 20.0 + 35.0/0.3501 = 20.0 + 99.97
= 120.0\ \mathrm{mS\,m^{-1}}$. Check: $20.0 + 99.97(0.3501) = 55.0$ ✔. At
$s = 2.50\ \mathrm{m}$ the same layer has $W_1 = 0.0845$:

$$\sigma_a^{(a)}(2.50) = 20.0 + 99.97(0.0845) = 28.4\ \mathrm{mS\,m^{-1}}.$$

**(b)** $W_1 = 0.7806$: $\sigma_1 = 20.0 + 35.0/0.7806 = 20.0 + 44.84
= 64.8\ \mathrm{mS\,m^{-1}}$. Check: $20.0 + 44.84(0.7806) = 55.0$ ✔. At
$s = 2.50\ \mathrm{m}$, $W_1 = 0.4811$:

$$\sigma_a^{(b)}(2.50) = 20.0 + 44.84(0.4811) = 41.6\ \mathrm{mS\,m^{-1}}.$$

**Difference:** $(41.6-28.4)/28.4 = +46\%$. The thin, strongly conductive layer
reads *lower* at the large spacing than the thick, moderately conductive one — the
large-spacing weights probe deeper, where model (a) has only the half-space. This
is why a single-spacing interpretation is a hypothesis, not a measurement.

---

## ★★5 — Conditioning of the two-spacing system

$$\det M = 0.3501(0.9155) - 0.6499(0.0845) = 0.32052 - 0.05492 = 0.26560,$$

$$M^{-1} = \frac{1}{0.26560}\begin{pmatrix} 0.9155 & -0.6499 \\ -0.0845 &
0.3501\end{pmatrix} = \begin{pmatrix} 3.4469 & -2.4469 \\ -0.3182 & 1.3182
\end{pmatrix}.$$

Infinity-norm condition number: the largest absolute row sum of $M$ is
$\max(1.0000, 1.0000) = 1.0000$ and of $M^{-1}$ is
$\max(5.8939, 1.6364) = 5.8939$, so $\kappa_\infty = 5.89$. The system is
well-conditioned in the ordinary sense, yet the two unknowns are not equally
determined, because the bound on the solution error is
$|\delta\sigma| \le |M^{-1}|\cdot|\delta\sigma_a|$ elementwise:

$$|\delta\sigma_1| \le 0.5(3.4469 + 2.4469) = 2.95\ \mathrm{mS\,m^{-1}},$$
$$|\delta\sigma_2| \le 0.5(0.3182 + 1.3182) = 0.82\ \mathrm{mS\,m^{-1}}.$$

A $\pm 0.5\ \mathrm{mS\,m^{-1}}$ reading error therefore becomes about
$\pm 3\ \mathrm{mS\,m^{-1}}$ in the surface-layer conductivity (roughly $5\%$ of a
$60\ \mathrm{mS\,m^{-1}}$ layer) but under $1\ \mathrm{mS\,m^{-1}}$ in the
half-space. The reason is that the two weight vectors differ mainly in their
surface component; the mean conductivity is pinned by both readings, while the
split between layers relies on their *difference*.

---

## ★★6 — Where is the conductor?

The two readings are $48.0$ and $26.8\ \mathrm{mS\,m^{-1}}$ against a uniform
$20.0\ \mathrm{mS\,m^{-1}}$ site, so the anomalous response is $28.0$ at
$s = 1.00\ \mathrm{m}$ and $6.8\ \mathrm{mS\,m^{-1}}$ at $s = 2.50\ \mathrm{m}$ —
it *shrinks* by a factor of four when the spacing grows.

From the lesson, a $0$–$0.5\ \mathrm{m}$ interval carries weight $0.3501$ at
$s = 1.00\ \mathrm{m}$ but only $0.0845$ at $s = 2.50\ \mathrm{m}$: a factor of
four. A $1.5\ \mathrm{m}$ thick interval carries $0.7806$ and $0.4811$: a factor
of only $1.6$. The observed factor of four matches the shallow interval.

The profile is therefore a thin, strongly conductive surface layer of about
$0.5\ \mathrm{m}$ with $\sigma \approx 20 + 28.0/0.3501 = 100\
\mathrm{mS\,m^{-1}}$, over a $20\ \mathrm{mS\,m^{-1}}$ half-space — exactly model
A of the lesson. **A reading that falls steeply with spacing points shallow.**

---

## ★★★7 — Separating salinity from clay (specification)

**Measurements.** The same lines at two spacings ($1.00$ and
$2.50\ \mathrm{m}$) and two frequencies ($9.8$ and $24.5\ \mathrm{kHz}$), plus
induced-polarisation (IP) soundings on a subset of stations
([09-03 IP](../../../09-electrical-em-methods/03-induced-polarisation/README.md)).

**Quantity to plot.** The spacing ratio
$R = \sigma_a(2.50)/\sigma_a(1.00)$, which is nearly independent of the overall
conductivity scale and is controlled by *where* the conductor is, plus the IP
phase, which responds to clay-surface conduction rather than to pore-water ions.

**Confounder.** A single reading constrains only the product form
$\sigma \approx \sigma_w\,\theta^{m}$ (Archie-type, teaching form). Saline pore
water and a larger water content are indistinguishable from one reading, and clay
adds a surface-conduction term that raises $\sigma$ at low salinity.
Two soil columns can therefore read identically while differing in salinity by an
order of magnitude.

**What breaks it.** (i) Depth: if salinity arrives with a water table while clay
conduction is a property of the whole profile, $R$ separates them. (ii) IP phase:
clay-dominated ground polarises; clean saline sand does not. (iii) A borehole
sample and a conductivity-to-salinity calibration, without which the salinity
itself is not recoverable from $\sigma$ at all. **Without (iii) the answer is a
conductivity map, not a salinity map.**

---

## ★★★8 — Measuring the LIN bias (specification)

**Model.** A 1-D layered ground with one conductive layer at a stated depth; the
coils are finite loops of radius $a$ with spacing $s$ in the HCP mode.

**Solver.** The exact quasi-static solution for a vertical magnetic dipole over a
layered earth: Hankel-transform each layer, propagate an impedance from the
bottom up, and integrate the surface field numerically. This is nonlinear in
$\sigma$ and contains everything the LIN model drops. It must be validated in two
limits before use: (i) $B \to 0$, where it must reproduce the LIN reading to
within the quadrature tolerance, and (ii) a homogeneous ground, where it must
return the true conductivity through the standard calibration.

**Metric.** The *bias* $b = \sigma_a^{\text{LIN}}/\sigma_{\text{layer}}$ evaluated
at fixed layer contrast while $B$ is increased (by raising $f$, $s$ or
$\sigma_{\text{layer}}$), with a low-$B$ control at each contrast so that solver
error and modelling bias can be separated.

**Falsification.** The claim "the LIN reading under-reports a highly conductive
layer" predicts $b < 1$ and deteriorating with $B$. If $b$ stays within the
control error, the claim is falsified — the LIN reading is simply a weighted
average whatever $B$ is, and only the *calibration* degrades. If $b > 1$ at large
$B$, the sign of the claim is wrong. Reporting only the bias, never a number, is
the point: the direction is an experimental result, not a consequence of the
approximation.
