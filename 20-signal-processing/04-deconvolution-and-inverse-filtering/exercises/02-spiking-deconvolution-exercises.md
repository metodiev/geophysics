# Exercises — 20-04-02 Spiking (Predictive) Deconvolution and Wavelet Estimation

Attempt these before reading the
[solutions](./02-spiking-deconvolution-solutions.md). The lesson is
[02 Spiking Deconvolution](../02-spiking-deconvolution.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the order-2 Yule-Walker equations for a process with autocorrelation
$r[0], r[1], r[2]$ and solve them symbolically.

**★2.** Define the kurtosis of a sequence and state its value for a Gaussian.

**★3.** State what the prediction gap $\alpha$ in predictive deconvolution means
physically and what it should be set to.

## ★★ Applied

**★★4.** Using the lesson's kurtosis table, choose an operator length for a
wavelet known to be 30 samples long, and state the expected kurtosis and
correlation.

**★★5.** Explain why a zero-phase wavelet cannot be spiked by a causal operator,
using the symmetry of its inverse.

**★★6.** The demo's autocorrelation at one period falls from 0.4613 to 0.0436 when
the gap equals the period, and stays near 0.39 for the wrong gaps. Compute the
suppression factor for each case and state the design conclusion.

## ★★★ Research-oriented

**★★★7.** Derive the minimum-phase spectral factorisation: given a power spectrum
$S(\omega)$, show that $S = |W_{\min}|^2$ for a unique causal, minimum-phase $W_{\min}$,
and state why this is what makes spiking deconvolution well defined.

**★★★8.** A reverberation period varies by $\pm10\%$ across a survey. Design a
predictive deconvolution robust to this, and state two ways to make it robust with
the cost of each.