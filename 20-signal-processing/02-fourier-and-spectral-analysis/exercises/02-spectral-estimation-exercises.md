# Exercises — 20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper

Attempt these before reading the
[solutions](./02-spectral-estimation-solutions.md). The lesson is
[02 Spectral Estimation](../02-spectral-estimation.md). **All models and data in
this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** State the bias and the variance of a periodogram ordinate for a Gaussian
stationary process, and explain in two sentences why the periodogram is
"inconsistent".

**★2.** A white-noise record of $\sigma = 3$ in signal units is sampled at
$f_s = 50\ \mathrm{Hz}$. Give the expected one-sided PSD level, its units, and
the level you would get if you mistakenly used the two-sided convention.

**★3.** For a periodogram of an $N = 4096$ record, how many degrees of freedom
does one interior bin have? Give the factor by which the measured level could
plausibly differ from the true level in each direction at 95 % confidence, using
the factor for $\nu = 2$ from the lesson.

## ★★ Applied

**★★4.** Derive the expected value of a windowed periodogram
$\mathrm E[\hat S(f)] = \frac{2}{f_s\sum_n w^{2}[n]}
\sum_\tau c_w[\tau]R[\tau]e^{-i\omega\tau}$ starting from
$\hat S \propto \lvert\sum_n w[n]x[n]e^{-i\omega n\Delta t}\rvert^{2}$, and show
that for white noise it reduces to $2\sigma^{2}\Delta t$ independent of the
window.

**★★5.** A study needs $\Delta f = 0.02\ \mathrm{Hz}$ and a coefficient of
variation of $0.1$ or better from a $2000\ \mathrm{s}$ record at
$f_s = 40\ \mathrm{Hz}$. Find the required segment length, the number of segments
for 0 %, 50 % and 75 % overlap, and the CV each choice achieves. State whether
the specification is achievable and which choice you would make.

**★★6.** A colleague averages $10\log_{10}$ of 32 independent periodogram
ordinates and reports the resulting noise floor. Compute the bias of that
average in dB using $\psi(K)-\ln K$, compare it with the single-ordinate
$2.5068\ \mathrm{dB}$, and state the two ways to remove the bias.

## ★★★ Research-oriented

**★★★7.** Design an estimator for a weak narrow spectral line
($0.05\ \mathrm{Hz}$ wide) in red noise whose PSD is $50$ times larger at
$0.1\ \mathrm{Hz}$ than at $1\ \mathrm{Hz}$. Choose the window, segment length,
overlap and taper count; compute the resulting resolution, degrees of freedom and
detection threshold over a $1\ \mathrm{Hz}$ search band; and state which of the
red noise's properties (slope, non-stationarity, trend) is most likely to
invalidate your threshold. Give the single diagnostic plot you would inspect
first.

**★★★8.** The measured leakage table in the lesson shows the multitaper's
far-field floor rising from $-87.3\ \mathrm{dB}$ at $K = 4$ to
$-44.0\ \mathrm{dB}$ at $K = 10$ for $\mathrm{NW} = 4$. Explain the mechanism,
predict what would happen if $NW$ were increased to $8$ with the same $K$ values,
and design a numerical experiment — inputs, statistic, expected outcome — that
would confirm or refute your prediction. State the outcome that would falsify it.
