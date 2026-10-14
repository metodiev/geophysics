# Exercises — Palaeo Sea Level Reconstruction from Marine Records

All values below come from the model of
[`../01-paleo-sea-level.md`](../01-paleo-sea-level.md) and its demo
`code/paleo_sea_level_demo.py`. **All models and data are SYNTHETIC.** Use the model
constants

$$\delta^{18}\mathrm{O}_{\text{carb}}=\delta^{18}\mathrm{O}_{\text{sw}}+0.22(15-T),
\qquad \delta^{18}\mathrm{O}_{\text{sw}}=-0.010\,SL_m,$$

$\rho_i=917$, $\rho_{\text{sw}}=1025\ \mathrm{kg\,m^{-3}}$,
$A_{\text{ocean}}=3.61\times10^{14}\ \mathrm{m^2}$.

## ★ Foundational

**1.1 — Forward model.** A sample formed at a sea level 60 m below present with a
water temperature of 11 °C. Compute $\delta^{18}\mathrm{O}_{\text{sw}}$, the
temperature term and the carbonate value. What fraction of the signal is the
temperature contribution?

**1.2 — Inversion.** A carbonate value of 2.20‰ is measured. Invert it for sea level
at assumed temperatures of 10 °C and 13 °C. By how much does the answer change per
kelvin, and does that agree with the coefficient ratio?

**1.3 — Conversions.** (a) Convert $8\times10^{15}\ \mathrm{m^3}$ of ice to an
ice-volume equivalent sea level. (b) Convert a mass rate of 1.5 mm/yr of sea level to
Gt/yr.

## ★★ Applied

**2.1 — Rate and chronology.** A 45 m rise is measured between two horizons dated at
16 ka and 8 ka, each with an uncertainty of ±0.8 ka. Compute the rate, propagate the
age uncertainty, and quote the relative error. Which measurement dominates the
error, the depth or the age?

**2.2 — Coral-terrace style reconstruction.** A terrace is dated at
$12\pm0.6$ ka and sits 22 m below the modelled present sea level, with a GIA
correction of $9\pm1.5$ m (positive, i.e. it raises the inferred sea level) and a
facies/datum uncertainty of ±2 m. (a) Compute the corrected sea-level position.
(b) Combine the uncertainties assuming independence. (c) Is a eustatic comparison
with a marine-isotope record worth 5 m meaningful?

**2.3 — Detection of a meltwater pulse.** Two records constrain the same interval: a
facies record giving $40\pm5$ m of rise, and an isotope record giving a value that
implies $18\pm8$ m. Can the two be reconciled, and what is the most likely
explanation for the difference in the model framework?

## ★★★ Research-oriented

**3.1 — The resolution ridge.** The temperature is known to 12 ± 1.5 K from a
magnesium/calcium proxy with a calibration error of $\pm1\ ^\circ\mathrm{C}$.
(a) Give the sea-level uncertainty contributed by the temperature alone.
(b) What temperature precision would be needed to resolve sea level to ±5 m?
(c) Comment on whether any stated proxy achieves this, and what that implies for
published palaeo sea-level curves.

**3.2 — Circularity of the GIA correction.** A study reconstructs sea level from
records around the margin of a former ice sheet, applying a GIA correction of order
60 m. (a) If the correction has a 10% error, what is the sea-level error?
(b) The GIA model uses a deglaciation history that was in part tuned to fit
sea-level records. Explain the circularity and propose one way to break it.

**3.3 — Designing an observation.** You are asked to constrain a 10 m sea-level
change at 15 ka. Using the uncertainties in this lesson (GIA 6 m, temperature
0.5 K otherwise unconstrained), decide whether the target is achievable with the
isotope record alone, and specify the minimum combination of independent
measurements you would require.
