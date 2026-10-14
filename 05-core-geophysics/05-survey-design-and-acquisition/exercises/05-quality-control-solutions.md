# Solutions — 05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata

> **Read this after attempting the exercises, not before.**

---

## ★1 — Combining in quadrature

$$\sigma_{\text{tot}} = \sqrt{0.020^{2} + 0.050^{2} + 0.100^{2}}
= \sqrt{0.0004 + 0.0025 + 0.0100} = \sqrt{0.0129} = \boxed{0.1136\ \mathrm{mGal}}.$$

Shares of the variance: $0.020^{2}/0.0129 = 3.1\%$, $0.050^{2}/0.0129 = 19.4\%$,
$0.100^{2}/0.0129 = \boxed{77.5\%}$. The 0.100 mGal term dominates, exactly as the
lesson's measured budget shows the positioning term carrying 87.9 %.

---

## ★2 — Mean, standard deviation and its uncertainty

Mean $= (979.100+979.104+979.098+979.102+979.096)/5 = \boxed{979.1000\ \mathrm{mGal}}$.

Deviations (mGal): $0.000, +0.004, -0.002, +0.002, -0.004$; sum of squares
$= 0 + 1.6\times10^{-5} + 4\times10^{-6} + 4\times10^{-6} + 1.6\times10^{-5}
= 4.0\times10^{-5}$.

$$s = \sqrt{\frac{4.0\times10^{-5}}{5-1}} = \sqrt{1.0\times10^{-5}}
= \boxed{0.00316\ \mathrm{mGal}}.$$

Relative standard error of $s$: $1/\sqrt{2(N-1)} = 1/\sqrt{8} = \boxed{35\%}$. **The
figure 0.0032 mGal should be quoted as roughly 0.003 ± 0.001 mGal**, or the
repeatability should be measured from far more occupations.

---

## ★3 — Tie and loop closure

A **tie** is a measurement connecting two reference points — a re-occupation of a base
station, or a link between two networks. A **loop closure** is the specific case of a
tie whose start and end are the same station within one traverse; its misclosure is
the accumulated error, $\dot d T + \epsilon$ in the lesson's notation.

---

## ★4 — Mislosure and residual

Mislosure $= \dot d T = 0.025 \times 30 = \boxed{0.75\ \mathrm{mGal}}$.

Residual $= \sigma_c/\sqrt{m} = 0.008/\sqrt{4} = \boxed{0.004\ \mathrm{mGal}}$
(equation (5) of the lesson). Note the residual does not depend on $T$; the *true*
nonlinear part of the drift, however, does scale with $T$, as question ★★8(c)
explores.

---

## ★5 — Irrecoverable metadata

| item | why irrecoverable |
|---|---|
| time of each reading, with the clock source | the elapsed time between stations determines the drift correction; a notebook entry with no time zone cannot be reconciled with a tide model |
| instrument pole height and how it was measured | a systematic height error of 1 cm is 0.0031 mGal and leaves no trace in the data |
| which geoid model was used for the heights | the largest budget term depends on it; a different model gives a different anomaly |
| weather, ground condition and setup anomalies | these are the only explanation for an outlier station; the data cannot say why it was bad |
| base-station readings with their times | the drift correction is *defined* by them |

Any of these can be *guessed* afterwards, but a guess is not a record.

---

## ★★6 — Halving the dominant term

**(a)** $\sqrt{0.080^{2} + 0.030^{2}} = \sqrt{0.0064+0.0009} = \sqrt{0.0073}
= \boxed{0.08544\ \mathrm{mGal}}$. (Note the terrain term carries
$0.0064/0.0073 = 87.7\%$ of the variance.)

**(b)** Halving the terrain term: $\sqrt{0.040^{2}+0.030^{2}} = \sqrt{0.0025}
= \boxed{0.05000\ \mathrm{mGal}}$ — an improvement of $(0.08544-0.05000)/0.08544
= \boxed{41.5\%}$.

**(c)** Halving the others: $\sqrt{0.080^{2}+0.015^{2}} = \sqrt{0.006625}
= \boxed{0.08139\ \mathrm{mGal}}$ — an improvement of $4.7\%$.

The comparison is the lesson's point in numbers: **halving the dominant term improves
the total by 41.5 %, halving the rest improves it by 4.7 %.** Resources go where the
variance is.

---

## ★★7 — Repeatability from six occupations

**(a)** $1/\sqrt{2 \times 5} = \boxed{31.6\%}$.

**(b)** $(N-1)s^{2}/\sigma^{2} \sim \chi^{2}_{5}$, so the interval for $\sigma^{2}$ is
$\left[\dfrac{5s^{2}}{12.83}, \dfrac{5s^{2}}{0.831}\right]$ and for $\sigma$:

$$\sigma \in \left[s\sqrt{\frac{5}{12.83}},\; s\sqrt{\frac{5}{0.831}}\right]
= \left[0.624\,s,\; 2.453\,s\right] = \boxed{[0.0094,\ 0.0368]\ \mathrm{mGal}}$$

for $s = 0.015$ mGal. The interval spans a factor 3.9, so the reported figure is
consistent with anything from 0.009 to 0.037 mGal.

**(c)** For 10 % relative standard error, $1/\sqrt{2(N-1)} = 0.10$ →
$N-1 = 50$ → $N = \boxed{51}$ occupations. This is why a serious repeatability
claim comes from a dedicated test with tens of occupations, not from a handful.

---

## ★★8 — Drift over a 9-hour day

**(a)** $\dot d T = 0.02 \times 0.75 = \boxed{0.015\ \mathrm{mGal}}$ maximum
accumulated drift within one 45-minute loop.

**(b)** Residual $= \sigma_c/\sqrt{m} = 0.010/\sqrt{12} = \boxed{0.0029\ \mathrm{mGal}}$.

**(c)** Equation (5) of the lesson describes the error in the *estimated rate*, which
is a single straight line. Any curvature in the true drift is not represented by that
line, and the residual from curvature grows with the loop length: a quadratic term
$\tfrac12 \ddot d T^{2}$ over the loop doubles when $T$ doubles while the
rate-estimation residual $\sigma_c/\sqrt{m}$ is unchanged. **So doubling the loop
interval doubles the curvature-driven residual while leaving the noise-driven
residual alone** — which is why the formula alone understates the penalty of long
loops, and why the honest budget reports both parts separately.

---

## ★★9 — Base-station time series

**(a)** $\dot d = 0.9/8 = \boxed{0.1125\ \mathrm{mGal\,h^{-1}}}$ (about
0.00188 mGal/min).

**(b)** The repeatability of a single occupation is the scatter about the fitted
line: $\boxed{0.011\ \mathrm{mGal}}$.

**(c)** The **absolute** accuracy depends on the base station's own absolute value
and on its *stability* — whether the monument has moved since the previous campaign.
The 20 re-occupations constrain the *relative* repeatability and the drift, but they
are all tied to the same monument, so a monument that has settled by 5 mm contributes
0.0015 mGal to every station and is invisible to this test. Detecting it needs an
independent reference — a different monument tied by levelling, or an absolute
instrument.

---

## ★★★10 — Correlation length and the repeatability estimate

A satisfactory experiment:

1. **Generate correlated noise** with a chosen correlation length $\ell$ (e.g. via a
   Gaussian-filtered white field, or an exponential covariance), along a line.
2. **Simulate repeated occupations** of a set of stations, where the noise is the
   *same realisation* for stations within one occupation but fresh between
   occupations, and where spatial correlation exists within an occupation.
3. **Estimate repeatability** as the scatter of repeated readings per station, and
   also as the scatter pooled across stations.
4. **Expected result:** the per-station estimate is *unbiased* for the local noise
   level (because repeated occupations resample the temporal noise), but the
   *spatially pooled* estimate is biased high whenever $\ell$ is comparable with the
   station spacing, because neighbouring stations share a large common component that
   is not independent.
5. **Implication:** a repeatability quoted from a *set of stations* implicitly
   includes any spatially correlated component, while one quoted from a *single*
   station does not. The two numbers differ, and a report must say which was
   measured.

---

## ★★★11 — Correlated budget terms

Using $\sigma_{1+2}^{2} = \sigma_1^{2}+\sigma_2^{2}+2\rho\sigma_1\sigma_2$ with
$\sigma_1 = 0.154$ (positioning) and $\sigma_2 = 0.050$ (terrain):

| $\rho$ | correct $\sigma_{1+2}$ | quadrature value | error of the quadrature assumption |
|---|---|---|---|
| 0.0 | 0.16191 | 0.16191 | 0 % |
| 0.5 | 0.17717 | 0.16191 | **−8.6 %** (understates) |
| 0.9 | 0.18822 | 0.16191 | **−14.0 %** (understates) |

Two plausible strongly correlated pairs in a real survey:

1. **Vertical positioning and the terrain correction.** Both depend on the same
   digital elevation model; if the DEM is wrong, both are wrong in the same
   direction, and $\rho$ can be large. In the extreme, the free-air and terrain
   corrections are *designed* to be complementary and can partially cancel, which
   means the quadrature assumption overstates the pairing rather than understating it
   — the sign of the correlation depends on how both are computed. This is why the
   defensible statement is "these terms are correlated and their combined effect must
   be estimated jointly", not "the total is the quadrature sum".
2. **Tidal correction residual and drift residual.** Both are smooth functions of
   time. Over a survey day they are partially aliased with each other: a linear drift
   fitted to data that still contain a tidal residual will absorb part of the tide.
   $\rho > 0$ between the two residuals after correction, and the quadrature sum
   understates the total by several per cent.

---

## ★★★12 — Critique of the single-station proposal

A satisfactory critique covers:

- **What it does measure:** the *instrument and setup* scatter, together with the
  temporal noise that varies over the duration of the 200 occupations. It also
  constrains the drift, if the series is long enough for a rate to be fitted, and
  (with a spectral analysis) any periodic component such as a tidal residual.
- **What it does not measure:** anything spatially varying. The terrain-correction
  residual, the geoid/datum error, the near-surface coupling variation between
  stations, and the *spatial* component of cultural noise are all invisible at one
  site. The budget term that dominates the lesson's measured budget — vertical
  positioning at 87.9 % of the variance — is precisely a spatial term and is entirely
  unconstrained by the proposal.
- **The temptation it creates:** a 200-occupation test produces a small, precise,
  *unrepresentative* number. Publishing it as "the survey repeatability" reports the
  best-behaved term as if it were the total.
- **A design that does constrain the missing terms:** (i) repeat occupations at a
  *set* of stations spread across the survey area, including the wettest, driest,
  noisiest and most topographically extreme sites; (ii) a repeat of a whole line,
  compared with independent positioning; (iii) simultaneous base-station recording to
  separate temporal from spatial effects; (iv) an independent levelling or GNSS check
  of a subset of heights to bound the datum term.
