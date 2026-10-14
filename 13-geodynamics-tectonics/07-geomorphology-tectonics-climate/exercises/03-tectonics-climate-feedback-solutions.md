# Solutions — 13-07-03 Tectonic-Climate Feedbacks on Geological Timescales

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [03 Tectonic-Climate Feedbacks](../03-tectonics-climate-feedback.md).

---

## ★1 — The model and its terms

$$\frac{\mathrm{d}N}{\mathrm{d}t} = F_{\text{out}} - u\left(\frac{N}{N_0}\right)^{a}
e^{\beta(T-T_0)}, \qquad T = T_0 + S\log_2\!\frac{N}{N_0}.$$

- $u$ — the weathering efficiency (exposed fresh rock, runoff, weatherable
  mineral supply): a *tectonic* knob held constant in a climate experiment.
- $a$ — the exponent describing how weathering responds to the carbon reservoir
  (through the ocean chemistry and the CO$_2$ partial pressure).
- $\beta$ — the sensitivity of the weathering rate to temperature, in K$^{-1}$.
- $S$ — the climate sensitivity in K per doubling of CO$_2$: a *climate* property,
  not a carbon-cycle one.

---

## ★2 — Deriving the steady-state sensitivity

At steady state $F_{\text{out}} = u(N/N_0)^ae^{\beta S\log_2(N/N_0)}$. Take
logarithms:

$$\ln F_{\text{out}} = \ln u + a\ln\frac{N}{N_0}
+ \frac{\beta S}{\ln 2}\ln\frac{N}{N_0}
= \ln u + \left(a + \frac{\beta S}{\ln 2}\right)\ln\frac{N}{N_0}.$$

Differentiate with respect to $\ln F_{\text{out}}$ at fixed $u$:

$$\boxed{\ \frac{\mathrm{d}\ln N}{\mathrm{d}\ln F_{\text{out}}}
= \frac{1}{a + \beta S/\ln 2}\ }$$

The result is exact for this model — no linearisation was used — and it shows
that the *temperature* dependence acts exactly like an extra reservoir exponent:
the two are indistinguishable in the steady state.

---

## ★3 — The exponent for $a = 0.4$, $\beta = 0.05$, $S = 3$

$$\frac{\beta S}{\ln 2} = \frac{0.05\times3}{0.6931} = 0.2164, \qquad
a + \frac{\beta S}{\ln 2} = 0.4 + 0.2164 = 0.6164,$$

$$\frac{\mathrm{d}\ln N}{\mathrm{d}\ln F_{\text{out}}} = \frac{1}{0.6164}
= \mathbf{1.622}.$$

Without the feedback the exponent would be $1/a = 2.5$, so the feedback reduces
the CO$_2$ response by a factor of 1.54.

---

## ★4 — Temperature change for a doubling of outgassing

Closed form: a doubling is $\Delta\ln F_{\text{out}} = \ln 2$, so
$\Delta\ln N = 1.622\times\ln 2 = 1.124$, i.e. a factor $e^{1.124} = 3.077$ in
$N$. Then

$$\Delta T = S\log_2(3.077) = 3\times1.622 = 4.87\ \mathrm{K}.$$

(Indeed $\Delta T = S\log_2N$ is exactly $S\/\ln 2\times\Delta\ln N =
(3/0.6931)\times1.124 = 4.87$ K, which is why the closed form is exact here: for
this model the relation between $T$ and $\ln N$ is linear, and only the
*comparison* with a finite perturbation's curvature, as in the lesson's 10% case,
introduces a discrepancy.)

Exact steady state: solve $2F_{\text{out},0} =
u(N/N_0)^{0.4}e^{0.05\,T(N)}$ numerically, giving the same 4.87 K by
construction. The lesson's 3.5% discrepancy at a 10% perturbation arises because
there the *definition* of the closed form used a linearisation in
$\ln F_{\text{out}}$ around a different reference; here the relation is exact, so
the check is exact — a useful distinction to notice.

---

## ★5 — Equilibration time

$$\tau = \frac{1}{a+\beta S/\ln 2} = \frac{1}{0.6164} = \mathbf{1.622\ t^*}.$$

With $N_0 = 4.0\times10^{18}$ mol C and $F_{\text{out}} = 1.0\times10^{13}$ mol C/yr:

$$t^* = \frac{4.0\times10^{18}}{1.0\times10^{13}} = 4.0\times10^{5}\ \mathrm{yr},
\qquad \tau = 1.622\times4.0\times10^{5} = 6.5\times10^{5}\ \mathrm{yr}.$$

So the thermostat equilibrates in a few hundred thousand years — fast compared
with a 10 Myr tectonic ramp.

---

## ★6 — Two parameter sets, same present state

$$\text{set 1: } 0.05 + \frac{0.05\times3}{\ln 2} = 0.05+0.2164 = 0.2664,$$
$$\text{set 2: } 0.80 + \frac{0.20\times3}{\ln 2} = 0.80+0.8656 = 1.6656 .$$

Both reproduce the present state by construction (the weathering law is
normalised to $F_w(N_0) = F_{\text{out},0}$), but they have very different total
sensitivities. The predicted ratio of their temperature responses is

$$\frac{1/0.2664}{1/1.6656} = \frac{1.6656}{0.2664} = 6.25,$$

against the lesson's measured 11.261/1.801 = 6.25 ✓. Note that the *ratio* is
predicted exactly by the closed form even though the absolute values are not: the
degeneracy is in the sensitivity, and the sensitivity is exactly computable from
the parameters.

---

## ★7 — Is the response complete by the end of a 10 Myr ramp?

$\tau = 6.5\times10^{5}$ yr (★5), so the ramp lasts $10^{7}/6.5\times10^{5} =
15.4$ relaxation times. The response is complete to better than one part in
$10^{6}$; **no lag is detectable** for these parameters.

**Observable that would reveal a lag if it were not complete.** A mismatch between
the *timing* of the forcing and the timing of the climate response: in the
complete case the CO$_2$ minimum coincides with the peak weathering efficiency
(the end of the ramp); with a lag it trails it by of order $\tau$. In the record,
that means comparing the age of the tectonic marker (an exhumation episode dated
by thermochronology) with the age of the CO$_2$ minimum to within $\tau$ — so the
required geochronological precision is better than $\tau$, which for plausible
parameters (a few $10^{5}$ yr) is demanding but achievable.

---

## ★8 — A validation statement

> The Cenozoic decline in CO$_2$ was caused by increased silicate weathering
> driven by the growth of mountain belts. We test this by requiring that an
> independent record of weathering intensity (for example a lithium-isotope or
> a strontium-isotope record) rise *before* the CO$_2$ decline, by an amount
> consistent with the modelled lag of order 0.5 Myr; that the spatial pattern of
> weathering (recorded in marginal-marine sediments on the continental shelves
> surrounding the orogen) coincide with the orogen rather than with the global
> rainfall pattern; and that the total CO$_2$ drawdown over the interval equal
> the integral of the outgassing-weathering imbalance, which requires an
> independent outgassing history.

**Discriminating observation.** A *time-resolved weathering proxy* at a location
whose tectonic history is independently dated. The uplift hypothesis predicts
that the weathering signal leads the CO$_2$ decline (the response has a lag), and
that the spatial pattern follows the tectonic belt. **A climate-feedback
explanation** predicts that the weathering signal *follows* the CO$_2$ decline
(warmer and wetter means more weathering) and that the spatial pattern follows
the rainfall and temperature pattern, which does not respect the tectonic belt.
The observation must therefore be time-resolved to better than the lag
(sub-million-year) and spatially located (a transect across the orogen), which is
exactly why such records are so hard to obtain.

---

## ★9 — A synthetic recovery test for $a$ and $\beta$

**Dataset.** (i) a synthetic temperature record sampled every 1 Myr with
$\pm1$ K noise; (ii) a synthetic outgassing proxy with a stated multiplicative
uncertainty, say 20% per point.

**Metric.** The joint posterior (or the admitted set) in the $(a,\beta)$ plane,
mapped by exploring the forward model's steady state for each parameter pair; the
quantity to report is the *width* of the admitted band, not the best-fit point.

**Expected degeneracy.** Only the combination $a + \beta S/\ln 2$ appears in the
steady-state relation (★2). With a fixed $S$, a one-parameter family of
$(a,\beta)$ pairs fits any temperature record exactly, so the admitted set is a
line with slope $\mathrm{d}\beta/\mathrm{d}a = -\ln 2/S = -0.231$ K$^{-1}$.

**Precision required.** The degeneracy is broken only by a record that samples
the *individual* dependences — for instance an independent, time-resolved
outgassing history, which converts the experiment from "fit the sum" to "fit the
two terms". Quantitatively: distinguishing $\beta = 0.05$ from $\beta = 0.06$
changes $a+\beta S/\ln 2$ by 0.043, i.e. a 7% change in the steady-state CO$_2$
response, so the outgassing proxy must constrain relative changes to better than
about 5% — an order of magnitude better than typical proxies. The honest
conclusion of such a test is usually a *bound* on the combination, not separate
values of $a$ and $\beta$.

---

## ★10 — Ranking the three omissions

**(a) Equilibration time.** The dominant omission is the **ocean buffering**,
then organic carbon, then carbonate weathering.

*Argument.* The equilibration time is the reservoir divided by the sink's
sensitivity. Ocean buffering changes *how much carbon the climate system holds
for a given atmospheric CO$_2$* — i.e. it changes the effective reservoir $N$ by
a large factor, because most of the carbon is in the ocean as bicarbonate. A
larger effective reservoir lengthens $\tau$ proportionally, so omitting it can
change the timescale by an order of magnitude in the wrong direction. Organic
carbon has a much shorter residence time (thousands of years) and participates in
the glacial-interglacial cycle rather than in the 10 Myr balance, so its effect on
a million-year timescale is small. Carbonate weathering responds on tens of
thousands of years — faster than silicate weathering but coupled to the same
ocean chemistry — so it adds a term that partly overlaps with buffering rather
than acting on a distinct timescale.

**(b) Steady-state sensitivity.** Here the ranking reverses: **carbonate
weathering** first, then ocean buffering, then organic carbon.

*Argument.* The steady-state sensitivity of the *silicate* thermostat is its
response to temperature and CO$_2$; a second, faster-responding carbonate sink
takes up part of the imbalance and therefore *flattens* the effective sensitivity
of the whole system — it is an additional negative feedback acting on the same
variable, so its omission overestimates the steady-state sensitivity. Buffering
redistributes the same carbon between reservoirs and changes the sensitivity by a
smaller factor (it is largely a rescaling of $N$), and organic carbon is small at
these timescales.

The general lesson is that an omission's importance depends on the question: a
model can be adequate for a *rate* question (where the fast sinks are the large
error) and inadequate for a *level* question (where the competing sinks are), and
a study that reports only one of the two has not tested its model against the
regime it is being used in.
