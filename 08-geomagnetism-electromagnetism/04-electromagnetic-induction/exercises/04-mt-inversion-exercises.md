# Exercises — 08-04-04 MT Inversion: 1-D, 2-D and 3-D Approaches

Attempt these before reading the
[solutions](./04-mt-inversion-solutions.md). The lesson is
[04 MT Inversion](../04-mt-inversion.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the conductance of a $20\ \Omega$m layer 4 km thick. State the
unit.

**★2.** From the trade-off table, at $\mu = 10^{-1}$ the rms misfit is 0.15181 and
the model roughness 0.3383; at $\mu = 10^{-3}$ they are 0.06268 and 1.0396. Compute
the changes in misfit and roughness and state what was bought and what was paid.

**★3.** A static shift of $s = 2$ multiplies the impedance. Compute the change in
$\rho_a$ and in the phase.

## ★★ Applied

**★★4.** The Occam criterion used in the lesson is "the smoothest model whose
misfit is within 10% of the best achieved". The best misfit is 0.06087 and
$\mu = 10^{-2}$ gives 0.07689. Decide whether $\mu = 10^{-2}$ is admitted by the
criterion, and compute the threshold explicitly.

**★★5.** Three models with the same conductance of 100 S fit the data with rms
misfits of 0.06176, 0.08415 and 0.11518, against a noise level of 0.05885.
Compute each misfit as a multiple of the noise and state whether the data can
discriminate the models.

**★★6.** A colleague inverts $\rho_a$ alone, ignoring the phase, and reports a
model with a top layer of $600\ \Omega$m. Using the static-shift arithmetic of
★3, state the factor by which the reported resistivity could be wrong and why the
inclusion of phase would prevent it.

## ★★★ Research-oriented

**★★★7.** Design an experiment to determine the minimum layer thickness that a
given period band can resolve for a conductor of $10\ \Omega$m at 2 km depth.
State the period band, the metric (a misfit difference between a thin and a thick
model), and the noise level at which the discrimination fails.

**★★★8.** Write the section of an MT interpretation report entitled "What the
data constrain", using only quantities that the lesson shows to be robust.
Include one statement about the conductance, one about the depth range, and one
about what is not resolved.
