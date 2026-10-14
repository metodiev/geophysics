# Exercises — 23-03-03 Positioning and Elevation Determination in the Field

Attempt these before reading the
[solutions](./03-positioning-in-field-solutions.md). The lesson is
[03 Positioning in the Field](../03-positioning-in-field.md). All values are
**SYNTHETIC** or derived from the stated standard formulas.

Use: free-air $0.3086\ \mathrm{mGal/m}$; Bouguer $0.0419\rho\ \mathrm{mGal/m}$;
latitude gradient $0.811\sin(2\varphi)\ \mathrm{mGal/km}$.

## ★ Foundational

**★1.** Compute the free-air, Bouguer and combined elevation gradients for
$\rho = 2.67\ \mathrm{g/cm^3}$. Then compute the elevation accuracy required for a
target anomaly accuracy of $0.02\ \mathrm{mGal}$ on the Bouguer anomaly.

**★2.** At latitude 40°, compute the normal-gravity latitude gradient and the
anomaly error produced by a 60 m north–south position error.

## ★★ Applied

**★★3.** An autonomous GNSS solution has a per-epoch random error of 6.0 m and is
averaged over 400 epochs. Compute the random error of the average. State the
residual error that remains and why averaging does not reduce it, and name the
field check that detects it.

**★★4.** A survey's GNSS heights are ellipsoidal and the geoid undulation reaches
35 m. Compute the error introduced into the Bouguer anomaly if it is ignored.
State two remedies in order of preference and the accuracy consequence of each.

## ★★★ Research-oriented

**★★★5.** Design the positioning and elevation plan for a microgravity survey
with a 0.015 mGal target over a 2 km² area: state the method, the elevation
accuracy required and how it is achieved, the north–south position requirement, the
datum handling, the field checks, and the resulting contribution to the error
budget relative to the other terms of the survey. Show the arithmetic.

**★★★6.** Specify an experiment that would establish the *actual* positioning
accuracy achieved by a survey: state the measurements, the reference, the metric
with units, the number of check points needed to demonstrate 0.05 m at 95 %
confidence, and two systematic errors the test cannot detect. A specification that
could not be executed during the survey is a failed answer.
