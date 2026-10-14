# Exercises — 20-01-01 Signal Classification: Continuous/Discrete, Deterministic/Random

Attempt these before reading the
[solutions](./01-signal-classification-solutions.md). The lesson is
[01 Signal Classification](../01-signal-classification.md).
**All models and data in this module are SYNTHETIC**, so every rate, amplitude
and record length below is a teaching choice, not a measurement.

## ★ Foundational

**★1.** Classify each of the following on all four axes (independent variable,
dependent variable, predictability, energy or power) and give the unit of the
record:

  (a) a synthetic broadband ground-velocity record sampled at $100\ \mathrm{Hz}$
  for $60\ \mathrm{s}$;
  (b) the calibration curve of a gravimeter, gravity in mGal as a function of
  dial reading;
  (c) $x(t) = 1.5\cos(2\pi\cdot 0.25\,t)\ \mathrm{m\,s^{-1}}$ for
  $-\infty < t < \infty$;
  (d) a simulated tidal water-level record in metres, sampled once an hour for
  one year.

**★2.** For $x(t) = 5.0\sin(2\pi\cdot 0.5t)\ \mathrm{m\,s^{-1}}$ averaged over
$20\ \mathrm{s}$, compute $E$, $P$, the rms and the crest factor with units.
Show the integral.

**★3.** A synthetic triangle wave has peak amplitude $4\ \mathrm{mGal}$ and a
synthetic square wave has the same peak amplitude. Compute both rms values and
the ratio of their powers. Watch the units: the peak is in mGal in both cases.

## ★★ Applied

**★★4.** Starting from
$x_e(t) = \tfrac12[x(t)+x(-t)]$ and $x_o(t) = \tfrac12[x(t)-x(-t)]$, prove that
$\int_{-T/2}^{T/2} x_e x_o\,\mathrm dt = 0$ and hence that the energies add.
Then decide whether the decomposition is well defined for a causal signal
$N$-sample record $x[0..N-1]$ (that is, whether you must extend the record).

**★★5.** A single realisation of synthetic Gaussian noise of variance
$\sigma^{2}$ is sampled with $N = 1024$ samples and gives rms
$2.40\ \mathrm{m\,s^{-1}}$. Quote the $1\sigma$ uncertainty of that rms from
$\sigma/\sqrt{2N}$, compute the relative uncertainty, and state how many samples
are needed to reach $0.5\%$ relative uncertainty. Why must you treat the value
you just inserted for $\sigma$ as provisional?

**★★6.** An analyst tests for periodicity with the *biased* autocorrelation and
declares a signal non-periodic because the value at the candidate lag is $0.90$
in a record of $N = 2000$ samples at that lag $= 200$ samples. Recompute the
expected biased value for a genuinely periodic signal of this record length and
lag, and state whether the conclusion is sound.

## ★★★ Research-oriented

**★★★7.** Design a stationarity test for a record that is expected to be
non-stationary in *frequency* but constant in amplitude (a dispersive surface-wave
train). State the statistic, the window length and its resolution limit, the null
distribution you would compare against, and what result would falsify stationarity.
A specification that could not be executed is a failed answer.

**★★★8.** The rms spread formula $\sigma/\sqrt{2N}$ assumes independent samples.
For a first-order autoregressive process $x[n] = \phi x[n-1] + \epsilon[n]$ with
$\epsilon \sim \mathcal N(0,\sigma_\epsilon^{2})$ and lag-$k$ autocorrelation
$\rho(k) = \phi^{|k|}$, the variance of the sample second moment is

$$\operatorname{Var}(s^{2}) \approx \frac{2\sigma^{4}}{N}
\sum_{k=-\infty}^{\infty} \rho^{2}(k)
= \frac{2\sigma^{4}}{N}\cdot\frac{1+\phi^{2}}{1-\phi^{2}}.$$

Derive the effective sample count $N_{\text{eff}}$ from this, evaluate the
relative uncertainty of an rms estimate for $\phi = 0.9$ and $N = 4096$, and
compare with the i.i.d. value $1/\sqrt{2N}$. State one geophysical record class
for which this correction is essential, and say which way the honest error bar
moves.
