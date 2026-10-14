# Exercises — 11-02-01 Geophysical Signatures of Major Deposit Types

Attempt these before reading the
[solutions](./01-deposit-signatures-solutions.md). The lesson is
[01 Geophysical Signatures](../01-deposit-signatures.md). All property contrasts,
geometries and noise levels are **SYNTHETIC** teaching values.

Useful: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$\mu_0/4\pi = 10^{-7}\ \mathrm{H\,m^{-1}}$, $1\ \mathrm{mGal} = 10^{-5}\
\mathrm{m\,s^{-2}}$, $1\ \mathrm{nT} = 10^{-9}$ T.

## ★ Foundational

**★1.** Using the formulas of the lesson, compute the gravity anomaly of a sphere
of radius $150\ \mathrm{m}$ at $z = 300\ \mathrm{m}$ for
$\Delta\rho = 250\ \mathrm{kg\,m^{-3}}$, and state its unit.

**★2.** For the same body with $\kappa = 0.02$ SI in $B_0 = 50\
\mathrm{\mu T}$, compute the axial magnetic anomaly in nT.

**★3.** The host has $K = 2.0\%$, $eU = 2.0$ ppm, $eTh = 10.0$ ppm. Compute the
three radioelement contrasts in per cent for a body with $K = 1.0\%$,
$eU = 1.5$ ppm, $eTh = 4.0$ ppm.

**★4.** State, in one sentence each, why (a) the EM index spans four orders of
magnitude across the class table while gravity spans one, and (b) a radioelement
contrast is reported as a percentage rather than in physical units.

## ★★ Applied

**★★5.** For the body of ★1–★3, form the six-component signature vector, normalise
it to unit length, and compute the cosine against the VMS and graphite-schist rows
of the lesson table. State which class it most resembles.

**★★6.** Two classes have unit signature vectors with cosine $0.9994$. Using the
known-amplitude error formula with $\|\mathbf{s}_i - \mathbf{s}_j\| = 0.0354
\|\mathbf{s}_i\|$ and purely magnetic discrimination ($\sigma = 0.2$ nT on a
$1458\ \mathrm{nT}$ signature), compute $P_{\text{err}}$. Then recompute it for a
body $10$ times weaker (all amplitudes divided by 10) and for the
direction-only (unknown-amplitude) case, and state the practical conclusion.

**★★7.** In the lesson's worked example the magnetic channel separates VMS from a
Ni–Cu body at $520\sigma$. Suppose the depth were unknown and could be anywhere
between $250$ and $500\ \mathrm{m}$ while the radius stayed $150\ \mathrm{m}$.
Compute the range of expected magnetic anomalies for both classes over that depth
range, and state whether the discrimination survives.

**★★8.** Show that the normalised signature matrix has a large condition number by
computing the singular values yourself for the reduced $4\times4$ matrix formed by
the gravity, magnetics, EM and K columns of the first four classes of the table.
State which direction is the weakest.

## ★★★ Research-oriented

**★★★9.** The lesson shows that the EM channel contributes almost no
class-discriminating *direction* after row normalisation. Construct a weighting
scheme that fixes this (for example weighting each channel by the inverse of its
typical noise, or by a geologist's prior) and recompute the singular values and the
condition number. State precisely what you have assumed by choosing the weights,
and why any such choice is a statement about the classes, not about the physics.

**★★★10.** Design a synthetic benchmark for class identification that does not
assume the class list is complete: generate a held-out class not present in the
training table, define the decision rule, and specify the metric you would report
(a confusion matrix alone cannot express "none of the above"). Give the numerical
procedure and the expected failure mode.

**★★★11.** Remanent magnetisation can reverse the sign of a magnetic anomaly while
leaving its magnitude unchanged. Under the direction-only decision rule of the
lesson, compute how the cosine between two formerly similar classes changes when
one of them becomes strongly remanent with reversed polarity, and state the
consequence for prospecting in a terrain with known remanent magnetisation.
