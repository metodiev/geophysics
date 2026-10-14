# Solutions — 10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment. Where a problem has more than one defensible answer, that
> is said. All models are **SYNTHETIC**; conventions are labelled.

Lesson: [01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](../01-spt-cpt-crosshole.md).

---

## ★1 — SPT corrections

$$N_{60} = N\frac{ER}{60} = 12 \times \frac{55}{60} = 11.00,$$

$$C_N = \sqrt{\frac{p_a}{\sigma'_v}} = \sqrt{\frac{100}{70}}
= \sqrt{1.42857} = 1.1952,$$

$$(N_1)_{60} = 11.00 \times 1.1952 = 13.15.$$

Units: $N$, $N_{60}$ and $(N_1)_{60}$ are counts (dimensionless); $C_N$ is
dimensionless (a ratio of two stresses in the same unit). $ER$ is quoted as a
percentage and used as a ratio, so it must be divided by the reference $60$ in the
*same* units — a common slip is to divide newtons by $60\%$ and drop the
percentage.

The two corrections act in opposite directions: the low hammer energy raises the
count ($\times 0.9167$) and the low confining stress raises it again
($\times 1.1952$). Reporting $N = 12$ would be $9\%$ below $(N_1)_{60}$ and, worse,
would not be comparable with any published correlation.

---

## ★2 — Same-depth cross-hole pair

$$V_s = \frac{L}{t} = \frac{5.0}{19.2\times10^{-3}} = 260.42\ \mathrm{m\,s^{-1}},$$

$$G_{\max} = \rho V_s^{2} = 1950 \times (260.42)^{2}
= 1.3224\times10^{8}\ \mathrm{Pa} = 132.2\ \mathrm{MPa}.$$

**Assumptions.**

1. The path between the two receivers (here, source and receiver at the same depth)
   is a **straight horizontal line inside one layer**, so $L$ is the true path
   length. In a layered medium a diving ray through a faster layer could arrive
   earlier, in which case $L/t$ is not the layer velocity (Section 3.4 of the
   lesson).
2. $\rho$ is known, or assumed, for the depth in question. $G_{\max}$ is exact
   *given* $\rho$ and $V_s$; its uncertainty is theirs combined in quadrature
   ($V_s$ entering twice, so $\delta G/G = \sqrt{(\delta\rho/\rho)^2 + 4(\delta V_s/V_s)^2}$).

---

## ★3 — Cone indices with a pore-pressure correction

$$q_t = q_c + (1-a)u_2 = 5000 + 0.2(300) = 5060.0\ \mathrm{kPa}
= 5.060\ \mathrm{MPa}.$$

$$R_f = \frac{f_s}{q_t}\times100 = \frac{45}{5060}\times100 = 0.889\%,$$

$$Q = \frac{q_t-\sigma_v}{\sigma'_v} = \frac{5060-90}{60} = 82.83,$$

$$F = \frac{f_s}{q_t-\sigma_v}\times100 = \frac{45}{4970}\times100 = 0.905\%,$$

$$I_c = \sqrt{(3.47-\log_{10}82.83)^{2} + (1.22+\log_{10}0.905)^{2}}
= \sqrt{(3.47-1.9182)^{2} + (1.22-0.0434)^{2}}
= \sqrt{2.408 + 1.384} = 1.948.$$

$I_c = 1.95$ falls in the sand band ($1.31$–$2.05$).

**Is the pore-pressure correction significant?** The correction is
$0.2(300)/5060 = 1.19\%$ of $q_t$. In a stiff deposit that is negligible; in soft,
silty ground with $u_2$ of the same order as $q_c$ it changes both $q_t$ and the
derived $Q$, and hence the classification. The rule is to apply it always —
it is algebra, not a judgement — and to check its size in the printout.

---

## ★4 — Straight-ray interval velocity, and its failure

**(a)**

$$v = \frac{r_2-r_1}{t_2-t_1} = \frac{4.472-4.123}{(20.002-22.906)\times10^{-3}}
= \frac{0.349}{-2.904\times10^{-3}} = -120.2\ \mathrm{m\,s^{-1}}.$$

The sign is the physics, not an error. The receiver at $3\ \mathrm{m}$ is deeper,
and the ray reaching it **dives through the faster second layer**
($260\ \mathrm{m\,s^{-1}}$ against $180\ \mathrm{m\,s^{-1}}$), so it arrives
**earlier** than the arrival at $2\ \mathrm{m}$. Any formula that assumes a straight
ray converts a negative time difference into a negative velocity.

**(b)** With $t_2 = 24.000\ \mathrm{ms}$:

$$v = \frac{0.349}{1.094\times10^{-3}} = 319.0\ \mathrm{m\,s^{-1}}.$$

That is the answer the straight-ray formula would give if there were no refraction
at all — i.e. if the material between the two receivers were homogeneous at
$319\ \mathrm{m\,s^{-1}}$, which is neither layer's velocity. Even the
"plausible-looking" number is wrong here; it is a weighted average over a path that
spans two velocities. **A plausible interval velocity is not evidence that the
assumption held**; the check is consistency between several source–receiver pairs
and geometry, not the size of the number.

---

## ★5 — Down-hole interval velocity uncertainty

For an interval, both endpoint times carry the same errors, so the uncertainty of
the difference is $\sqrt{2}\sigma$ for each error source. With a
$0.05\ \mathrm{ms}$ pick precision and a $0.05\ \mathrm{ms}$ trigger jitter:

$$\sigma_{\Delta t} = \sqrt{2(0.05)^{2} + 2(0.05)^{2}} = 0.100\ \mathrm{ms}.$$

The interval travel time across $\Delta z = 1\ \mathrm{m}$ is $\Delta z/v$:

| layer | $v$ (m/s) | $\Delta t$ (ms) | $\sigma_{\Delta t}/\Delta t$ |
|---|---|---|---|
| slow | $180$ | $5.56$ | $1.8\%$ |
| fast | $600$ | $1.67$ | $6.0\%$ |

**The fast interval is worse, by a factor of $3.33$** — exactly the velocity ratio,
because the same absolute timing error is a larger fraction of a shorter time. This
is why a down-hole survey designed for a shallow soft layer can be excellent and the
same survey's deep, stiff intervals almost useless, with no change in the equipment.

Doubling the receiver spacing halves both numbers ($0.9\%$ and $3.0\%$), which is
the cheapest available improvement.

---

## ★6 — A ratio is not a correlation

$$\frac{(N_1)_{60}}{V_s} = \frac{18}{280} = 0.0643\ \mathrm{s\,m^{-1}}.$$

Three things needed before the ratio could convert a blow count into a velocity at
another site:

1. **A population, not a point.** A regression needs many sites spanning the
   relevant range of grain size, density, ageing and stress history; one ratio is
   one realisation of a bivariate distribution.
2. **A stated functional form and its residual scatter.** The usual form is
   $\log V_s = a + b\log (N_1)_{60}$, fitted by least squares to the population;
   the quantity that matters for design is the standard error of the prediction, not
   the value of $a$.
3. **The applicable range and the refuse conditions.** A fit obtained in young
   Holocene sands is not transferable to cemented, aged or gravelly deposits, nor to
   depths or stress levels outside the fitted range — and the scatter in
   cemented/aged ground can exceed the full range of the correlation.

---

## ★7 — A programme for a $5\%$ interval velocity

**Requirement:** $5\%$ in a $180\ \mathrm{m\,s^{-1}}$ layer, with
$0.2\ \mathrm{ms}$ random trigger jitter and $0.05\ \mathrm{ms}$ pick precision
(both given).

**Geometry: same-depth (horizontal) pairs.** From ★2 the velocity is $L/t$ with
**no differencing at all**, so the timing error enters once, not twice. With
$L = 5.0\ \mathrm{m}$ and $v = 180\ \mathrm{m\,s^{-1}}$, $t = 27.78\ \mathrm{ms}$,
and a $0.2\ \mathrm{ms}$ trigger plus $0.05\ \mathrm{ms}$ pick gives
$\sigma_t = 0.206\ \mathrm{ms}$:

$$\frac{\sigma_v}{v} = \frac{0.206}{27.78} = 0.74\%,$$

comfortably inside $5\%$ with a factor of seven of margin. The same calculation for
the deepest, fastest layer the site may contain is the check: at
$600\ \mathrm{m\,s^{-1}}$, $t = 8.33\ \mathrm{ms}$ and $\sigma_v/v = 2.4\%$ — still
inside the requirement, which is why same-depth is the right choice.

**Receiver spacing and number.** For the same-depth configuration, spacing is a
*coverage* decision, not an accuracy decision: sample every $1\ \mathrm{m}$ through
the layer of interest and at least $2\ \mathrm{m}$ elsewhere, with two pairs per
layer at its top and bottom so the interval boundaries are seen and not assumed.

**Quality-control checks.**

1. **Reciprocity.** Fire A-to-B and then B-to-A at each depth pair; the two times
   must agree within the stated timing error. A disagreement larger than that is a
   trigger, coupling or borehole-deviation problem, and it is detectable in the
   field within minutes.
2. **Trigger verification.** Record a shot at zero offset (source and receiver at
   the same depth and same hole) or use a wire trigger with a known delay; a
   constant delay does not affect interval velocities but must be known to compare
   with any uphole time.
3. **Borehole deviation.** Inclinometer data for both holes, because $L$ and
   $\Delta z$ are the geometry the velocity rests on; a $1^\circ$ tilt over
   $20\ \mathrm{m}$ is $0.35\ \mathrm{m}$ of path length, i.e. $1.75\%$ of a
   $20\ \mathrm{m}$ path.
4. **Repeatability.** Re-occupy one depth pair at the end of the survey: the
   difference is a direct estimate of the whole system's timing repeatability,
   better evidence than the equipment specification.

**What would invalidate it, and the detection.** A velocity *decrease* with depth
(a soft layer beneath a stiff one) means the first arrival may be a diving wave from
above; the detection is a first-arrival time that does not vary smoothly with depth
and a reciprocity failure. A wet, casing-coupled borehole can leak tube waves into
the first break; the detection is a strong, dispersive arrival ahead of the
expected one.

---

## ★8 — Why a transferable correlation needs a population

Take the two SYNTHETIC ratios from the lesson: $(N_1)_{60}/V_s = 0.0765\
\mathrm{s\,m^{-1}}$ at $4.5\ \mathrm{m}$ and $0.0554$ at $6.0\ \mathrm{m}$. They
differ by $38\%$ within one profile of one site, at two depths $1.5\ \mathrm{m}$
apart. Two consequences follow immediately:

1. **A single ratio has no predictive content** for the other depth in the same
   hole — the ratio is itself a function of depth, because the two quantities
   respond differently to confining stress (a blow count is a strength-like
   measure, $V_s$ a stiffness-like one).
2. **A regression needs the scatter as well as the trend.** Fit
   $\log V_s = a + b\log (N_1)_{60}$ across a population; the useful statistic is
   the standard error of the prediction, $s$, and the coefficient of determination
   $R^2$. In clean sands a fit of this kind typically explains a few tens of per
   cent of the variance — i.e. the residual scatter is of the same order as the
   range of values a design would care about.

**Refuse to apply it** (i) in cemented, aged or gravelly deposits, where cementation
and fabric dominate the stiffness while the blow count responds to the skeleton
(and may be *lower* because the sampler cannot penetrate the gravel), and (ii) at
stress levels or grain sizes outside the fitted range, where $C_N$ and the
penetration mechanism change. In both cases the right measurement is a borehole or
a surface-wave $V_s$, not a converted blow count.

---

## ★9 — Two borehole surveys, one layer, $17\%$ apart

$340$ against $290\ \mathrm{m\,s^{-1}}$: a $17\%$ difference, each survey claiming
$3\%$. Ranked by likelihood in practice:

1. **Different material, or different depth.** The two holes are metres apart;
   within one geotechnical unit, $V_s$ routinely varies by $10$–$20\%$ over a metre
   vertically. *Test:* compare the depth intervals and the lithological logs, and
   check whether the down-hole value is an interval average over a heterogeneous
   span while the cross-hole value is a point measurement in the same layer.
2. **Ray-path/refraction bias in the down-hole interval** (Section 3.3 of the
   lesson). If the down-hole interval spans a velocity *decrease* or an interface,
   the straight-ray distance-difference formula returns a value between the layer
   velocities. *Test:* recompute the down-hole times with a layered model and see
   whether a single velocity can explain all the arrivals; a systematic residual
   that correlates with depth is the signature.
3. **Trigger or geometry error in the cross-hole survey.** A wrong borehole
   separation (deviation not surveyed) scales $V_s$ directly: $17\%$ is
   $0.85\ \mathrm{m}$ of a $5\ \mathrm{m}$ separation. *Test:* the inclinometer
   survey, and reciprocity between the two holes.
4. **Anisotropy or a steeply dipping fabric**, in which case both numbers are
   correct and measure different directions. *Test:* cross-hole at two azimuths.

**What to report in the meantime.** Both numbers with their geometries, the
admitted range $290$–$340\ \mathrm{m\,s^{-1}}$, and the statement that the spread is
larger than either survey's stated uncertainty, so at least one of the two is
biased. The engineering consequence must be stated too: $G_{\max}$ scales as
$V_s^2$, so a $17\%$ velocity spread is a $37\%$ stiffness spread — enough to move a
settlement prediction by more than a third.
