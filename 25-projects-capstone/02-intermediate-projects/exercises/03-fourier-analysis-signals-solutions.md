# Solutions — 25-02-03 Project: Fourier Analysis of a Geophysical Signal

> Read after attempting. Lesson:
> [03 Fourier Analysis](../03-fourier-analysis-signals.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/fourier_analysis_signals_demo.py`](../code/fourier_analysis_signals_demo.py).

---

## ★1 — Resolution and limits

Duration: $T = N/f_s = 4096\ \mathrm{s}$.

Resolution: $\Delta f = f_s/N = 1.0/4096 = 2.4414\times10^{-4}\ \mathrm{Hz}$.

Nyquist: $f_s/2 = 0.50\ \mathrm{Hz}$; shortest representable period
$2/f_s = 2.0\ \mathrm{s}$.

Longest resolvable period: $1/\Delta f = 4096\ \mathrm{s} = T$ — the record
length *is* the longest period, which is why a period comparable to the record
cannot be estimated reliably.

---

## ★2 — PSD units and the integral

The signal unit is arbitrary (say, signal unit); the PSD's unit is

$$[ \widehat{S} ] = \frac{(\text{signal unit})^{2}}{\mathrm{Hz}}.$$

The PSD is a *density*: it is the variance contributed per unit frequency band. A
single sinusoid contributes $A^{2}/2$ of variance, spread over its line, so

$$\int_0^{f_s/2}\widehat{S}(f)\,\mathrm{d}f = \operatorname{Var}(x),$$

which has unit (signal unit)². A spectrum in *amplitude* units — as a naive FFT
magnitude is — cannot be integrated to a variance, and comparing the two without
stating the convention is the first defect of §9 of the lesson.

---

## ★3 — Peak-bin amplitude

$$A_\text{peak bin} = \sqrt{2\,\widehat{S}\,\Delta f}
= \sqrt{2 \times 331.1041 \times 0.000977}
= \sqrt{0.64686} = 0.80429.$$

Shortfall:

$$\frac{1.00 - 0.80429}{1.00} = 19.6\%,$$

matching the demonstration's $0.8042$. The shortfall is not an error of the
transform: with a Hann window the line's power sits in three bins, so the largest
bin holds roughly two thirds of $A^{2}/2$.

---

## ★4 — Where the rest of the power is

$$A_\text{lobe} = \sqrt{2\,\Delta f \sum_{\text{lobe}}\widehat{S}}
\;\Longrightarrow\;
\sum_{\text{lobe}}\widehat{S} = \frac{A_\text{lobe}^{2}}{2\Delta f}
= \frac{1.0178^{2}}{2 \times 0.000977} = \frac{1.03592}{0.001954}
= 530.1\ \text{unit}^{2}\,\mathrm{Hz^{-1}}.$$

Ratio to the single peak bin:

$$\frac{530.1}{331.1041} = 1.601.$$

The ratio is not 1 because the Hann window's squared amplitude spectrum is a
three-bin-wide lobe: the central bin carries about $1/1.60 = 62\%$ of the line's
power, and the two neighbours carry the rest. The value depends on where the line
falls relative to a bin, which is why the correction cannot be applied as a
constant and the lobe must be *integrated*.

---

## ★5 — Leakage in three currencies, and the resolution cost

| window | sidelobe/peak (power) | amplitude ratio | suppression (dB) | main lobe |
|---|---|---|---|---|
| rectangular | $0.1101$ | $\sqrt{0.1101} = 0.3318$ | $-9.6$ | 1 bin |
| Hann | $0.0008$ | $\sqrt{0.0008} = 0.0283$ | $-30.9$ | 2 bins |

Suppression factor: $0.1101/0.0008 = 138$ in power, $0.3318/0.0283 = 11.7$ in
amplitude.

Main-lobe widths in frequency: rectangular $1 \times \Delta f =
0.000977\ \mathrm{Hz}$; Hann $2 \times \Delta f = 0.001954\ \mathrm{Hz}$.

**Resolution cost.** Any two lines closer than the main-lobe width merge. In
period terms, at 0.05 Hz the rectangular window resolves
$\delta T \approx \Delta f/f^{2} = 0.000977/0.0025 = 0.39\ \mathrm{s}$, while Hann
resolves $0.78\ \mathrm{s}$ — so a Hann spectrum cannot separate periods 20.0 s
and 20.4 s that a rectangular one barely can. The trade is a factor of 2 in
resolution for a factor of 138 in leakage, which is why Hann is the default and
rectangular is reserved for exactly periodic data.

---

## ★6 — The null, checked against theory

White-noise PSD level:

$$\widehat{S}_\text{noise} = \frac{2\sigma^{2}}{f_s} = \frac{2 \times 0.09}{1.0}
= 0.1800\ \text{unit}^{2}\,\mathrm{Hz^{-1}}.$$

Measured-over-predicted threshold ratio:

$$\frac{1.6216}{0.1800} = 9.01.$$

Prediction for the maximum of $n = 512$ independent exponential variables:

$$\frac{t}{m} = -\ln\!\left(1 - 0.95^{1/512}\right)
= -\ln\!\left(1 - e^{\ln 0.95/512}\right)
= -\ln(9.99\times10^{-5}) = 9.21.$$

Agreement to $2\%$ ($9.01$ against $9.21$) — the small deficit is the Hann
window's effective noise bandwidth being slightly narrower than the bin width, so
the noise level recovered from the threshold is
$m = 1.6216/9.21 = 0.1760$ versus the nominal $0.1800$.

**Consequence.** Searching $512$ bins at a per-bin 5% threshold would give a false
positive in $1 - 0.95^{512} \approx 100\%$ of pure-noise records. Calibrating the
*maximum* at the 95th percentile restores the 5% rate and costs a threshold
$9.2$ times the noise level — which is exactly the honest price of a search.

---

## ★★★7 — A detection procedure with a measured false-positive rate

**Estimator and window.** Welch's method: 50%-overlapping segments of length
$N_\text{seg} = 512$ with a Hann window, averaged into a PSD with a stated
effective bandwidth. Averaging is required because a single periodogram bin has
about 100% relative variance.

**Null model.** Red noise, not white. Fit an AR(1) (or a power-law
$S \propto f^{-\alpha}$) to the spectrum away from candidate lines, and use the
*fitted* null. The demonstration's own check (§6) shows that an exponential
distribution per bin is the right shape; the colour sets the mean level as a
function of frequency.

**Measured, not assumed, false-positive rate.** Generate $M \ge 1000$ surrogate
series by the same AR(1) process (or by Fourier-phase randomisation of the real
spectrum, which preserves the observed colour exactly), run the identical
procedure on each, and record the proportion whose maximum exceeds the candidate
threshold. The threshold is then set so that the measured proportion is the
target, typically 0.05.

**Multiplicity.** The threshold applies to the **maximum over all searched
frequencies**, as in §8 of the lesson. Searching $n$ bins inflates a per-bin rate
$p$ to $1-(1-p)^{n}$; with $n = 512$ and $p = 0.05$ that is essentially 1. The
two honest options are (i) calibrate the maximum at 0.05 and accept the $9.2\times$
threshold, or (ii) state the per-bin rate *and* the number of bins searched, and
multiply.

**Falsification test.** Run the procedure on 1000 pure-red-noise surrogates and
report the empirical rate. The single number that falsifies the procedure is the
measured false-positive rate: if it exceeds the target by more than the binomial
sampling error $1/\sqrt{2M}$ (about $2.2\%$ for $M = 10^{3}$), the null model or
the calibration is wrong. A procedure whose rate has never been measured is not a
procedure, it is a threshold.
