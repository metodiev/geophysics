# Exercises — 06-11-06 Hazard Maps, Site Amplification and Design Codes

Attempt these before reading the
[solutions](./06-hazard-mapping-solutions.md). The lesson is
[06 Hazard Mapping](../06-hazard-mapping.md). All models and data in this module
are **SYNTHETIC**.

## ★ Foundational

**★1.** A soil layer has $\beta_1 = 180\ \mathrm{m\,s^{-1}}$,
$\rho_1 = 1.7\ \mathrm{g\,cm^{-3}}$, $H = 25$ m over a half-space with
$\beta_2 = 900\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2.5\ \mathrm{g\,cm^{-3}}$. Compute
the impedance ratio, the fundamental resonance frequency, and the lossless peak
amplification.

**★2.** From the demonstration's damping table ($A(f_0) = 5.333, 5.119, 4.408,
3.755, 2.893$ for $Q = \infty, 100, 20, 10, 5$), interpolate the expected peak for
$Q = 15$ and state the trend in one sentence.

**★3.** With the synthetic bedrock curve
$\lambda = 0.002(z/0.1)^{-2.5}\ \mathrm{yr^{-1}}$ and a site factor $F = 1.5$,
compute the surface rate of exceeding $0.2\ \mathrm{g}$ and the corresponding
return period.

## ★★ Applied

**★★4.** With the nonlinearity $F(z_s) = 1 + (F_\text{lin}-1)/[1+(z_s/0.30)^2]$ and
$F_\text{lin} = 1.7989$, compute the amplification and the implied bedrock PGA for a
surface PGA of $0.30\ \mathrm{g}$. State whether the nonlinear factor is above or
below the linear one and why.

**★★5.** The demonstration reports band-averaged factors of 2.1254 (0.5–2 Hz) and
1.7989 (0.5–10 Hz) for the same site. Explain the difference using the location of
the fundamental resonance, and state which band a structure with a 1 s period cares
about.

**★★6.** Four boreholes at $x = 0, 4, 9, 15$ km report
$V_{S30} = 420, 260, 620, 330\ \mathrm{m\,s^{-1}}$. Compute the linear
interpolation to $x = 6.5$ km and the corresponding amplification from
$A = (760/V_{S30})^{0.5}$; compare with the nearest-borehole and
inverse-distance answers (260 and 425.1 m/s) and state which rule you would report.

## ★★★ Research-oriented

**★★★7.** Design a field programme that measures a site's SH transfer function
empirically and validates the 1D model, using ambient noise and earthquake records.
State the observable, the estimator, the frequency band where it must work, the
validation metric, and one systematic effect that will corrupt the estimate if it
is ignored.

**★★★8.** Design a study that decomposes the epistemic spread of a hazard-map
pixel into (i) the interpolation rule, (ii) the $V_{S30}$-to-amplification
relation, (iii) the GMPE choice and (iv) the source-model rate. State the
experimental design, the score, and how you would report the result so that a map
user can act on it.
