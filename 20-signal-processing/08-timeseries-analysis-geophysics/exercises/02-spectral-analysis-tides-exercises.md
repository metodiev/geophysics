# Exercises — 20-08-02 Tidal Harmonic Analysis and Prediction

Attempt these before reading the
[solutions](./02-spectral-analysis-tides-solutions.md). The lesson is
[02 Tidal Harmonic Analysis and Prediction](../02-spectral-analysis-tides.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the harmonic tide model. State which quantities are known before
the analysis and which are estimated, and how many parameters a five-constituent
fit has.

**★2.** Using $\lvert\sigma_1 - \sigma_2\rvert$ from the lesson tables, compute
the Rayleigh separation time in hours and days for (a) M2–S2 and (b) K1–O1.

**★3.** A tide gauge records every 6 hours. Compute the sampling frequency and
Nyquist in degrees per hour, and state whether M2 (28.9841 °/h) is aliased and
why.

## ★★ Applied

**★★4.** From the Rayleigh table, a 10-day hourly record gives a standard
deviation of 0.00425 m for the M2 amplitude and a 60-day record gives 0.00098 m,
with the same 0.03 m of noise. Compute the ratio and the corresponding condition
numbers, and state what you would report to justify using a 30-day record.

**★★5.** A colleague fits M2, S2 and the mean to a **daily** record and reports
$A_{M2} = 1.20$ m, $A_{S2} = 0.079$ m, mean $= 2.4$ m. Using the alias table,
explain what has happened to S2 and what the reported 0.079 m actually is.

**★★6.** Using the prediction table, state the fit residual and the prediction rms
at 7 days and at 60 days, and explain why the two statistics rank the records
differently.

## ★★★ Research-oriented

**★★★7.** Design a tidal analysis for a gauge that samples hourly but whose
record has a 3-month gap in its middle. Specify how you would handle the gap in
the design matrix, the constituents you would be able to separate, the ones you
would drop, and the diagnostic you would use to detect that a dropped
constituent has leaked into the retained ones.

**★★★8.** The lesson's §5 shows prediction error falling from 0.0195 m at 7 days
to 0.0025 m at 60 days for a *noise-free* truth. Redesign the measurement so that
the prediction is validated against a noisy held-out record, and state how that
changes the interpretation of the error floor.
