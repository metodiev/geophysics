# Solutions — 14-01-01 The Hydrologic Cycle and Water Balance

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All catchments are **SYNTHETIC**.

Lesson: [01 The Hydrologic Cycle and Water Balance](../01-hydrologic-cycle.md).
Constants used: 1 mm over 1 km$^2$ $= 1000$ m$^3$; 1 Julian year
$= 3.15576 \times 10^{7}$ s.

---

## ★1 — Depth to volume

Using $V = d \times 10^{-3} \times A \times 10^{6}$ m$^3$ with $d$ in mm and $A$
in km$^2$:

(a) $V = 25 \times 10^{-3} \times 12 \times 10^{6} = 3.0 \times 10^{5}$ m$^3$.

(b) $V = 1 \times 10^{-3} \times 10^{6} = 1000$ m$^3$ — the identity in the lesson.

(c) $V = 320 \times 10^{-3} \times 250 \times 10^{6} = 8.0 \times 10^{7}$ m$^3$ yr$^{-1}$.

---

## ★2 — Closing a balance

$$\Delta S = 1000 - 600 - 350 = 50\ \mathrm{mm\,yr^{-1}}.$$
$$Q/P = 350/1000 = 0.350, \qquad ET/P = 600/1000 = 0.600, \qquad
\Delta S/P = 50/1000 = 0.050.$$
Sum: $0.350 + 0.600 + 0.050 = 1.000$ ✔. The catchment gained 50 mm of water,
i.e. 5% of precipitation.

---

## ★3 — Residence time

$$\tau = \frac{V}{Q_v} = \frac{2.4 \times 10^{8}}{3.0 \times 10^{7}}
= 8.00\ \mathrm{yr}, \qquad
8.00 \times 365.25 = 2922\ \mathrm{d}.$$

Comment: 8 years is long enough that a contaminant entering this store would
travel roughly $1/8$ of the way to the outlet per year on average. It is also
long enough that a single dry year tells you nothing about the store's status.

---

## ★★4 — Depth rate to discharge

$$V = 350 \times 10^{-3}\ \mathrm{m} \times 400 \times 10^{6}\ \mathrm{m^2}
= 1.40 \times 10^{8}\ \mathrm{m^3\,yr^{-1}},$$
$$Q_v = \frac{1.40 \times 10^{8}\ \mathrm{m^3}}{3.15576 \times 10^{7}\ \mathrm{s}}
= 4.436\ \mathrm{m^3\,s^{-1}} \approx 4436\ \mathrm{L\,s^{-1}}.$$

Unit cancellation: $\mathrm{m}\,\mathrm{m^2} = \mathrm{m^3}$, divided by
$\mathrm{s}$ gives $\mathrm{m^3\,s^{-1}}$. If your answer came out near $1.4
\times 10^{8}$ you divided by nothing; if it came out near $1.4 \times 10^{11}$
you converted km$^2$ to m$^2$ twice.

---

## ★★5 — Error amplification with a small residual

$\Delta S = 1200 - 800 - 380 = 20\ \mathrm{mm\,yr^{-1}}$.

| Term | 5% or 10% of value | Shift in $\Delta S$ | % of $\Delta S = 20$ |
|---|---|---|---|
| $P = 1200$ | $\pm$60 | $+60$ | 300% |
| $ET = 800$ | $\pm$80 | $-80$ | 400% |
| $Q = 380$ | $\pm$19 | $-19$ | 95% |

The residual is 1.7% of precipitation, so a 5% error in precipitation is three
times the answer. For $Q$ to contribute only 10% of $\Delta S$ we need
$0.10 \times 20 = 2.0\ \mathrm{mm}$, i.e. a fractional error
$2.0/380 = 0.53\%$:

$$Q \text{ must be accurate to about } 0.5\%.$$

**Interpretation.** The smaller the true storage change, the better the
measurements must be — and no measurement of $P$ available from a rain-gauge
network reaches 0.5%. This is the quantitative reason that storage change is
measured by other means (water levels, gravity) rather than inferred as a
residual.

---

## ★★6 — Baseflow as a discharge

$$Q_{\text{total}} = \frac{574.8 \times 10^{-3} \times 250 \times 10^{6}}
{3.15576 \times 10^{7}} = 4.554\ \mathrm{m^3\,s^{-1}},$$
$$Q_{\text{base}} = \frac{434.7 \times 10^{-3} \times 250 \times 10^{6}}
{3.15576 \times 10^{7}} = 3.444\ \mathrm{m^3\,s^{-1}},$$
$$Q_{\text{storm}} = \frac{140.0 \times 10^{-3} \times 250 \times 10^{6}}
{3.15576 \times 10^{7}} = 1.109\ \mathrm{m^3\,s^{-1}}.$$

Sum of parts: $3.444 + 1.109 = 4.553\ \mathrm{m^3\,s^{-1}}$ against a total of
$4.554$: a discrepancy of $0.001\ \mathrm{m^3\,s^{-1}}$, i.e. 0.02%. The cause is
rounding in the printed mm values ($434.7 + 140.0 = 574.7 \ne 574.8$). **Check
closure before interpreting the split** — a closure error is the quickest way to
catch a unit mistake.

---

## ★★7 — Recession constant

$Q(t) = 12.0\,e^{-t/45}$ mm d$^{-1}$:

| $t$ (d) | 0 | 30 | 60 | 90 |
|---|---|---|---|---|
| $Q$ (mm d$^{-1}$) | 12.00 | 6.161 | 3.163 | 1.624 |

Check the form of the decay: each 45-day step multiplies $Q$ by
$e^{-1} = 0.3679$, so $12.00 \times 0.3679 = 4.415$ mm d$^{-1}$ at $t = 45$,
and $6.161$ at $t = 30$ is
$12.00\,e^{-30/45} = 12.00 \times 0.5134 = 6.161$ ✔.

From two points:
$$\ln\frac{Q(0)}{Q(20)} = \ln\frac{6.00}{3.00} = \ln 2 = 0.6931
= \frac{20}{\tau},$$
$$\tau = \frac{20}{0.6931} = 28.85\ \mathrm{d}.$$

Note that the two-point estimate requires **two points on the same recession with
no recharge in between**. Using points that straddle a storm inflates $\tau$; this
is the systematic error that the least-squares fit of the lesson (30.94 d against
a true 30.00 d, 3.1% high) shows in miniature.

---

## ★★★8 — Detecting a decline: a design, with an error budget

Neither a single method nor a single year suffices. The table states what each
method measures and the assumed detection threshold; **every threshold must be
stated as an assumption in a real study**, because it comes from the instrument and
the survey design, not from physics alone.

| Method | Measures directly | Assumed threshold (mm of water) | Systematic error that mimics a trend |
|---|---|---|---|
| Repeat water-level survey | water-table elevation | $S_y \times 1\ \mathrm{cm}$; for $S_y = 0.1$ this is 1.0 mm | land subsidence; a changed datum or benchmark |
| Repeat microgravity | mass change (Bouguer slab) | $\approx 12$ mm for a 5 µGal repeatability (below) | instrument drift; water-table depth change with no mass change |
| Satellite gravimetry | total water storage (incl. soil, snow, surface) | 20–50 mm at basin scale (assumed) | leakage from neighbouring basins; glacial-isostatic and other solid-Earth signals |
| Water balance (this lesson) | nothing directly; constrains fluxes | $\gtrsim$ 40 mm yr$^{-1}$ (Section 5 error budget) | a single unmeasured flux |
| Recession analysis | drainable storage | $\approx 1$–5 mm via $\tau \times \bar Q$ | changing ET during recession |

**Microgravity arithmetic.** A water-table change $\Delta h$ in an infinite slab of
density $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$ produces
$$\Delta g = 2\pi G \rho_w \Delta h
= 2\pi (6.674 \times 10^{-11})(1000)(\Delta h)
= 4.193 \times 10^{-7}\ \Delta h \ \mathrm{m\,s^{-2}}\,(\Delta h \text{ in m}).$$
Using $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ and
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$:
$$\Delta g = 41.9\ \mathrm{\mu Gal} \text{ per metre of water table}.$$
A 5 µGal repeatability therefore resolves
$\Delta h = 5/41.9 = 0.119\ \mathrm{m}$ of water-table change, which for
$S_y = 0.1$ is $0.1 \times 119 = 11.9\ \mathrm{mm}$ of stored water. Note the
$\rho_w = 1000\ \mathrm{kg\,m^{-3}}$ and $G = 6.674 \times 10^{-11}\
\mathrm{m^3\,kg^{-1}\,s^{-2}}$ used — both are exact standard constants of the
model.

**Why one year cannot work.** From the lesson's error budget, a 5% error on $P$
alone moves $\Delta S$ by 42.5 mm on a 50 mm signal. A $5\ \mathrm{mm\,yr^{-1}}$
decline is one tenth of one term's plausible error. Averaging $N$ independent years
reduces a random error by $1/\sqrt{N}$, so reaching an uncertainty of
$5\ \mathrm{mm\,yr^{-1}}$ at 1σ requires roughly
$N \approx (42.5/5)^2 = 72$ years of *independent* precipitation errors — and
precipitation errors are correlated, not independent, so the honest statement is
that the water balance cannot detect this trend at all.

**Design that can.** Ten years, three independent legs:

1. **Water levels** in 6–10 piezometers, quarterly, with two benchmarked
   survey-grade levelling ties per campaign. Expected noise
   $\approx 1\ \mathrm{mm}$ of stored water per campaign at $S_y = 0.1$, so a
   $5\ \mathrm{mm\,yr^{-1}}$ trend is
   $5 \times 10 = 50\ \mathrm{mm}$ over the decade — a factor of 50 above the
   per-campaign noise, i.e. clearly detectable, provided the datum is stable. This
   leg carries the detection.
2. **Microgravity** on a fixed grid, annually, to check that the water-level
   story is a mass story and not a subsidence- or datum-driven artefact. Its
   12 mm threshold cannot detect the trend year on year, but over 10 years the
   cumulative $50\ \mathrm{mm}$ is $50/11.9 = 4.2$ times its threshold, so it can
   confirm the signal.
3. **Recession analysis** each year, to show the store's discharge constant is not
   changing, which is the alternative explanation for a declining water level.

The two legs that *measure mass or level* do the detection; the balance is used
only as a consistency check, and its failure to close is treated as evidence of an
unmeasured flux rather than as a measurement.

---

## Mastery checkpoint — worked

Synthetic catchment: $A = 400\ \mathrm{km^2}$, $P = 700$, $Q = 210$,
$\Delta S = 80\ \mathrm{mm\,yr^{-1}}$.

**(a) ET and the ratios.**
$$ET = P - Q - \Delta S = 700 - 210 - 80 = 410\ \mathrm{mm\,yr^{-1}}.$$
$$Q/P = 210/700 = 0.300, \quad ET/P = 410/700 = 0.586, \quad
\Delta S/P = 80/700 = 0.114.$$
Sum: $0.300 + 0.586 + 0.114 = 1.000$ ✔ (the third ratio is $0.1143$ before
rounding, so the rounded sum lands on 1.000).

**(b) Volumes and discharge.**
$$V_P = 700 \times 10^{-3} \times 400 \times 10^{6} = 2.80 \times 10^{8}\
\mathrm{m^3\,yr^{-1}},$$
$$V_Q = 210 \times 10^{-3} \times 400 \times 10^{6} = 8.40 \times 10^{7}\
\mathrm{m^3\,yr^{-1}},$$
$$Q_v = \frac{8.40 \times 10^{7}}{3.15576 \times 10^{7}}
= 2.662\ \mathrm{m^3\,s^{-1}} \approx 2662\ \mathrm{L\,s^{-1}}.$$

**(c) ET range consistent with $\Delta S = 80 \pm 20\ \mathrm{mm\,yr^{-1}}$.**
$ET = P - Q - \Delta S = 490 - \Delta S$, so $\Delta S \in [60, 100]$ gives
$$ET \in [490 - 100,\ 490 - 60] = [390,\ 430]\ \mathrm{mm\,yr^{-1}}.$$
The uncertainty is symmetric in mm but the *relative* uncertainty in $ET$ is only
$\pm 5\%$ while the relative uncertainty in $\Delta S$ is $\pm 25\%$. Large terms
are measured well; small residual terms are not.

**(d) Storage volume implied by $\tau = 4.2$ yr.**
$$V = \tau\,Q_v = 4.2 \times 8.40 \times 10^{7} = 3.53 \times 10^{8}\ \mathrm{m^3}.$$
As a depth over the catchment:
$$3.53 \times 10^{8} / (400 \times 10^{6}) = 0.882\ \mathrm{m} = 882\ \mathrm{mm}.$$
Plausibility: 882 mm of *drainable* water is 1.26 times the annual precipitation
and 4.2 times the annual runoff. That is a plausible thickness of mobile water
(for example a 15–30 m thick aquifer with a specific yield of 3–6%), so the claim
is not absurd — but it is a claim about *mobile* water. If the colleague meant
total water in the rock, 882 mm would correspond to a much thinner saturated
thickness and the number would be an under-estimate of the store. The answer
therefore ends with a question about definitions, not just a number.

**(e) The question about the baseflow index.** Ask: *what filter time constant and
what filter equation defined it?* From the lesson's table, the same data give a
baseflow index anywhere from 0.525 to 0.950 as the filter constant moves from 120 d
to 5 d. An index of 0.85 is reproducible only if the definition travels with it.
