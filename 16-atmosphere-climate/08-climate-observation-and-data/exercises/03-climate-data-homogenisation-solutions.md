# Solutions — 16-08-03 Homogenisation, Bias Adjustment and Uncertainty

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [03 Homogenisation, Bias Adjustment and Uncertainty](../03-climate-data-homogenisation.md).

---


## ★ Foundational

## ★1 — Trend from a step

$$\delta(\text{trend}) = \delta_{\text{step}}\,
\frac{\sum_{t\ge t_0}(t-\bar t)}{\sum_t (t-\bar t)^{2}}
= 0.30 \times \frac{1250}{83{,}325} = 0.30 \times 0.015002
= \mathbf{0.00450\ \mathrm{K\,yr^{-1}}}.$$

The trend bias is $0.0045\ \mathrm{K}$ per year from a $0.3\ \mathrm{K}$ step —
$22\%$ of a $0.02\ \mathrm{K\,yr^{-1}}$ trend, from one instrument change.

---

## ★2 — What the difference removes

The candidate $C$ and the reference $R$ both contain the same regional climate
signal $\text{climate}(t)$, so
$D = C - R = [\text{climate} + b_C + n_C] - [\text{climate} + b_R + n_R]
= (b_C - b_R) + (n_C - n_R)$: the climate cancels and the difference is the bias
difference plus noise. A **network-wide** instrument change, however, enters
*both* $b_C$ and $b_R$ equally, so it cancels too: the difference has no step, and
the detection fails. This is why homogenisation requires a reference that shares
the candidate's climate but *not* its instrument history — a station with a
different instrument, or better several such stations so that a shared break in
any one can be identified.

---

## ★3 — Delta change

$$\text{future mean} = 12.0 + 2.5 = \mathbf{14.5\ ^\circ C}.$$

Delta change preserves the **observed distribution's shape** (its variability and
higher-order statistics) and imposes only the model's simulated *change*. It does
not correct the model's climatology, and it cannot represent a change in
variability; those require a distributional method such as quantile mapping.

---

## ★★ Applied

## ★★4 — Split-mean $t$-statistic

$$T = \frac{\overline{D}_{\ge} - \overline{D}_{<}}
{\sqrt{s^{2}_{\ge}/n_{\ge} + s^{2}_{<}/n_{<}}}
= \frac{0.55 - 0.05}{\sqrt{0.28^{2}/10 + 0.30^{2}/10}}.$$

Denominator: $\sqrt{0.00784 + 0.00900} = \sqrt{0.01684} = 0.12977\ \mathrm{K}$.

$$T = \frac{0.50}{0.12977} = \mathbf{3.85}.$$

$|T| = 3.85 > 3.0$, so this single candidate break year is flagged. **In a scan,
that verdict is not enough**: the rule must also account for the fact that the
same test was applied at every candidate year, which is what raises the
false-positive rate to $0.120$ in the demonstration.

---

## ★★5 — Undetected steps in a network

Expected undetected steps: $(1 - 0.65)\times 1000 = \mathbf{350}$.

Trend bias per undetected step:
$$\delta(\text{trend}) = 0.30 \times \frac{800}{42{,}660}
= 0.30 \times 0.018753 = 0.005626\ \mathrm{K\,yr^{-1}}.$$

So roughly $350$ stations enter the network mean carrying about
$0.0056\ \mathrm{K\,yr^{-1}}$ of spurious trend each. If those biases are shared
(a common instrument type, an era of changes), they do not average down in the
network mean: the network trend acquires a systematic offset of order
$0.005\ \mathrm{K\,yr^{-1}}$, a quarter of the true trend. **The undetected
inhomogeneities, not the detected ones, set the accuracy of a homogenised
network** — which is why the detection limit must be reported.

---

## ★★6 — Two quantile mappings

With historical model mean $10.0$, future model mean $13.0$ and observed historical
mean $11.0$ (equal standard deviations, so the correction is a pure shift):

**(a) Transfer built on the historical pair.** $F_{\text{obs,hist}}^{-1}
F_{\text{model,hist}}(x) = x + 1.0\ \mathrm{K}$. Applied to the future model:

$$\text{corrected future mean} = 13.0 + 1.0 = \mathbf{14.0\ K}, \qquad
\text{reported change} = 14.0 - 11.0 = \mathbf{+3.0\ K}.$$

The model's change is preserved.

**(b) Future model mapped onto the historical observed distribution.**
$F_{\text{obs,hist}}^{-1} F_{\text{model,fut}}(x)$ maps the future model onto the
historical *observed* distribution, so its mean becomes the observed historical
mean:

$$\text{corrected future mean} = \mathbf{11.0\ K}, \qquad
\text{reported change} = 11.0 - 11.0 = \mathbf{0.0\ K}.$$

The climate change signal is removed by construction. Both are called "bias
correction"; (a) is a bias adjustment, (b) is an error.

---

## ★★★ Research-oriented

## ★★★7 — A calibrated detection rule (design)

**Test statistic.** For each candidate year $t_0$ and each station $i$, the
split-mean $t$-statistic on the neighbour difference,
$T_i(t_0)$, as in Section 2 of the lesson. For a network-level rule, combine across
stations into the maximum over stations of a spatially weighted aggregate, or
screen each station separately and then correct for multiplicity across the
network.

**Null distribution.** Generate it by **resampling under the null**, not from a
table, because the statistics are correlated in time (the region's climate signal)
and across stations (shared weather):
1. Take the homogeneous neighbour differences and, in each realisation,
   **randomly permute the candidate's years relative to the reference** — a
   "bootstrapping under the null" construction — or
2. build a surrogate by **circularly shifting** the candidate series against the
   reference by a random lag, which preserves both the autocorrelation structure
   and the cross-station correlation of the observed differences while destroying
   the alignment that a break would require.
3. For each surrogate, compute the *maximum* of $|T_i(t_0)|$ over all candidate
   years and all stations, and record it. The $95$th percentile of that maximum
   distribution is the calibrated threshold, which automatically accounts for the
   number of candidates and for the spatial dependence.

**Metric.** Report the **receiver-operating-characteristic (ROC) curve** of the
rule — detection rate versus false-positive rate — and, because the costs are
asymmetric, the detection rate at a *fixed* false-positive rate (e.g. the
detection rate at a $5\%$ false-positive rate), as a function of step size. A rule
quoted as "detects $0.5\ \mathrm{K}$ steps" is not specified until the
false-positive rate at which that detection rate was achieved is stated.

---

## ★★★8 — A ramp, not a step

**What happens.** A single-break, step-based method models the inhomogeneity as one
level change at one date. Faced with a ramp of total size $+0.4\ \mathrm{K}$ spread
over 25 years, the scan's maximum statistic is achieved by splitting the record
somewhere in the *middle* of the ramp — because a single split best correlates
with a monotone change when it is placed at the ramp's centre. The method then
subtracts a constant from one side, which:

- **under-corrects** the early part of the ramp (the bias there is smaller than the
  estimated step), so a spurious *positive* trend remains in the first part;
- **over-corrects** the late part (the bias there is larger than the estimated
  step), so a spurious *negative* trend is introduced there;
- **and leaves a residual trend of order** the ramp's slope difference, which for
  $0.4\ \mathrm{K}$ over $25$ years is $0.016\ \mathrm{K\,yr^{-1}}$ — comparable to
  a real climate trend.

**Experiment.** Generate synthetic records with a known ramp
($+0.4\ \mathrm{K}$ over 25 years starting at a known year), add station and
regional noise as in the demonstration, apply the step-based method, and measure
(i) the residual trend error, (ii) the distribution of the detected breakpoint
date, and (iii) how the error depends on the ramp duration.

**Result that would show step-based homogenisation is adequate.** If, for a ramp
of the network's typical duration, the *residual trend error* is small compared
with the network's reported trend uncertainty **and** the detected break date falls
inside the ramp with a well-behaved adjustment (i.e. the fitted step approximates
the ramp's midpoint rise), then the step model's error is below the reporting
precision and the simpler method is adequate. The decision is quantitative: report
the residual error and the trend uncertainty side by side, and choose accordingly.
