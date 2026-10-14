# Exercises — 20-02-05 Time-Frequency Analysis: STFT, Wavelets, Spectrograms

Attempt these before reading the
[solutions](./05-time-frequency-solutions.md). The lesson is
[05 Time-Frequency Analysis](../05-time-frequency.md). **All models and data in
this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** Write the STFT definition and the spectrogram, and state in one sentence
what the time axis and the frequency axis each represent.

**★2.** State the time-bandwidth uncertainty relation in both the
$\sigma_t\sigma_\omega$ and the $\sigma_t\sigma_f$ forms, give the numerical value
of the constant in the second form, and name the window that attains it.

**★3.** A spectrogram is computed with a 512-sample Hann window at
$f_s = 2000\ \mathrm{Hz}$. Give (a) $\Delta f$, (b) the measured $-3\ \mathrm{dB}$
two-tone resolution in hertz, and (c) the energy-RMS time width $\sigma_t$ in
milliseconds.

## ★★ Applied

**★★4.** Two components are $4\ \mathrm{Hz}$ apart at $f_s = 1000\ \mathrm{Hz}$.
Using the measured resolution rule of the lesson, give the minimum segment length
that separates them at the $-3\ \mathrm{dB}$ criterion. Then state what happens to
the time localisation of a transient under that choice, with the number.

**★★5.** A ridge is fitted between $t = 1.0\ \mathrm{s}$ and $t = 1.4\ \mathrm{s}$
with a 256-sample window at $f_s = 1000\ \mathrm{Hz}$, giving a slope of
$20\ \mathrm{Hz\,s^{-1}}$. Compute the uncertainty on the slope from the two-endpoint
argument and state two ways to reduce it, with the factor each buys.

**★★6.** A colleague sums a spectrogram over time and calls the result "the power
spectrum". Explain what they have actually computed, using the marginal
relationships of the lesson, and state the bias: for a 256-sample Hann segment at
$f_s = 1000\ \mathrm{Hz}$, compare the effective resolution of the marginal with
that of the full-record spectrum when the record is 8192 samples long.

## ★★★ Research-oriented

**★★★7.** Design a time-frequency analysis for a synthetic dispersive surface-wave
train at $0.3$–$3\ \mathrm{Hz}$, sampled at $20\ \mathrm{Hz}$, where the group
velocity must be measured to $2\%$ and the arrival time to $50\ \mathrm{ms}$.
Specify the window shape and length, the time and frequency resolutions, whether a
single-window STFT can meet both requirements, and — if it cannot — the
multi-resolution (constant-Q) alternative with the scale factor that would.
Quantify the impossibility or the design with the lesson's measured constants.

**★★★8.** The measured Gaussian time-bandwidth product is exactly $1/(4\pi)$ and
the Hann window's is $1.0262$ times that. Design a numerical experiment that would
detect a window whose product is $5\%$ above the bound, stating the statistic, the
precision required on each width, and the discretisation effects that could
masquerade as a $5\%$ excess (with the magnitudes you would expect). Then state
which of your controls would fail if the window were poorly sampled (few samples
per standard deviation).
