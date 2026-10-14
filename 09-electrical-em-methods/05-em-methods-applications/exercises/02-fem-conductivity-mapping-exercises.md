# Exercises — 09-05-02 FEM Conductivity Mapping and Apparent Conductivity

Attempt these before the [solutions](./02-fem-conductivity-mapping-solutions.md).
Lesson: [02 FEM Conductivity Mapping](../02-fem-conductivity-mapping.md). All
models **SYNTHETIC**.

## ★ Foundational

**★1.** Compute $\theta = \omega\mu_0\sigma r^{2}/4$ for $r = 10$ m,
$f = 25$ kHz and $\sigma = 0.02$ S/m, and state whether the LIN calibration
applies.

**★2.** From the lesson's response table at $\sigma = 0.05$ S/m and $r = 20$ m,
state the quadrature at $100$ Hz in ppm and as a fraction of the primary.

**★3.** Explain in two sentences why a conductivity mapper uses the quadrature
rather than the in-phase channel.

## ★★ Applied

**★★4.** Using the measured LIN exponents (quadrature $\propto\theta^{0.9701}$,
in-phase $\propto\theta^{1.4723}$), estimate the ratio of the in-phase to the
quadrature at $\theta = 10^{-3}$, and state what that implies for detection.

**★★5.** Using the LIN error table ($0\%$ at $\theta = 0.01$, $-44.05\%$ at
$0.10$), estimate by interpolation the induction number at which the error
reaches $10\%$, and convert that into a maximum conductivity for $r = 20$ m and
$f = 1000$ Hz.

**★★6.** Two layered grounds give apparent conductivities of $0.0211$ and
$0.0361$ S/m. Using the measured equivalence band, state what a single-frequency
survey can and cannot conclude from those two numbers.

## ★★★ Research-oriented

**★★★7.** Design a two-separation survey to separate two members of the
equivalence family of the lesson. State the separations, the statistic, and the
assumed noise level needed for a $3\sigma$ decision.

**★★★8.** The demonstration defines the depth of exploration by scaling the top
$z$ metres by $10\%$. Propose an alternative definition, state why it might be
preferable for a layered ground, and predict qualitatively how the measured
numbers would change.
