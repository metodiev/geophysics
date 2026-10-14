# Exercises — 20-02-06 Wavelet Transforms and Multiresolution Analysis

Attempt these before reading the
[solutions](./06-wavelet-analysis-solutions.md). The lesson is
[06 Wavelet Transforms and Multiresolution Analysis](../06-wavelet-analysis.md).
**All models and data in this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** State the four orthonormality conditions for a two-channel filter bank and
say which of them fails if you forget the $1/\sqrt2$ normalisation of $h$.

**★2.** Write the Daubechies-4 lowpass coefficients from their exact algebraic
form and compute $\sum_n h[n]$ and $\sum_n h^{2}[n]$ from your expression, by hand.

**★3.** A $500\ \mathrm{Hz}$-sampled record is decomposed with db4 to $J = 4$
levels. Give the band edges of $d_1, d_2, d_3, d_4$ and $a_4$ in hertz.

## ★★ Applied

**★★4.** Using the measured relation $f = \omega_0/(2\pi a\Delta t)$ with
$\omega_0 = 6$, find the scale of maximum response at $f_s = 100\ \mathrm{Hz}$ for
the frequencies 1, 5 and 25 Hz. Then state the measurement uncertainty on each
frequency, using the measured $Q \approx 3.7$, and say which of the three you could
separate from a neighbour 0.2 Hz away.

**★★5.** With the measured $\sigma_t\times f = 0.6752$, compute the number of
samples the analysing wavelet spans at 2 Hz and at 20 Hz for $f_s = 100\
\mathrm{Hz}$, and state why the answer is the same number of *cycles* in both
cases. Then explain, in terms of that number, why the transform cannot resolve two
frequencies 0.01 Hz apart at 0.05 Hz no matter how long the record is.

**★★6.** A three-level db4 decomposition of a synthetic record gives detail
energies 4.0, 25.0 and 100.0 in $d_1$, $d_2$, $d_3$ and an approximation energy of
871.0. Compute the band edges at $f_s = 200\ \mathrm{Hz}$, the fraction of the
total energy in each band, and the slope of the energy spectrum in dB per octave
between adjacent detail bands. State what the slope implies and one reason it
could be misleading.

## ★★★ Research-oriented

**★★★7.** Design a multiresolution denoising scheme for a synthetic record
containing (i) a $0.5\ \mathrm{Hz}$ sinusoid of amplitude 2, (ii) a $4\
\mathrm{Hz}$ dispersive arrival of amplitude 0.5, and (iii) Gaussian noise of
$\sigma = 1$, at $f_s = 100\ \mathrm{Hz}$ and $N = 16384$ samples. Specify the
transform, the number of levels, the threshold rule and its estimator, and the
expected SNR improvement *per band*. State which feature your scheme risks
destroying, and give the diagnostic you would compute to check that it has not.
Use the lesson's measured denoising results for calibration.

**★★★8.** Your implementation of the periodic DWT reconstructs a test signal with
a maximum error of $3\times10^{-3}$ — small, but five orders of magnitude larger
than the $1.3\times10^{-15}$ the lesson reports. Design a diagnostic procedure
that distinguishes (a) a wrong filter (one coefficient mistyped), (b) a wrong
synthesis alignment, (c) a boundary/buffer-length error, and (d) accumulated
rounding in single precision. Give the specific test and the expected signature of
each, and state which one would be *invisible* in the energy-partition test.
