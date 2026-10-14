# Solutions — 16-09-05 Climate-Geohazard Interactions

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [05 Climate-Geohazard Interactions](../05-climate-geohazards.md).

---


## ★ Foundational

## ★1 — Factor of safety at $r_u = 0.3$

Cohesion term:
$$\frac{c'}{\gamma z\sin\beta\cos\beta}
= \frac{5000}{18000 \times 3.0 \times \sin 22^\circ \cos 22^\circ}
= \frac{5000}{18000 \times 3.0 \times 0.37461 \times 0.92718}
= \frac{5000}{18756} = 0.2666.$$

Friction term:
$$\frac{\cos^{2}\beta\,(1-r_u)\tan\phi'}{\sin\beta\cos\beta}
= \frac{\cos\beta\,(1-r_u)\tan\phi'}{\sin\beta}
= \frac{(1-r_u)\tan\phi'}{\tan\beta}
= \frac{0.7 \times 0.57735}{0.40403} = 1.0003.$$

$$F = 0.2666 + 1.0003 = \mathbf{1.267}\ > 1: \text{stable}.$$

The friction term carries the entire $r_u$ dependence: from $1.429$ at $r_u = 0$ to
$1.000$ at $r_u = 0.3$, a $30\%$ reduction in the dominant resistance term for a
$30\%$ rise in pore pressure.

---

## ★2 — Thaw settlement

$$\Delta z = f_{\text{ice}}\left(h_{\text{warm}} - h_{\text{now}}\right)
= 0.25 \times (1.9 - 1.2) = 0.25 \times 0.70 = \mathbf{0.175\ m}.$$

$17.5\ \mathrm{cm}$ of settlement from a $0.7\ \mathrm{m}$ deepening of the active
layer. Whether that is tolerable depends entirely on the structure: a buried
pipeline can tolerate it, a rigid foundation cannot.

---

## ★3 — Inclusion–exclusion

$$\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B)
= 0.05 + 0.08 - 0.01 = \mathbf{0.12}.$$

A compound-flood impact whose mechanism requires **both** drivers (surge overtopping
*and* a high river stage simultaneously, for example a defended estuary where the
sea and the river meet) uses the **intersection**, $\Pr(A \cap B) = 0.01$. If the
impact occurs when **either** exceeds (a general inundation footprint), it uses the
union, $0.12$. The two differ by a factor of $12$ here — which is why the impact
mechanism must be stated before the probability is quoted.

---

## ★★ Applied

## ★★4 — A sea-level rise as a threshold shift

Exceedance probability of a level $h$ for a lognormal with median
$m = 1.20\ \mathrm{m}$ and log-scale $\sigma = 0.35$:

$$\Pr(S > h) = \Phi\!\left(-\frac{\ln h - \ln m}{\sigma}\right).$$

$h = 1.80$: $z = (\ln 1.80 - \ln 1.20)/0.35 = (0.58779 - 0.18232)/0.35 =
1.1585$, so $\Pr = \Phi(-1.1585) = 0.1233$, a return period of $8.11$ years.

Effective threshold after a $0.30\ \mathrm{m}$ rise: $h = 1.50$;
$z = (\ln 1.50 - \ln 1.20)/0.35 = (0.40547 - 0.18232)/0.35 = 0.6376$,
so $\Pr = \Phi(-0.6376) = 0.2619$, a return period of $3.82$ years.

$$\text{ratio} = \frac{0.2619}{0.1233} = \mathbf{2.12}.$$

A $0.30\ \mathrm{m}$ rise makes the surge (alone) exceed the old defence level
about $2.1$ times as often, with the structure untouched. Note that this is the
*marginal* response; the compound response in the lesson was $2.02\times$ for the
same $0.50\ \mathrm{m}$ rise — different metric, different number.

---

## ★★5 — Settlement range

$$\Delta z = f_{\text{ice}} \times 0.8\ \mathrm{m}.$$

$$\Delta z_{\min} = 0.20 \times 0.8 = 0.160\ \mathrm{m}, \qquad
\Delta z_{\max} = 0.40 \times 0.8 = 0.320\ \mathrm{m}.$$

So the settlement is $0.24\ \mathrm{m}$ (centre) with a range
$[0.16, 0.32]\ \mathrm{m}$ — a factor of two across the plausible ice content.

**Which input dominates:** the **excess-ice fraction**. It is both the larger
relative uncertainty ($\pm33\%$ on $0.30$) and the harder quantity to measure,
because it varies laterally at the scale of metres and is usually sampled at a few
boreholes. The thaw-depth change is comparatively better constrained by
temperature monitoring. Practical consequence: a settlement estimate should be
reported as a map or a range, not as a single number, because the *variability* is
the mechanism of damage.

---

## ★★6 — Critical pore-pressure ratio for a cohesionless slope

$$\tan\beta = (1-r_u)\tan\phi'
\;\Longrightarrow\;
r_u = 1 - \frac{\tan\beta}{\tan\phi'}
= 1 - \frac{0.46631}{0.62487}
= 1 - 0.74625 = \mathbf{0.254}.$$

Above $r_u = 0.254$ the factor of safety falls below one and the slope fails in
this idealisation. Note how different this threshold is from the cohesive case of
★1 ($0.4$–$0.5$): cohesion buys margin, and a cohesionless slope fails at a much
more modest pore pressure. **The threshold is a site property, not a climate
property**, which is precisely why the same climate change can be benign at one
slope and fatal at another.

---

## ★★★ Research-oriented

## ★★★7 — Attributing a change in compound flood frequency (design)

**Data.** Long, quality-controlled records of (i) sea level (tide gauges corrected
for vertical land motion, plus altimetry), (ii) storm surge residuals (surge minus
the tide, i.e. the meteorologically driven component), (iii) river stage or
discharge upstream of the confluence or estuary.

**Model.** A bivariate (or multivariate) distribution for (surge, river stage)
with (a) time-varying marginal parameters — at minimum a location shift following
the observed sea level — and (b) a time-varying dependence parameter, i.e. a
copula with a trend in $\rho$, or a non-stationary copula parameter.

**Estimator and metric.** Fit the non-stationary model by maximum likelihood and
report the fitted trend in each component: the marginal shift (in metres per
decade) and the copula parameter trend. Then decompose the change in the compound
exceedance probability into the two contributions by counterfactual simulation:
(a) the observed dependence with the *historical* sea level, (b) the observed sea
level with the *historical* dependence, and (c) both. Report the fraction of the
total probability change attributable to each, with intervals from a block
bootstrap that preserves the serial dependence.

**The confounder to control: land motion.** Both the surge record and the river
record are referenced to a local datum that moves with vertical land motion
(subsidence, compaction, groundwater withdrawal — interplay with
[16-09-02](../02-geodesy-climate.md)). If the datum moves downward, both drivers
appear to rise together, the *dependence* appears to increase, and the study would
attribute to a change in storm behaviour what is a change in the ground. Control:
measure vertical land motion independently (GNSS) and apply it before fitting, and
report the sensitivity of the attribution to the land-motion series.

**A second confounder:** changes in river management (dams, abstraction, land use)
alter the river-stage marginal for reasons unrelated to weather.

---

## ★★★8 — Thaw-driven versus rainfall-driven slope failure (design)

**Observables.**
1. **Ground temperature** (borehole or thermistor string) — the thaw depth and
   the timing of thaw, which is the direct driver of the thaw mechanism.
2. **Pore pressure** at one or more depths (piezometers or pressure transducers) —
   the direct driver of both mechanisms, and the variable $r_u$ is computed from.
3. **Precipitation and snowmelt** (gauge and/or reanalysis) — the rainfall driver.
4. **Surface displacement** (GNSS, InSAR or tiltmeters) — the mechanical response
   and its *timing*.
5. **Seismic or acoustic emissions** — microcracking before failure, with the
   operating-point caveat of a detection threshold
   ([16-09-01](../01-seismic-monitoring-climate.md)).
6. **Subsurface structure and ice content** — from geophysics (refraction,
   MASW, ERT), to establish where excess ice and thus thaw-susceptible material
   actually is.

**Thresholds.** The failure threshold is expressed in $r_u$ (or in effective
stress), not in the raw drivers: $r_u^{\text{crit}}$ from the slope's strength
parameters, with its own uncertainty.

**Patterns that distinguish the mechanisms.**
- *Thaw-driven*: displacement and pore-pressure rise **correlate with thaw depth
  and ground temperature**, occur in the **thaw season**, and are present in
  **years with normal rainfall** — the pressure is released by meltwater from the
  thawing ice, whose supply is set by temperature. A seasonal signature that
  recurs without rainfall anomalies is the discriminator.
- *Rainfall-driven*: displacement correlates with **rainfall intensity or
  accumulation over a stated antecedent window**, occurs during or shortly after
  storms including **late-season and winter events** (when thaw is not deepening),
  and is absent in dry years.

**When the two are indistinguishable.** They are indistinguishable when (i) the
observations do not separate the timing — for example, monthly rather than
sub-daily pore-pressure sampling, so a rainstorm and a thaw pulse are averaged
together; (ii) the two drivers are **collinear** at the site, because summer
rainfall and thaw both peak at the same time of year; and (iii) the excess-ice
content is unknown, so the meltwater supply cannot be computed independently of
the pressure record. The additional measurement that breaks the degeneracy is a
**winter or early-spring comparison**: rainfall can raise pressure in any season
(if the ground is unfrozen or a rain-on-snow event occurs), while thaw-driven
pore pressure requires seasonal thawing. Reporting the winter baseline is
therefore the decisive experiment, not a supplementary one.
