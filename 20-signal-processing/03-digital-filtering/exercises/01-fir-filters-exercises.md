# Exercises — 20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares

Attempt these before reading the
[solutions](./01-fir-filters-solutions.md). The lesson is
[01 FIR Filter Design](../01-fir-filters.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** For $f_s = 250$ Hz and $f_c = 50$ Hz, write the ideal lowpass impulse
response $h_d[n]$ and evaluate $h_d[0], h_d[1], h_d[2], h_d[3], h_d[4]$.

**★2.** State the condition on the coefficients of an $N$-tap FIR filter that
makes its phase exactly linear, and give the resulting group delay in samples.

**★3.** Explain in two sentences why truncating the ideal lowpass impulse response
leaves ripples that do not disappear as the number of taps grows.

## ★★ Applied

**★★4.** A 121-tap lowpass is windowed with Hamming and with Blackman at the same
cutoff. Using the demo's measured table, state which window gives at least 60 dB
of stopband attenuation and by how much the transition edge differs between them.

**★★5.** Design a lowpass for $f_s = 200$ Hz, passband to 20 Hz, stopband from
35 Hz, requiring 55 dB. Estimate the Kaiser order and $\beta$, then state the
group delay in samples and in milliseconds for the odd order nearest your
estimate.

**★★6.** At the same order, the demo measures 60.44 dB (Kaiser window) and
79.22 dB (Parks-McClellan). Explain the 18.78 dB difference in terms of the error
norm each method minimises.

## ★★★ Research-oriented

**★★★7.** Take a 61-tap symmetric Hamming lowpass and perturb one coefficient
(the 20th) by 1%. Measure or bound the resulting group-delay variation in the
passband, and state what this says about the sensitivity of linear phase to
coefficient errors.

**★★★8.** The demo's Kaiser order estimate for the 40/60 Hz specification is 47
taps, and the measured attenuation is 60.44 dB. Construct a specification for
which the *estimate* is off by more than 5 dB, explain analytically why the
estimate fails there, and verify numerically.