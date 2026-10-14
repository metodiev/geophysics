# Exercises — 25-02-03 Project: Fourier Analysis of a Geophysical Signal

Attempt these before reading the
[solutions](./03-fourier-analysis-signals-solutions.md). The project is
[03 Fourier Analysis](../03-fourier-analysis-signals.md). Values printed by
[`code/fourier_analysis_signals_demo.py`](../code/fourier_analysis_signals_demo.py):

| Quantity | Demonstration value |
|---|---|
| sampling / length | $f_s = 1.0\ \mathrm{Hz}$, $N = 1024$, 1024 s |
| resolution | $\Delta f = 0.000977\ \mathrm{Hz}$ (1024 s) |
| components | $0.050\ \mathrm{Hz}$ (A = 1.00), $0.110\ \mathrm{Hz}$ (A = 0.50) |
| noise | $\sigma = 0.30$ signal unit |
| peak 1 frequency / PSD | $0.0498\ \mathrm{Hz}$ / $331.1041\ \text{unit}^{2}\,\mathrm{Hz^{-1}}$ |
| peak 1 amplitude | peak bin $0.8042$, lobe sum $1.0178$ |
| peak 2 frequency / PSD | $0.1104\ \mathrm{Hz}$ / $79.6003\ \text{unit}^{2}\,\mathrm{Hz^{-1}}$ |
| peak 2 amplitude | peak bin $0.3943$, lobe sum $0.5265$ |
| Parseval ratio | $1.0213$ (time $0.729328$, spectral $0.744887$) |
| leakage | rectangular $-9.6\ \mathrm{dB}$, Hann $-30.9\ \mathrm{dB}$ |
| 95th-percentile null | $1.6216\ \text{unit}^{2}\,\mathrm{Hz^{-1}}$ |
| second peak above threshold | $49.1\times$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** A record is sampled at $1.0\ \mathrm{Hz}$ for $N = 4096$ samples. State
the duration, the resolution $\Delta f$, the Nyquist frequency, the shortest
representable period and the longest resolvable period.

**★2.** State the unit of the demonstration's PSD in terms of the signal unit, and
explain why the PSD integrates to a variance rather than to an amplitude squared.

**★3.** Verify the demonstration's peak-bin amplitude for component 1: compute
$\sqrt{2\,\widehat{S}\,\Delta f}$ with $\widehat{S} = 331.1041\
\text{unit}^{2}\,\mathrm{Hz^{-1}}$ and $\Delta f = 0.000977\ \mathrm{Hz}$, and
state the percentage shortfall against the true $1.00$.

## ★★ Applied

**★★4.** The five-bin lobe sum gives an amplitude of $1.0178$. Invert
$A = \sqrt{2\,\Delta f \sum_{\text{lobe}}\widehat{S}}$ to obtain the lobe's summed
PSD, and state the ratio of that sum to the single peak bin's PSD. Explain why the
ratio is not 1.

**★★5.** Convert the two leakage figures to power ratios and to linear amplitude
ratios, and state the suppression factor. Then compute each window's main-lobe
width in Hz and state the resolution cost of the Hann window.

**★★6.** The white noise has $\sigma = 0.30$ signal unit, so its one-sided PSD
level is approximately $2\sigma^{2}/f_s$. Compute that level, form the ratio of
the measured 95th-percentile threshold $1.6216$ to it, and compare with the
prediction for the maximum of $n = 512$ independent exponential variables at the
95th percentile, $t/m = -\ln\!\left(1-0.95^{1/n}\right)$.

## ★★★ Research-oriented

**★★★7.** Design a detection procedure for a periodic signal in a real station
series: state the estimator and window, the null model (including the noise
colour), how the false-positive rate is *measured* rather than assumed, how the
threshold is adjusted for the number of frequencies searched, and how you would
demonstrate that the procedure does not fire on a pure-red-noise surrogate. State
the expected false-positive rate at the threshold you choose, and the one number
that would falsify your procedure.
