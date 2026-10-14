# Exercises — 06-05-02 Separating Scattering from Intrinsic Attenuation

Attempt these before reading the
[solutions](./02-scattering-vs-intrinsic-solutions.md). The lesson is
[02 Separating Scattering from Intrinsic Attenuation](../02-scattering-vs-intrinsic.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A medium has $v = 3000\ \mathrm{m\,s^{-1}}$ and a Gaussian correlation
length $a = 500\ \mathrm{m}$. Compute the crossover frequency $f_c$ and the
product $ka$ at $0.1\ \mathrm{Hz}$, $1\ \mathrm{Hz}$ and $10\ \mathrm{Hz}$.
Classify each frequency as Rayleigh, geometric, or transitional.

**★2.** A $10\ \mathrm{km}$ path in a medium with $v = 3500\ \mathrm{m\,s^{-1}}$
yields a fitted slope of $-\ln A$ against $f$ of $m = 0.05\ \mathrm{Hz^{-1}}$.
Compute $Q_{\text{app}}$, and compute $\alpha$ at $5\ \mathrm{Hz}$ with units.
Show the unit cancellation explicitly.

**★3.** A measurement gives $1/Q_{\text{meas}} = 0.020$ and an independent
estimate of the scattering contribution gives $1/Q_{\text{scat}} = 0.005$.
Compute $Q_{\text{int}}$ and $Q_{\text{app}}$. Which of the two is
$Q_{\text{meas}}$? State which inequality must always hold, and what a small
measured $Q$ does and does not prove.

## ★★ Applied

**★★4.** Derive
$1/Q_{\text{app}} = 1/Q_{\text{int}} + 1/Q_{\text{scat}}$ from the decay laws,
stating the assumption. Then use the demonstration's values
($1/Q_{\text{scat}} = 7.7476\times10^{-3}$, $Q_{\text{int}} = 100$) to check the
rule numerically: compare $1/Q_{\text{int}} + 1/Q_{\text{scat}}$ with the measured
$1/Q_{\text{meas}} = 0.018167$ and report the discrepancy as a percentage, in the
same sense as the demonstration's table ($+2.36\%$).

**★★5.** A two-band analysis of the same structure gives
$Q = 240 \pm 9$ over $[2, 6]\ \mathrm{Hz}$ and $Q = 120 \pm 8$ over
$[6, 22]\ \mathrm{Hz}$. **(a)** Compute the ratio and its standard error (treat
the two errors as independent and propagate). **(b)** Is the ratio significantly
different from 1? **(c)** Which mechanism does the sign of the effect favour, and
what would a purely intrinsic attenuator have produced? **(d)** Give one
alternative explanation that this test cannot exclude.

**★★6.** The demonstration's six sub-ensembles of about 667 realisations give
$1/Q_{\text{app}} = 7.751223\times10^{-3} \pm 4.670219\times10^{-4}$. Compute the
relative standard error, then compute how many realisations would be needed for a
$1\%$ and for a $2\%$ measurement of $1/Q_{\text{app}}$. Comment on whether such
a measurement is available in practice for a *real* structure.

## ★★★ Research-oriented

**★★★7.** You are asked to decide whether a low-$Q$ anomaly in a crustal volume
is intrinsic or scattering-dominated, with access to a dense local array
(30 stations within $20\ \mathrm{km}$), regional earthquakes, and ambient noise.
Design the study: name three independent discriminators from the lesson, give the
band and metric for each, state the expected signature of each mechanism, and
state explicitly what result would count as *evidence for* intrinsic attenuation
and what would count as *failure to separate* the two.

**★★★8.** Show that a single-band spectral-ratio measurement cannot distinguish
the two mechanisms by constructing two media with the *same* $Q_{\text{app}} =
150$ over $[2, 8]\ \mathrm{Hz}$: one purely intrinsic, one purely scattering
(with $Q_{\text{int}} = \infty$). Then explain why the two are distinguishable if
the analysis is extended to $[0.5, 30]\ \mathrm{Hz}$, and give the frequency
dependence you expect in each case in the two limits $ka \ll 1$ and
$ka \gg 1$.
