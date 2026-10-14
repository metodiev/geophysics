# Solutions — 16-08-01 Surface, Radiosonde and Satellite Records

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [01 Surface, Radiosonde and Satellite Records](../01-surface-and-satellite-records.md).

---


## ★ Foundational

## ★1 — Trend of a short anomaly series

Design matrix $\mathbf{X} = [\mathbf{1}, \mathbf{t}]$ with $t = 0,\dots,9$;
$\bar t = 4.5$, $\sum (t-\bar t)^2 = 82.5$, $\sum (t-\bar t)y = 6.0$.

$$\hat\beta = \frac{\sum (t-\bar t)\,y_t}{\sum (t-\bar t)^{2}}
= \frac{6.0}{82.5} = 0.0727\ \mathrm{K\,yr^{-1}}.$$

Residuals about the fit $\hat y = -0.00727 + 0.0727t$ give
$s^{2}_{\text{res}} = 0.03964/8 = 0.004955$, so
$\operatorname{SE} = \sqrt{0.004955/82.5} = 0.00775\ \mathrm{K\,yr^{-1}}$.

Trend: $+0.0727 \pm 0.0077\ \mathrm{K\,yr^{-1}}$. Note that a decade-long series
gives a standard error fifteen times larger than the 120-year synthetic record —
short records buy precision in nothing.

---

## ★2 — Unit conversions

$$0.015\ \mathrm{K\,yr^{-1}} \times 10\ \mathrm{yr\,decade^{-1}}
= 0.15\ \mathrm{K\,decade^{-1}}.$$
$$0.015\ \mathrm{K\,yr^{-1}} \times 120\ \mathrm{yr} = 1.8\ \mathrm{K}.$$

The total is a *change over the record*, not a rate, and comparing it with a
$0.8\ \mathrm{K}$ composition discontinuity (Section 4 of the lesson) is what
makes that discontinuity first-order.

---

## ★3 — Constant offsets and anomalies

With $y_i(t) = T(t) + c_i$ for constant $c_i$, the anomaly relative to the station
mean is

$$y_i'(t) = y_i(t) - \overline{y_i} = T(t) + c_i - \overline{T} - c_i
= T'(t).$$

The offset cancels exactly, so the station's **trend is unchanged**: a constant
offset has no trend, and removing it (or not) cannot affect a fitted slope. The
offsets matter only for the *absolute* values, which are not used. The trend of
station X and station Y is the trend of the truth plus each station's own noise.

---

## ★★ Applied

## ★★4 — Step leverage on a fitted trend

$$\delta(\text{trend}) = \delta\,\frac{\sum_{t\ge60}(t-\bar t)}{\sum_t(t-\bar t)^{2}}
= 0.15 \times \frac{1800}{143{,}990} = 0.15 \times 0.01250
= 0.001875\ \mathrm{K\,yr^{-1}}.$$

Against a formal standard error of $0.0005\ \mathrm{K\,yr^{-1}}$ this is

$$\frac{0.001875}{0.0005} = 3.75\times$$

the formal error. **The adjustment uncertainty dominates.** The lesson's
worked example uses $\delta = 0.1\ \mathrm{K}$ and gets $0.00125\
\mathrm{K\,yr^{-1}} = 2.5\times$ the formal error; the two exercises differ only in
the step size, and the linear scaling is the point.

---

## ★★5 — Naive averaging

$$\text{error} = 0.0168 - 0.0150 = +0.0018\ \mathrm{K\,yr^{-1}}
= 12\% \text{ of the true trend}.$$

Adding ten more unbiased stations does not fix it because the error is
**systematic, not random**. The mean of $n$ records each carrying the same
unadjusted step still contains that step: if all stations in the network had their
instruments changed at the same time (as happens in a coordinated network
upgrade), the step is common to every one of them, and the average of $n$ copies
of a bias is the bias. Only an *independent* estimate of the step — from
overlapping records, neighbour comparisons, or documented metadata — can remove
it. More stations of the same type add precision about a biased quantity.

---

## ★★6 — Composition artefact

$$\text{true trend} = +0.0150, \qquad \text{fitted} = +0.0246, \qquad
\text{artefact} = +0.0246 - 0.0150 = +0.0096\ \mathrm{K\,yr^{-1}}.$$

The artefact ($64\%$ of the true trend, and $39\%$ of the fitted trend) comes from
the composition change, not from any station's own record.

Why anomaly formation alone does not remove it: anomaly formation removes each
site's **time-constant** offset relative to its own climatology, but the artefact
arises because the *set of sites* changes. The old and new sites have different
anomaly *levels* only if their anomalies are not interchangeable — if the new
sites sit in a region whose anomalies do not track the old region's, then
replacing one group by the other changes the index. A common-network reduction
(using only sites present throughout, or a pairwise difference network) is what
removes the change; anomaly formation alone is necessary but not sufficient.

---

## ★★★ Research-oriented

## ★★★7 — Drift sensitivity (design)

**Model.** Truth $T(t)$ with a known linear trend over $N = 30$ years; a synthetic
diurnal cycle of amplitude $A$ and a linear local-time drift of $\theta$ hours per
year; observed series
$y(t) = T(t) + A\left[\cos\phi(t) - \cos\phi(0)\right]$ with
$\phi(t) = 2\pi\left(13 + \theta t - 14\right)/24$ hours.

**Parametrisation.** Sweep $A \in \{0.5, 1.0, 2.0\}\ \mathrm{K}$ and $\theta$ from
$0$ to $0.2\ \mathrm{h\,yr^{-1}}$, and for each combination fit an OLS trend to
$y$.

**Metric.** The spurious trend $\hat\beta(\theta) - \beta_{\text{true}}$, and the
value $\theta^\star$ at which it reaches the target $0.005\ \mathrm{K\,yr^{-1}}$
for each $A$.

**Result to report.** $\theta^\star$ as a function of $A$; the demonstration
shows the sensitivity is roughly proportional to $A$ and to the total drift, so the
report is a one-line scaling law with numbers attached, not a single number.

**How the design could understate the sensitivity.** By using a **linear** drift
from a local time *centred on the reference*. If the drift starts at the reference
hour, $\cos\phi(0) = 1$ and the diurnal term is purely decreasing, giving the
largest spurious trend; if the drift is symmetric about the reference (as a full
orbit-precession cycle is), the linear component cancels and the spurious trend is
much smaller. A design that assumes a symmetric cycle, or that removes a *fitted*
linear trend from the diurnal term before measuring, can conclude that drift does
not matter when in fact the answer depends on where the cycle starts.

---

## ★★★8 — Comparing two products

The difference is $0.017 - 0.014 = 0.003\ \mathrm{K\,yr^{-1}}$, and the difference
of two independent fits with standard errors of $0.001$ each has standard error
$\sqrt{0.001^2 + 0.001^2} = 0.00141$, so the formal significance is
$0.003/0.00141 = 2.1\sigma$. That is the calculation the colleague did.

It is not the right calculation. Each product carries an adjustment-history
uncertainty of $\pm 0.1\ \mathrm{K}$ in a mid-record step, and the step leverage
gives an extra trend uncertainty of
$0.1 \times 1800/143{,}990 = 0.00125\ \mathrm{K\,yr^{-1}}$ per product. Both terms
are of the same size as the difference being tested, and they are **not
independent** if the two products share stations, share a reference series, or
inherit the same metadata corrections.

Response: *"The formal significance ignores both products' adjustment-history
uncertainty. A single $\pm 0.1\ \mathrm{K}$ mid-record step adjustment contributes
about $0.00125\ \mathrm{K\,yr^{-1}}$ to each trend, and the two products' error
terms are not independent if they share data or reference series. The quoted
difference is therefore not resolvable until the shared error structure is
modelled. What is needed: (i) the overlap of the two station/satellite sets;
(ii) the documented adjustment uncertainties for each product, with the timing of
each step; (iii) a common error model that separates shared from independent
components. If the difference survives those, we can discuss it."*
