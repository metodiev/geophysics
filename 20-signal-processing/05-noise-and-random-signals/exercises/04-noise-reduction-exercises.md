# Exercises — 20-05-04 Noise Reduction Strategies in Practice

Attempt these before reading the
[solutions](./04-noise-reduction-solutions.md). The lesson is
[04 Noise Reduction](../04-noise-reduction.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** Compute the stacking SNR gain in dB for $M = 64$ records, and state the
condition on the noise that makes the number valid.

**★2.** A trace has signal rms $0.20$ and noise rms $0.05$. Compute the SNR in
dB. If the signal rms is then halved with the noise unchanged, by how many dB does
the SNR fall?

**★3.** A power-line harmonic of the same phase appears in every record of a
stack. State what happens to it under averaging, and name one remedy from the
lesson.

## ★★ Applied

**★★4.** Using the filtering table of the lesson, choose a passband for a study
that requires distortion $D < 0.2$. Report the SNR achieved and the pulse width,
and state what a study needing $D<0.05$ would have to accept.

**★★5.** For a Wiener filter with signal and noise spectra in the ratio
$S_{ss}/S_{nn} = 4$ at some frequency, compute $H(f)$ and the attenuation in dB
applied to that frequency.

**★★6.** A stack of $M = 25$ records is formed with the median instead of the
mean. Compute the ratio of standard deviations of the two estimators for
Gaussian noise and hence the SNR penalty in dB, and state the benefit that pays
for it.

## ★★★ Research-oriented

**★★★7.** Design a complete noise-reduction budget for a target of $+20\ \mathrm{dB}$
SNR improvement from an input of $0\ \mathrm{dB}$, using at least two levers.
State the number of records, the filter band, the estimator, and the total
achieved improvement with its assumptions. A design that could not be executed is
a failed answer.

**★★★8.** A colleague tunes a filter by maximising the SNR on a synthetic test
record with a known signal, and it over-smooths. Explain the mechanism, and
design a protocol that would prevent it, stating the measurement that would
detect the over-smoothing.
