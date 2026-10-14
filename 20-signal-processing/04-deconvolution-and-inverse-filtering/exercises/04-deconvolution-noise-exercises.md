# Exercises — 20-04-04 Deconvolution in the Presence of Noise

Attempt these before reading the
[solutions](./04-deconvolution-noise-solutions.md). The lesson is
[04 Deconvolution in the Presence of Noise](../04-deconvolution-noise.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the output noise power spectrum of an inverse filter applied to
white input noise, and evaluate the gain at a frequency where $|W| = 0.01$.

**★2.** State the relation between the water level and prewhitening.

**★3.** Explain in one sentence why the naive inverse's error does not improve much
when the record SNR improves.

## ★★ Applied

**★★4.** For a wavelet with usable-band condition number 2000, state the frequency
above which the inverse filter's gain exceeds 1000, given that the gain at the top
of the band is $1/\min|W|$ and the peak gain is $1/\min|W|$ scaled by the overall
wavelet level.

**★★5.** Using the error-versus-SNR table, state the benefit of improving the
record SNR from 10 dB to 30 dB for the naive inverse and for the NSR rule, with
numbers, and explain the difference.

**★★6.** The demo reports that 100.00% of the output noise power from an
unstabilised inverse lies above 100 Hz while only 0.14% of the wavelet's energy
does. Explain why this makes prewhitening so cheap here, and state a wavelet for
which it would be expensive.

## ★★★ Research-oriented

**★★★7.** Derive the frequency-dependent optimal water level for coloured noise and
show that it reduces to a constant when the noise is white.

**★★★8.** A record has a noise-to-signal power ratio of $10^{-4}$ in the signal
band but $10^{-2}$ outside it. Design the regularisation and explain why a single
water level is the wrong tool.