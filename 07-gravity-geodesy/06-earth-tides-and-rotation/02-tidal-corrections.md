---
id: 07-06-02
title: "Tidal Corrections in Precise Measurements"
level: advanced
prereqs: ["07-06-01", "07-02-03", "07-01-04"]
tags: [gravity, geodesy, earth-tides, gravimetry, corrections]
---

# Tidal Corrections in Precise Measurements

## Learning objectives

By the end of this lesson you will be able to:

1. **Rank** the signals in a precise gravity measurement — target, tide, load,
   drift — and state which must be removed and to what accuracy.
2. **Derive** a simple field correction from $P_2$ and **measure** its error, so
   that the cost of a simple formula is a number rather than a warning.
3. **Explain** what each term of the gravity-tide factor
   $\delta = 1 + h_2 - \tfrac32k_2$ contributes and how an error in $h_2$ or $k_2$
   propagates into a corrected reading.
4. **Quantify** the effect of adding constituents to a tidal model: which
   omission costs how many microGal at which latitude.
5. **Compute** the vector sum of a body tide and an ocean load, and explain why a
   $15\%$ load changes the fitted amplitude by $13\%$ at one phase and *could*
   reduce it at another.
6. **Propagate** a tide-model error into an estimated gravimeter drift over a
   survey loop, and state why the error is systematic rather than random.
7. **State** which of the corrections in a processing sequence are measurements
   and which are models, and how each model's error should be reported.

## Prerequisites

- [01 Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) —
  the potential, the constituent frequencies and the gravity-tide factor.
- [07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../02-gravity-instruments-and-surveys/03-survey-procedures.md) —
  the drift and loop bookkeeping this lesson perturbs.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  where the tidal correction sits in the processing sequence.

> **All models and data in this module are SYNTHETIC.** The station, the load
> tide, the survey loop, the drift and the noise are teaching values. The
> ephemeris is the simplified model of lesson 01.

## 1. The hierarchy that dictates the required accuracy

A relative gravimeter reads to about $1\ \mathrm{\mu Gal}$
($10^{-8}\ \mathrm{m\,s^{-2}}$) and a microgravity survey hunts anomalies of
$10$–$100\ \mathrm{\mu Gal}$. Within the same measurement are:

| signal | size | status |
|---|---|---|
| body tide (M2, mid-latitudes) | $20$–$50\ \mathrm{\mu Gal}$ amplitude | model, from the tide potential |
| solid-Earth gravity-tide factor | $+15\%$ of the geometric tide | Earth parameters $h_2, k_2$ |
| ocean load tide | $10$–$20\%$ of the body tide (coastal) | model, from a hydrodynamic ocean tide |
| atmospheric pressure loading | $\approx-0.3\ \mathrm{\mu Gal\,hPa^{-1}}$ (rounded conventional factor) | measurement + model |
| instrument drift | $1$–$10\ \mathrm{\mu Gal\,h^{-1}}$ | estimated from loops |
| **target anomaly** | $10$–$100\ \mathrm{\mu Gal}$ | what the survey is for |

So a tide whose amplitude exceeds the target by a factor of a few must be removed
to better than $\sim1\%$ — otherwise the residual is itself a target-sized
anomaly that varies with time and station occupation. The whole lesson is about
how precisely that can be done, and with what.

## 2. A simple field correction, and what it costs

The simplest correction uses only the degree-2 lunar semidiurnal term with the
body in the equatorial plane:

$$g_{\text{tide}}^{\text{simple}}(t) = -\underbrace{\tfrac34\frac{2GM_mR}{d^{3}}
\delta}_{\text{amplitude}}\cos^{2}\varphi\,\cos\left(\omega_{M2}t\right).$$

*Worked example 1.* With the constants of [01](01-solid-earth-tides.md),
$GM_mR/d^{3} = 5.499227\times10^{-7}$, $\delta = 1.1530$, so

$$\tfrac34(2)(5.499227\times10^{-7})(1.1530) = 9.5109\times10^{-7}\
\mathrm{m\,s^{-2}} = 95.11\ \mathrm{\mu Gal},$$

and at $\varphi = 45^\circ$ the amplitude is
$95.11\cos^{2}45^\circ = 47.555\ \mathrm{\mu Gal}$.

The demonstration implements exactly this and compares it with the full model at
$(45^\circ\mathrm{N}, 7^\circ\mathrm{E})$ over 30 days:

| correction model | rms error | max error |
|---|---|---|
| M2 only, equatorial (the simple formula) | $49.890$ | $125.436$ |
| M2 only, fitted amplitude at the station | $45.738$ | $102.079$ |
| M2 + S2, fitted | $41.745$ | $90.073$ |
| M2 + S2 + K1 + O1, fitted | $5.590$ | $16.279$ |

Units are microGal. **Three conclusions that a table like this is usually not
allowed to show:**

1. The simple formula's residual ($49.9\ \mathrm{\mu Gal}$ rms,
   $125.4\ \mathrm{\mu Gal}$ maximum) is *larger than the signal it corrects*.
   A "latitude factor" correction is not a correction; it is a placeholder.
2. Fitting the M2 amplitude at the station buys only $8\%$ of the error: the
   problem is the *missing terms*, not the wrong amplitude.
3. Adding the two diurnal constituents is what changes the picture, because they
   are as large as the semidiurnal terms at mid-latitudes. This is why the
   demonstration's section 3 finds the simple model's error **largest at the
   equator** ($54.9\ \mathrm{\mu Gal}$), not smallest: the omitted declination
   modulation scales with $\cos^{2}\varphi$, while the omitted diurnal species
   vanishes there — two omissions acting in opposite directions, with the
   $\cos^{2}\varphi$ term winning.

*Worked example 2 (what accuracy the correction needs).* Suppose the survey
target is $10\ \mathrm{\mu Gal}$. Requiring the tide residual to be $10\%$ of the
target means an allowed error of $1\ \mathrm{\mu Gal}$. That is
$1/125.4 = 0.8\%$ of the simple formula's maximum error and
$1/16.3 = 6.1\%$ of the four-constituent model's maximum error. **So even a
four-constituent model is not good enough for a $10\ \mathrm{\mu Gal}$ target at
$45^\circ$N: it exceeds the entire error budget by a factor of 16.** The survey
must use a fuller constituent list — and the load and the $\delta$ factor must be
handled separately on top of that.

## 3. The corrections, term by term

The full instrument reading is modelled as

$$g_{\text{reading}}(t) = g_{\text{station}} + \delta g_{\text{tide}}(t) +
\delta g_{\text{load}}(t) + \delta g_{\text{atm}}(t) +
\text{drift}(t) + \varepsilon(t),$$

and every term on the right except the first has to be estimated. Their status:

| term | source | typical error |
|---|---|---|
| $\delta g_{\text{tide}}$ | potential + ephemeris + $\delta$ | $0.1$–$1\ \mathrm{\mu Gal}$ with a proper constituent list |
| $\delta g_{\text{load}}$ | hydrodynamic ocean-tide model + load Green's function | $10\%$–$20\%$ of a load that is itself $10\%$–$20\%$ of the tide |
| $\delta g_{\text{atm}}$ | barometric pressure at the station | $0.3\ \mathrm{\mu Gal\,hPa^{-1}}$ times the local pressure change |
| drift | loops and repeats | the subject of Section 5 |

*Worked example 3 (the gravity-tide factor).* With $h_2 = 0.6090$ and
$k_2 = 0.3040$, $\delta = 1.1530$. A $1\%$ error in $h_2$ alone means
$\Delta h_2 = 0.00609$, and since $\partial\delta/\partial h_2 = 1$,
$\Delta\delta = 0.00609 = 0.53\%$ of $\delta$. On a $42\ \mathrm{\mu Gal}$
M2 amplitude that is $0.22\ \mathrm{\mu Gal}$. **An Earth-parameter error at the
one-per-cent level is therefore a fifth of a microGal — negligible compared with
a $10\%$–$20\%$ ocean-load error**, which is the opposite of what a discussion
focused on Love numbers would suggest, and it is a numerical fact rather than an
opinion.

## 4. Body tide plus load: a vector sum

The ocean responds to the same astronomical forcing, so the load tide has
essentially **the same frequencies** as the body tide. At each constituent the
two add as vectors:

$$A_{\text{observed}} = \left|A_{\text{body}} + A_{\text{load}}
e^{-i\Delta\phi}\right| .$$

*Worked example 4.* A synthetic load with $15\%$ of the body amplitude and a
$30^\circ$ lag gives

$$\left|1 + 0.15e^{-i30^\circ}\right|
= \left|1 + 0.1299 - 0.0750i\right| = 1.1324 ,$$

so the fitted M2 amplitude grows by $13.2\%$ — and the demonstration measures
exactly that ($+5.609\ \mathrm{\mu Gal}$ on $42.369\ \mathrm{\mu Gal}$). The
phase matters as much as the amplitude: a load lagging by $180^\circ$ would
*reduce* the fitted amplitude by $15\%$. **Two stations with the same body tide
and different coastal geometry therefore have different fitted amplitudes, and
neither is more "correct" than the other.**

Because the body and load tides share frequencies, **a single station's record
cannot separate them.** The practical remedy is to remove a modally predicted
load and to quote the model's error as a systematic uncertainty; the alternative
is a network of stations with different coastal geometries, which is a research
programme rather than a processing step.

## 5. What a tide-model error does to a survey

A relative gravimeter drift is estimated by the change of reading between repeats
at the same station. If the tide is modelled rather than measured, an error in the
model enters that change *systematically*: it does not average down with more
readings in the same loop, because the error is a smooth function of time and the
loop is a short interval.

The demonstration simulates a 6-hour loop with a true drift of
$5.0\ \mathrm{\mu Gal\,h^{-1}}$ and $2.0\ \mathrm{\mu Gal}$ of reading noise:

| tide model used | fitted drift ($\mathrm{\mu Gal\,h^{-1}}$) | error |
|---|---|---|
| none | $30.674$ | $+25.674$ |
| correct, but $10\%$ too small | $7.135$ | $+2.135$ |
| correct | $4.519$ | $-0.481$ |
| $10\%$ too large | $1.904$ | $-3.096$ |

The uncorrected loop absorbs the tidal slope and returns six times the true
drift. A $10\%$ correction error still biases the drift by
$+2.6\ \mathrm{\mu Gal\,h^{-1}}$, more than half of the drift itself — and that
bias changes sign with the sign of the tide error, so it cannot be blamed on the
instrument. The residual with a correct correction ($-0.5\ \mathrm{\mu Gal\,h^{-1}}$)
is the reading noise ($2\ \mathrm{\mu Gal}$) divided by the 6-hour lever arm.

*Worked example 5 (why the bias is large).* The M2 slope of a signal of amplitude
$A$ and period $12.42\ \mathrm{h}$ is at most
$A\omega_{M2} = 42 \times 2\pi/12.42 = 21\ \mathrm{\mu Gal\,h^{-1}}$, and the
mean absolute slope over a random phase is about $0.6$ of that,
$\sim13\ \mathrm{\mu Gal\,h^{-1}}$. The measured $25.7\ \mathrm{\mu Gal\,h^{-1}}$
for the uncorrected loop is larger because the loop also contains the diurnal
species and the Sun. **A 6-hour loop cannot be drift-corrected to
$1\ \mathrm{\mu Gal\,h^{-1}}$ without a tide model good to a few per cent.**

## 6. Assumptions and regime of validity

1. **The ephemeris is adequate.** A one-arc-minute position error of the Moon
   changes the tide by well under $0.1\%$; the ephemeris is not the limitation.
2. **The Earth-response parameters are adequate.** $h_2$, $k_2$ are known to
   better than $1\%$, which is $0.2\ \mathrm{\mu Gal}$ — not the limitation.
3. **The ocean load model is the limitation.** $10\%$–$20\%$ errors in coastal
   load models are normal, and they enter the reading directly.
4. **The ocean tide is dynamic, not equilibrium.** A load model needs a
   hydrodynamic ocean tide; the body tide does not.
5. **The station does not move.** Tidal displacements change the station's height
   by up to $\sim30\ \mathrm{cm}$, which is a free-air effect of about
   $-0.3\ \mathrm{\mu Gal\,cm^{-1}}$ — i.e. of order $1$–$10\ \mathrm{\mu Gal}$
   depending on latitude and phase. For a microgravity survey this may need to be
   applied separately; for a centimetre-level study it certainly does.
6. **The atmosphere is treated separately.** A $10\ \mathrm{hPa}$ pressure change
   is $\sim3\ \mathrm{\mu Gal}$; ignoring it is a target-sized error.
7. **Tides are not only gravity.** The same potential drives tilt, strain and
   displacement, which matter for tiltmeters, strainmeters, GNSS and levelling.

## 7. Python demonstration

`code/tidal_corrections_demo.py` prints, with units:

1. **The simple field correction** — amplitude $95.11\cos^{2}\varphi\
   \mathrm{\mu Gal}$ — and its measured residual ($49.890\ \mathrm{\mu Gal}$ rms,
   $125.436\ \mathrm{\mu Gal}$ max).
2. **Four models compared**: M2-only equatorial, M2-only fitted, M2+S2, and
   M2+S2+K1+O1, with rms and maximum residuals ($5.590$ and
   $16.279\ \mathrm{\mu Gal}$ for the last).
3. **Latitude dependence**: the simple model's error peaks at the equator
   ($54.940\ \mathrm{\mu Gal}$) while the four-constituent error is smallest near
   $30^\circ$ ($4.398$).
4. **The ocean load**, as a vector sum: a $15\%$, $30^\circ$-lag load changes the
   fitted M2 amplitude by $+13.2\%$ and the K1 amplitude by
   $+1.895\ \mathrm{\mu Gal}$.
5. **The survey loop**: fitted drift with no correction, with a $10\%$ error and
   with a correct correction.

Print-only, fixed seed, no network, exits 0.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/02-tidal-corrections-exercises.md`](./exercises/02-tidal-corrections-exercises.md)
and
[`exercises/02-tidal-corrections-solutions.md`](./exercises/02-tidal-corrections-solutions.md).

- **★** Compute the simple correction amplitude at $\varphi = 60^\circ$ and state
  the ratio to a $20\ \mathrm{\mu Gal}$ target.
- **★** Compute $\delta$ for $h_2 = 0.6140$, $k_2 = 0.3020$ and the change in a
  $42\ \mathrm{\mu Gal}$ M2 amplitude.
- **★★** Given the demonstration's latitude table, decide which is the "best
  simple model" for a survey at $60^\circ$N and justify it with the numbers.
- **★★** A load of $20\%$ amplitude lags the body tide by $60^\circ$. Compute
  the change in the fitted M2 amplitude, and the phase of the resulting
  constituent.
- **★★★** Design a study that would separate the body tide, the ocean load and a
  local lateral-structure anomaly using a network of gravimeters.

## 9. Mastery checkpoint

Do this without notes:

> A microgravity survey at $45^\circ$N hunts a $10\ \mathrm{\mu Gal}$ target with
> a gravimeter reading to $1\ \mathrm{\mu Gal}$. **(a)** Compute the simple
> correction's amplitude and state the required relative accuracy of the
> correction. **(b)** State which correction model you would use and justify it
> from the demonstration's error table. **(c)** A 15% load lags the body tide by
> $30^\circ$: compute the change in the fitted M2 amplitude. **(d)** During a
> 4-hour loop the pressure falls by $8\ \mathrm{hPa}$; compute the resulting
> gravity change and compare it with the target. **(e)** State which term in your
> error budget is the largest, and what you would do about it.

*Answers.* **(a)** $95.11\cos^{2}45^\circ = 47.555\ \mathrm{\mu Gal}$; to keep
the residual below $1\ \mathrm{\mu Gal}$ the correction must be accurate to
$1/47.555 = 2.1\%$. **(b)** The four-constituent model
(M2+S2+K1+O1), whose maximum error at $45^\circ$ is
$16.279\ \mathrm{\mu Gal}$ — still *larger* than the target, so in practice one
adds further constituents (P1, K2, the elliptic terms) or uses a full
tide-prediction algorithm; the honest statement is that the four-constituent model
is not sufficient and the table shows by how much.
**(c)** $\left|1 + 0.15e^{-i30^\circ}\right| = 1.1324$, so the fitted amplitude
grows by $13.2\%$: $42.369 \to 47.978\ \mathrm{\mu Gal}$. **(d)** With the rounded
conventional barometric factor $-0.3\ \mathrm{\mu Gal\,hPa^{-1}}$, an $8\
\mathrm{hPa}$ fall is $+2.4\ \mathrm{\mu Gal}$ — $24\%$ of the target, and
comparable to the tide residual, so it must be applied or monitored.
**(e)** The ocean load, in coastal regions: remove it with the best available
model and report the model's error as a systematic uncertainty, not as part of
the random error.

## 10. Common pitfalls

1. **Using a "latitude factor" formula and assuming it corrects the tide.** The
   demonstration measures its residual as larger than the signal.
2. **Fitting M2 only.** The diurnal species is as large as the semidiurnal one
   at most latitudes.
3. **Adding amplitudes instead of vectors.** The load and the body tide have
   phases; a $15\%$ load can be $+13\%$ or $-15\%$ in the fitted amplitude.
4. **Treating a tide-model error as random.** It is a smooth function of time and
   biases drift and ties systematically.
5. **Ignoring the atmosphere.** $\sim3\ \mathrm{\mu Gal}$ per $10\ \mathrm{hPa}$
   is target-sized.
6. **Correcting the tide but not the height change.** The free-air effect of the
   tidal displacement is of order $1$–$10\ \mathrm{\mu Gal}$.
7. **Quoting a correction without its model.** "Tide corrected" is not a
   statement; "corrected with a stated constituent list and a stated load model,
   residual $\le X$" is.

## 11. Real-world applications

- **Microgravity surveys** for cavities, voids, archaeology and engineering —
  where the target is small and the tide is large.
- **Geodetic networks** — levelling and GNSS, where the tidal displacement and
  the loading displacement enter the heights.
- **Tilt and strain monitoring**, where the same potential appears as a strain
  signal with amplitudes of nstrain.
- **Volcano and reservoir monitoring**, where a tide-correction error appears as
  a spurious temporal change.

## 12. Further reading

- **Torge, W. & Müller, J., *Geodesy*** — tidal corrections and Love numbers.
- **Stacey, F. D. & Davis, P. M., *Physics of the Earth*** — Earth response,
  loading and the atmosphere.
- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the potential and the
  conventional corrections.
- **Lambeck, K., *The Earth's Variable Rotation*** — tides as an observable of
  the Earth, and the link to the next lesson.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [01 Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) —
  the theory being applied here.
- [03 Earth Rotation, Polar Motion, LOD and Excitation](03-earth-rotation.md) —
  the rotational counterpart of the same forcing.
- [07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../02-gravity-instruments-and-surveys/03-survey-procedures.md) —
  the loop bookkeeping this lesson perturbs.
- [07-03-06 Microgravity for Cavities, Tunnels and Archaeology](../03-gravity-anomalies-and-modelling/06-microgravity-applications.md) —
  the surveys whose targets are smaller than the tide.

## 14. Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md).
- [07-02 Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md).
- [07-03 Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md).
- [26-reference-library](../../26-reference-library/README.md).

## 15. Self-assessment checklist

- [ ] I can rank tide, load, atmosphere, drift and target by size.
- [ ] I can compute a simple correction and its measured error.
- [ ] I can propagate a $h_2$ error into a reading.
- [ ] I can add a body tide and a load as vectors.
- [ ] I can explain why a single station cannot separate body and load.
- [ ] I can propagate a tide error into a drift estimate.
- [ ] I can state which corrections are models and how their errors are reported.
