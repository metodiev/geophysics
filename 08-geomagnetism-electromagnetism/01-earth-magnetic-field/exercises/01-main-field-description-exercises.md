# Exercises — 08-01-01 Describing the Main Field: Declination, Inclination, Intensity

Attempt these before reading the
[solutions](./01-main-field-description-solutions.md). The lesson is
[01 Describing the Main Field](../01-main-field-description.md). All models are
**SYNTHETIC** teaching values.

Use $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ and
$1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$ exactly.

## ★ Foundational

**★1.** A site has $X = 21000\ \mathrm{nT}$, $Y = -4200\ \mathrm{nT}$,
$Z = 38500\ \mathrm{nT}$. Compute $H$, $F$, $D$ (east-positive) and $I$
(down-positive), showing each step. State which hemisphere the site is in.

**★2.** A site has $F = 48000\ \mathrm{nT}$. Express it in tesla, in
microtesla, in gammas, and as the equivalent magnetising field $B/\mu_0$ in
$\mathrm{A\,m^{-1}}$.

**★3.** State the unit of each of $X$, $Y$, $Z$, $H$, $F$, $D$, $I$ and verify
by dimensional analysis that the expression $H^2+Z^2$ has the same unit as
$F^2$.

## ★★ Applied

**★★4.** At site A of the lesson ($H = 20056.171\ \mathrm{nT}$,
$F = 46542.991\ \mathrm{nT}$) an instrument error contributes
$\mathrm{d}Y = 5\ \mathrm{nT}$. Estimate $\mathrm{d}D$ with the linearisation and
with the exact four-quadrant formula, and give the difference in arcminutes.
Repeat for a synthetic near-pole site with $H = 471.699\ \mathrm{nT}$ and comment
on where the linearisation is acceptable.

**★★5.** A three-axis sensor is mounted so that its $X$ axis is rotated by an
angle $\varepsilon$ clockwise (as seen from above) from geographic north. That
is, the reported components are $X' = X\cos\varepsilon + Y\sin\varepsilon$ and
$Y' = -X\sin\varepsilon + Y\cos\varepsilon$. Show that the reported declination
is $D' = D - \varepsilon$ and compute the error for $\varepsilon = 0.2^{\circ}$.

**★★6.** At a synthetic site with $H = 471.699\ \mathrm{nT}$, how large a
component error $\mathrm{d}Y$ can be tolerated if declination is to be quoted to
$1^{\circ}$? Compare with the same number at $H = 20056.171\ \mathrm{nT}$ and
state the practical conclusion in one sentence.

## ★★★ Research-oriented

**★★★7.** A total-field magnetometer is the only instrument available, and the
task is to determine $I$ at a site. Design a measurement and an analysis that
extracts $I$ from several total-field readings taken at different known
orientations of a coil that adds a known bias field. State the algebra, the
number of readings, and the one assumption that could invalidate the result.
A specification that could not be executed is a failed answer.

**★★★8.** Treating $(H,D,I)$ as spherical coordinates in the frame of section 1,
show analytically that the volume element is $\mathrm{d}V = H^2\cos I\,
\mathrm{d}H\,\mathrm{d}D\,\mathrm{d}I$. Then say what has to change about the
statement if $I$ is measured downward from the horizontal rather than as a
colatitude -- and why the cosine appears at all.
