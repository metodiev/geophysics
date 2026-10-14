# Exercises — 20-02-04 Cross-Spectra, Coherence and Phase Estimation

Attempt these before reading the
[solutions](./04-cross-spectra-coherence-solutions.md). The lesson is
[04 Cross-Spectra, Coherence and Phase Estimation](../04-cross-spectra-coherence.md).
**All models and data in this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** Write the magnitude-squared coherence in terms of the auto- and
cross-spectra. State its range and its units.

**★2.** A synthetic two-channel test has true coherence $0.64$ at $2\ \mathrm{Hz}$.
Convert it to an output signal-to-noise ratio in dB. Then state what the coherence
would be if the output SNR were 20 dB.

**★3.** A cross-spectrum phase has a fitted slope of $-0.19\ \mathrm{rad}$ per
rad/sample. Give the delay in samples and in seconds at $f_s = 100\ \mathrm{Hz}$,
and state which convention (which argument of `scipy.signal.csd`) the sign
implies.

## ★★ Applied

**★★4.** A coherence of $0.7$ is measured with $K = 16$ independent averages.
Compute (a) the bias term from $\gamma^{2}+(1-\gamma^{2})^{2}/K$, (b) the
bias-corrected value, and (c) the significance threshold at $\alpha = 0.05$.
State whether the detection survives the correction.

**★★5.** A transfer function is estimated with $K = 25$ averages. Compute the
predicted relative error of $\lvert\hat H\rvert$ at coherences 0.95, 0.8, 0.5 and
0.2, and state the coherence below which you would refuse to report $H$ if the
requirement is $10\%$ accuracy.

**★★6.** A search covers 100 independent frequency bins for evidence of a
coherent relationship, at a nominal $\alpha = 0.05$ per bin. Compute the
family-wise false-alarm probability using the measured single-bin threshold (a)
naively and (b) with a Bonferroni correction. Then give the threshold
$1-\alpha^{1/(K-1)}$ for $K = 50$ in both cases and explain why the lesson's
measured "maximum of 31 bins" column was 1.00 at $K=7$.

## ★★★ Research-oriented

**★★★7.** Design an experiment to measure a frequency-dependent time delay
between two synthetic channels with a target uncertainty of $0.02$ samples at
$5\ \mathrm{Hz}$, using the scaling measured in the lesson. Specify: the band, the
segment length, the number of segments, the expected coherence needed, the delay
estimator and its weighting, and the number of independent realisations required.
State where your design is limited by bias rather than variance, and give the one
measurement that would reveal a systematic (rather than random) delay error.

**★★★8.** A colleague reports a coherence of $0.45$ between two channels at
$0.02\ \mathrm{Hz}$, computed as a single cross-spectrum (no averaging) over a
50-second record. Identify *three* independent problems with the claim, compute
the numbers that expose each, and state the minimal analysis that would make the
claim defensible. Use the lesson's results, not new assumptions.
