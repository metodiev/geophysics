# Solutions — 10-06-03 Monitoring Contaminant Transport with Geophysics

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. $z_{0.95} = 1.6449$; power $= 1-\Phi(z_{0.95}-s)$ with $s$ the effect in
> units of the noise.

Lesson: [03 Monitoring Contaminant Transport](../03-contaminant-monitoring.md).

---

## ★1 — Pore velocity, arrival time, dispersion

$$v = \frac{q}{n_e} = \frac{0.15}{0.25} = 0.600\ \mathrm{m\,day^{-1}},$$
$$t_{\text{arr}} = \frac{x}{v} = \frac{20.0}{0.600} = 33.33\ \mathrm{days},$$
$$D = \alpha_L v = 1.0(0.600) = 0.600\ \mathrm{m^2\,day^{-1}}.$$

Note the factor of $1/0.25 = 4$ between the Darcy flux and the transport velocity.
A prediction using $q$ would have given $133$ days instead of $33$ — the single
largest source of error in plume-arrival forecasts, and it is a *porosity* error,
not a geophysical one.

---

## ★2 — Aliasing from the measured table

| target | interval (days) | fraction of the peak |
|---|---|---|
| retain 90% | 5 | $90.2\%$ |
| halve the peak | 10 | $54.2\%$ |
| essentially miss it | 30 | $0.5\%$ |

The table is the whole argument for a short interval: the loss is a factor of two
at 10 days, and the reported time series is still smooth and plausible at that
interval.

---

## ★3 — Why conductivity is a mixture

The measured conductivity is $\sigma = \sigma_{\text{bg}} + kC$, so recovering
$C$ requires the background conductivity $\sigma_{\text{bg}}$ (a site property that
varies seasonally), the calibration $k$ (a property of the contaminant's ionic
composition), and the assumption that the relation is linear in the concentration
range of interest. Neither $\sigma_{\text{bg}}$ nor $k$ is measured by the
geophysics. The two measurements that make the result a concentration are **a water
sample analysed for the contaminant and its ionic strength** (for $k$) and **a
background station** outside the plume (for $\sigma_{\text{bg}}$).

---

## ★★4 — Detection power

$$s = \frac{20}{2} = 10 \quad\Longrightarrow\quad
\text{power} = 1-\Phi(1.6449-10) \approx 1.000 .$$

For 95% power, $1-\Phi(1.6449-s) = 0.95$ requires
$1.6449 - s = -1.6449$, so $s = 3.29$ and the smallest rise detectable with 95%
probability is

$$\text{rise}_{95} = 3.29 \times 2\ \mathrm{mS\,m^{-1}} = 6.58\ \mathrm{mS\,m^{-1}} .$$

So the report "no change" from this survey means "no plume with a rise above about
$6.6\ \mathrm{mS\,m^{-1}}$". Any weaker claim is unsupported by the data.

---

## ★★5 — Which error dominates

**(a) Calibration.** A relative error $\delta$ in $k$ produces a concentration error
of $1/(1+\delta)-1$:

| calibration error | error in inferred $C$ |
|---|---|
| $-25\%$ | $+33.3\%$ |
| $+25\%$ | $-20.0\%$ |

**(b) Background.** A background error of $\Delta\sigma_{\text{bg}}$ shifts the
inferred rise by the same amount, so the *relative* error in $C$ is
$-\Delta\sigma_{\text{bg}}/(kC)$, i.e.

$$-\frac{2}{20} = -10.0\%\ \text{for the 20 mS/m rise}, \qquad
-\frac{2}{120} = -1.7\%\ \text{for the 120 mS/m rise}.$$

**Which dominates.** For the weak plume the calibration error ($+33\%/-20\%$)
exceeds the background error ($-10\%$) but the two are the same order; for the
strong plume the calibration error dominates by an order of magnitude. The general
rule: the background error matters in proportion to *how small the plume's rise is
compared with the background uncertainty*, and calibration error scales with the
result itself — so **weak plumes need a background survey, strong plumes need a
calibration**.

---

## ★★6 — Choosing the survey interval

With a peak at $13.40$ days and a passage of $12.3$ days, an interval of
$2$ days samples the peak to $98.5\%$ (measured) and an interval of $1$ day to
$99.3\%$. Choose **$2$ days**: it costs half the survey effort of a daily
programme for a loss of $1.5\%$ of the peak, while a $5$-day interval already
loses $10\%$.

**Systematic error left.** The retained fraction is a *bias*, not a random error:
if the true peak rise is $127.5\ \mathrm{mS\,m^{-1}}$, a $2$-day interval reports
$125.6$ and a $5$-day interval reports $115.0$, consistently under. Because the
bias is deterministic, the honest report states the retained fraction alongside the
result (for example "peak rise $126\ \mathrm{mS\,m^{-1}}$, $98.5\%$ of the true
peak at this sampling interval"), and a *dense* survey once is what establishes the
passage duration that the correction needs.

---

## ★★★7 — A six-month compliance monitoring programme (specification)

**Survey interval.** The passage duration must be estimated first: from the
predicted $q$, $n_e$ and $\alpha_L$, and then measured by a *dense* campaign (daily
for two weeks) around the predicted arrival. Design the routine interval at
one-fifth of the measured passage (so that at least five samples fall on the
transient), and always include the dense campaign in the first year.

**Method and resolution.** ERT or EM along the compliance line, chosen by the depth
of the water table and the expected plume conductivity: ERT where a section is
needed, EM where speed and repeatability matter more. The *resolution* claimed must
be the measured repeatability (an NRMS or an equivalent conductivity noise), not
the instrument's specification.

**Calibration.** (i) A water sample from the source zone *and* one from the front,
since the ionic composition changes; (ii) a background station measured every
epoch, since $\sigma_{\text{bg}}$ drifts with the water table; (iii) a head
measurement at a piezometer to convert the water-table change into a saturation
change and remove it from the conductivity signal.

**Detection claim with its power.** State the smallest conductivity rise detectable
with 95% probability (about $3.3\sigma$) *after* the multiplicity correction for
the number of quadrupoles scanned, and translate it to a concentration with the
calibration and its uncertainty.

**Confounders.** Water-table movement; temperature (a seasonal effect with a known
depth structure); salinity changes from other sources; and the pore-water
conductivity of the native groundwater, which varies with depth.

**Falsification test.** Repeat a subset of stations within the same week: if the
within-week spread is comparable to the between-epoch change being reported, the
change is not resolved. Additionally, verify that any claimed plume front moves
*downstream* at a speed consistent with $q/n_e$; a front that moves at any other
speed requires an explanation before it is reported.

---

## ★★★8 — Predicted 30 days, observed 45 days

Ordered by prior probability, with the test for each:

1. **Effective porosity or Darcy flux wrong** (the prediction used $q$ instead of
   $q/n_e$, or $n_e$ is an order-of-magnitude guess). *Test:* a tracer test or a
   pumping test giving $q$ and $n_e$ independently; a factor-of-1.5 error in
   either produces exactly this delay.
2. **Retardation**: the contaminant sorbs, so it travels at $v/R$ while the
   *conductivity* front travels at $v$. *Test:* compare the conductivity-front
   arrival with a chemical analysis of the same water samples; if the chemistry
   lags the conductivity, the conductivity is following a non-sorbing ion.
3. **The plume was detected only when it became detectable** — the front arrived on
   time but its conductivity rise was below the threshold. *Test:* examine the
   earlier epochs at the *corrected* threshold and compute the power against the
   observed rise; a front arriving at 30 days with a rise of $1\sigma$ would be
   reported as "no change".
4. **Background drift**: a seasonal change in $\sigma_{\text{bg}}$ masked and then
   unmasked the plume. *Test:* the background station's time series; if the
   background moved by more than the plume's rise, the arrival time is not
   measurable from the conductivity alone.
5. **The source history is not what was assumed**: the release was delayed,
   intermittent, or of lower strength than the model. *Test:* the site's own
   records, and the shape of the observed rise (a delayed but identical shape
   points to transport, a different shape to the source).

The ordering matters: causes 1 and 2 are properties of the aquifer and the
contaminant, and they are the most common explanation for a *uniform* delay of the
whole transient. Causes 3–5 predict a changed *shape* as well, and the shape of the
observed conductivity curve is the diagnostic that separates them.
