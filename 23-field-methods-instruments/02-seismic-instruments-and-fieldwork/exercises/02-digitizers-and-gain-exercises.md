# Exercises — 23-02-02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering

Attempt these before reading the
[solutions](./02-digitizers-and-gain-solutions.md). The lesson is
[02 Digitizers and Gain](../02-digitizers-and-gain.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A converter has a full-scale range of $\pm2.5\ \mathrm{V}$ and 18 bits.
Compute the LSB, the quantisation noise rms and the ideal SNR for a full-scale
sinusoid. State the unit of each quantity.

**★2.** A record is sampled at $f_s = 400\ \mathrm{sps}$. Compute the alias
frequency of a 250 Hz signal and of a 500 Hz signal. A wanted signal occupies
100 Hz: state the distance from each alias to the wanted signal and which one is
the more dangerous.

## ★★ Applied

**★★3.** A passband ends at 40 Hz and the sample rate is $f_s = 200\ \mathrm{sps}$.
Using the Butterworth model $|H| = 1/\sqrt{1+(f/f_c)^{2n}}$ with a corner at
40 Hz, compute the number of poles required to attenuate the 160 Hz signal by
120 dB, and state the attenuation actually achieved at that order.

**★★4.** An event has a peak amplitude of $1.2\times$ full scale.
Compute the fraction of a cycle lost to the limiter, the apparent amplitude as a
fraction of the true amplitude, and the fraction of the record's samples that
would be affected if the event were a 20-cycle wave train.

## ★★★ Research-oriented

**★★★5.** Design a recording configuration for local earthquakes: a 2–30 Hz band
of interest, expected peak ground velocities between $10^{-5}$ and
$10^{-3}\ \mathrm{m/s}$, a 24-bit converter with a $\pm10\ \mathrm{V}$ range, and a
sensor whose generator constant you must choose. Specify the sample rate, the
anti-alias corner and order, the preamplifier gain, the resulting clip velocity and
the smallest velocity the record resolves. Show the arithmetic and state which
requirement drove each choice.

**★★★6.** Design a laboratory measurement of the *effective* number of bits of a
digitizer: state the stimulus, the analysis, the metric with units, the
assumptions, the number of samples needed, and two things the test does not
measure. A specification that could not be executed is a failed answer.
