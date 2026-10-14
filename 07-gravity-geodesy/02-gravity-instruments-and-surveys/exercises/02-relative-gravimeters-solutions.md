# Solutions — 07-02-02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](../02-relative-gravimeters.md).

---

## ★1 — A plain spring

$$\omega_{0}^{2} = \frac{k}{m} = \frac{3.948}{0.10} = 39.48\ \mathrm{s^{-2}},
\qquad f_{0} = \frac{\sqrt{39.48}}{2\pi} = 1.0000\ \mathrm{Hz}.$$

$$\text{static extension} = \frac{g}{\omega_{0}^{2}}
= \frac{9.820250}{39.48} = 0.248740\ \mathrm{m} = 248.74\ \mathrm{mm}.$$

$$\frac{\mathrm{d}x}{\mathrm{d}g} = \frac{1}{\omega_{0}^{2}}
= \frac{1}{39.48} = 2.53293\times10^{-2}\ \mathrm{m\ per\ m\,s^{-2}},$$

$$\text{so } 1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}
\;\longrightarrow\; 2.53293\times10^{-10}\ \mathrm{m} = 0.2533\ \mathrm{nm}.$$

The doubling of the mass from the lesson's example doubles the static extension but
leaves the *sensitivity* $\mathrm{d}x/\mathrm{d}g = m/k$ unchanged, because $k$ was
doubled with it. Sensitivity is governed by the frequency, not by the mass: to move
more per microgal, lower the frequency.

---

## ★2 — Readout noise in gravity units

$$5\ \mathrm{nm} \;\longrightarrow\;
\frac{5\times10^{-9}}{2.53293\times10^{-2}} = 1.974\times10^{-7}\
\mathrm{m\,s^{-2}} = 19.74\ \mathrm{\mu Gal}.$$

Equivalently $5\ \mathrm{nm}/0.2533\ \mathrm{nm} = 19.74$ times the microgal
displacement. **A 5 nm readout on a 1 Hz spring is a twenty-microgal instrument**:
this is the quantitative statement of why the plain spring is inadequate, and it is
the design pressure behind astatisation (★★4).

---

## ★3 — Non-linearity residual

$$\max\left|\text{residual}\right| = \tfrac23 c_{2}L^{2}
= \tfrac23 \times 4\times10^{-12}\times\left(4.0\times10^{4}\right)^{2}
= \tfrac23\times4\times10^{-12}\times1.6\times10^{9}
= 4.2667\times10^{-3}\ \text{counts}.$$

Converting counts to microgal through $c_{1} = 2\times10^{-3}$ counts/µGal
(so 1 count $= 500$ µGal):

$$\text{residual} = \frac{4.2667\times10^{-3}}{2\times10^{-3}}
= 2.1333\ \mathrm{\mu Gal}.$$

**Comment.** The quadratic coefficient here is only
$4\times10^{-12}$ counts/µGal², and the non-linearity at the span end is
$c_{2}L/c_{1} = 8\times10^{-5}$ of the reading — yet it leaves $2.1\
\mathrm{\mu Gal}$, comparable with a microgal target. The lesson's table gives the
same message with different numbers, and both follow from the same formula: the
residual grows as the *square* of the span, so the residual is a diagnostic of the
span as much as of the instrument.

---

## ★★4 — An astatic sensor with $\eta = 0.995$

$$A = \frac{1}{1-\eta} = \frac{1}{0.005} = 200.$$

Effective stiffness relative to a 1 Hz spring:

$$k_{\text{eff}} = k\left(1-\eta\right) = 0.005\,k,
\qquad
\omega_{\text{eff}}^{2} = 39.478\times0.005 = 0.197392\ \mathrm{s^{-2}},$$

$$T = \frac{2\pi}{\omega_{\text{eff}}} = 14.142\ \mathrm{s},$$

$$\frac{\mathrm{d}x}{\mathrm{d}g} = \frac{1}{\omega_{\text{eff}}^{2}}
= 5.06606\ \mathrm{m\ per\ m\,s^{-2}}
\;\Longrightarrow\;
1\ \mathrm{\mu Gal} \;\longrightarrow\; 50.66\ \mathrm{nm}.$$

(The mass does not enter: $k_{\text{eff}}$ and $m$ would scale together. Quoting
$m = 0.05\ \mathrm{kg}$ fixes $k_{\text{eff}} = 0.05\times0.197392 = 9.8696\times
10^{-3}\ \mathrm{N\,m^{-1}}$.)

So a $15\ \mathrm{s}$ period and $200\times$ amplification turn a
$0.25\ \mathrm{nm}$ requirement into a $50.7\ \mathrm{nm}$ requirement — comfortably
within optical or capacitive readout. The cost is what ★★5 computes.

---

## ★★5 — The geometric price of the amplification

With $l = 0.30\ \mathrm{m}$ and $\eta = 0.995$,

$$l - l_{0} = l\left(1-\eta\right) = 1.5000\times10^{-3}\ \mathrm{m},$$

$$\delta g_{\text{equiv}} = g\,\frac{\delta l_{0}}{l-l_{0}}
= \frac{9.820250}{1.5000\times10^{-3}}\,\delta l_{0}
= 6546.83\ \delta l_{0}\ \mathrm{m\,s^{-2}\ per\ m}.$$

| $\delta l_{0}$ (m) | $\delta g_{\text{equiv}}$ |
|---|---|
| $10^{-10}$ (0.1 nm) | $6.5468\times10^{-7}\ \mathrm{m\,s^{-2}} = 65.47\ \mathrm{\mu Gal}$ |
| $10^{-7}$ (0.1 µm) | $6.5468\times10^{-4}\ \mathrm{m\,s^{-2}} = 65\,468\ \mathrm{\mu Gal}$ |

**Stability for $0.2\ \mathrm{\mu Gal}$:**

$$\delta l_{0} = \frac{0.2\times10^{-8}}{6546.83} = 3.055\times10^{-13}\ \mathrm{m}.$$

A third of a picometre. Note the comparison with ★★4: the amplification relaxed the
*readout* requirement from $0.25\ \mathrm{nm}$ to $50.7\ \mathrm{nm}$, while it
tightened the *geometric stability* requirement from a level set by the plain
spring's $1\ \mathrm{Hz}$ geometry to $0.3\ \mathrm{pm}$. **The product of the two
requirements is essentially fixed**, which is the quantitative form of "astatisation
buys readout resolution, not stability".

---

## ★★6 — The temperature that the geometry demands

With $\mathrm{d}l_{0}/\mathrm{d}T = 5\times10^{-9}\ \mathrm{m\,K^{-1}}$:

$$\frac{\mathrm{d}g}{\mathrm{d}T} = 6546.83\times5\times10^{-9}
= 3.2734\times10^{-5}\ \mathrm{m\,s^{-2}\,K^{-1}}
= 3273.4\ \mathrm{\mu Gal\,K^{-1}},$$

$$\delta T = \frac{0.2\times10^{-8}}{3.2734\times10^{-5}} = 6.11\times10^{-5}\ \mathrm{K}.$$

**Is $6\times10^{-5}\ \mathrm{K}$ achievable with a simple enclosure?** No. A
passive enclosure in a field environment holds temperature to perhaps a tenth of a
kelvin, three orders of magnitude too loose. Reaching $6\times10^{-5}\ \mathrm{K}$
requires active thermostats with feedback, thermal mass and long settling times —
which is exactly why such instruments are built as thermostatted, insulated
assemblies and why they must be allowed to settle after transport.

**What it implies for a survey.** The requirement cannot be met by the enclosure
alone over a full day outdoors, so the survey must (i) accept a temperature-driven
drift and *measure* it by re-occupying a base, (ii) keep the instrument's
environment as stable as possible (shade, insulation, no direct sun, short
transects), and (iii) treat any large temperature excursion as an event that
invalidates the drift model for that interval. This is the mechanical origin of the
loop-and-tie procedure of lesson [03](../03-survey-procedures.md).

---

## ★★★7 — A $5\ \mathrm{\mu Gal}$ survey design (specification and arithmetic)

**Given.** Readout noise $\sigma_{s} = 0.4\ \mathrm{\mu Gal}$ per sample; drift
$25\ \mathrm{\mu Gal\,h^{-1}}$; the drift model has residuals of the order of a few
microgal if the settling is not removed; area $20\ \mathrm{km^{2}}$ with stations
every $\sim200\ \mathrm{m}$ gives about 200 stations.

**Term 1: readout noise.** With $n_{s}$ samples per station,
$\sigma_{\text{read}} = 0.4/\sqrt{n_{s}}$. For $n_{s} = 4$ it is
$0.20\ \mathrm{\mu Gal}$; for $n_{s} = 16$, $0.10\ \mathrm{\mu Gal}$. Reaching
$0.2\ \mathrm{\mu Gal}$ costs 4 samples per station, i.e. almost nothing in time
(seconds).

**Term 2: drift model error.** A linear drift model evaluated at time $t$ after the
last base occupation has an error set by the model's own inadequacy, not only by the
drift rate. Take the lesson's measured behaviour as a guide: with settling removed,
the residual of a good linear model is comparable with the noise per reading
($\sim0.3\ \mathrm{\mu Gal}$) *provided* the extrapolation interval is short. As a
working rule, allow the drift error to grow as
$0.05\ \mathrm{\mu Gal}$ per minute of extrapolation after a settling interval — a
SYNTHETIC rate consistent with the lesson's arithmetic (an hour of
$25\ \mathrm{\mu Gal\,h^{-1}}$ drift is $25\ \mathrm{\mu Gal}$, so a 20% model error
at one hour is $5\ \mathrm{\mu Gal}$; halving the interval quarters nothing but
halves the extrapolation).

**Loop structure.** With a 4-minute station occupation (travel plus reading) and a
target of $5\ \mathrm{\mu Gal}$ total, the drift term dominates unless the base is
re-occupied often. A **star (spider) pattern** from a central base — travel out to a
station, measure, return to base, repeat — keeps the extrapolation interval at
roughly 8 minutes, giving a drift-model error of about
$0.4\ \mathrm{\mu Gal}$, and its arithmetic is transparent. A **loop** closes the
drift model over a longer interval and is preferred when the base is far, at the
cost of a larger extrapolation error at each station.

**Dominant term.** With the star pattern: readout $0.20\ \mathrm{\mu Gal}$,
drift-model $0.4\ \mathrm{\mu Gal}$, calibration (from lesson 07-01-05, if the
meter's scale is good to $0.04\%$ over a $5\ \mathrm{mGal}$ span)
$2.0\ \mathrm{\mu Gal}$, lever-arm/tilt error (say $1\ \mathrm{\mu Gal}$),
reduction errors (elevation, from lesson 07-01-04: $0.05\ \mathrm{m}$ of height at
$0.1995\ \mathrm{mGal\,m^{-1}}$ is $1.0\ \mathrm{\mu Gal}$). Quadrature:
$\sqrt{0.20^{2}+0.4^{2}+2.0^{2}+1.0^{2}+1.0^{2}} = 2.49\ \mathrm{\mu Gal}$, so the
$5\ \mathrm{\mu Gal}$ target is met with margin — but **the calibration dominates**,
and no change of loop structure touches it.

**Falsification.** (i) Repeat a subset of 20 stations on a different day and at a
different time of day; the difference should be consistent with the quoted
$5\ \mathrm{\mu Gal}$ and should show no correlation with time-of-day (which would
indicate residual drift). (ii) Re-occupy the base at the end of a loop; a
non-zero closure inconsistent with the budget falsifies the drift model. (iii) Cross
the area along two independent traverses and compare at the crossings.

---

## ★★8 — Which instrument is limiting (specification)

**Design.** Both meters occupy the same set of stations, in the same order, on the
same day, interleaved in time. Tie both to the same absolute base at the start and
end of every loop. Record the base values at every re-occupation so each instrument's
drift is observed, not assumed.

**Analysis.**

1. **Drift estimation without assuming a functional form.** Use the sequence of base
   readings as a time series of drift and model it with a *spline* or a local
   regression rather than a straight line. The choice of smoothness is itself a
   parameter: cross-validate it (leave-one-base-occupation-out) and report the
   residual at the omitted point. A linear model is a special case; the spline
   answers the question "does the data require more than a line?" quantitatively.
2. **Comparing the instruments.** For each station form the difference
   $d_{i} = g_{A,i} - g_{B,i}$, computed from each instrument's own drift-corrected
   values. The variance of $d$ is $\sigma_{A}^{2} + \sigma_{B}^{2} - 2\rho\sigma_{A}
   \sigma_{B}$; if the two are independent ($\rho \approx 0$) it estimates the sum of
   the variances, and if one instrument is known (from repeats) to be the quieter, the
   other's scatter follows. Additionally, compare the *closure errors* of the loops
   recorded by each instrument: the instrument with the larger loop misclosure is
   limiting the survey, regardless of its nominal noise specification.
3. **Separating a station difference from an instrument difference.** Repeat each
   station twice with each instrument, in different loop positions. A station-dependent
   effect stays with the station; an instrument effect follows the instrument and
   appears also at the base.
4. **Correlated errors.** Check the difference series for correlation with time
   (residual drift), with station elevation (a reduction error), and with tilt. Any
   correlation identifies a shared or systematic effect rather than noise.

**What this cannot do.** If both instruments share a reduction error (for example the
same elevation model or the same Bouguer density), the comparison is blind to it;
only an independent data set (levelling, GNSS, a density measurement) can expose it.

---

## ★★★9 — A drift record in which the linear model fails

**SYNTHETIC constructions and their signatures.**

1. **A step.** The instrument is knocked or transported between two occupations:
   $\text{drift}(t) = \alpha t + \Delta H(t - t_{s})$, with $H$ the step function.
   Signature: a linear fit leaves residuals of one sign before $t_{s}$ and the
   opposite sign after, with a jump at $t_{s}$. The test is the *sign pattern* of the
   residuals (runs test) plus the magnitude of the jump relative to the residual
   scatter.
2. **A curvature.** A thermal cycle gives
   $\text{drift}(t) = \alpha t + \beta t^{2}$: the linear fit leaves a parabolic
   residual, correlated with $t^{2}$. The test is a regression of the residuals on
   $t^{2}$, or a comparison of nested models (line versus quadratic) by an
   $F$-test / likelihood ratio, with the number of base occupations setting the
   degrees of freedom.
3. **A temperature-correlated drift.** If the instrument's temperature record $T(t)$
   is available, regress the drift residuals on $T$; a significant slope means the
   drift is temperature-driven and can be corrected with the measured temperature
   rather than with time. The lesson's sensitivity ($3273\
   \mathrm{\mu Gal\,K^{-1}}$ for the astatic example) predicts the coefficient, so the
   regression has a *predicted* slope and the test is whether the data agree with it —
   a much stronger test than significance alone.
4. **A temperature *step* in the middle of a loop** (a cloud passing, the sun moving
   onto the instrument) is the commonest field case: it appears as a correlated
   residual at stations visited in a specific time window, and the diagnostic is a
   map of residuals against loop position.

**Test and false-alarm rate.** Use the base-occupation series (they are independent
of the station readings and cheap to collect). Fit the linear model, compute the
residual $r_{i}$ at each base occupation with its uncertainty $\sigma_{i}$, and
apply a $\chi^{2}$ goodness-of-fit test with $N - 2$ degrees of freedom. Reject the
linear model at the 5% significance level when
$\chi^{2} > \chi^{2}_{0.95}\left(N-2\right)$; this fixes the false-alarm rate at 5%
by construction, and the *power* of the test improves with more base occupations.
Report the $\chi^{2}$ value, the degrees of freedom and the largest standardised
residual, so that a reader can see whether a rejection is due to one event (a step)
or to a systematic shape (curvature). If the survey's target is
$5\ \mathrm{\mu Gal}$ and the largest standardised residual corresponds to a
$10\ \mathrm{\mu Gal}$ excursion, the correct conclusion is that the affected
stations must be re-measured, not that the model should be patched.
